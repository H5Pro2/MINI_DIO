# 1871X - XRP-Hartkern: Reproduktion 2024-Realwelt

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1870X_XRP_HARTKERN_2024_REALWELT.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `fehlt_im_folgefenster:546; lokale_qualitaet_reproduziert:51; lokale_qualitaet_wird_offen:13; lokale_qualitaet_wird_nachhallnah:13; lokale_qualitaet_wird_nullnah:13; qualitaet_reproduziert:7; lokale_qualitaet_driftet:6; lokale_qualitaet_wird_kernnah:2`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `fehlt_im_folgefenster:357; lokale_qualitaet_reproduziert:51; lokale_qualitaet_wird_offen:11; lokale_qualitaet_wird_nullnah:11; lokale_qualitaet_wird_nachhallnah:10; lokale_qualitaet_driftet:5; lokale_qualitaet_wird_kernnah:1`
- Asset-Profil: `PAXG::fehlt_im_folgefenster:135; SOL::fehlt_im_folgefenster:135; BTC::fehlt_im_folgefenster:126; DOGE::fehlt_im_folgefenster:120; XRP::lokale_qualitaet_reproduziert:51; XRP::fehlt_im_folgefenster:30; XRP::lokale_qualitaet_wird_offen:13; XRP::lokale_qualitaet_wird_nachhallnah:13; XRP::lokale_qualitaet_wird_nullnah:13; XRP::qualitaet_reproduziert:7; XRP::lokale_qualitaet_driftet:6; XRP::lokale_qualitaet_wird_kernnah:2`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `fehlt_im_folgefenster` | 546 | 0.839 |
| `lokale_qualitaet_reproduziert` | 51 | 0.078 |
| `lokale_qualitaet_wird_offen` | 13 | 0.020 |
| `lokale_qualitaet_wird_nachhallnah` | 13 | 0.020 |
| `lokale_qualitaet_wird_nullnah` | 13 | 0.020 |
| `qualitaet_reproduziert` | 7 | 0.011 |
| `lokale_qualitaet_driftet` | 6 | 0.009 |
| `lokale_qualitaet_wird_kernnah` | 2 | 0.003 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| XRP | `dio_00ja` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| XRP | `dio_00ja` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nullnah:1` | `phase_offen_gemischt:1` |
| XRP | `dio_00ly` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:1; phase_kernnah:1` | `phase_nullnah:1` |
| XRP | `dio_04uf` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4` | `phase_nullnah:1` |
| XRP | `dio_04uf` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4` | `phase_nullnah:1` |
| XRP | `dio_05yg` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3` | `phase_nullnah:1` |
| XRP | `dio_06er` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| XRP | `dio_06s7` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_kernnah:2; phase_offen_gemischt:1` | `phase_nullnah:1` |
| XRP | `dio_09bn` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| XRP | `dio_09bn` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| XRP | `dio_09bn` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| XRP | `dio_0g2r` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:1; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| XRP | `dio_0g2r` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| XRP | `dio_0l7p` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| XRP | `dio_0l7p` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1` |
| XRP | `dio_0m9z` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nullnah:2; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| XRP | `dio_0m9z` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:6` | `phase_offen_gemischt:1` |
| XRP | `dio_0nlj` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| XRP | `dio_0nlj` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| XRP | `dio_0nlj` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| XRP | `dio_0obq` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:2` | `phase_offen_gemischt:1` |
| XRP | `dio_0oc3` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:6` | `phase_offen_gemischt:1` |
| XRP | `dio_0pz6` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| XRP | `dio_0pz6` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| XRP | `dio_0tay` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| XRP | `dio_0z9t` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_ohne_nullfamilie:1` | `phase_nullnah:1` |
| XRP | `dio_104t` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| XRP | `dio_1492` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| XRP | `dio_1492` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| XRP | `dio_1492` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.
