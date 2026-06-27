# MCM-Token Rohwelt-Segmentlupe

## Zweck

Diese Diagnose liest konkrete Kontaktsegmente fuer ausgewaehlte MCM-Episodentokens.
Sie betrachtet Vorfenster, Kontaktfenster und Nachfenster direkt aus den `episodes.csv`-Spuren.

## Uebersicht

| Token | Segmente | Welten | mittlere Dauer | Richtung im Kontakt | Effekt im Kontakt |
|---|---:|---:|---:|---|---|
| dio_mcm_episode_0v5p8er | 16 | 4 | 125.81 | seitwaerts:16 | stabil:15; tragend_unruhig:1 |
| dio_mcm_episode_14l8khu | 18 | 3 | 50.33 | seitwaerts:18 | stabil:17; tragend_unruhig:1 |
| dio_mcm_episode_1q3us3f | 26 | 6 | 67.81 | seitwaerts:26 | stabil:25; tragend_unruhig:1 |
| dio_mcm_episode_1xx3u1e | 23 | 4 | 133.04 | seitwaerts:23 | stabil:21; tragend_unruhig:2 |

## Tokenbefunde

### `dio_mcm_episode_0v5p8er`

- Welten: `DOGE_2025_5M:10; XRP_2025_5M:4; SYNTH_BRUCH_RAND:1; SYNTH_RAND:1`
- Lautheit Kontakt minus Vorfenster: `+0.0297`
- Unschaerfe Kontakt minus Vorfenster: `-0.0118`
- Rekopplung Kontakt minus Vorfenster: `-0.0028`
- Strain Kontakt minus Vorfenster: `+0.0024`

### `dio_mcm_episode_14l8khu`

- Welten: `DOGE_2025_5M:15; XRP_2025_5M:2; SYNTH_RAND:1`
- Lautheit Kontakt minus Vorfenster: `-0.0144`
- Unschaerfe Kontakt minus Vorfenster: `-0.0251`
- Rekopplung Kontakt minus Vorfenster: `+0.0034`
- Strain Kontakt minus Vorfenster: `-0.0052`

### `dio_mcm_episode_1q3us3f`

- Welten: `XRP_2025_5M:14; DOGE_2024_5M:3; XRP_2024_5M:3; DOGE_2025_5M:2; PAXG_2024_5M:2; SYNTH_RAND:2`
- Lautheit Kontakt minus Vorfenster: `-0.0191`
- Unschaerfe Kontakt minus Vorfenster: `-0.0201`
- Rekopplung Kontakt minus Vorfenster: `+0.0028`
- Strain Kontakt minus Vorfenster: `-0.0053`

### `dio_mcm_episode_1xx3u1e`

- Welten: `PAXG_2025_5M:13; XRP_2024_5M:8; DOGE_2024_5M:1; XRP_2025_5M:1`
- Lautheit Kontakt minus Vorfenster: `+0.0005`
- Unschaerfe Kontakt minus Vorfenster: `+0.0087`
- Rekopplung Kontakt minus Vorfenster: `-0.0015`
- Strain Kontakt minus Vorfenster: `+0.0022`

## Befund

Die Segmentlupe trennt Tokenoberflaeche von Kontaktlage.
Wenn ein Token im Kontakt lauter/unschaerfer und weniger rekoppelnd wird, passt das zur Driftlesung.
Wenn ein Token im Kontakt leiser/schaerfer oder rekoppelnder wird, passt das zur Reifungs- oder Rueckbindungslesung.

## Wie es weitergeht

Als naechstes sollten die Segmentbefunde gegen die Driftlupe verbunden werden: fuer jeden Token ein Kurzurteil, ob der Zonenwechsel eher Weltphase, Rezeptoraufnahme oder MCM-Drift ist.
