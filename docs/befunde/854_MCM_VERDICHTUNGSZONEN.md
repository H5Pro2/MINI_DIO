# MCM-Verdichtungszonen

## Zweck

Diese Diagnose liest vorhandene MINI_DIO-Episoden als Verdichtungszonen.
Sie prueft, ob Feldzeichen eher stabile Inseln, Driftzonen, Randnaehe, Rekopplungszonen oder Uebergaenge in hoehere Clusterordnung bilden.

Die Diagnose ist passiv: kein Gate, keine Handlung, keine Runtime-Regel.

## Hierarchie

1. Grundfrage: Welche Verdichtungsformen bildet das MCM-Feld aus wiederkehrender Weltwirkung?
2. Unterpruefung: Welche Zeichen wirken stabil, driftend, randnah, rekoppelnd oder clusterbildend?
3. Folgeschritt: Verdichtungszonen gegen neue Welten pruefen, ohne daraus Handlung abzuleiten.

## Klassenuebersicht

| Verdichtungszone | Anzahl |
|---|---:|
| junge_spur | 82 |
| rekopplungszone | 39 |
| driftzone | 30 |
| hoeherer_cluster_uebergang | 23 |
| stabile_bedeutungsinsel | 23 |
| offene_bedeutungszone | 16 |
| randnahe_verdichtung | 4 |

## Staerkste Zonen

