# 1831 - Daempfung Asset 10k gegen Nullwelten

Stand: 2026-07-08 22:27:48

## Grundfrage

Was passiert, wenn Rueckfuehrungsdaempfung nicht nur nachtraeglich gelesen wird, sondern direkt im isolierten MINI_DIO-Lauf wirkt?

## Aufbau

- jeder Faktor laeuft mit frischer Memory
- Standardfaktor `1.0` bleibt Referenz
- die Daempfung betrifft nur `mcm_rekopplung_quality` im passiven MCM-Feldeffekt
- keine Handlung, kein Gate, keine Entry-Logik wird daraus gebaut

## Gesamtbefund

- Faktoren: `1.00, 0.50, 0.30`
- mittlere Rekopplung bei staerkster Daempfung: `0.212715`
- mittlere Unique-Syntax bei staerkster Daempfung: `506.17`
- mittlere Episodenfamilien bei staerkster Daempfung: `503.50`

## Vergleich

| Welt | Faktor | Rekopplung | Carry | Strain | Adaptive Rekopplung | Sinneskopplung | Symbole | Episodenfamilien | dominante Feldklasse | Delta Rekopplung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| BTC_2025_5M_10K | 1.00 | 0.7075 | 0.5529 | 0.1698 | 0.7428 | 0.8424 | 677 | 674 | `stabil` | 0.0000 |
| BTC_2025_5M_10K | 0.50 | 0.3537 | 0.5529 | 0.1698 | 0.7442 | 0.8424 | 677 | 674 | `stabil` | -0.3537 |
| BTC_2025_5M_10K | 0.30 | 0.2122 | 0.5529 | 0.1698 | 0.7446 | 0.8424 | 677 | 674 | `stabil` | -0.4952 |
| DOGE_2025_5M_10K | 1.00 | 0.7069 | 0.5526 | 0.1706 | 0.7414 | 0.8413 | 673 | 670 | `stabil` | 0.0000 |
| DOGE_2025_5M_10K | 0.50 | 0.3534 | 0.5526 | 0.1706 | 0.7350 | 0.8413 | 673 | 670 | `stabil` | -0.3534 |
| DOGE_2025_5M_10K | 0.30 | 0.2121 | 0.5526 | 0.1706 | 0.7389 | 0.8413 | 673 | 670 | `stabil` | -0.4948 |
| NULL_RANDOM_2400 | 1.00 | 0.7123 | 0.5437 | 0.1521 | 0.7174 | 0.8554 | 221 | 221 | `stabil` | 0.0000 |
| NULL_RANDOM_2400 | 0.50 | 0.3562 | 0.5437 | 0.1521 | 0.6565 | 0.8554 | 221 | 221 | `stabil` | -0.3562 |
| NULL_RANDOM_2400 | 0.30 | 0.2137 | 0.5437 | 0.1521 | 0.6403 | 0.8554 | 221 | 221 | `stabil` | -0.4986 |
| NULL_SHUFFLE_2400 | 1.00 | 0.7028 | 0.5346 | 0.1653 | 0.7078 | 0.8444 | 224 | 222 | `stabil` | 0.0000 |
| NULL_SHUFFLE_2400 | 0.50 | 0.3514 | 0.5346 | 0.1653 | 0.6353 | 0.8444 | 224 | 222 | `stabil` | -0.3514 |
| NULL_SHUFFLE_2400 | 0.30 | 0.2108 | 0.5346 | 0.1653 | 0.7239 | 0.8444 | 224 | 222 | `stabil` | -0.4920 |
| PAXG_2025_5M_10K | 1.00 | 0.7171 | 0.5583 | 0.1651 | 0.7531 | 0.8531 | 577 | 573 | `stabil` | 0.0000 |
| PAXG_2025_5M_10K | 0.50 | 0.3586 | 0.5583 | 0.1651 | 0.7533 | 0.8531 | 577 | 573 | `stabil` | -0.3586 |
| PAXG_2025_5M_10K | 0.30 | 0.2151 | 0.5583 | 0.1651 | 0.7533 | 0.8531 | 577 | 573 | `stabil` | -0.5020 |
| XRP_2025_5M_10K | 1.00 | 0.7077 | 0.5536 | 0.1699 | 0.7428 | 0.8422 | 665 | 661 | `stabil` | 0.0000 |
| XRP_2025_5M_10K | 0.50 | 0.3538 | 0.5536 | 0.1699 | 0.7394 | 0.8422 | 665 | 661 | `stabil` | -0.3538 |
| XRP_2025_5M_10K | 0.30 | 0.2123 | 0.5536 | 0.1699 | 0.7446 | 0.8422 | 665 | 661 | `stabil` | -0.4954 |

## Lesung

Dieser Test ist haerter als die reine Auswertungsdaempfung, weil die gedaempfte Rekopplung bereits in Klassifikation, Episodenbildung und passiver Rekopplungslesung mitlaeuft.

Belastbar ist hier zuerst die Richtung der Reaktion: Bleiben die Welten geordnet, werden sie diffuser, steigt Strain, oder veraendert sich nur die Rekopplungsnaehe?

Die 10k-Assetfenster zeigen dieselbe robuste Grundrichtung wie die kurzen Kontrollwelten, aber mit deutlich breiterer Bedeutungsbildung:

- alle Asset- und Nullwelten bleiben dominant `stabil`,
- die statische Rekopplung sinkt mit dem Faktor,
- die Assetwelten behalten deutlich mehr Symbole und Episodenfamilien,
- adaptive Rekopplung bleibt in Assetwelten hoeher als in Nullwelten,
- Strain bleibt als Einzelwert nicht ausreichend trennscharf.

Damit bestaetigt der Lauf: Der Unterschied liegt nicht im einfachen Stabil/Kollaps-Verhalten, sondern in der Breite und Qualitaet der entstehenden Feldbedeutung.

## Grenze

Auch dieser Test ist noch kein Beweis fuer eine vollstaendige Feldtheorie. Er zeigt aber, ob eine gezielte Veraenderung im Lauf eine nachvollziehbare Feldantwort erzeugt.
