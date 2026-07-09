# 1466 - Melodie-Gleichlage Reproduktion

## Zweck

Diese Pruefung reproduziert den Gleichlagenpunkt aus `1463`.

Die konkrete Frage war:

Bleibt die Gleichlage zwischen `dio_0ein` und `dio_1fll` bei gleicher Welt und frischem Speicher stabil, oder driftet sie bei Wiederholung?

## Aufbau

Verwendet wurde dieselbe Welt:

- Datei: `data/synthetic_1463_melody_block_frame_bs13_narrow112_amp_driftctrl_1200_5m.csv`
- `block_size`: `13`
- Amplitude: `0.00112`
- Richtungswechsel: `455`
- Modus: `world_relative`
- Speicher: pro Reproduktion frisch gestartet
- Wiederholungen: `5`

## Ergebnis

| Lauf | `dio_0ein` | `dio_1fll` | Differenz | Dominanz | Symbole | stabil | unruhig | Rekopplung | Nachhall |
|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 1 | 173 | 173 | 0 | gleich | 51 | 1140 | 54 | 0.732461 | 0.570924 |
| 2 | 173 | 173 | 0 | gleich | 51 | 1140 | 54 | 0.732461 | 0.570924 |
| 3 | 173 | 173 | 0 | gleich | 51 | 1140 | 54 | 0.732461 | 0.570924 |
| 4 | 173 | 173 | 0 | gleich | 51 | 1140 | 54 | 0.732461 | 0.570924 |
| 5 | 173 | 173 | 0 | gleich | 51 | 1140 | 54 | 0.732461 | 0.570924 |

## Befund

Die Gleichlage ist unter identischer Welt und frischem Speicher reproduzierbar.

Es zeigt sich keine Drift zwischen `dio_0ein` und `dio_1fll`.

Auch die Begleitwerte bleiben identisch:

- Symbolzahl,
- stabile Feldwirkung,
- tragende Unruhe,
- Rekopplung,
- Nachhall,
- Fokus-/Beobachtungston.

## Lesung

Dieser Punkt wirkt nicht wie zufaellige Streuung.

Innerhalb dieser kontrollierten Melodiewelt bildet MINI_DIO einen stabilen Gleichlagenpunkt zwischen zwei Bedeutungsnachbarn.

Fachlich ist das kein Beweis fuer eine allgemeine MCM-Gesetzmaessigkeit. Es ist aber ein starker reproduzierbarer Befund innerhalb dieser synthetischen Weltfamilie.

## Schlussfolgerung

Der Kippbereich enthaelt mindestens einen stabil reproduzierbaren Gleichlagenpunkt:

`block_size 13`, Amplitude `0.00112`

Damit wird der Begriff `Schwellenband` weiter geschaerft:

Es gibt nicht nur eine Zone unscharfer Drift, sondern innerhalb der Zone kann ein stabiler Balancepunkt entstehen.

## Grenze

Diese Reproduktion prueft nur identische Weltbedingungen.

Offen bleibt, ob kleine Stoerungen um `0.00112` herum die Gleichlage erhalten, verschieben oder aufloesen.
