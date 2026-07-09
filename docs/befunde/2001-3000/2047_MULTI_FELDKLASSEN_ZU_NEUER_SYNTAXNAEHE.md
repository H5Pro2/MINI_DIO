# 2046 - Von Feldklassen-Verfügbarkeit zu neuer Syntaxnähe

## Zweck

2044 zeigte keinen exakten Rückgriff auf alte Syntax. 2045 zeigte aber Feldklassen-Verfügbarkeit. Diese Auswertung prüft den nächsten Schritt: Bildet die neue Welt innerhalb dieser Feldklassen eigene stabile Syntaxfamilien?

Das ist passiv. Eine neue Syntaxfamilie ist hier keine Entscheidung und keine Handlung, sondern eine mögliche Bedeutungsnähe, die aus Feldkontakt wiederholt entsteht.

## Übersicht

- Familien-Feldzeilen: `1286`
- Syntaxfamilien: `539`
- Reifungsverteilung: `{'junge_syntaxinsel': 152, 'weltuebergreifend_feldoffen': 47, 'weltuebergreifend_feldstabil': 340}`
- Dominante Feldklassen nach Ereignissen: `{'tragende_rekopplung': 29784, 'offene_rekopplung': 189, 'spannungsnahe_oeffnung': 8, 'offener_feldkontakt': 1}`

## Reifere Syntaxfamilien

| symbol_family | events | holdout_labels | dominant_field_contact_class | dominant_field_share | syntax_reifung | avg_carry | avg_strain | avg_rekopplung |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dio_104t | 2412 | doge2024:1;btc2024:1;paxg2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.588 | 0.163 | 0.726 |
| dio_0l7p | 2063 | btc2024:1;doge2024:1;paxg2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.594 | 0.151 | 0.733 |
| dio_14wj | 1696 | paxg2024:1;btc2024:1;doge2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.599 | 0.143 | 0.739 |
| dio_155c | 1208 | btc2024:1;doge2024:1;paxg2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.580 | 0.171 | 0.721 |
| dio_0m9z | 1191 | btc2024:1;doge2024:1;paxg2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.575 | 0.181 | 0.713 |
| dio_0h9h | 1012 | btc2024:1;paxg2024:1;doge2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.590 | 0.157 | 0.730 |
| dio_00ly | 619 | doge2024:1;btc2024:1;paxg2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.587 | 0.156 | 0.730 |
| dio_06s7 | 604 | doge2024:1;btc2024:1;paxg2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.594 | 0.145 | 0.736 |
| dio_1kpz | 601 | doge2024:1;btc2024:1;paxg2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.595 | 0.145 | 0.737 |
| dio_02n3 | 590 | paxg2024:1;btc2024:1;doge2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.593 | 0.138 | 0.741 |
| dio_06er | 565 | paxg2024:1;btc2024:1;doge2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.597 | 0.143 | 0.741 |
| dio_1lsu | 527 | doge2024:1;paxg2024:1;btc2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.576 | 0.172 | 0.719 |
| dio_1fll | 501 | paxg2024:1;btc2024:1;doge2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.599 | 0.131 | 0.747 |
| dio_0pz6 | 486 | doge2024:1;btc2024:1;paxg2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.592 | 0.152 | 0.733 |
| dio_03uk | 464 | paxg2024:1;btc2024:1;doge2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.591 | 0.146 | 0.736 |
| dio_01hu | 450 | paxg2024:1;btc2024:1;doge2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.581 | 0.155 | 0.730 |
| dio_0dd2 | 431 | paxg2024:1;btc2024:1;doge2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.587 | 0.156 | 0.732 |
| dio_1jc2 | 390 | paxg2024:1;btc2024:1;doge2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.597 | 0.137 | 0.740 |

## Stärkste Familien pro Welt/Feldklasse

| holdout_label | symbol_family | field_contact_class | events | distinct_symbols | top_symbols | avg_carry | avg_strain | avg_rekopplung |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| doge2024 | dio_104t | tragende_rekopplung | 931 | 1 | dio_104t4us:931 | 0.589 | 0.162 | 0.725 |
| btc2024 | dio_104t | tragende_rekopplung | 837 | 1 | dio_104t4us:837 | 0.589 | 0.161 | 0.725 |
| btc2024 | dio_0l7p | tragende_rekopplung | 779 | 1 | dio_0l7pvdk:779 | 0.596 | 0.151 | 0.732 |
| doge2024 | dio_0l7p | tragende_rekopplung | 753 | 1 | dio_0l7pvdk:753 | 0.596 | 0.151 | 0.733 |
| paxg2024 | dio_14wj | tragende_rekopplung | 714 | 1 | dio_14wjmk5:714 | 0.598 | 0.143 | 0.742 |
| paxg2024 | dio_104t | tragende_rekopplung | 644 | 1 | dio_104t4us:644 | 0.584 | 0.165 | 0.728 |
| paxg2024 | dio_0l7p | tragende_rekopplung | 531 | 1 | dio_0l7pvdk:531 | 0.592 | 0.153 | 0.735 |
| btc2024 | dio_14wj | tragende_rekopplung | 493 | 1 | dio_14wjmk5:493 | 0.599 | 0.143 | 0.737 |
| doge2024 | dio_14wj | tragende_rekopplung | 489 | 1 | dio_14wjmk5:489 | 0.599 | 0.143 | 0.737 |
| btc2024 | dio_155c | tragende_rekopplung | 485 | 1 | dio_155c3g6:485 | 0.582 | 0.170 | 0.720 |
| btc2024 | dio_0m9z | tragende_rekopplung | 443 | 1 | dio_0m9zys3:443 | 0.576 | 0.180 | 0.713 |
| doge2024 | dio_0m9z | tragende_rekopplung | 434 | 1 | dio_0m9zys3:434 | 0.576 | 0.181 | 0.712 |
| doge2024 | dio_155c | tragende_rekopplung | 434 | 1 | dio_155c3g6:434 | 0.581 | 0.171 | 0.719 |
| paxg2024 | dio_02n3 | tragende_rekopplung | 421 | 1 | dio_02n3w6a:421 | 0.597 | 0.140 | 0.748 |
| btc2024 | dio_0h9h | tragende_rekopplung | 365 | 1 | dio_0h9h06p:365 | 0.591 | 0.156 | 0.729 |
| paxg2024 | dio_1fll | tragende_rekopplung | 357 | 1 | dio_1fllaqz:357 | 0.608 | 0.129 | 0.757 |
| paxg2024 | dio_0h9h | tragende_rekopplung | 327 | 1 | dio_0h9h06p:327 | 0.588 | 0.157 | 0.733 |
| doge2024 | dio_0h9h | tragende_rekopplung | 320 | 1 | dio_0h9h06p:320 | 0.590 | 0.157 | 0.729 |

## Lesung

Wenn eine neue Welt keine alte Syntax wiederholt, aber eigene Syntaxfamilien in stabiler Feldklasse ausbildet, ist das ein anderer Reifeschritt: Nicht Erinnerung als Kopie, sondern neue Bedeutung aus ähnlicher Feldwirkung.

Wichtig ist die Grenze: Diese Familien zeigen nur wiederkehrende Feldnähe innerhalb XRP. Erst wenn dieselben Familien oder verwandte Familien in weiteren Welten anschließen, entsteht daraus eine belastbarere Vorwahrnehmungsrolle.

## Grenze

Keine Handlung, keine Richtung, kein Gate. Die Auswertung beschreibt nur, ob Feldverfügbarkeit in neue Syntaxnähe übergeht.
