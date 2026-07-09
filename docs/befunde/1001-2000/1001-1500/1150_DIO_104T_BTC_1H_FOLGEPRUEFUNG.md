# 1150 - Dio 104T Btc 1H Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_104t` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 222 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0630 | 0.0496 | -0.0422 | 0.0673 | 0.7256 | 0.1334 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 222 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0630 | 0.0490 | -0.0426 | 0.0673 | 0.7255 | 0.1333 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 1931 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0625 | 0.0320 | -0.0203 | 0.0644 | 0.7293 | 0.1386 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 488 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0256 | 0.0203 | 0.0025 | 0.0634 | 0.7300 | 0.1349 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 488 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0256 | 0.0187 | 0.0015 | 0.0634 | 0.7299 | 0.1349 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 366 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0093 | 0.0185 | -0.0053 | 0.0666 | 0.7280 | 0.1360 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 888 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0109 | 0.0160 | -0.0088 | 0.0709 | 0.7307 | 0.1351 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 366 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0093 | 0.0176 | -0.0059 | 0.0666 | 0.7278 | 0.1359 |
| zeit_1h | follow_candidate_btc_2024_1h_2k | tragende_verarbeitung | 888 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0109 | 0.0155 | -0.0091 | 0.0709 | 0.7307 | 0.1351 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
