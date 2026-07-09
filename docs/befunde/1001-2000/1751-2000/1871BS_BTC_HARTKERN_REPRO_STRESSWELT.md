# 1871BS - BTC-Hartkern: Reproduktion Stresswelt

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1869BS_BTC_HARTKERN_STRESSWELT.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `fehlt_im_folgefenster:543; lokale_qualitaet_reproduziert:45; lokale_qualitaet_wird_offen:22; lokale_qualitaet_wird_nullnah:14; lokale_qualitaet_wird_nachhallnah:12; qualitaet_reproduziert:8; lokale_qualitaet_wird_kernnah:4; lokale_qualitaet_driftet:3`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `fehlt_im_folgefenster:356; lokale_qualitaet_reproduziert:45; lokale_qualitaet_wird_offen:16; lokale_qualitaet_wird_nachhallnah:12; lokale_qualitaet_wird_nullnah:11; lokale_qualitaet_wird_kernnah:3; lokale_qualitaet_driftet:3`
- Asset-Profil: `PAXG::fehlt_im_folgefenster:135; SOL::fehlt_im_folgefenster:135; XRP::fehlt_im_folgefenster:135; DOGE::fehlt_im_folgefenster:120; BTC::lokale_qualitaet_reproduziert:45; BTC::lokale_qualitaet_wird_offen:22; BTC::fehlt_im_folgefenster:18; BTC::lokale_qualitaet_wird_nullnah:14; BTC::lokale_qualitaet_wird_nachhallnah:12; BTC::qualitaet_reproduziert:8; BTC::lokale_qualitaet_wird_kernnah:4; BTC::lokale_qualitaet_driftet:3`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `fehlt_im_folgefenster` | 543 | 0.834 |
| `lokale_qualitaet_reproduziert` | 45 | 0.069 |
| `lokale_qualitaet_wird_offen` | 22 | 0.034 |
| `lokale_qualitaet_wird_nullnah` | 14 | 0.022 |
| `lokale_qualitaet_wird_nachhallnah` | 12 | 0.018 |
| `qualitaet_reproduziert` | 8 | 0.012 |
| `lokale_qualitaet_wird_kernnah` | 4 | 0.006 |
| `lokale_qualitaet_driftet` | 3 | 0.005 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| BTC | `dio_00ly` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| BTC | `dio_04uf` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_kernnah:1` | `phase_nullnah:1` |
| BTC | `dio_04uf` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| BTC | `dio_06s7` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| BTC | `dio_09bn` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_09bn` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_0dd2` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| BTC | `dio_0dd2` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| BTC | `dio_0dd2` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:2` | `phase_offen_gemischt:1` |
| BTC | `dio_0g2r` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:6` | `phase_offen_gemischt:1` |
| BTC | `dio_0g2r` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| BTC | `dio_0h9h` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_0h9h` | `spaet` | `phase_nachhallnah_ohne_kern` | `phase_nachhallnah_ohne_kern` | `lokale_qualitaet_reproduziert` | `phase_nachhallnah_ohne_kern:4; phase_nullnah:1; phase_offen_gemischt:1` | `phase_nachhallnah_ohne_kern:1` |
| BTC | `dio_0l7p` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| BTC | `dio_0nlj` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| BTC | `dio_0nlj` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1` |
| BTC | `dio_0obq` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:6` | `phase_offen_gemischt:1` |
| BTC | `dio_0oc3` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_kernnah:1; phase_nullnah:1` | `phase_offen_gemischt:1` |
| BTC | `dio_0pz6` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_0pz6` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_0pz6` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:2; phase_offen_gemischt:1` | `phase_nullnah:1` |
| BTC | `dio_0tay` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_0tay` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| BTC | `dio_0tay` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| BTC | `dio_104t` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| BTC | `dio_104t` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:2; phase_offen_gemischt:1` | `phase_nullnah:1` |
| BTC | `dio_1492` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_1492` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_1492` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_14wj` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.
