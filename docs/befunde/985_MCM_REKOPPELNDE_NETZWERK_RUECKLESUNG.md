# MCM-Rolennetzwerk: Rekopplungs-Ruecklesung

## Zweck

Diese Datei legt die Klasse `netz_rekoppelnd_verbunden` passiv auf Brueckenkanten, Austrittsphasen und Nicht-Bruecken-Rollen zurueck.
Sie prueft, welche Kanten-, Phasen- und Rollenbedingungen diese Netzwerklage tragen.

## Sicherheitsgrenze

- passive Ruecklesung
- keine Handlung
- kein Gate
- keine Richtung
- keine Strategie

## Ursachenlesung

- `rekopplung_durch_entlastende_bruecke`: 28
- `rekopplung_durch_phasenwechsel`: 3
- `rekopplung_durch_nachbarschaft`: 1

## Staerkste Knoten

| Knoten | Lesung | Nachbarn | Kanten | Rekopplung-Delta | Strain-Delta | Kantenarten | Austrittsphasen | Nicht-Bruecken |
|---|---|---:|---:|---:|---:|---|---|---|
| `1eju9g0` | `rekopplung_durch_entlastende_bruecke` | 2 | 84 | 0.022038 | -0.028983 | `aussen_zu_bruecke:5 | bruecke_zu_aussen:5` | `rekoppelnder_austritt:10` | `` |
| `1al8fjz` | `rekopplung_durch_entlastende_bruecke` | 7 | 62 | 0.009781 | -0.015749 | `aussen_zu_bruecke:23 | bruecke_zu_aussen:14` | `rekoppelnder_austritt:26 | oeffnend_belastender_austritt:11` | `nichtbruecke_sinnesrauschen:1 | nichtbruecke_zentrum_schwach:1` |
| `077r0df` | `rekopplung_durch_entlastende_bruecke` | 1 | 49 | 0.008765 | -0.014178 | `bruecke_zu_aussen:4 | aussen_zu_bruecke:3` | `rekoppelnder_austritt:6 | gemischter_austritt:1` | `` |
| `0om13wf` | `rekopplung_durch_entlastende_bruecke` | 8 | 33 | 0.038419 | -0.026158 | `aussen_zu_bruecke:14 | bruecke_zu_aussen:9 | bruecke_zu_bruecke:2` | `rekoppelnder_austritt:15 | oeffnend_belastender_austritt:10` | `nichtbruecke_rekopplungsfeld:1` |
| `00nzcuc` | `rekopplung_durch_entlastende_bruecke` | 1 | 18 | 0.001977 | -0.006122 | `aussen_zu_bruecke:5 | bruecke_zu_aussen:1` | `rekoppelnder_austritt:4 | oeffnend_belastender_austritt:1 | gemischter_austritt:1` | `` |
| `06ccuqv` | `rekopplung_durch_entlastende_bruecke` | 1 | 8 | 0.00668 | -0.010058 | `aussen_zu_bruecke:4` | `rekoppelnder_austritt:4` | `nichtbruecke_zentrum_schwach:1` |
| `0i7gfxw` | `rekopplung_durch_entlastende_bruecke` | 2 | 7 | 0.010492 | -0.01855 | `bruecke_zu_bruecke:4 | aussen_zu_bruecke:3` | `rekoppelnder_austritt:6 | gemischter_austritt:1` | `nichtbruecke_zentrum_schwach:1` |
| `0y1i8dq` | `rekopplung_durch_entlastende_bruecke` | 1 | 6 | 0.029051 | -0.023539 | `aussen_zu_bruecke:3 | bruecke_zu_aussen:3` | `rekoppelnder_austritt:4 | oeffnend_belastender_austritt:2` | `nichtbruecke_rekopplungsfeld:1` |
| `1n9f8vr` | `rekopplung_durch_phasenwechsel` | 2 | 5 | -0.002425 | -0.014967 | `aussen_zu_bruecke:4 | bruecke_zu_aussen:1` | `gemischter_austritt:4 | rekoppelnder_austritt:1` | `` |
| `080f74u` | `rekopplung_durch_entlastende_bruecke` | 1 | 5 | 0.000565 | -0.000101 | `bruecke_zu_aussen:5` | `rekoppelnder_austritt:5` | `nichtbruecke_zentrum_schwach:1` |
| `0sv0ru8` | `rekopplung_durch_entlastende_bruecke` | 1 | 5 | 0.029024 | -0.004298 | `aussen_zu_bruecke:5` | `rekoppelnder_austritt:5` | `nichtbruecke_zentrum_schwach:1` |
| `1aurt3q` | `rekopplung_durch_entlastende_bruecke` | 1 | 5 | 0.029024 | -0.004298 | `bruecke_zu_aussen:5` | `rekoppelnder_austritt:5` | `nichtbruecke_zentrum_schwach:1` |
| `0qhs6nb` | `rekopplung_durch_phasenwechsel` | 2 | 4 | 0.013186 | 0.006448 | `aussen_zu_bruecke:2 | bruecke_zu_aussen:2` | `rekoppelnder_austritt:2 | oeffnend_belastender_austritt:2` | `nichtbruecke_driftfeld:1` |
| `0u69u6w` | `rekopplung_durch_entlastende_bruecke` | 1 | 4 | 0.042666 | -0.064625 | `aussen_zu_bruecke:4` | `rekoppelnder_austritt:4` | `` |
| `0ybhu2p` | `rekopplung_durch_entlastende_bruecke` | 1 | 4 | 0.041406 | -0.018645 | `aussen_zu_bruecke:2 | bruecke_zu_aussen:2` | `rekoppelnder_austritt:2 | oeffnend_belastender_austritt:2` | `nichtbruecke_sinnesrauschen:1` |
| `10mbxau` | `rekopplung_durch_entlastende_bruecke` | 1 | 4 | 0.042666 | -0.064625 | `bruecke_zu_aussen:4` | `rekoppelnder_austritt:4` | `` |
| `17eveju` | `rekopplung_durch_entlastende_bruecke` | 1 | 4 | 0.007346 | -0.012371 | `bruecke_zu_aussen:4` | `rekoppelnder_austritt:4` | `` |
| `0r1o8ja` | `rekopplung_durch_entlastende_bruecke` | 2 | 4 | 0.034301 | -0.025796 | `aussen_zu_bruecke:2 | bruecke_zu_aussen:2` | `rekoppelnder_austritt:2 | oeffnend_belastender_austritt:2` | `nichtbruecke_driftfeld:1` |
| `1i31hl0` | `rekopplung_durch_entlastende_bruecke` | 2 | 4 | 1.3e-05 | -0.016382 | `aussen_zu_bruecke:3 | bruecke_zu_aussen:1` | `oeffnend_belastender_austritt:2 | rekoppelnder_austritt:2` | `nichtbruecke_offen:1` |
| `0htnihj` | `rekopplung_durch_entlastende_bruecke` | 1 | 4 | 0.02672 | -0.025095 | `aussen_zu_bruecke:4` | `rekoppelnder_austritt:4` | `` |
| `00dz86x` | `rekopplung_durch_nachbarschaft` | 2 | 3 | -0.048302 | 0.040379 | `bruecke_zu_aussen:3` | `oeffnend_belastender_austritt:3` | `nichtbruecke_offen:1` |
| `0dxi31r` | `rekopplung_durch_entlastende_bruecke` | 1 | 3 | 0.002454 | -0.009052 | `aussen_zu_bruecke:3` | `rekoppelnder_austritt:3` | `` |
| `0xsq19y` | `rekopplung_durch_entlastende_bruecke` | 1 | 3 | 0.018721 | -0.023801 | `bruecke_zu_aussen:3` | `rekoppelnder_austritt:3` | `` |
| `1a9sbfi` | `rekopplung_durch_entlastende_bruecke` | 1 | 3 | 0.018721 | -0.023801 | `aussen_zu_bruecke:3` | `rekoppelnder_austritt:3` | `` |
| `1k7xap1` | `rekopplung_durch_entlastende_bruecke` | 1 | 3 | 0.030204 | -0.03772 | `aussen_zu_bruecke:3` | `rekoppelnder_austritt:3` | `` |
| `0tf9fq3` | `rekopplung_durch_phasenwechsel` | 2 | 3 | -0.00294 | -0.005848 | `bruecke_zu_bruecke:2 | aussen_zu_bruecke:1` | `gemischter_austritt:2 | rekoppelnder_austritt:1` | `nichtbruecke_rekopplungsfeld:1` |
| `17rahh6` | `rekopplung_durch_entlastende_bruecke` | 1 | 2 | 0.006245 | -0.014584 | `aussen_zu_bruecke:1 | bruecke_zu_aussen:1` | `rekoppelnder_austritt:1 | oeffnend_belastender_austritt:1` | `` |
| `0ldenly` | `rekopplung_durch_entlastende_bruecke` | 1 | 2 | 0.06182 | -0.04263 | `aussen_zu_bruecke:1 | bruecke_zu_aussen:1` | `rekoppelnder_austritt:2` | `nichtbruecke_sinnesrauschen:1` |
| `0n5sqpn` | `rekopplung_durch_entlastende_bruecke` | 1 | 2 | 0.018158 | -0.006227 | `bruecke_zu_aussen:2` | `rekoppelnder_austritt:2` | `nichtbruecke_rekopplungsfeld:1` |
| `0q7j4gf` | `rekopplung_durch_entlastende_bruecke` | 2 | 2 | 0.077487 | -0.0629 | `aussen_zu_bruecke:1 | bruecke_zu_aussen:1` | `rekoppelnder_austritt:2` | `nichtbruecke_sinnesrauschen:1 | nichtbruecke_offen:1` |
| `0tv1tha` | `rekopplung_durch_entlastende_bruecke` | 1 | 1 | 0.042512 | -0.061082 | `bruecke_zu_aussen:1` | `rekoppelnder_austritt:1` | `nichtbruecke_randspannung:1` |
| `1mesbjy` | `rekopplung_durch_entlastende_bruecke` | 1 | 1 | 0.015811 | -0.053733 | `aussen_zu_bruecke:1` | `rekoppelnder_austritt:1` | `nichtbruecke_sinnesrauschen:1` |

## Interpretation

Rekoppelnde Verbindung ist in dieser Ruecklesung keine blosse Verbindung.
Sie entsteht dort, wo Bruecken- und Aussenkanten Entlastung tragen: Rekopplung steigt, Strain faellt.

Das spricht fuer eine entlastende Netzwerksituation:

```text
Knoten bleibt sichtbar.
Nachbarschaft wirkt mit.
Die Verbindung traegt ruhig genug.
Das Feld rekoppelt verbunden statt belastet zu fragmentieren.
```

## Grenze

Diese Lesung beschreibt nur Feldbedingungen.
Sie erzeugt keine Handlung und keine Regel.

## Wie es weitergeht

Als naechstes sollten die Ruecklesungen von `netz_fragmentiert_belastet` und `netz_rekoppelnd_verbunden` direkt verglichen werden.
Dann wird sichtbar, welche Feldbedingungen Belastung von Rekopplung unterscheiden.
