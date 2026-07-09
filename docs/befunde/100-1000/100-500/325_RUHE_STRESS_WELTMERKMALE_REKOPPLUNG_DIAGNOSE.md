# Lokale Weltmerkmale und Rekopplung - Diagnose

Stand: 2026-06-19 22:11:40

## Zweck

Diese Diagnose legt Rohweltmerkmale neben lokale Rekopplungsrollen.
Sie prueft, welche Weltmerkmale den Uebergang von aktiv-rekoppelnd zu bindend begleiten.

Hierarchie der Pruefung:

1. Grundfrage: Welche Weltmerkmale erzeugen oder begleiten Rekopplungsbindung?
2. Unterpruefung: Drift, Range, Volumenrhythmus, Richtungswechsel und Verdichtung gegen Feldlast/Memory/Rekopplung legen.
3. Folgeschritt: Bewerten, ob Bindung eher aus Weltstruktur, Nachhall oder Feldzustand entsteht.

## Einzelwerte

| Welt | Gruppe | Rolle | Kontrast | Feldlast | Memorylast | Rekopplung | Verdichtung | Drift | avg Range | p95 Range | Richtungswechsel | Persistenz |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SIDEWAYS_2024 | sonstige | reiz_aktiv_rekoppelnd | -0.6083 | 0.0050 | 0.0111 | 0.642210 | 3.1420 | -0.0212 | 0.002946 | 0.006353 | 0.4770 | 0.5230 |
| SIDEWAYS_2026 | sonstige | nachhall_rekoppelnd | -0.5999 | 0.0030 | 0.0070 | 0.643330 | 7.7426 | -0.0437 | 0.006917 | 0.016076 | 0.4729 | 0.5271 |
| NEG_STRESS_2023 | stress | reiz_aktiv_rekoppelnd | -0.6145 | 0.0060 | 0.0131 | 0.644143 | 3.4169 | -0.0293 | 0.003167 | 0.006923 | 0.3958 | 0.6042 |
| NEG_STRESS_2024 | stress | reiz_aktiv_rekoppelnd | -0.5954 | 0.0060 | 0.0131 | 0.641425 | 3.3703 | -0.0528 | 0.003240 | 0.006465 | 0.4850 | 0.5150 |

## Gruppenmittel

### Stress

- Kontrast Bindung-Aktiv: `-0.6049`
- Feldlast: `0.0060`
- Memorylast: `0.0131`
- Weltverdichtung: `3.3936`
- Richtungswechsel: `0.4404`

## Staerkste Bindung

- `NEG_STRESS_2024`: Kontrast `-0.5954`, Verdichtung `3.3703`, Range `0.003240`, Richtungswechsel `0.4850`
- `SIDEWAYS_2026`: Kontrast `-0.5999`, Verdichtung `7.7426`, Range `0.006917`, Richtungswechsel `0.4729`
- `SIDEWAYS_2024`: Kontrast `-0.6083`, Verdichtung `3.1420`, Range `0.002946`, Richtungswechsel `0.4770`
- `NEG_STRESS_2023`: Kontrast `-0.6145`, Verdichtung `3.4169`, Range `0.003167`, Richtungswechsel `0.3958`

## Staerkste Rohweltverdichtung

- `SIDEWAYS_2026`: Verdichtung `7.7426`, Rolle `nachhall_rekoppelnd`, Kontrast `-0.5999`
- `NEG_STRESS_2023`: Verdichtung `3.4169`, Rolle `reiz_aktiv_rekoppelnd`, Kontrast `-0.6145`
- `NEG_STRESS_2024`: Verdichtung `3.3703`, Rolle `reiz_aktiv_rekoppelnd`, Kontrast `-0.5954`
- `SIDEWAYS_2024`: Verdichtung `3.1420`, Rolle `reiz_aktiv_rekoppelnd`, Kontrast `-0.6083`

## Befund

Diese Diagnose ist noch keine Erklaerung, sondern eine Kopplungskarte.
Sie zeigt, ob lokale Bindung mit Rohweltmerkmalen zusammenfaellt oder ob Feldzustand und Memory staerker erklaeren.

## Zusatzbefund

Der Vergleich der gleich langen Ruhe-/Stresswelten zeigt keine einfache Gleichung `Stress = Rand`.
Die Unterschiede liegen feiner:

- `NEG_STRESS_2023` hat weniger Richtungswechsel (`0.3958`), hoehere Persistenz (`0.6042`) und die hoechste Rekopplung (`0.644143`).
- `NEG_STRESS_2024` hat staerkeren negativen Drift (`-0.0528`), mehr Richtungswechsel (`0.4850`) und niedrigere Rekopplung (`0.641425`).
- In der Topologiepruefung wurde `NEG_STRESS_2023` dadurch zentrumsnaeher gelesen, waehrend `NEG_STRESS_2024` offener/variantenreicher wurde.
- `SIDEWAYS_2026` zeigt hohe Weltverdichtung (`7.7426`), aber niedrige Feld- und Memorylast; das spricht fuer Verdichtung ohne Kollaps, nicht automatisch fuer Stress.

Damit liegt der relevante Unterschied nicht allein in Lautstaerke oder Range.
Wichtiger scheint die Kopplung aus Richtungswechsel, Drift, Persistenz und Feldrekopplung zu sein.
MINI_DIO liest also nicht nur "wie stark" eine Welt ist, sondern wie gut die Weltspannung wieder in eine tragende Feldlage zurueckgefuehrt werden kann.

## Wie es weitergeht

Als naechstes sollte diese Differenz lokal auf Episodenebene gelesen werden:
Welche Abschnitte in `NEG_STRESS_2024` erzeugen offene Variante, und welche Abschnitte in `NEG_STRESS_2023` bleiben zentrumsnah rekoppelnd?
