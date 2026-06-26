from __future__ import annotations

import csv
import hashlib
import math
from dataclasses import dataclass
from pathlib import Path


NOTE_NAMES = ("C", "D", "E", "G", "A")


@dataclass(frozen=True)
class MelodyConfig:
    min_hz: float = 110.0
    max_hz: float = 1760.0
    baseline_alpha: float = 0.04
    phrase_size: int = 4


@dataclass(frozen=True)
class Candle:
    timestamp_ms: str
    symbol: str
    timeframe: str
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass(frozen=True)
class MelodyFrame:
    index: int
    timestamp_ms: str
    symbol: str
    timeframe: str
    close: float
    direction: float
    energy: float
    relative_energy: float
    pitch_hz: float
    amplitude: float
    roughness: float
    note: str
    octave: int
    tone_role: str
    phrase_symbol: str
    speech_token: str


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _hash_symbol(prefix: str, text: str, length: int = 7) -> str:
    digest = hashlib.blake2s(text.encode("utf-8"), digest_size=8).hexdigest()
    return f"{prefix}_{digest[:length]}"


def read_candles(path: Path) -> list[Candle]:
    rows: list[Candle] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            rows.append(
                Candle(
                    timestamp_ms=str(row.get("timestamp_ms") or row.get("timestamp") or ""),
                    symbol=str(row.get("symbol") or ""),
                    timeframe=str(row.get("timeframe") or ""),
                    open=_float(row.get("open")),
                    high=_float(row.get("high")),
                    low=_float(row.get("low")),
                    close=_float(row.get("close")),
                    volume=_float(row.get("volume")),
                )
            )
    return rows


def _energy(candle: Candle, previous: Candle | None, previous_volume: float) -> tuple[float, float]:
    price_ref = max(abs(candle.close), 1e-9)
    body = abs(candle.close - candle.open) / price_ref
    candle_range = max(0.0, candle.high - candle.low) / price_ref
    if previous and previous.close:
        move = abs(candle.close - previous.close) / max(abs(previous.close), 1e-9)
    else:
        move = body
    if previous_volume:
        volume_shift = abs(math.log(max(candle.volume, 1e-9) / max(previous_volume, 1e-9)))
    else:
        volume_shift = 0.0
    energy = (move * 0.42) + (candle_range * 0.34) + (body * 0.18) + (min(volume_shift, 4.0) * 0.015)
    direction = (candle.close - candle.open) / price_ref
    return energy, direction


def _note_from_pitch(pitch_hz: float, config: MelodyConfig) -> tuple[str, int]:
    span = max(1e-9, config.max_hz - config.min_hz)
    normalized = _clamp((pitch_hz - config.min_hz) / span)
    note_index = min(len(NOTE_NAMES) - 1, int(normalized * len(NOTE_NAMES)))
    octave = 2 + min(5, int(normalized * 6))
    return NOTE_NAMES[note_index], octave


def _tone_role(relative_energy: float, direction: float, roughness: float) -> str:
    if roughness >= 0.70 and relative_energy >= 1.30:
        return "bruchton"
    if relative_energy >= 1.55:
        return "spannungston"
    if relative_energy <= 0.72 and roughness <= 0.28:
        return "ruheton"
    if direction > 0.0008:
        return "aufhellungston"
    if direction < -0.0008:
        return "abdunklungston"
    return "trageton"


def _speech_token(tone_role: str, note: str, octave: int, relative_energy: float) -> str:
    band = "leise" if relative_energy < 0.85 else "mittel" if relative_energy < 1.25 else "laut"
    return _hash_symbol("dio_snd", f"{tone_role}|{note}|{octave}|{band}", length=6)


def build_market_melody(candles: list[Candle], config: MelodyConfig | None = None) -> list[MelodyFrame]:
    config = config or MelodyConfig()
    if not candles:
        return []
    frames: list[MelodyFrame] = []
    baseline = 0.0
    previous: Candle | None = None
    previous_energy = 0.0
    phrase_roles: list[str] = []
    for index, candle in enumerate(candles):
        energy, direction = _energy(candle, previous, previous.volume if previous else 0.0)
        if index == 0:
            baseline = max(energy, 1e-9)
        else:
            baseline = (baseline * (1.0 - config.baseline_alpha)) + (energy * config.baseline_alpha)
        relative_energy = energy / max(baseline, 1e-9)
        compressed = _clamp(math.log1p(relative_energy) / math.log(4.0))
        pitch_hz = config.min_hz + ((config.max_hz - config.min_hz) * compressed)
        amplitude = _clamp(math.sqrt(max(0.0, relative_energy)) / 1.65)
        roughness = _clamp(abs(energy - previous_energy) / max(baseline, 1e-9))
        note, octave = _note_from_pitch(pitch_hz, config)
        tone_role = _tone_role(relative_energy, direction, roughness)
        phrase_roles.append(tone_role)
        if len(phrase_roles) > config.phrase_size:
            phrase_roles.pop(0)
        phrase_symbol = _hash_symbol("dio_mel", "|".join(phrase_roles), length=8)
        speech_token = _speech_token(tone_role, note, octave, relative_energy)
        frames.append(
            MelodyFrame(
                index=index,
                timestamp_ms=candle.timestamp_ms,
                symbol=candle.symbol,
                timeframe=candle.timeframe,
                close=candle.close,
                direction=direction,
                energy=energy,
                relative_energy=relative_energy,
                pitch_hz=pitch_hz,
                amplitude=amplitude,
                roughness=roughness,
                note=note,
                octave=octave,
                tone_role=tone_role,
                phrase_symbol=phrase_symbol,
                speech_token=speech_token,
            )
        )
        previous = candle
        previous_energy = energy
    return frames


def write_melody_csv(path: Path, frames: list[MelodyFrame]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(MelodyFrame.__dataclass_fields__.keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for frame in frames:
            writer.writerow({field: getattr(frame, field) for field in fieldnames})
