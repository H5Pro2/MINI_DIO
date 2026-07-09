# PAXG 1h: offene Rollenbreite statt Rekopplung

Stand: 2026-07-08

## Grundfrage

Nach 1776 blieb offen:

```text
Kann PAXG 1h in anderen Fenstern doch `verteilt_rekoppelnd` bilden,
oder trägt 1h systematisch eher offene Rollenbreite?
```

## Prüfung

Zusätzlich zu den bereits geprüften späten 1h-Fenstern wurden frühe PAXG-1h-Fenster geschnitten und geprüft:

```text
0-1000
1000-2000
2000-3000
3000-4000
```

für:

```text
PAXG 2024 1h
PAXG 2025 1h
```

Die neuen Slices liegen unter:

```text
data/paxg_2024_1h_follow_early_*.csv
data/paxg_2025_1h_follow_early_*.csv
```

Die zusammengeführte Rücklesung liegt in:

```text
reports/paxg_1h_early_late_sequence_rawworld_contrast.csv
reports/paxg_1h_early_late_sequence_rawworld_contrast.md
reports/paxg_1h_early_late_sequence_rawworld_contrast_groups.csv
```

## Ergebnis

Über 12 geprüfte PAXG-1h-Anschlüsse:

```text
8 x verteilt_offen
2 x mittlere_uebergangsphase
2 x kompakt_nachhallend
0 x verteilt_rekoppelnd
```

Die `verteilt_offen`-Fenster tragen im Mittel:

```text
Rollen: 7.125
Kombinationen: 19.0
adaptive_rekopplung_experience: 0.460674
Nachhall: 0.301414
```

## Befund

PAXG 1h ist nicht rollenarm.

Im Gegenteil:

```text
PAXG 1h bildet mehrfach deutliche Rollenbreite.
```

Aber diese Breite wird in der bisherigen Prüfung nicht als `verteilt_rekoppelnd`, sondern als `verteilt_offen` gelesen.

## Deutung

Damit wird die Trennung aus 1776 gestützt:

```text
Rollenbreite ist nicht automatisch Rekopplung.
```

Das 1h-Zeitmaß erzeugt oder erhält Breite, aber die Rückbindung bleibt offenbar anders als bei PAXG 5m.

Vorläufig:

```text
PAXG 5m: phasenweise rekoppelnde Rollenbreite
PAXG 1h: häufig offene Rollenbreite
```

## Bedeutung für MINI_DIO

MINI_DIO liest Zeitmaß nicht nur als Glättung.

1h verändert die Qualität des Feldmilieus:

- weniger lokale Mikroanschlussdichte,
- trotzdem Rollenbreite,
- aber offenere Rückbindung.

Das ist methodisch wichtig, weil daraus folgt:

```text
Breite, Rekopplung und Zeitmaß müssen getrennt gelesen werden.
```

## Grenze

Der Befund gilt für die 12 bisher geprüften PAXG-1h-Anschlüsse.

Er ist stark genug als Arbeitsbefund, aber nicht als endgültige Aussage über alle möglichen PAXG-1h-Phasen.
