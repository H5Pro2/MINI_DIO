# MCM-Anschlussanker Unterrollen

## Zweck

Diese passive Diagnose prueft, ob die starken Anschlussanker dieselbe Feldfunktion tragen oder unterschiedliche Unterrollen ausbilden.
Sie vergleicht Kantenbreite, Dauer, Weltspanne, Ein-/Austrittsverhalten und Nachbarschaftstypen.

## Rollenvergleich

| Token | Unterrolle | Gewicht | Dauer | Ein Gewicht | Aus Gewicht | Kanten | Welten | Pfadklasse | Zone |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| `0b7nep9` | tiefer_verteilender_anschlussanker | 35 | 470.94 | 18 | 17 | 14 | 2 | brueckenpfad | hoeherer_cluster_uebergang -> hoeherer_cluster_uebergang |
| `1jx2k4i` | weltbreiter_kernnaher_inselanker | 33 | 133.18 | 16 | 17 | 2 | 5 | stabile_insel | stabile_bedeutungsinsel -> stabile_bedeutungsinsel |

## Nachbarschaft

### `0b7nep9`

- Kantentypen: `bruecke_zu_aussen:8; aussen_zu_bruecke:6`
- Austrittsphasen: `oeffnend_belastender_austritt:5; rekoppelnder_austritt:5; gemischter_austritt:4`
- Nachbar-Klassen: `schwacher_anschluss:12; lokaler_anschlussanker:2`
- Nachbar-Pfade: `-:5; rekoppelnder_pfad:3; offener_driftpfad:2; randpfad:2; brueckenpfad:1; junge_oberflaeche:1`

| Richtung | Nachbar | Nachbarrolle | Relation | Kantentyp | Gewicht | Welten | Dauer | Phase |
|---|---|---|---|---|---:|---:|---:|---|
| eingehend | `00nzcuc` | lokaler_anschlussanker / - | eintritt | aussen_zu_bruecke | 8 | 2 | 232.25 | oeffnend_belastender_austritt |
| ausgehend | `00nzcuc` | lokaler_anschlussanker / - | austritt | bruecke_zu_aussen | 6 | 2 | 3.17 | gemischter_austritt |
| ausgehend | `0w4x7xs` | schwacher_anschluss / rekoppelnder_pfad | austritt | bruecke_zu_aussen | 5 | 1 | 114.40 | rekoppelnder_austritt |
| eingehend | `0w4x7xs` | schwacher_anschluss / rekoppelnder_pfad | eintritt | aussen_zu_bruecke | 4 | 1 | 134.50 | gemischter_austritt |
| eingehend | `0ykar6i` | schwacher_anschluss / offener_driftpfad | eintritt | aussen_zu_bruecke | 2 | 2 | 1036.00 | oeffnend_belastender_austritt |
| eingehend | `1f4jh6c` | schwacher_anschluss / rekoppelnder_pfad | eintritt | aussen_zu_bruecke | 2 | 1 | 14.50 | rekoppelnder_austritt |
| eingehend | `17c7qwp` | schwacher_anschluss / brueckenpfad | eintritt | aussen_zu_bruecke | 1 | 1 | 1972.00 | rekoppelnder_austritt |
| eingehend | `1fej2vb` | schwacher_anschluss / - | eintritt | aussen_zu_bruecke | 1 | 1 | 2034.00 | gemischter_austritt |

### `1jx2k4i`

- Kantentypen: `aussen_zu_bruecke:1; bruecke_zu_aussen:1`
- Austrittsphasen: `gemischter_austritt:1; rekoppelnder_austritt:1`
- Nachbar-Klassen: `brueckenkern:2`
- Nachbar-Pfade: `brueckenpfad:2`

| Richtung | Nachbar | Nachbarrolle | Relation | Kantentyp | Gewicht | Welten | Dauer | Phase |
|---|---|---|---|---|---:|---:|---:|---|
| ausgehend | `1joiyc3` | brueckenkern / brueckenpfad | eintritt | aussen_zu_bruecke | 17 | 5 | 203.12 | gemischter_austritt |
| eingehend | `1joiyc3` | brueckenkern / brueckenpfad | austritt | bruecke_zu_aussen | 16 | 5 | 58.88 | rekoppelnder_austritt |

## Interpretation

Die starken Anschlussanker sind nicht gleichartig:

- `0b7nep9` wirkt als tiefer verteilender Anschlussanker. Er hat viele Ein- und Austritte, sehr lange Phasen und bindet offene Drift-/Seitenbereiche an.
- `1jx2k4i` wirkt als weltbreiter kernnaher Inselanker. Er koppelt stabil ueber mehrere Welten, aber deutlich fokussierter und mit weniger Nachbarschaftsbreite.

Damit ist Anschlussanker nicht nur eine Staerke-Klasse, sondern wahrscheinlich eine eigene Zwischenebene mit Unterrollen.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob lokale Anschlussanker eher zu `0b7nep9` oder zu `1jx2k4i` tendieren. Daraus kann eine feinere Anschlussanker-Familienkarte entstehen.