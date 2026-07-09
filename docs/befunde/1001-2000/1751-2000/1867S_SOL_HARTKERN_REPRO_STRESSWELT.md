# 1867S - SOL-Hartkern: Reproduktion Stresswelt

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1866S_SOL_HARTKERN_STRESSWELT.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `fehlt_im_folgefenster:549; lokale_qualitaet_reproduziert:42; qualitaet_reproduziert:17; lokale_qualitaet_wird_offen:16; lokale_qualitaet_wird_nachhallnah:14; lokale_qualitaet_wird_nullnah:10; lokale_qualitaet_wird_kernnah:3`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `fehlt_im_folgefenster:377; lokale_qualitaet_reproduziert:42; lokale_qualitaet_wird_offen:10; lokale_qualitaet_wird_nachhallnah:10; lokale_qualitaet_wird_nullnah:4; lokale_qualitaet_wird_kernnah:3`
- Asset-Profil: `PAXG::fehlt_im_folgefenster:135; XRP::fehlt_im_folgefenster:135; BTC::fehlt_im_folgefenster:126; DOGE::fehlt_im_folgefenster:120; SOL::lokale_qualitaet_reproduziert:42; SOL::fehlt_im_folgefenster:33; SOL::qualitaet_reproduziert:17; SOL::lokale_qualitaet_wird_offen:16; SOL::lokale_qualitaet_wird_nachhallnah:14; SOL::lokale_qualitaet_wird_nullnah:10; SOL::lokale_qualitaet_wird_kernnah:3`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `fehlt_im_folgefenster` | 549 | 0.843 |
| `lokale_qualitaet_reproduziert` | 42 | 0.065 |
| `qualitaet_reproduziert` | 17 | 0.026 |
| `lokale_qualitaet_wird_offen` | 16 | 0.025 |
| `lokale_qualitaet_wird_nachhallnah` | 14 | 0.022 |
| `lokale_qualitaet_wird_nullnah` | 10 | 0.015 |
| `lokale_qualitaet_wird_kernnah` | 3 | 0.005 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| SOL | `dio_00ja` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| SOL | `dio_00ly` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nachhallnah_ohne_kern:2; phase_nullnah:1` | `phase_offen_gemischt:1` |
| SOL | `dio_04uf` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_kernnah:1` | `phase_nullnah:1` |
| SOL | `dio_05yg` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| SOL | `dio_06er` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_06er` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_06s7` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_06s7` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_09bn` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0dd2` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4` | `phase_nullnah:1` |
| SOL | `dio_0h9h` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0h9h` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1` |
| SOL | `dio_0jkk` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:2; phase_nullnah:1; phase_nachhallnah_ohne_kern:1; phase_ohne_nullfamilie:1` | `phase_offen_gemischt:1` |
| SOL | `dio_0jkk` | `mitte` | `phase_kernnah` | `phase_kernnah` | `lokale_qualitaet_reproduziert` | `phase_kernnah:2; phase_nullnah:1; phase_offen_gemischt:1; phase_ohne_nullfamilie:1` | `phase_kernnah:1` |
| SOL | `dio_0jkk` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_ohne_nullfamilie:1` | `phase_offen_gemischt:1` |
| SOL | `dio_0l7p` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1` |
| SOL | `dio_0m9z` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0nlj` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_kernnah:1` | `phase_nullnah:1` |
| SOL | `dio_0nlj` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:1` |
| SOL | `dio_0nlj` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1` |
| SOL | `dio_0oc3` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_kernnah:1` | `phase_offen_gemischt:1` |
| SOL | `dio_0pz6` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0tay` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_kernnah:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_0tay` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_1492` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_kernnah:1` | `phase_nullnah:1` |
| SOL | `dio_1492` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:1; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_1492` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1` |
| SOL | `dio_14wj` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1` |
| SOL | `dio_14wj` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1` |
| SOL | `dio_17ct` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_kernnah:1` | `phase_nullnah:1` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.

## Wie es weitergeht

Als nächstes sollte aus den stabil reproduzierten lokalen Familien eine kleine passive Reifegruppe gebildet werden.
Diese Gruppe darf keine Handlung steuern; sie dient nur als sauberer Kern für weitere Feldrollen-Reifung.
