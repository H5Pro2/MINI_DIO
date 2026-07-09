# 1881D - DOGE-Hartkern: Reproduktion Folgefenster

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1880D_DOGE_HARTKERN_FOLGEFENSTER.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `fehlt_im_folgefenster:554; lokale_qualitaet_reproduziert:32; lokale_qualitaet_wird_offen:22; lokale_qualitaet_wird_nullnah:14; qualitaet_reproduziert:11; lokale_qualitaet_wird_nachhallnah:10; lokale_qualitaet_driftet:6; lokale_qualitaet_wird_kernnah:2`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `fehlt_im_folgefenster:376; lokale_qualitaet_reproduziert:32; lokale_qualitaet_wird_offen:18; lokale_qualitaet_wird_nachhallnah:9; lokale_qualitaet_wird_nullnah:6; lokale_qualitaet_driftet:4; lokale_qualitaet_wird_kernnah:1`
- Asset-Profil: `PAXG::fehlt_im_folgefenster:135; SOL::fehlt_im_folgefenster:135; XRP::fehlt_im_folgefenster:135; BTC::fehlt_im_folgefenster:126; DOGE::lokale_qualitaet_reproduziert:32; DOGE::fehlt_im_folgefenster:23; DOGE::lokale_qualitaet_wird_offen:22; DOGE::lokale_qualitaet_wird_nullnah:14; DOGE::qualitaet_reproduziert:11; DOGE::lokale_qualitaet_wird_nachhallnah:10; DOGE::lokale_qualitaet_driftet:6; DOGE::lokale_qualitaet_wird_kernnah:2`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `fehlt_im_folgefenster` | 554 | 0.851 |
| `lokale_qualitaet_reproduziert` | 32 | 0.049 |
| `lokale_qualitaet_wird_offen` | 22 | 0.034 |
| `lokale_qualitaet_wird_nullnah` | 14 | 0.022 |
| `qualitaet_reproduziert` | 11 | 0.017 |
| `lokale_qualitaet_wird_nachhallnah` | 10 | 0.015 |
| `lokale_qualitaet_driftet` | 6 | 0.009 |
| `lokale_qualitaet_wird_kernnah` | 2 | 0.003 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| DOGE | `dio_00ja` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| DOGE | `dio_00ly` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| DOGE | `dio_06er` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:1; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| DOGE | `dio_06s7` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| DOGE | `dio_06s7` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:1; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| DOGE | `dio_06s7` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| DOGE | `dio_07uk` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_ohne_nullfamilie:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| DOGE | `dio_09bn` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| DOGE | `dio_0h9h` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| DOGE | `dio_0h9h` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| DOGE | `dio_0nlj` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| DOGE | `dio_0obq` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:2` | `phase_offen_gemischt:1` |
| DOGE | `dio_0oc3` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nullnah:1` | `phase_offen_gemischt:1` |
| DOGE | `dio_0oc3` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nachhallnah_ohne_kern:1; phase_nullnah:1` | `phase_offen_gemischt:1` |
| DOGE | `dio_0pz6` | `spaet` | `phase_nachhallnah_ohne_kern` | `phase_nachhallnah_ohne_kern` | `lokale_qualitaet_reproduziert` | `phase_nachhallnah_ohne_kern:3; phase_nullnah:2; phase_offen_gemischt:1` | `phase_nachhallnah_ohne_kern:1` |
| DOGE | `dio_104t` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| DOGE | `dio_1492` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4` | `phase_nullnah:1` |
| DOGE | `dio_1492` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:1` | `phase_nullnah:1` |
| DOGE | `dio_1492` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:1` | `phase_nullnah:1` |
| DOGE | `dio_14wj` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:1; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| DOGE | `dio_17ct` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:2` | `phase_offen_gemischt:1` |
| DOGE | `dio_19pg` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| DOGE | `dio_19pg` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| DOGE | `dio_1ewh` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| DOGE | `dio_1ewh` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| DOGE | `dio_1kpz` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| DOGE | `dio_1kpz` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| DOGE | `dio_1lsu` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| DOGE | `dio_1pij` | `frueh` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:5` | `phase_ohne_nullfamilie:1` |
| DOGE | `dio_1pij` | `mitte` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:5` | `phase_ohne_nullfamilie:1` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.
