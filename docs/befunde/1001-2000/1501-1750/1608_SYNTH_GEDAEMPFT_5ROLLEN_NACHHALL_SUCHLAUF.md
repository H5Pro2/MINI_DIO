# Synthetische gedaempfte 5-Rollen-Nachhall-Suche

Stand: 2026-07-06 10:16:29

## Grundfrage

Kann eine gedaempfte synthetische Rand-/Bruch-Welt Rollenbreite erzeugen, ohne extremen Nachhall zu tragen?

## Unterpruefung

Zwei aus dem vorhandenen MCM-Builder erzeugte gedaempfte Rand-/Bruch-Welten werden in 2000er-Fenstern auf Rollenbreite und Nachhall geprueft.
Die Diagnose ist passiv und erzeugt keine Handlung.

## Klassenverteilung

- `einzelrekopplung`: `11`
- `mehrrollen_kandidat`: `1`
- `uebergang_mit_randkontakt`: `2`

## Fenster

| Welt | Start | Klasse | Rollen | Dauerrollen | Lange Rollen | Strain | Rekopplung | Carry | Strain-Q | Top-Rollen |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| RAND_DOMINANZ_GEDAEMPFT | 0 | mehrrollen_kandidat | 5 | 3 | 3 | 2 | 0.7279 | 0.5647 | 0.1351 | dio_mcm_episode_1q3us3f:field_carried:1250; dio_mcm_episode_1bdmoa8:field_carried:371; dio_mcm_episode_1k5qdaq:field_carried:371; dio_mcm_episode_0eghs1d:field_strained:1; dio_mcm_episode_15kj0zg:field_strained:1 |
| BRUCH_RAND_GEDAEMPFT | 3000 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7510 | 0.6039 | 0.1216 | dio_mcm_episode_0wjn8vm:field_carried:1466; dio_mcm_episode_1bdmoa8:field_carried:527; dio_mcm_episode_15kj0zg:field_strained:1 |
| BRUCH_RAND_GEDAEMPFT | 2000 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7457 | 0.5939 | 0.1231 | dio_mcm_episode_11c3uxd:field_carried:1527; dio_mcm_episode_0wjn8vm:field_carried:466; dio_mcm_episode_15kj0zg:field_strained:1 |
| BRUCH_RAND_GEDAEMPFT | 6000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7585 | 0.6194 | 0.1183 | dio_mcm_episode_1v8o9kh:field_carried:1994 |
| BRUCH_RAND_GEDAEMPFT | 5000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7585 | 0.6193 | 0.1183 | dio_mcm_episode_1v8o9kh:field_carried:1994 |
| BRUCH_RAND_GEDAEMPFT | 4000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7570 | 0.6152 | 0.1180 | dio_mcm_episode_1v8o9kh:field_carried:1994 |
| RAND_DOMINANZ_GEDAEMPFT | 5000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7566 | 0.6147 | 0.1178 | dio_mcm_episode_1v8o9kh:field_carried:1994 |
| RAND_DOMINANZ_GEDAEMPFT | 6000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7565 | 0.6147 | 0.1177 | dio_mcm_episode_1v8o9kh:field_carried:1994 |
| RAND_DOMINANZ_GEDAEMPFT | 4000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7560 | 0.6129 | 0.1177 | dio_mcm_episode_1v8o9kh:field_carried:1994 |
| RAND_DOMINANZ_GEDAEMPFT | 3000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7473 | 0.5993 | 0.1253 | dio_mcm_episode_0d9qets:field_carried:1994 |
| BRUCH_RAND_GEDAEMPFT | 0 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7363 | 0.5786 | 0.1289 | dio_mcm_episode_0d9qets:field_carried:1994 |
| RAND_DOMINANZ_GEDAEMPFT | 2000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7368 | 0.5792 | 0.1286 | dio_mcm_episode_0d9qets:field_carried:1994 |
| BRUCH_RAND_GEDAEMPFT | 1000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7326 | 0.5712 | 0.1292 | dio_mcm_episode_0d9qets:field_carried:1994 |
| RAND_DOMINANZ_GEDAEMPFT | 1000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7289 | 0.5652 | 0.1328 | dio_mcm_episode_0f7nmol:field_carried:1994 |

## Lesung

Die Fenstersuche trennt Asset-Faerbung von lokaler Feldlage. Entscheidend ist nicht, welches Asset gelesen wird, sondern ob das konkrete Fenster mehrere MCM-Feldrollen hervorbringt.
