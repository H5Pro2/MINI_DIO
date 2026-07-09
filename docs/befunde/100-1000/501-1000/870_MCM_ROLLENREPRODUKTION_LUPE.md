# MCM-Rollenreproduktion Lupe

## Zweck

Diese Diagnose liest nicht mehr die globale Pfadverteilung, sondern die konkrete Rollenwiederkehr einzelner Tokens zwischen `864` und `868`.
Sie prueft passiv, welche Bruecken, Randlagen und jungen Oberflaechen ihre Rolle behalten, wechseln oder nachreifen.

## Klassenbestand

| Pfadklasse | 864 | 868 |
|---|---:|---:|
| brueckenpfad | 18 | 19 |
| randpfad | 3 | 3 |
| junge_oberflaeche | 30 | 29 |
| stabile_insel | 14 | 11 |
| rekoppelnder_pfad | 41 | 24 |
| offener_driftpfad | 27 | 16 |
| gemischter_pfad | 9 | 1 |

## Rollenbeziehungen

| Beziehung | Anzahl |
|---|---:|
| junge_spur_reift | 5 |
| neu_aufgetaucht | 24 |
| offenheit_rekoppelt | 6 |
| reife_oeffnet | 2 |
| rollenstabil | 47 |
| rollenwechsel | 19 |
| verschwunden | 63 |

## Zielrollen

- Stabile Brueckenpfade: `12`
- Stabile Randpfade: `3`
- Junge Oberflaechen bleiben jung: `8`
- Junge Oberflaechen reifen in tragendere Rollen: `5`

### Stabile Brueckenpfade

- `dio_mcm_episode_05lquqm`
- `dio_mcm_episode_0b7nep9`
- `dio_mcm_episode_0db07p4`
- `dio_mcm_episode_0e7qvj1`
- `dio_mcm_episode_0jbl5pq`
- `dio_mcm_episode_0mji3u6`
- `dio_mcm_episode_0qzjuvj`
- `dio_mcm_episode_18l3thm`
- `dio_mcm_episode_18n06fj`
- `dio_mcm_episode_1al8fjz`
- `dio_mcm_episode_1joiyc3`
- `dio_mcm_episode_1xx3u1e`

### Stabile Randpfade

- `dio_mcm_episode_0mm85pw`
- `dio_mcm_episode_0mw7rev`
- `dio_mcm_episode_102i30n`

### Nachreifende Junge Oberflaechen

- `dio_mcm_episode_0l3i7ey` -> `brueckenpfad`
- `dio_mcm_episode_0mvjoir` -> `brueckenpfad`
- `dio_mcm_episode_0rsf867` -> `rekoppelnder_pfad`
- `dio_mcm_episode_1f4jh6c` -> `rekoppelnder_pfad`
- `dio_mcm_episode_1fx4022` -> `rekoppelnder_pfad`

## Klassenuebergaenge

| 864 | 868 | Anzahl |
|---|---|---:|
| brueckenpfad | brueckenpfad | 12 |
| brueckenpfad | junge_oberflaeche | 1 |
| brueckenpfad | offener_driftpfad | 1 |
| brueckenpfad | stabile_insel | 2 |
| gemischter_pfad | gemischter_pfad | 1 |
| gemischter_pfad | junge_oberflaeche | 2 |
| gemischter_pfad | rekoppelnder_pfad | 1 |
| junge_oberflaeche | brueckenpfad | 2 |
| junge_oberflaeche | junge_oberflaeche | 8 |
| junge_oberflaeche | offener_driftpfad | 5 |
| junge_oberflaeche | rekoppelnder_pfad | 3 |
| offener_driftpfad | brueckenpfad | 2 |
| offener_driftpfad | junge_oberflaeche | 4 |
| offener_driftpfad | offener_driftpfad | 6 |
| offener_driftpfad | rekoppelnder_pfad | 3 |
| randpfad | randpfad | 3 |
| rekoppelnder_pfad | rekoppelnder_pfad | 9 |
| rekoppelnder_pfad | stabile_insel | 1 |
| stabile_insel | brueckenpfad | 1 |
| stabile_insel | junge_oberflaeche | 1 |
| stabile_insel | offener_driftpfad | 1 |
| stabile_insel | rekoppelnder_pfad | 2 |
| stabile_insel | stabile_insel | 8 |

## Befund

Randrollen bleiben konkret reproduzierbar: dieselben Tokens koennen erneut randnah bleiben. Das stuetzt die Lesart, dass Randnaehe nicht bloss Rauschen ist.
Brueckenrollen sind nicht nur global stabil, sondern auch teilweise tokenstabil. Das ist ein starker Hinweis auf wiederkehrende Uebergangsfunktionen im MCM-Feld.
Ein Teil junger Oberflaechen reift in stabilere, rekoppelnde oder brueckenartige Rollen. Das passt zur Idee, dass Oberflaeche nicht wertlos ist, sondern Vorform spaeterer Bedeutung sein kann.

## Wie es weitergeht

Als naechstes sollte die Lupe an den stabilen Brueckenpfaden ansetzen: Welche Weltmerkmale halten diese Bruecken aktiv, und unterscheiden sie sich von jungen Oberflaechen, die nicht nachreifen?
