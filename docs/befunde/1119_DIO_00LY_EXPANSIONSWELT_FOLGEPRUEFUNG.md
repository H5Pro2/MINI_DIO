# 1119 - Dio 00Ly Expansionswelt Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_00ly` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 10 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0054 | 0.0677 | -0.0411 | 0.0910 | 0.7260 | 0.1345 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 10 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0054 | 0.0668 | -0.0415 | 0.0910 | 0.7234 | 0.1331 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 497 | wechselnde_form | geordnetes_hinhoeren | offen | -0.0506 | 0.0165 | -0.0237 | 0.0635 | 0.7120 | 0.1318 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 497 | wechselnde_form | geordnetes_hinhoeren | offen | -0.0506 | 0.0162 | -0.0238 | 0.0635 | 0.7109 | 0.1311 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 776 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0246 | 0.0214 | -0.0253 | 0.0725 | 0.7170 | 0.1282 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 776 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0246 | 0.0212 | -0.0253 | 0.0725 | 0.7163 | 0.1277 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
