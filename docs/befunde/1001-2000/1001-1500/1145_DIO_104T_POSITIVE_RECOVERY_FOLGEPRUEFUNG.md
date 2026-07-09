# 1145 - Dio 104T Positive Recovery Folgepruefung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Wie sieht die reale Rueckkopplung der Brueckenfamilie `dio_104t` in einzelnen Rohweltfenstern aus?

## Repraesentative Ereignisse

| Weltgruppe | Welt | Muster | Tick | Visual | Ton | Feld | Spannung Delta | Rekopplung Delta | Strain Delta | Spannung | Rekopplung | Strain |
|---|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 155 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0498 | 0.0423 | -0.0234 | 0.0692 | 0.7150 | 0.1392 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 155 | stabile_scharfe_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0498 | 0.0417 | -0.0235 | 0.0692 | 0.7157 | 0.1399 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 485 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0497 | 0.0386 | -0.0211 | 0.0641 | 0.7275 | 0.1305 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 485 | wechselnde_form | geordnetes_hinhoeren | rekoppelt | -0.0497 | 0.0374 | -0.0218 | 0.0641 | 0.7275 | 0.1306 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 106 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0522 | 0.0317 | -0.0286 | 0.0673 | 0.7125 | 0.1275 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 106 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | offen | -0.0522 | 0.0308 | -0.0292 | 0.0673 | 0.7102 | 0.1260 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 604 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0306 | 0.0242 | -0.0084 | 0.0670 | 0.7241 | 0.1396 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 471 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0224 | 0.0153 | -0.0105 | 0.0800 | 0.7203 | 0.1389 |
| feld_5m | follow_candidate_positive_recovery_2025_5m_1k | tragende_verarbeitung | 471 | wechselnde_form | geordnetes_hinhoeren_mit_wechsel | rekoppelt | -0.0224 | 0.0148 | -0.0108 | 0.0800 | 0.7203 | 0.1389 |

## Lesart

Die gleiche Symbolfamilie wird nicht durch sich selbst bedeutungsvoll. Ihre Bedeutung entsteht aus der Kopplung an Vorfenster, aktuelles Feld und Rezeptorhaltung.

Wenn `tragende_verarbeitung` und `kippnaehe` fuer dieselbe Familie verschiedene Spannungs-, Rekopplungs- und Strain-Verlaeufe zeigen, dann bestaetigt das die Grenze aus 1074:

```text
innere Familie allein reicht nicht;
Realitaetsrueckkopplung entscheidet die aktuelle Lesart.
```

## Wie es weitergeht

Als naechstes sollte aus diesen Ereignissen ein kleiner Rohwelt-Ausschnitt mit Tickfenstern extrahiert werden, damit die Feldfolge vor und nach der Familie sichtbar wird.
