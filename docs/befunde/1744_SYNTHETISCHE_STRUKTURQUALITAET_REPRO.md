# 1744 - Synthetische Strukturqualität Repro

## Zweck

Diese Prüfung wiederholt die drei synthetischen Strukturqualitäten mit frischer Memory:

- ruhige Driftwelt,
- Bruch-/Randwelt,
- kontrollierte Expansionswelt.

Ziel ist nicht, eine universelle MCM-Regel zu beweisen. Ziel ist zu prüfen, ob MINI_DIO bei gleicher Welt und neuem Speicher dieselbe passive Topologie und dieselben lokalen Druckprofile erneut bildet.

## Ergebnis

Die Repro-Prüfung ist in den gemessenen Werten exakt deckungsgleich mit dem jeweiligen Ursprungslauf.

| Welt | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ruhe Orig | 994 | 1.0000 | 0.0000 | 0.0000 | 0.7570 | 0.6156 | 0.1182 | 0.9189 |
| Ruhe Repro | 994 | 1.0000 | 0.0000 | 0.0000 | 0.7570 | 0.6156 | 0.1182 | 0.9189 |
| Bruch/Rand Orig | 7994 | 0.9994 | 0.0006 | 0.0000 | 0.7507 | 0.6069 | 0.1251 | 0.9090 |
| Bruch/Rand Repro | 7994 | 0.9994 | 0.0006 | 0.0000 | 0.7507 | 0.6069 | 0.1251 | 0.9090 |
| Expansion Orig | 9994 | 0.9859 | 0.0141 | 0.0000 | 0.7079 | 0.5537 | 0.1704 | 0.8407 |
| Expansion Repro | 9994 | 0.9859 | 0.0141 | 0.0000 | 0.7079 | 0.5537 | 0.1704 | 0.8407 |

Auch die relative Randdruck-Lupe reproduziert die Profile exakt:

| Welt | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ruhe Orig | 0.3994 | 0.1509 | 0.2706 | 0.1791 | 0.1182 | 0.0164 | 0.0844 | 0.0053 |
| Ruhe Repro | 0.3994 | 0.1509 | 0.2706 | 0.1791 | 0.1182 | 0.0164 | 0.0844 | 0.0053 |
| Bruch/Rand Orig | 0.4567 | 0.0997 | 0.3914 | 0.0522 | 0.1251 | 0.0255 | 0.1065 | 0.0147 |
| Bruch/Rand Repro | 0.4567 | 0.0997 | 0.3914 | 0.0522 | 0.1251 | 0.0255 | 0.1065 | 0.0147 |
| Expansion Orig | 0.4260 | 0.1328 | 0.3387 | 0.1026 | 0.1704 | 0.1043 | 0.1842 | 0.1005 |
| Expansion Repro | 0.4260 | 0.1328 | 0.3387 | 0.1026 | 0.1704 | 0.1043 | 0.1842 | 0.1005 |

## Lesart

Der Befund spricht dafür, dass die synthetischen Weltqualitäten nicht nur zufällig gelesen wurden. Bei gleicher Welt und frischem Speicher entstehen dieselbe zentrumsnahe Grundtopologie und dieselben lokalen Druckprofile erneut.

Damit wird die bisherige Trennung gestützt:

```text
globale Feldordnung = zentrumsnahe Rekopplung
lokale Weltfärbung  = Ruhe, Bruch/Rand, Expansion
```

Wichtig bleibt die Grenze: Die Reproduzierbarkeit gilt für diese geprüften Welten, diese Aufnahme und diese Diagnose. Sie ist kein Beweis einer universellen MCM-Topologie, aber ein stärkerer methodischer Hinweis als ein einzelner Lauf.

## Zugehörige Reports

- [synthetische_strukturqualitaet_repro_topology.md](../../reports/synthetische_strukturqualitaet_repro_topology.md)
- [synthetische_strukturqualitaet_repro_randdruck.md](../../reports/synthetische_strukturqualitaet_repro_randdruck.md)

## Wie es weitergeht

Als nächstes sollte die gleiche Repro-Logik auf reale Fenster mit stärkerer Milieudrift gelegt werden. Entscheidend ist, ob dort ebenfalls gleiche Rollenkerne wiederkehren oder ob die lokale Weltfärbung mehr Varianz erzeugt.
