# MCM-Feldphasen-Klassen

Stand: 2026-07-01

## Zweck

Diese Diagnose trennt die Feldphasen-Memory in allgemeine, breit getragene, weltgebundene und junge/driftende Phasen.

Die Klassifikation ist relativ zur gelesenen Mehrwelt-Matrix. Sie ist keine feste Regel fuer MINI_DIO.

## Eingabe

- `docs\befunde\1243_MCM_FELDPHASEN_MEMORY_MEHRWELT.csv`

## Profil

- Phasenfamilien: `36`
- Klassen: `{'breit_getragene_feldphase': 14, 'allgemeine_feldphase': 12, 'weltgebundene_feldphase': 5, 'grenzphase_mit_entlastung': 3, 'lokale_oder_driftende_phase': 1, 'junge_phasenspur': 1}`
- Rollenfamilien: `{'rand_offen_kopplung': 14, 'zentrum_offen_rekopplung': 12, 'randgebundene_phase': 10}`

## Klassenuebersicht

| Klasse | Anzahl | Lesart |
|---|---:|---|
| breit_getragene_feldphase | 14 | ueber viele Welten sichtbar, aber weniger dicht |
| allgemeine_feldphase | 12 | ueber viele Welten und mit hoher Wiederkehr getragen |
| weltgebundene_feldphase | 5 | an bestimmte Welten oder Weltarten gebunden |
| grenzphase_mit_entlastung | 3 | Rand/Kipp wirkt als Grenzimpuls mit Entlastung |
| lokale_oder_driftende_phase | 1 | lokal sichtbar oder noch nicht stabil getragen |
| junge_phasenspur | 1 | einzelne junge Spur, noch keine Familie |

## Relevante Phasen

### allgemeine_feldphase

| Phase | Anzahl | Weltdeckung | Dichte | Wirkung | Rollenfamilie |
|---|---:|---:|---:|---|---|
| zentrum_stabil->offene_variante->zentrum_stabil | 8997 | 0.9474 | 1.0000 | phase_offen | zentrum_offen_rekopplung |
| offene_variante->zentrum_stabil->offene_variante | 7764 | 0.9737 | 0.8630 | phase_offen | zentrum_offen_rekopplung |
| rekopplungsnaehe->zentrum_stabil->offene_variante | 5140 | 0.9474 | 0.5713 | phase_offen | zentrum_offen_rekopplung |
| zentrum_stabil->rekopplungsnaehe->zentrum_stabil | 5112 | 0.9474 | 0.5682 | rekopplung_findet_zentrum | zentrum_offen_rekopplung |
| offene_variante->zentrum_stabil->rekopplungsnaehe | 4248 | 0.9474 | 0.4722 | zentrum_oeffnet_rekopplung | zentrum_offen_rekopplung |
| zentrum_stabil->offene_variante->rekopplungsnaehe | 3807 | 0.9474 | 0.4231 | phase_offen | zentrum_offen_rekopplung |
| offene_variante->rekopplungsnaehe->zentrum_stabil | 3378 | 0.9474 | 0.3755 | rekopplung_findet_zentrum | zentrum_offen_rekopplung |
| rekopplungsnaehe->zentrum_stabil->rekopplungsnaehe | 2985 | 0.9474 | 0.3318 | zentrum_oeffnet_rekopplung | zentrum_offen_rekopplung |
| offene_variante->rekopplungsnaehe->offene_variante | 2950 | 1.0000 | 0.3279 | phase_offen | zentrum_offen_rekopplung |
| rekopplungsnaehe->offene_variante->zentrum_stabil | 2880 | 0.9211 | 0.3201 | phase_offen | zentrum_offen_rekopplung |
| zentrum_stabil->rekopplungsnaehe->offene_variante | 2036 | 0.8947 | 0.2263 | phase_offen | zentrum_offen_rekopplung |
| rekopplungsnaehe->offene_variante->rekopplungsnaehe | 1964 | 0.9737 | 0.2183 | phase_offen | zentrum_offen_rekopplung |

### grenzphase_mit_entlastung

| Phase | Anzahl | Weltdeckung | Dichte | Wirkung | Rollenfamilie |
|---|---:|---:|---:|---|---|
| offene_variante->spannungsrand_kippnaehe->offene_variante | 1341 | 0.7632 | 0.1490 | rand_entlastet_in_offenheit | rand_offen_kopplung |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | 772 | 0.9211 | 0.0858 | zentrumsbruch_in_offenheit | rand_offen_kopplung |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | 212 | 0.7632 | 0.0236 | rand_entlastet_in_offenheit | rand_offen_kopplung |

