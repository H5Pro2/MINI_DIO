# 1829 - Daempfung Real Null Erweiterte Welten

Stand: 2026-07-08 22:18:24

## Grundfrage

Was passiert, wenn Rueckfuehrungsdaempfung nicht nur nachtraeglich gelesen wird, sondern direkt im isolierten MINI_DIO-Lauf wirkt?

## Aufbau

- jeder Faktor laeuft mit frischer Memory
- Standardfaktor `1.0` bleibt Referenz
- die Daempfung betrifft nur `mcm_rekopplung_quality` im passiven MCM-Feldeffekt
- keine Handlung, kein Gate, keine Entry-Logik wird daraus gebaut

## Gesamtbefund

- Faktoren: `1.00, 0.50, 0.30`
- mittlere Rekopplung bei staerkster Daempfung: `0.209929`
- mittlere Unique-Syntax bei staerkster Daempfung: `305.67`
- mittlere Episodenfamilien bei staerkster Daempfung: `304.00`

## Vergleich

| Welt | Faktor | Rekopplung | Carry | Strain | Adaptive Rekopplung | Sinneskopplung | Symbole | Episodenfamilien | dominante Feldklasse | Delta Rekopplung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| NULL_RANDOM_2400 | 1.00 | 0.7123 | 0.5437 | 0.1521 | 0.7174 | 0.8554 | 221 | 221 | `stabil` | 0.0000 |
| NULL_RANDOM_2400 | 0.50 | 0.3562 | 0.5437 | 0.1521 | 0.6565 | 0.8554 | 221 | 221 | `stabil` | -0.3562 |
| NULL_RANDOM_2400 | 0.30 | 0.2137 | 0.5437 | 0.1521 | 0.6403 | 0.8554 | 221 | 221 | `stabil` | -0.4986 |
| NULL_SHUFFLE_2400 | 1.00 | 0.7028 | 0.5346 | 0.1653 | 0.7078 | 0.8444 | 224 | 222 | `stabil` | 0.0000 |
| NULL_SHUFFLE_2400 | 0.50 | 0.3514 | 0.5346 | 0.1653 | 0.6353 | 0.8444 | 224 | 222 | `stabil` | -0.3514 |
| NULL_SHUFFLE_2400 | 0.30 | 0.2108 | 0.5346 | 0.1653 | 0.7239 | 0.8444 | 224 | 222 | `stabil` | -0.4920 |
| SOL_EXPANSION_2023_2K | 1.00 | 0.6963 | 0.5211 | 0.1662 | 0.7363 | 0.8386 | 339 | 336 | `stabil` | 0.0000 |
| SOL_EXPANSION_2023_2K | 0.50 | 0.3482 | 0.5211 | 0.1662 | 0.7332 | 0.8386 | 339 | 336 | `stabil` | -0.3482 |
| SOL_EXPANSION_2023_2K | 0.30 | 0.2089 | 0.5211 | 0.1662 | 0.7320 | 0.8386 | 339 | 336 | `stabil` | -0.4874 |
| SOL_NEG_STRESS_2023_2K | 1.00 | 0.6962 | 0.5204 | 0.1661 | 0.7350 | 0.8393 | 357 | 355 | `stabil` | 0.0000 |
| SOL_NEG_STRESS_2023_2K | 0.50 | 0.3481 | 0.5204 | 0.1661 | 0.7230 | 0.8393 | 357 | 355 | `stabil` | -0.3481 |
| SOL_NEG_STRESS_2023_2K | 0.30 | 0.2089 | 0.5204 | 0.1661 | 0.7266 | 0.8393 | 357 | 355 | `stabil` | -0.4873 |
| SOL_QUIET_2025_2K | 1.00 | 0.6951 | 0.5195 | 0.1666 | 0.7357 | 0.8391 | 337 | 334 | `stabil` | 0.0000 |
| SOL_QUIET_2025_2K | 0.50 | 0.3475 | 0.5195 | 0.1666 | 0.7347 | 0.8391 | 337 | 334 | `stabil` | -0.3475 |
| SOL_QUIET_2025_2K | 0.30 | 0.2085 | 0.5195 | 0.1666 | 0.7342 | 0.8391 | 337 | 334 | `stabil` | -0.4865 |
| SOL_SIDEWAYS_2026_2K | 1.00 | 0.6959 | 0.5187 | 0.1648 | 0.7349 | 0.8426 | 356 | 356 | `stabil` | 0.0000 |
| SOL_SIDEWAYS_2026_2K | 0.50 | 0.3480 | 0.5187 | 0.1648 | 0.7201 | 0.8426 | 356 | 356 | `stabil` | -0.3480 |
| SOL_SIDEWAYS_2026_2K | 0.30 | 0.2088 | 0.5187 | 0.1648 | 0.7367 | 0.8426 | 356 | 356 | `stabil` | -0.4871 |

## Lesung

Dieser Test ist haerter als die reine Auswertungsdaempfung, weil die gedaempfte Rekopplung bereits in Klassifikation, Episodenbildung und passiver Rekopplungslesung mitlaeuft.

Belastbar ist hier zuerst die Richtung der Reaktion: Bleiben die Welten geordnet, werden sie diffuser, steigt Strain, oder veraendert sich nur die Rekopplungsnaehe?

Die erweiterte Weltgruppe bestaetigt die Grundrichtung aus 1827:

- alle geprueften Welten bleiben in der dominanten Feldklasse `stabil`,
- die statische Rekopplung sinkt mit dem Faktor erwartbar,
- reale Welten bilden mehr Symbole und Episodenfamilien als Nullwelten,
- reale Welten halten die adaptive Rekopplung meist hoeher,
- Nullwelten bleiben deutlich schmaler, kollabieren aber nicht chaotisch.

Damit reicht die dominante Feldklasse erneut nicht aus. Die relevante Trennung liegt in Bedeutungsbreite, adaptiver Rekopplung und Rollenvarianz.

## Grenze

Auch dieser Test ist noch kein Beweis fuer eine vollstaendige Feldtheorie. Er zeigt aber, ob eine gezielte Veraenderung im Lauf eine nachvollziehbare Feldantwort erzeugt.
