# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-20 17:43:09

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\intake_memory_probe_btc2024_5m_2k`
- CSV: `docs\befunde\430_BTC2024_5M_2K_SINNESACHSEN_EPISODENKARTE.csv`

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

### BTC_2024_5M_2K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0747 | 149 | 0.7192 | 0.1334 | 0.0609 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0727 | 145 | 0.7128 | 0.1375 | 0.1015 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0687 | 137 | 0.7258 | 0.1322 | 0.0583 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0567 | 113 | 0.7193 | 0.1351 | 0.0953 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1jx2k4i | 0.0361 | 72 | 0.6984 | 0.1426 | 0.0978 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1jx2k4i | 0.0341 | 68 | 0.7050 | 0.1369 | 0.0620 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0341 | 68 | 0.7047 | 0.1404 | 0.1001 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0336 | 67 | 0.6954 | 0.1562 | 0.1112 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0336 | 67 | 0.7023 | 0.1541 | 0.1000 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1joiyc3 | 0.0316 | 63 | 0.7113 | 0.1374 | 0.0662 |

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