### breit_getragene_feldphase

| Phase | Anzahl | Weltdeckung | Dichte | Wirkung | Rollenfamilie |
|---|---:|---:|---:|---|---|
| spannungsrand_kippnaehe->offene_variante->spannungsrand_kippnaehe | 874 | 0.7368 | 0.0971 | phase_offen | rand_offen_kopplung |
| spannungsrand_kippnaehe->offene_variante->zentrum_stabil | 798 | 0.9474 | 0.0887 | phase_offen | rand_offen_kopplung |
| spannungsrand_kippnaehe->offene_variante->rekopplungsnaehe | 652 | 1.0000 | 0.0725 | phase_offen | rand_offen_kopplung |
| offene_variante->zentrum_stabil->spannungsrand_kippnaehe | 648 | 0.8947 | 0.0720 | phase_offen | rand_offen_kopplung |
| rekopplungsnaehe->zentrum_stabil->spannungsrand_kippnaehe | 475 | 0.9211 | 0.0528 | phase_offen | randgebundene_phase |
| zentrum_stabil->spannungsrand_kippnaehe->zentrum_stabil | 380 | 0.5789 | 0.0422 | phase_offen | randgebundene_phase |
| zentrum_stabil->offene_variante->spannungsrand_kippnaehe | 304 | 0.7105 | 0.0338 | phase_offen | rand_offen_kopplung |
| rekopplungsnaehe->offene_variante->spannungsrand_kippnaehe | 220 | 0.7105 | 0.0245 | phase_offen | rand_offen_kopplung |
| spannungsrand_kippnaehe->zentrum_stabil->offene_variante | 206 | 0.7105 | 0.0229 | phase_offen | rand_offen_kopplung |
| zentrum_stabil->spannungsrand_kippnaehe->rekopplungsnaehe | 152 | 0.6053 | 0.0169 | phase_offen | randgebundene_phase |
| offene_variante->rekopplungsnaehe->spannungsrand_kippnaehe | 126 | 0.7632 | 0.0140 | phase_offen | rand_offen_kopplung |
| zentrum_stabil->rekopplungsnaehe->spannungsrand_kippnaehe | 126 | 0.5526 | 0.0140 | phase_offen | randgebundene_phase |

### lokale_oder_driftende_phase

| Phase | Anzahl | Weltdeckung | Dichte | Wirkung | Rollenfamilie |
|---|---:|---:|---:|---|---|
| spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | 181 | 0.1579 | 0.0201 | phase_offen | randgebundene_phase |

### weltgebundene_feldphase

| Phase | Anzahl | Weltdeckung | Dichte | Wirkung | Rollenfamilie |
|---|---:|---:|---:|---|---|
| spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | 43 | 0.4211 | 0.0048 | zentrum_oeffnet_rekopplung | randgebundene_phase |
| offene_variante->spannungsrand_kippnaehe->zentrum_stabil | 32 | 0.5263 | 0.0036 | offenheit_geraet_in_kippnaehe | rand_offen_kopplung |
| offene_variante->spannungsrand_kippnaehe->rekopplungsnaehe | 32 | 0.4474 | 0.0036 | offenheit_geraet_in_kippnaehe | rand_offen_kopplung |
| rekopplungsnaehe->spannungsrand_kippnaehe->rekopplungsnaehe | 23 | 0.2895 | 0.0026 | phase_offen | randgebundene_phase |
| rekopplungsnaehe->spannungsrand_kippnaehe->zentrum_stabil | 18 | 0.2895 | 0.0020 | phase_offen | randgebundene_phase |

### junge_phasenspur

| Phase | Anzahl | Weltdeckung | Dichte | Wirkung | Rollenfamilie |
|---|---:|---:|---:|---|---|
| spannungsrand_kippnaehe->rekopplungsnaehe->spannungsrand_kippnaehe | 1 | 0.0263 | 0.0001 | phase_offen | randgebundene_phase |

## Befund

Die Feldphasen-Memory zeigt eine klare Schichtung:

- Ein Kern aus allgemeinen Zentrum/Offenheit/Rekopplungs-Phasen.
- Ein zweiter Bereich aus Rand/Kipp-Phasen, die meist in Offenheit entlasten.
- Wenige junge oder lokale Spuren.

Damit wirkt die Feldphasen-Memory nicht wie beliebiges Sammeln, sondern wie eine sortierte passive Bewegungsordnung.

## Bedeutung

MINI_DIO bekommt dadurch keine Handlung. Es bekommt eine bessere passive Innenzeit:

```text
nicht nur: Das Feld ist so.
sondern: Das Feld bewegt sich wiederholt so.
```
