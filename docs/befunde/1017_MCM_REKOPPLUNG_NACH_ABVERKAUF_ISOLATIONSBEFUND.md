# 1017 - Rekopplung nach Abverkauf: Isolationsbefund

## Fragestellung

Ist `rekopplung_nach_abverkauf` ein stabiler neuer MCM-Erweiterungstyp, oder nur ein Nebeneffekt einzelner großer 1H-Bewegungen?

## Geprüfte Quellen

- `1013_MCM_ACHSE_TYPEN_WIEDERKEHR_ASSET_ZEIT`
- `1014_MCM_ACHSE_TYPEN_WIEDERKEHR_KAS_GEGENPROBE`
- `1016_MCM_REKOPPLUNG_NACH_ABVERKAUF_ISOLATION`

## Befund

`rekopplung_nach_abverkauf` erscheint bisher in:

| Quelle | Welt | Anzahl | Bemerkung |
|---|---|---:|---|
| 1013 | `BTC_2024_1H` | 2 | Nach vorherigem Abverkauf entsteht ein breites Rekopplungsfenster. |
| 1014 | `KAS2024_1H_ASSET_PROBE` | 2 | Gleiche Grundform bei anderem Asset und ebenfalls 1H. |

In der breiteren 1016-Prüfung über Long-/Quiet-/Stress-Welten erscheint `rekopplung_nach_abverkauf` nicht erneut als eigener Typ.

Dort erscheint aber der verwandte Referenztyp:

| Typ | Anzahl | Bemerkung |
|---|---:|---|
| `abverkauf_mit_rekopplung` | 7 | Abverkauf wird mit Rekopplungsanteil gelesen, über mehrere Welten und Zeitebenen. |

## Interpretation

Der Befund spricht aktuell nicht dafür, `rekopplung_nach_abverkauf` schon als stabilen Einzel-Archetyp zu setzen.

Sauberer ist diese Lesung:

```text
abverkauf_mit_rekopplung
  = stabile Grundfamilie

rekopplung_nach_abverkauf
  = mögliche Erweiterungsform dieser Familie
  = tritt bisher vor allem in großen 1H-Erholungsfenstern auf
```

Damit wäre `rekopplung_nach_abverkauf` kein isolierter Kern, sondern eine konkrete Ausprägung einer größeren MCM-Familie:

```text
Abverkauf
  -> Druck / Bruch / Belastung
  -> lokale Rekopplung
  -> erneute tragende Feldnähe
```

## Forschungsgrenze

Das ist passiv-diagnostisch.

Der Typ wird nicht als Signal, Handlung, Richtung oder Gate verwendet.

## Aktueller Schluss

`rekopplung_nach_abverkauf` ist interessant, aber noch nicht als stabiler eigener MCM-Archetyp bestätigt.

Stärker bestätigt ist aktuell:

```text
abverkauf_mit_rekopplung als wiederkehrende MCM-Typfamilie.
```

Diese Familie kann unter bestimmten Weltbedingungen als `rekopplung_nach_abverkauf` erscheinen.

## Wie es weitergeht

Als nächstes sollte nicht der Einzeltyp, sondern die ganze Familie `abverkauf + rekopplung` geprüft werden: Welche Weltmerkmale lassen sie als Bruch, als Rekopplung oder als Nach-Abverkauf-Erholung erscheinen?
