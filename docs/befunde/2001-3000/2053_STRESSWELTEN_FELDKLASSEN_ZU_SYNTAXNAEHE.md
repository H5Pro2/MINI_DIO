# 2046 - Von Feldklassen-Verfügbarkeit zu neuer Syntaxnähe

## Zweck

2044 zeigte keinen exakten Rückgriff auf alte Syntax. 2045 zeigte aber Feldklassen-Verfügbarkeit. Diese Auswertung prüft den nächsten Schritt: Bildet die neue Welt innerhalb dieser Feldklassen eigene stabile Syntaxfamilien?

Das ist passiv. Eine neue Syntaxfamilie ist hier keine Entscheidung und keine Handlung, sondern eine mögliche Bedeutungsnähe, die aus Feldkontakt wiederholt entsteht.

## Übersicht

- Familien-Feldzeilen: `17303`
- Syntaxfamilien: `12182`
- Reifungsverteilung: `{'junge_syntaxinsel': 9676, 'lokal_feldstabil': 1, 'weltuebergreifend_feldoffen': 1092, 'weltuebergreifend_feldstabil': 1413}`
- Dominante Feldklassen nach Ereignissen: `{'tragende_rekopplung': 30200, 'offene_rekopplung': 10553, 'spannungsnahe_oeffnung': 749, 'offener_feldkontakt': 260, 'getragen_offen': 184}`

## Reifere Syntaxfamilien

| symbol_family | events | holdout_labels | dominant_field_contact_class | dominant_field_share | syntax_reifung | avg_carry | avg_strain | avg_rekopplung |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dio_104t | 1420 | doge_stress:1 | tragende_rekopplung | 1.000 | lokal_feldstabil | 0.576 | 0.149 | 0.723 |
| dio_155c | 952 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.566 | 0.156 | 0.717 |
| dio_0l7p | 788 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.578 | 0.136 | 0.729 |
| dio_0m9z | 762 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.559 | 0.164 | 0.710 |
| dio_0h9h | 508 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.570 | 0.138 | 0.725 |
| dio_14wj | 486 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.579 | 0.125 | 0.733 |
| dio_00ly | 337 | doge_stress:1;btc_stress:1 | tragende_rekopplung | 0.997 | weltuebergreifend_feldstabil | 0.482 | 0.152 | 0.688 |
| dio_0oc3 | 328 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.538 | 0.169 | 0.700 |
| dio_17ct | 316 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.563 | 0.146 | 0.719 |
| dio_1lsu | 292 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.555 | 0.151 | 0.713 |
| dio_1q85 | 284 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.555 | 0.157 | 0.711 |
| dio_0pz6 | 268 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.572 | 0.130 | 0.730 |
| dio_1ewh | 268 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.554 | 0.146 | 0.714 |
| dio_06s7 | 248 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.572 | 0.123 | 0.732 |
| dio_00ja | 234 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.548 | 0.162 | 0.702 |
| dio_0obq | 230 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.545 | 0.156 | 0.708 |
| dio_1kpz | 220 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.569 | 0.122 | 0.731 |
| dio_06er | 218 | doge_stress:1 | tragende_rekopplung | 1.000 | junge_syntaxinsel | 0.575 | 0.121 | 0.735 |

## Stärkste Familien pro Welt/Feldklasse

| holdout_label | symbol_family | field_contact_class | events | distinct_symbols | top_symbols | avg_carry | avg_strain | avg_rekopplung |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| doge_stress | dio_104t | tragende_rekopplung | 1420 | 1 | dio_104t4us:1420 | 0.576 | 0.149 | 0.723 |
| doge_stress | dio_155c | tragende_rekopplung | 952 | 1 | dio_155c3g6:952 | 0.566 | 0.156 | 0.717 |
| doge_stress | dio_0l7p | tragende_rekopplung | 788 | 1 | dio_0l7pvdk:788 | 0.578 | 0.136 | 0.729 |
| doge_stress | dio_0m9z | tragende_rekopplung | 762 | 1 | dio_0m9zys3:762 | 0.559 | 0.164 | 0.710 |
| doge_stress | dio_0h9h | tragende_rekopplung | 508 | 1 | dio_0h9h06p:508 | 0.570 | 0.138 | 0.725 |
| doge_stress | dio_14wj | tragende_rekopplung | 486 | 1 | dio_14wjmk5:486 | 0.579 | 0.125 | 0.733 |
| doge_stress | dio_00ly | tragende_rekopplung | 336 | 1 | dio_00lyjkf:336 | 0.567 | 0.135 | 0.725 |
| doge_stress | dio_0oc3 | tragende_rekopplung | 328 | 1 | dio_0oc3c1g:328 | 0.538 | 0.169 | 0.700 |
| doge_stress | dio_17ct | tragende_rekopplung | 316 | 1 | dio_17ctp0f:316 | 0.563 | 0.146 | 0.719 |
| doge_stress | dio_1lsu | tragende_rekopplung | 292 | 1 | dio_1lsuk2g:292 | 0.555 | 0.151 | 0.713 |
| doge_stress | dio_1q85 | tragende_rekopplung | 284 | 1 | dio_1q85toi:284 | 0.555 | 0.157 | 0.711 |
| doge_stress | dio_0pz6 | tragende_rekopplung | 268 | 1 | dio_0pz659c:268 | 0.572 | 0.130 | 0.730 |
| doge_stress | dio_1ewh | tragende_rekopplung | 268 | 1 | dio_1ewh8ej:268 | 0.554 | 0.146 | 0.714 |
| doge_stress | dio_06s7 | tragende_rekopplung | 248 | 1 | dio_06s7dt1:248 | 0.572 | 0.123 | 0.732 |
| doge_stress | dio_00ja | tragende_rekopplung | 234 | 1 | dio_00jaski:234 | 0.548 | 0.162 | 0.702 |
| doge_stress | dio_0obq | tragende_rekopplung | 230 | 1 | dio_0obqjqx:230 | 0.545 | 0.156 | 0.708 |
| doge_stress | dio_1kpz | tragende_rekopplung | 220 | 1 | dio_1kpzc2b:220 | 0.569 | 0.122 | 0.731 |
| doge_stress | dio_06er | tragende_rekopplung | 218 | 1 | dio_06er2zu:218 | 0.575 | 0.121 | 0.735 |

## Lesung

Wenn eine neue Welt keine alte Syntax wiederholt, aber eigene Syntaxfamilien in stabiler Feldklasse ausbildet, ist das ein anderer Reifeschritt: Nicht Erinnerung als Kopie, sondern neue Bedeutung aus ähnlicher Feldwirkung.

Wichtig ist die Grenze: Diese Familien zeigen nur wiederkehrende Feldnähe innerhalb XRP. Erst wenn dieselben Familien oder verwandte Familien in weiteren Welten anschließen, entsteht daraus eine belastbarere Vorwahrnehmungsrolle.

## Grenze

Keine Handlung, keine Richtung, kein Gate. Die Auswertung beschreibt nur, ob Feldverfügbarkeit in neue Syntaxnähe übergeht.
