# 1881P - PAXG-Hartkern: Reproduktion Folgefenster

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1880P_PAXG_HARTKERN_FOLGEFENSTER.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `fehlt_im_folgefenster:555; lokale_qualitaet_wird_nullnah:27; lokale_qualitaet_reproduziert:24; qualitaet_reproduziert:18; lokale_qualitaet_wird_offen:10; lokale_qualitaet_wird_kernnah:8; lokale_qualitaet_wird_nachhallnah:6; lokale_qualitaet_driftet:3`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `fehlt_im_folgefenster:391; lokale_qualitaet_reproduziert:24; lokale_qualitaet_wird_nullnah:13; lokale_qualitaet_wird_kernnah:7; lokale_qualitaet_wird_offen:5; lokale_qualitaet_wird_nachhallnah:5; lokale_qualitaet_driftet:1`
- Asset-Profil: `SOL::fehlt_im_folgefenster:135; XRP::fehlt_im_folgefenster:135; BTC::fehlt_im_folgefenster:126; DOGE::fehlt_im_folgefenster:120; PAXG::fehlt_im_folgefenster:39; PAXG::lokale_qualitaet_wird_nullnah:27; PAXG::lokale_qualitaet_reproduziert:24; PAXG::qualitaet_reproduziert:18; PAXG::lokale_qualitaet_wird_offen:10; PAXG::lokale_qualitaet_wird_kernnah:8; PAXG::lokale_qualitaet_wird_nachhallnah:6; PAXG::lokale_qualitaet_driftet:3`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `fehlt_im_folgefenster` | 555 | 0.853 |
| `lokale_qualitaet_wird_nullnah` | 27 | 0.041 |
| `lokale_qualitaet_reproduziert` | 24 | 0.037 |
| `qualitaet_reproduziert` | 18 | 0.028 |
| `lokale_qualitaet_wird_offen` | 10 | 0.015 |
| `lokale_qualitaet_wird_kernnah` | 8 | 0.012 |
| `lokale_qualitaet_wird_nachhallnah` | 6 | 0.009 |
| `lokale_qualitaet_driftet` | 3 | 0.005 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| PAXG | `dio_00ja` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:1; phase_kernnah:1` | `phase_nullnah:1` |
| PAXG | `dio_00ly` | `mitte` | `phase_nachhallnah_ohne_kern` | `phase_nachhallnah_ohne_kern` | `lokale_qualitaet_reproduziert` | `phase_nachhallnah_ohne_kern:3; phase_offen_gemischt:2; phase_kernnah:1` | `phase_nachhallnah_ohne_kern:1` |
| PAXG | `dio_00ly` | `spaet` | `phase_nachhallnah_ohne_kern` | `phase_nachhallnah_ohne_kern` | `lokale_qualitaet_reproduziert` | `phase_nachhallnah_ohne_kern:4; phase_offen_gemischt:1; phase_kernnah:1` | `phase_nachhallnah_ohne_kern:1` |
| PAXG | `dio_06er` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_07o8` | `frueh` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:4; phase_kernnah:2` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_07o8` | `mitte` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:4; phase_kernnah:2` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_07o8` | `spaet` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:4; phase_kernnah:2` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_09bn` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:2` | `phase_nullnah:1` |
| PAXG | `dio_0dd2` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_0dd2` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_0m9z` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_0m9z` | `spaet` | `phase_nachhallnah_ohne_kern` | `phase_nachhallnah_ohne_kern` | `lokale_qualitaet_reproduziert` | `phase_nachhallnah_ohne_kern:3; phase_offen_gemischt:2; phase_nullnah:1` | `phase_nachhallnah_ohne_kern:1` |
| PAXG | `dio_0z9t` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_104t` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:1; phase_kernnah:1; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_17ct` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_19pg` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:2; phase_offen_gemischt:1` | `phase_nullnah:1` |
| PAXG | `dio_1ewh` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nullnah:2; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1ewh` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1kpz` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_kernnah:1` | `phase_nullnah:1` |
| PAXG | `dio_1lsu` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1q85` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| PAXG | `dio_1xrt` | `frueh` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:4` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_1xrt` | `mitte` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:4` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_1xrt` | `spaet` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:4` | `phase_ohne_nullfamilie:1` |
| BTC | `dio_00ja` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:3; phase_offen_gemischt:2; phase_kernnah:1` | `` |
| BTC | `dio_00ly` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:4; phase_offen_gemischt:2` | `` |
| BTC | `dio_00ly` | `mitte` | `phase_nachhallnah_ohne_kern` | `fehlt` | `fehlt_im_folgefenster` | `phase_nachhallnah_ohne_kern:3; phase_offen_gemischt:2; phase_nullnah:1` | `` |
| BTC | `dio_00ly` | `spaet` | `phase_offen_gemischt` | `fehlt` | `fehlt_im_folgefenster` | `phase_offen_gemischt:5; phase_nachhallnah_ohne_kern:1` | `` |
| BTC | `dio_04uf` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:5; phase_kernnah:1` | `` |
| BTC | `dio_04uf` | `mitte` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.
