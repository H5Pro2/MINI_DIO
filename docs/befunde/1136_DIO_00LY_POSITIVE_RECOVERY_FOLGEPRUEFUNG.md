# 1136 - Dio 00Ly Positive Recovery Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_00ly` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 681 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0796 | 0.0413 | -0.0501 | 0.0660 | 0.7169 | 0.1320 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 681 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0796 | 0.0406 | -0.0503 | 0.0660 | 0.7167 | 0.1321 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 976 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0397 | 0.0247 | -0.0271 | 0.0694 | 0.7261 | 0.1241 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 976 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0397 | 0.0245 | -0.0271 | 0.0694 | 0.7261 | 0.1242 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 906 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0237 | 0.0143 | -0.0165 | 0.0724 | 0.7181 | 0.1347 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 906 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0237 | 0.0137 | -0.0167 | 0.0724 | 0.7181 | 0.1349 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
