# 1856 - Phasengenaue Familien-Anschlussbaseline

## Grundfrage

Sinkt die offene Drift, wenn die Baseline nicht nur nach Asset/Familie, sondern nach Asset/Familie/Phase gelesen wird?

## Methode

- Baseline-Quellen: `docs\befunde\1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv; docs\befunde\1848_ANSCHLUSSQUALITAET_NEUE_FENSTER.csv`, aufgeteilt in `frueh`, `mitte`, `spaet`.
- Folge: `1853`, ebenfalls phasengenau gelesen.
- Vergleich pro Asset/Familie/Phase.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Phasen-Paare: `618`
- Baseline-Phasenschlüssel: `621`
- Folge-Phasenschlüssel: `618`
- Phasen-Zustände: `phase_offen_wird_spezifisch:333; phase_spezifisch_wird_offen:114; phase_nachhall_wird_kernnah:105; neu_ohne_phasenbaseline:30; phase_reproduziert:27; phase_kontextdrift:9`
- Phasen-Übergänge: `offen_gemischt->kernnah:228; kernnah->offen_gemischt:114; nachhallnah_ohne_kern->kernnah:105; offen_gemischt->nullnah:90; offen_gemischt->kernnah_ohne_feldzeit:15; neu_ohne_phasenbaseline->kernnah:12; kernnah->kernnah:12; neu_ohne_phasenbaseline->nullnah:12; offen_gemischt->offen_gemischt:9; neu_ohne_phasenbaseline->offen_gemischt:6; kernnah_ohne_feldzeit->nullnah:6; kernnah_ohne_feldzeit->kernnah_ohne_feldzeit:6; nullnah->kernnah:3`

## Zustände

| Zustand | Paare | Anteil |
|---|---:|---:|
| `phase_offen_wird_spezifisch` | 333 | 0.539 |
| `phase_spezifisch_wird_offen` | 114 | 0.184 |
| `phase_nachhall_wird_kernnah` | 105 | 0.170 |
| `neu_ohne_phasenbaseline` | 30 | 0.049 |
| `phase_reproduziert` | 27 | 0.044 |
| `phase_kontextdrift` | 9 | 0.015 |

## Beispielzeilen

| Asset | Familie | Phase | Baseline | Folge | Zustand |
|---|---|---|---|---|---|
| BTC | `dio_104t` | `frueh` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_104t` | `mitte` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_104t` | `spaet` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_155c` | `frueh` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_155c` | `mitte` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_155c` | `spaet` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_0l7p` | `frueh` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_0l7p` | `mitte` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_0l7p` | `spaet` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_0m9z` | `frueh` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_0m9z` | `mitte` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_0m9z` | `spaet` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_0h9h` | `frueh` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_0h9h` | `mitte` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_0h9h` | `spaet` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_14wj` | `frueh` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_14wj` | `mitte` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_14wj` | `spaet` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_1lsu` | `frueh` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_1lsu` | `mitte` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_1lsu` | `spaet` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_00ly` | `frueh` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_00ly` | `mitte` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |
| BTC | `dio_00ly` | `spaet` | `nachhallnah_ohne_kern` | `kernnah` | `phase_nachhall_wird_kernnah` |

## Einordnung

Die phasengenaue Lesung verringert die offene Drift nicht automatisch.
Das spricht dafür, dass die bisherige Anschlussqualität noch zu stark auf Fensterqualität basiert.
Phase allein reicht nicht, wenn die Qualität selbst noch nicht phasenlokal berechnet wird.

Der wichtige Befund ist methodisch:
Eine engere Baseline muss nicht nur Phasen trennen, sondern die Anschlussqualität innerhalb der Phase neu lesen.

## Wie es weitergeht

Als nächstes sollte Anschlussqualität nicht mehr nur vom Gesamtfenster geerbt werden.
Sie muss phasenlokal berechnet werden: Frueh/Mitte/Spaet jeweils gegen passende Nullwelt-Phasen.
