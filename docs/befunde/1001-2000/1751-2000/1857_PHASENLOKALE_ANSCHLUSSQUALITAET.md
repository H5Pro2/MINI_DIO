# 1857 - Phasenlokale Anschlussqualität

## Grundfrage

Was passiert, wenn Anschlussqualität nicht mehr vom Gesamtfenster geerbt wird, sondern pro Phase gegen passende Nullwelt-Phasen gelesen wird?

## Methode

- Quellen: `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv; docs\befunde\1848_ANSCHLUSSQUALITAET_NEUE_FENSTER.csv; docs\befunde\1853_FAMILIEN_ANSCHLUSSKARTE_NEUE_WELTEN.csv`.
- Realwelt-Phase wird gegen `null_random` und `null_shuffle` derselben Quelle, desselben Assets, desselben Fensters und derselben Familie gelesen.
- Die Klassifikation ist ein Diagnose-Bucket, keine Feldregel und keine Handlungsschicht.
- Positive Größen werden gegen die stärkste Nullreferenz gelesen; Strain wird gegen die niedrigste Nullreferenz protokolliert.

## Kurzbefund

- Phasenzeilen: `3240`
- Phasenlokale Qualitäten: `phase_nullnah:1423; phase_offen_gemischt:1046; phase_nachhallnah_ohne_kern:353; phase_ohne_nullfamilie:258; phase_kernnah:160`
- Geerbte Fensterqualitäten: `offen_gemischt:1188; kernnah:1080; kernnah_ohne_feldzeit:432; nullnah:324; nachhallnah_ohne_kern:108; anschlussnah:108`
- Fenster-zu-Phase-Übergänge: `offen_gemischt->phase_nullnah:519; kernnah->phase_nullnah:448; offen_gemischt->phase_offen_gemischt:375; kernnah->phase_offen_gemischt:362; kernnah_ohne_feldzeit->phase_nullnah:208; nullnah->phase_nullnah:163; kernnah_ohne_feldzeit->phase_offen_gemischt:135; offen_gemischt->phase_nachhallnah_ohne_kern:130; kernnah->phase_nachhallnah_ohne_kern:113; offen_gemischt->phase_ohne_nullfamilie:111; nullnah->phase_offen_gemischt:107; kernnah->phase_ohne_nullfamilie:90; kernnah->phase_kernnah:67; kernnah_ohne_feldzeit->phase_nachhallnah_ohne_kern:59; nachhallnah_ohne_kern->phase_nullnah:57; offen_gemischt->phase_kernnah:53; anschlussnah->phase_offen_gemischt:37; nachhallnah_ohne_kern->phase_offen_gemischt:30; nullnah->phase_nachhallnah_ohne_kern:28; anschlussnah->phase_nullnah:28; nullnah->phase_ohne_nullfamilie:18; anschlussnah->phase_ohne_nullfamilie:18; kernnah_ohne_feldzeit->phase_kernnah:15; kernnah_ohne_feldzeit->phase_ohne_nullfamilie:15; anschlussnah->phase_kernnah:14; nachhallnah_ohne_kern->phase_nachhallnah_ohne_kern:12; anschlussnah->phase_nachhallnah_ohne_kern:11; nullnah->phase_kernnah:8; nachhallnah_ohne_kern->phase_ohne_nullfamilie:6; nachhallnah_ohne_kern->phase_kernnah:3`
- Qualität gleich Fenster: `617`
- Qualität anders als Fenster: `2623`

## Phasenlokale Zustände

| Zustand | Zeilen | Anteil |
|---|---:|---:|
| `phase_nullnah` | 1423 | 0.439 |
| `phase_offen_gemischt` | 1046 | 0.323 |
| `phase_nachhallnah_ohne_kern` | 353 | 0.109 |
| `phase_ohne_nullfamilie` | 258 | 0.080 |
| `phase_kernnah` | 160 | 0.049 |

## Beispielzeilen

