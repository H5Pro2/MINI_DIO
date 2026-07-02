# MCM-Feldphasen-Memory

Stand: 2026-07-01

## Zweck

Diese Datei verdichtet vorhandene Feldphasen-Uebergaenge in eine passive Feldphasen-Memory.

Sie ist:

- keine Handlungsschicht,
- kein Gate,
- keine Strategie,
- kein Richtungssignal.

Sie speichert nur, welche Feldrollenfolgen wiederkehren.

## Eingaben

- `docs\befunde\1219_FELDPHASEN_MATRIX_MEHRWELTEN_TRANSITIONS.csv`
- `docs\befunde\1221_FELDPHASEN_MATRIX_SYNTH_EXTREMWELTEN_TRANSITIONS.csv`
- `docs\befunde\1223_STRESS_QUIET_FELDPHASEN_VERGLEICH_2024_5M_TRANSITIONS.csv`
- `docs\befunde\1225_AKTUELLE_REZEPTORSCHICHT_STRESS_QUIET_FELDPHASEN_TRANSITIONS.csv`
- `docs\befunde\1227_AKTUELLE_REZEPTORSCHICHT_STRESS_QUIET_FELDPHASEN_1H_TRANSITIONS.csv`
- `docs\befunde\1229_SYNTHETISCHE_SINNESACHSEN_STRESS_FELDPHASEN_TRANSITIONS.csv`
- `docs\befunde\854_MCM_VERDICHTUNGSZONEN_TRANSITIONS.csv`
- `docs\befunde\855_MCM_VERDICHTUNGSZONEN_FRISCHE_WELTGRUPPE_TRANSITIONS.csv`
- `docs\befunde\865_MCM_VERDICHTUNGSZONEN_WEITERE_WELTGRUPPE_TRANSITIONS.csv`
- `docs\befunde\917_MCM_VERDICHTUNGSZONEN_VIERTE_WELTGRUPPE_TRANSITIONS.csv`
- `docs\befunde\928_MCM_VERDICHTUNGSZONEN_FUENFTE_WELTGRUPPE_TRANSITIONS.csv`
- `docs\befunde\939_MCM_VERDICHTUNGSZONEN_SECHSTE_WELTGRUPPE_TRANSITIONS.csv`
- `docs\befunde\949_MCM_VERDICHTUNGSZONEN_SIEBTE_WELTGRUPPE_TRANSITIONS.csv`
- `docs\befunde\962_MCM_VERDICHTUNGSZONEN_ACHTE_WELTGRUPPE_TRANSITIONS.csv`
- `docs\befunde\973_MCM_VERDICHTUNGSZONEN_NEUNTE_WELTGRUPPE_TRANSITIONS.csv`
- `docs\befunde\977_MCM_VERDICHTUNGSZONEN_ZEHNTE_STRESSWELT_TRANSITIONS.csv`

## Profil

- Phasenfamilien: `36`
- Qualitaeten: `{'cross_world_open_phase': 29, 'cross_world_phase_family': 6, 'young_phase_trace': 1}`
- Wirkungen: `{'phase_offen': 25, 'rekopplung_findet_zentrum': 3, 'zentrum_oeffnet_rekopplung': 3, 'rand_entlastet_in_offenheit': 2, 'offenheit_geraet_in_kippnaehe': 2, 'zentrumsbruch_in_offenheit': 1}`

## Staerkste Phasenfamilien

