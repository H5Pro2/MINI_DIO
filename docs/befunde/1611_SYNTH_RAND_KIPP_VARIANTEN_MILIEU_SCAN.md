# SYNTH_RAND_KIPP Varianten Milieu-Scan

Stand: 2026-07-06 10:28:20

## Grundfrage

Welche Rand-/Kipp-Variation erzeugt Selektivitaet bei gleicher Rollenbreite?

## Unterpruefung

Randphase, Rekopplungslaenge und Phasenordnung werden variiert, ohne die MCM-Feldlogik zu veraendern.
Die Diagnose ist passiv und erzeugt keine Handlung.

## Klassenverteilung

- `einzelrekopplung`: `13`
- `uebergang_mit_randkontakt`: `8`

## Fenster

| Welt | Start | Klasse | Rollen | Dauerrollen | Lange Rollen | Strain | Rekopplung | Carry | Strain-Q | Top-Rollen |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| RAND_KIPP_SHORT | 4000 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7456 | 0.5963 | 0.1259 | dio_mcm_episode_0wjn8vm:field_carried:1144; dio_mcm_episode_1bdmoa8:field_carried:849; dio_mcm_episode_15kj0zg:field_strained:1 |
| RAND_KIPP_RECOUP | 6000 | uebergang_mit_randkontakt | 3 | 2 | 1 | 1 | 0.7444 | 0.5956 | 0.1263 | dio_mcm_episode_0wjn8vm:field_carried:1894; dio_mcm_episode_1bdmoa8:field_carried:99; dio_mcm_episode_145zr64:field_strained:1 |
| RAND_KIPP_RECOUP | 5000 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7442 | 0.5945 | 0.1265 | dio_mcm_episode_1bdmoa8:field_carried:1099; dio_mcm_episode_137ak0z:field_carried:894; dio_mcm_episode_145zr64:field_strained:1 |
| RAND_KIPP_SHIFT | 2000 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7381 | 0.5855 | 0.1293 | dio_mcm_episode_0wjn8vm:field_carried:1294; dio_mcm_episode_1bdmoa8:field_carried:699; dio_mcm_episode_0d2gm2j:field_strained:1 |
| RAND_KIPP_SHORT | 3000 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7408 | 0.5859 | 0.1252 | dio_mcm_episode_11c3uxd:field_carried:1849; dio_mcm_episode_1rhsska:field_carried:144; dio_mcm_episode_15kj0zg:field_strained:1 |
| RAND_KIPP_SHORT | 0 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7342 | 0.5768 | 0.1331 | dio_mcm_episode_0v5p8er:field_carried:1394; dio_mcm_episode_1bdmoa8:field_carried:599; dio_mcm_episode_15uimof:field_strained:1 |
| RAND_KIPP_RECOUP | 0 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7272 | 0.5686 | 0.1397 | dio_mcm_episode_1q3us3f:field_carried:1394; dio_mcm_episode_1bdmoa8:field_carried:599; dio_mcm_episode_15uimof:field_strained:1 |
| RAND_KIPP_SHIFT | 0 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7272 | 0.5686 | 0.1397 | dio_mcm_episode_1q3us3f:field_carried:1394; dio_mcm_episode_1bdmoa8:field_carried:599; dio_mcm_episode_15uimof:field_strained:1 |
| RAND_KIPP_SHIFT | 6000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7567 | 0.6129 | 0.1192 | dio_mcm_episode_1v8o9kh:field_carried:1994 |
| RAND_KIPP_SHORT | 6000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7565 | 0.6147 | 0.1177 | dio_mcm_episode_1v8o9kh:field_carried:1994 |
| RAND_KIPP_RECOUP | 4000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7513 | 0.6054 | 0.1205 | dio_mcm_episode_1v8o9kh:field_carried:1994 |
| RAND_KIPP_SHORT | 5000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7493 | 0.6037 | 0.1244 | dio_mcm_episode_0d9qets:field_carried:1994 |
| RAND_KIPP_SHIFT | 5000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7474 | 0.6002 | 0.1251 | dio_mcm_episode_0d9qets:field_carried:1994 |
| RAND_KIPP_RECOUP | 3000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7385 | 0.5811 | 0.1254 | dio_mcm_episode_0d9qets:field_carried:1994 |
| RAND_KIPP_SHORT | 2000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7353 | 0.5780 | 0.1285 | dio_mcm_episode_0d9qets:field_carried:1994 |
| RAND_KIPP_SHIFT | 1000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7237 | 0.5614 | 0.1399 | dio_mcm_episode_04nzkto:field_carried:1994 |
| RAND_KIPP_SHORT | 1000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7281 | 0.5658 | 0.1340 | dio_mcm_episode_0f7nmol:field_carried:1994 |
| RAND_KIPP_SHIFT | 4000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7314 | 0.5713 | 0.1306 | dio_mcm_episode_04dzz4p:field_carried:1994 |
| RAND_KIPP_RECOUP | 2000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7293 | 0.5696 | 0.1321 | dio_mcm_episode_04dzz4p:field_carried:1994 |
| RAND_KIPP_SHIFT | 3000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7289 | 0.5680 | 0.1314 | dio_mcm_episode_04dzz4p:field_carried:1994 |
| RAND_KIPP_RECOUP | 1000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7194 | 0.5535 | 0.1407 | dio_mcm_episode_04nzkto:field_carried:1994 |

## Lesung

Die Fenstersuche trennt Asset-Faerbung von lokaler Feldlage. Entscheidend ist nicht, welches Asset gelesen wird, sondern ob das konkrete Fenster mehrere MCM-Feldrollen hervorbringt.

## Wie es weitergeht

Als naechstes sollte der staerkste neu gefundene Uebergangs- oder Mehrrollen-Kandidat als Real-Sleep-Real-Kette mit Sleep-Reorganisation reproduziert werden.
