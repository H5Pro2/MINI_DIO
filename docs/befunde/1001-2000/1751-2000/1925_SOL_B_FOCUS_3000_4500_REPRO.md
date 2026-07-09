# 1925 - SOL B Fokus 3000 4500 Repro

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1923_SOL_B_FOCUS_3000_4500.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `fehlt_im_folgefenster:637; lokale_qualitaet_reproduziert:8; lokale_qualitaet_wird_offen:2; lokale_qualitaet_driftet:2; lokale_qualitaet_wird_kernnah:2`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `fehlt_im_folgefenster:435; lokale_qualitaet_reproduziert:8; lokale_qualitaet_wird_offen:2; lokale_qualitaet_driftet:1`
- Asset-Profil: `PAXG::fehlt_im_folgefenster:135; XRP::fehlt_im_folgefenster:135; BTC::fehlt_im_folgefenster:126; SOL::fehlt_im_folgefenster:121; DOGE::fehlt_im_folgefenster:120; SOL::lokale_qualitaet_reproduziert:8; SOL::lokale_qualitaet_wird_offen:2; SOL::lokale_qualitaet_driftet:2; SOL::lokale_qualitaet_wird_kernnah:2`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `fehlt_im_folgefenster` | 637 | 0.978 |
| `lokale_qualitaet_reproduziert` | 8 | 0.012 |
| `lokale_qualitaet_wird_offen` | 2 | 0.003 |
| `lokale_qualitaet_driftet` | 2 | 0.003 |
| `lokale_qualitaet_wird_kernnah` | 2 | 0.003 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| SOL | `dio_0kx9` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3` | `phase_nullnah:1` |
| SOL | `dio_0kx9` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3` | `phase_nullnah:1` |
| SOL | `dio_0nlj` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_kernnah:1` | `phase_nullnah:1` |
| SOL | `dio_0tay` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_kernnah:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_14wj` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_14wj` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1` |
| SOL | `dio_1kpz` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_1u5i` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3` | `phase_nullnah:1` |
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
| BTC | `dio_06jk` | `frueh` | `phase_offen_gemischt` | `fehlt` | `fehlt_im_folgefenster` | `phase_offen_gemischt:2; phase_ohne_nullfamilie:1` | `` |
| BTC | `dio_06jk` | `spaet` | `phase_offen_gemischt` | `fehlt` | `fehlt_im_folgefenster` | `phase_offen_gemischt:2; phase_ohne_nullfamilie:1` | `` |
| BTC | `dio_06s7` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:6` | `` |
| BTC | `dio_06s7` | `mitte` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:5; phase_nachhallnah_ohne_kern:1` | `` |
| BTC | `dio_06s7` | `spaet` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `` |
| BTC | `dio_07uk` | `mitte` | `phase_offen_gemischt` | `fehlt` | `fehlt_im_folgefenster` | `phase_offen_gemischt:2; phase_kernnah:1; phase_nachhallnah_ohne_kern:1` | `` |
| BTC | `dio_07uk` | `spaet` | `phase_offen_gemischt` | `fehlt` | `fehlt_im_folgefenster` | `phase_offen_gemischt:2; phase_nullnah:1; phase_nachhallnah_ohne_kern:1` | `` |
| BTC | `dio_09bn` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:6` | `` |
| BTC | `dio_09bn` | `mitte` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:6` | `` |
| BTC | `dio_09bn` | `spaet` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:5; phase_nachhallnah_ohne_kern:1` | `` |
| BTC | `dio_0dd2` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:4; phase_offen_gemischt:2` | `` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.
