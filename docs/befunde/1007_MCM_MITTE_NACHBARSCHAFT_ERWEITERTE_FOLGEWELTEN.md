# 1007 - Mitte-Nachbarschaft in Folgewelten

Passive Pruefung, ob die zuvor gefundene Mitte-Nachbarschaft als feste Kopie, verlegte Rolle oder nicht sichtbare Spur in Folgewelten erscheint.

Wichtig: Diese Datei beschreibt nur Lesebefunde. Sie wirkt nicht auf MINI_DIO, nicht auf Handlung und nicht auf Regulation.

## Ergebnisuebersicht

- Beziehung erhalten: 3
- Beziehung geschwaecht: 0
- Beziehung verlagert: 0
- Beziehung nicht sichtbar: 4

## Weltbefunde

| Welt | Lesung | Beide Knoten | Reziprok | A Rolle | B Rolle | A Rekopplung | B Rekopplung | A Strain | B Strain |
|---|---:|---:|---:|---|---|---:|---:|---:|---:|
| VIERTE_WELT | beziehung_nicht_sichtbar | 0 | 0 | -/-/- | -/-/- | 0.0 | 0.0 | 0.0 | 0.0 |
| FUENFTE_WELT | beziehung_erhalten | 1 | 1 | nichtbruecke_rekopplungsfeld/stabile_bedeutungsinsel/zentrum_stabil | nichtbruecke_zentrum_schwach/stabile_bedeutungsinsel/zentrum_stabil | 0.654652 | 0.645957 | 0.178347 | 0.19074 |
| SECHSTE_WELT | beziehung_nicht_sichtbar | 0 | 0 | -/-/- | -/-/- | 0.0 | 0.0 | 0.0 | 0.0 |
| SIEBTE_WELT | beziehung_nicht_sichtbar | 0 | 0 | -/-/- | -/-/- | 0.0 | 0.0 | 0.0 | 0.0 |
| ACHTE_WELT | beziehung_nicht_sichtbar | 0 | 0 | -/-/- | -/-/- | 0.0 | 0.0 | 0.0 | 0.0 |
| NEUNTE_WELT | beziehung_erhalten | 1 | 1 | nichtbruecke_rekopplungsfeld/rekopplungszone/zentrum_stabil | nichtbruecke_zentrum_schwach/stabile_bedeutungsinsel/zentrum_stabil | 0.658442 | 0.648933 | 0.171057 | 0.184893 |
| ZEHNTE_STRESSWELT | beziehung_erhalten | 1 | 1 | nichtbruecke_rekopplungsfeld/rekopplungszone/zentrum_stabil | nichtbruecke_zentrum_schwach/rekopplungszone/zentrum_stabil | 0.658572 | 0.648979 | 0.169046 | 0.182718 |

## Befund

Die Achse `183drjy <-> 1t5bcxp` erscheint nicht als alte starre Kopie in allen Folgewelten. Erhalten bleibt sie in: `FUENFTE_WELT, NEUNTE_WELT, ZEHNTE_STRESSWELT`. Nicht sichtbar ist sie in: `VIERTE_WELT, SECHSTE_WELT, SIEBTE_WELT, ACHTE_WELT`. Wo sie erhalten bleibt, sind beide Knoten vorhanden, beide liegen zentrumsnah, und beide verweisen reziprok ueber `top_previous` / `top_next` aufeinander.

Damit ist die Mitte-Nachbarschaft eher eine verlegte Feldrolle als ein fixer Token. Das passt zum bisherigen Befund: MINI_DIO bildet keine statische Symbolkopie, sondern eine wieder erkennbare Feldbeziehung, die erst unter passenden Folgeweltbedingungen als Achse sichtbar wird.

## Deutung

- `183drjy` traegt die rekoppelnde Seite der Mitte.
- `1t5bcxp` traegt die zentrumsnahe Stabilisierungsseite.
- In `ZEHNTE_STRESSWELT` bleibt die Beziehung erhalten, obwohl die Zone von `1t5bcxp` in Richtung Rekopplung wandert.
- Die alte Mitte ist damit nicht verloren, sondern funktional in eine neue Weltlage verschoben.

## Wie es weitergeht

Als naechstes sollte diese Achsenbeziehung gegen eine neue, andersartige Folgewelt gelesen werden. Ziel ist zu pruefen, ob `183drjy <-> 1t5bcxp` stabil bleibt, sich erneut verlagert oder nur als Uebergangsbruecke zwischen zwei Feldphasen wirkte.
