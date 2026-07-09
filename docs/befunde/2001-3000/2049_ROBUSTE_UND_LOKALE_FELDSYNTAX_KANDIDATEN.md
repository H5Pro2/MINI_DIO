# 2049 - Robuste und lokale Feldsyntax-Kandidaten

## Zweck

Diese Auswertung trennt die gemeinsame Feldsyntax aus 2048 von lokalen Syntaxinseln. Damit wird sichtbar, welche Familien als robuste Feldsyntax-Kandidaten gelten und welche Familien zunächst nur lokal oder jung bleiben.

Die Karte bleibt passiv. Sie gibt MINI_DIO keine Handlung, sondern beschreibt nur Reife und Reichweite einer Syntaxfamilie.

## Übersicht

- Kandidaten gesamt: `997`
- Klassenverteilung: `{'gemeinsame_feldsyntax_offen': 121, 'gemeinsame_syntax_verschoben': 29, 'lokale_junge_syntaxinsel': 578, 'robuste_feldsyntax': 269}`

## Klassen

| candidate_class | families | present_in | fields | max_xrp_events | max_multi_events |
| --- | --- | --- | --- | --- | --- |
| gemeinsame_feldsyntax_offen | 121 | xrp_and_multi:121 | tragende_rekopplung:105;offene_rekopplung:16 | 118 | 110 |
| gemeinsame_syntax_verschoben | 29 | xrp_and_multi:29 | tragende_rekopplung:17;offene_rekopplung:6;spannungsnahe_oeffnung:4;getragen_offen:2 | 88 | 10 |
| lokale_junge_syntaxinsel | 578 | xrp_only:458;multi_only:120 | tragende_rekopplung:277;offene_rekopplung:196;spannungsnahe_oeffnung:92;offener_feldkontakt:13 | 78 | 27 |
| robuste_feldsyntax | 269 | xrp_and_multi:269 | tragende_rekopplung:267;offene_rekopplung:2 | 3380 | 2412 |

## Stärkste Kandidaten

| symbol_family | candidate_class | present_in | same_field | same_reifung | xrp_events | multi_events | xrp_field | multi_field | xrp_mcm | multi_mcm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dio_104t | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 3380 | 2412 | tragende_rekopplung | tragende_rekopplung | 0.577/0.150/0.724 | 0.588/0.163/0.726 |
| dio_0l7p | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 1046 | 2063 | tragende_rekopplung | tragende_rekopplung | 0.575/0.133/0.729 | 0.594/0.151/0.733 |
| dio_155c | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 1872 | 1208 | tragende_rekopplung | tragende_rekopplung | 0.563/0.160/0.716 | 0.580/0.171/0.721 |
| dio_0m9z | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 1734 | 1191 | tragende_rekopplung | tragende_rekopplung | 0.558/0.167/0.710 | 0.575/0.181/0.713 |
| dio_14wj | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 964 | 1696 | tragende_rekopplung | tragende_rekopplung | 0.577/0.127/0.733 | 0.599/0.143/0.739 |
| dio_0h9h | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 1318 | 1012 | tragende_rekopplung | tragende_rekopplung | 0.573/0.140/0.726 | 0.590/0.157/0.730 |
| dio_00ly | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 852 | 619 | tragende_rekopplung | tragende_rekopplung | 0.568/0.136/0.726 | 0.587/0.156/0.730 |
| dio_1pij | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 708 | 29 | tragende_rekopplung | tragende_rekopplung | 0.533/0.179/0.696 | 0.464/0.196/0.670 |
| dio_00ja | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 684 | 242 | tragende_rekopplung | tragende_rekopplung | 0.551/0.163/0.704 | 0.562/0.183/0.702 |
| dio_1ewh | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 642 | 150 | tragende_rekopplung | tragende_rekopplung | 0.556/0.149/0.715 | 0.559/0.168/0.710 |
| dio_0dd2 | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 616 | 431 | tragende_rekopplung | tragende_rekopplung | 0.571/0.136/0.729 | 0.587/0.156/0.732 |
| dio_06s7 | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 342 | 604 | tragende_rekopplung | tragende_rekopplung | 0.566/0.122/0.730 | 0.594/0.145/0.736 |
| dio_1kpz | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 290 | 601 | tragende_rekopplung | tragende_rekopplung | 0.564/0.120/0.730 | 0.595/0.145/0.737 |
| dio_02n3 | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 138 | 590 | tragende_rekopplung | tragende_rekopplung | 0.556/0.112/0.730 | 0.593/0.138/0.741 |
| dio_0pz6 | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 586 | 486 | tragende_rekopplung | tragende_rekopplung | 0.572/0.132/0.730 | 0.592/0.152/0.733 |
| dio_1lsu | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 566 | 527 | tragende_rekopplung | tragende_rekopplung | 0.551/0.155/0.712 | 0.576/0.172/0.719 |
| dio_06er | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 370 | 565 | tragende_rekopplung | tragende_rekopplung | 0.574/0.120/0.736 | 0.597/0.143/0.741 |
| dio_17ct | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 550 | 349 | tragende_rekopplung | tragende_rekopplung | 0.560/0.150/0.717 | 0.578/0.167/0.722 |
| dio_0obq | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 542 | 149 | tragende_rekopplung | tragende_rekopplung | 0.542/0.161/0.706 | 0.550/0.178/0.707 |
| dio_1q85 | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 526 | 276 | tragende_rekopplung | tragende_rekopplung | 0.551/0.161/0.709 | 0.568/0.179/0.712 |
| dio_1fll | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 282 | 501 | tragende_rekopplung | tragende_rekopplung | 0.576/0.109/0.741 | 0.599/0.131/0.747 |
| dio_0tay | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 470 | 334 | tragende_rekopplung | tragende_rekopplung | 0.562/0.141/0.721 | 0.581/0.163/0.725 |
| dio_03uk | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 178 | 464 | tragende_rekopplung | tragende_rekopplung | 0.485/0.221/0.658 | 0.591/0.146/0.736 |
| dio_01hu | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 234 | 450 | tragende_rekopplung | tragende_rekopplung | 0.553/0.134/0.721 | 0.581/0.155/0.730 |
| dio_09bn | robuste_feldsyntax | xrp_and_multi | 1 | 1 | 444 | 283 | tragende_rekopplung | tragende_rekopplung | 0.568/0.129/0.729 | 0.586/0.149/0.733 |

## Lesung

`robuste_feldsyntax` bedeutet: dieselbe Familie tritt in XRP und in BTC/DOGE/PAXG auf, mit gleicher Feldklasse und gleicher Reifung. Das ist der stärkste passive Kandidat für weltübergreifende Feldsyntax.

`lokale_junge_syntaxinsel` bedeutet nicht wertlos. Es heißt nur: Noch nicht weltübergreifend getragen. Diese Inseln können bei weiterer Weltzufuhr reifen, sich teilen oder verschwinden.

## Grenze

Keine Handlung, keine Richtung, kein Gate. Diese Karte ist eine passive Reife- und Reichweitenkarte der Feldsyntax.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob lokale starke Familien bei weiterer Weltzufuhr in `robuste_feldsyntax` übergehen oder ob sie asset-/weltgebundene Milieuinseln bleiben.