| Zone | Token | Beobachtungen | Welten | Rolle | Nachbarn | Zentrum | Offen | Rand | Rekopplung | Strain | Top-Next |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| driftzone | dio_mcm_episode_09rbps0 | 11 | 1 | offene_variante | 3 | 0.4545 | 0.5455 | 0.0000 | 0.6603 | 0.1787 | dio_mcm_episode_03hr8bf |
| driftzone | dio_mcm_episode_0ag2osp | 4 | 2 | zentrum_stabil | 7 | 1.0000 | 0.0000 | 0.0000 | 0.7114 | 0.1468 | dio_mcm_episode_0a6333q |
| driftzone | dio_mcm_episode_1y2gc2i | 4 | 2 | zentrum_stabil | 4 | 1.0000 | 0.0000 | 0.0000 | 0.6700 | 0.1594 | dio_mcm_episode_1y26981 |
| driftzone | dio_mcm_episode_006di8e | 3 | 1 | zentrum_stabil | 2 | 0.6667 | 0.3333 | 0.0000 | 0.6615 | 0.1679 | dio_mcm_episode_1xp8xyu |
| driftzone | dio_mcm_episode_0a6333q | 3 | 2 | offene_variante | 4 | 0.0000 | 1.0000 | 0.0000 | 0.6251 | 0.2292 | dio_mcm_episode_0iiok1d |
| driftzone | dio_mcm_episode_0e6va2r | 3 | 1 | zentrum_stabil | 2 | 0.6667 | 0.3333 | 0.0000 | 0.7161 | 0.1402 | dio_mcm_episode_1rpy7z2 |
| driftzone | dio_mcm_episode_0i7gfxw | 3 | 1 | offene_variante | 2 | 0.3333 | 0.6667 | 0.0000 | 0.6724 | 0.1725 | dio_mcm_episode_0hjnwsk |
| driftzone | dio_mcm_episode_0i8oyce | 3 | 1 | offene_variante | 4 | 0.3333 | 0.6667 | 0.0000 | 0.6982 | 0.1542 | dio_mcm_episode_0cvptbz |
| driftzone | dio_mcm_episode_0lne9ax | 3 | 2 | zentrum_stabil | 3 | 1.0000 | 0.0000 | 0.0000 | 0.7185 | 0.1247 | dio_mcm_episode_0jbl5pq |
| driftzone | dio_mcm_episode_0nj1l40 | 3 | 1 | zentrum_stabil | 2 | 0.6667 | 0.3333 | 0.0000 | 0.7027 | 0.1448 | dio_mcm_episode_0e6va2r |
| driftzone | dio_mcm_episode_0tv1tha | 3 | 1 | offene_variante | 2 | 0.3333 | 0.6667 | 0.0000 | 0.6277 | 0.2096 | dio_mcm_episode_0yk71el |
| driftzone | dio_mcm_episode_1f4jh6c | 3 | 1 | zentrum_stabil | 2 | 0.6667 | 0.3333 | 0.0000 | 0.6943 | 0.1462 | dio_mcm_episode_0b7nep9 |
| driftzone | dio_mcm_episode_1qqnvqf | 3 | 1 | zentrum_stabil | 2 | 0.6667 | 0.3333 | 0.0000 | 0.6741 | 0.1659 | dio_mcm_episode_0ykar6i |
| driftzone | dio_mcm_episode_1rpy7z2 | 3 | 1 | zentrum_stabil | 2 | 0.6667 | 0.3333 | 0.0000 | 0.7054 | 0.1441 | dio_mcm_episode_1pwdejt |
| driftzone | dio_mcm_episode_1xp8xyu | 3 | 1 | spannungsrand_kippnaehe | 2 | 0.3333 | 0.3333 | 0.3333 | 0.6294 | 0.2182 | dio_mcm_episode_1ahj81f |
| driftzone | dio_mcm_episode_1y26981 | 3 | 1 | zentrum_stabil | 2 | 0.6667 | 0.3333 | 0.0000 | 0.6522 | 0.1788 | dio_mcm_episode_17i4j9o |
| driftzone | dio_mcm_episode_0igfdmt | 2 | 2 | zentrum_stabil | 4 | 1.0000 | 0.0000 | 0.0000 | 0.6442 | 0.2053 | dio_mcm_episode_195dhqf |
| driftzone | dio_mcm_episode_0khjbll | 2 | 2 | zentrum_stabil | 4 | 1.0000 | 0.0000 | 0.0000 | 0.6873 | 0.1330 | dio_mcm_episode_13lt69z |
| driftzone | dio_mcm_episode_0ml8r41 | 2 | 1 | offene_variante | 2 | 0.5000 | 0.5000 | 0.0000 | 0.6411 | 0.2210 | dio_mcm_episode_17wwyn1 |
| driftzone | dio_mcm_episode_0mvt50o | 2 | 2 | offene_variante | 4 | 0.0000 | 1.0000 | 0.0000 | 0.6726 | 0.1825 | dio_mcm_episode_0ldht3x |
| driftzone | dio_mcm_episode_0pfredm | 2 | 1 | zentrum_stabil | 2 | 0.5000 | 0.5000 | 0.0000 | 0.6654 | 0.1777 | dio_mcm_episode_0vj3fzh |
| driftzone | dio_mcm_episode_0qhs6nb | 2 | 2 | offene_variante | 4 | 0.0000 | 1.0000 | 0.0000 | 0.6199 | 0.2194 | dio_mcm_episode_0lne9ax |
| driftzone | dio_mcm_episode_0r1o8ja | 2 | 2 | offene_variante | 4 | 0.0000 | 1.0000 | 0.0000 | 0.6399 | 0.1944 | dio_mcm_episode_0om13wf |
| driftzone | dio_mcm_episode_0tph7s0 | 2 | 2 | zentrum_stabil | 4 | 1.0000 | 0.0000 | 0.0000 | 0.7055 | 0.1458 | dio_mcm_episode_0fkg6al |
| driftzone | dio_mcm_episode_0u69u6w | 2 | 2 | zentrum_stabil | 4 | 1.0000 | 0.0000 | 0.0000 | 0.6644 | 0.1661 | dio_mcm_episode_06ccuqv |
| driftzone | dio_mcm_episode_0ybhu2p | 2 | 2 | zentrum_stabil | 3 | 1.0000 | 0.0000 | 0.0000 | 0.6843 | 0.1527 | dio_mcm_episode_0om13wf |
| driftzone | dio_mcm_episode_1eriotr | 2 | 1 | offene_variante | 3 | 0.5000 | 0.5000 | 0.0000 | 0.6490 | 0.2089 | dio_mcm_episode_07vx0iw |
| driftzone | dio_mcm_episode_1jc5z5p | 2 | 1 | zentrum_stabil | 2 | 0.5000 | 0.5000 | 0.0000 | 0.6462 | 0.1938 | dio_mcm_episode_1ovglru |
| driftzone | dio_mcm_episode_1ovglru | 2 | 2 | zentrum_stabil | 4 | 1.0000 | 0.0000 | 0.0000 | 0.6695 | 0.1600 | dio_mcm_episode_0t1ymth |
| driftzone | dio_mcm_episode_1vprn0y | 2 | 2 | offene_variante | 4 | 0.0000 | 1.0000 | 0.0000 | 0.5929 | 0.2661 | dio_mcm_episode_1uizm2j |
| hoeherer_cluster_uebergang | dio_mcm_episode_0e7qvj1 | 7519 | 3 | zentrum_stabil | 12 | 0.7598 | 0.2333 | 0.0069 | 0.7035 | 0.1542 | dio_mcm_episode_18l3thm |
| hoeherer_cluster_uebergang | dio_mcm_episode_1joiyc3 | 4629 | 3 | zentrum_stabil | 5 | 0.8194 | 0.1737 | 0.0069 | 0.6993 | 0.1532 | dio_mcm_episode_1jx2k4i |
| hoeherer_cluster_uebergang | dio_mcm_episode_0b7nep9 | 3050 | 3 | zentrum_stabil | 9 | 0.7928 | 0.2020 | 0.0052 | 0.7086 | 0.1514 | dio_mcm_episode_0ykar6i |
| hoeherer_cluster_uebergang | dio_mcm_episode_1xx3u1e | 2964 | 2 | zentrum_stabil | 5 | 0.8529 | 0.1447 | 0.0024 | 0.7196 | 0.1465 | dio_mcm_episode_0ybr5e3 |
| hoeherer_cluster_uebergang | dio_mcm_episode_0wjn8vm | 2172 | 2 | zentrum_stabil | 4 | 0.8278 | 0.1722 | 0.0000 | 0.7241 | 0.1373 | dio_mcm_episode_1engxbn |
| hoeherer_cluster_uebergang | dio_mcm_episode_0v5p8er | 2013 | 4 | zentrum_stabil | 4 | 0.8455 | 0.1515 | 0.0030 | 0.7122 | 0.1504 | dio_mcm_episode_14l8khu |
| hoeherer_cluster_uebergang | dio_mcm_episode_14coypf | 1584 | 2 | zentrum_stabil | 8 | 0.8074 | 0.1900 | 0.0025 | 0.7110 | 0.1504 | dio_mcm_episode_14l8khu |
| hoeherer_cluster_uebergang | dio_mcm_episode_0ykar6i | 1351 | 2 | zentrum_stabil | 4 | 0.8157 | 0.1813 | 0.0030 | 0.7106 | 0.1481 | dio_mcm_episode_0b7nep9 |
| hoeherer_cluster_uebergang | dio_mcm_episode_14l8khu | 906 | 3 | zentrum_stabil | 3 | 0.7693 | 0.2285 | 0.0022 | 0.7053 | 0.1557 | dio_mcm_episode_0v5p8er |
| hoeherer_cluster_uebergang | dio_mcm_episode_1hs3jsa | 612 | 2 | zentrum_stabil | 3 | 0.8676 | 0.1275 | 0.0049 | 0.7106 | 0.1492 | dio_mcm_episode_1q3us3f |

