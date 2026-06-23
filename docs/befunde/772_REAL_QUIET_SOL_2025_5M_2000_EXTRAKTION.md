# REAL Quiet SOL 2025 5m 2000 - Extraktion

Stand: 2026-06-23

## Zweck

Diese Notiz dokumentiert das ruhige Gegenfenster zur realen Sequenzbruch-Gegenprobe.

Beide Fenster stammen aus derselben Quelle:

```text
data/1-12_2025_5m_SOLUSDT.csv
```

Ziel ist kein Assetvergleich, sondern ein Innenweltvergleich innerhalb derselben Aussenwelt:

```text
belasteter Sequenzbruch
gegen
rohweltlich ruhigeres Fenster
```

## Quelle

- Quelle: `data/1-12_2025_5m_SOLUSDT.csv`
- Auszug: `data/kontrolliert_real_quiet_sol_2025_5m_2000.csv`
- Fensterlaenge: `2000`
- Suchschritt: `250`
- ausgewaehlter Startindex: `52250`
- ausgewaehlter Endindex: `54250`

## Rohweltliche Eigenschaften

Das ausgewaehlte Fenster traegt:

```text
avg_abs_return:    0.0011519001
max_abs_return:    0.0086968156
avg_range:         0.0021470605
return_volatility: 0.0015808389
drift:             0.0061765693
max_drawdown:      0.0694488895
direction_changes: 944
quiet_score:       0.5367880055
```

Verglichen mit dem realen Bruchfenster ist diese Welt rohweltlich ruhiger:

- deutlich geringere maximale Einzelbewegung,
- deutlich geringerer Drawdown,
- fast neutraler Drift,
- niedrigere Volatilitaet,
- niedrigere durchschnittliche Range.

## Bedeutung fuer die Gegenprobe

Diese Welt prueft eine wichtige Grenze:

```text
Ist ruhige Aussenwelt automatisch ruhige Innenfeldwirkung?
```

Die Antwort muss aus der Feldreaktion gelesen werden, nicht aus der Rohwelt allein.

## Artefakt

Der maschinenlesbare Extraktionsbericht liegt unter:

```text
docs/befunde/772_REAL_QUIET_SOL_2025_5M_2000_EXTRACT_REPORT.json
```

## Wie es weitergeht

Diese ruhige Welt wird gegen Forschungskette, Rezeptorachsen, Topologie und Kurzsegment-Feldwirkung gelesen und anschliessend direkt gegen das reale Bruchfenster verglichen.
