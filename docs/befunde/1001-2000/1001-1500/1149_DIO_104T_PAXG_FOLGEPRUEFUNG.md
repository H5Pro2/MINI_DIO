# 1149 - Dio 104T Paxg Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_104t` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_paxg_2024_5m_2k | kippnaehe | 12 | wechselnde_form | geordnetes_hinhoeren | belastet_kippnah | -0.0106 | 0.0199 | 0.0102 | 0.1009 | 0.6808 | 0.1860 |
| feld_5m | follow_candidate_paxg_2024_5m_2k | kippnaehe | 12 | wechselnde_form | geordnetes_hinhoeren | belastet_kippnah | -0.0106 | 0.0188 | 0.0095 | 0.1009 | 0.6784 | 0.1844 |
| feld_5m | follow_candidate_paxg_2024_5m_2k | tragende_verarbeitung | 559 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0843 | 0.0472 | -0.0449 | 0.0782 | 0.7306 | 0.1332 |
| feld_5m | follow_candidate_paxg_2024_5m_2k | tragende_verarbeitung | 559 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0843 | 0.0461 | -0.0456 | 0.0782 | 0.7305 | 0.1332 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
