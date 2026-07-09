# 1718 - dio_0ly7 Kopplungshierarchie

Stand: 2026-07-07

## Zweck

Diese Verdichtung ordnet die bisherigen `dio_0ly7`-Pruefungen hierarchisch:

1. Einzelachsenstoerung
2. Zweierkopplung
3. volle gekoppelte Last

Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.

## Ergebnislinie

| Pruefebene | Sichtbarkeit | Hauptlesung |
|---|---:|---|
| Einzelachsen | 2 von 6 ausreichend sichtbar | wenn sichtbar, `oeffnung_getragen` |
| Zweierkopplung | 3 von 3 sichtbar | Range-Kopplung kippt, Hoeren+Spannung traegt |
| volle gekoppelte Last | 6 von 6 sichtbar | `bruch_mit_range_aufweitung` |

## Detail

Einzelachsen:

```text
isolierte Hoer-, Sicht- oder Desynchronisationsstoerung
-> reicht bisher nicht aus, um dio_0ly7 zu brechen
```

Zweierkopplung:

```text
Range + Hoeren      -> bruch_mit_range_aufweitung
Range + Spannung    -> bruch_mit_range_aufweitung
Hoeren + Spannung   -> oeffnung_getragen
```

Volle gekoppelte Last:

```text
Range-Aufweitung + Hoeranstieg + Spannungsanstieg
-> bruch_mit_range_aufweitung
```

## Lesung

Der aktuelle Befund spricht dafuer, dass `dio_0ly7` nicht durch jede Stoerung kippt.

Die kritische Linie liegt bisher bei Range-Kopplung:

```text
Range allein:
  nicht ausreichend

Hoeren + Spannung:
  bisher getragen

Range + Hoeren oder Range + Spannung:
  Bruch sichtbar

Range + Hoeren + Spannung:
  Bruch stabil sichtbar
```

Damit wird die Bedeutung der Familie nicht als fixer Symbolwert gelesen, sondern als Kopplungsqualitaet:

```text
MCM-Bedeutung = Familie + Weltmilieu + Feldwirkung + Kopplungsgrad
```

## Grenze

Das ist kein Beweis fuer eine Ursache.
Es ist eine reproduzierbare passive Diagnose innerhalb der bisher getesteten Welten.

## Quellen

- [1713_DIO_0LY7_SYNTHETISCHE_ACHSENISOLATION.md](1713_DIO_0LY7_SYNTHETISCHE_ACHSENISOLATION.md)
- [1714_DIO_0LY7_SYNTHETISCHE_ACHSENISOLATION_KLASSEN.md](1714_DIO_0LY7_SYNTHETISCHE_ACHSENISOLATION_KLASSEN.md)
- [1715_DIO_0LY7_EINZELACHSE_GEGEN_GEKOUPPELTE_LAST.md](1715_DIO_0LY7_EINZELACHSE_GEGEN_GEKOUPPELTE_LAST.md)
- [1716_DIO_0LY7_ZWEIERKOPPLUNG.md](1716_DIO_0LY7_ZWEIERKOPPLUNG.md)
- [1717_DIO_0LY7_ZWEIERKOPPLUNG_KLASSEN.md](1717_DIO_0LY7_ZWEIERKOPPLUNG_KLASSEN.md)
