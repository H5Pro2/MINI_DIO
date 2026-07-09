# 1721 - Kopplungsvergleich dio_0ly7 und dio_01hu

Stand: 2026-07-07

## Zweck

Diese Datei vergleicht die beiden zuvor robusten Oeffnungs-Kandidaten `dio_0ly7` und `dio_01hu` gegen dieselben synthetischen Zweierkopplungen.

Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.

## Ausgangspunkt

Beide Familien waren in Realwelten als Kandidaten fuer `milieu_oeffnet_nach_entlastung` sichtbar:

```text
dio_0ly7:
  hohe Wiederkehr
  sehr stabile negative Hoer-/Spannungsdeltas

dio_01hu:
  ebenfalls wiederkehrend
  negative Hoer-/Spannungsdeltas
  etwas schwaecher und driftender
```

## Synthetische Zweierkopplung

| Familie | Vorkommen | Lesung |
|---|---:|---|
| dio_0ly7 | 95 | ausreichend sichtbar, achsensensitiv |
| dio_01hu | 2 | zu duenn, Kopplungsqualitaet offen |

## Detail dio_0ly7

```text
Range + Hoeren      -> bruch_mit_range_aufweitung
Range + Spannung    -> bruch_mit_range_aufweitung
Hoeren + Spannung   -> oeffnung_getragen
```

`dio_0ly7` reagiert also differenziert auf die Art der Kopplung.
Die kritische Qualitaet liegt bisher bei Range-Kopplung.

## Detail dio_01hu

```text
Range + Hoeren      -> 0 Vorkommen
Range + Spannung    -> 1 Vorkommen
Hoeren + Spannung   -> 1 Vorkommen
```

`dio_01hu` wird durch diese synthetischen Zweierwelten kaum aktiviert.
Das ist keine Widerlegung der Realwelt-Lesung.
Es zeigt nur, dass `dio_01hu` fuer diese synthetische Kopplungshierarchie nicht dicht genug sichtbar ist.

## Lesung

Der Vergleich trennt zwei verschiedene Eigenschaften:

```text
Realwelt-Robustheit
  heisst nicht automatisch:
  synthetische Kopplungssichtbarkeit

synthetische Kopplungssichtbarkeit
  heisst nicht automatisch:
  allgemeinere Bedeutung
```

Damit wird die MCM-Lesung genauer:

```text
Eine Familie kann in Realwelten stabil sein,
aber unter einer bestimmten kuenstlichen Stoerform kaum auftreten.

Eine andere Familie kann unter derselben Stoerform sichtbar bleiben
und dadurch ihre Kopplungsqualitaet offenlegen.
```

## Forschungsgrenze

`dio_0ly7` ist aktuell der bessere Kandidat fuer die Kopplungshierarchie.
`dio_01hu` bleibt ein Realwelt-Kandidat, aber nicht fuer diese synthetische Zweierkopplungsdiagnose.

## Quellen

- [1716_DIO_0LY7_ZWEIERKOPPLUNG.md](1716_DIO_0LY7_ZWEIERKOPPLUNG.md)
- [1717_DIO_0LY7_ZWEIERKOPPLUNG_KLASSEN.md](1717_DIO_0LY7_ZWEIERKOPPLUNG_KLASSEN.md)
- [1718_DIO_0LY7_KOPPLUNGSHIERARCHIE.md](1718_DIO_0LY7_KOPPLUNGSHIERARCHIE.md)
- [1719_DIO_01HU_ZWEIERKOPPLUNG.md](1719_DIO_01HU_ZWEIERKOPPLUNG.md)
- [1720_DIO_01HU_ZWEIERKOPPLUNG_KLASSEN.md](1720_DIO_01HU_ZWEIERKOPPLUNG_KLASSEN.md)
