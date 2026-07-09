# 1875B - PAXG-Hartkern: Reproduktion 2024 5m Folgefenster

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1874B_PAXG_HARTKERN_2024_5M_SHIFT.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `fehlt_im_folgefenster:564; lokale_qualitaet_reproduziert:28; lokale_qualitaet_wird_offen:19; qualitaet_reproduziert:16; lokale_qualitaet_wird_kernnah:13; lokale_qualitaet_wird_nachhallnah:7; lokale_qualitaet_wird_nullnah:4`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `fehlt_im_folgefenster:394; lokale_qualitaet_reproduziert:28; lokale_qualitaet_wird_offen:12; lokale_qualitaet_wird_kernnah:7; lokale_qualitaet_wird_nachhallnah:5`
- Asset-Profil: `SOL::fehlt_im_folgefenster:135; XRP::fehlt_im_folgefenster:135; BTC::fehlt_im_folgefenster:126; DOGE::fehlt_im_folgefenster:120; PAXG::fehlt_im_folgefenster:48; PAXG::lokale_qualitaet_reproduziert:28; PAXG::lokale_qualitaet_wird_offen:19; PAXG::qualitaet_reproduziert:16; PAXG::lokale_qualitaet_wird_kernnah:13; PAXG::lokale_qualitaet_wird_nachhallnah:7; PAXG::lokale_qualitaet_wird_nullnah:4`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `fehlt_im_folgefenster` | 564 | 0.866 |
| `lokale_qualitaet_reproduziert` | 28 | 0.043 |
| `lokale_qualitaet_wird_offen` | 19 | 0.029 |
| `qualitaet_reproduziert` | 16 | 0.025 |
| `lokale_qualitaet_wird_kernnah` | 13 | 0.020 |
| `lokale_qualitaet_wird_nachhallnah` | 7 | 0.011 |
| `lokale_qualitaet_wird_nullnah` | 4 | 0.006 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| PAXG | `dio_06er` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_kernnah:1; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_06er` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_0dd2` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| PAXG | `dio_0dd2` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:2` | `phase_offen_gemischt:1` |
| PAXG | `dio_0fe7` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_ohne_nullfamilie:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_0g2r` | `frueh` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:6` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_0g2r` | `mitte` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:6` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_0g2r` | `spaet` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:6` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_0pz6` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| PAXG | `dio_0pz6` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| PAXG | `dio_0z9t` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nachhallnah_ohne_kern:1; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_104t` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:1; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_14wj` | `frueh` | `phase_kernnah` | `phase_kernnah` | `lokale_qualitaet_reproduziert` | `phase_kernnah:6` | `phase_kernnah:1` |
| PAXG | `dio_14wj` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_kernnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_155c` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nullnah:2; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1ewh` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1gp2` | `frueh` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:5` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_1gp2` | `mitte` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:5` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_1gp2` | `spaet` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:5` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_1jc2` | `frueh` | `phase_kernnah` | `phase_kernnah` | `lokale_qualitaet_reproduziert` | `phase_kernnah:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_kernnah:1` |
| PAXG | `dio_1jc2` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_kernnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1kpz` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:2` | `phase_offen_gemischt:1` |
| PAXG | `dio_1lsu` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nullnah:2; phase_kernnah:1` | `phase_offen_gemischt:1` |
| PAXG | `dio_1u5i` | `mitte` | `phase_kernnah` | `phase_kernnah` | `lokale_qualitaet_reproduziert` | `phase_kernnah:4; phase_offen_gemischt:2` | `phase_kernnah:1` |
| PAXG | `dio_1u5i` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_kernnah:2` | `phase_offen_gemischt:1` |
| PAXG | `dio_1xrt` | `frueh` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:4` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_1xrt` | `mitte` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:4` | `phase_ohne_nullfamilie:1` |
| PAXG | `dio_1xrt` | `spaet` | `phase_ohne_nullfamilie` | `phase_ohne_nullfamilie` | `lokale_qualitaet_reproduziert` | `phase_ohne_nullfamilie:4` | `phase_ohne_nullfamilie:1` |
| BTC | `dio_00ja` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:3; phase_offen_gemischt:2; phase_kernnah:1` | `` |
| BTC | `dio_00ly` | `frueh` | `phase_nullnah` | `fehlt` | `fehlt_im_folgefenster` | `phase_nullnah:4; phase_offen_gemischt:2` | `` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.
