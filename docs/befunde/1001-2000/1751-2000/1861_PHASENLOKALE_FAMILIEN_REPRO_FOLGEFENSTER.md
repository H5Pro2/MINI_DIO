# 1861 - Phasenlokale Familien-Reproduktion in Folgefenstern

## Grundfrage

Tauchen phasenlokal eigenständige Familien in neuen Weltfenstern wieder mit derselben lokalen Phasenqualität auf?

## Methode

- Baseline: `docs\befunde\1858_PHASENLOKALE_FAMILIENSTABILITAET.csv`.
- Folgefenster: `docs\befunde\1860_PHASENLOKALE_FAMILIEN_FOLGEFENSTER.csv`.
- Verglichen wird Asset/Familie/Phase.
- Entscheidend ist nicht nur der Familienname, sondern die wiederkehrende lokale Phasenqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Verglichene Familien-Phasen-Paare: `651`
- Repro-Zustände: `lokale_qualitaet_reproduziert:254; lokale_qualitaet_wird_offen:110; lokale_qualitaet_wird_nullnah:78; qualitaet_reproduziert:69; lokale_qualitaet_wird_nachhallnah:51; fehlt_im_folgefenster:48; lokale_qualitaet_wird_kernnah:23; lokale_qualitaet_driftet:18`
- Baseline-Zustände: `phasenlokal_eigenstaendig:446; geteilt_offen:101; einzelbeleg:57; fenstergetragen_stabil:47`
- Eigenständige Baseline-Familien: `lokale_qualitaet_reproduziert:254; lokale_qualitaet_wird_offen:81; lokale_qualitaet_wird_nullnah:42; lokale_qualitaet_wird_nachhallnah:40; lokale_qualitaet_wird_kernnah:13; lokale_qualitaet_driftet:11; fehlt_im_folgefenster:5`
- Asset-Profil: `BTC::lokale_qualitaet_reproduziert:56; SOL::lokale_qualitaet_reproduziert:52; DOGE::lokale_qualitaet_reproduziert:51; PAXG::lokale_qualitaet_reproduziert:48; XRP::lokale_qualitaet_reproduziert:47; XRP::lokale_qualitaet_wird_offen:31; SOL::qualitaet_reproduziert:27; PAXG::lokale_qualitaet_wird_nullnah:24; DOGE::lokale_qualitaet_wird_offen:21; PAXG::qualitaet_reproduziert:21; SOL::lokale_qualitaet_wird_offen:20; BTC::lokale_qualitaet_wird_offen:19; PAXG::lokale_qualitaet_wird_offen:19; XRP::lokale_qualitaet_wird_nullnah:17; BTC::lokale_qualitaet_wird_nullnah:14; DOGE::lokale_qualitaet_wird_nullnah:12; BTC::lokale_qualitaet_wird_nachhallnah:12; SOL::lokale_qualitaet_wird_nachhallnah:12; BTC::fehlt_im_folgefenster:12; XRP::fehlt_im_folgefenster:12; DOGE::lokale_qualitaet_wird_nachhallnah:11; XRP::lokale_qualitaet_wird_nachhallnah:11; SOL::lokale_qualitaet_wird_nullnah:11; DOGE::qualitaet_reproduziert:10; PAXG::lokale_qualitaet_wird_kernnah:9; XRP::lokale_qualitaet_driftet:9; DOGE::fehlt_im_folgefenster:9; PAXG::fehlt_im_folgefenster:9; SOL::lokale_qualitaet_wird_kernnah:7; DOGE::lokale_qualitaet_driftet:6; BTC::qualitaet_reproduziert:6; SOL::fehlt_im_folgefenster:6; PAXG::lokale_qualitaet_wird_nachhallnah:5; XRP::qualitaet_reproduziert:5; BTC::lokale_qualitaet_wird_kernnah:4; XRP::lokale_qualitaet_wird_kernnah:3; BTC::lokale_qualitaet_driftet:3`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `lokale_qualitaet_reproduziert` | 254 | 0.390 |
| `lokale_qualitaet_wird_offen` | 110 | 0.169 |
| `lokale_qualitaet_wird_nullnah` | 78 | 0.120 |
| `qualitaet_reproduziert` | 69 | 0.106 |
| `lokale_qualitaet_wird_nachhallnah` | 51 | 0.078 |
| `fehlt_im_folgefenster` | 48 | 0.074 |
| `lokale_qualitaet_wird_kernnah` | 23 | 0.035 |
| `lokale_qualitaet_driftet` | 18 | 0.028 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand | Baseline-Profil | Folge-Profil |
|---|---|---|---|---|---|---|---|
| BTC | `dio_00ja` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_kernnah:1` | `phase_nullnah:1; phase_offen_gemischt:1` |
| BTC | `dio_00ly` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1; phase_offen_gemischt:1` |
| BTC | `dio_00ly` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:5; phase_nachhallnah_ohne_kern:1` | `phase_offen_gemischt:2` |
| BTC | `dio_04uf` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_kernnah:1` | `phase_nullnah:1; phase_kernnah:1` |
| BTC | `dio_04uf` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:1; phase_nachhallnah_ohne_kern:1` |
| BTC | `dio_06er` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:2` |
| BTC | `dio_06s7` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_06s7` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:2` |
| BTC | `dio_09bn` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_09bn` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_09bn` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:2` |
| BTC | `dio_0dd2` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:2` | `phase_offen_gemischt:1; phase_nullnah:1` |
| BTC | `dio_0h9h` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_0l7p` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_0l7p` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_offen_gemischt:2` | `phase_nullnah:2` |
| BTC | `dio_0l7p` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:2` |
| BTC | `dio_0nlj` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:2` |
| BTC | `dio_0nlj` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:4; phase_nachhallnah_ohne_kern:2` | `phase_nullnah:2` |
| BTC | `dio_0obq` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_nullnah:2` | `phase_offen_gemischt:2` |
| BTC | `dio_0obq` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:6` | `phase_offen_gemischt:2` |
| BTC | `dio_0oc3` | `frueh` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:4; phase_kernnah:1; phase_nullnah:1` | `phase_offen_gemischt:1; phase_nullnah:1` |
| BTC | `dio_0oc3` | `mitte` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:3; phase_nullnah:2; phase_kernnah:1` | `phase_offen_gemischt:2` |
| BTC | `dio_0oc3` | `spaet` | `phase_offen_gemischt` | `phase_offen_gemischt` | `lokale_qualitaet_reproduziert` | `phase_offen_gemischt:6` | `phase_offen_gemischt:2` |
| BTC | `dio_0pz6` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_0pz6` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:1; phase_offen_gemischt:1` |
| BTC | `dio_0pz6` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_nachhallnah_ohne_kern:2; phase_offen_gemischt:1` | `phase_nullnah:1; phase_offen_gemischt:1` |
| BTC | `dio_0tay` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:6` | `phase_nullnah:2` |
| BTC | `dio_0tay` | `mitte` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:3; phase_offen_gemischt:2; phase_nachhallnah_ohne_kern:1` | `phase_nullnah:2` |
| BTC | `dio_0tay` | `spaet` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:5; phase_offen_gemischt:1` | `phase_nullnah:2` |
| BTC | `dio_0z9t` | `frueh` | `phase_nullnah` | `phase_nullnah` | `lokale_qualitaet_reproduziert` | `phase_nullnah:2; phase_ohne_nullfamilie:1` | `phase_nullnah:1` |

## Einordnung

Der Bericht trennt Namenswiederkehr von Qualitätswiederkehr.
Eine Familie ist erst dann stärker lesbar, wenn sie nicht nur erneut auftaucht, sondern in derselben Phase eine ähnliche lokale Anschlussqualität trägt.

Wenn viele phasenlokal eigenständige Familien ihre Qualität verlieren, spricht das für echte Kontextdrift.
Wenn ein Teil stabil bleibt, spricht das für lokale Feldrollen, die über neue Weltfenster getragen werden können.

## Wie es weitergeht

Als nächstes sollte aus den stabil reproduzierten lokalen Familien eine kleine passive Reifegruppe gebildet werden.
Diese Gruppe darf keine Handlung steuern; sie dient nur als sauberer Kern für weitere Feldrollen-Reifung.
