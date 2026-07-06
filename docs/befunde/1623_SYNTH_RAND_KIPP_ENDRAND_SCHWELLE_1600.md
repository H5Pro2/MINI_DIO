# SYNTH_RAND_KIPP Endrand-Schwelle 1600

Stand: 2026-07-06 11:40:21

## Grundfrage

Ab wann kippt das breite Rollenfeld in selektive Offline-Rekopplung?

## Unterpruefung

Fenster start250 mit erweitertem Endrand bis Zeile 1850. Diagnose passiv.
Die Diagnose ist passiv und erzeugt keine Handlung.

## Klassenverteilung

- `mehrrollen_kandidat`: `1`

## Fenster

| Welt | Start | Klasse | Rollen | Dauerrollen | Lange Rollen | Strain | Rekopplung | Carry | Strain-Q | Top-Rollen |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| SYNTH_RAND_KIPP_START0 | 250 | mehrrollen_kandidat | 5 | 3 | 3 | 2 | 0.7347 | 0.5799 | 0.1345 | dio_mcm_episode_1k5qdaq:field_carried:899; dio_mcm_episode_0mji3u6:field_carried:444; dio_mcm_episode_1bdmoa8:field_carried:249; dio_mcm_episode_0qvqqtg:field_strained:1; dio_mcm_episode_15uimof:field_strained:1 |

## Lesung

Die Fenstersuche trennt Asset-Faerbung von lokaler Feldlage. Entscheidend ist nicht, welches Asset gelesen wird, sondern ob das konkrete Fenster mehrere MCM-Feldrollen hervorbringt.

## Wie es weitergeht

Als naechstes sollte der staerkste neu gefundene Uebergangs- oder Mehrrollen-Kandidat als Real-Sleep-Real-Kette mit Sleep-Reorganisation reproduziert werden.
