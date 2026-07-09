# 1401 - Mittelruhige Drift als Schwellenpruefung

## Zweck

Diese Pruefung erhoeht die gerichtete Drift gegenueber `1400`, haelt aber die Richtungswechsel niedrig.

Ziel ist die Frage:

Wann kippt offene Nachbarschaft in Spannungsnaehe?

## Welt

- Datei: `data/synthetic_1401_medium_quiet_drift_1000_5m.csv`
- Label: `HOLDOUT_MEDIUM_QUIET_DRIFT`
- Kerzen: `1000`
- Richtungswechsel: `4`
- Drift: `0.1275951277857785`
- Quiet Score: `0.15846023139067797`

Die Welt ist staerker gerichtet als `1400`, bleibt aber ruhig im Sinne geringer Richtungswechsel.

## MINI_DIO Befund

- Trades: `0`
- Unique Symbols: `4`
- Innenwirkung: `inner_effect_stable:994`
- Passive MCM-Klasse: `stabil:994`
- Avg MCM Carry Quality: `0.6184175945619768`
- Avg MCM Rekopplung Quality: `0.7587362722333216`
- Avg MCM Strain Quality: `0.11752988339326825`
- Avg Mini Afterimage: `0.8692642620753334`

Trotz staerkerer Drift bleibt die Innenfeldlage stabiler als in der positiven Expansion.

## Rollenvergleich

In `1395_HOLDOUT_FELDROLLEN_STABILITAET` faellt `HOLDOUT_MEDIUM_QUIET_DRIFT` in die Naehe von `offene_nachbarschaftsrolle`.

- `neue_holdout_lage`: `4`
- `rolle_schwach_beruehrt`: `5`
- `rolle_als_nachbarschaft`: `1`

Das eine starke Nachbarschaftsfenster wird in `1396` als `ruhige_bis_mittlere_spannung` gelesen, nicht als unruhige Spannungsdichte.

## Erkenntnis

Richtung allein erzeugt im MCM-Feld keine Spannungsrolle.

Die bisherige Schwelle liegt eher bei:

- Richtungswechsel
- Ton-/Energie-Unruhe
- Spannungsdichte
- Feldabstand durch unruhige Kopplung

Damit wird die Hypothese weiter gestuetzt:

`unruhige_spannungsnaehe` ist keine reine Drift- oder Trendrolle. Sie beschreibt eine unruhig verdichtete Feldnaehe.

## Grenze

Dieser Befund ist passiv. Er beschreibt Feldlesung, keine Handlung.
