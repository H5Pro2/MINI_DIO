# 2046 - Von Feldklassen-Verfügbarkeit zu neuer Syntaxnähe

## Zweck

2044 zeigte keinen exakten Rückgriff auf alte Syntax. 2045 zeigte aber Feldklassen-Verfügbarkeit. Diese Auswertung prüft den nächsten Schritt: Bildet die neue Welt innerhalb dieser Feldklassen eigene stabile Syntaxfamilien?

Das ist passiv. Eine neue Syntaxfamilie ist hier keine Entscheidung und keine Handlung, sondern eine mögliche Bedeutungsnähe, die aus Feldkontakt wiederholt entsteht.

## Übersicht

- Familien-Feldzeilen: `3446`
- Syntaxfamilien: `2570`
- Reifungsverteilung: `{'junge_syntaxinsel': 2008, 'weltuebergreifend_feldoffen': 113, 'weltuebergreifend_feldstabil': 449}`
- Dominante Feldklassen nach Ereignissen: `{'tragende_rekopplung': 35172, 'offene_rekopplung': 3230, 'spannungsnahe_oeffnung': 432, 'getragen_offen': 110, 'offener_feldkontakt': 96}`

## Reifere Syntaxfamilien

| symbol_family | events | holdout_labels | dominant_field_contact_class | dominant_field_share | syntax_reifung | avg_carry | avg_strain | avg_rekopplung |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dio_104t | 3500 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.578 | 0.151 | 0.725 |
| dio_155c | 1736 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.564 | 0.160 | 0.716 |
| dio_0m9z | 1604 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.558 | 0.168 | 0.710 |
| dio_0h9h | 1184 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.572 | 0.140 | 0.727 |
| dio_0l7p | 966 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.575 | 0.133 | 0.729 |
| dio_14wj | 874 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.578 | 0.127 | 0.733 |
| dio_00ly | 728 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.568 | 0.137 | 0.725 |
| dio_0dd2 | 680 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.571 | 0.136 | 0.729 |
| dio_1ewh | 618 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.557 | 0.147 | 0.716 |
| dio_00ja | 568 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.549 | 0.163 | 0.703 |
| dio_1lsu | 516 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.551 | 0.155 | 0.712 |
| dio_0obq | 494 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.542 | 0.161 | 0.706 |
| dio_17ct | 494 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.559 | 0.151 | 0.717 |
| dio_1pij | 468 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.529 | 0.178 | 0.696 |
| dio_0tay | 418 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.561 | 0.142 | 0.720 |
| dio_0pz6 | 416 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.567 | 0.132 | 0.728 |
| dio_09bn | 396 | xrp2025_1h:1;xrp2024_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.568 | 0.129 | 0.730 |
| dio_06er | 388 | xrp2024_1h:1;xrp2025_1h:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.571 | 0.120 | 0.735 |

## Stärkste Familien pro Welt/Feldklasse

| holdout_label | symbol_family | field_contact_class | events | distinct_symbols | top_symbols | avg_carry | avg_strain | avg_rekopplung |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xrp2024_1h | dio_104t | tragende_rekopplung | 1788 | 1 | dio_104t4us:1788 | 0.579 | 0.150 | 0.725 |
| xrp2025_1h | dio_104t | tragende_rekopplung | 1712 | 1 | dio_104t4us:1712 | 0.578 | 0.151 | 0.724 |
| xrp2025_1h | dio_155c | tragende_rekopplung | 876 | 1 | dio_155c3g6:876 | 0.563 | 0.160 | 0.716 |
| xrp2024_1h | dio_155c | tragende_rekopplung | 860 | 1 | dio_155c3g6:860 | 0.564 | 0.159 | 0.716 |
| xrp2024_1h | dio_0m9z | tragende_rekopplung | 828 | 1 | dio_0m9zys3:828 | 0.559 | 0.167 | 0.711 |
| xrp2025_1h | dio_0m9z | tragende_rekopplung | 776 | 1 | dio_0m9zys3:776 | 0.557 | 0.169 | 0.709 |
| xrp2025_1h | dio_0h9h | tragende_rekopplung | 628 | 1 | dio_0h9h06p:628 | 0.573 | 0.140 | 0.727 |
| xrp2024_1h | dio_0h9h | tragende_rekopplung | 556 | 1 | dio_0h9h06p:556 | 0.571 | 0.139 | 0.727 |
| xrp2024_1h | dio_0l7p | tragende_rekopplung | 520 | 1 | dio_0l7pvdk:520 | 0.575 | 0.133 | 0.730 |
| xrp2024_1h | dio_14wj | tragende_rekopplung | 468 | 1 | dio_14wjmk5:468 | 0.579 | 0.126 | 0.734 |
| xrp2025_1h | dio_0l7p | tragende_rekopplung | 446 | 1 | dio_0l7pvdk:446 | 0.574 | 0.133 | 0.729 |
| xrp2024_1h | dio_0dd2 | tragende_rekopplung | 428 | 1 | dio_0dd2ogm:428 | 0.575 | 0.137 | 0.730 |
| xrp2025_1h | dio_14wj | tragende_rekopplung | 406 | 1 | dio_14wjmk5:406 | 0.578 | 0.127 | 0.733 |
| xrp2025_1h | dio_00ly | tragende_rekopplung | 372 | 1 | dio_00lyjkf:372 | 0.568 | 0.137 | 0.725 |
| xrp2024_1h | dio_00ly | tragende_rekopplung | 356 | 1 | dio_00lyjkf:356 | 0.568 | 0.136 | 0.726 |
| xrp2025_1h | dio_1ewh | tragende_rekopplung | 354 | 1 | dio_1ewh8ej:354 | 0.558 | 0.148 | 0.716 |
| xrp2025_1h | dio_00ja | tragende_rekopplung | 338 | 1 | dio_00jaski:338 | 0.551 | 0.163 | 0.704 |
| xrp2024_1h | dio_06er | tragende_rekopplung | 270 | 1 | dio_06er2zu:270 | 0.578 | 0.122 | 0.737 |

## Lesung

Wenn eine neue Welt keine alte Syntax wiederholt, aber eigene Syntaxfamilien in stabiler Feldklasse ausbildet, ist das ein anderer Reifeschritt: Nicht Erinnerung als Kopie, sondern neue Bedeutung aus ähnlicher Feldwirkung.

Wichtig ist die Grenze: Diese Familien zeigen nur wiederkehrende Feldnähe innerhalb XRP. Erst wenn dieselben Familien oder verwandte Familien in weiteren Welten anschließen, entsteht daraus eine belastbarere Vorwahrnehmungsrolle.

## Grenze

Keine Handlung, keine Richtung, kein Gate. Die Auswertung beschreibt nur, ob Feldverfügbarkeit in neue Syntaxnähe übergeht.
