# 1108 - Dio 0Pq6 Frische Paxg Folgewelt

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_0pq6` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_paxg_2024_5m_2k | kippnaehe | 110 | wechselnde_form | geordnetes_hinhoeren | offen | 0.0139 | -0.0509 | 0.0359 | 0.0820 | 0.6664 | 0.1592 |
| feld_5m | follow_candidate_paxg_2024_5m_2k | kippnaehe | 110 | wechselnde_form | geordnetes_hinhoeren | offen | 0.0139 | -0.0500 | 0.0362 | 0.0820 | 0.6693 | 0.1608 |
| feld_5m | follow_candidate_paxg_2024_5m_2k | kippnaehe | 500 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | 0.0038 | -0.0051 | 0.0090 | 0.0959 | 0.6891 | 0.1593 |
| feld_5m | follow_candidate_paxg_2024_5m_2k | kippnaehe | 500 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | 0.0038 | -0.0039 | 0.0096 | 0.0959 | 0.6909 | 0.1604 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
