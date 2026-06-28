# MCM-Rolennetzwerk: Fragmentierungs-Ruecklesung

## Zweck

Diese Datei legt die Klasse `netz_fragmentiert_belastet` passiv auf Brueckenkanten, Austrittsphasen und Nicht-Bruecken-Rollen zurueck.
Sie prueft, welche Kanten-, Phasen- und Rollenbedingungen diese Netzwerklage tragen.

## Sicherheitsgrenze

- passive Ruecklesung
- keine Handlung
- kein Gate
- keine Richtung
- keine Strategie

## Ursachenlesung

- `fragmentierung_durch_aussen_brueckenriss`: 25
- `fragmentierung_offen`: 3

## Staerkste Knoten

| Knoten | Lesung | Nachbarn | Kanten | Rekopplung-Delta | Strain-Delta | Kantenarten | Austrittsphasen | Nicht-Bruecken |
|---|---|---:|---:|---:|---:|---|---|---|
| `0e7qvj1` | `fragmentierung_durch_aussen_brueckenriss` | 17 | 1425 | -0.046927 | 0.046124 | `bruecke_zu_aussen:75 | bruecke_zu_bruecke:54 | aussen_zu_bruecke:32` | `oeffnend_belastender_austritt:104 | rekoppelnder_austritt:34 | gemischter_austritt:23` | `nichtbruecke_zentrum_getragen:1` |
| `18l3thm` | `fragmentierung_durch_aussen_brueckenriss` | 5 | 837 | -0.035568 | 0.027827 | `bruecke_zu_bruecke:32 | bruecke_zu_aussen:11 | aussen_zu_bruecke:11` | `oeffnend_belastender_austritt:20 | gemischter_austritt:19 | rekoppelnder_austritt:15` | `` |
| `0mji3u6` | `fragmentierung_durch_aussen_brueckenriss` | 4 | 468 | -0.012034 | 0.000955 | `bruecke_zu_bruecke:30 | aussen_zu_bruecke:10 | bruecke_zu_aussen:1` | `rekoppelnder_austritt:19 | oeffnend_belastender_austritt:18 | gemischter_austritt:4` | `nichtbruecke_rekopplungsfeld:1` |
| `1joiyc3` | `fragmentierung_durch_aussen_brueckenriss` | 9 | 298 | -0.050945 | 0.059546 | `bruecke_zu_aussen:31 | bruecke_zu_bruecke:16 | aussen_zu_bruecke:11` | `oeffnend_belastender_austritt:31 | rekoppelnder_austritt:20 | gemischter_austritt:7` | `nichtbruecke_zentrum_schwach:1` |
| `14coypf` | `fragmentierung_durch_aussen_brueckenriss` | 9 | 200 | -0.056852 | 0.054883 | `bruecke_zu_bruecke:28 | bruecke_zu_aussen:23 | aussen_zu_bruecke:11` | `oeffnend_belastender_austritt:35 | rekoppelnder_austritt:18 | gemischter_austritt:9` | `nichtbruecke_zentrum_schwach:1` |
| `0jbl5pq` | `fragmentierung_durch_aussen_brueckenriss` | 8 | 185 | -0.005535 | 0.007555 | `aussen_zu_bruecke:33 | bruecke_zu_bruecke:18 | bruecke_zu_aussen:12` | `oeffnend_belastender_austritt:28 | rekoppelnder_austritt:22 | gemischter_austritt:13` | `nichtbruecke_zentrum_getragen:1` |
| `18n06fj` | `fragmentierung_durch_aussen_brueckenriss` | 4 | 169 | -0.016058 | 0.012278 | `bruecke_zu_bruecke:18 | aussen_zu_bruecke:11 | bruecke_zu_aussen:2` | `oeffnend_belastender_austritt:16 | rekoppelnder_austritt:14 | gemischter_austritt:1` | `nichtbruecke_rekopplungsfeld:1` |
| `0ybr5e3` | `fragmentierung_offen` | 3 | 125 | -0.015003 | -9.9e-05 | `bruecke_zu_aussen:10 | aussen_zu_bruecke:10` | `rekoppelnder_austritt:11 | oeffnend_belastender_austritt:6 | gemischter_austritt:3` | `` |
| `0mw7rev` | `fragmentierung_durch_aussen_brueckenriss` | 5 | 27 | -0.149746 | 0.170479 | `bruecke_zu_aussen:17 | aussen_zu_bruecke:2` | `oeffnend_belastender_austritt:17 | rekoppelnder_austritt:2` | `` |
| `0mm85pw` | `fragmentierung_durch_aussen_brueckenriss` | 4 | 24 | -0.165949 | 0.180238 | `bruecke_zu_aussen:14 | aussen_zu_bruecke:2` | `oeffnend_belastender_austritt:16` | `` |
| `02ujuqf` | `fragmentierung_durch_aussen_brueckenriss` | 4 | 21 | -0.009544 | 0.012344 | `aussen_zu_bruecke:7 | bruecke_zu_bruecke:4` | `oeffnend_belastender_austritt:9 | rekoppelnder_austritt:2` | `` |
| `0wjn8vm` | `fragmentierung_durch_aussen_brueckenriss` | 4 | 18 | -0.005251 | 0.002715 | `bruecke_zu_aussen:5 | aussen_zu_bruecke:5` | `oeffnend_belastender_austritt:6 | rekoppelnder_austritt:3 | gemischter_austritt:1` | `` |
| `1i1sl4l` | `fragmentierung_offen` | 2 | 18 | 0.003503 | -0.00754 | `aussen_zu_bruecke:4 | bruecke_zu_aussen:4` | `rekoppelnder_austritt:6 | oeffnend_belastender_austritt:2` | `` |
| `10b8y4e` | `fragmentierung_offen` | 2 | 13 | -0.019334 | -0.005315 | `aussen_zu_bruecke:9` | `rekoppelnder_austritt:5 | oeffnend_belastender_austritt:4` | `nichtbruecke_zentrum_schwach:1` |
| `0jlkrep` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 12 | -0.04087 | 0.033094 | `aussen_zu_bruecke:6 | bruecke_zu_aussen:5` | `oeffnend_belastender_austritt:10 | rekoppelnder_austritt:1` | `` |
| `1engxbn` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 9 | -0.005449 | 0.005374 | `bruecke_zu_aussen:1 | aussen_zu_bruecke:1` | `oeffnend_belastender_austritt:2` | `` |
| `1qqnvqf` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 6 | -0.012487 | 0.021576 | `aussen_zu_bruecke:3` | `oeffnend_belastender_austritt:3` | `` |
| `19dxnmz` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 6 | -0.153692 | 0.173211 | `bruecke_zu_aussen:6` | `oeffnend_belastender_austritt:6` | `` |
| `1f4jh6c` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 6 | -0.027023 | 0.012253 | `aussen_zu_bruecke:5` | `oeffnend_belastender_austritt:4 | rekoppelnder_austritt:1` | `` |
| `0fljihc` | `fragmentierung_durch_aussen_brueckenriss` | 2 | 5 | -0.133296 | 0.1606 | `bruecke_zu_aussen:5` | `oeffnend_belastender_austritt:5` | `` |
| `0dsrwv5` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 5 | -0.026241 | 0.028258 | `aussen_zu_bruecke:5` | `oeffnend_belastender_austritt:5` | `` |
| `19w9kxc` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 5 | -0.187611 | 0.204766 | `bruecke_zu_aussen:5` | `oeffnend_belastender_austritt:5` | `` |
| `0k7ekcr` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 3 | -0.197885 | 0.21761 | `bruecke_zu_aussen:3` | `oeffnend_belastender_austritt:3` | `` |
| `15cyz2v` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 3 | -0.104051 | 0.168316 | `bruecke_zu_aussen:3` | `oeffnend_belastender_austritt:3` | `` |
| `0jwgafx` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 2 | -0.052793 | 0.037359 | `aussen_zu_bruecke:2` | `oeffnend_belastender_austritt:2` | `` |
| `1n2f96o` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 2 | -0.009507 | 0.015195 | `aussen_zu_bruecke:2` | `oeffnend_belastender_austritt:2` | `` |
| `14k61ms` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 1 | -0.028548 | 0.003996 | `bruecke_zu_aussen:1` | `oeffnend_belastender_austritt:1` | `` |
| `1x5cw2v` | `fragmentierung_durch_aussen_brueckenriss` | 1 | 1 | -0.064778 | 0.094045 | `aussen_zu_bruecke:1` | `oeffnend_belastender_austritt:1` | `nichtbruecke_zentrum_schwach:1` |

## Interpretation

Belastete Fragmentierung ist in dieser Ruecklesung keine einfache Leere.
Sie entsteht dort, wo Knoten sichtbar und oft sogar stark vernetzt bleiben, aber Rekopplung in den Kanten faellt und Strain steigt.

Das spricht fuer eine belastete Netzwerksituation:

```text
Knoten bleibt da.
Nachbarschaft bleibt da.
Aber die Verbindung traegt nicht ruhig genug.
Das Feld fragmentiert belastet statt zu verschwinden.
```

## Grenze

Diese Lesung beschreibt nur Feldbedingungen.
Sie erzeugt keine Handlung und keine Regel.

## Wie es weitergeht

Als naechstes sollten die Ruecklesungen von `netz_fragmentiert_belastet` und `netz_rekoppelnd_verbunden` direkt verglichen werden.
Dann wird sichtbar, welche Feldbedingungen Belastung von Rekopplung unterscheiden.
