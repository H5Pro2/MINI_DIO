# 839 - Rezeptor-zu-MCM-Kette: Audit

Stand: 2026-06-26 00:40:43

## Zweck

Diese Diagnose prueft die technische Kette:

```text
Aussenwelt -> Sehen / Hoeren / direkter Kontakt -> Rezeptoren -> MCM-Feldwirkung
```

Sie prueft keine Handlung, keine Strategie und keine Topologie. Es geht nur um die Frage, ob Rohdaten, Doppelwirkung oder unklare Feldkopplung in der aktuellen Mechanik sichtbar sind.

## Ergebnis

- Gepruefte Welten: 4
- Groesste Abweichung zwischen `rezeptoren.field_intake_pressure` und `mcm_feldwirkung.mcm_tension`: `0.000000`
- Groesster Anteil aktiver direkter Kontaktachse: `0.000000`

Befund:

- Roh-OHLCV gelangt nicht direkt in das MCM-Feld.
- Direkter Kontakt ist in den aktuellen Kurswelten inaktiv.
- `raw_field_intake_pressure` bleibt Diagnose.
- `adapted_field_intake_pressure` wird als `rezeptoren.field_intake_pressure` an das Feld weitergegeben.
- `mcm_feldwirkung.mcm_tension` ist aktuell technisch identisch mit `rezeptoren.field_intake_pressure`.

Das ist fachlich sauber als Alias der Feldspannung lesbar. Kritisch wird es nur dort, wo beide Werte gleichzeitig als getrennte Eingangsfeatures verarbeitet werden.

## Weltuebersicht

| Welt | Frames | Visual | Hoeren | Raw Intake | Adapted Intake | Reduktion | MCM Tension | Delta Tension/Input | Direkter Kontakt |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SOL_2024_5M | 2000 | 0.299784 | 0.213964 | 0.127712 | 0.108693 | 0.019020 | 0.108693 | 0.000000 | 0.000000 |
| BTC_2024_5M | 2000 | 0.282417 | 0.207646 | 0.124149 | 0.105827 | 0.018322 | 0.105827 | 0.000000 | 0.000000 |
| KAS_2024_5M | 2000 | 0.293225 | 0.213852 | 0.127618 | 0.108674 | 0.018944 | 0.108674 | 0.000000 | 0.000000 |
| PAXG_2024_5M | 2000 | 0.265306 | 0.192354 | 0.118421 | 0.100966 | 0.017455 | 0.100966 | 0.000000 | 0.000000 |

## Kritischer Mechanikpunkt

`mcm_neuron.FEATURES` liest derzeit sowohl:

- `rezeptoren.field_intake_pressure`
- `mcm_feldwirkung.mcm_tension`

Da beide Werte identisch sind, entsteht im neuronalen Eingangsvektor eine doppelte Funktionspraesenz derselben Feldspannung.

Das ist keine Rohdatenflutung, aber eine Dopplung der gleichen Funktion. Fachlich sollte spaeter entschieden werden:

1. Entweder das Mini-MCM-Neuron liest nur die verdichtete `mcm_feldwirkung`.
2. Oder Rezeptorwerte bleiben als getrennte Wahrnehmungsspur im Syntax-/Diagnosevektor, aber nicht als zweite Feldspannung im MCM-Neuron.

## Bewertung

Die Rezeptorschicht ist grundsaetzlich vorhanden und schuetzt das Feld bereits vor direkter Rohdatenuebernahme. Die wichtigste offene Stelle ist nicht Rohdatenflutung, sondern Schichtklarheit im neuronalen Eingangsvektor.

## Umsetzung nach Audit

Nach diesem Audit wurde die Eingangsfeature-Liste des Mini-MCM-Neurons bereinigt:

- `mini_dio/mcm_neuron.py` liest im Feldkern nur noch:
  - `mcm_feldwirkung.mcm_coherence`
  - `mcm_feldwirkung.mcm_tension`
  - `mcm_feldwirkung.mcm_asymmetry`

Damit bleibt die Rezeptorschicht als Aufnahme- und Diagnoseschicht erhalten, aber die identische Feldspannung wird nicht mehr doppelt als `rezeptoren.field_intake_pressure` und `mcm_feldwirkung.mcm_tension` in das Mini-MCM-Neuron eingespeist.

Rezeptorachsen bleiben weiter sichtbar in:

- Syntax,
- Debug,
- Befundreports,
- rezeptorischer Analyse.

Sie wirken aber nicht mehr als zweite Feldspannung im neuronalen Feldkern.

## Wie es weitergeht

Als naechstes sollte ein kurzer Vergleichslauf pruefen, ob die Topologie nach der Feature-Bereinigung stabil bleibt und ob das Feld weniger doppelt von derselben Eingangsspannung gepraegt wird.
