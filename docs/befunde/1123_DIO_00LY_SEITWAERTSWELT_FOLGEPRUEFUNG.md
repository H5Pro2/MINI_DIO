# 1123 - Dio 00Ly Seitwaertswelt Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_00ly` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1001 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0421 | 0.0271 | -0.0232 | 0.0846 | 0.7213 | 0.1346 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1001 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0421 | 0.0261 | -0.0237 | 0.0846 | 0.7212 | 0.1347 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 962 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0381 | 0.0116 | -0.0133 | 0.0694 | 0.7176 | 0.1360 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 962 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0381 | 0.0108 | -0.0137 | 0.0694 | 0.7176 | 0.1360 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1236 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0197 | 0.0185 | -0.0202 | 0.0664 | 0.7187 | 0.1363 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1236 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0197 | 0.0182 | -0.0203 | 0.0664 | 0.7187 | 0.1364 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 865 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0223 | 0.0119 | -0.0163 | 0.0672 | 0.7221 | 0.1303 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 865 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0223 | 0.0115 | -0.0164 | 0.0672 | 0.7220 | 0.1304 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1291 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0110 | 0.0115 | -0.0086 | 0.0747 | 0.7237 | 0.1300 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1291 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0110 | 0.0109 | -0.0090 | 0.0747 | 0.7237 | 0.1300 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1943 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0103 | 0.0103 | -0.0233 | 0.0759 | 0.7309 | 0.1217 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1943 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0103 | 0.0103 | -0.0233 | 0.0759 | 0.7309 | 0.1217 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