| Phase | Anzahl | Welten | Wirkung | Qualitaet | Rekopplung danach | Strain danach | Notiz |
|---|---:|---:|---|---|---:|---:|---|
| zentrum_stabil->offene_variante->zentrum_stabil | 8997 | 36 | phase_offen | cross_world_open_phase | 0.0467 | -0.0367 | Feldphase bleibt offen lesbar |
| offene_variante->zentrum_stabil->offene_variante | 7764 | 37 | phase_offen | cross_world_open_phase | -0.0460 | 0.0357 | Feldphase bleibt offen lesbar |
| rekopplungsnaehe->zentrum_stabil->offene_variante | 5140 | 36 | phase_offen | cross_world_open_phase | -0.0487 | 0.0389 | Feldphase bleibt offen lesbar |
| zentrum_stabil->rekopplungsnaehe->zentrum_stabil | 5112 | 36 | rekopplung_findet_zentrum | cross_world_phase_family | 0.0198 | -0.0117 | Rekopplungsnaehe findet Zentrum |
| offene_variante->zentrum_stabil->rekopplungsnaehe | 4248 | 36 | zentrum_oeffnet_rekopplung | cross_world_open_phase | -0.0159 | 0.0075 | Feldphase bleibt offen lesbar |
| zentrum_stabil->offene_variante->rekopplungsnaehe | 3807 | 36 | phase_offen | cross_world_open_phase | 0.0320 | -0.0274 | Feldphase bleibt offen lesbar |
| offene_variante->rekopplungsnaehe->zentrum_stabil | 3378 | 36 | rekopplung_findet_zentrum | cross_world_phase_family | 0.0191 | -0.0156 | Rekopplungsnaehe findet Zentrum |
| rekopplungsnaehe->zentrum_stabil->rekopplungsnaehe | 2985 | 36 | zentrum_oeffnet_rekopplung | cross_world_open_phase | -0.0188 | 0.0099 | Feldphase bleibt offen lesbar |
| offene_variante->rekopplungsnaehe->offene_variante | 2950 | 38 | phase_offen | cross_world_open_phase | -0.0316 | 0.0298 | Feldphase bleibt offen lesbar |
| rekopplungsnaehe->offene_variante->zentrum_stabil | 2880 | 35 | phase_offen | cross_world_open_phase | 0.0435 | -0.0317 | Feldphase bleibt offen lesbar |
| zentrum_stabil->rekopplungsnaehe->offene_variante | 2036 | 34 | phase_offen | cross_world_open_phase | -0.0298 | 0.0287 | Feldphase bleibt offen lesbar |
| rekopplungsnaehe->offene_variante->rekopplungsnaehe | 1964 | 37 | phase_offen | cross_world_open_phase | 0.0307 | -0.0265 | Feldphase bleibt offen lesbar |
| offene_variante->spannungsrand_kippnaehe->offene_variante | 1341 | 29 | rand_entlastet_in_offenheit | cross_world_phase_family | 0.0609 | -0.0942 | Randspannung bleibt nicht stehen, sondern entlastet in Offenheit |
| spannungsrand_kippnaehe->offene_variante->spannungsrand_kippnaehe | 874 | 28 | phase_offen | cross_world_open_phase | -0.0532 | 0.0910 | Feldphase bleibt offen lesbar |
| spannungsrand_kippnaehe->offene_variante->zentrum_stabil | 798 | 36 | phase_offen | cross_world_open_phase | 0.0576 | -0.0441 | Feldphase bleibt offen lesbar |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | 772 | 35 | zentrumsbruch_in_offenheit | cross_world_phase_family | 0.0738 | -0.0961 | zentrumsnahe Ordnung bricht kurz und entlastet in offenen Neuordnungsraum |
| spannungsrand_kippnaehe->offene_variante->rekopplungsnaehe | 652 | 38 | phase_offen | cross_world_open_phase | 0.0428 | -0.0381 | Feldphase bleibt offen lesbar |
| offene_variante->zentrum_stabil->spannungsrand_kippnaehe | 648 | 34 | phase_offen | cross_world_open_phase | -0.1356 | 0.1427 | Feldphase bleibt offen lesbar |
| rekopplungsnaehe->zentrum_stabil->spannungsrand_kippnaehe | 475 | 35 | phase_offen | cross_world_open_phase | -0.1400 | 0.1467 | Feldphase bleibt offen lesbar |
| zentrum_stabil->spannungsrand_kippnaehe->zentrum_stabil | 380 | 22 | phase_offen | cross_world_open_phase | 0.1140 | -0.1351 | Feldphase bleibt offen lesbar |
| zentrum_stabil->offene_variante->spannungsrand_kippnaehe | 304 | 27 | phase_offen | cross_world_open_phase | -0.0832 | 0.1012 | Feldphase bleibt offen lesbar |
| rekopplungsnaehe->offene_variante->spannungsrand_kippnaehe | 220 | 27 | phase_offen | cross_world_open_phase | -0.0775 | 0.1073 | Feldphase bleibt offen lesbar |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | 212 | 29 | rand_entlastet_in_offenheit | cross_world_phase_family | 0.0734 | -0.0962 | Randspannung bleibt nicht stehen, sondern entlastet in Offenheit |
| spannungsrand_kippnaehe->zentrum_stabil->offene_variante | 206 | 27 | phase_offen | cross_world_open_phase | -0.0590 | 0.0638 | Feldphase bleibt offen lesbar |

## Befund

MINI_DIO kann Feldphasen nicht nur als Einzelrollen lesen, sondern als wiederkehrende Bewegungsfolgen verdichten.

Besonders wichtig ist die Trennung:

```text
Feldrolle = momentane Innenfeldlage
Feldphase = Bewegung dieser Lage ueber Vorher/Jetzt/Nachher
```

Damit entsteht mehr Tiefe, ohne Handlung zu erzeugen.

## Grenze

Diese Memory darf nicht direkt in Handlung, Richtung oder Bewertung uebersetzt werden.
Sie beschreibt passive Phasenerfahrung.

## Wie es weitergeht

Als naechstes sollte diese Feldphasen-Memory gegen weitere Welten laufen. Entscheidend ist, ob neue Welten vorhandene Phasenfamilien erweitern, neue junge Phasen erzeugen oder bestehende Phasen driften lassen.
