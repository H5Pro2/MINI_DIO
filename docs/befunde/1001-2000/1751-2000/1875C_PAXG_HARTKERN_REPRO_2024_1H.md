# 1875C - PAXG-Hartkern: Reproduktion 2024 1h

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1874C_PAXG_HARTKERN_2024_1H.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `fehlt_im_folgefenster:558; lokale_qualitaet_wird_offen:23; lokale_qualitaet_reproduziert:19; lokale_qualitaet_wird_nullnah:17; qualitaet_reproduziert:11; lokale_qualitaet_wird_kernnah:9; lokale_qualitaet_wird_nachhallnah:8; lokale_qualitaet_driftet:6`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `fehlt_im_folgefenster:394; lokale_qualitaet_reproduziert:19; lokale_qualitaet_wird_offen:15; lokale_qualitaet_wird_kernnah:7; lokale_qualitaet_wird_nullnah:6; lokale_qualitaet_driftet:3; lokale_qualitaet_wird_nachhallnah:2`
- Asset-Profil: `SOL::fehlt_im_folgefenster:135; XRP::fehlt_im_folgefenster:135; BTC::fehlt_im_folgefenster:126; DOGE::fehlt_im_folgefenster:120; PAXG::fehlt_im_folgefenster:42; PAXG::lokale_qualitaet_wird_offen:23; PAXG::lokale_qualitaet_reproduziert:19; PAXG::lokale_qualitaet_wird_nullnah:17; PAXG::qualitaet_reproduziert:11; PAXG::lokale_qualitaet_wird_kernnah:9; PAXG::lokale_qualitaet_wird_nachhallnah:8; PAXG::lokale_qualitaet_driftet:6`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `fehlt_im_folgefenster` | 558 | 0.857 |
| `lokale_qualitaet_wird_offen` | 23 | 0.035 |
| `lokale_qualitaet_reproduziert` | 19 | 0.029 |
| `lokale_qualitaet_wird_nullnah` | 17 | 0.026 |
| `qualitaet_reproduziert` | 11 | 0.017 |
| `lokale_qualitaet_wird_kernnah` | 9 | 0.014 |
| `lokale_qualitaet_wird_nachhallnah` | 8 | 0.012 |
| `lokale_qualitaet_driftet` | 6 | 0.009 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| PAXG | `dio_04uf` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_ohne_nullfamilie:1` | `phase_nullnah:1` |
| PAXG | `dio_09bn` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:2` | `phase_nullnah:1` |
| PAXG | `dio_0dd2` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_0dd2` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_0nlj` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3` | `phase_nullnah:1` |
| PAXG | `dio_0obq` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_0pz6` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| PAXG | `dio_0pz6` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| PAXG | `dio_104t` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:1; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_14wj` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_kernnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_155c` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_17ct` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| PAXG | `dio_19pg` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:2; phase_offen_gemischt:1` | `phase_nullnah:1` |
| PAXG | `dio_19pg` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:2; phase_offen_gemischt:1` | `phase_nullnah:1` |
| PAXG | `dio_1ewh` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nullnah:2; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1ewh` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1kpz` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:2; phase_offen_gemischt:1` | `phase_nullnah:1` |
| PAXG | `dio_1lsu` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1q85` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_00ja` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:3; phase_offen_gemischt:2; phase_kernnah:1` | `` |
| BTC | `dio_00ly` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:4; phase_offen_gemischt:2` | `` |
| BTC | `dio_00ly` | `mitte` | `phase_nachhallnah_ohne_kern` | `fehlt` | `fehlt_im_folgefenster` | `phase_nachhallnah_ohne_kern:3; phase_offen_gemischt:2; phase_nullnah:1` | `` |
| BTC | `dio_00ly` | `spaet` | `phase_offen_gemischt` | `fehlt` | `fehlt_im_folgefenster` | `phase_offen_gemischt:5; phase_nachhallnah_ohne_kern:1` | `` |
| BTC | `dio_04uf` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:5; phase_kernnah:1` | `` |
| BTC | `dio_04uf` | `mitte` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `` |
| BTC | `dio_04uf` | `spaet` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:4; phase_offen_gemischt:2` | `` |
| BTC | `dio_05yg` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:3; phase_offen_gemischt:1` | `` |
| BTC | `dio_06er` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:5; phase_offen_gemischt:1` | `` |
| BTC | `dio_06er` | `mitte` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `` |
| BTC | `dio_06er` | `spaet` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:2; phase_offen_gemischt:1` | `` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.
