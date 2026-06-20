# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-20 13:06:15

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_sensesplit_worldcheck`
- CSV: `docs\befunde\402_LOKALE_SINNESACHSEN_EPISODENKARTE.csv`

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

### BRIDGE_2024_1000

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1459 | 145 | 0.7142 | 0.1325 | 0.0605 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1388 | 138 | 0.7066 | 0.1407 | 0.1074 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0775 | 77 | 0.6899 | 0.1594 | 0.1140 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0624 | 62 | 0.7095 | 0.1374 | 0.0659 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0523 | 52 | 0.6657 | 0.1831 | 0.1142 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0463 | 46 | 0.7091 | 0.1582 | 0.1191 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0443 | 44 | 0.6820 | 0.1775 | 0.1885 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0382 | 38 | 0.6947 | 0.1459 | 0.1085 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0302 | 30 | 0.6444 | 0.2192 | 0.2579 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0282 | 28 | 0.6770 | 0.1809 | 0.2040 |

### NEG_STRESS_2023_1000

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1861 | 185 | 0.7137 | 0.1349 | 0.0605 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1761 | 175 | 0.7081 | 0.1412 | 0.1007 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1117 | 111 | 0.6947 | 0.1568 | 0.1143 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0795 | 79 | 0.6625 | 0.1903 | 0.1276 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0584 | 58 | 0.7092 | 0.1526 | 0.1112 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0573 | 57 | 0.6813 | 0.1755 | 0.1884 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0382 | 38 | 0.6755 | 0.1820 | 0.2164 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0292 | 29 | 0.7105 | 0.1314 | 0.0563 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0241 | 24 | 0.6354 | 0.2297 | 0.2650 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0241 | 24 | 0.7020 | 0.1414 | 0.0928 |

### POS_EXPANSION_2023_1000

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1600 | 159 | 0.7162 | 0.1330 | 0.0562 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1328 | 132 | 0.7078 | 0.1403 | 0.1033 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0755 | 75 | 0.6981 | 0.1557 | 0.1130 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0573 | 57 | 0.7030 | 0.1361 | 0.0611 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0553 | 55 | 0.6915 | 0.1507 | 0.1159 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0463 | 46 | 0.6726 | 0.1842 | 0.1282 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0443 | 44 | 0.7084 | 0.1542 | 0.1135 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0443 | 44 | 0.6880 | 0.1725 | 0.1857 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0382 | 38 | 0.6853 | 0.1585 | 0.1094 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0342 | 34 | 0.6793 | 0.1781 | 0.2006 |

### REAL_SOL_1000

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1660 | 165 | 0.7151 | 0.1324 | 0.0610 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1358 | 135 | 0.7013 | 0.1454 | 0.1108 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0815 | 81 | 0.6948 | 0.1554 | 0.1094 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0533 | 53 | 0.6619 | 0.1904 | 0.1382 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0523 | 52 | 0.6837 | 0.1712 | 0.1831 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0423 | 42 | 0.6736 | 0.1808 | 0.2083 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0342 | 34 | 0.7086 | 0.1515 | 0.1127 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0332 | 33 | 0.7133 | 0.1320 | 0.0922 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0322 | 32 | 0.7131 | 0.1372 | 0.0586 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0241 | 24 | 0.6417 | 0.2215 | 0.2662 |

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
