# MCM-Brueckenanker Pruefung: 0b7nep9

## Zweck

Diese Diagnose prueft, ob ein starker Bruecken-Token als Brueckenkern, Anschlussanker oder lokaler Vermittler zu lesen ist.

## Tokenprofil

| Token | Pfadklasse | Bewegung | Zone vorher | Zone nachher | Rolle |
|---|---|---|---|---|---|
| `0b7nep9` | brueckenpfad | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | zentrum_stabil -> zentrum_stabil |

## Netzwerkbefund

- Ankerklasse: `starker_anschlussanker`
- Gewichtete Kantenkontakte: `35`
- Gewichtete mittlere Dauer: `470.94`
- Kantentypen: `aussen_zu_bruecke:6; bruecke_zu_aussen:8`
- Relationen: `eintritt:6; austritt:8`
- In Kernpaaren aus 876: `nein`

## Staerkste Kanten

| Richtung | Nachbar | Relation | Kantentyp | Gewicht | Welten | Dauer | Phase |
|---|---|---|---|---:|---:|---:|---|
| eingehend | `00nzcuc` | eintritt | aussen_zu_bruecke | 8 | 2 | 232.25 | oeffnend_belastender_austritt |
| ausgehend | `00nzcuc` | austritt | bruecke_zu_aussen | 6 | 2 | 3.17 | gemischter_austritt |
| ausgehend | `0w4x7xs` | austritt | bruecke_zu_aussen | 5 | 1 | 114.40 | rekoppelnder_austritt |
| eingehend | `0w4x7xs` | eintritt | aussen_zu_bruecke | 4 | 1 | 134.50 | gemischter_austritt |
| eingehend | `0ykar6i` | eintritt | aussen_zu_bruecke | 2 | 2 | 1036.00 | oeffnend_belastender_austritt |
| eingehend | `1f4jh6c` | eintritt | aussen_zu_bruecke | 2 | 1 | 14.50 | rekoppelnder_austritt |
| eingehend | `17c7qwp` | eintritt | aussen_zu_bruecke | 1 | 1 | 1972.00 | rekoppelnder_austritt |
| eingehend | `1fej2vb` | eintritt | aussen_zu_bruecke | 1 | 1 | 2034.00 | gemischter_austritt |
| ausgehend | `0fljihc` | austritt | bruecke_zu_aussen | 1 | 1 | 931.00 | oeffnend_belastender_austritt |
| ausgehend | `0mm85pw` | austritt | bruecke_zu_aussen | 1 | 1 | 1284.00 | oeffnend_belastender_austritt |
| ausgehend | `0mw7rev` | austritt | bruecke_zu_aussen | 1 | 1 | 1141.00 | oeffnend_belastender_austritt |
| ausgehend | `0rz7ra9` | austritt | bruecke_zu_aussen | 1 | 1 | 2034.00 | gemischter_austritt |
| ausgehend | `0tosxof` | austritt | bruecke_zu_aussen | 1 | 1 | 1972.00 | rekoppelnder_austritt |
| ausgehend | `0ykar6i` | austritt | bruecke_zu_aussen | 1 | 1 | 27.00 | rekoppelnder_austritt |

## Interpretation

Der Token wirkt nicht wie ein Brueckenkern im Sinne der Paarbildung aus 876.
Er wirkt als starker Anschlussanker: stabiler Brueckenpfad mit mehreren Ein- und Austrittskanten zu nichtzentralen Feldbereichen.

Fachlich ist das relevant:

Ein Anschlussanker kann eine Drift-Eigenphase tragen, ohne selbst Teil des zentralen Brueckenkerns zu sein.
Damit entsteht eine Zwischenebene zwischen Brueckenkern und offener Drift.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob weitere starke Anschlussanker existieren oder ob `0b7nep9` in dieser Rolle singulaer bleibt.