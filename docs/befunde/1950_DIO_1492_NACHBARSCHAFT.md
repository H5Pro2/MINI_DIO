# 1950 - dio_1492 Nachbarschaftspr?fung

## Fragestellung

Nach dem Befund, dass `dio_1492` als zentrumsstabile Achse erscheint, wurde gepr?ft, ob seine Anschlussrollen stabil wiederkehren oder ob die Nachbarschaft je nach Welt wechselt.

Die Pr?fung bleibt passiv. Es wird keine Handlungslogik, kein Signal und kein Gate abgeleitet.

## Datengrundlage

Quelle: `1949_DIO_1492_NETZWERK_ACHSE.csv`

Gepr?ft wurden die Felder:

- `top_previous`
- `top_next`
- `world_names`
- `network_axis_reading`

## Ergebnis

- `dio_1492`-Achsenzeilen: `16`
- unterschiedliche Nachbarn: `17`
- Nachbarn mit Mehrweltbezug: `6`
- stabil eingestufte Nachbarn: `2`

Stabilit?tsklassen:

- `einzelanschluss`: `11`
- `mehrweltlich_duenn`: `4`
- `stabil_mehrweltlich`: `2`

## Lesung

Die Achse ist stabiler als ihre unmittelbare Umgebung.

`dio_1492` selbst bleibt in den gepr?ften Verdichtungszonen zentrumsstabil. Die Nachbarschaft ist aber nicht vollst?ndig fest. Es gibt einzelne wiederkehrende Anschlussrollen und mehrere d?nne oder weltgebundene Anschl?sse.

Das spricht gegen eine starre Symboltabelle. Fachlich sauberer ist die Lesung:

`dio_1492` wirkt als passive Zentrumsachse, an der je nach Weltkontext unterschiedliche Anschlussrollen andocken k?nnen.

## Wichtigster Befund

Die Nachbarschaft best?tigt die Achsenlesung, aber sie zeigt zugleich Beweglichkeit.

Das bedeutet:

- Die Achse bleibt erkennbar.
- Die Umgebung bleibt variabel.
- Die Feldordnung ist nicht starr.
- Die MCM-Topologie wirkt eher wie ein dynamisches Bedeutungsnetz als wie eine feste Tabelle.

## Top-Nachbarn

- `dio_mcm_episode_1aavr7r`: count `4`, Welten `2`, Richtung previous `2` / next `2`, Klasse `stabil_mehrweltlich`
- `dio_mcm_episode_0e7qvj1`: count `3`, Welten `3`, Richtung previous `1` / next `2`, Klasse `stabil_mehrweltlich`
- `dio_mcm_episode_1yy9dcm`: count `2`, Welten `1`, Richtung previous `2` / next `0`, Klasse `einzelanschluss`
- `dio_mcm_episode_1ytjvg8`: count `2`, Welten `1`, Richtung previous `0` / next `2`, Klasse `einzelanschluss`
- `dio_mcm_episode_0k1pid9`: count `2`, Welten `2`, Richtung previous `2` / next `0`, Klasse `mehrweltlich_duenn`
- `dio_mcm_episode_0vff3w6`: count `2`, Welten `1`, Richtung previous `0` / next `2`, Klasse `einzelanschluss`
- `dio_mcm_episode_1q3us3f`: count `2`, Welten `2`, Richtung previous `2` / next `0`, Klasse `mehrweltlich_duenn`
- `dio_mcm_episode_1pwdejt`: count `2`, Welten `1`, Richtung previous `2` / next `0`, Klasse `einzelanschluss`
- `dio_mcm_episode_0x6cqpn`: count `2`, Welten `1`, Richtung previous `0` / next `2`, Klasse `einzelanschluss`
- `dio_mcm_episode_1pmt8u2`: count `2`, Welten `6`, Richtung previous `2` / next `0`, Klasse `mehrweltlich_duenn`

## Grenze

Ein Nachbar-Token ist hier noch keine semantisch erkl?rte Bedeutung. Er zeigt nur, dass bestimmte Anschl?sse im Bedeutungsnetz wiederholt neben `dio_1492` auftreten.

## N?chster Pr?fpunkt

Als n?chstes sollte gepr?ft werden, ob die stabileren Nachbarn von `dio_1492` eigene Rollenqualit?t tragen: Zentrum, Br?cke, Rand, offene Zone oder Rekopplung. Erst dadurch wird sichtbar, ob `dio_1492` eine Achse mit geordneten Anschlussr?umen bildet oder nur wiederkehrend in einem allgemeinen Zentrum liegt.
