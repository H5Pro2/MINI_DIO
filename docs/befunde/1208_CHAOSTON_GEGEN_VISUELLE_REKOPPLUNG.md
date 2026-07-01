# Befund 1208 - Chaoston gegen visuelle Rekopplung

## Grundfrage

Befund 1206 zeigte:

```text
Stabile Tonform kann visuelle Formbrueche abfedern.
```

Die Gegenfrage war:

```text
Kann klare visuelle Rekopplung chaotische Tonform ebenso abfedern?
```

## Datengrundlage

- Builder: `data_builder/synthetic_desync_world_builder.py`
- Variant: `visual_recoupling_chaotic_tone`
- Welt: `data/synthetic_mcm_visual_recoupling_chaotic_tone_5m.csv`
- Lauf: `debug/1207_visual_recoupling_chaotic_tone/dio_mini_lauf_2/`
- Topologiematrix: `docs/befunde/1207_VISUELLE_REKOPPLUNG_CHAOSTON_TOPOLOGIE_MATRIX.md`
- Phasenruecklesung: `docs/befunde/1207_VISUELLE_REKOPPLUNG_CHAOSTON_PHASEN_RUECKLESUNG.md`

## Kerndaten

- Episoden: `6594`
- Topologiezustand: `gemischte_rollenordnung`
- `zentrum_stabil`: `0.9484`
- `offene_variante`: `0.0285`
- `spannungsrand_kippnaehe`: `0.0231`
- Rekopplung: `0.7467`
- Carry: `0.5906`
- Strain: `0.1359`
- Sinneskopplung: `0.8999`

## Phasenbefund

| Phase | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Hoer-Gap | Lautheit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhige_form_leiser_ton | `0.9988` | `0.0000` | `0.0013` | `0.7618` | `0.6192` | `0.1190` | `0.0039` | `0.0068` |
| klare_rekopplung_chaostone | `0.9992` | `0.0008` | `0.0000` | `0.7460` | `0.5895` | `0.1235` | `0.0493` | `0.1013` |
| visuelle_rekopplung_lautimpuls | `0.8700` | `0.0650` | `0.0650` | `0.7399` | `0.5737` | `0.1536` | `0.1076` | `0.2054` |
| klare_form_chaotischer_nachhall | `0.9589` | `0.0400` | `0.0011` | `0.7235` | `0.5546` | `0.1506` | `0.1318` | `0.2634` |
| zweite_rekopplung_chaostone | `0.9150` | `0.0429` | `0.0421` | `0.7498` | `0.5949` | `0.1402` | `0.0683` | `0.1296` |
| stille_schlussrekopplung | `1.0000` | `0.0000` | `0.0000` | `0.7632` | `0.6228` | `0.1188` | `0.0032` | `0.0058` |

## Vergleich gegen Befund 1206

| Gegenprobe | Zentrum | Offen | Rand/Kipp |
|---|---:|---:|---:|
| visuelle Brueche bei stabiler Tonform | `0.9848` | `0.0149` | `0.0003` |
| visuelle Rekopplung bei Chaoston | `0.9484` | `0.0285` | `0.0231` |

## Interpretation

Klare visuelle Rekopplung kann Chaoston teilweise integrieren, aber nicht so stark wie stabile Tonform visuelle Brueche abfedert.

Der Unterschied sitzt vor allem in der Rand-/Kippnaehe:

```text
stabile Tonform gegen visuelle Brueche: Rand/Kipp ca. 0.03%
Chaoston gegen visuelle Rekopplung: Rand/Kipp ca. 2.31%
```

Die Phasen zeigen:

- einfache chaotische Tonform bei klarer Rekopplung bleibt fast zentriert,
- Lautimpuls erzeugt deutlich Rand/Kipp und offene Variante,
- chaotischer Nachhall erzeugt eher offene Variante als Rand,
- Stille rekoppelt das Feld wieder vollstaendig.

## MCM-Lesart

Hoeren bleibt im aktuellen MINI_DIO die staerkere Randachse.

Das bedeutet nicht, dass Hoeren schlecht oder stoerend ist. Es bedeutet:

```text
Die Hoerachse wirkt naeher an zeitlicher Feldspannung.
```

Visuelle Ordnung stabilisiert, aber impulsive Hoerformen koennen trotzdem Randnaehe erzeugen. Umgekehrt kann stabile Tonform visuelle Brueche sehr stark abfedern.

## Schlussfolgerung

Die Sinnesachsen sind nicht gleichwertig austauschbar:

- Sehen liefert Formordnung.
- Hoeren liefert zeitliche Spannung und Rhythmus.
- Das MCM-Feld bildet aus ihrer Kopplungsqualitaet eine Rollenordnung.

Der aktuelle Befund stuetzt die Annahme:

```text
Hoeren ist eine MCM-nahe Stimulationsachse.
Sehen wirkt staerker als strukturelle Einordnung.
```

## Wie es weitergeht

Als naechstes sollte keine weitere Einzelwelt gebaut werden, sondern eine kompakte Vergleichsmatrix ueber die vier Sinnesachsen-Gegenproben: reine Hoerwelt, stabile Form/chaotisches Hoeren, visuelle Brueche/stabile Tonform, visuelle Rekopplung/Chaoston.
