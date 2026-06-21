# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-21 12:16:16

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\_codex_asset_year_stability\BTC2025_5M`
- CSV: `docs\befunde\486_BTC2025_5M_SINNESACHSEN_EPISODENKARTE.csv`

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

### BTC2025_5M

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1876 | 374 | 0.7137 | 0.1342 | 0.0628 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1866 | 372 | 0.7085 | 0.1412 | 0.1069 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1138 | 227 | 0.6979 | 0.1567 | 0.1144 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0752 | 150 | 0.6628 | 0.1896 | 0.1267 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0522 | 104 | 0.7097 | 0.1563 | 0.1202 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0522 | 104 | 0.6833 | 0.1747 | 0.1916 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0471 | 94 | 0.6760 | 0.1829 | 0.2109 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1rxdw4p | 0.0226 | 45 | 0.7150 | 0.1371 | 0.1057 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0216 | 43 | 0.6510 | 0.2076 | 0.2222 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0201 | 40 | 0.6370 | 0.2300 | 0.2927 |

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
