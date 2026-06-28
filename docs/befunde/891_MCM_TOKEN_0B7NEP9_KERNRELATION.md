# MCM-Token Kernrelation: 0b7nep9

## Zweck

Diese Diagnose legt einen isolierten Token gegen den zentralen Brueckenkern und prueft, ob er Gegenbereich, paralleler Driftpol oder Seitenphase im selben Topologieraum ist.

## Zieltoken

| Token | Pfadklasse | Bewegung | Zone vorher | Zone nachher | Rolle |
|---|---|---|---|---|---|
| `0b7nep9` | brueckenpfad | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | zentrum_stabil -> zentrum_stabil |

## Zentraler Brueckenkern

| Token | Pfadklasse | Bewegung | Zone vorher | Zone nachher | Rolle |
|---|---|---|---|---|---|
| `0e7qvj1` | brueckenpfad | stabil | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | zentrum_stabil -> zentrum_stabil |
| `18l3thm` | brueckenpfad | reifung_oder_verdichtung | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | zentrum_stabil -> zentrum_stabil |

## Direkte Kopplung

Keine direkte Nachbarschaft zum zentralen Kern sichtbar.

## Staerkste Nachbarpaare

| Paar | Kontakte |
|---|---:|
| `0b7nep9 -> 0b7nep9` | 7417 |
| `0ykar6i -> 0b7nep9` | 38 |
| `0b7nep9 -> 0ykar6i` | 38 |
| `0w4x7xs -> 0b7nep9` | 9 |
| `0b7nep9 -> 0w4x7xs` | 8 |
| `0ykar6i -> 0ykar6i` | 6 |
| `1eju9g0 -> 0b7nep9` | 6 |
| `0b7nep9 -> 1eju9g0` | 6 |
| `1eju9g0 -> 1eju9g0` | 4 |
| `0b7nep9 -> 0mw7rev` | 3 |
| `01s42m6 -> 0b7nep9` | 3 |
| `0b7nep9 -> 1pmt8u2` | 1 |

## Brueckennahe Kopplung

| Relation | Nachbar | Klasse | Bewegung | Kontakte |
|---|---|---|---|---:|
| entry | `17c7qwp` | brueckenpfad | reifung_oder_verdichtung | 1 |

## Interpretation

Der Token ist kein direkter Gegenpol des zentralen Brueckenkerns.
Er koppelt indirekt ueber andere Brueckenpfade, besonders ueber brueckennahe Nachbarn.

Damit wirkt er eher wie eine lange Seitenphase im selben Topologieraum als wie ein separater Gegenbereich.

Wichtig:

Wenn ein Token von `brueckenpfad` zu `offener_driftpfad` wechselt, kann das eine Feldoeffnung aus einer Brueckenlage heraus bedeuten.
Das ist fachlich anders als chaotischer Rand: es ist eher eine gehaltene Eigenphase, die aus dem Uebergangsraum heraus driftet.

## Wie es weitergeht

Als naechstes sollte die Kette `zentraler Brueckenkern -> 0b7nep9 -> 0ykar6i` als Topologiepfad zusammengefasst werden.
Ziel: klaeren, ob hier ein vermittelter Seitenarm oder eine zweite Brueckenordnung entsteht.
