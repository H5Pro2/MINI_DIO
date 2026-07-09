# Expansionswelt-Befund

Stand: 2026-06-18

## Zweck

Diese Prüfung untersucht, wie MINI_DIO eine positive Expansionswelt passiv liest.

Die Leitfrage war:

```text
Bleibt Expansion ruhig_feldzeitnah,
wird sie lastnah,
wird sie last_feldzeitnah,
oder erzwingt sie eine neue Mischklasse?
```

## Geprüfte Welt

```text
data/kontrolliert_2023_positive_expansion_test1_1000_5m_SOLUSDT.csv
```

Die Welt wurde aus der vorhandenen 10k-Expansionswelt als 1000-Zeilen-Testfenster erstellt.

## Ergebnis Der Forschungskette

MINI_DIO lief passiv über zwei Läufe mit gleicher Memory.

```text
Kerzen:                  1000
Trades:                  0 -> 0
Episoden:                994 -> 994
Unique Syntaxsymbole:    913 -> 913
Top-Syntax-Überlappung:  1.0
Top-Familien-Überlappung: 1.0
```

Innenfeldwerte im zweiten Lauf:

```text
MCM-Rekopplung:       0.633577
MCM-Tragqualität:     0.357946
Sinnes-MCM-Kopplung:  0.839469
```

Passive MCM-Wirkungsklassen:

```text
stabil:           565
tragend_unruhig:  384
kippend:           18
gespannt:          22
diffus:             5
```

Episodenzustände:

```text
field_carried:  972
field_strained:  22
```

## Feldklassen-Lesung

Im bestehenden Feldklassen-Report wurde die Expansionswelt als:

```text
mittlere Feldlage
```

gelesen.

Das liegt daran, dass die Expansionswelt sehr hohe Rekopplung, hohe Sinnes-MCM-Kopplung und starke stabile Dominanz zeigt, aber die Tragqualität knapp unter der bisherigen ruhigen Nähegruppe liegt.

Wichtig:

```text
Das wirkt nicht wie Stress-Gegenpol.
Es wirkt auch nicht wie eine klare neue Lastklasse.
```

## Relative Kurzsegment-Lesung

Gegen ein ruhiges Segment und ein Stresssegment wurde die Expansionswelt relativ gelesen als:

```text
ruhig_feldzeitnah
```

Vergleich:

```text
Expansion: ruhig_feldzeitnah
Ruhe:      ruhenah
Stress:   lastnah
```

Die Expansionswelt trägt also ruhige Feldnähe, aber mit stärkerer Feldzeitspur als das reine Ruhefenster.

## Interpretation

Die Expansionswelt erzwingt aktuell keine neue Mischklasse.

Sie wirkt eher wie:

```text
ruhige Feldzeitnähe mit Expansionsbewegung
```

Das heißt:

- Das Feld bleibt überwiegend getragen.
- Es entstehen stabile und tragend-unruhige Innenfeldwirkungen.
- Die Spannung bleibt niedrig genug, um nicht in Lastnähe zu kippen.
- Nachhall und Wiederkehr sind sichtbarer als im reinen Ruhefenster.
- Die Expansion scheint nicht als Überlastung gelesen zu werden, sondern als bewegte, noch tragende Feldzeit.

## Bedeutung Für MINI_DIO

Dieser Befund ist wichtig, weil er zeigt:

```text
Bewegung ist nicht automatisch Last.
Expansion ist nicht automatisch Stress.
Ein bewegter Weltkontakt kann feldzeitnah und trotzdem getragen sein.
```

Damit wird die MCM-Lesung feiner:

```text
Ruhe
  -> wenig Last, wenig Feldzeitspur

Expansion
  -> wenig Last, mehr Feldzeitspur, hohe stabile Dominanz

Stress
  -> mehr Last, schwächere Rekopplung, mehr Spannung/Kippnähe
```

## Grenze

Dieser Befund gilt zunächst für den geprüften 1000-Zeilen-Ausschnitt.

Die 10k-Expansionswelt lief noch nicht vollständig durch, weil der erste Versuch in ein Zeitlimit lief. Für eine stärkere Aussage sollte später entweder:

- die volle 10k-Welt mit höherem Timeout laufen,
- oder mehrere 1000er Expansionsfenster aus verschiedenen Abschnitten geprüft werden.

## Wie Es Weitergeht

Als nächstes ist sinnvoll:

```text
Weitere Expansionsfenster prüfen.
```

Ziel:

- bleibt Expansion wieder ruhig_feldzeitnah?
- gibt es eine stärker aktive Expansion, die last_feldzeitnah wird?
- entsteht bei extremer Expansion ein echter Gegenpol?
- bleibt die Topologie stabil, oder bilden sich neue Bedeutungsinseln?

