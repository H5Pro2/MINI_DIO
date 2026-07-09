# PAXG 2024: Kontrolle für rekoppelnde Rollenbreite

Stand: 2026-07-08

## Grundfrage

Nach der 2025-Sequenzmatrix war PAXG der deutlichste Fall für `verteilt_rekoppelnd`. Die offene Frage war:

```text
Ist rekoppelnde Rollenbreite nur ein PAXG-2025-Befund,
oder erscheint sie auch in PAXG 2024?
```

## Unterprüfung

PAXG 2024 wurde mit derselben lokalen Vier-Fenster-Logik geprüft:

```text
5000-6000 -> 6000-7000
6000-7000 -> 7000-8000
7000-8000 -> 8000-9000
8000-9000 -> 9000-10000
```

Reports:

```text
reports/paxg_2024_lokale_realsleepreal_sequenz.md
reports/paxg_2024_lokale_realsleepreal_sequenz.csv
reports/paxg_2024_sequence_rawworld_contrast.md
reports/paxg_2024_sequence_rawworld_contrast_groups.csv
```

## Sequenz

| Anschluss | Achsenklasse | Rollen | Kombinationen | Rekopplung | Nachhall |
|---|---|---:|---:|---:|---:|
| 5000-6000 -> 6000-7000 | mittlere_uebergangsphase | 3 | 3 | 0.7024 | 0.3336 |
| 6000-7000 -> 7000-8000 | mittlere_uebergangsphase | 3 | 3 | 0.6969 | 0.2992 |
| 7000-8000 -> 8000-9000 | verteilt_rekoppelnd | 5 | 10 | 0.7070 | 0.3770 |
| 8000-9000 -> 9000-10000 | mittlere_uebergangsphase | 3 | 3 | 0.7087 | 0.3641 |

## Klassenmittel

| Klasse | n | Rollen | Kombis | Rekopplung | Adaptiv | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mittlere_uebergangsphase | 3 | 3.00 | 3.00 | 0.7027 | 0.7142 | 0.3323 | 1.1525 | 1.0663 | -0.0862 |
| verteilt_rekoppelnd | 1 | 5.00 | 10.00 | 0.7070 | 0.7422 | 0.3770 | 0.9458 | 1.0352 | 0.0893 |

## Befund

PAXG 2024 bildet ebenfalls `verteilt_rekoppelnd`, aber nur in einem der vier lokalen Anschlüsse. Damit wird die 2025-Lesung gestützt und gleichzeitig präzisiert:

```text
Rekoppelnde Rollenbreite ist PAXG-nah sichtbar,
aber sie ist phasenabhängig und nicht dauerhaft.
```

Der rekoppelnde Abschnitt liegt wieder bei:

- ruhigerer Basis-Weltenergie,
- höherer Rekopplung,
- stärkerem Nachhall,
- breiterer Rollenbildung.

## Deutung

Der Befund stützt die Trennung:

```text
verteilt_offen      = breite Rollenöffnung, weniger stark rückgebunden
verteilt_rekoppelnd = breite Rollenbildung, stärker getragen und nachhallender
```

PAXG zeigt diese rekoppelnde Breite auch 2024, aber nicht durchgehend. Das spricht gegen eine starre Assetetikette und für eine lokale Feldphase innerhalb einer assettypischen Rekopplungsneigung.

## Grenze

Der Befund ist passiv und phasenbezogen. Er sagt nicht, dass PAXG immer rekoppelnd ist. Er zeigt nur:

```text
PAXG kann rekoppelnde Rollenbreite in mehreren Jahren ausbilden.
```

## Folgeschritt

Als nächstes sollte die gemeinsame Lesung aus 2024 und 2025 als Arbeitsdefinition verdichtet werden:

```text
Was ist rekoppelnde Rollenbreite im MCM-Feld?
```
