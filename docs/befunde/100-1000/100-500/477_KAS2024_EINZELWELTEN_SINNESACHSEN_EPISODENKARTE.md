# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 11:09:15

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_kas_profile_stability`
- CSV: `docs\befunde\477_KAS2024_EINZELWELTEN_SINNESACHSEN_EPISODENKARTE.csv`

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

### KAS2024_15M

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2096 | 418 | 0.7176 | 0.1344 | 0.0637 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1956 | 390 | 0.7099 | 0.1418 | 0.1087 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0993 | 198 | 0.6998 | 0.1573 | 0.1151 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0637 | 127 | 0.7115 | 0.1563 | 0.1215 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0637 | 127 | 0.6646 | 0.1892 | 0.1389 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0587 | 117 | 0.6869 | 0.1716 | 0.1881 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0512 | 102 | 0.6810 | 0.1782 | 0.2048 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0311 | 62 | 0.6356 | 0.2304 | 0.2940 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | 0.0301 | 60 | 0.7059 | 0.1326 | 0.0629 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0271 | 54 | 0.6576 | 0.2046 | 0.2114 |

### KAS2024_1H

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

### KAS2024_30M

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2156 | 430 | 0.7179 | 0.1342 | 0.0638 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2026 | 404 | 0.7073 | 0.1421 | 0.1069 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0953 | 190 | 0.6976 | 0.1574 | 0.1138 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0797 | 159 | 0.6614 | 0.1930 | 0.1386 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0722 | 144 | 0.7094 | 0.1543 | 0.1189 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0637 | 127 | 0.6768 | 0.1812 | 0.2126 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0582 | 116 | 0.6865 | 0.1725 | 0.1918 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0311 | 62 | 0.6349 | 0.2318 | 0.2953 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0191 | 38 | 0.6598 | 0.2015 | 0.2062 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0145 | 29 | 0.6340 | 0.2275 | 0.2425 |

### KAS2024_5M

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
