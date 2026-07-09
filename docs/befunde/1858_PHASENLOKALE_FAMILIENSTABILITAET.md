# 1858 - Phasenlokale Familienstabilität

## Grundfrage

Welche Familien bleiben phasenlokal stabil, und welche wirken eher nur durch die geerbte Fensterqualität getragen?

## Methode

- Quelle: `docs\befunde\1857_PHASENLOKALE_ANSCHLUSSQUALITAET.csv`.
- Gruppierung: Asset/Familie/Phase.
- Gelesen wird die Verteilung phasenlokaler Anschlussqualitäten aus 1857.
- Die Zustände beschreiben passive Lesbarkeit, keine Handlung und kein Gate.

## Kurzbefund

- Familien-Phasen-Paare: `651`
- Stabilitätszustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Dominante Phasenqualitäten: `phase_nullnah:303; phase_offen_gemischt:204; phase_ohne_nullfamilie:79; phase_nachhallnah_ohne_kern:42; phase_kernnah:23`
- Asset-Profil: `XRP::phasenlokal_eigenstaendig:101; BTC::phasenlokal_eigenstaendig:100; DOGE::phasenlokal_eigenstaendig:88; SOL::phasenlokal_eigenstaendig:85; PAXG::phasenlokal_eigenstaendig:72; PAXG::geteilt_offen:25; SOL::fenstergetragen_stabil:24; DOGE::geteilt_offen:24; PAXG::fenstergetragen_stabil:20; BTC::geteilt_offen:19; PAXG::einzelbeleg:18; XRP::einzelbeleg:18; SOL::geteilt_offen:17; XRP::geteilt_offen:16; SOL::einzelbeleg:9; BTC::einzelbeleg:6; DOGE::einzelbeleg:6; DOGE::fenstergetragen_stabil:2; BTC::fenstergetragen_stabil:1`
- Phasen-Profil: `mitte::phasenlokal_eigenstaendig:155; frueh::phasenlokal_eigenstaendig:147; spaet::phasenlokal_eigenstaendig:144; spaet::geteilt_offen:35; frueh::geteilt_offen:33; mitte::geteilt_offen:33; frueh::einzelbeleg:19; mitte::einzelbeleg:19; spaet::einzelbeleg:19; spaet::fenstergetragen_stabil:19; frueh::fenstergetragen_stabil:18; mitte::fenstergetragen_stabil:10`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `phasenlokal_eigenstaendig` | 446 | 0.685 |
| `geteilt_offen` | 101 | 0.155 |
| `einzelbeleg` | 57 | 0.088 |
| `fenstergetragen_stabil` | 47 | 0.072 |

## Beispielzeilen

| Asset | Familie | Phase | Zustand | Dominant | Profil | Fensterabweichung | Rekopplung-Edge | Temporal-Edge |
|---|---|---|---|---|---|---:|---:|---:|
| BTC | `dio_06s7` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00446 | -0.02629 |
| BTC | `dio_09bn` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00437 | -0.07264 |
| BTC | `dio_09bn` | `mitte` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00353 | -0.01698 |
| BTC | `dio_0g2r` | `frueh` | `phasenlokal_eigenstaendig` | `phase_offen_gemischt` | `phase_offen_gemischt:6` | 5 | -0.00303 | 0.02832 |
| BTC | `dio_0g2r` | `spaet` | `phasenlokal_eigenstaendig` | `phase_offen_gemischt` | `phase_offen_gemischt:6` | 5 | -0.00353 | -0.00082 |
| BTC | `dio_0h9h` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00335 | -0.00295 |
| BTC | `dio_0l7p` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00440 | -0.00543 |
| BTC | `dio_0obq` | `mitte` | `phasenlokal_eigenstaendig` | `phase_offen_gemischt` | `phase_offen_gemischt:6` | 5 | -0.00199 | 0.00099 |
| BTC | `dio_0oc3` | `spaet` | `phasenlokal_eigenstaendig` | `phase_offen_gemischt` | `phase_offen_gemischt:6` | 5 | -0.00285 | -0.00253 |
| BTC | `dio_0pz6` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00550 | -0.02828 |
| BTC | `dio_0pz6` | `mitte` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00503 | -0.00453 |
| BTC | `dio_0tay` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00291 | -0.04891 |
| BTC | `dio_1492` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00477 | -0.03889 |
| BTC | `dio_1492` | `mitte` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00507 | -0.01430 |
| BTC | `dio_1492` | `spaet` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00495 | -0.00701 |
| BTC | `dio_14wj` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00592 | -0.01429 |
| BTC | `dio_17ct` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00641 | -0.02408 |
| BTC | `dio_17ct` | `mitte` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00343 | -0.00513 |
| BTC | `dio_19pg` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 5 | -0.00395 | -0.06192 |
| DOGE | `dio_09bn` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 6 | -0.00464 | -0.02875 |
| DOGE | `dio_09bn` | `mitte` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 6 | -0.00373 | -0.00559 |
| DOGE | `dio_0l7p` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 6 | -0.00364 | -0.00453 |
| DOGE | `dio_0m9z` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 6 | -0.00246 | -0.00443 |
| DOGE | `dio_0nlj` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 6 | -0.00392 | -0.05674 |
| DOGE | `dio_0nlj` | `spaet` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 6 | -0.00460 | -0.00642 |
| DOGE | `dio_19pg` | `frueh` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 6 | -0.00514 | -0.05112 |
| DOGE | `dio_19pg` | `mitte` | `phasenlokal_eigenstaendig` | `phase_nullnah` | `phase_nullnah:6` | 6 | -0.00262 | -0.01468 |
| PAXG | `dio_0g2r` | `frueh` | `phasenlokal_eigenstaendig` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie:6` | 6 | 0.74104 | 0.75279 |

## Einordnung

Der Bericht trennt zwei Fälle:

- `phasenlokal_eigenstaendig`: Die Familie hat innerhalb einer Phase eine erkennbare lokale Qualität und weicht häufiger vom Fensterprofil ab.
- `fenstergetragen_stabil`: Die Familie ist stabil, wird aber stärker vom Gesamtfenster mitgetragen.

Damit wird die passive Bedeutungsreife präziser. Eine Familie ist nicht nur ein Name und nicht nur eine Fensterrolle.
Sie kann als lokaler Phasenanker gelesen werden, wenn sie unter mehreren Weltfenstern eine eigene Phasenqualität trägt.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese phasenlokal eigenständigen Familien über neue Weltfenster wiederkehren.
Wichtig ist dabei nicht mehr nur `taucht der Name wieder auf`, sondern `taucht dieselbe lokale Phasenqualität wieder auf`.
