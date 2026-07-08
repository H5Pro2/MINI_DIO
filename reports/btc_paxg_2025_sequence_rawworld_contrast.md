# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 16:28:45

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mittlere_uebergangsphase | 2 | 4.0000 | 6.0000 | 3.5000 | 0.691261 | 0.733327 | 0.5962 | 0.2995 | 1.5976 | 2.1206 | 0.5229 | 0.009278 | 0.020467 | 0.001378 | 0.001840 |
| verteilt_offen | 3 | 6.0000 | 15.0000 | 8.3333 | 0.691360 | 0.729199 | 0.4875 | 0.3126 | 3.0232 | 2.2986 | -0.7246 | 0.025795 | 0.013519 | 0.002584 | 0.001986 |
| verteilt_rekoppelnd | 3 | 8.0000 | 20.0000 | 10.0000 | 0.704207 | 0.736206 | 0.2952 | 0.3753 | 0.9887 | 1.4035 | 0.4147 | 0.011629 | 0.012492 | 0.000783 | 0.001135 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BTC_2025_FOLLOW_0_1000 | BTC_2025_LOCAL_SEQ | verteilt_offen | 7 | 20 | 11 | 0.692227 | 0.3269 | 4.1171 | 2.6488 | -1.4683 |
| PAXG_2025_FOLLOW_0_1000 | PAXG_2025_LOCAL_SEQ | mittlere_uebergangsphase | 4 | 6 | 3 | 0.694303 | 0.3160 | 1.2518 | 1.0622 | -0.1896 |
| BTC_2025_FOLLOW_1000_2000 | BTC_2025_LOCAL_SEQ | verteilt_offen | 5 | 10 | 6 | 0.691002 | 0.3115 | 2.6488 | 2.3037 | -0.3451 |
| PAXG_2025_FOLLOW_1000_2000 | PAXG_2025_LOCAL_SEQ | verteilt_rekoppelnd | 7 | 18 | 8 | 0.699749 | 0.3426 | 1.0622 | 0.9637 | -0.0985 |
| BTC_2025_FOLLOW_2000_3000 | BTC_2025_LOCAL_SEQ | verteilt_offen | 6 | 15 | 8 | 0.690850 | 0.2993 | 2.3037 | 1.9435 | -0.3602 |
| PAXG_2025_FOLLOW_2000_3000 | PAXG_2025_LOCAL_SEQ | verteilt_rekoppelnd | 5 | 10 | 4 | 0.708043 | 0.3996 | 0.9637 | 0.9402 | -0.0235 |
| BTC_2025_FOLLOW_3000_4000 | BTC_2025_LOCAL_SEQ | mittlere_uebergangsphase | 4 | 6 | 4 | 0.688220 | 0.2831 | 1.9435 | 3.1789 | 1.2355 |
| PAXG_2025_FOLLOW_3000_4000 | PAXG_2025_LOCAL_SEQ | verteilt_rekoppelnd | 12 | 32 | 18 | 0.704830 | 0.3837 | 0.9402 | 2.3065 | 1.3663 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
