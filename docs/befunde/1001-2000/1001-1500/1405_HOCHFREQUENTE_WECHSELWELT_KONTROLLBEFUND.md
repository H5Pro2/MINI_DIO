# 1405 - Hochfrequente Wechselwelt als Unruhe-Ausloeser

## Zweck

Diese Pruefung trennt Frequenzwechsel von grossem Drawdown.

Ziel ist zu klaeren:

Entsteht `tragend_unruhig` eher durch schnelle Richtungswechsel als durch Range, Drawdown oder rohe Lautstaerke?

## Welt

- Datei: `data/synthetic_1405_high_frequency_switch_1000_5m.csv`
- Label: `HOLDOUT_HIGH_FREQUENCY_SWITCH`
- Kerzen: `1000`
- Richtungswechsel: `998`
- Drift: `-0.0013114560255705757`
- Avg Range: `0.00547018177019043`
- Avg Abs Return: `0.0011501773490516505`
- Max Drawdown: `0.035295687584651875`
- Quiet Score: `0.7720339415051238`

Die Welt ist nicht tief fallend und nicht stark trendend. Ihre Hauptqualitaet ist dichter Richtungswechsel.

## MINI_DIO Befund

- Trades: `0`
- Unique Symbols: `55`
- Innenwirkung: `inner_effect_stable:590`, `inner_effect_carried_unrest:404`
- Passive MCM-Klasse: `stabil:590`, `tragend_unruhig:404`
- Avg MCM Carry Quality: `0.537480134314267`
- Avg MCM Rekopplung Quality: `0.7045980528113008`
- Avg MCM Strain Quality: `0.15293390551674124`
- Avg Sensory Coupling: `0.8201772617950914`
- Avg Mini Afterimage: `0.282405423495559`
- Neuro-Tones: `focus_tone:992`, `observation_tone:2`

Die Innenfeldwirkung bleibt tragend, wird aber deutlich unruhiger.

## Rollenvergleich

Die 100er-Fenster liegen als neue Holdout-Lagen nahe `ruhige_feldnaehe`.

Wichtig ist dabei die Effektmischung:

- jedes Fenster enthaelt eine stabile Mehrheitswirkung,
- zugleich liegt in jedem Fenster ein Anteil `tragend_unruhig`,
- insgesamt entstehen `404` tragend-unruhige Episoden.

Damit zeigt die grobe Rollennaehe nicht die ganze Wirkung. Die feinere Episodenebene ist hier entscheidend.

## Erkenntnis

Hochfrequenter Richtungswechsel ist bisher der klarste Ausloeser fuer getragene Unruhe.

Im Vergleich:

- 1403: mehr Rauschen -> mehr Symbolvielfalt, aber keine starke Unruhe.
- 1404: mehr Range/Drawdown -> mehr Symbolvielfalt, aber stabile Innenwirkung.
- 1405: sehr dichter Wechsel -> starke Symbolfragmentierung und `tragend_unruhig`.

Das spricht dafuer, dass das MCM-Feld nicht nur auf Groesse oder Lautstaerke reagiert, sondern stark auf zeitliche Wechselstruktur.

## Methodische Korrektur

Die Rollenberichte speichern jetzt neben der Mehrheitswirkung auch `effect_mix`.

Grund: Bei 1405 glitt die 100er-Fenster-Mehrheit sonst ueber die tragend-unruhigen Teilanteile hinweg.

## Grenze

Dieser Befund ist passiv.

Er zeigt keine Handlung, sondern eine Innenfeldreaktion auf eine synthetische Welt mit dichter Wechselstruktur.
