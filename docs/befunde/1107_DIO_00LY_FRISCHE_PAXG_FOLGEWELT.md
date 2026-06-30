# 1107 - Dio 00Ly Frische Paxg Folgewelt

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_00ly` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_paxg_2024_5m_2k | tragende_verarbeitung | 1730 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.1145 | 0.0509 | -0.0550 | 0.0833 | 0.7258 | 0.1298 |
| feld_5m | follow_candidate_paxg_2024_5m_2k | tragende_verarbeitung | 1730 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.1145 | 0.0503 | -0.0554 | 0.0833 | 0.7257 | 0.1297 |
| feld_5m | follow_candidate_paxg_2024_5m_2k | tragende_verarbeitung | 490 | stabile_scharfe_form | geordnetes_hinhoeren | rekoppelt | -0.0478 | 0.0340 | -0.0341 | 0.0642 | 0.7215 | 0.1294 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
