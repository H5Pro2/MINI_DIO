# 1952 - dio_1492 ?bergangsketten der Anschlussr?ume

## Fragestellung

Nach der Pr?fung der Anschlussr?ume wurde gepr?ft, ob diese R?ume eigene ?bergangsketten bilden.

Hierarchie der Pr?fung:

- Grundfrage: Organisiert `dio_1492` ein lokales Feldnetz?
- Unterpr?fung: F?hren die Anschlussr?ume in erkennbare Rollenqualit?ten hinein oder aus ihnen heraus?
- Folgeschritt: Pr?fen, ob die st?rksten ?berg?nge in neuen Welten reproduzierbar bleiben.

Die Pr?fung bleibt passiv. Es wird keine Handlungslogik, kein Signal und kein Gate abgeleitet.

## Datengrundlage

Ausgangspunkt waren die sechs Anschlussr?ume aus `1951_DIO_1492_ANSCHLUSSRAEUME.csv`. Gelesen wurden alle vorhandenen Verdichtungszonen-Transitionen.

- gepr?fte ?bergangskanten mit Anschlussraum-Bezug: `29`
- Anschlussr?ume mit Transitionstreffern: `3`

Richtungen:

- `outgoing`: `17`
- `incoming`: `12`

Pfadlesungen:

- `anschluss_zu_rekopplung`: `10`
- `anschluss_zu_zentrum`: `9`
- `anschluss_zu_unbestimmt`: `5`
- `anschluss_zu_uebergang`: `3`
- `anschluss_zu_offener_varianz`: `2`

## Befund

Die Anschlussr?ume f?hren nicht zuf?llig ins Leere. Ihre Transitionen zeigen vor allem Wege zu Zentrum, Rekopplung und ?bergangszonen. Damit wirkt `dio_1492` nicht nur als Achse mit Nachbarn, sondern als Achse mit lokalen ?bergangspfaden.

Das ist wichtig: Die Feldordnung bleibt dynamisch, aber sie ist nicht beliebig. Anschlussr?ume k?nnen als Korridore gelesen werden, ?ber die das Feld zwischen Zentrum, Rekopplung, ?bergang und offener Varianz wechselt.

## St?rkste ?berg?nge

- `dio_mcm_episode_0e7qvj1` outgoing `dio_mcm_episode_1hdpu9s`: count `176`, `anschluss_zu_zentrum`, andere Zone `stabile_bedeutungsinsel`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_0e7qvj1` incoming `dio_mcm_episode_0mji3u6`: count `170`, `anschluss_zu_uebergang`, andere Zone `hoeherer_cluster_uebergang`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_0e7qvj1` incoming `dio_mcm_episode_1hdpu9s`: count `162`, `anschluss_zu_zentrum`, andere Zone `stabile_bedeutungsinsel`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_0e7qvj1` outgoing `dio_mcm_episode_1jwnjz4`: count `113`, `anschluss_zu_rekopplung`, andere Zone `rekopplungszone`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_0e7qvj1` incoming `dio_mcm_episode_1jwnjz4`: count `98`, `anschluss_zu_rekopplung`, andere Zone `rekopplungszone`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_0e7qvj1` incoming `dio_mcm_episode_0z748ck`: count `87`, `anschluss_zu_rekopplung`, andere Zone `rekopplungszone`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_0e7qvj1` outgoing `dio_mcm_episode_0mji3u6`: count `85`, `anschluss_zu_uebergang`, andere Zone `hoeherer_cluster_uebergang`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_0e7qvj1` outgoing `dio_mcm_episode_18l3thm`: count `60`, `anschluss_zu_zentrum`, andere Zone `stabile_bedeutungsinsel`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_0e7qvj1` incoming `dio_mcm_episode_18l3thm`: count `49`, `anschluss_zu_zentrum`, andere Zone `stabile_bedeutungsinsel`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_1q3us3f` incoming `dio_mcm_episode_18l3thm`: count `38`, `anschluss_zu_zentrum`, andere Zone `stabile_bedeutungsinsel`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_1q3us3f` outgoing `dio_mcm_episode_1hdpu9s`: count `37`, `anschluss_zu_zentrum`, andere Zone `stabile_bedeutungsinsel`, andere Rolle `zentrum_stabil`
- `dio_mcm_episode_1q3us3f` incoming `dio_mcm_episode_1hdpu9s`: count `32`, `anschluss_zu_zentrum`, andere Zone `stabile_bedeutungsinsel`, andere Rolle `zentrum_stabil`

## Interpretation

`dio_1492` zeigt damit drei Ebenen:

1. Achse: `dio_1492` selbst bleibt zentrumsnah und phasen?bergreifend sichtbar.
2. Anschlussraum: direkte Nachbarn tragen eigene Feldqualit?t.
3. ?bergangskette: diese Anschlussr?ume f?hren in weitere Rollenqualit?ten hinein oder aus ihnen heraus.

Das spricht f?r ein lokales Feldnetz, nicht nur f?r eine einzelne Bedeutungsinsel.

## Grenze

Eine Transition ist hier keine Absicht und kein bewusstes Handeln. Sie zeigt nur, dass im passiven Bedeutungsnetz wiederkehrende Anschlussfolgen auftreten.

## N?chster Pr?fpunkt

Als n?chstes sollte gepr?ft werden, ob die st?rksten ?bergangsketten bei neuen Welten erneut erscheinen. Entscheidend ist, ob sie reproduzierbar bleiben, sich teilen oder unter anderer Weltspannung driften.
