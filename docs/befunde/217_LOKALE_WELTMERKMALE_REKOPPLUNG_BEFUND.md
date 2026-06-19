# Lokale Weltmerkmale und Rekopplung - Befund

Stand: 2026-06-19

## Zweck

Diese Notiz bewertet, welche Rohweltmerkmale den Uebergang von aktiv-rekoppelnd zu bindend begleiten.

Geprueft wurden lokale Stress- und Ruhe-/Entlastungssegmente.

## Hierarchie der Pruefung

1. Grundfrage: Welche Weltmerkmale begleiten lokale Rekopplungsbindung?
2. Unterpruefung: Drift, Range, Volumenrhythmus, Richtungswechsel und Verdichtung gegen Feldlast / Memorylast / Rekopplung legen.
3. Folgeschritt: Entscheiden, ob der Uebergang eher durch Weltstruktur oder durch bereits bestehende Feld-/Memorylage entsteht.

## Kernergebnis

Lokale Bindung folgt in den bisherigen Segmenten vor allem:

```text
Rohweltverdichtung + Range + Feldlast + Memorylast
```

Nicht eindeutig dominant ist:

```text
Richtungswechsel allein
```

Der staerkste Unterschied liegt in der Verdichtung:

| Gruppe | Weltverdichtung | Feldlast | Memorylast | Kontrast Bindung-Aktiv |
|---|---:|---:|---:|---:|
| Stress | `12.2503` | `0.1938` | `0.2105` | `-0.0681` |
| Ruhe | `1.9882` | `0.0149` | `0.0404` | `-0.5462` |

Das bedeutet:

Stresssegmente sind nicht nur anders benannt.

Sie tragen messbar mehr Weltverdichtung, mehr Feldlast und mehr Memorylast.

## Staerkste bindende Abschnitte

| Welt | Rolle | Kontrast | Verdichtung | avg Range | Richtungswechsel | Feldlast | Memorylast |
|---|---|---:|---:|---:|---:|---:|---:|
| STRESS_2023_TEST4 | `last_memory_bindend` | `0.1294` | `17.0762` | `0.015069` | `0.4592` | `0.2660` | `0.2447` |
| STRESS_2025_STRESS | `last_memory_bindend` | `0.1203` | `19.0124` | `0.013453` | `0.5204` | `0.2872` | `0.2234` |
| STRESS_2024_REAL | `uebergang_bindend` | `0.0322` | `16.8929` | `0.014709` | `0.4286` | `0.2340` | `0.2447` |

Diese drei Abschnitte zeigen dieselbe Richtung:

- hohe Verdichtung,
- hohe Range,
- hohe Feldlast,
- hohe Memorylast,
- schwächere Rekopplung.

## Wichtiger Gegenfall

`STRESS_2024_SIDEWAYS` bleibt `reiz_aktiv_rekoppelnd`.

Werte:

```text
Verdichtung: 4.6274
Feldlast:    0.0532
Memorylast:  0.0532
Kontrast:   -0.4669
```

Das ist wichtig, weil es die Mechanik organisch haelt:

```text
Stressname allein erzeugt keine Bindung.
```

Erst lokale Verdichtung und Feld-/Memorywirkung bringen das Segment in Richtung Bindung.

## Richtungswechsel

Richtungswechsel unterscheidet die Gruppen nur schwach:

```text
Stress: 0.4458
Ruhe:   0.4143
```

Das ist kein starker Trenner.

Die lokalen Bindungsfaelle haben zwar Richtungswechsel, aber der Richtungswechsel allein erklaert die Bindung nicht.

Wichtiger sind:

- Range,
- Verdichtung,
- Feldlast,
- Memorylast.

## MCM-Deutung

Der Uebergang von aktiv-rekoppelnd zu bindend wirkt bisher nicht wie:

```text
Richtung wechselt -> Bindung
```

Sondern eher wie:

```text
lokale Welt verdichtet sich
  -> Range und Energie nehmen zu
  -> Feldlast steigt
  -> Memorylast steigt
  -> aktive Rekopplung wird ueberholt
```

Das passt zur MCM-Lesart:

Die Weltstruktur wirkt nicht direkt als Regel.

Sie erzeugt eine Innenfeldwirkung.

Erst diese Innenfeldwirkung entscheidet, ob etwas loesbar bleibt oder bindet.

## Bedeutung fuer MINI_DIO

MINI_DIO sollte lokale Weltmerkmale passiv lesen, aber nicht direkt danach reagieren.

Wichtig ist die Trennung:

```text
Rohweltmerkmal
  -> Sinneswirkung
  -> Feldwirkung
  -> Memorywirkung
  -> Rekopplung oder Bindung
```

Damit bleibt die MCM-Logik sauber.

Nicht:

```text
hohe Range -> Lastbindung
```

Sondern:

```text
hohe Range kann Feldlast erzeugen
Feldlast kann Memorylast erzeugen
Memorylast kann Rekopplung ueberholen
```

## Forschungsstand

Umgesetzt als Diagnose:

- `tools/report_local_world_feature_coupling.py`
- `docs/befunde/216_LOKALE_WELTMERKMALE_REKOPPLUNG_DIAGNOSE.md`
- `docs/befunde/216_LOKALE_WELTMERKMALE_REKOPPLUNG_DIAGNOSE.csv`

Der Befund liegt hier:

- `docs/befunde/217_LOKALE_WELTMERKMALE_REKOPPLUNG_BEFUND.md`

## Wie es weitergeht

Als naechstes sollte die Frage nach Feldzustand gegen Weltstruktur geprueft werden.

Grundfrage:

Kann dieselbe oder aehnliche Rohweltverdichtung unterschiedlich wirken, je nachdem in welchem Feldzustand MINI_DIO vorher ist?

Konkrete Unterpruefung:

1. Segmente mit aehnlicher Verdichtung suchen.
2. Pruefen, ob Feldlast / Memorylast trotzdem unterschiedlich ausfallen.
3. Daraus ableiten, ob Rekopplung eine reine Weltstrukturfrage oder eine Feldhistorie-Frage ist.

Das ist wichtig, weil ein organisches MCM-System nicht nur auf Weltwerte reagieren sollte, sondern auf die Kopplung von Weltstruktur und eigener Feldlage.
