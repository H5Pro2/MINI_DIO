# MCM-Feldphasen Rohfeld-Kopplung

Stand: 2026-07-02

## Grundfrage

Sind situative Randphasen eher durch Rohfeldlast, Rekopplungsbruch, Entlastung, Zeitrahmen oder Assetcharakter lesbar?

## Eingaben

- `docs\befunde\1245_MCM_FELDPHASEN_KLASSEN.csv`
- `docs\befunde\1246_MCM_FELDPHASEN_WELTARTEN_TRIGGER.csv`

## Profil

- untersuchte Phasen: `10`
- Phasenklassen: `{'weltgebundene_feldphase': 5, 'grenzphase_mit_entlastung': 3, 'lokale_oder_driftende_phase': 1, 'junge_phasenspur': 1}`
- Kopplungsklassen: `{'last_mit_entlastender_folge': 7, 'rekopplung_vor_belastung': 2, 'gemischte_rohfeldkopplung': 1}`

## Rohfeld-Kopplung

| Phase | Klasse | Kopplung | Intake | Rekopplung | Strain | Delta Rekopplung | Delta Strain | Top-Weltart | Top-Asset | Zeit |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| offene_variante->spannungsrand_kippnaehe->offene_variante | grenzphase_mit_entlastung | last_mit_entlastender_folge | 0.1411 | 0.5910 | 0.2819 | 0.0609 | -0.0942 | stress_oder_negative_welt | SOL | 5m |
| zentrum_stabil->spannungsrand_kippnaehe->offene_variante | grenzphase_mit_entlastung | last_mit_entlastender_folge | 0.4308 | 0.5901 | 0.2808 | 0.0738 | -0.0961 | stress_oder_negative_welt | - | unbekannt |
| rekopplungsnaehe->spannungsrand_kippnaehe->offene_variante | grenzphase_mit_entlastung | last_mit_entlastender_folge | 0.3727 | 0.5892 | 0.2790 | 0.0734 | -0.0962 | ruhige_oder_seitwaerts_welt | BTC | unbekannt |
| spannungsrand_kippnaehe->zentrum_stabil->spannungsrand_kippnaehe | lokale_oder_driftende_phase | rekopplung_vor_belastung | 0.1153 | 0.7391 | 0.1409 | -0.1116 | 0.1343 | synthetische_sinneswelt | SYNTH | unbekannt |
| spannungsrand_kippnaehe->zentrum_stabil->rekopplungsnaehe | weltgebundene_feldphase | gemischte_rohfeldkopplung | 0.1291 | 0.7173 | 0.1454 | -0.0121 | 0.0001 | alt_asset_welt | BTC | 5m |
| offene_variante->spannungsrand_kippnaehe->rekopplungsnaehe | weltgebundene_feldphase | last_mit_entlastender_folge | 0.3615 | 0.5919 | 0.2719 | 0.1131 | -0.1211 | stress_oder_negative_welt | BTC | 5m |
| offene_variante->spannungsrand_kippnaehe->zentrum_stabil | weltgebundene_feldphase | last_mit_entlastender_folge | 0.3452 | 0.5983 | 0.2653 | 0.1219 | -0.1238 | stress_oder_negative_welt | BTC | unbekannt |
| rekopplungsnaehe->spannungsrand_kippnaehe->rekopplungsnaehe | weltgebundene_feldphase | last_mit_entlastender_folge | 0.3982 | 0.5989 | 0.2715 | 0.1046 | -0.1167 | alt_asset_welt | - | 5m |
| rekopplungsnaehe->spannungsrand_kippnaehe->zentrum_stabil | weltgebundene_feldphase | last_mit_entlastender_folge | 0.3785 | 0.5989 | 0.2628 | 0.1205 | -0.1186 | ruhige_oder_seitwaerts_welt | BTC | 5m |
| spannungsrand_kippnaehe->rekopplungsnaehe->spannungsrand_kippnaehe | junge_phasenspur | rekopplung_vor_belastung | 0.1090 | 0.7049 | 0.1368 | -0.1045 | 0.1186 | expansive_oder_positive_welt | - | 10k_segment |

## Befund

Die situativen Randphasen sind rohfeldseitig vor allem als Kopplungsereignisse lesbar.

Wichtig ist die Trennung:

```text
Rand/Kipp als Zustand ist nicht automatisch Kollaps.
Entscheidend ist, ob danach Rekopplung steigt und Strain faellt.
```

Grenzphasen mit Entlastung zeigen genau diese Richtung: Belastung wird sichtbar, danach nimmt Rekopplung zu und Strain faellt.

Weltgebundene Randphasen sind uneinheitlicher. Sie koennen aus Stress-/Negativwelt, Alt-Asset-Kontext, ruhigen/seitwaerts Welten oder synthetischen Sinneswelten kommen.

## Bedeutung

Damit wird die MCM-Lesung genauer:

```text
Nicht die Randnaehe allein ist entscheidend.
Entscheidend ist die Feldbewegung nach der Randnaehe.
```

## Grenze

Diese Diagnose nutzt aggregierte Feldphasenwerte. Fuer eine vollstaendige Rohwelt-Erklaerung muessen spaeter OHLCV-Fenster, Ton-/Lautheitsprofile und Rezeptorprofile direkt pro Phase angebunden werden.

## Wie es weitergeht

Als naechstes sollte fuer die wichtigsten Randphasen eine echte Fensterlupe gebaut werden: Phase finden, Rohweltfenster ziehen, Ton-/Intake-/Rekopplungsprofil danebenlegen.
