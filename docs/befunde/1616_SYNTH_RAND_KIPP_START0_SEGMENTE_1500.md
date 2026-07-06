# SYNTH_RAND_KIPP start0 Segmentanalyse 1500

Stand: 2026-07-06 11:25:58

## Grundfrage

Ab welcher Binnenlaenge entsteht die selektive 5-Rollen-Breite?

## Unterpruefung

Das bekannte selektive Fenster wird in ueberlappende 1500er-Binnensegmente zerlegt. Diagnose passiv.
Die Diagnose ist passiv und erzeugt keine Handlung.

## Klassenverteilung

- `mehrrollen_kandidat`: `1`
- `uebergang_mit_randkontakt`: `2`

## Fenster

| Welt | Start | Klasse | Rollen | Dauerrollen | Lange Rollen | Strain | Rekopplung | Carry | Strain-Q | Top-Rollen |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| SYNTH_RAND_KIPP_START0 | 250 | mehrrollen_kandidat | 5 | 3 | 3 | 2 | 0.7364 | 0.5816 | 0.1324 | dio_mcm_episode_1k5qdaq:field_carried:899; dio_mcm_episode_0mji3u6:field_carried:344; dio_mcm_episode_1bdmoa8:field_carried:249; dio_mcm_episode_0qvqqtg:field_strained:1; dio_mcm_episode_15uimof:field_strained:1 |
| SYNTH_RAND_KIPP_START0 | 0 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7469 | 0.5978 | 0.1244 | dio_mcm_episode_0wjn8vm:field_carried:994; dio_mcm_episode_1bdmoa8:field_carried:499; dio_mcm_episode_15uimof:field_strained:1 |
| SYNTH_RAND_KIPP_START0 | 500 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7284 | 0.5702 | 0.1389 | dio_mcm_episode_1bdmoa8:field_carried:899; dio_mcm_episode_0mji3u6:field_carried:594; dio_mcm_episode_0eghs1d:field_strained:1 |

## Lesung

Die Fenstersuche trennt Asset-Faerbung von lokaler Feldlage. Entscheidend ist nicht, welches Asset gelesen wird, sondern ob das konkrete Fenster mehrere MCM-Feldrollen hervorbringt.

## Wie es weitergeht

Als naechstes sollte der staerkste neu gefundene Uebergangs- oder Mehrrollen-Kandidat als Real-Sleep-Real-Kette mit Sleep-Reorganisation reproduziert werden.
