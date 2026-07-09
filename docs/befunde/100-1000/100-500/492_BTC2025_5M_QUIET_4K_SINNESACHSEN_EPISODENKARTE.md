# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 13:02:58

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_btc2025_section_shift\BTC2025_5M_QUIET_4K`
- CSV: `docs\befunde\492_BTC2025_5M_QUIET_4K_SINNESACHSEN_EPISODENKARTE.csv`

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

### BTC2025_5M_QUIET_4K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1397 | 558 | 0.7245 | 0.1300 | 0.0582 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1249 | 499 | 0.7192 | 0.1375 | 0.1011 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0779 | 311 | 0.7064 | 0.1546 | 0.1073 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0541 | 216 | 0.7049 | 0.1402 | 0.0998 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0538 | 215 | 0.7111 | 0.1327 | 0.0603 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0443 | 177 | 0.6938 | 0.1695 | 0.1867 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0428 | 171 | 0.6984 | 0.1542 | 0.1042 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0426 | 170 | 0.6762 | 0.1817 | 0.1222 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0383 | 153 | 0.6877 | 0.1769 | 0.2103 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0371 | 148 | 0.7170 | 0.1528 | 0.1119 |

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
