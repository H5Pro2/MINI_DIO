# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-20 21:07:20

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\intake_memory_probe_btc2024_5m_stress_4k\dio_mini_lauf_1`
- CSV: `docs\befunde\440_BTC2024_5M_STRESS_4K_SINNESACHSEN_EPISODENKARTE.csv`

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

### BTC_2024_5M_STRESS_4K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1rxdw4p | 0.0729 | 291 | 0.7155 | 0.1382 | 0.1001 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0714 | 285 | 0.7201 | 0.1324 | 0.0623 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1rxdw4p | 0.0671 | 268 | 0.7219 | 0.1322 | 0.0603 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0653 | 261 | 0.7144 | 0.1394 | 0.1031 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0646 | 258 | 0.7234 | 0.1320 | 0.0600 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0558 | 223 | 0.7152 | 0.1392 | 0.0987 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0476 | 190 | 0.6999 | 0.1576 | 0.1145 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0318 | 127 | 0.6605 | 0.1942 | 0.1315 |
| feldinput | inner_effect_stable | dio_mcm_episode_1rxdw4p | 0.0313 | 125 | 0.6873 | 0.1756 | 0.2104 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_1rxdw4p | 0.0298 | 119 | 0.6896 | 0.1708 | 0.1942 |

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
