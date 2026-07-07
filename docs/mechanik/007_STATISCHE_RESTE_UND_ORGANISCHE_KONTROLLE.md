# 007 - Statische Reste und organische Kontrolle

Stand: 2026-07-08

## Zweck

Diese Datei trennt statische Elemente im MINI_DIO-System nach ihrer Funktion.

Ziel ist nicht, jede Zahl aus dem Projekt zu entfernen.
Ziel ist, dass keine feste Zahl die Feldbedeutung oder Wahrnehmungsregulation als harte Regel bestimmt.

## Grundregel

```text
Diagnose darf klassifizieren.
Das MCM-Feld darf nicht durch starre Klassen gesteuert werden.
```

Damit gilt:

```text
Auswertungstools:
  duerfen Schwellen nutzen, um Befunde lesbar zu machen.

Runtime/Feldmechanik:
  soll ueber weiche Druckvergleiche, Erfahrung, Wiederkehr und Feldwirkung laufen.
```

## Erste Bereinigung

Zwei Runtime-Bereiche wurden von festen Grenzwerten auf dominante Druckvergleiche umgestellt.

### Adaptive Rekopplung

Vorher:

```text
experience < 0.20        -> adaptive_jung
delta > 0.025            -> adaptive_rekopplung_angehoben
delta < -0.025           -> adaptive_rekopplung_gedaempft
role_experience >= 0.55  -> milieu_rollennah
path_experience >= 0.35  -> milieu_pfadnah
```

Jetzt:

```text
adaptive_jung
adaptive_rekopplung_angehoben
adaptive_rekopplung_gedaempft
adaptive_rekopplung_nahe_statisch

entstehen aus konkurrierenden Druckanteilen.
Die staerkste Feldtendenz benennt den Zustand.
```

### Rezeptorische Achsenpraeferenz

Vorher:

```text
wenn ueberlastet:
  Hoeren runter
  Fuehlen runter

wenn zu duenn:
  Hoeren hoch
  Fuehlen hoch
```

Jetzt:

```text
Hoeren:
  up / down / soften / hold konkurrieren als Druckanteile

Sehen:
  up / down / soften / hold konkurrieren als Druckanteile

Fuehlen:
  up / down / soften / hold konkurrieren als Druckanteile
```

Die jeweilige Achse wird nicht mehr durch eine harte Bedingung gesetzt.
Die dominante innere Tendenz bestimmt die passive Praeferenz.

## Noch vorhandene statische Bereiche

### Diagnose

Viele Dateien unter `tools/` nutzen Schwellen fuer:

```text
zu_duenn
bruch_mit_range_aufweitung
oeffnung_getragen
Rand / Zentrum / Bruecke
```

Das ist akzeptabel, solange diese Werte nur Berichte erzeugen.

### Benennung

Einige Runtime-Dateien benennen Feldrollen noch mit festen Klassifikationen.
Diese Bereiche sind als naechste Kandidaten zu pruefen:

```text
mini_dio/mcm_effect_map.py
mini_dio/worldlage_classifier.py
mini_dio/mcm_fragmentation_memory.py
mini_dio/mcm_role_maturation_memory.py
```

### Kompatibilitaet

`mini_dio/action_selection.py` enthaelt noch aktive Kompatibilitaet.
Dieser Bereich gehoert nicht zum passiven MCM-Forschungskern und muss getrennt bleiben.

## Forschungsgrenze

`volle Kontrolle` bedeutet hier nicht:

```text
DIO bekommt beliebige Handlungsmacht.
```

Gemeint ist:

```text
Das Feld und seine Erfahrungsstruktur duerfen Bedeutung, Aufnahme und Regulation aus ihrer eigenen Lage heraus bilden.
```

Die Kontrolle liegt also nicht in harten Regeln, sondern in:

```text
Wiederkehr
Feldwirkung
Nachhall
Kopplung
Drift
erfahrungsgewichteter Rueckfuehrung
```

## Wie es weitergeht

Als naechstes sollten `mcm_effect_map.py` und `worldlage_classifier.py` geprueft werden. Dort sitzen noch feste Feldrollen-Klassifikationen, die wahrscheinlich in relative Feldrollen oder druckbasierte Lesungen ueberfuehrt werden sollten.
