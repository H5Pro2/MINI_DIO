# 1153 - Dio 104T Sideways Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_104t` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 858 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0795 | 0.0475 | -0.0339 | 0.0689 | 0.7271 | 0.1365 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 858 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0795 | 0.0463 | -0.0346 | 0.0689 | 0.7270 | 0.1364 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1690 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0648 | 0.0413 | -0.0342 | 0.0639 | 0.7350 | 0.1360 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1690 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0648 | 0.0409 | -0.0344 | 0.0639 | 0.7350 | 0.1360 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1002 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0657 | 0.0399 | -0.0254 | 0.0654 | 0.7335 | 0.1328 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1002 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0657 | 0.0389 | -0.0260 | 0.0654 | 0.7334 | 0.1328 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 125 | wechselnde_form | geordnetes_hinhoeren | offen | -0.0260 | 0.0293 | -0.0213 | 0.0657 | 0.7179 | 0.1279 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 125 | wechselnde_form | geordnetes_hinhoeren | offen | -0.0260 | 0.0287 | -0.0216 | 0.0657 | 0.7159 | 0.1266 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1121 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0256 | 0.0224 | -0.0149 | 0.0705 | 0.7304 | 0.1368 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 629 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0220 | 0.0260 | -0.0165 | 0.0766 | 0.7236 | 0.1356 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 1121 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0256 | 0.0221 | -0.0151 | 0.0705 | 0.7304 | 0.1368 |
| feld_5m | follow_candidate_sideways_2026_5m_2k | tragende_verarbeitung | 629 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0220 | 0.0251 | -0.0171 | 0.0766 | 0.7235 | 0.1355 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
