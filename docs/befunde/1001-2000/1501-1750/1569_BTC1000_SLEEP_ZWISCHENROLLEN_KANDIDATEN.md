# BTC1000 Sleep-Zwischenrollen Kandidaten

Stand: 2026-07-05 21:24:58

## Zweck

Diese Auswertung prueft, ob eine andere Ausgangswelt denselben Zwischenrollen-Speicher erweitert oder nur die bisherigen SOL-Kandidaten bestaetigt.

Als Ausgangswelt wurde ein kontrolliertes BTC-2024-5m-Fenster mit 1000 Zeilen verwendet.

Eine Zwischenrolle ist hier noch keine neue autonome Bedeutung. Gemeint ist nur:

```text
Eine Offline-Kombination kommt bei gleicher Welt voll zurueck
und findet in einer verwandten Folgewelt zumindest teilweise Anschluss.
```

Die Auswertung bleibt passiv: keine Handlung, keine Richtung, kein Gate.

## Zaehler

- `broad_intermediate_candidate`: `3`

## Kandidaten

| Kombination | Zustand | gleiche Welt | Ruhewelt | Stress | Mosaik |
|---|---|---|---|---|---|
| `dio_mcm_episode_0e7qvj1|dio_mcm_episode_0sjrih9` | `broad_intermediate_candidate` | `sleep_combination_fully_reactivated` | `sleep_combination_partly_reactivated` | `sleep_combination_partly_reactivated` | `sleep_combination_fully_reactivated` |
| `dio_mcm_episode_0e7qvj1|dio_mcm_episode_1k2bqha` | `broad_intermediate_candidate` | `sleep_combination_fully_reactivated` | `sleep_combination_fully_reactivated` | `sleep_combination_fully_reactivated` | `sleep_combination_partly_reactivated` |
| `dio_mcm_episode_0sjrih9|dio_mcm_episode_1k2bqha` | `broad_intermediate_candidate` | `sleep_combination_fully_reactivated` | `sleep_combination_partly_reactivated` | `sleep_combination_partly_reactivated` | `sleep_combination_partly_reactivated` |

## Lesung

Die BTC-Ausgangswelt bildet ein engeres Offline-Kombinationsfeld als die fruehere SOL-Weichphase:

```text
BTC1000: 3 Kombinationen
SOL-Weichphase: 10 Kombinationen
```

Alle drei BTC-Kombinationen werden in der gleichen BTC-Welt voll rueckgelesen. Anders als bei der frueheren SOL-Pruefung bleiben sie aber nicht nur in der ruhigen Folgewelt anschlussfaehig, sondern auch in BTC-1h und in der Mosaik-/Altsequenz mindestens teilweise sichtbar.

Damit sind sie als `broad_intermediate_candidate` zu lesen.

Wichtig ist der Speicherbefund:

```text
vorher: 7 Kandidaten
nachher: 9 Kandidaten
```

Ein bereits bekannter Kandidat wurde erneut getroffen:

```text
dio_mcm_episode_0e7qvj1 | dio_mcm_episode_1k2bqha
seen_count: 2 -> 3
```

Zwei neue BTC-nahe Kandidaten kamen dazu:

```text
dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0sjrih9
dio_mcm_episode_0sjrih9 | dio_mcm_episode_1k2bqha
```

Damit bleibt die fruehere SOL-Kandidatengruppe nicht isoliert. Mindestens ein Kernkandidat wird assetuebergreifend erneut beruehrt, waehrend BTC zwei eigene Erweiterungen daneben legt.

## Grenze

Diese Kandidaten sind keine Handlung und keine sichere neue Semantik. Sie sind eine passive Messspur fuer Offline-Kombinationen, die spaeter teilweise wieder Weltnaehe finden.

## Passiver Speicher

- Speicher: `memory\sleep_intermediate_candidates\passive_sleep_intermediate_candidates.json`
- gespeicherte Kandidaten gesamt: `9`
