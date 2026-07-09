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
| junge_spur | 48 |
| rekopplungszone | 23 |
| hoeherer_cluster_uebergang | 21 |
| driftzone | 18 |
| offene_bedeutungszone | 10 |
| stabile_bedeutungsinsel | 9 |
| randnahe_verdichtung | 8 |

## Fehlende Eingaben

- `QUIET_SOL=C:\Users\TV\Desktop\MINI_DIO\debug\field_quiet_candidates_sol2025\dio_mini_lauf_2\episodes.csv`
- `QUIET_BTC=C:\Users\TV\Desktop\MINI_DIO\debug\field_quiet_candidates_btc2025\dio_mini_lauf_2\episodes.csv`
- `BTC_STRESS=C:\Users\TV\Desktop\MINI_DIO\debug\intake_memory_probe_btc2024_5m_stress_4k\dio_mini_lauf_2\episodes.csv`

## Staerkste Zonen

| Zone | Token | Beobachtungen | Welten | Rolle | Nachbarn | Zentrum | Offen | Rand | Rekopplung | Strain | Top-Next |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| driftzone | dio_mcm_episode_0q7skyc | 5 | 3 | offene_variante | 9 | 0.0000 | 1.0000 | 0.0000 | 0.6226 | 0.2324 | dio_mcm_episode_0rbnu89 |
| driftzone | dio_mcm_episode_0r1o8ja | 5 | 3 | offene_variante | 9 | 0.0000 | 1.0000 | 0.0000 | 0.6277 | 0.2183 | dio_mcm_episode_0n5sqpn |
| driftzone | dio_mcm_episode_0t1ymth | 3 | 1 | offene_variante | 2 | 0.3333 | 0.6667 | 0.0000 | 0.6335 | 0.2044 | dio_mcm_episode_0db07p4 |
| driftzone | dio_mcm_episode_0vq085e | 3 | 1 | zentrum_stabil | 2 | 0.6667 | 0.3333 | 0.0000 | 0.6448 | 0.1955 | dio_mcm_episode_085wm7v |
| driftzone | dio_mcm_episode_0yx4mnl | 3 | 1 | offene_variante | 2 | 0.3333 | 0.6667 | 0.0000 | 0.6608 | 0.1710 | dio_mcm_episode_0ndgwx3 |
| driftzone | dio_mcm_episode_180stw7 | 3 | 3 | zentrum_stabil | 5 | 1.0000 | 0.0000 | 0.0000 | 0.6754 | 0.1732 | dio_mcm_episode_17qt878 |
| driftzone | dio_mcm_episode_19g1diz | 3 | 3 | zentrum_stabil | 6 | 1.0000 | 0.0000 | 0.0000 | 0.6728 | 0.1557 | dio_mcm_episode_0v93uai |
| driftzone | dio_mcm_episode_00i7zy5 | 2 | 2 | offene_variante | 3 | 0.5000 | 0.5000 | 0.0000 | 0.6541 | 0.1793 | dio_mcm_episode_0393v08 |
| driftzone | dio_mcm_episode_0i2iiq6 | 2 | 1 | offene_variante | 2 | 0.5000 | 0.5000 | 0.0000 | 0.6625 | 0.1666 | dio_mcm_episode_1x5cw2v |
| driftzone | dio_mcm_episode_0mvjoir | 2 | 1 | offene_variante | 2 | 0.5000 | 0.5000 | 0.0000 | 0.6664 | 0.1831 | dio_mcm_episode_0l3i7ey |
| driftzone | dio_mcm_episode_0ndgwx3 | 2 | 1 | offene_variante | 2 | 0.5000 | 0.5000 | 0.0000 | 0.6856 | 0.1651 | dio_mcm_episode_0mji3u6 |
| driftzone | dio_mcm_episode_0om13wf | 2 | 2 | zentrum_stabil | 4 | 1.0000 | 0.0000 | 0.0000 | 0.6675 | 0.1725 | dio_mcm_episode_0y1i8dq |
| driftzone | dio_mcm_episode_102i30n | 2 | 1 | offene_variante | 2 | 0.5000 | 0.5000 | 0.0000 | 0.6475 | 0.1872 | dio_mcm_episode_1ovglru |
| driftzone | dio_mcm_episode_1bcj8qx | 2 | 2 | offene_variante | 3 | 0.5000 | 0.5000 | 0.0000 | 0.6583 | 0.1997 | dio_mcm_episode_0z748ck |
| driftzone | dio_mcm_episode_1ffzhaj | 2 | 1 | spannungsrand_kippnaehe | 2 | 0.5000 | 0.0000 | 0.5000 | 0.6209 | 0.2408 | dio_mcm_episode_0t1ymth |
| driftzone | dio_mcm_episode_1iq1hgz | 2 | 2 | offene_variante | 4 | 0.0000 | 1.0000 | 0.0000 | 0.6068 | 0.2410 | dio_mcm_episode_0om13wf |
| driftzone | dio_mcm_episode_1t42af6 | 2 | 1 | zentrum_stabil | 2 | 0.5000 | 0.5000 | 0.0000 | 0.6559 | 0.1937 | dio_mcm_episode_1joiyc3 |
| driftzone | dio_mcm_episode_1xp8o2t | 2 | 1 | zentrum_stabil | 3 | 0.5000 | 0.5000 | 0.0000 | 0.6367 | 0.2051 | dio_mcm_episode_1ehj34s |
| hoeherer_cluster_uebergang | dio_mcm_episode_1joiyc3 | 424 | 2 | zentrum_stabil | 4 | 0.7759 | 0.2170 | 0.0071 | 0.6814 | 0.1624 | dio_mcm_episode_0db07p4 |
| hoeherer_cluster_uebergang | dio_mcm_episode_0mji3u6 | 123 | 3 | zentrum_stabil | 6 | 0.6829 | 0.3008 | 0.0163 | 0.6826 | 0.1655 | dio_mcm_episode_0e7qvj1 |
| hoeherer_cluster_uebergang | dio_mcm_episode_0jbl5pq | 28 | 4 | zentrum_stabil | 6 | 0.6071 | 0.3929 | 0.0000 | 0.6903 | 0.1648 | dio_mcm_episode_0qzjuvj |
| hoeherer_cluster_uebergang | dio_mcm_episode_0aztxel | 11 | 3 | zentrum_stabil | 7 | 0.7273 | 0.2727 | 0.0000 | 0.6873 | 0.1707 | dio_mcm_episode_0jbl5pq |
| hoeherer_cluster_uebergang | dio_mcm_episode_0hjnwsk | 8 | 4 | zentrum_stabil | 4 | 0.7500 | 0.2500 | 0.0000 | 0.7063 | 0.1388 | dio_mcm_episode_0qzjuvj |
| hoeherer_cluster_uebergang | dio_mcm_episode_0l3i7ey | 8 | 4 | zentrum_stabil | 7 | 0.7500 | 0.2500 | 0.0000 | 0.6987 | 0.1552 | dio_mcm_episode_0aztxel |
| hoeherer_cluster_uebergang | dio_mcm_episode_07llqq8 | 7 | 2 | zentrum_stabil | 5 | 0.5714 | 0.1429 | 0.2857 | 0.6457 | 0.2087 | dio_mcm_episode_01yulb6 |
| hoeherer_cluster_uebergang | dio_mcm_episode_0y1i8dq | 7 | 3 | zentrum_stabil | 9 | 0.7143 | 0.2857 | 0.0000 | 0.6663 | 0.1717 | dio_mcm_episode_0ultars |
| hoeherer_cluster_uebergang | dio_mcm_episode_0ultars | 6 | 2 | offene_variante | 5 | 0.3333 | 0.6667 | 0.0000 | 0.6516 | 0.1898 | dio_mcm_episode_0ne8zu9 |
| hoeherer_cluster_uebergang | dio_mcm_episode_0v93uai | 6 | 3 | zentrum_stabil | 7 | 0.6667 | 0.3333 | 0.0000 | 0.6580 | 0.1824 | dio_mcm_episode_0jbl5pq |
| hoeherer_cluster_uebergang | dio_mcm_episode_1rkfb77 | 6 | 2 | offene_variante | 4 | 0.5000 | 0.5000 | 0.0000 | 0.6569 | 0.1850 | dio_mcm_episode_1u741ze |
| hoeherer_cluster_uebergang | dio_mcm_episode_1u741ze | 5 | 2 | zentrum_stabil | 4 | 0.6000 | 0.4000 | 0.0000 | 0.6604 | 0.1867 | dio_mcm_episode_1rylps5 |
| hoeherer_cluster_uebergang | dio_mcm_episode_0dsrwv5 | 4 | 2 | zentrum_stabil | 4 | 0.7500 | 0.2500 | 0.0000 | 0.6594 | 0.1713 | dio_mcm_episode_0aj06nw |
| hoeherer_cluster_uebergang | dio_mcm_episode_0n5sqpn | 4 | 3 | offene_variante | 5 | 0.5000 | 0.5000 | 0.0000 | 0.6937 | 0.1603 | dio_mcm_episode_0lne9ax |
| hoeherer_cluster_uebergang | dio_mcm_episode_1ehj34s | 4 | 2 | zentrum_stabil | 4 | 0.7500 | 0.2500 | 0.0000 | 0.6558 | 0.1848 | dio_mcm_episode_0z748ck |
| hoeherer_cluster_uebergang | dio_mcm_episode_1i31hl0 | 4 | 2 | offene_variante | 6 | 0.2500 | 0.7500 | 0.0000 | 0.6525 | 0.2027 | dio_mcm_episode_00yl137 |
| hoeherer_cluster_uebergang | dio_mcm_episode_0ifxej6 | 3 | 3 | zentrum_stabil | 6 | 0.6667 | 0.3333 | 0.0000 | 0.6369 | 0.2131 | dio_mcm_episode_19g1diz |
| hoeherer_cluster_uebergang | dio_mcm_episode_0ppr02l | 3 | 2 | zentrum_stabil | 4 | 0.6667 | 0.3333 | 0.0000 | 0.6645 | 0.1661 | dio_mcm_episode_0y1i8dq |
| hoeherer_cluster_uebergang | dio_mcm_episode_0rbnu89 | 3 | 3 | offene_variante | 5 | 0.3333 | 0.6667 | 0.0000 | 0.6261 | 0.2247 | dio_mcm_episode_1iq1hgz |
| hoeherer_cluster_uebergang | dio_mcm_episode_0ybhu2p | 3 | 2 | offene_variante | 4 | 0.3333 | 0.6667 | 0.0000 | 0.6665 | 0.1905 | dio_mcm_episode_0y1i8dq |
| hoeherer_cluster_uebergang | dio_mcm_episode_0q7j4gf | 2 | 2 | offene_variante | 4 | 0.5000 | 0.5000 | 0.0000 | 0.6386 | 0.2096 | dio_mcm_episode_0n5sqpn |
| junge_spur | dio_mcm_episode_00yl137 | 1 | 1 | offene_variante | 2 | 0.0000 | 1.0000 | 0.0000 | 0.6859 | 0.1754 | dio_mcm_episode_0ultars |

