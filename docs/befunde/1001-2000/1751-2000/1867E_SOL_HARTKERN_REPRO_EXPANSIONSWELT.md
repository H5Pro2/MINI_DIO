# 1867E - SOL-Hartkern: Reproduktion Expansionswelt

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1866E_SOL_HARTKERN_EXPANSIONSWELT.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `fehlt_im_folgefenster:546; lokale_qualitaet_reproduziert:38; lokale_qualitaet_wird_nachhallnah:17; lokale_qualitaet_wird_offen:14; lokale_qualitaet_wird_nullnah:12; qualitaet_reproduziert:12; lokale_qualitaet_wird_kernnah:9; lokale_qualitaet_driftet:3`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `fehlt_im_folgefenster:377; lokale_qualitaet_reproduziert:38; lokale_qualitaet_wird_nachhallnah:12; lokale_qualitaet_wird_offen:11; lokale_qualitaet_wird_nullnah:4; lokale_qualitaet_wird_kernnah:3; lokale_qualitaet_driftet:1`
- Asset-Profil: `PAXG::fehlt_im_folgefenster:135; XRP::fehlt_im_folgefenster:135; BTC::fehlt_im_folgefenster:126; DOGE::fehlt_im_folgefenster:120; SOL::lokale_qualitaet_reproduziert:38; SOL::fehlt_im_folgefenster:30; SOL::lokale_qualitaet_wird_nachhallnah:17; SOL::lokale_qualitaet_wird_offen:14; SOL::lokale_qualitaet_wird_nullnah:12; SOL::qualitaet_reproduziert:12; SOL::lokale_qualitaet_wird_kernnah:9; SOL::lokale_qualitaet_driftet:3`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `fehlt_im_folgefenster` | 546 | 0.839 |
| `lokale_qualitaet_reproduziert` | 38 | 0.058 |
| `lokale_qualitaet_wird_nachhallnah` | 17 | 0.026 |
| `lokale_qualitaet_wird_offen` | 14 | 0.022 |
| `lokale_qualitaet_wird_nullnah` | 12 | 0.018 |
| `qualitaet_reproduziert` | 12 | 0.018 |
| `lokale_qualitaet_wird_kernnah` | 9 | 0.014 |
| `lokale_qualitaet_driftet` | 3 | 0.005 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| SOL | `dio_00ja` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| SOL | `dio_00ly` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| SOL | `dio_04uf` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_kernnah:1` | `phase_nullnah:1` |
| SOL | `dio_05yg` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| SOL | `dio_06er` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_06er` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:1; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| SOL | `dio_06er` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_06s7` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_07uk` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:2; phase_ohne_nullfamilie:1` | `phase_offen_gemischt:1` |
| SOL | `dio_07uk` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:2; phase_ohne_nullfamilie:1` | `phase_offen_gemischt:1` |
| SOL | `dio_0dd2` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4` | `phase_nullnah:1` |
| SOL | `dio_0jkk` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_ohne_nullfamilie:1` | `phase_offen_gemischt:1` |
| SOL | `dio_0l7p` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1` |
| SOL | `dio_0m9z` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0oc3` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_kernnah:1` | `phase_offen_gemischt:1` |
| SOL | `dio_0oc3` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nachhallnah_ohne_kern:1; phase_nullnah:1` | `phase_offen_gemischt:1` |
| SOL | `dio_0pz6` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0pz6` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0pz6` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:2; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0tay` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_kernnah:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0tay` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0tay` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1` |
| SOL | `dio_104t` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1` |
| SOL | `dio_1492` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_kernnah:1` | `phase_nullnah:1` |
| SOL | `dio_1492` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_1492` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| SOL | `dio_14wj` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_17ct` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_kernnah:1` | `phase_nullnah:1` |
| SOL | `dio_17ct` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_17ct` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nullnah:2; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.
