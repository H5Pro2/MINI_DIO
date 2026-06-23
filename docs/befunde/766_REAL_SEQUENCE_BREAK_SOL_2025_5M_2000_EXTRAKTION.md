# REAL Sequence Break SOL 2025 5m 2000 - Extraktion

Stand: 2026-06-22

## Zweck

Diese Notiz dokumentiert die reale Sequenzbruch-Gegenprobe.

Im Gegensatz zu den synthetischen Phasenwelten wurde hier keine kuenstliche Phasenfolge gesetzt.
Es wurde ein echtes 5m-Fenster aus SOL 2025 gesucht, das rohweltlich hohe Belastung traegt.

## Quelle

- Quelle: `data/1-12_2025_5m_SOLUSDT.csv`
- Auszug: `data/kontrolliert_real_sequence_break_sol_2025_5m_2000.csv`
- Fensterlaenge: `2000`
- Suchschritt: `250`
- ausgewaehlter Startindex: `80250`
- ausgewaehlter Endindex: `82250`

## Rohweltliche Eigenschaften

Das gewaehlt Fenster traegt:

```text
avg_abs_return:    0.0022839595
max_abs_return:    0.1056061117
avg_range:         0.0044585481
return_volatility: 0.0045048843
drift:            -0.1703643999
max_drawdown:      0.2716080614
direction_changes: 1005
stress_score:      1.8612105930
```

Damit ist es ein realer belasteter Weltabschnitt mit:

- negativem Drift,
- hoher maximaler Einzelbewegung,
- deutlichem Drawdown,
- vielen Richtungswechseln,
- hoher lokaler Weltspannung.

## Bedeutung fuer die Gegenprobe

Diese Welt ist fachlich geeignet, um die synthetischen Nachhall-/Topologie-Befunde gegen eine echte Sequenz zu pruefen.

Die Frage lautet:

```text
Bleibt die MCM-Topologie auch dann lesbar,
wenn Bruch, Druck, Richtungswechsel und Rekopplung nicht kuenstlich gesetzt,
sondern real aus der Weltsequenz kommen?
```

## Artefakt

Der maschinenlesbare Extraktionsbericht liegt unter:

```text
docs/befunde/766_REAL_SEQUENCE_BREAK_SOL_2025_5M_2000_EXTRACT_REPORT.json
```

## Wie es weitergeht

Diese extrahierte Welt wird in der passiven Forschungskette gelesen und anschliessend gegen Rezeptorachsen, Topologie und Kurzsegment-Feldwirkung ausgewertet.
