# Synthetische Versatzwelt: mehr Syntax ohne Rollenöffnung

Stand: 2026-07-08

## Grundfrage

Nach Befund 1768 war sichtbar:

```text
Regelmäßige Mehrpaket-Ordnung bindet kompakt,
statt Rollenbreite zu öffnen.
```

Die nächste Frage war:

```text
Erzeugt Asymmetrie mehr Rollenbreite,
wenn ein Paket trägt, ein Paket driftet
und ein Paket verzögert rekoppelt?
```

## Umsetzung

Der synthetische Welt-Builder wurde um das Preset `rekopplungsbreite_versatz` erweitert.

Die Welt enthält:

- ein tragendes Öffnungs-/Rekopplungspaket,
- eine Abstand-/Nachhallphase,
- ein driftendes Paket,
- einen verzögerten Nachhall,
- eine späte Rekopplung,
- eine ruhige Rückbindung.

Geändert wurde nur die kontrollierte Außenwelt. Die MCM-Feldlogik blieb unverändert.

## Ergebnis

Die lokalen 1000er-Anschlüsse zeigten über drei Varianten:

```text
24 von 24 Fenstern: kompakt_nachhallend
0 mittlere Übergangsphasen
0 verteilt offene Phasen
0 verteilt rekoppelnde Phasen
```

Der Versatz erzeugte also keine topologische Rollenöffnung.

## Auffälligkeit

Trotz der kompakten Achsenklasse stieg lokal die Syntaxmenge deutlich.

Die stärksten Fenster lagen bei:

```text
Syntax 48
Syntax 45
Syntax 44
Syntax 41
```

Diese Fenster lagen weiter bei:

```text
1 Rolle
0 Kombinationen
kompakt_nachhallend
```

Damit entsteht eine wichtige Trennung:

```text
Mehr innere Zeichenvarianz ist nicht automatisch mehr Rollenbreite.
```

## Rohwelt-Rücklesung

Die Klassenmittel zeigen:

- Rollen: `1`,
- Kombinationen: `0`,
- Cross-State: `0`,
- Rekopplung: etwa `0.749`,
- Nachhall: etwa `0.733`,
- Basis-Energie höher als bei 1768,
- Folgeenergie leicht fallend,
- Range nahezu stabil,
- Drift leicht fallend.

Kurz:

```text
Die Versatzwelt macht die Oberfläche variabler,
aber das Feld rekoppelt sie weiterhin in eine kompakte Rolle.
```

## Deutung

Der Befund grenzt die Mechanik weiter ein.

Asymmetrie allein reicht nicht.

Versatz allein reicht nicht.

Mehr Syntax allein reicht nicht.

Für `verteilt_rekoppelnd` scheint nicht nur Zeichenvarianz nötig zu sein, sondern echte topologische Ko-Aktivierung:

- mehrere Rollen müssen gleichzeitig oder anschlussfähig aktiv werden,
- diese Rollen müssen miteinander kombinieren,
- die Kombination darf nicht nur offen driften,
- sie muss rekoppeln, ohne in eine einzige Rolle zurückzufallen.

## Bedeutung für MINI_DIO

MINI_DIO zeigt hier eine sinnvolle Eigenschaft:

```text
Das Feld trennt Zeichenvarianz von Rollenvarianz.
```

Das ist wichtig, weil es gegen eine einfache Fehlinterpretation schützt:

```text
Viele Symbole bedeuten nicht automatisch tiefere Feldtopologie.
```

Die aktuelle Lesung lautet:

```text
Die synthetische Welt erzeugt mehr innere Oberflächenvariation,
aber keine neue Rollenmatrix.
```

## Grenze

Diese Prüfung ist ein negativer Befund für diese synthetische Versatzform.

Sie zeigt nicht, dass synthetische Rollenbreite unmöglich ist.

Sie zeigt:

```text
Rollenbreite braucht mehr als Asymmetrie und Symbolzunahme.
```

## Wie es weitergeht

Als nächstes sollte nicht weiter an Paketnamen oder Syntaxmenge gearbeitet werden. Sinnvoller ist eine Ko-Aktivierungsprüfung: zwei unterschiedliche Rollenmilieus müssen zeitlich überlappen oder sich knapp versetzt berühren. Ziel ist zu prüfen, ob erst solche Rollenüberlappung Kombinationen erzeugt.