| Quelle | Asset | Familie | Phase | Fenster | Phase lokal | Geerbt | Share-Edge | Rekopplung-Edge | Temporal-Edge |
|---|---|---|---|---:|---|---|---:|---:|---:|
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_104t` | `frueh` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0024 | -0.0026 | -0.0004 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_104t` | `mitte` | 0 | `phase_nachhallnah_ohne_kern` | `nachhallnah_ohne_kern` | -0.0252 | -0.0038 | 0.0013 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_104t` | `spaet` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0075 | -0.0020 | 0.0000 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_155c` | `frueh` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0123 | -0.0009 | 0.0058 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_155c` | `mitte` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0027 | -0.0019 | 0.0003 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_155c` | `spaet` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0006 | -0.0024 | 0.0013 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0m9z` | `frueh` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0003 | -0.0024 | 0.0001 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0m9z` | `mitte` | 0 | `phase_nullnah` | `nachhallnah_ohne_kern` | -0.0045 | -0.0030 | -0.0001 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0m9z` | `spaet` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0003 | -0.0008 | -0.0031 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0l7p` | `frueh` | 0 | `phase_nullnah` | `nachhallnah_ohne_kern` | -0.0102 | -0.0038 | -0.0055 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0l7p` | `mitte` | 0 | `phase_nullnah` | `nachhallnah_ohne_kern` | -0.0003 | -0.0044 | -0.0010 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0l7p` | `spaet` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0033 | -0.0039 | -0.0031 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0h9h` | `frueh` | 0 | `phase_nullnah` | `nachhallnah_ohne_kern` | -0.0024 | -0.0056 | -0.0015 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0h9h` | `mitte` | 0 | `phase_nullnah` | `nachhallnah_ohne_kern` | -0.0057 | -0.0030 | -0.0006 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0h9h` | `spaet` | 0 | `phase_nachhallnah_ohne_kern` | `nachhallnah_ohne_kern` | -0.0060 | -0.0022 | 0.0009 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_14wj` | `frueh` | 0 | `phase_nullnah` | `nachhallnah_ohne_kern` | -0.0033 | -0.0043 | -0.0074 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_14wj` | `mitte` | 0 | `phase_nullnah` | `nachhallnah_ohne_kern` | -0.0063 | -0.0053 | -0.0019 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_14wj` | `spaet` | 0 | `phase_nullnah` | `nachhallnah_ohne_kern` | -0.0042 | -0.0050 | -0.0062 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_00ly` | `frueh` | 0 | `phase_nullnah` | `nachhallnah_ohne_kern` | -0.0027 | -0.0044 | -0.0093 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_00ly` | `mitte` | 0 | `phase_nachhallnah_ohne_kern` | `nachhallnah_ohne_kern` | -0.0054 | -0.0008 | 0.0008 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_00ly` | `spaet` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0021 | -0.0010 | -0.0028 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0oc3` | `frueh` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0057 | -0.0044 | 0.0217 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0oc3` | `mitte` | 0 | `phase_nullnah` | `nachhallnah_ohne_kern` | -0.0006 | -0.0056 | -0.0004 |
| `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv` | BTC | `dio_0oc3` | `spaet` | 0 | `phase_offen_gemischt` | `nachhallnah_ohne_kern` | 0.0045 | -0.0012 | 0.0007 |

## Einordnung

Diese Prüfung trennt erstmals die Frage `Welche Qualität trägt das Fenster?` von `Welche Qualität trägt diese Familie in dieser Phase?`.
Damit wird sichtbar, ob eine Familie nur durch die Gesamtwelt mitgezogen wird oder ob sie lokal in Früh-, Mittel- oder Spätphase selbst Anschluss trägt.

Wenn die phasenlokale Qualität deutlich von der Fensterqualität abweicht, ist das kein Fehler, sondern ein Hinweis auf mehrdimensionale Feldlesung:
Fenster, Familie und Phase tragen nicht automatisch dieselbe Bedeutung.
