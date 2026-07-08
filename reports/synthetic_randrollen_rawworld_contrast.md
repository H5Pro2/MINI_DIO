# Sequenz-Rohwelt-Rücklesung

Stand: 2026-07-08 14:58:17

## Zweck

Diese passive Diagnose legt Achsenklassen neben Rohweltmerkmale der jeweiligen Basis- und Folgewelt.
Sie prüft, wodurch sich `verteilt_offen`, `verteilt_rekoppelnd`, `kompakt_nachhallend` und `mittlere_uebergangsphase` in den aktuellen lokalen Sequenzen unterscheiden.

## Klassenmittel

| Klasse | n | Rollen | Kombis | Cross | Rekopplung | Adaptiv | Erfahrung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Drift | Folge Drift | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 6 | 1.5000 | 0.5000 | 0.0000 | 0.722506 | 0.724978 | 0.0040 | 0.5649 | 2.3046 | 2.3308 | 0.0262 | 0.005595 | 0.005663 | 0.003891 | 0.003963 |

## Einzelzeilen

| Label | Welt | Klasse | Rollen | Kombis | Cross | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYN_RANDROLLEN_BRIDGE_TO_SHIFT | SYN_RANDROLLEN_REKOPPLUNGSBREITE | kompakt_nachhallend | 1 | 0 | 0 | 0.726859 | 0.5508 | 2.1027 | 2.4124 | 0.3097 |
| SYN_RANDROLLEN_SHIFT_TO_MOSAIC | SYN_RANDROLLEN_REKOPPLUNGSBREITE | kompakt_nachhallend | 1 | 0 | 0 | 0.723851 | 0.5372 | 2.4124 | 2.2876 | -0.1248 |
| SYN_RANDROLLEN_MOSAIC_TO_LONG | SYN_RANDROLLEN_REKOPPLUNGSBREITE | kompakt_nachhallend | 1 | 0 | 0 | 0.720292 | 0.4966 | 2.2876 | 2.2885 | 0.0009 |
| SYN_RANDROLLEN_INTERWOVEN_TO_LONG | SYN_RANDROLLEN_REKOPPLUNGSBREITE | kompakt_nachhallend | 2 | 1 | 0 | 0.727333 | 0.6239 | 2.3174 | 2.2885 | -0.0288 |
| SYN_NULL_SHUFFLE_TO_RANDOM | SYN_NULL_KONTROLLE | kompakt_nachhallend | 2 | 1 | 0 | 0.715555 | 0.6004 | 2.3633 | 2.3443 | -0.0190 |
| SYN_NULL_RANDOM_TO_SHUFFLE | SYN_NULL_KONTROLLE | kompakt_nachhallend | 2 | 1 | 0 | 0.721146 | 0.5804 | 2.3443 | 2.3633 | 0.0190 |

## Befund

`verteilt_rekoppelnd` zeigt in dieser Auswertung nicht nur mehr Rollenbreite, sondern vor allem höhere Rekopplung, höheren Nachhall und geringere offene Driftwirkung als rein `verteilt_offen`.

`verteilt_offen` wirkt als breite, aber weniger stark rückgebundene Rollenöffnung. `verteilt_rekoppelnd` wirkt als breite, aber getragene Rollenbildung.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt.
