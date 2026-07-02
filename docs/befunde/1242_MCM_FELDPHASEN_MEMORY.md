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

- `docs\befunde\1225_AKTUELLE_REZEPTORSCHICHT_STRESS_QUIET_FELDPHASEN_TRANSITIONS.csv`
- `docs\befunde\1227_AKTUELLE_REZEPTORSCHICHT_STRESS_QUIET_FELDPHASEN_1H_TRANSITIONS.csv`
- `docs\befunde\1229_SYNTHETISCHE_SINNESACHSEN_STRESS_FELDPHASEN_TRANSITIONS.csv`

## Profil

- Phasenfamilien: `35`
- Qualitaeten: `{'cross_world_open_phase': 29, 'cross_world_phase_family': 6}`
- Wirkungen: `{'phase_offen': 24, 'rekopplung_findet_zentrum': 3, 'zentrum_oeffnet_rekopplung': 3, 'rand_entlastet_in_offenheit': 2, 'offenheit_geraet_in_kippnaehe': 2, 'zentrumsbruch_in_offenheit': 1}`

## Staerkste Phasenfamilien

| Phase | Anzahl | Welten | Wirkung | Qualitaet | Rekopplung danach | Strain danach | Notiz |
|---|---:|---:|---|---|---:|---:|---|
| zentrum_stabil->offene_variante->zentrum_stabil | 2808 | 12 | phase_offen | cross_world_open_phase | 0.0480 | -0.0378 | Feldphase bleibt offen lesbar |
| offene_variante->zentrum_stabil->offene_variante | 2503 | 12 | phase_offen | cross_world_open_phase | -0.0454 | 0.0344 | Feldphase bleibt offen lesbar |
| rekopplungsnaehe->zentrum_stabil->offene_variante | 1532 | 12 | phase_offen | cross_world_open_phase | -0.0485 | 0.0384 | Feldphase bleibt offen lesbar |
| zentrum_stabil->rekopplungsnaehe->zentrum_stabil | 1367 | 12 | rekopplung_findet_zentrum | cross_world_phase_family | 0.0181 | -0.0070 | Rekopplungsnaehe findet Zentrum |
| offene_variante->zentrum_stabil->rekopplungsnaehe | 1264 | 12 | zentrum_oeffnet_rekopplung | cross_world_open_phase | -0.0134 | 0.0015 | Feldphase bleibt offen lesbar |
| zentrum_stabil->offene_variante->rekopplungsnaehe | 1261 | 12 | phase_offen | cross_world_open_phase | 0.0321 | -0.0288 | Feldphase bleibt offen lesbar |
| offene_variante->rekopplungsnaehe->zentrum_stabil | 1065 | 12 | rekopplung_findet_zentrum | cross_world_phase_family | 0.0181 | -0.0133 | Rekopplungsnaehe findet Zentrum |
| rekopplungsnaehe->offene_variante->zentrum_stabil | 969 | 11 | phase_offen | cross_world_open_phase | 0.0424 | -0.0299 | Feldphase bleibt offen lesbar |
| offene_variante->rekopplungsnaehe->offene_variante | 954 | 11 | phase_offen | cross_world_open_phase | -0.0314 | 0.0308 | Feldphase bleibt offen lesbar |
| rekopplungsnaehe->zentrum_stabil->rekopplungsnaehe | 779 | 12 | zentrum_oeffnet_rekopplung | cross_world_open_phase | -0.0160 | 0.0042 | Feldphase bleibt offen lesbar |
| zentrum_stabil->rekopplungsnaehe->offene_variante | 639 | 11 | phase_offen | cross_world_open_phase | -0.0307 | 0.0328 | Feldphase bleibt offen lesbar |
| rekopplungsnaehe->offene_variante->rekopplungsnaehe | 594 | 11 | phase_offen | cross_world_open_phase | 0.0307 | -0.0266 | Feldphase bleibt offen lesbar |
| zentrum_stabil->spannungsrand_kippnaehe->zentrum_stabil | 311 | 11 | phase_offen | cross_world_open_phase | 0.1126 | -0.1372 | Feldphase bleibt offen lesbar |
| offene_variante->zentrum_stabil->spannungsrand_kippnaehe | 289 | 11 | phase_offen | cross_world_open_phase | -0.1410 | 0.1511 | Feldphase bleibt offen lesbar |
| spannungsrand_kippnaehe->offene_variante->zentrum_stabil | 284 | 11 | phase_offen | cross_world_open_phase | 0.0549 | -0.0405 | Feldphase bleibt offen lesbar |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | 259 | 11 | zentrumsbruch_in_offenheit | cross_world_phase_family | 0.0775 | -0.1018 | zentrumsnahe Ordnung bricht kurz und entlastet in offenen Neuordnungsraum |
| spannungsrand_kippnaehe->offene_variante->rekopplungsnaehe | 207 | 11 | phase_offen | cross_world_open_phase | 0.0408 | -0.0385 | Feldphase bleibt offen lesbar |
| offene_variante->spannungsrand_kippnaehe->offene_variante | 186 | 10 | rand_entlastet_in_offenheit | cross_world_phase_family | 0.0737 | -0.0950 | Randspannung bleibt nicht stehen, sondern entlastet in Offenheit |
| rekopplungsnaehe->zentrum_stabil->spannungsrand_kippnaehe | 176 | 11 | phase_offen | cross_world_open_phase | -0.1428 | 0.1507 | Feldphase bleibt offen lesbar |
| spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | 174 | 2 | phase_offen | cross_world_open_phase | -0.1109 | 0.1341 | Feldphase bleibt offen lesbar |
| spannungsrand_kippnaehe->zentrum_stabil->offene_variante | 140 | 11 | phase_offen | cross_world_open_phase | -0.0649 | 0.0768 | Feldphase bleibt offen lesbar |
| zentrum_stabil->offene_variante->spannungsrand_kippnaehe | 105 | 9 | phase_offen | cross_world_open_phase | -0.0851 | 0.1038 | Feldphase bleibt offen lesbar |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | 93 | 11 | rand_entlastet_in_offenheit | cross_world_phase_family | 0.0792 | -0.0994 | Randspannung bleibt nicht stehen, sondern entlastet in Offenheit |
| zentrum_stabil->spannungsrand_kippnaehe->rekopplungsnaehe | 69 | 11 | phase_offen | cross_world_open_phase | 0.0986 | -0.1165 | Feldphase bleibt offen lesbar |

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
