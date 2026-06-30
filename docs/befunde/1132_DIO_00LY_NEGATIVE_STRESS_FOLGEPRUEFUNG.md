# 1132 - Dio 00Ly Negative Stress Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_00ly` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 369 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0667 | 0.0449 | -0.0444 | 0.0637 | 0.7232 | 0.1223 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 369 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0667 | 0.0446 | -0.0446 | 0.0637 | 0.7218 | 0.1214 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 699 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0333 | 0.0340 | -0.0282 | 0.0772 | 0.7186 | 0.1299 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 699 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0333 | 0.0337 | -0.0283 | 0.0772 | 0.7193 | 0.1304 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 357 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0428 | 0.0235 | -0.0262 | 0.0912 | 0.7092 | 0.1383 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 357 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0428 | 0.0228 | -0.0267 | 0.0912 | 0.7074 | 0.1371 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 321 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0352 | 0.0120 | -0.0186 | 0.0682 | 0.7067 | 0.1292 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 884 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0348 | 0.0080 | -0.0144 | 0.0752 | 0.7128 | 0.1380 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 884 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0348 | 0.0078 | -0.0144 | 0.0752 | 0.7132 | 0.1383 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 233 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0146 | 0.0120 | -0.0252 | 0.0678 | 0.7097 | 0.1215 |
| feld_5m | follow_candidate_negative_stress_2024_5m_1k | tragende_verarbeitung | 233 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0146 | 0.0115 | -0.0256 | 0.0678 | 0.7075 | 0.1201 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