## Staerkste Uebergaenge

| Von | Nach | Anzahl |
|---|---|---:|
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 21 |
| dio_mcm_episode_18l3thm | dio_mcm_episode_0e7qvj1 | 19 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1jwnjz4 | 18 |
| dio_mcm_episode_1jwnjz4 | dio_mcm_episode_0e7qvj1 | 16 |
| dio_mcm_episode_18l3thm | dio_mcm_episode_1q3us3f | 14 |
| dio_mcm_episode_1q3us3f | dio_mcm_episode_18l3thm | 14 |
| dio_mcm_episode_0mji3u6 | dio_mcm_episode_0e7qvj1 | 13 |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_0ykar6i | 12 |
| dio_mcm_episode_1jx2k4i | dio_mcm_episode_1joiyc3 | 11 |
| dio_mcm_episode_0ykar6i | dio_mcm_episode_0b7nep9 | 11 |
| dio_mcm_episode_1xx3u1e | dio_mcm_episode_0ybr5e3 | 11 |
| dio_mcm_episode_14l8khu | dio_mcm_episode_0v5p8er | 11 |
| dio_mcm_episode_0v5p8er | dio_mcm_episode_14l8khu | 11 |
| dio_mcm_episode_1joiyc3 | dio_mcm_episode_1jx2k4i | 10 |
| dio_mcm_episode_1eju9g0 | dio_mcm_episode_0b7nep9 | 10 |
| dio_mcm_episode_0b7nep9 | dio_mcm_episode_1eju9g0 | 10 |
| dio_mcm_episode_1eju9g0 | dio_mcm_episode_0ybr5e3 | 10 |
| dio_mcm_episode_0ybr5e3 | dio_mcm_episode_1eju9g0 | 10 |
| dio_mcm_episode_0ybr5e3 | dio_mcm_episode_1xx3u1e | 10 |
| dio_mcm_episode_0ykar6i | dio_mcm_episode_0ybr5e3 | 9 |

## Befund

Verdichtung erscheint nicht als einzelner Absolutwert.
Sie entsteht aus Wiederkehr, Rollenanteil, Nachbarschaft, Rekopplung, Strain und Weltuebergreifung.

Damit passt die Diagnose zum Theorieanker der MCM-Verdichtung: Eine starke Innenfeldspur kann stabil bleiben, driften, randnah werden, rekoppeln oder als Uebergang in eine groessere Clusterordnung wirken.

Wichtig: Diese Zonen sind Lesarten der vorhandenen Feldorganisation. Sie schreiben MINI_DIO keine Form vor.

## Wie es weitergeht

Als naechstes sollte die Verdichtungszonen-Matrix gegen eine frische Weltgruppe laufen. Ziel: pruefen, ob dieselben Zonen wiederkehren oder ob neue Uebergangscluster entstehen.
