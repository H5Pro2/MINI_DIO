# Recovery-Expansionswelt-Befund

Stand: 2026-06-18

## Zweck

Nach positiver und extremer Expansion wurde eine Erholungs-Expansion geprüft.

Die Leitfrage:

```text
Findet das Feld nach stärkerer Bewegung wieder in ruhigere Kopplung,
oder bleibt die Lastspur erhalten?
```

## Geprüfte Welt

```text
data/kontrolliert_2025_positive_recovery_test1_1000_5m_SOLUSDT.csv
```

Die Welt wurde aus der vorhandenen 10k-Positive-Recovery-Welt als 1000-Zeilen-Testfenster erstellt.

## Ergebnis Der Forschungskette

```text
Kerzen:                   1000
Trades:                   0 -> 0
Episoden:                 994 -> 994
Unique Syntaxsymbole:     924 -> 924
Top-Syntax-Überlappung:   1.0
Top-Familien-Überlappung: 1.0
```

Innenfeldwerte im zweiten Lauf:

```text
MCM-Rekopplung:       0.630474
MCM-Tragqualität:     0.359369
Sinnes-MCM-Kopplung:  0.836705
```

Passive MCM-Wirkungsklassen:

```text
stabil:           511
tragend_unruhig:  409
gespannt:          32
kippend:           30
rekoppelnd:         1
diffus:            11
```

Episodenzustände:

```text
field_carried:  961
field_strained:  33
```

## Vergleich Der Expansionsachse

Positive Expansion:

```text
Lesung:       ruhig_feldzeitnah
Rekopplung:   0.633577
Strain/Kipp:  40
Memory:       40
```

Extreme Expansion:

```text
Lesung:       lastnah / last_feldzeitnah
Rekopplung:   0.623022
Strain/Kipp:  129
Memory:       86
```

Recovery-Expansion:

```text
Lesung:       ruhig_feldzeitnah
Rekopplung:   0.630474
Strain/Kipp:  62
Memory:       56
```

## Befund

Die Recovery-Expansion findet wieder in eine ruhigere Feldkopplung zurück.

Sie ist nicht so glatt wie die positive Expansion, aber deutlich weniger belastet als die extreme Expansion.

Damit entsteht eine plausible Achse:

```text
positive Expansion
  -> ruhig_feldzeitnah

extreme Expansion
  -> lastnah / last_feldzeitnah

Recovery-Expansion
  -> zurück zu ruhig_feldzeitnah,
     aber mit Restspannung und stärkerer Übergangsbewegung
```

## Interpretation

MINI_DIO liest Expansion nicht als feste Kategorie.

Das Feld unterscheidet:

- getragene Expansion,
- überlastete Expansion,
- erholende Expansion.

Das ist wichtig, weil es eine organische Kipp- und Rückführungsbewegung zeigt.

```text
Weltbewegung kann das Feld belasten.
Wenn Rekopplung und Tragqualität zurückkommen,
wird dieselbe Grundbewegung wieder ruhiger gelesen.
```

## Bedeutung Für Die MCM-Forschung

Die Expansionsachse zeigt keine starre Klassifikation.

Sie zeigt eher:

```text
Feldzustand über Bewegung
```

Die MCM-Feldwirkung scheint nicht nur die äußere Bewegung zu lesen, sondern auch:

- wie tragbar sie ist,
- wie stark sie nachhallt,
- ob sie Last erzeugt,
- ob sie rekoppeln kann,
- ob sie sich wieder beruhigt.

Das passt zur bisherigen These:

```text
Das MCM-Feld bildet eigene Innenordnung aus Weltkontakt.
```

## Grenze

Auch dieser Befund ist zunächst ein 1000-Zeilen-Fenster.

Er ist stark genug als Arbeitsbefund, aber noch kein Abschlussbefund über alle Recovery-Phasen.

## Wie Es Weitergeht

Als nächstes sollten wir gezielt eine Übergangswelt prüfen:

```text
late positive
```

Ziel:

- bildet `late positive` eine echte Übergangsform?
- liegt sie zwischen Recovery und Extreme?
- oder wird sie wieder klar ruhenah/feldzeitnah gelesen?

