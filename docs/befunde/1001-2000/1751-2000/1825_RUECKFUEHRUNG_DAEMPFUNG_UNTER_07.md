# 1825 - Rueckfuehrungsdaempfung unter 0.7

Stand: 2026-07-08 21:55:01

## Grundfrage

Was passiert, wenn Rueckfuehrungsdaempfung nicht nur nachtraeglich gelesen wird, sondern direkt im isolierten MINI_DIO-Lauf wirkt?

## Aufbau

- jeder Faktor laeuft mit frischer Memory
- Standardfaktor `1.0` bleibt Referenz
- die Daempfung betrifft nur `mcm_rekopplung_quality` im passiven MCM-Feldeffekt
- keine Handlung, kein Gate, keine Entry-Logik wird daraus gebaut

## Gesamtbefund

- Faktoren: `1.00, 0.70, 0.65, 0.60, 0.55, 0.50`
- mittlere Rekopplung bei staerkster Daempfung: `0.356064`
- mittlere Unique-Syntax bei staerkster Daempfung: `598.50`
- mittlere Episodenfamilien bei staerkster Daempfung: `595.00`

## Vergleich

| Welt | Faktor | Rekopplung | Carry | Strain | Adaptive Rekopplung | Sinneskopplung | Symbole | Episodenfamilien | dominante Feldklasse | Delta Rekopplung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| BTC_2025_5M_10K | 1.00 | 0.7075 | 0.5529 | 0.1698 | 0.7428 | 0.8424 | 677 | 674 | `stabil` | 0.0000 |
| BTC_2025_5M_10K | 0.70 | 0.4952 | 0.5529 | 0.1698 | 0.7414 | 0.8424 | 677 | 674 | `stabil` | -0.2122 |
| BTC_2025_5M_10K | 0.65 | 0.4599 | 0.5529 | 0.1698 | 0.7412 | 0.8424 | 677 | 674 | `stabil` | -0.2476 |
| BTC_2025_5M_10K | 0.60 | 0.4245 | 0.5529 | 0.1698 | 0.7410 | 0.8424 | 677 | 674 | `stabil` | -0.2830 |
| BTC_2025_5M_10K | 0.55 | 0.3891 | 0.5529 | 0.1698 | 0.7408 | 0.8424 | 677 | 674 | `stabil` | -0.3184 |
| BTC_2025_5M_10K | 0.50 | 0.3537 | 0.5529 | 0.1698 | 0.7442 | 0.8424 | 677 | 674 | `stabil` | -0.3537 |
| PAXG_2024_5M_10K | 1.00 | 0.7168 | 0.5564 | 0.1668 | 0.7520 | 0.8517 | 520 | 516 | `stabil` | 0.0000 |
| PAXG_2024_5M_10K | 0.70 | 0.5017 | 0.5564 | 0.1668 | 0.7490 | 0.8517 | 520 | 516 | `stabil` | -0.2150 |
| PAXG_2024_5M_10K | 0.65 | 0.4659 | 0.5564 | 0.1668 | 0.7485 | 0.8517 | 520 | 516 | `stabil` | -0.2509 |
| PAXG_2024_5M_10K | 0.60 | 0.4301 | 0.5564 | 0.1668 | 0.7480 | 0.8517 | 520 | 516 | `stabil` | -0.2867 |
| PAXG_2024_5M_10K | 0.55 | 0.3942 | 0.5564 | 0.1668 | 0.7475 | 0.8517 | 520 | 516 | `stabil` | -0.3225 |
| PAXG_2024_5M_10K | 0.50 | 0.3584 | 0.5564 | 0.1668 | 0.7471 | 0.8517 | 520 | 516 | `stabil` | -0.3584 |

## Lesung

Dieser Test ist haerter als die reine Auswertungsdaempfung, weil die gedaempfte Rekopplung bereits in Klassifikation, Episodenbildung und passiver Rekopplungslesung mitlaeuft.

Belastbar ist hier zuerst die Richtung der Reaktion: Bleiben die Welten geordnet, werden sie diffuser, steigt Strain, oder veraendert sich nur die Rekopplungsnaehe?

Im Bereich `0.7` bis `0.5` bleibt die Reaktion weiter graduell. BTC und PAXG verhalten sich erneut fast parallel:

- die statische Rekopplung sinkt weiter erwartbar,
- Carry, Strain und Sinneskopplung bleiben unveraendert,
- Symbol- und Episodenfamilien bleiben gleich breit,
- die dominante Feldklasse bleibt durchgehend `stabil`,
- adaptive Rekopplung bleibt hoch und verliert nur minimal.

Damit ist bis `0.5` noch kein Topologiebruch sichtbar. Der Eingriff veraendert die Rueckfuehrungsnaehe, aber nicht die passive Feldordnung selbst. Das ist methodisch wichtig: Die Topologie haengt in diesen Welten nicht einfach linear an der statischen Rekopplungszahl.

## Grenze

Auch dieser Test ist noch kein Beweis fuer eine vollstaendige Feldtheorie. Er zeigt aber, ob eine gezielte Veraenderung im Lauf eine nachvollziehbare Feldantwort erzeugt.
