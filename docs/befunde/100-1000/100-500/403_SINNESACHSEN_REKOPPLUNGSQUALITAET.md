# 403 - Sinnesachsen-Rekopplungsqualitaet

## Fragestellung

Die globale Achspruefung zeigte nahe Mittelwerte. Diese Auswertung prueft deshalb lokal, welche Sinnesachse in Episoden eher rekoppelt und welche Achse mehr Strain oder Feldinput traegt.

Wichtig: Das ist Diagnose. Es ist keine Handlung, kein Gate und keine neue Steuerregel.

## Weltbezogene Rangordnung

| Welt | Beste Achse | Qualitaet | Balance | Hoechster Strain | Hoechster Feldinput |
|---|---:|---:|---:|---:|---:|
| BRIDGE_2024_1000 | hoeren_hin | ruhig_rekoppelnd | 0.5582 | fuehlen_abstand 0.2384 | feldinput 0.2508 |
| NEG_STRESS_2023_1000 | hoeren_hin | ruhig_rekoppelnd | 0.5597 | fuehlen_abstand 0.2144 | feldinput 0.2546 |
| POS_EXPANSION_2023_1000 | hoeren_hin | ruhig_rekoppelnd | 0.5603 | fuehlen_abstand 0.2272 | feldinput 0.2582 |
| REAL_SOL_1000 | hoeren_hin | ruhig_rekoppelnd | 0.5607 | fuehlen_abstand 0.2330 | feldinput 0.2534 |

## Achsenbefund

- `hoeren_hin`: mittlere Rekopplung 0.7104, mittlerer Strain 0.1354.
- `sehen_fokus`: mittlere Rekopplung 0.7016, mittlerer Strain 0.1438.
- `feldinput`: mittlere Rekopplung 0.6491, mittlerer Strain 0.2123, mittlerer Feldinput 0.2541.

## Interpretation

Die Sinnesachsen sind nicht gleichwertig im lokalen Innenfeld. In den geprueften Welten wirkt `hoeren_hin` am haeufigsten ruhig rekoppelnd. `sehen_fokus` bleibt tragend, liegt aber etwas naeher an Formspannung. Lokaler `feldinput` traegt dagegen mehr Strain und Kontaktlast. Das bestaetigt die Trennung: Hoeren, Sehen und Feldkontakt muessen getrennt gelesen werden, bevor daraus eine MCM-Feldwirkung entsteht.

## Mechanische Bedeutung

MINI_DIO braucht keine globale Daempfung des MCM-Feldes. Sichtbar wird eher eine rezeptorisch-regulatorische Wahrnehmungsschicht: Der Organismus kann lernen, ob eine Weltlage besser ueber Hinhoren, fokussiertes Sehen, Abstand oder gedrosselten Feldkontakt tragbar aufgenommen wird.

## Naechster Pruefpunkt

Als naechstes sollte geprueft werden, ob `hoeren_hin` wirklich eine ruhige Rekopplungsachse bleibt, wenn neue Welten mit anderer Lautstaerke, Drift und Bruchfolge hinzukommen.
