# 2048 - Weltübergreifende Syntaxfamilien-Überlappung

## Zweck

Diese Auswertung vergleicht die neue XRP-Syntaxnähe aus 2046 mit der Multi-Welt-Syntaxnähe aus 2047. Geprüft wird, ob Familien nur lokal entstehen oder ob dieselben Familien in unterschiedlichen Weltspannungen wieder auftauchen.

## Übersicht

- XRP-Syntaxfamilien: `877`
- Multi-Syntaxfamilien: `539`
- gemeinsame Familien: `419`
- Jaccard-Überlappung: `0.420`
- gemeinsame Familien mit gleicher Feldklasse: `390`
- gemeinsame Familien mit gleicher Reifung: `320`
- XRP-only: `458`
- Multi-only: `120`
- Feldklassen in gemeinsamen Familien: `{'tragende_rekopplung': 389, 'offene_rekopplung': 24, 'spannungsnahe_oeffnung': 4, 'getragen_offen': 2}`

## Stärkste gemeinsame Familien

| symbol_family | xrp_events | multi_events | xrp_field | multi_field | same_field | xrp_reifung | multi_reifung | same_reifung | xrp_mcm | multi_mcm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dio_104t | 3380 | 2412 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.577/0.150/0.724 | 0.588/0.163/0.726 |
| dio_155c | 1872 | 1208 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.563/0.160/0.716 | 0.580/0.171/0.721 |
| dio_0m9z | 1734 | 1191 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.558/0.167/0.710 | 0.575/0.181/0.713 |
| dio_0l7p | 1046 | 2063 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.575/0.133/0.729 | 0.594/0.151/0.733 |
| dio_0h9h | 1318 | 1012 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.573/0.140/0.726 | 0.590/0.157/0.730 |
| dio_14wj | 964 | 1696 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.577/0.127/0.733 | 0.599/0.143/0.739 |
| dio_00ly | 852 | 619 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.568/0.136/0.726 | 0.587/0.156/0.730 |
| dio_1lsu | 566 | 527 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.551/0.155/0.712 | 0.576/0.172/0.719 |
| dio_0pz6 | 586 | 486 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.572/0.132/0.730 | 0.592/0.152/0.733 |
| dio_0dd2 | 616 | 431 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.571/0.136/0.729 | 0.587/0.156/0.732 |
| dio_06er | 370 | 565 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.574/0.120/0.736 | 0.597/0.143/0.741 |
| dio_17ct | 550 | 349 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.560/0.150/0.717 | 0.578/0.167/0.722 |
| dio_06s7 | 342 | 604 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.566/0.122/0.730 | 0.594/0.145/0.736 |
| dio_0tay | 470 | 334 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.562/0.141/0.721 | 0.581/0.163/0.725 |
| dio_1jc2 | 308 | 390 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.568/0.113/0.733 | 0.597/0.137/0.740 |
| dio_1kpz | 290 | 601 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.564/0.120/0.730 | 0.595/0.145/0.737 |
| dio_09bn | 444 | 283 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.568/0.129/0.729 | 0.586/0.149/0.733 |
| dio_1fll | 282 | 501 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.576/0.109/0.741 | 0.599/0.131/0.747 |
| dio_1r55 | 278 | 349 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.545/0.149/0.713 | 0.572/0.168/0.722 |
| dio_1q85 | 526 | 276 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.551/0.161/0.709 | 0.568/0.179/0.712 |
| dio_0nlj | 248 | 292 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.568/0.114/0.735 | 0.594/0.139/0.740 |
| dio_00ja | 684 | 242 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.551/0.163/0.704 | 0.562/0.183/0.702 |
| dio_01hu | 234 | 450 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.553/0.134/0.721 | 0.581/0.155/0.730 |
| dio_0kx9 | 234 | 380 | tragende_rekopplung | tragende_rekopplung | 1 | weltuebergreifend_feldstabil | weltuebergreifend_feldstabil | 1 | 0.565/0.113/0.732 | 0.596/0.137/0.740 |

## Lesung

Der Befund trennt zwei Dinge: lokale Syntaxbildung und weltübergreifende Feldsyntax. Wenn dieselbe Familie in XRP und in BTC/DOGE/PAXG mit gleicher Feldklasse auftaucht, spricht das für eine wiederkehrende innere Feldform, nicht nur für assetgebundene Oberfläche.

Die Jaccard-Überlappung ist dabei bewusst konservativ: Sie misst nur exakte Familiennamen. Bedeutungsnähe ohne identischen Namen wird hier noch nicht gezählt.

## Grenze

Auch diese Überlappung ist passiv. Sie beweist keine Handlung und keine Absicht. Sie zeigt, ob Syntaxfamilien über unterschiedliche Weltkontakte hinweg feldnah wiederkehren.
