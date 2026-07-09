# MCM-Feldphasen Rohwelt-Fensterlupe

Stand: 2026-07-02

## Grundfrage

Welche konkrete Rohweltbewegung steht unter den zuvor gefundenen MCM-Feldphasen-Fenstern?

## Hierarchie

```text
Grundfrage: Feldfolge um Rand/Kipp
Unterpruefung: konkrete Rohweltbewegung im gleichen Tickbereich
Folgeschritt: Ton-/Rezeptorprofil mit Rohchartfenster zusammenlegen
```

## Eingabe

- Feldfenster: `docs\befunde\1249_MCM_FELDPHASEN_FENSTERLUPE.csv`
- Rohwelt-Zuordnung: nur eindeutig gemappte CSV-Dateien aus `data/`

## Profil

- gekoppelte Rohfenster: `256`
- nicht gekoppelte Events: `{'keine_eindeutige_rohwelt': 213}`
- Bewegungsarten: `{'bewegungsbruch': 255, 'gemischte_rohwelt': 1}`
- Feldfenster-Lesarten: `{'lastkontakt_entlastet': 253, 'rekopplung_bricht_in_last': 3}`
- Welten: `{'POS_EXPANSION_10K': 47, 'XRP_5M_10K': 43, 'NEG_STRESS_10K': 38, 'DOGE_5M_10K': 32, 'SIDEWAYS_10K': 30, 'BTC_1H_2K': 16, 'PAXG_5M_10K': 13, 'SOL_1H_2K': 11, 'SOL_5M_2K': 9, 'KAS_5M_2K': 9, 'BTC_5M_2K': 8}`

## Phasenbezug

- `zentrum_stabil->spannungsrand_kippnaehe->offene_variante`: `130`
- `offene_variante->spannungsrand_kippnaehe->offene_variante`: `92`
- `rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante`: `27`
- `rekopplungsnaehe->spannungsrand_kippnaehe->rekopplungsnaehe`: `4`
- `offene_variante->spannungsrand_kippnaehe->rekopplungsnaehe`: `2`
- `offene_variante->spannungsrand_kippnaehe->zentrum_stabil`: `1`

## Staerkste gekoppelte Fenster

