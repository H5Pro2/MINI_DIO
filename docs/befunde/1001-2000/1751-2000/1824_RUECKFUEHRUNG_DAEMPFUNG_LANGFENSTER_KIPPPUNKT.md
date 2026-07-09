# 1824 - Rueckfuehrungsdaempfung Langfenster-Kipppunkt

Stand: 2026-07-08 21:42:40

## Grundfrage

Was passiert, wenn Rueckfuehrungsdaempfung nicht nur nachtraeglich gelesen wird, sondern direkt im isolierten MINI_DIO-Lauf wirkt?

## Aufbau

- jeder Faktor laeuft mit frischer Memory
- Standardfaktor `1.0` bleibt Referenz
- die Daempfung betrifft nur `mcm_rekopplung_quality` im passiven MCM-Feldeffekt
- keine Handlung, kein Gate, keine Entry-Logik wird daraus gebaut

## Gesamtbefund

- Faktoren: `1.00, 0.90, 0.80, 0.70`
- mittlere Rekopplung bei staerkster Daempfung: `0.498490`
- mittlere Unique-Syntax bei staerkster Daempfung: `598.50`
- mittlere Episodenfamilien bei staerkster Daempfung: `595.00`

## Vergleich

| Welt | Faktor | Rekopplung | Carry | Strain | Adaptive Rekopplung | Sinneskopplung | Symbole | Episodenfamilien | dominante Feldklasse | Delta Rekopplung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| BTC_2025_5M_10K | 1.00 | 0.7075 | 0.5529 | 0.1698 | 0.7428 | 0.8424 | 677 | 674 | `stabil` | 0.0000 |
| BTC_2025_5M_10K | 0.90 | 0.6367 | 0.5529 | 0.1698 | 0.7423 | 0.8424 | 677 | 674 | `stabil` | -0.0707 |
| BTC_2025_5M_10K | 0.80 | 0.5660 | 0.5529 | 0.1698 | 0.7419 | 0.8424 | 677 | 674 | `stabil` | -0.1415 |
| BTC_2025_5M_10K | 0.70 | 0.4952 | 0.5529 | 0.1698 | 0.7414 | 0.8424 | 677 | 674 | `stabil` | -0.2122 |
| PAXG_2024_5M_10K | 1.00 | 0.7168 | 0.5564 | 0.1668 | 0.7520 | 0.8517 | 520 | 516 | `stabil` | 0.0000 |
| PAXG_2024_5M_10K | 0.90 | 0.6451 | 0.5564 | 0.1668 | 0.7510 | 0.8517 | 520 | 516 | `stabil` | -0.0717 |
| PAXG_2024_5M_10K | 0.80 | 0.5734 | 0.5564 | 0.1668 | 0.7500 | 0.8517 | 520 | 516 | `stabil` | -0.1434 |
| PAXG_2024_5M_10K | 0.70 | 0.5017 | 0.5564 | 0.1668 | 0.7490 | 0.8517 | 520 | 516 | `stabil` | -0.2150 |

## Lesung

Dieser Test ist haerter als die reine Auswertungsdaempfung, weil die gedaempfte Rekopplung bereits in Klassifikation, Episodenbildung und passiver Rekopplungslesung mitlaeuft.

Belastbar ist hier zuerst die Richtung der Reaktion: Bleiben die Welten geordnet, werden sie diffuser, steigt Strain, oder veraendert sich nur die Rekopplungsnaehe?

Im geprueften Bereich `1.0` bis `0.7` entsteht kein harter Kipppunkt. BTC und PAXG reagieren fast parallel:

- die statische Rekopplung sinkt graduell,
- Carry, Strain und Sinneskopplung bleiben stabil,
- die dominante Feldklasse bleibt `stabil`,
- Symbol- und Episodenfamilien bleiben gleich breit,
- adaptive Rekopplung bleibt hoch und puffert die statische Daempfung stark ab.

Damit wirkt die Daempfung in diesen Langfenstern nicht wie ein Topologiebruch, sondern wie eine veraenderte Rueckfuehrungsnaehe innerhalb einer weiterhin getragenen Feldordnung.

## Grenze

Auch dieser Test ist noch kein Beweis fuer eine vollstaendige Feldtheorie. Er zeigt aber, ob eine gezielte Veraenderung im Lauf eine nachvollziehbare Feldantwort erzeugt.
