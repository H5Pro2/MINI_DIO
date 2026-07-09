# 1391 - Bedeutungsnetz Nachbarschaftsdrift

## Zweck

Diese Diagnose isoliert alte Bedeutungsnetz-Knoten aus `1390` und prueft, ob Folgewelten sie exakt wiederfinden, nur benachbart aktivieren oder in mehrere Nachbarschaften aufteilen.

Die Diagnose bleibt passiv. Sie beschreibt Feldnaehe, keine Handlung.

## Befund

- untersuchte alte Knoten: `11`
- Driftzustaende: `nachbarschaft_ohne_exakten_kern:6, schwache_spur:3, stabil_wiederkehrend:2`
- Knoten mit moeglicher Teilung oder Erweiterung: `6`

## Staerkste Knoten

- `dio_meaning_node_5495a55c` (tragende_bedeutungsnaehe): `nachbarschaft_ohne_exakten_kern`, Fenster `51`, exakt `0`, nah `51`, Welten `3`
- `dio_meaning_node_d1e40f2c` (junge_spur): `stabil_wiederkehrend`, Fenster `43`, exakt `43`, nah `0`, Welten `3`
- `dio_meaning_node_476ccc10` (tragende_bedeutungsnaehe): `nachbarschaft_ohne_exakten_kern`, Fenster `34`, exakt `0`, nah `34`, Welten `3`
- `dio_meaning_node_65a8719c` (junge_spur): `nachbarschaft_ohne_exakten_kern`, Fenster `21`, exakt `0`, nah `21`, Welten `3`
- `dio_meaning_node_d5b684fe` (rollenuebergreifend_offen): `nachbarschaft_ohne_exakten_kern`, Fenster `19`, exakt `0`, nah `19`, Welten `3`
- `dio_meaning_node_ddfb5575` (rollenuebergreifend_offen): `nachbarschaft_ohne_exakten_kern`, Fenster `17`, exakt `0`, nah `17`, Welten `3`
- `dio_meaning_node_b7394769` (tragende_bedeutungsnaehe): `stabil_wiederkehrend`, Fenster `13`, exakt `6`, nah `7`, Welten `2`
- `dio_meaning_node_0fabb2f9` (junge_spur): `nachbarschaft_ohne_exakten_kern`, Fenster `10`, exakt `0`, nah `10`, Welten `3`
- `dio_meaning_node_b1b48d61` (junge_spur): `schwache_spur`, Fenster `5`, exakt `0`, nah `5`, Welten `1`
- `dio_meaning_node_119d9d87` (tragende_bedeutungsnaehe): `schwache_spur`, Fenster `2`, exakt `0`, nah `2`, Welten `1`

## Lesung

Stabil wiederkehrende Knoten wirken wie ein erhaltener Bedeutungsanker.
Wiederkehr mit Teilung bedeutet: ein alter Knoten bleibt erkennbar, bildet aber neue Nachbarschaften aus.
Nachbarschaft ohne exakten Kern bedeutet: Die alte Bedeutung wird nicht kopiert, aber das Feld findet weiterhin eine aehnliche Lage.
