# 1994 - Erste MCM-Rollenmatrix

## Grundfrage

Die letzten Pruefungen haben mehrere wiederkehrende Rollen sichtbar gemacht. Diese Matrix ordnet sie nicht nach Symbolnamen, sondern nach Feldfunktion.

## Datenbasis

- `0hiolzy`: PEPE-A, situative Milieuinsel
- `1yxc2ug`: PEPE-C, aktive Grundrollen-Rekopplung
- `0hvxln3`: 9-Welten-Ruecklesung
- `14sn1ov`: 9-Welten-Ruecklesung

Ausgabe:

- `docs/befunde/1001-2000/1751-2000/1994_MCM_ROLLENMATRIX_FUNKTIONSKARTE.csv`

## Matrix

| Rolle | Funktionsklasse | Unterform | Hauptmerkmal |
|---|---|---|---|
| `0hiolzy` | Milieuinsel | ruhig rekoppelnd tief | langes Segment, hoher Nachhall, hohe Wiederkehr |
| `1yxc2ug` | Aktive Rekopplung | verteilt aktiv rauer | mehrere Segmente, mehr Weltaktivitaet, weniger Tiefe |
| `0hvxln3` | Aktive Rekopplung | kompakt stark getragen | sehr kurze Segmente, hohe Tragung, mehrweltlich |
| `14sn1ov` | Aktive Rekopplung | visuell offen beanspruchend | kurze Segmente, hohe visuelle Luecke, mehrweltlich |

## Messbare Trennung

`0hiolzy`:

- 769 Treffer
- 10 Segmente
- laengstes Segment 668 Ticks
- Nachhall ca. 0.828
- Wiederkehr ca. 0.941

`1yxc2ug`:

- 304 Treffer
- 26 Segmente
- laengstes Segment 31 Ticks
- Nachhall ca. 0.617
- Wiederkehr ca. 0.666

`0hvxln3`:

- in 9 Welten sichtbar
- mittlere Trefferzahl ca. 42.7
- mittlere Segmentzahl ca. 24.1
- laengstes Segment durchgehend 3 Ticks
- Nachhall ca. 0.472
- Wiederkehr ca. 0.535

`14sn1ov`:

- in 9 Welten sichtbar
- mittlere Trefferzahl ca. 44.0
- mittlere Segmentzahl ca. 22.1
- laengstes Segment durchgehend 3 Ticks
- Nachhall ca. 0.479
- Wiederkehr ca. 0.541

## Interpretation

MINI_DIO bildet keine reine Symboltabelle. Die gleiche Speicherebene traegt unterschiedliche Feldfunktionen:

- **Milieuinsel:** lange, tiefe, phasengebundene Bedeutungsverdichtung.
- **Aktive Rekopplung:** kurze, wiederkehrende, dynamische Kontaktfunktion.
- **Unterform kompakt:** staerker getragen, klarer angebunden.
- **Unterform visuell offen:** staerker visuell beansprucht, offener, weniger kompakt.

Damit entsteht eine erste MCM-Funktionskarte.

## Bedeutung fuer DIO

Fuer die weitere Entwicklung ist dieser Punkt zentral:

DIO sollte nicht nur speichern:

```text
Dieses Symbol kam wieder vor.
```

Sondern:

```text
Dieses Symbol kam wieder vor und wirkte als bestimmte Feldfunktion.
```

Das ist eine andere Qualitaet von Memory. Es entsteht ein Speicher von Bedeutungsrollen:

- Was ist lang und tief?
- Was ist kurz und aktiv?
- Was ist Bruecke?
- Was ist Randspannung?
- Was ist offene visuelle Beanspruchung?
- Was ist kompakte Rekopplung?

## Schlussfolgerung

Die Rollenmatrix ist ein erster Schritt von Symbolspeicher zu Feldfunktionsspeicher. Das ist fuer ein reiferes DIO-System wichtig, weil spaetere Wahrnehmung und moegliche Handlung nicht aus festen Regeln entstehen sollten, sondern aus gereifter Rollenfunktion.

## Wie es weitergeht

Als naechstes sollte die Rollenmatrix in eine mechanische Struktur ueberfuehrt werden: MINI_DIO sollte Feldfunktionsqualitaeten passiv im Memory mittragen koennen, ohne daraus direkte Handlung abzuleiten.
