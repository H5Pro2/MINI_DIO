# 1144 - Dio 104T Negative Stress Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_104t` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | kippnaehe | 20 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0117 | -0.0027 | 0.0016 | 0.0892 | 0.6590 | 0.1705 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | kippnaehe | 20 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0117 | -0.0021 | 0.0021 | 0.0892 | 0.6617 | 0.1722 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 545 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0197 | 0.0332 | -0.0131 | 0.0844 | 0.7251 | 0.1395 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 545 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0197 | 0.0324 | -0.0135 | 0.0844 | 0.7250 | 0.1394 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 264 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0246 | 0.0222 | -0.0194 | 0.0664 | 0.7182 | 0.1309 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 264 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0246 | 0.0215 | -0.0197 | 0.0664 | 0.7184 | 0.1313 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 57 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0199 | 0.0256 | -0.0144 | 0.0649 | 0.7112 | 0.1338 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 57 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0199 | 0.0255 | -0.0145 | 0.0649 | 0.7091 | 0.1324 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 420 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0124 | 0.0304 | -0.0173 | 0.0655 | 0.7257 | 0.1313 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 420 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0124 | 0.0297 | -0.0177 | 0.0655 | 0.7258 | 0.1314 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 383 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | 0.0096 | 0.0146 | -0.0021 | 0.0835 | 0.7200 | 0.1357 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 383 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | 0.0096 | 0.0135 | -0.0026 | 0.0835 | 0.7202 | 0.1360 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
