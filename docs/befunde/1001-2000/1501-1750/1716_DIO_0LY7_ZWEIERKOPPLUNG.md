# 1716 - Synthetische Zweierkopplung der Oeffnungs-Vorform

Stand: 2026-07-07 23:29:14

## Zweck

Diese Diagnose prueft, ob die Oeffnungs-Vorform bei synthetischen Zweierkopplungen getragen bleibt oder bereits vor der vollen Dreierlast kippt.
Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.

## Hierarchie

1. Grundfrage: Welche gekoppelte Stoerung bricht `dio_0ly7`?
2. Unterpruefung: Range+Hoeren, Range+Spannung und Hoeren+Spannung getrennt lesen.
3. Folgeschritt: Gegen Einzelachsen und volle gekoppelte Last verdichten.

## Aggregat

| Familie | Welten mit Treffer | Vorkommen | Vor Hoeren | Hit Hoeren | Delta Hoeren | Vor Spannung | Hit Spannung | Delta Spannung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ALLE | 3 | 95 | 0.0357 | 0.0338 | -0.0018 | 0.0420 | 0.0418 | -0.0002 |
| dio_0ly7 | 3 | 95 | 0.0357 | 0.0338 | -0.0018 | 0.0420 | 0.0418 | -0.0002 |

## Einzelwelten

| Welt | Familie | Vorkommen | Vor Hoeren | Hit Hoeren | Delta Hoeren | Vor Spannung | Hit Spannung | Delta Spannung |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| SYN_PAIR_RANGE_HEARING | dio_0ly7 | 58 | 0.0236 | 0.0314 | 0.0079 | 0.0327 | 0.0399 | 0.0072 |
| SYN_PAIR_RANGE_TENSION | dio_0ly7 | 27 | 0.0287 | 0.0313 | 0.0027 | 0.0362 | 0.0400 | 0.0038 |
| SYN_PAIR_HEARING_TENSION | dio_0ly7 | 10 | 0.0547 | 0.0387 | -0.0161 | 0.0571 | 0.0455 | -0.0117 |

## Lesung

Wenn Range+Hoeren oder Range+Spannung kippen, aber Hoeren+Spannung getragen bleibt, spricht das fuer Range als kritischen Kopplungsanteil.
Die Form wird dann nicht durch jede Zweierlast gebrochen, sondern durch bestimmte Kopplungsqualitaeten.
