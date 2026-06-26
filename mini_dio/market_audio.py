from __future__ import annotations

import csv
import math
import wave
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class WavRenderConfig:
    sample_rate: int = 22050
    seconds_per_frame: float = 0.025
    master_volume: float = 0.45


def _float(value: object) -> float:
    try:
        return float(value or 0.0)
    except Exception:
        return 0.0


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def _read_melody_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def _role_shape(tone_role: str) -> tuple[float, float]:
    if tone_role == "ruheton":
        return 0.35, 0.02
    if tone_role == "trageton":
        return 0.55, 0.04
    if tone_role == "aufhellungston":
        return 0.65, 0.07
    if tone_role == "abdunklungston":
        return 0.58, -0.06
    if tone_role == "spannungston":
        return 0.82, 0.10
    if tone_role == "bruchton":
        return 0.95, -0.12
    return 0.50, 0.00


def _sample_for_frame(row: dict[str, str], sample_index: int, frame_samples: int, sample_rate: int, config: WavRenderConfig) -> float:
    pitch_hz = max(30.0, _float(row.get("pitch_hz")))
    amplitude = _clamp(_float(row.get("amplitude")))
    roughness = _clamp(_float(row.get("roughness")))
    role_gain, detune = _role_shape(str(row.get("tone_role") or ""))
    t = sample_index / sample_rate
    phase = 2.0 * math.pi * pitch_hz * t
    base = math.sin(phase)
    overtone = math.sin((phase * 2.0) + (roughness * math.pi)) * 0.18
    detuned = math.sin(2.0 * math.pi * pitch_hz * (1.0 + detune) * t) * (0.12 + (roughness * 0.12))

    if frame_samples <= 1:
        envelope = 1.0
    else:
        position = sample_index / (frame_samples - 1)
        attack = min(1.0, position / 0.18)
        release = min(1.0, (1.0 - position) / 0.22)
        envelope = max(0.0, min(attack, release))

    signal = (base + overtone + detuned) * amplitude * role_gain * envelope * config.master_volume
    return max(-1.0, min(1.0, signal))


def render_melody_csv_to_wav(
    melody_csv: Path,
    wav_path: Path,
    config: WavRenderConfig | None = None,
    max_frames: int | None = None,
) -> dict[str, float | int | str]:
    config = config or WavRenderConfig()
    rows = _read_melody_rows(melody_csv)
    if max_frames is not None and max_frames > 0:
        rows = rows[:max_frames]
    wav_path.parent.mkdir(parents=True, exist_ok=True)
    frame_samples = max(1, int(config.sample_rate * config.seconds_per_frame))
    total_samples = len(rows) * frame_samples
    peak = 0.0
    with wave.open(str(wav_path), "wb") as handle:
        handle.setnchannels(1)
        handle.setsampwidth(2)
        handle.setframerate(config.sample_rate)
        for row in rows:
            for sample_index in range(frame_samples):
                sample = _sample_for_frame(row, sample_index, frame_samples, config.sample_rate, config)
                peak = max(peak, abs(sample))
                handle.writeframesraw(int(sample * 32767).to_bytes(2, byteorder="little", signed=True))
    duration_seconds = total_samples / max(1, config.sample_rate)
    return {
        "melody_csv": str(melody_csv),
        "wav_path": str(wav_path),
        "frames": len(rows),
        "sample_rate": config.sample_rate,
        "seconds_per_frame": config.seconds_per_frame,
        "duration_seconds": duration_seconds,
        "peak": peak,
    }
