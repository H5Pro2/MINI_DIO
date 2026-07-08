# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 14:48:53

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 8 | 1.0000 | 0.0000 | 0.0000 | 0.739568 | 0.739568 | 0.0000 | 0.6555 | 7.4600 | 4.1509 | -3.3091 | 0.689986 | 0.580711 | 0.012585 | 0.006542 |
| mittlere_uebergangsphase | 4 | 3.0000 | 3.0000 | 2.0000 | 0.743548 | 0.765292 | 0.0593 | 0.6974 | 11.1508 | 11.4307 | 0.2799 | 0.543437 | 0.595667 | 0.014346 | 0.016361 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN_HARMONIE_FOLLOW_0_1000 | SYN_HARMONIE_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.751216 | 0.7475 | 2.5185 | 3.9282 | 1.4098 |
| SYN_HARMONIE_FOLLOW_1000_2000 | SYN_HARMONIE_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.750519 | 0.7651 | 3.9282 | 2.5234 | -1.4049 |
| SYN_HARMONIE_FOLLOW_2000_3000 | SYN_HARMONIE_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.751808 | 0.7658 | 2.5234 | 1.2604 | -1.2629 |
| SYN_HARMONIE_FOLLOW_3000_4000 | SYN_HARMONIE_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.754863 | 0.7935 | 1.2604 | 0.6579 | -0.6026 |
| SYN_BRUCH_RAND_FOLLOW_0_1000 | SYN_BRUCH_RAND_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.744082 | 0.6966 | 8.4322 | 9.6187 | 1.1865 |
| SYN_BRUCH_RAND_FOLLOW_1000_2000 | SYN_BRUCH_RAND_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.710010 | 0.3874 | 9.6187 | 4.2147 | -5.4040 |
| SYN_BRUCH_RAND_FOLLOW_2000_3000 | SYN_BRUCH_RAND_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.748168 | 0.7196 | 4.2147 | 2.9570 | -1.2577 |
| SYN_BRUCH_RAND_FOLLOW_3000_4000 | SYN_BRUCH_RAND_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.751847 | 0.7670 | 2.9570 | 6.3086 | 3.3516 |
| SYN_RAND_DOM_FOLLOW_0_1000 | SYN_RAND_DOM_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.725185 | 0.5703 | 23.6432 | 11.9730 | -11.6702 |
| SYN_RAND_DOM_FOLLOW_1000_2000 | SYN_RAND_DOM_SEQ | kompakt_nachhallend | 1 | 0 | 0 | 0.724772 | 0.4943 | 11.9730 | 5.6927 | -6.2803 |
| SYN_RAND_DOM_FOLLOW_2000_3000 | SYN_RAND_DOM_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.744771 | 0.6946 | 5.6927 | 27.5211 | 21.8284 |
| SYN_RAND_DOM_FOLLOW_3000_4000 | SYN_RAND_DOM_SEQ | mittlere_uebergangsphase | 3 | 3 | 2 | 0.733490 | 0.6315 | 27.5211 | 2.2742 | -25.2469 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