| Phase | Welt | Tick | Feldlesart | Bewegung | Return | Range | Expansion | Richtung | Loudness | Strain | Folge |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| offene_variante->spannungsrand_kippnaehe->offene_variante | SIDEWAYS_10K | 4233 | lastkontakt_entlastet | bewegungsbruch | -0.0188 | 0.0242 | 2.9874 | 0.0725 | 0.9519 | 0.3461 | reko 0.112921, strain -0.136681 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | NEG_STRESS_10K | 8955 | lastkontakt_entlastet | bewegungsbruch | -0.0045 | 0.0383 | 2.4250 | 0.0909 | 0.9045 | 0.3389 | reko 0.142662, strain -0.167226 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | XRP_5M_10K | 8809 | lastkontakt_entlastet | bewegungsbruch | 0.0133 | 0.0511 | 10.3566 | 0.0909 | 0.9603 | 0.3382 | reko 0.102462, strain -0.128729 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | SIDEWAYS_10K | 547 | lastkontakt_entlastet | bewegungsbruch | 0.0734 | 0.0969 | 2.9649 | 0.2174 | 0.8642 | 0.3359 | reko 0.113509, strain -0.143231 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | XRP_5M_10K | 1929 | lastkontakt_entlastet | bewegungsbruch | -0.0028 | 0.0174 | 4.4375 | 0.0606 | 0.9265 | 0.3356 | reko 0.079648, strain -0.102336 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | POS_EXPANSION_10K | 2314 | lastkontakt_entlastet | bewegungsbruch | 0.0116 | 0.0343 | 5.7687 | 0.0333 | 0.9628 | 0.3356 | reko 0.108985, strain -0.153367 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | DOGE_5M_10K | 6408 | lastkontakt_entlastet | bewegungsbruch | -0.0372 | 0.0471 | 4.2016 | 0.1714 | 0.9013 | 0.3347 | reko 0.13561, strain -0.160545 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | POS_EXPANSION_10K | 5480 | lastkontakt_entlastet | bewegungsbruch | -0.0246 | 0.0444 | 3.5657 | 0.0145 | 0.8439 | 0.3335 | reko 0.115333, strain -0.143606 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | SOL_5M_2K | 1776 | lastkontakt_entlastet | bewegungsbruch | -0.0111 | 0.0497 | 5.2969 | 0.0571 | 0.9561 | 0.3302 | reko 0.094494, strain -0.113216 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | SIDEWAYS_10K | 291 | lastkontakt_entlastet | bewegungsbruch | -0.1298 | 0.1507 | 2.4014 | 0.3824 | 0.8827 | 0.3297 | reko 0.117051, strain -0.161918 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | DOGE_5M_10K | 406 | lastkontakt_entlastet | bewegungsbruch | 0.0009 | 0.0208 | 4.4431 | 0.2121 | 0.8367 | 0.3297 | reko 0.129793, strain -0.166437 |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | XRP_5M_10K | 2375 | lastkontakt_entlastet | bewegungsbruch | -0.0085 | 0.0129 | 3.1900 | 0.0000 | 0.8227 | 0.3291 | reko 0.116292, strain -0.150527 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | BTC_5M_2K | 803 | lastkontakt_entlastet | bewegungsbruch | 0.0019 | 0.0366 | 4.2159 | 0.1429 | 0.8673 | 0.3288 | reko 0.116212, strain -0.149028 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | DOGE_5M_10K | 8179 | lastkontakt_entlastet | bewegungsbruch | 0.0317 | 0.0536 | 9.7371 | 0.0149 | 0.6618 | 0.3284 | reko 0.076725, strain -0.11989 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | PAXG_5M_10K | 1024 | lastkontakt_entlastet | bewegungsbruch | -0.0044 | 0.0089 | 6.8580 | 0.0870 | 0.8023 | 0.3280 | reko 0.116706, strain -0.150507 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | NEG_STRESS_10K | 4370 | lastkontakt_entlastet | bewegungsbruch | 0.0181 | 0.0671 | 3.0199 | 0.0303 | 0.8781 | 0.3275 | reko 0.13532, strain -0.158434 |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | XRP_5M_10K | 8584 | lastkontakt_entlastet | bewegungsbruch | -0.0269 | 0.0420 | 3.2431 | 0.0323 | 0.8188 | 0.3271 | reko 0.111338, strain -0.134014 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | POS_EXPANSION_10K | 7063 | lastkontakt_entlastet | bewegungsbruch | 0.0651 | 0.0885 | 6.1283 | 0.1343 | 0.9158 | 0.3268 | reko 0.069325, strain -0.104215 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | POS_EXPANSION_10K | 1000 | lastkontakt_entlastet | bewegungsbruch | -0.0361 | 0.0568 | 6.6047 | 0.1746 | 0.8801 | 0.3264 | reko 0.102961, strain -0.136208 |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | SOL_5M_2K | 276 | lastkontakt_entlastet | bewegungsbruch | 0.0191 | 0.0554 | 3.2024 | 0.0145 | 0.9159 | 0.3251 | reko 0.09367, strain -0.130778 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | SOL_5M_2K | 1759 | lastkontakt_entlastet | bewegungsbruch | 0.0157 | 0.0569 | 5.7413 | 0.2286 | 0.8671 | 0.3243 | reko 0.071296, strain -0.09808 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | XRP_5M_10K | 8448 | lastkontakt_entlastet | bewegungsbruch | -0.0032 | 0.0104 | 4.3870 | 0.0476 | 0.8867 | 0.3242 | reko 0.135064, strain -0.152588 |
| offene_variante->spannungsrand_kippnaehe->offene_variante | POS_EXPANSION_10K | 307 | lastkontakt_entlastet | bewegungsbruch | 0.0008 | 0.0199 | 5.0508 | 0.0492 | 0.9165 | 0.3242 | reko 0.091261, strain -0.126303 |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | DOGE_5M_10K | 6434 | lastkontakt_entlastet | bewegungsbruch | -0.0493 | 0.0654 | 4.4091 | 0.2000 | 0.7619 | 0.3240 | reko 0.114486, strain -0.146912 |

## Befund

Diese Diagnose koppelt Feldfolge und Rohwelt nur dort, wo eine eindeutige Rohdatei vorhanden ist.

Damit wird sichtbar, ob `lastkontakt_entlastet` eher mit gerichteter Bewegung, Bewegungsbruch, Expansion oder gemischter Rohwelt zusammenfaellt.

## Grenze

Viele Feldfenster stammen aus synthetischen oder historisch zusammengesetzten Welten. Diese werden hier bewusst nicht zwangsweise auf Rohdaten gemappt.
