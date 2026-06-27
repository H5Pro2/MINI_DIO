# MCM-Verdichtungszonen Reproduktion

## Zweck

Diese Diagnose vergleicht zwei Verdichtungszonen-Laeufe.
Sie prueft, ob die Zonenstruktur reproduziert wird oder ob sie an eine einzelne Debuggruppe gebunden ist.

Die Diagnose ist passiv: kein Gate, keine Handlung, keine Runtime-Regel.

## Klassenvergleich

| Verdichtungszone | BASIS_854 | WEITERE_865 | Differenz |
|---|---:|---:|---:|
| driftzone | 30 | 20 | -10 |
| hoeherer_cluster_uebergang | 23 | 22 | -1 |
| junge_spur | 82 | 73 | -9 |
| offene_bedeutungszone | 16 | 13 | -3 |
| randnahe_verdichtung | 4 | 6 | +2 |
| rekopplungszone | 39 | 35 | -4 |
| stabile_bedeutungsinsel | 23 | 24 | +1 |

## Token-Stabilitaet

- Gemeinsame Tokens gesamt: `103`
- Tokens mit gleicher Verdichtungszone: `45`
- Tokens mit wechselnder Verdichtungszone: `58`
- Ueberlappung der Top-20-Tokens: `8`

## Gemeinsame Top-Tokens

| Token | Basiszone | Folgezone | Basis-Beobachtungen | Folge-Beobachtungen | Basis-Welten | Folge-Welten |
|---|---|---|---:|---:|---:|---:|
| dio_mcm_episode_0b7nep9 | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 3050 | 8503 | 3 | 3 |
| dio_mcm_episode_0e7qvj1 | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 7519 | 14002 | 3 | 6 |
| dio_mcm_episode_18l3thm | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | 598 | 1539 | 2 | 5 |
| dio_mcm_episode_1ahj81f | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 565 | 364 | 4 | 4 |
| dio_mcm_episode_1hs3jsa | hoeherer_cluster_uebergang | rekopplungszone | 612 | 532 | 2 | 1 |
| dio_mcm_episode_1joiyc3 | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 4629 | 5826 | 3 | 7 |
| dio_mcm_episode_1jwnjz4 | stabile_bedeutungsinsel | rekopplungszone | 471 | 507 | 2 | 1 |
| dio_mcm_episode_1q3us3f | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 1093 | 1627 | 3 | 3 |

## Befund

Die Klassenverteilung reproduziert sich deutlich: junge Spuren bleiben die groesste Gruppe, danach folgen Rekopplungszonen, Driftzonen, stabile Bedeutungsinseln, hoehere Clusteruebergaenge, offene Bedeutungszonen und wenige randnahe Verdichtungen.

Die genaue Tokenzuordnung kann wechseln. Das ist fachlich wichtig: MINI_DIO reproduziert nicht nur starre Namen, sondern vor allem eine Feldordnung aus Verdichtungsrollen.

Damit wird die MCM-Lesart gestaerkt: Verdichtung ist nicht bloss Wiederholung, sondern eine reproduzierbare Rollenstruktur mit variabler Oberflaeche.

## Wie es weitergeht

Als naechstes sollte ein gezielter Blick auf die wechselnden Tokens erfolgen. Ziel: unterscheiden, ob ein Wechsel echte Drift, Weltfaerbung oder nur Oberflaechenvarianz ist.
