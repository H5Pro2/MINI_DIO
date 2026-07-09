# 1403 - High-Noisy-Drift als Rauschgrenzen-Pruefung

## Zweck

Diese Pruefung erhoeht gegenueber `1402` die synthetische Unruhe deutlich.

Ziel ist zu klaeren:

Reicht hoehere Oberflaechenvarianz aus, um aus stabiler Nachbarschaft echte Spannungsnaehe zu bilden?

## Welt

- Datei: `data/synthetic_1403_high_noisy_drift_1000_5m.csv`
- Label: `HOLDOUT_HIGH_NOISY_DRIFT`
- Kerzen: `1000`
- Richtungswechsel: `31`
- Drift: `0.13078553957630656`
- Quiet Score: `0.40766831658357966`
- Max Drawdown: `0.1332642588815784`

Die Welt ist deutlich unruhiger als `1402`, bleibt aber im Feld nicht kollabierend.

## MINI_DIO Befund

- Trades: `0`
- Unique Symbols: `12`
- Innenwirkung: `inner_effect_stable:994`
- Passive MCM-Klasse: `stabil:994`
- Avg MCM Carry Quality: `0.6029291762274028`
- Avg MCM Rekopplung Quality: `0.7514984383826241`
- Avg MCM Strain Quality: `0.1177041384675605`
- Avg Sensory Coupling: `0.9136205609628811`
- Avg Mini Afterimage: `0.7286094899569522`
- Neuro-Tones: `focus_tone:399`, `observation_tone:595`

Die Symbolvielfalt steigt, der Nachhall sinkt, aber die MCM-Wirkung bleibt stabil.

## Rollenvergleich

- `neue_holdout_lage`: `4`
- `rolle_schwach_beruehrt`: `6`
- Starke Rollen-Nachbarschaft: `0`
- Naechste Rollen: vor allem `offene_nachbarschaftsrolle`, einmal schwach `weite_weltspannungsnaehe`

Damit reicht hoehere Drift-Unruhe allein nicht aus, um eine starke Spannungsnaehe zu erzeugen.

## Erkenntnis

Die Schwelle zur Spannungsnaehe liegt nicht in Rauschen allein.

Wahrscheinlicher ist eine Kopplung aus:

- groesserer Range,
- dichterer Richtungswechselstruktur,
- staerkerer Ton-/Energieverdichtung,
- hoeherer oder anders gebundener Rezeptoraufnahme.

1403 wirkt wie Oberflaechenvarianz: MINI_DIO bildet mehr Syntaxfamilien, haelt die Innenfeldwirkung aber stabil.

## Grenze

Dieser Befund ist passiv. Er beschreibt keine Handlung, kein Entry-System und keine Regel.
