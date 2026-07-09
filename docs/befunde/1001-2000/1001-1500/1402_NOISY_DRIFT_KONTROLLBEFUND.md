# 1402 - Noisy Drift als Unruhe-Schwellenpruefung

## Zweck

Diese Pruefung haelt die Drift ungefaehr auf dem Niveau von `1401`, erhoeht aber Rauschen und Richtungswechsel.

Ziel ist zu klaeren:

Reicht moderate Unruhe aus, um offene Nachbarschaft in Spannungsnaehe zu kippen?

## Welt

- Datei: `data/synthetic_1402_noisy_drift_1000_5m.csv`
- Label: `HOLDOUT_NOISY_DRIFT`
- Kerzen: `1000`
- Richtungswechsel: `21`
- Drift: `0.12884308628184235`
- Quiet Score: `0.2638638475027208`

Die Welt ist deutlich unruhiger als `1401`, aber noch nicht im Bereich starker chaotischer Wechsel.

## MINI_DIO Befund

- Trades: `0`
- Unique Symbols: `10`
- Innenwirkung: `inner_effect_stable:994`
- Passive MCM-Klasse: `stabil:994`
- Avg MCM Carry Quality: `0.6079810450732388`
- Avg MCM Rekopplung Quality: `0.7539050283397778`
- Avg MCM Strain Quality: `0.11746653697871894`
- Avg Mini Afterimage: `0.7801285215714263`

Die Unruhe erhoeht Symbolvielfalt und senkt Nachhall/Rekopplung leicht, fuehrt aber noch nicht zu `tragend_unruhig` oder Kippnaehe.

## Erkenntnis

Die bisherige Schwelle zur Spannungsnaehe liegt hoeher als moderate Drift-Unruhe.

Richtung allein reicht nicht. Moderate Richtungswechsel reichen ebenfalls noch nicht. Die bisher starken Spannungsrollen treten eher bei dichterer Wechselstruktur, groesserer Range oder staerkerer Ton-/Energieverdichtung auf.

## Grenze

Dieser Befund ist passiv und beschreibt nur Innenfeldlesung.

## Wie es weitergeht

Als naechstes sollte eine High-Noisy-Drift mit gleicher Drift, aber deutlich hoeherem Richtungswechselbereich geprueft werden. Damit laesst sich die Schwelle zur Spannungsnaehe enger eingrenzen.