## Staerkste Uebergaenge

| Von | Nach | Anzahl |
|---|---|---:|
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1hdpu9s | 22 |
| dio_mcm_episode_1hdpu9s | dio_mcm_episode_0e7qvj1 | 21 |
| dio_mcm_episode_0z748ck | dio_mcm_episode_0e7qvj1 | 15 |
| dio_mcm_episode_0qzjuvj | dio_mcm_episode_0z748ck | 13 |
| dio_mcm_episode_1ahj81f | dio_mcm_episode_1jx2k4i | 12 |
| dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | 11 |
| dio_mcm_episode_1jx2k4i | dio_mcm_episode_1ahj81f | 11 |
| dio_mcm_episode_0mji3u6 | dio_mcm_episode_0e7qvj1 | 10 |
| dio_mcm_episode_1hdpu9s | dio_mcm_episode_1q3us3f | 10 |
| dio_mcm_episode_1q3us3f | dio_mcm_episode_1hdpu9s | 10 |
| dio_mcm_episode_0lne9ax | dio_mcm_episode_0jbl5pq | 5 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 5 |
| dio_mcm_episode_1hdpu9s | dio_mcm_episode_1rxdw4p | 5 |
| dio_mcm_episode_1rxdw4p | dio_mcm_episode_1hdpu9s | 5 |
| dio_mcm_episode_1rxdw4p | dio_mcm_episode_0lfde2c | 5 |
| dio_mcm_episode_0lfde2c | dio_mcm_episode_1rxdw4p | 5 |
| dio_mcm_episode_0db07p4 | dio_mcm_episode_1joiyc3 | 4 |
| dio_mcm_episode_1joiyc3 | dio_mcm_episode_0db07p4 | 3 |
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_19cadje | 3 |
| dio_mcm_episode_0l3i7ey | dio_mcm_episode_0aztxel | 3 |

## Befund

Verdichtung erscheint nicht als einzelner Absolutwert.
Sie entsteht aus Wiederkehr, Rollenanteil, Nachbarschaft, Rekopplung, Strain und Weltuebergreifung.

Damit passt die Diagnose zum Theorieanker der MCM-Verdichtung: Eine starke Innenfeldspur kann stabil bleiben, driften, randnah werden, rekoppeln oder als Uebergang in eine groessere Clusterordnung wirken.

Wichtig: Diese Zonen sind Lesarten der vorhandenen Feldorganisation. Sie schreiben MINI_DIO keine Form vor.

## Wie es weitergeht

Als naechstes sollte die Verdichtungszonen-Matrix gegen eine frische Weltgruppe laufen. Ziel: pruefen, ob dieselben Zonen wiederkehren oder ob neue Uebergangscluster entstehen.
