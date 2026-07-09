# PAXG 2025 Holdout-Matrix

## Datengrundlage

Geprüft wurden drei PAXG-2025-Welten mit je 1994 Episoden:

| Welt | Quelle | Hinweis |
|---|---|---|
| PAXG_2025_5M_HOLDOUT | `data/kontrolliert_paxg_2025_5m_test1_2000_PAXGUSDT.csv` | 5m-Fenster |
| PAXG_2025_15M_HOLDOUT | `data/kontrolliert_paxg_2025_15m_test1_2000_PAXGUSDT.csv` | aus 5m aggregiertes 15m-Fenster |
| PAXG_2025_1H_HOLDOUT | `data/kontrolliert_paxg_2025_1h_test1_2000_PAXGUSDT.csv` | 1h-Fenster |

## Topologie

| Welt | Topologiezustand | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2025_5M_HOLDOUT | stark_zentriert_wenig_rand | 0.9950 | 0.0050 | 0.0000 | 0.2417 | 0.7165 | 0.5397 | 0.1565 | 0.8628 |
| PAXG_2025_15M_HOLDOUT | stark_zentriert_wenig_rand | 0.9900 | 0.0100 | 0.0000 | 0.2467 | 0.6984 | 0.5179 | 0.1639 | 0.8441 |
| PAXG_2025_1H_HOLDOUT | stark_zentriert_wenig_rand | 0.9935 | 0.0065 | 0.0000 | 0.2477 | 0.6952 | 0.5162 | 0.1665 | 0.8400 |

## Randdruck-Lupe

| Welt | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2025_5M_HOLDOUT | 0.4152 | 0.1510 | 0.3561 | 0.0777 | 0.1565 | 0.0911 | 0.1509 | 0.0828 |
| PAXG_2025_15M_HOLDOUT | 0.3932 | 0.1700 | 0.3250 | 0.1118 | 0.1639 | 0.1043 | 0.1802 | 0.0983 |
| PAXG_2025_1H_HOLDOUT | 0.3977 | 0.1655 | 0.3104 | 0.1264 | 0.1665 | 0.1096 | 0.1819 | 0.1050 |

## Lesart

PAXG 2025 bestätigt die bisherige Trennung zwischen stabiler Topologie und lokaler Feldfärbung. Alle drei Zeitachsen bleiben `stark_zentriert_wenig_rand`, ohne sichtbare Rand-/Kippdominanz.

Gleichzeitig verschiebt sich die lokale Aufnahmequalität:

- 5m trägt die stärkste Rekopplung und die geringste Dämpfung.
- 15m und 1h glätten das Feld etwas, erhöhen aber Dämpfung, Strain und Sinneslücken.
- Die offene Variante bleibt klein und wird nicht zu einem Topologiebruch.

Damit wirkt PAXG 2025 nicht wie eine neue Topologie, sondern wie dieselbe zentrumsnahe Rollenordnung mit zeitachsenabhängiger lokaler Färbung.

## Grenze

Die 15m-Welt wurde aus 5m-Daten aggregiert. Der Befund ist deshalb ein Holdout-Hinweis, kein endgültiger Beweis für alle PAXG-Phasen.
