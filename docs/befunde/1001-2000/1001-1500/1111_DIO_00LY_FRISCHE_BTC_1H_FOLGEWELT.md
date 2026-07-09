# 1111 - Dio 00Ly Frische Btc 1H Folgewelt

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_00ly` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 618 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0633 | 0.0552 | -0.0446 | 0.0635 | 0.7242 | 0.1275 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 618 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0633 | 0.0544 | -0.0449 | 0.0635 | 0.7244 | 0.1277 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 1339 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0534 | 0.0231 | -0.0266 | 0.0706 | 0.7301 | 0.1265 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 1339 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0534 | 0.0226 | -0.0269 | 0.0706 | 0.7301 | 0.1265 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 973 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0400 | 0.0243 | -0.0243 | 0.0779 | 0.7273 | 0.1283 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 973 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0400 | 0.0237 | -0.0247 | 0.0779 | 0.7272 | 0.1282 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 900 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0394 | 0.0166 | -0.0207 | 0.0682 | 0.7254 | 0.1286 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 900 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0394 | 0.0165 | -0.0208 | 0.0682 | 0.7257 | 0.1287 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 1075 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0285 | 0.0242 | -0.0142 | 0.0719 | 0.7204 | 0.1357 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 1075 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0285 | 0.0238 | -0.0145 | 0.0719 | 0.7205 | 0.1357 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 790 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0255 | 0.0241 | -0.0296 | 0.0819 | 0.7298 | 0.1242 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 790 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0255 | 0.0240 | -0.0296 | 0.0819 | 0.7300 | 0.1243 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 1476 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | 0.0107 | -0.0010 | 0.0040 | 0.0653 | 0.7276 | 0.1293 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 1476 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | 0.0107 | -0.0007 | 0.0042 | 0.0653 | 0.7276 | 0.1292 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
