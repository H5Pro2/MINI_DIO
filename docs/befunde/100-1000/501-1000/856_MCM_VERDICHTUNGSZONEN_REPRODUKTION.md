# MCM-Verdichtungszonen Reproduktion

## Zweck

Diese Diagnose vergleicht zwei Verdichtungszonen-Laeufe.
Sie prueft, ob die Zonenstruktur reproduziert wird oder ob sie an eine einzelne Debuggruppe gebunden ist.

Die Diagnose ist passiv: kein Gate, keine Handlung, keine Runtime-Regel.

## Klassenvergleich

| Verdichtungszone | 854_Ausgangsgruppe | 855_Frische_Weltgruppe | Differenz |
|---|---:|---:|---:|
| driftzone | 30 | 38 | +8 |
| hoeherer_cluster_uebergang | 23 | 19 | -4 |
| junge_spur | 82 | 74 | -8 |
| offene_bedeutungszone | 16 | 17 | +1 |
| randnahe_verdichtung | 4 | 4 | +0 |
| rekopplungszone | 39 | 41 | +2 |
| stabile_bedeutungsinsel | 23 | 26 | +3 |

## Token-Stabilitaet

- Gemeinsame Tokens gesamt: `142`
- Tokens mit gleicher Verdichtungszone: `84`
- Tokens mit wechselnder Verdichtungszone: `58`
- Ueberlappung der Top-20-Tokens: `15`

## Gemeinsame Top-Tokens

| Token | Basiszone | Folgezone | Basis-Beobachtungen | Folge-Beobachtungen | Basis-Welten | Folge-Welten |
|---|---|---|---:|---:|---:|---:|
| dio_mcm_episode_08lp0ua | rekopplungszone | rekopplungszone | 3269 | 3263 | 2 | 2 |
| dio_mcm_episode_0b7nep9 | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 3050 | 4573 | 3 | 3 |
| dio_mcm_episode_0e7qvj1 | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 7519 | 9806 | 3 | 5 |
| dio_mcm_episode_0qvodoj | rekopplungszone | rekopplungszone | 6302 | 6308 | 3 | 3 |
| dio_mcm_episode_0wjn8vm | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 2172 | 2166 | 2 | 2 |
| dio_mcm_episode_0ybr5e3 | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 1537 | 3868 | 1 | 1 |
| dio_mcm_episode_0ykar6i | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 1351 | 3830 | 2 | 3 |
| dio_mcm_episode_14coypf | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | 1584 | 1234 | 2 | 1 |
| dio_mcm_episode_1ahj81f | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 565 | 850 | 4 | 5 |
| dio_mcm_episode_1engxbn | rekopplungszone | rekopplungszone | 1768 | 1774 | 2 | 2 |
| dio_mcm_episode_1joiyc3 | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | 4629 | 4604 | 3 | 6 |
| dio_mcm_episode_1jwnjz4 | stabile_bedeutungsinsel | stabile_bedeutungsinsel | 471 | 514 | 2 | 2 |
| dio_mcm_episode_1q3us3f | stabile_bedeutungsinsel | rekopplungszone | 1093 | 464 | 3 | 3 |
| dio_mcm_episode_1v8o9kh | rekopplungszone | rekopplungszone | 3207 | 3207 | 3 | 3 |
| dio_mcm_episode_1xx3u1e | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | 2964 | 1854 | 2 | 3 |

## Befund

Die Klassenverteilung reproduziert sich deutlich: junge Spuren bleiben die groesste Gruppe, danach folgen Rekopplungszonen, Driftzonen, stabile Bedeutungsinseln, hoehere Clusteruebergaenge, offene Bedeutungszonen und wenige randnahe Verdichtungen.

Die genaue Tokenzuordnung kann wechseln. Das ist fachlich wichtig: MINI_DIO reproduziert nicht nur starre Namen, sondern vor allem eine Feldordnung aus Verdichtungsrollen.

Damit wird die MCM-Lesart gestaerkt: Verdichtung ist nicht bloss Wiederholung, sondern eine reproduzierbare Rollenstruktur mit variabler Oberflaeche.

## Wie es weitergeht

Als naechstes sollte ein gezielter Blick auf die wechselnden Tokens erfolgen. Ziel: unterscheiden, ob ein Wechsel echte Drift, Weltfaerbung oder nur Oberflaechenvarianz ist.
