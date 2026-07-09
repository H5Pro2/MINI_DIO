# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-20 13:14:00

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_sensesplit_axis_validate`
- CSV: `docs\befunde\404_SINNESACHSEN_EPISODENKARTE_GEGENPROBE.csv`

## Methode

Pro Welt werden die Achsen weltrelativ normalisiert. Eine Achse gilt lokal dominant, wenn sie in dieser Welt deutlich ueber ihrem eigenen Durchschnitt liegt.

Gelesene Achsen:

- `sehen_fokus`
- `sehen_abstand`
- `hoeren_hin`
- `hoeren_leise`
- `fuehlen_abstand`
- `feldinput`
- `ausgeglichen`

## Top-Befunde je Welt

### BTC_2025_1H_2000

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1610 | 321 | 0.7206 | 0.1329 | 0.0593 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1319 | 263 | 0.7132 | 0.1388 | 0.0970 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0707 | 141 | 0.7008 | 0.1541 | 0.1030 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0502 | 100 | 0.6612 | 0.1902 | 0.1315 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0486 | 97 | 0.7167 | 0.1514 | 0.1101 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0426 | 85 | 0.6868 | 0.1703 | 0.1797 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0336 | 67 | 0.6793 | 0.1791 | 0.2049 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0336 | 67 | 0.7197 | 0.1357 | 0.0625 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0326 | 65 | 0.7139 | 0.1363 | 0.0901 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1ahj81f | 0.0271 | 54 | 0.7023 | 0.1376 | 0.0868 |

### KAS_2024_1H_2000

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2282 | 455 | 0.7164 | 0.1343 | 0.0627 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2177 | 434 | 0.7090 | 0.1408 | 0.1039 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1003 | 200 | 0.6962 | 0.1584 | 0.1151 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0817 | 163 | 0.6660 | 0.1887 | 0.1327 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0682 | 136 | 0.7104 | 0.1557 | 0.1184 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0667 | 133 | 0.6874 | 0.1727 | 0.1842 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0481 | 96 | 0.6772 | 0.1829 | 0.2079 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0306 | 61 | 0.6328 | 0.2329 | 0.2948 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0216 | 43 | 0.6574 | 0.2050 | 0.2129 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0186 | 37 | 0.6321 | 0.2264 | 0.2154 |

### KAS_2024_5M_2000

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1439 | 287 | 0.7183 | 0.1336 | 0.0619 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1389 | 277 | 0.7106 | 0.1423 | 0.1111 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | 0.0772 | 154 | 0.7124 | 0.1347 | 0.0637 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | 0.0687 | 137 | 0.7024 | 0.1429 | 0.1054 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0667 | 133 | 0.6989 | 0.1570 | 0.1166 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0592 | 118 | 0.6694 | 0.1872 | 0.1264 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0366 | 73 | 0.7109 | 0.1564 | 0.1188 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0341 | 68 | 0.6898 | 0.1693 | 0.1847 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0321 | 64 | 0.6850 | 0.1759 | 0.2098 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1jx2k4i | 0.0291 | 58 | 0.6897 | 0.1586 | 0.1140 |

### SOL_2025_5M_2000

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1745 | 348 | 0.7177 | 0.1334 | 0.0642 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1605 | 320 | 0.7094 | 0.1410 | 0.1091 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0752 | 150 | 0.6978 | 0.1580 | 0.1163 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0632 | 126 | 0.6689 | 0.1879 | 0.1326 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0542 | 108 | 0.7034 | 0.1389 | 0.0664 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0522 | 104 | 0.6889 | 0.1705 | 0.1846 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0446 | 89 | 0.6810 | 0.1798 | 0.2143 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0421 | 84 | 0.7107 | 0.1543 | 0.1197 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0371 | 74 | 0.6925 | 0.1480 | 0.1123 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0306 | 61 | 0.6880 | 0.1574 | 0.1104 |

## Erste Lesart

Die Weltmittelwerte waren eng. Lokal entstehen aber unterscheidbare Achsenlagen. Entscheidend ist nicht, dass eine Welt insgesamt lauter oder visueller ist, sondern welche Achse in konkreten Episoden hervorsticht und ob diese Episode rekoppelt oder belastet.

Damit verschiebt sich die naechste Pruefung von globaler Regulation zu episodischer Kopplung:

```text
Welche Achsenlage wurde vom Feld getragen?
Welche Achsenlage erzeugte Strain?
Welche Achsenlage blieb nur offen oder ausgeglichen?
```

## Wie es weitergeht

Als naechstes wird aus dieser Karte eine kleine Rekopplungsanalyse abgeleitet: Welche Achsenlage hat pro Welt die beste Rekopplung bei niedriger Belastung?
