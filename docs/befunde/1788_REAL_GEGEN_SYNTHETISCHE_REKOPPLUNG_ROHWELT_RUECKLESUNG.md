# 1788 - Real gegen synthetische Rekopplung, Rohwelt-Rücklesung

## Grundfrage

Nach 1787 war die zentrale Frage enger:

```text
Warum erzeugen synthetische Welten sehr starke Rückbindung und Nachhall,
bleiben aber kompakt,
während reale BTC-/PAXG-Fenster verteilte rekoppelnde Rollenbildung zeigen?
```

## Prüfung

Verglichen wurden:

- reale BTC-2025-Rekopplungszonen aus 15m, 30m und 1h,
- reale PAXG-2024- und PAXG-2025-Rekopplungsfenster,
- synthetische 1787-/1788-Welten mit starker Breite, Wiederkehr und Nachhall.

Die Rücklesung betrachtet nicht nur Rekopplung, sondern auch:

- Rollenanzahl,
- Kombinationen,
- Cross-State-Kopplung,
- Nachhall,
- adaptive Erfahrung,
- Rohwelt-Energie,
- Drift,
- Range,
- Richtungswechsel der Folgewelt.

## Ergebnis

| Gruppe | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Rohwelt-Charakter |
|---|---|---:|---:|---:|---:|---:|---|
| BTC 2025 | `verteilt_rekoppelnd` | 5.33 | 11.67 | 4.33 | 0.6954 | 0.3456 | zeitmaßnah, Drift steigt, Range komprimiert |
| PAXG 2024 | `verteilt_rekoppelnd` | 5.00 | 10.00 | 6.00 | 0.7070 | 0.3770 | ruhiger Energie-/Driftanstieg |
| PAXG 2025 | `verteilt_rekoppelnd` | 8.00 | 20.00 | 10.00 | 0.7042 | 0.3753 | breite Rollenbildung, mehr Nachhall |
| SYN1787 | `kompakt_nachhallend` | 2.00 | 1.00 | 0.00 | 0.7516 | 0.8079 | sehr starke kompakte Bindung |
| SYN1788 | `kompakt_nachhallend` | 2.00 | 1.00 | 0.00 | 0.7511 | 0.8003 | sehr starke kompakte Bindung |

## Interpretation

Die synthetischen Welten sind nicht zu schwach. Im Gegenteil:

```text
synthetisch:
  sehr hohe Rekopplung
  sehr hoher Nachhall
  aber nur 2 Rollen und 1 Kombination

real:
  niedrigere Rekopplung
  niedrigerer Nachhall
  aber mehr Rollen, mehr Kombinationen und mehr Cross-State-Kopplung
```

Damit trennt sich eine wichtige MCM-Lesung:

```text
starke Bindung
  != verteilte rekoppelnde Feldfunktion
```

Die reale rekoppelnde Breite scheint nicht aus reiner Stärke zu entstehen, sondern aus einer Weltphase, in der mehrere Rollen gleichzeitig unterscheidbar bleiben und dennoch rückgebunden werden.

## Bedeutung für MINI_DIO

Der Befund verbessert die bisherige Modellgrenze:

- `kompakt_nachhallend` ist eine starke, enge Bindung.
- `verteilt_offen` ist breite Rollenbildung ohne ausreichend getragene Rückbindung.
- `verteilt_rekoppelnd` ist breite Rollenbildung mit tragender Rückbindung.

Für MINI_DIO heißt das:

```text
Mehr Nachhall macht das Feld nicht automatisch intelligenter.
Mehr Rekopplung macht das Feld nicht automatisch breiter.
Breite wird erst dann wertvoll, wenn sie als Rollenraum unterscheidbar bleibt.
```

## Grenze

Das ist keine Aussage, dass synthetische Welten keine verteilte Rekopplung erzeugen können. Es zeigt nur: Die bisher geprüften synthetischen Welten erzeugen starke kompakte Bindung, aber nicht die reale verteilte Rekopplungsform von BTC/PAXG.

## Artefakte

- `reports/real_vs_synthetic_rekopplung_rawworld_signature.csv`
- `reports/btc_2025_rekopplungszonen_treffer.csv`
- `reports/paxg_2024_sequence_rawworld_contrast.csv`
- `reports/btc_paxg_2025_sequence_rawworld_contrast.csv`
- `reports/synthetic_1787_breadth_afterimage_axis_probe.csv`
- `reports/synthetic_1788_role_mosaic_afterimage_axis_probe.csv`

## Wie es weitergeht

Als nächstes sollte die reale Rollenbreite selbst genauer gelesen werden: Welche konkreten Rollen und `dio_*`-Familien tragen bei BTC/PAXG die verteilte Rekopplung, und fehlen genau diese Familien in den synthetischen Welten?
