# SYNTH_RAND_KIPP start0 Segmentanalyse 500

Stand: 2026-07-06 11:25:26

## Grundfrage

Welche Binnenbereiche tragen mehrere Rollen?

## Unterpruefung

Das bekannte selektive Fenster wird in ueberlappende 500er-Binnensegmente zerlegt. Diagnose passiv.
Die Diagnose ist passiv und erzeugt keine Handlung.

## Klassenverteilung

- `einzelrekopplung`: `5`
- `uebergang_mit_randkontakt`: `2`

## Fenster

| Welt | Start | Klasse | Rollen | Dauerrollen | Lange Rollen | Strain | Rekopplung | Carry | Strain-Q | Top-Rollen |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| SYNTH_RAND_KIPP_START0 | 1000 | uebergang_mit_randkontakt | 3 | 2 | 1 | 1 | 0.7322 | 0.5713 | 0.1310 | dio_mcm_episode_1bdmoa8:field_carried:399; dio_mcm_episode_1u741ze:field_carried:94; dio_mcm_episode_0qvqqtg:field_strained:1 |
| SYNTH_RAND_KIPP_START0 | 1250 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7033 | 0.5250 | 0.1506 | dio_mcm_episode_0mji3u6:field_carried:344; dio_mcm_episode_1bdmoa8:field_carried:149; dio_mcm_episode_0eghs1d:field_strained:1 |
| SYNTH_RAND_KIPP_START0 | 0 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7541 | 0.6085 | 0.1194 | dio_mcm_episode_1v8o9kh:field_carried:494 |
| SYNTH_RAND_KIPP_START0 | 250 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7506 | 0.5988 | 0.1187 | dio_mcm_episode_1v8o9kh:field_carried:494 |
| SYNTH_RAND_KIPP_START0 | 750 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7497 | 0.5977 | 0.1172 | dio_mcm_episode_0d9qets:field_carried:494 |
| SYNTH_RAND_KIPP_START0 | 500 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7496 | 0.5954 | 0.1168 | dio_mcm_episode_0d9qets:field_carried:494 |
| SYNTH_RAND_KIPP_START0 | 1500 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.6886 | 0.5060 | 0.1610 | dio_mcm_episode_1rzvd1k:field_carried:494 |

## Lesung

Die Fenstersuche trennt Asset-Faerbung von lokaler Feldlage. Entscheidend ist nicht, welches Asset gelesen wird, sondern ob das konkrete Fenster mehrere MCM-Feldrollen hervorbringt.

## Wie es weitergeht

Als naechstes sollte der staerkste neu gefundene Uebergangs- oder Mehrrollen-Kandidat als Real-Sleep-Real-Kette mit Sleep-Reorganisation reproduziert werden.
