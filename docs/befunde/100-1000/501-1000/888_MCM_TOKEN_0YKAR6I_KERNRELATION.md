# MCM-Token Kernrelation: 0ykar6i

## Zweck

Diese Diagnose legt einen isolierten Token gegen den zentralen Brueckenkern und prueft, ob er Gegenbereich, paralleler Driftpol oder Seitenphase im selben Topologieraum ist.

## Zieltoken

| Token | Pfadklasse | Bewegung | Zone vorher | Zone nachher | Rolle |
|---|---|---|---|---|---|
| `0ykar6i` | offener_driftpfad | oeffnung_oder_drift | hoeherer_cluster_uebergang | driftzone | zentrum_stabil -> zentrum_stabil |

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
| `0ykar6i -> 0ykar6i` | 3440 |
| `0ykar6i -> 0b7nep9` | 36 |
| `0b7nep9 -> 0ykar6i` | 36 |
| `0b7nep9 -> 0b7nep9` | 8 |
| `0geqqo3 -> 0ykar6i` | 8 |
| `0ykar6i -> 0geqqo3` | 8 |
| `0ykar6i -> 0ybr5e3` | 6 |
| `0ybr5e3 -> 0ykar6i` | 6 |
| `0ybr5e3 -> 0ybr5e3` | 3 |
| `1qqnvqf -> 0ykar6i` | 2 |
| `0ykar6i -> 1pmt8u2` | 1 |
| `0ykar6i -> -` | 1 |

## Brueckennahe Kopplung

| Relation | Nachbar | Klasse | Bewegung | Kontakte |
|---|---|---|---|---:|
| exit | `0b7nep9` | brueckenpfad | stabil | 44 |
| entry | `0b7nep9` | brueckenpfad | stabil | 44 |

## Interpretation

Der Token ist kein direkter Gegenpol des zentralen Brueckenkerns.
Er koppelt indirekt ueber andere Brueckenpfade, besonders ueber brueckennahe Nachbarn.

Damit wirkt er eher wie eine lange Seitenphase im selben Topologieraum als wie ein separater Gegenbereich.

Wichtig:

Wenn ein Token von `brueckenpfad` zu `offener_driftpfad` wechselt, kann das eine Feldoeffnung aus einer Brueckenlage heraus bedeuten.
Das ist fachlich anders als chaotischer Rand: es ist eher eine gehaltene Eigenphase, die aus dem Uebergangsraum heraus driftet.

## Wie es weitergeht

Als naechstes sollte der wichtigste Vermittler `0b7nep9` isoliert werden. Ziel: pruefen, ob er der eigentliche Anschluss zwischen Brueckenkern und Drift-Eigenphase ist.