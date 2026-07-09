# 1152 - Dio 104T Expansion Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_104t` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 76 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0446 | 0.0459 | -0.0364 | 0.0688 | 0.7106 | 0.1347 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 76 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0446 | 0.0457 | -0.0366 | 0.0688 | 0.7089 | 0.1336 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 34 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0414 | 0.0452 | -0.0432 | 0.0630 | 0.7083 | 0.1263 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 34 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0414 | 0.0451 | -0.0430 | 0.0630 | 0.7099 | 0.1275 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 500 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0498 | 0.0293 | -0.0224 | 0.0691 | 0.7262 | 0.1331 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 500 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0498 | 0.0284 | -0.0229 | 0.0691 | 0.7261 | 0.1330 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 499 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0403 | 0.0259 | -0.0205 | 0.0721 | 0.7229 | 0.1338 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 499 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0403 | 0.0249 | -0.0211 | 0.0721 | 0.7228 | 0.1337 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 95 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0096 | 0.0353 | -0.0244 | 0.0728 | 0.7182 | 0.1305 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 95 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0096 | 0.0351 | -0.0245 | 0.0728 | 0.7169 | 0.1296 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 948 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | 0.0109 | 0.0104 | 0.0085 | 0.0750 | 0.7255 | 0.1397 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 948 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | 0.0109 | 0.0098 | 0.0081 | 0.0750 | 0.7255 | 0.1397 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 945 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | 0.0055 | 0.0094 | 0.0048 | 0.0675 | 0.7263 | 0.1389 |
| feld_5m | follow_candidate_expansion_2023_5m_1k | tragende_verarbeitung | 945 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | 0.0055 | 0.0088 | 0.0045 | 0.0675 | 0.7263 | 0.1389 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
