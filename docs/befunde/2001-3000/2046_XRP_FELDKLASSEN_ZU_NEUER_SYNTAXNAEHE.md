# 2046 - Von Feldklassen-Verfügbarkeit zu neuer Syntaxnähe

## Zweck

2044 zeigte keinen exakten Rückgriff auf alte Syntax. 2045 zeigte aber Feldklassen-Verfügbarkeit. Diese Auswertung prüft den nächsten Schritt: Bildet die neue Welt innerhalb dieser Feldklassen eigene stabile Syntaxfamilien?

Das ist passiv. Eine neue Syntaxfamilie ist hier keine Entscheidung und keine Handlung, sondern eine mögliche Bedeutungsnähe, die aus Feldkontakt wiederholt entsteht.

## Übersicht

- Familien-Feldzeilen: `1587`
- Syntaxfamilien: `877`
- Reifungsverteilung: `{'junge_syntaxinsel': 399, 'weltuebergreifend_feldoffen': 86, 'weltuebergreifend_feldstabil': 392}`
- Dominante Feldklassen nach Ereignissen: `{'tragende_rekopplung': 38686, 'offene_rekopplung': 866, 'spannungsnahe_oeffnung': 330, 'offener_feldkontakt': 56, 'getragen_offen': 38}`

## Reifere Syntaxfamilien

| symbol_family | events | holdout_labels | dominant_field_contact_class | dominant_field_share | syntax_reifung | avg_carry | avg_strain | avg_rekopplung |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dio_104t | 3380 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.577 | 0.150 | 0.724 |
| dio_155c | 1872 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.563 | 0.160 | 0.716 |
| dio_0m9z | 1734 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.558 | 0.167 | 0.710 |
| dio_0h9h | 1318 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.573 | 0.140 | 0.726 |
| dio_0l7p | 1046 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.575 | 0.133 | 0.729 |
| dio_14wj | 964 | xrp2024:1;xrp2025:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.577 | 0.127 | 0.733 |
| dio_00ly | 852 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.568 | 0.136 | 0.726 |
| dio_1pij | 708 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.533 | 0.179 | 0.696 |
| dio_00ja | 684 | xrp2024:1;xrp2025:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.551 | 0.163 | 0.704 |
| dio_1ewh | 642 | xrp2024:1;xrp2025:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.556 | 0.149 | 0.715 |
| dio_0dd2 | 616 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.571 | 0.136 | 0.729 |
| dio_0pz6 | 586 | xrp2024:1;xrp2025:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.572 | 0.132 | 0.730 |
| dio_1lsu | 566 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.551 | 0.155 | 0.712 |
| dio_17ct | 550 | xrp2024:1;xrp2025:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.560 | 0.150 | 0.717 |
| dio_0obq | 542 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.542 | 0.161 | 0.706 |
| dio_1q85 | 526 | xrp2024:1;xrp2025:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.551 | 0.161 | 0.709 |
| dio_0tay | 470 | xrp2025:1;xrp2024:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.562 | 0.141 | 0.721 |
| dio_09bn | 444 | xrp2024:1;xrp2025:1 | tragende_rekopplung | 1.000 | weltuebergreifend_feldstabil | 0.568 | 0.129 | 0.729 |

## Stärkste Familien pro Welt/Feldklasse

| holdout_label | symbol_family | field_contact_class | events | distinct_symbols | top_symbols | avg_carry | avg_strain | avg_rekopplung |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| xrp2025 | dio_104t | tragende_rekopplung | 1742 | 1 | dio_104t4us:1742 | 0.578 | 0.150 | 0.725 |
| xrp2024 | dio_104t | tragende_rekopplung | 1638 | 1 | dio_104t4us:1638 | 0.577 | 0.150 | 0.724 |
| xrp2025 | dio_155c | tragende_rekopplung | 990 | 1 | dio_155c3g6:990 | 0.564 | 0.160 | 0.716 |
| xrp2024 | dio_155c | tragende_rekopplung | 882 | 1 | dio_155c3g6:882 | 0.562 | 0.160 | 0.715 |
| xrp2025 | dio_0m9z | tragende_rekopplung | 874 | 1 | dio_0m9zys3:874 | 0.559 | 0.167 | 0.709 |
| xrp2024 | dio_0m9z | tragende_rekopplung | 860 | 1 | dio_0m9zys3:860 | 0.558 | 0.167 | 0.710 |
| xrp2025 | dio_0h9h | tragende_rekopplung | 686 | 1 | dio_0h9h06p:686 | 0.574 | 0.140 | 0.727 |
| xrp2024 | dio_0h9h | tragende_rekopplung | 632 | 1 | dio_0h9h06p:632 | 0.572 | 0.139 | 0.726 |
| xrp2025 | dio_0l7p | tragende_rekopplung | 526 | 1 | dio_0l7pvdk:526 | 0.576 | 0.133 | 0.729 |
| xrp2024 | dio_0l7p | tragende_rekopplung | 520 | 1 | dio_0l7pvdk:520 | 0.574 | 0.133 | 0.729 |
| xrp2024 | dio_14wj | tragende_rekopplung | 494 | 1 | dio_14wjmk5:494 | 0.577 | 0.127 | 0.733 |
| xrp2025 | dio_14wj | tragende_rekopplung | 470 | 1 | dio_14wjmk5:470 | 0.578 | 0.127 | 0.732 |
| xrp2025 | dio_00ly | tragende_rekopplung | 454 | 1 | dio_00lyjkf:454 | 0.569 | 0.136 | 0.726 |
| xrp2024 | dio_00ly | tragende_rekopplung | 398 | 1 | dio_00lyjkf:398 | 0.567 | 0.136 | 0.725 |
| xrp2025 | dio_1pij | tragende_rekopplung | 392 | 1 | dio_1pij39c:392 | 0.534 | 0.179 | 0.697 |
| xrp2024 | dio_00ja | tragende_rekopplung | 362 | 1 | dio_00jaski:362 | 0.552 | 0.162 | 0.705 |
| xrp2024 | dio_1ewh | tragende_rekopplung | 340 | 1 | dio_1ewh8ej:340 | 0.557 | 0.148 | 0.715 |
| xrp2024 | dio_0pz6 | tragende_rekopplung | 324 | 1 | dio_0pz659c:324 | 0.572 | 0.132 | 0.730 |

## Lesung

Wenn eine neue Welt keine alte Syntax wiederholt, aber eigene Syntaxfamilien in stabiler Feldklasse ausbildet, ist das ein anderer Reifeschritt: Nicht Erinnerung als Kopie, sondern neue Bedeutung aus ähnlicher Feldwirkung.

Wichtig ist die Grenze: Diese Familien zeigen nur wiederkehrende Feldnähe innerhalb XRP. Erst wenn dieselben Familien oder verwandte Familien in weiteren Welten anschließen, entsteht daraus eine belastbarere Vorwahrnehmungsrolle.

## Grenze

Keine Handlung, keine Richtung, kein Gate. Die Auswertung beschreibt nur, ob Feldverfügbarkeit in neue Syntaxnähe übergeht.
