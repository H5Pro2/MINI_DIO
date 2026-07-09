# 1823 - Direkter Lauf-Stresstest: Rueckfuehrungsdaempfung

Stand: 2026-07-08 21:33:14

## Grundfrage

Was passiert, wenn Rueckfuehrungsdaempfung nicht nur nachtraeglich gelesen wird, sondern direkt im isolierten MINI_DIO-Lauf wirkt?

## Aufbau

- jeder Faktor laeuft mit frischer Memory
- Standardfaktor `1.0` bleibt Referenz
- die Daempfung betrifft nur `mcm_rekopplung_quality` im passiven MCM-Feldeffekt
- keine Handlung, kein Gate, keine Entry-Logik wird daraus gebaut

## Gesamtbefund

- Faktoren: `1.00, 0.75, 0.50`
- mittlere Rekopplung bei staerkster Daempfung: `0.357342`
- mittlere Unique-Syntax bei staerkster Daempfung: `177.00`
- mittlere Episodenfamilien bei staerkster Daempfung: `176.00`

## Vergleich

| Welt | Faktor | Rekopplung | Carry | Strain | Adaptive Rekopplung | Sinneskopplung | Symbole | Episodenfamilien | dominante Feldklasse | Delta Rekopplung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| noisy_drift | 1.00 | 0.7539 | 0.6082 | 0.1179 | 0.7539 | 0.9164 | 10 | 10 | `stabil` | 0.0000 |
| noisy_drift | 0.75 | 0.5654 | 0.6082 | 0.1179 | 0.5654 | 0.9164 | 10 | 10 | `stabil` | -0.1885 |
| noisy_drift | 0.50 | 0.3770 | 0.6082 | 0.1179 | 0.3770 | 0.9164 | 10 | 10 | `stabil` | -0.3770 |
| null_random | 1.00 | 0.7123 | 0.5437 | 0.1521 | 0.7174 | 0.8554 | 221 | 221 | `stabil` | 0.0000 |
| null_random | 0.75 | 0.5342 | 0.5437 | 0.1521 | 0.6990 | 0.8554 | 221 | 221 | `stabil` | -0.1781 |
| null_random | 0.50 | 0.3562 | 0.5437 | 0.1521 | 0.6565 | 0.8554 | 221 | 221 | `stabil` | -0.3562 |
| null_shuffle | 1.00 | 0.7028 | 0.5346 | 0.1653 | 0.7078 | 0.8444 | 224 | 222 | `stabil` | 0.0000 |
| null_shuffle | 0.75 | 0.5271 | 0.5346 | 0.1653 | 0.5578 | 0.8444 | 224 | 222 | `stabil` | -0.1757 |
| null_shuffle | 0.50 | 0.3514 | 0.5346 | 0.1653 | 0.6353 | 0.8444 | 224 | 222 | `stabil` | -0.3514 |
| smooth_control | 1.00 | 0.6897 | 0.5026 | 0.1636 | 0.7292 | 0.8409 | 253 | 251 | `stabil` | 0.0000 |
| smooth_control | 0.75 | 0.5173 | 0.5026 | 0.1636 | 0.7299 | 0.8409 | 253 | 251 | `stabil` | -0.1724 |
| smooth_control | 0.50 | 0.3448 | 0.5026 | 0.1636 | 0.7272 | 0.8409 | 253 | 251 | `stabil` | -0.3448 |

## Lesung

Dieser Test ist haerter als die reine Auswertungsdaempfung, weil die gedaempfte Rekopplung bereits in Klassifikation, Episodenbildung und passiver Rekopplungslesung mitlaeuft.

Belastbar ist hier zuerst die Richtung der Reaktion: Bleiben die Welten geordnet, werden sie diffuser, steigt Strain, oder veraendert sich nur die Rekopplungsnaehe?

Der erste direkte Befund ist klar begrenzt:

- die statische Rekopplung sinkt proportional zur Daempfung,
- Carry, Strain und Sinneskopplung bleiben in diesem Test stabil,
- die dominante Feldklasse bleibt in allen vier Welten `stabil`,
- die adaptive Rekopplung faellt nicht ueberall gleich stark mit.

Damit wirkt die Rueckfuehrungsdaempfung im direkten Lauf zuerst als Rekopplungsnaehe-Veraenderung, nicht als sofortiger Topologiebruch. Besonders wichtig ist: Die adaptive Rekopplung kann einen Teil der Daempfung abfedern. Das spricht fuer eine passive Kompensationslesung im Feld, muss aber mit laengeren Weltfenstern weiter geprueft werden.

## Grenze

Auch dieser Test ist noch kein Beweis fuer eine vollstaendige Feldtheorie. Er zeigt aber, ob eine gezielte Veraenderung im Lauf eine nachvollziehbare Feldantwort erzeugt.
