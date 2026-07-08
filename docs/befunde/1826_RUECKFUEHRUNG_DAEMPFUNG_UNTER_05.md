# 1826 - Rueckfuehrungsdaempfung unter 0.5

Stand: 2026-07-08 22:05:25

## Grundfrage

Was passiert, wenn Rueckfuehrungsdaempfung nicht nur nachtraeglich gelesen wird, sondern direkt im isolierten MINI_DIO-Lauf wirkt?

## Aufbau

- jeder Faktor laeuft mit frischer Memory
- Standardfaktor `1.0` bleibt Referenz
- die Daempfung betrifft nur `mcm_rekopplung_quality` im passiven MCM-Feldeffekt
- keine Handlung, kein Gate, keine Entry-Logik wird daraus gebaut

## Gesamtbefund

- Faktoren: `1.00, 0.50, 0.45, 0.40, 0.35, 0.30`
- mittlere Rekopplung bei staerkster Daempfung: `0.213639`
- mittlere Unique-Syntax bei staerkster Daempfung: `598.50`
- mittlere Episodenfamilien bei staerkster Daempfung: `595.00`

## Vergleich

| Welt | Faktor | Rekopplung | Carry | Strain | Adaptive Rekopplung | Sinneskopplung | Symbole | Episodenfamilien | dominante Feldklasse | Delta Rekopplung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| BTC_2025_5M_10K | 1.00 | 0.7075 | 0.5529 | 0.1698 | 0.7428 | 0.8424 | 677 | 674 | `stabil` | 0.0000 |
| BTC_2025_5M_10K | 0.50 | 0.3537 | 0.5529 | 0.1698 | 0.7442 | 0.8424 | 677 | 674 | `stabil` | -0.3537 |
| BTC_2025_5M_10K | 0.45 | 0.3184 | 0.5529 | 0.1698 | 0.7443 | 0.8424 | 677 | 674 | `stabil` | -0.3891 |
| BTC_2025_5M_10K | 0.40 | 0.2830 | 0.5529 | 0.1698 | 0.7444 | 0.8424 | 677 | 674 | `stabil` | -0.4245 |
| BTC_2025_5M_10K | 0.35 | 0.2476 | 0.5529 | 0.1698 | 0.7446 | 0.8424 | 677 | 674 | `stabil` | -0.4599 |
| BTC_2025_5M_10K | 0.30 | 0.2122 | 0.5529 | 0.1698 | 0.7446 | 0.8424 | 677 | 674 | `stabil` | -0.4952 |
| PAXG_2024_5M_10K | 1.00 | 0.7168 | 0.5564 | 0.1668 | 0.7520 | 0.8517 | 520 | 516 | `stabil` | 0.0000 |
| PAXG_2024_5M_10K | 0.50 | 0.3584 | 0.5564 | 0.1668 | 0.7471 | 0.8517 | 520 | 516 | `stabil` | -0.3584 |
| PAXG_2024_5M_10K | 0.45 | 0.3225 | 0.5564 | 0.1668 | 0.7466 | 0.8517 | 520 | 516 | `stabil` | -0.3942 |
| PAXG_2024_5M_10K | 0.40 | 0.2867 | 0.5564 | 0.1668 | 0.7461 | 0.8517 | 520 | 516 | `stabil` | -0.4301 |
| PAXG_2024_5M_10K | 0.35 | 0.2509 | 0.5564 | 0.1668 | 0.7458 | 0.8517 | 520 | 516 | `stabil` | -0.4659 |
| PAXG_2024_5M_10K | 0.30 | 0.2150 | 0.5564 | 0.1668 | 0.7452 | 0.8517 | 520 | 516 | `stabil` | -0.5017 |

## Lesung

Dieser Test ist haerter als die reine Auswertungsdaempfung, weil die gedaempfte Rekopplung bereits in Klassifikation, Episodenbildung und passiver Rekopplungslesung mitlaeuft.

Belastbar ist hier zuerst die Richtung der Reaktion: Bleiben die Welten geordnet, werden sie diffuser, steigt Strain, oder veraendert sich nur die Rekopplungsnaehe?

Auch unter `0.5` bleibt kein harter Kipppunkt sichtbar. Bis Faktor `0.3` gilt:

- die statische Rekopplung sinkt stark und fast linear,
- Carry, Strain und Sinneskopplung bleiben unveraendert,
- Symbol- und Episodenfamilien bleiben gleich breit,
- die dominante Feldklasse bleibt `stabil`,
- adaptive Rekopplung bleibt hoch; bei BTC steigt sie sogar leicht, bei PAXG sinkt sie nur gering.

Damit trennt sich die gelesene Topologie weiter von der statischen Rekopplungszahl. Der Eingriff reduziert die gemessene Rueckfuehrungsnaehe, aber die passive Feldorganisation bleibt in diesen beiden Langfenstern erhalten.

Das ist kein Beweis fuer absolute Robustheit. Es ist aber ein starker Hinweis, dass MINI_DIO hier nicht einfach kollabiert, sobald eine einzelne Achse numerisch gedaempft wird. Die Feldordnung scheint von mehreren tragenden Anteilen gehalten zu werden.

## Grenze

Auch dieser Test ist noch kein Beweis fuer eine vollstaendige Feldtheorie. Er zeigt aber, ob eine gezielte Veraenderung im Lauf eine nachvollziehbare Feldantwort erzeugt.

## Wie es weitergeht

Als naechstes sollte nicht sofort weiter nach unten skaliert werden. Sinnvoller ist die Gegenprobe mit Stress-, Expansions- und Nullwelten bei denselben Faktoren. Entscheidend ist, ob nur BTC/PAXG stabil bleiben oder ob die robuste Feldordnung weltuebergreifend bestehen bleibt.
