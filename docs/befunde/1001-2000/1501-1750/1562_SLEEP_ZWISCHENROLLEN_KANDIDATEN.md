# Sleep-Zwischenrollen Kandidaten

Stand: 2026-07-05 19:56:04

## Zweck

Diese Auswertung prueft, ob weiche Sleep-Kombinationen als Zwischenrollen-Kandidaten lesbar sind.

Eine Zwischenrolle ist hier noch keine neue autonome Bedeutung. Gemeint ist nur:

```text
Eine Offline-Kombination kommt bei gleicher Welt voll zurueck
und findet in einer verwandten Folgewelt zumindest teilweise Anschluss.
```

Die Auswertung bleibt passiv: keine Handlung, keine Richtung, kein Gate.

## Zaehler

- `origin_bound_combination`: `3`
- `quiet_intermediate_candidate`: `7`

## Kandidaten

| Kombination | Zustand | gleiche Welt | Ruhewelt | Stress | Mosaik |
|---|---|---|---|---|---|
| `dio_mcm_episode_0e7qvj1|dio_mcm_episode_0eghs1d` | `quiet_intermediate_candidate` | `sleep_combination_fully_reactivated` | `sleep_combination_partly_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` |
| `dio_mcm_episode_0e7qvj1|dio_mcm_episode_0qrlave` | `quiet_intermediate_candidate` | `sleep_combination_fully_reactivated` | `sleep_combination_partly_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` |
| `dio_mcm_episode_0e7qvj1|dio_mcm_episode_1k2bqha` | `quiet_intermediate_candidate` | `sleep_combination_fully_reactivated` | `sleep_combination_fully_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` |
| `dio_mcm_episode_0e7qvj1|dio_mcm_episode_1wra2fc` | `quiet_intermediate_candidate` | `sleep_combination_fully_reactivated` | `sleep_combination_partly_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` |
| `dio_mcm_episode_0eghs1d|dio_mcm_episode_0qrlave` | `origin_bound_combination` | `sleep_combination_fully_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` |
| `dio_mcm_episode_0eghs1d|dio_mcm_episode_1k2bqha` | `quiet_intermediate_candidate` | `sleep_combination_fully_reactivated` | `sleep_combination_partly_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` |
| `dio_mcm_episode_0eghs1d|dio_mcm_episode_1wra2fc` | `origin_bound_combination` | `sleep_combination_fully_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` |
| `dio_mcm_episode_0qrlave|dio_mcm_episode_1k2bqha` | `quiet_intermediate_candidate` | `sleep_combination_fully_reactivated` | `sleep_combination_partly_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` |
| `dio_mcm_episode_0qrlave|dio_mcm_episode_1wra2fc` | `origin_bound_combination` | `sleep_combination_fully_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` |
| `dio_mcm_episode_1k2bqha|dio_mcm_episode_1wra2fc` | `quiet_intermediate_candidate` | `sleep_combination_fully_reactivated` | `sleep_combination_partly_reactivated` | `sleep_combination_not_reactivated` | `sleep_combination_not_reactivated` |

## Lesung

Die weiche Sleep-Ausbreitung enthaelt Kandidaten fuer Zwischenrollen: Kombinationen, die in der Ursprungswelt voll ruecklesbar sind und in der ruhigen Folgewelt mindestens teilweise anschliessen. Stress und Mosaik nehmen diese Kandidaten aktuell nicht auf.

## Grenze

Diese Kandidaten sind keine Handlung und keine sichere neue Semantik. Sie sind eine passive Messspur fuer Offline-Kombinationen, die spaeter teilweise wieder Weltnaehe finden.

## Passiver Speicher

- Speicher: `memory\sleep_intermediate_candidates\passive_sleep_intermediate_candidates.json`
- gespeicherte Kandidaten gesamt: `7`
