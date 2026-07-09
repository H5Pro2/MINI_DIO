# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-20 22:39:58

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\intake_memory_probe_btc2024_1h_stress_4k\dio_mini_lauf_1`
- CSV: `docs\befunde\445_BTC2024_1H_STRESS_4K_SINNESACHSEN_EPISODENKARTE.csv`

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

### BTC_2024_1H_STRESS_4K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2366 | 945 | 0.7223 | 0.1345 | 0.0618 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.2088 | 834 | 0.7142 | 0.1386 | 0.1011 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1127 | 450 | 0.7020 | 0.1571 | 0.1152 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0739 | 295 | 0.7155 | 0.1528 | 0.1158 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0641 | 256 | 0.6707 | 0.1874 | 0.1378 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0616 | 246 | 0.6932 | 0.1694 | 0.1823 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0591 | 236 | 0.6827 | 0.1785 | 0.2089 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0288 | 115 | 0.6354 | 0.2328 | 0.3062 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0188 | 75 | 0.6623 | 0.2033 | 0.2136 |
| fuehlen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0173 | 69 | 0.6446 | 0.2152 | 0.2109 |

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
