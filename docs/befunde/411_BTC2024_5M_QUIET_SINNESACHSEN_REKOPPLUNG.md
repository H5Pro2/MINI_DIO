# 411 - Sinnesachsen-Rekopplungsqualitaet

## Fragestellung

Die globale Achspruefung zeigte nahe Mittelwerte. Diese Auswertung prueft deshalb lokal, welche Sinnesachse in Episoden eher rekoppelt und welche Achse mehr Strain oder Feldinput traegt.

Wichtig: Das ist Diagnose. Es ist keine Handlung, kein Gate und keine neue Steuerregel.

## Weltbezogene Rangordnung

| Welt | Beste Achse | Qualitaet | Balance | Hoechster Strain | Hoechster Feldinput |
|---|---:|---:|---:|---:|---:|
| BTC_2024_5M_QUIET_4000 | hoeren_hin | ruhig_rekoppelnd | 0.5702 | fuehlen_abstand 0.2203 | feldinput 0.2516 |

## Achsenbefund

- `hoeren_hin`: mittlere Rekopplung 0.7197, mittlerer Strain 0.1340.
- `sehen_fokus`: mittlere Rekopplung 0.7128, mittlerer Strain 0.1394.
- `feldinput`: mittlere Rekopplung 0.6634, mittlerer Strain 0.2014, mittlerer Feldinput 0.2516.

## Interpretation

Die Sinnesachsen sind nicht gleichwertig im lokalen Innenfeld. In den geprueften Welten wirkt `hoeren_hin` am haeufigsten ruhig rekoppelnd. `sehen_fokus` bleibt tragend, liegt aber etwas naeher an Formspannung. Lokaler `feldinput` traegt dagegen mehr Strain und Kontaktlast. Das bestaetigt die Trennung: Hoeren, Sehen und Feldkontakt muessen getrennt gelesen werden, bevor daraus eine MCM-Feldwirkung entsteht.

## Mechanische Bedeutung

MINI_DIO braucht keine globale Daempfung des MCM-Feldes. Sichtbar wird eher eine rezeptorisch-regulatorische Wahrnehmungsschicht: Der Organismus kann lernen, ob eine Weltlage besser ueber Hinhoren, fokussiertes Sehen, Abstand oder gedrosselten Feldkontakt tragbar aufgenommen wird.

## Naechster Pruefpunkt

Als naechstes sollte geprueft werden, ob `hoeren_hin` wirklich eine ruhige Rekopplungsachse bleibt, wenn neue Welten mit anderer Lautstaerke, Drift und Bruchfolge hinzukommen.
