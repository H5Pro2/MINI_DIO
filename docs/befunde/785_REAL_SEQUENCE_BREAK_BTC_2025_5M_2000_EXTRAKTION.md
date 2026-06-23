# REAL Sequence Break BTC 2025 5m 2000 - Extraktion

Stand: 2026-06-23

## Zweck

Diese Notiz dokumentiert die reale BTC-2025-Sequenzbruch-Gegenprobe.

Nach der BTC-Feldruhe-Auswahl wird ein rohweltlich belastetes Fenster aus derselben Quelle extrahiert.
Damit kann MINI_DIO nicht nur auf ruhige Kandidaten, sondern auf echte Bruch-/Stressabschnitte geprueft werden.

## Quelle

- Quelle: `data/1-12_2025_5m_BTCUSDT.csv`
- Auszug: `data/kontrolliert_real_sequence_break_btc_2025_5m_2000.csv`
- Fensterlaenge: `2000`
- Suchschritt: `250`
- ausgewaehlter Startindex: `80500`
- ausgewaehlter Endindex: `82500`

## Rohweltliche Eigenschaften

Das gewaehlte Fenster traegt:

```text
avg_abs_return:    0.0011318507
max_abs_return:    0.0733815789
avg_range:         0.0020891296
return_volatility: 0.0025655155
drift:            -0.1109178122
max_drawdown:      0.1677102648
direction_changes: 1012
stress_score:      1.2819497288
```

Damit ist es ein real belasteter BTC-Weltabschnitt mit:

- negativem Drift,
- deutlichem Drawdown,
- hoher maximaler Einzelbewegung,
- vielen Richtungswechseln,
- erhoehter lokaler Weltspannung.

## Bedeutung fuer die Gegenprobe

Die Frage lautet:

```text
Bleibt die MCM-Topologie auch bei BTC unter realem Bruchdruck lesbar,
oder bildet sich eine deutlich andere Rollenordnung als im feldruhigen BTC-Kandidaten?
```

## Artefakt

Der maschinenlesbare Extraktionsbericht liegt unter:

```text
docs/befunde/785_REAL_SEQUENCE_BREAK_BTC_2025_5M_2000_EXTRACT_REPORT.json
```

## Wie es weitergeht

Diese extrahierte Welt wird in der passiven Forschungskette gelesen und danach direkt gegen den BTC-Feldruhe-Kandidaten verglichen.
