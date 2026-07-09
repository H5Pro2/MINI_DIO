# Synthetische Milieu-Nachhall-Fenstersuche

Stand: 2026-07-06 10:08:26

## Grundfrage

Welche synthetischen Welten erzeugen niedrigen oder hohen Nachhall und wie koppelt das an Rollenbreite?

## Unterpruefung

Harmonische, Bruch-/Rand-, Randdominanz- und Zeitdehnungswelten werden als Gegenprobe zum selektiven SYNTH_RAND_KIPP-Fenster gelesen.
Die Diagnose ist passiv und erzeugt keine Handlung.

## Klassenverteilung

- `einzelrekopplung`: `4`
- `uebergang_mit_randkontakt`: `7`

## Fenster

| Welt | Start | Klasse | Rollen | Dauerrollen | Lange Rollen | Strain | Rekopplung | Carry | Strain-Q | Top-Rollen |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| BRUCH_RAND_A | 0 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7509 | 0.6048 | 0.1218 | dio_mcm_episode_0wjn8vm:field_carried:1294; dio_mcm_episode_1bdmoa8:field_carried:699; dio_mcm_episode_15uimof:field_strained:1 |
| BRUCH_RAND_A | 4000 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7502 | 0.6029 | 0.1221 | dio_mcm_episode_0wjn8vm:field_carried:1094; dio_mcm_episode_1bdmoa8:field_carried:899; dio_mcm_episode_0e6i6ce:field_strained:1 |
| RAND_DOMINANZ_A | 4000 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7427 | 0.5919 | 0.1272 | dio_mcm_episode_1bdmoa8:field_carried:1399; dio_mcm_episode_1q3us3f:field_carried:594; dio_mcm_episode_0d2gm2j:field_strained:1 |
| RAND_KIPP | 4000 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7427 | 0.5919 | 0.1272 | dio_mcm_episode_1bdmoa8:field_carried:1399; dio_mcm_episode_1q3us3f:field_carried:594; dio_mcm_episode_0d2gm2j:field_strained:1 |
| ZEITDEHNUNG_KOMPAKT | 0 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7364 | 0.5774 | 0.1273 | dio_mcm_episode_0wjn8vm:field_carried:1644; dio_mcm_episode_1bdmoa8:field_carried:349; dio_mcm_episode_15uimof:field_strained:1 |
| RAND_DOMINANZ_A | 0 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7272 | 0.5686 | 0.1397 | dio_mcm_episode_1q3us3f:field_carried:1394; dio_mcm_episode_1bdmoa8:field_carried:599; dio_mcm_episode_15uimof:field_strained:1 |
| RAND_KIPP | 0 | uebergang_mit_randkontakt | 3 | 2 | 2 | 1 | 0.7272 | 0.5686 | 0.1397 | dio_mcm_episode_1q3us3f:field_carried:1394; dio_mcm_episode_1bdmoa8:field_carried:599; dio_mcm_episode_15uimof:field_strained:1 |
| HARMONIE_KOMPAKT | 0 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7521 | 0.6071 | 0.1200 | dio_mcm_episode_1v8o9kh:field_carried:1994 |
| BRUCH_RAND_A | 2000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7307 | 0.5685 | 0.1301 | dio_mcm_episode_0d9qets:field_carried:1994 |
| RAND_DOMINANZ_A | 2000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7293 | 0.5696 | 0.1321 | dio_mcm_episode_04dzz4p:field_carried:1994 |
| RAND_KIPP | 2000 | einzelrekopplung | 1 | 1 | 1 | 0 | 0.7293 | 0.5696 | 0.1321 | dio_mcm_episode_04dzz4p:field_carried:1994 |

## Lesung

Die Fenstersuche trennt Asset-Faerbung von lokaler Feldlage. Entscheidend ist nicht, welches Asset gelesen wird, sondern ob das konkrete Fenster mehrere MCM-Feldrollen hervorbringt.

## Wie es weitergeht

Als naechstes sollte der staerkste Hoch-Nachhall-Uebergang als Real-Sleep-Real-Kette reproduziert werden. Ziel ist zu pruefen, ob hoher Nachhall allein schon selektive Offline-Reorganisation erzeugt.
