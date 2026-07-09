# Synthetische Randrollen-Null-Nachhall-Fenstersuche

Stand: 2026-07-06 10:14:38

## Grundfrage

Gibt es synthetische 5-Rollen-Fenster mit niedrigerem Nachhall als SYNTH_RAND_KIPP?

## Unterpruefung

Vorhandene Randrollen-, Mosaik- und Nullkontrollwelten werden passiv nach Rollenbreite und Nachhall gelesen.
Die Diagnose ist passiv und erzeugt keine Handlung.

## Klassenverteilung

- `einzelrekopplung`: `17`

## Fenster

| Welt | Start | Klasse | Rollen | Dauerrollen | Lange Rollen | Strain | Rekopplung | Carry | Strain-Q | Top-Rollen |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| RANDROLLEN_SHIFTED | 0 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7178 | 0.5481 | 0.1402 | dio_mcm_episode_0bio6c8:field_carried:1194 |
| RANDROLLEN_INTERWOVEN | 600 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7208 | 0.5513 | 0.1373 | dio_mcm_episode_0f7nmol:field_carried:1194 |
| RANDROLLEN_MOSAIC | 0 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7169 | 0.5443 | 0.1406 | dio_mcm_episode_0dgle71:field_carried:1194 |
| RANDROLLEN_MOSAIC_3600 | 0 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7169 | 0.5443 | 0.1406 | dio_mcm_episode_0dgle71:field_carried:1194 |
| RANDROLLEN_MOSAIC_3600 | 1200 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7169 | 0.5443 | 0.1406 | dio_mcm_episode_0dgle71:field_carried:1194 |
| RANDROLLEN_MOSAIC_3600 | 2400 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7169 | 0.5443 | 0.1406 | dio_mcm_episode_0dgle71:field_carried:1194 |
| RANDROLLEN_INTERWOVEN | 0 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7170 | 0.5444 | 0.1403 | dio_mcm_episode_0dgle71:field_carried:1194 |
| RANDROLLEN_MOSAIC_3600 | 600 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7166 | 0.5439 | 0.1407 | dio_mcm_episode_0dgle71:field_carried:1194 |
| RANDROLLEN_MOSAIC_3600 | 1800 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7166 | 0.5439 | 0.1407 | dio_mcm_episode_0dgle71:field_carried:1194 |
| RANDROLLEN_INTERWOVEN | 1200 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7166 | 0.5440 | 0.1404 | dio_mcm_episode_0dgle71:field_carried:1194 |
| RANDROLLEN_START_END | 0 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7183 | 0.5477 | 0.1402 | dio_mcm_episode_0ko7wqc:field_carried:1194 |
| NULL_RANDOM_SIGN | 1200 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7058 | 0.5218 | 0.1432 | dio_mcm_episode_0dgle71:field_carried:1194 |
| NULL_RANDOM_SIGN | 0 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7060 | 0.5214 | 0.1433 | dio_mcm_episode_0dgle71:field_carried:1194 |
| NULL_RANDOM_SIGN | 600 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7041 | 0.5206 | 0.1447 | dio_mcm_episode_0dgle71:field_carried:1194 |
| NULL_SHUFFLE | 1200 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.6964 | 0.5096 | 0.1532 | dio_mcm_episode_1joiyc3:field_carried:1194 |
| NULL_SHUFFLE | 600 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.6963 | 0.5089 | 0.1526 | dio_mcm_episode_1joiyc3:field_carried:1194 |
| NULL_SHUFFLE | 0 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.6951 | 0.5078 | 0.1542 | dio_mcm_episode_1joiyc3:field_carried:1194 |

## Lesung

Die Fenstersuche trennt Asset-Faerbung von lokaler Feldlage. Entscheidend ist nicht, welches Asset gelesen wird, sondern ob das konkrete Fenster mehrere MCM-Feldrollen hervorbringt.
