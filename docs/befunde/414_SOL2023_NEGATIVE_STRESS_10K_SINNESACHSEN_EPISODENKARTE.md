# Lokale Sinnesachsen-Episodenkarte

Stand: 2026-06-20 15:14:34

## Grundfrage

Welche Sinnesachse dominiert lokal in einer Episode, und welche Innenfeldwirkung traegt diese Lage?

Diese Diagnose liest keine Handlung und kein Gate. Sie prueft nur, ob Sehen, Hoeren, Abstand oder Feldinput lokal unterschiedlich mit Rekopplung, Strain und MCM-Preview-Symbolen gekoppelt sind.

## Quelle

- Debug-Wurzel: `debug\intake_memory_probe_sol2023_negative_stress_10k`
- CSV: `docs\befunde\414_SOL2023_NEGATIVE_STRESS_10K_SINNESACHSEN_EPISODENKARTE.csv`

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

### SOL_2023_NEGATIVE_STRESS_10K

| Achse | Innenfeld | Preview | Anteil | Count | Rekopplung | Strain | Feldinput |
|---|---|---|---:|---:|---:|---:|---:|
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1725 | 1724 | 0.7252 | 0.1327 | 0.0611 |
| sehen_fokus | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.1615 | 1614 | 0.7188 | 0.1391 | 0.1041 |
| sehen_abstand | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0996 | 995 | 0.7075 | 0.1557 | 0.1136 |
| sehen_abstand | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0635 | 635 | 0.6751 | 0.1858 | 0.1285 |
| hoeren_leise | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0522 | 522 | 0.6952 | 0.1703 | 0.1859 |
| ausgeglichen | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0460 | 460 | 0.7168 | 0.1542 | 0.1147 |
| feldinput | inner_effect_stable | dio_mcm_episode_0e7qvj1 | 0.0430 | 430 | 0.6911 | 0.1764 | 0.2079 |
| feldinput | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0239 | 239 | 0.6474 | 0.2249 | 0.2910 |
| hoeren_hin | inner_effect_stable | dio_mcm_episode_0gqol8d | 0.0192 | 192 | 0.7303 | 0.1332 | 0.0578 |
| hoeren_leise | inner_effect_carried_unrest | dio_mcm_episode_0e7qvj1 | 0.0163 | 163 | 0.6706 | 0.1990 | 0.2074 |

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
