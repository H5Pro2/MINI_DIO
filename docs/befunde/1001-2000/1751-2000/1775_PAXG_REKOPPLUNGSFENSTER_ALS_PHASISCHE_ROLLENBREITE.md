# PAXG-Rekopplungsfenster als phasische Rollenbreite

Stand: 2026-07-08

## Grundfrage

Nach 1774 war klar:

```text
PAXG-Rekopplung wirkt nicht wie bloße Mikrodifferenz,
sondern wie Mikrobewegung mit erfahrungsgetragener Anschlussgeschichte.
```

Die nächste Unterprüfung war:

```text
Ist diese rekoppelnde Breite dauerhaft,
oder liegt sie als lokale Phase in einer Nachbarschaft?
```

## Rücklesung

Ausgewertet wurde die PAXG-2024-Sequenz:

```text
reports/paxg_2024_sequence_rawworld_contrast.csv
```

Zusätzlich wurde ein kompakter Nachbarschaftsreport erzeugt:

```text
reports/paxg_2024_rekopplungsfenster_nachbarschaft.csv
reports/paxg_2024_rekopplungsfenster_nachbarschaft.md
```

## Ergebnis

Die vier PAXG-Anschlussfenster zeigen:

```text
0-1000      -> mittlere_uebergangsphase
1000-2000   -> mittlere_uebergangsphase
2000-3000   -> verteilt_rekoppelnd
3000-4000   -> mittlere_uebergangsphase
```

Das rekoppelnde Fenster entspricht:

```text
Basis: data/paxg_2024_follow_candidate_7000_8000.csv
Folge: data/paxg_2024_follow_candidate_8000_9000.csv
```

## Auffällige Werte

Im rekoppelnden Fenster:

```text
Rollen = 5
Kombinationen = 10
Syntax = 182
adaptive_rekopplung_experience = 0.120333
Nachhall = 0.377034
Energie-Delta = +0.089341
Drift-Delta = +0.008977
Range-Delta = +0.000045
```

Die beiden vorherigen Fenster haben mehr Syntax:

```text
Syntax 214
Syntax 226
```

aber nur:

```text
3 Rollen
3 Kombinationen
mittlere_uebergangsphase
```

## Befund

Die rekoppelnde Breite entsteht nicht dort, wo die meisten Zeichen entstehen.

Sie entsteht dort, wo mehrere Rollen und Kombinationen mit erhöhter adaptiver Erfahrung zusammenfallen.

Kurz:

```text
Nicht Zeichenmenge öffnet PAXG,
sondern phasische Anschlussqualität.
```

## Deutung

`verteilt_rekoppelnd` wirkt hier nicht als dauerhafte Asseteigenschaft.

Es wirkt als lokale Feldphase:

```text
mittlere Übergangsphase
-> rekoppelnde Rollenbreite
-> mittlere Übergangsphase
```

Damit wird PAXG als rekopplungsfähiger Pol gestützt, aber nicht als starre Klasse gesetzt.

## Bedeutung für MINI_DIO

MINI_DIO trennt damit drei Ebenen:

- Syntaxdichte,
- Rollenbreite,
- phasische Anschlussqualität.

Diese Trennung ist relevant, weil eine spätere organische Erweiterung nicht auf mehr Zeichen optimieren sollte.

Wichtiger ist:

```text
Welche Feldphase kann mehrere Rollen gleichzeitig halten,
ohne dass sie zerstreut?
```

## Grenze

Der Befund gilt für die bisher rückgelesenen PAXG-2024-Anschlussfenster.

Er sagt noch nicht, ob dieselbe phasische Struktur in PAXG 2025, PAXG 1h oder anderen ruhigen Welten in gleicher Form wiederkehrt.
