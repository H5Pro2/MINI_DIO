# Extreme Expansionswelt-Befund

Stand: 2026-06-18

## Zweck

Nach der positiven Expansionswelt wurde eine stärkere Expansionswelt geprüft.

Die Frage war:

```text
Bleibt Expansion auch bei höherer Weltspannung ruhig_feldzeitnah,
oder kippt sie in Last/Feldzeit?
```

## Geprüfte Welt

```text
data/kontrolliert_2023_extreme_expansion_test1_1000_5m_SOLUSDT.csv
```

Die Welt wurde aus der vorhandenen 10k-Extreme-Expansion als 1000-Zeilen-Testfenster erstellt.

## Ergebnis Der Forschungskette

```text
Kerzen:                   1000
Trades:                   0 -> 0
Episoden:                 994 -> 994
Unique Syntaxsymbole:     947 -> 947
Top-Syntax-Überlappung:   1.0
Top-Familien-Überlappung: 1.0
```

Innenfeldwerte im zweiten Lauf:

```text
MCM-Rekopplung:       0.623022
MCM-Tragqualität:     0.353039
Sinnes-MCM-Kopplung:  0.829622
```

Passive MCM-Wirkungsklassen:

```text
stabil:           466
tragend_unruhig:  388
kippend:           69
gespannt:          60
diffus:            11
```

Episodenzustände:

```text
field_carried:  934
field_strained:  60
```

## Vergleich Zur Positiven Expansion

Positive Expansion:

```text
Rekopplung:       0.633577
Tragqualität:     0.357946
Strain/Kippung:   40
Memory:           40
Lesung:           ruhig_feldzeitnah
```

Extreme Expansion:

```text
Rekopplung:       0.623022
Tragqualität:     0.353039
Strain/Kippung:   129
Memory:           86
Lesung:           last_feldzeitnah
```

## Befund

Die extreme Expansion wird nicht mehr ruhig_feldzeitnah gelesen.

Sie kippt relativ zu Ruhe, Stress und positiver Expansion in:

```text
last_feldzeitnah
```

Das ist wichtig, weil es eine Kippachse sichtbar macht:

```text
ruhige Expansion
  -> getragen, stabil, feldzeitnah

extreme Expansion
  -> weiterhin reproduzierbar, aber mehr Last, mehr Kippnähe,
     schwächere Rekopplung und mehr Episodenmemory
```

## Interpretation

Expansion ist für MINI_DIO nicht automatisch Last.

Aber:

```text
Wenn die Expansion stärker wird, kann dieselbe Bewegungsart
von ruhiger Feldzeitnähe in lastnahe Feldzeit kippen.
```

Das spricht für eine organische Lesung:

- Weltbewegung wird nicht starr klassifiziert.
- Das MCM-Feld liest die Belastbarkeit der Bewegung.
- Feldzeit kann ruhig oder belastet eingebettet sein.
- Reproduzierbarkeit bleibt erhalten, obwohl die Feldqualität kippt.

## Bedeutung Für Die MCM-Lesung

Die Expansionsprüfung trennt drei Zustände:

```text
Ruhe:
  wenig Last, wenig Feldzeitspur

Positive Expansion:
  wenig Last, deutliche Feldzeitspur

Extreme Expansion:
  mehr Last, deutliche Feldzeitspur
```

Damit wird `feldzeitnah` nicht als gut oder schlecht gelesen.

Feldzeit ist eine Tiefe der Feldwirkung.
Ob sie tragend oder belastend wirkt, hängt von Rekopplung, Strain, Memorylast und Sinnes-MCM-Kopplung ab.

## Grenze

Dieser Befund gilt zunächst für einen 1000-Zeilen-Ausschnitt.

Die volle 10k-Welt sollte später mit höherem Timeout geprüft werden, wenn die Laufzeit dafür bewusst eingeplant wird.

## Wie Es Weitergeht

Als nächstes sollte eine weitere Expansionsart geprüft werden:

```text
positive recovery oder late positive.
```

Ziel:

- bleibt die Kippachse stabil?
- gibt es eine Erholungs-Expansion, die wieder ruhiger wird?
- bildet sich zwischen ruhig_feldzeitnah und last_feldzeitnah eine Übergangsform?

