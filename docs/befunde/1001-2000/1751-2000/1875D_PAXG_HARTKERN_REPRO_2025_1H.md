# 1875D - PAXG-Hartkern: Reproduktion 2025 1h

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1874D_PAXG_HARTKERN_2025_1H.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `fehlt_im_folgefenster:552; lokale_qualitaet_reproduziert:26; lokale_qualitaet_wird_nullnah:20; lokale_qualitaet_wird_offen:19; qualitaet_reproduziert:14; lokale_qualitaet_wird_nachhallnah:10; lokale_qualitaet_wird_kernnah:10`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `fehlt_im_folgefenster:388; lokale_qualitaet_reproduziert:26; lokale_qualitaet_wird_offen:13; lokale_qualitaet_wird_nachhallnah:7; lokale_qualitaet_wird_nullnah:7; lokale_qualitaet_wird_kernnah:5`
- Asset-Profil: `SOL::fehlt_im_folgefenster:135; XRP::fehlt_im_folgefenster:135; BTC::fehlt_im_folgefenster:126; DOGE::fehlt_im_folgefenster:120; PAXG::fehlt_im_folgefenster:36; PAXG::lokale_qualitaet_reproduziert:26; PAXG::lokale_qualitaet_wird_nullnah:20; PAXG::lokale_qualitaet_wird_offen:19; PAXG::qualitaet_reproduziert:14; PAXG::lokale_qualitaet_wird_nachhallnah:10; PAXG::lokale_qualitaet_wird_kernnah:10`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `fehlt_im_folgefenster` | 552 | 0.848 |
| `lokale_qualitaet_reproduziert` | 26 | 0.040 |
| `lokale_qualitaet_wird_nullnah` | 20 | 0.031 |
| `lokale_qualitaet_wird_offen` | 19 | 0.029 |
| `qualitaet_reproduziert` | 14 | 0.022 |
| `lokale_qualitaet_wird_nachhallnah` | 10 | 0.015 |
| `lokale_qualitaet_wird_kernnah` | 10 | 0.015 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| PAXG | `dio_04uf` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_ohne_nullfamilie:1` | `phase_nullnah:1` |
| PAXG | `dio_09bn` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:2` | `phase_nullnah:1` |
| PAXG | `dio_0dd2` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:2` | `phase_offen_gemischt:1` |
| PAXG | `dio_0dd2` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_0obq` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_0pz6` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| PAXG | `dio_0pz6` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| PAXG | `dio_0pz6` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| PAXG | `dio_0z9t` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_0z9t` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nachhallnah_ohne_kern:1; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_10dv` | `mitte` | `phase_nachhallnah_ohne_kern` | `phase_nachhallnah_ohne_kern` | `lokale_qualitaet_reproduziert` | `phase_nachhallnah_ohne_kern:4; phase_nullnah:2` | `phase_nachhallnah_ohne_kern:1` |
| PAXG | `dio_12fw` | `frueh` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:3` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_12fw` | `mitte` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:3` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_12fw` | `spaet` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:3` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_14wj` | `frueh` | `phase_kernnah` | `phase_kernnah` | `lokale_qualitaet_reproduziert` | `phase_kernnah:6` | `phase_kernnah:1` |
| PAXG | `dio_14wj` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_kernnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_155c` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nullnah:2; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_155c` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| PAXG | `dio_155c` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_17ct` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| PAXG | `dio_17ct` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_19pg` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1ewh` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1lsu` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nullnah:2; phase_kernnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1lsu` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1q85` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| BTC | `dio_00ja` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:3; phase_offen_gemischt:2; phase_kernnah:1` | `` |
| BTC | `dio_00ly` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:4; phase_offen_gemischt:2` | `` |
| BTC | `dio_00ly` | `mitte` | `phase_nachhallnah_ohne_kern` | `fehlt` | `fehlt_im_folgefenster` | `phase_nachhallnah_ohne_kern:3; phase_offen_gemischt:2; phase_nullnah:1` | `` |
| BTC | `dio_00ly` | `spaet` | `phase_offen_gemischt` | `fehlt` | `fehlt_im_folgefenster` | `phase_offen_gemischt:5; phase_nachhallnah_ohne_kern:1` | `` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.
