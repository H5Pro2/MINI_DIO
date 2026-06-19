# 320 - MCM-Feldwirkung als fachlicher Alias

## Grundfrage

Soll `fuehlen` im Code weiter der Name fuer MCM-Feldwirkung bleiben?

Antwort:

```text
Kurzfristig ja, aus Kompatibilitaet.
Fachlich nein, weil `fuehlen` nach Hautkontakt klingt.
```

Deshalb wurde ein kompatibler Alias eingefuehrt:

```text
mcm_feldwirkung = fuehlen
```

## Warum kein harter Rename?

`fuehlen` ist tief in bestehenden Debugs, Reports und CSV-Auswertungen verankert.

Ein harter Rename wuerde alte Befunde und bestehende Werkzeuge unnoetig brechen.

Deshalb gilt:

```text
Neue Kernlogik liest bevorzugt `mcm_feldwirkung`.
Alte Reports koennen weiter `fuehlen` lesen.
```

## Umgesetzte Code-Aenderung

Die Sinnesstruktur enthaelt jetzt beide Namen:

```text
senses["mcm_feldwirkung"]
senses["fuehlen"]
```

Beide tragen aktuell dieselben Werte:

- `mcm_coherence`
- `mcm_tension`
- `mcm_asymmetry`

Der fachliche Name ist:

```text
mcm_feldwirkung
```

Der Kompatibilitaetsname ist:

```text
fuehlen
```

## Angepasste Kernbereiche

Folgende Bereiche lesen jetzt bevorzugt `mcm_feldwirkung` und fallen nur bei Bedarf auf `fuehlen` zurueck:

- Mini-MCM-Neuron-Input
- passive Episodenwirkung
- neurochemischer Spiegel
- Syntaxvektor
- Beobachtungsdruck
- sensorische Distanz / Afterimage-Bindung

Der Runner schreibt zusaetzlich neue Debugspalten:

- `mcm_feldwirkung_mcm_coherence`
- `mcm_feldwirkung_mcm_tension`
- `mcm_feldwirkung_mcm_asymmetry`

Die alten Spalten bleiben erhalten:

- `fuehlen_mcm_coherence`
- `fuehlen_mcm_tension`
- `fuehlen_mcm_asymmetry`

## Fachliche Bedeutung

Damit ist klarer:

```text
Sehen und Hoeren erzeugen keine Hautwahrnehmung.
Sie erzeugen Rezeptorwirkung.
Diese Rezeptorwirkung erzeugt MCM-Feldwirkung.
```

`fuehlen` darf spaeter fuer eine echte oder simulierte taktile Achse frei werden.

## Grenze

Dieser Umbau veraendert nicht absichtlich die Feldwerte.

Er ist ein Sprach- und Schnittstellenumbau:

```text
gleiche Werte
saubererer Name
kompatible Ausgabe
```

## Wie es weitergeht

Als naechstes sollten neue Befunde und Werkzeuge bevorzugt `mcm_feldwirkung_*` verwenden. Alte `fuehlen_*`-Spalten bleiben nur noch als Kompatibilitaet fuer historische Reports bestehen.
