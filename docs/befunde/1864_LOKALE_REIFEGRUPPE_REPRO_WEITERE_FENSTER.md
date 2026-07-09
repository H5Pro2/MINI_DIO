# 1864 - Lokale Reifegruppe: Reproduktion in weiteren Fenstern

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1863_LOKALE_REIFEGRUPPE_WEITERE_FOLGEFENSTER.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `lokale_qualitaet_reproduziert:220; lokale_qualitaet_wird_offen:122; lokale_qualitaet_wird_nullnah:84; qualitaet_reproduziert:64; lokale_qualitaet_wird_nachhallnah:61; fehlt_im_folgefenster:60; lokale_qualitaet_wird_kernnah:25; lokale_qualitaet_driftet:15`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `lokale_qualitaet_reproduziert:220; lokale_qualitaet_wird_offen:94; lokale_qualitaet_wird_nullnah:50; lokale_qualitaet_wird_nachhallnah:40; lokale_qualitaet_wird_kernnah:18; fehlt_im_folgefenster:15; lokale_qualitaet_driftet:9`
- Asset-Profil: `XRP::lokale_qualitaet_reproduziert:51; BTC::lokale_qualitaet_reproduziert:46; DOGE::lokale_qualitaet_reproduziert:45; PAXG::lokale_qualitaet_reproduziert:39; SOL::lokale_qualitaet_reproduziert:39; DOGE::lokale_qualitaet_wird_offen:27; SOL::lokale_qualitaet_wird_offen:26; XRP::lokale_qualitaet_wird_offen:24; PAXG::lokale_qualitaet_wird_offen:23; BTC::lokale_qualitaet_wird_offen:22; SOL::fehlt_im_folgefenster:21; XRP::lokale_qualitaet_wird_nullnah:20; PAXG::qualitaet_reproduziert:19; SOL::lokale_qualitaet_wird_nullnah:18; PAXG::fehlt_im_folgefenster:18; BTC::lokale_qualitaet_wird_nullnah:17; DOGE::lokale_qualitaet_wird_nullnah:16; SOL::qualitaet_reproduziert:16; DOGE::lokale_qualitaet_wird_nachhallnah:15; BTC::qualitaet_reproduziert:14; PAXG::lokale_qualitaet_wird_nullnah:13; XRP::lokale_qualitaet_wird_nachhallnah:13; BTC::lokale_qualitaet_wird_nachhallnah:12; BTC::fehlt_im_folgefenster:12; SOL::lokale_qualitaet_wird_nachhallnah:11; PAXG::lokale_qualitaet_wird_kernnah:10; PAXG::lokale_qualitaet_wird_nachhallnah:10; XRP::fehlt_im_folgefenster:9; XRP::qualitaet_reproduziert:8; DOGE::qualitaet_reproduziert:7; DOGE::lokale_qualitaet_driftet:6; XRP::lokale_qualitaet_driftet:6; XRP::lokale_qualitaet_wird_kernnah:4; DOGE::lokale_qualitaet_wird_kernnah:4; SOL::lokale_qualitaet_wird_kernnah:4; BTC::lokale_qualitaet_wird_kernnah:3; PAXG::lokale_qualitaet_driftet:3`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `lokale_qualitaet_reproduziert` | 220 | 0.338 |
| `lokale_qualitaet_wird_offen` | 122 | 0.187 |
| `lokale_qualitaet_wird_nullnah` | 84 | 0.129 |
| `qualitaet_reproduziert` | 64 | 0.098 |
| `lokale_qualitaet_wird_nachhallnah` | 61 | 0.094 |
| `fehlt_im_folgefenster` | 60 | 0.092 |
| `lokale_qualitaet_wird_kernnah` | 25 | 0.038 |
| `lokale_qualitaet_driftet` | 15 | 0.023 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| BTC | `dio_00ly` | `mitte` | `phase_nachhallnah_ohne_kern` | `phase_nachhallnah_ohne_kern` | `lokale_qualitaet_reproduziert` | `phase_nachhallnah_ohne_kern:3; phase_offen_gemischt:2; phase_nullnah:1` | `phase_nachhallnah_ohne_kern:1; phase_offen_gemischt:1` |
| BTC | `dio_00ly` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1; phase_nullnah:1` |
| BTC | `dio_05yg` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:1` | `phase_nullnah:2` |
| BTC | `dio_06er` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:2` |
| BTC | `dio_06er` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:2` |
| BTC | `dio_06er` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:2; phase_offen_gemischt:1` | `phase_nullnah:1; phase_offen_gemischt:1` |
| BTC | `dio_06s7` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_06s7` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1; phase_offen_gemischt:1` |
| BTC | `dio_07uk` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:2; phase_nullnah:1; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1; phase_kernnah:1` |
| BTC | `dio_09bn` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:2` |
| BTC | `dio_0dd2` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:2` |
| BTC | `dio_0dd2` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:2` | `phase_offen_gemischt:1; phase_nachhallnah_ohne_kern:1` |
| BTC | `dio_0g2r` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:1; phase_kernnah:1` |
| BTC | `dio_0g2r` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:6` | `phase_offen_gemischt:2` |
| BTC | `dio_0l7p` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:2` |
| BTC | `dio_0nlj` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:1; phase_offen_gemischt:1` | `phase_nullnah:1; phase_offen_gemischt:1` |
| BTC | `dio_0nlj` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:1; phase_nachhallnah_ohne_kern:1` |
| BTC | `dio_0nlj` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:1; phase_nachhallnah_ohne_kern:1` |
| BTC | `dio_0oc3` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nullnah:2; phase_kernnah:1` | `phase_offen_gemischt:2` |
| BTC | `dio_0oc3` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:6` | `phase_offen_gemischt:2` |
| BTC | `dio_0pz6` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_0pz6` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_0pz6` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:2; phase_offen_gemischt:1` | `phase_nullnah:2` |
| BTC | `dio_0tay` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_0tay` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:2` |
| BTC | `dio_0tay` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:2` |
| BTC | `dio_104t` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:2` |
| BTC | `dio_104t` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:2; phase_offen_gemischt:1` | `phase_nullnah:2` |
| BTC | `dio_1492` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |
| BTC | `dio_1492` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.

## Wie es weitergeht

Als nächstes sollte aus den stabil reproduzierten lokalen Familien eine kleine passive Reifegruppe gebildet werden.
Diese Gruppe darf keine Handlung steuern; sie dient nur als sauberer Kern für weitere Feldrollen-Reifung.
