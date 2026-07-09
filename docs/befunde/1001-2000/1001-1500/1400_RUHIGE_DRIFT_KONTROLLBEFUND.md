# 1400 - Ruhige Drift als Kontrollbefund

## Zweck

Diese Pruefung stellt eine ruhige Driftwelt gegen die zuvor geprueften Holdouts:

- synthetisch glatte Kontrolle
- positive Expansion
- unruhige reale Holdout-Fenster

Ziel ist zu klaeren, ob ruhige gerichtete Bewegung eine eigene Zwischenrolle bildet, in Spannungsnaehe wandert oder bei offener Nachbarschaft bleibt.

## Welt

- Datei: `data/synthetic_1400_quiet_drift_1000_5m.csv`
- Label: `HOLDOUT_QUIET_DRIFT`
- Kerzen: `1000`
- Richtungswechsel: `5`
- Drift: `0.02034142948579984`
- Quiet Score: `0.1499417388685978`

Die Welt ist damit ruhig, leicht gerichtet und ohne starke Unruhe.

## MINI_DIO Befund

- Trades: `0`
- Unique Symbols: `6`
- Innenwirkung: `inner_effect_stable:994`
- Passive MCM-Klasse: `stabil:994`
- Avg MCM Carry Quality: `0.6164217816591637`
- Avg MCM Rekopplung Quality: `0.7571663912584952`
- Avg MCM Strain Quality: `0.11872279794642601`
- Avg Mini Afterimage: `0.8594985594447648`

Die ruhige Drift wird von MINI_DIO nicht als Spannungs- oder Kippnaehe gelesen, sondern als stabil tragende Innenfeldlage.

## Rollenvergleich

In `1395_HOLDOUT_FELDROLLEN_STABILITAET` faellt `HOLDOUT_QUIET_DRIFT` in allen Fenstern in die Naehe von `offene_nachbarschaftsrolle`.

- `neue_holdout_lage`: `3`
- `rolle_schwach_beruehrt`: `7`
- `rolle_als_nachbarschaft`: `0`

Damit bildet ruhige Drift keine neue starke Mischrolle. Sie bleibt nahe an offener Nachbarschaft, aber ohne starke Wiederkehrbindung.

## Erkenntnis

Der Befund trennt drei Weltarten klarer:

- glatte/ruhige Welt -> offene Nachbarschaft oder neue ruhige Lage
- ruhige Drift -> offene Nachbarschaft, schwach beruehrt
- Expansion/Unruhe -> Spannungsrollen und gerichtete Spannungsrollen

Damit wird die Benennung `unruhige_spannungsnaehe` fuer die alte Rolle `weite_weltspannungsnaehe` weiter plausibel. Nicht jede Bewegung erzeugt Spannungsnaehe. Entscheidend scheint nicht Richtung allein zu sein, sondern unruhige Spannungsdichte.

## Grenze

Dieser Befund beschreibt passive Feldlesung. Er ist keine Handlungslogik und keine Umbenennung im Code.
