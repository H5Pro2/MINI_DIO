# 1128 - Dio 0Pq6 Btc Quiet 5M Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_0pq6` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_btc_quiet_2024_5m_4k | tragende_verarbeitung | 3654 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0607 | 0.0085 | -0.0172 | 0.0648 | 0.7190 | 0.1309 |
| feld_5m | follow_candidate_btc_quiet_2024_5m_4k | tragende_verarbeitung | 3654 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0607 | 0.0081 | -0.0174 | 0.0648 | 0.7190 | 0.1309 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
