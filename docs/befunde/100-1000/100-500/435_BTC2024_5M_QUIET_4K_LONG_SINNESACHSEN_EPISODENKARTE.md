# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-20 20:53:38

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\intake_memory_probe_btc2024_5m_quiet_4k_long`
- CSV: `docs\befunde\435_BTC2024_5M_QUIET_4K_LONG_SINNESACHSEN_EPISODENKARTE.csv`

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

### BTC_2024_5M_QUIET_4K_LONG

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1740 | 695 | 0.7202 | 0.1337 | 0.0626 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1715 | 685 | 0.7140 | 0.1388 | 0.1028 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0909 | 363 | 0.7017 | 0.1558 | 0.1110 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0704 | 281 | 0.6739 | 0.1833 | 0.1222 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0508 | 203 | 0.6904 | 0.1723 | 0.1898 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0448 | 179 | 0.6850 | 0.1767 | 0.2083 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0421 | 168 | 0.7137 | 0.1536 | 0.1149 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0240 | 96 | 0.7154 | 0.1363 | 0.0626 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0228 | 91 | 0.6373 | 0.2298 | 0.2961 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_1hdpu9s | 0.0213 | 85 | 0.7059 | 0.1392 | 0.1039 |

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
