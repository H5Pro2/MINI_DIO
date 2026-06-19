# Lokale Rekopplungspole - Befund

Stand: 2026-06-19

## Zweck

Diese Notiz bewertet lokale Stresssegmente gegen lokale Ruhe-/Entlastungssegmente.

Die Frage war:

Treten `last_memory_bindend` und `reiz_aktiv_rekoppelnd` als lokale MCM-Gegenpole auf?

## Hierarchie der Pruefung

1. Grundfrage: Gibt es lokale Rekopplungspole?
2. Unterpruefung: Stresssegmente gegen Quiet-Segmente vergleichen.
3. Folgeschritt: Falls ja, lokale Rekopplungspole als passive MCM-Landkarte weiter pruefen.

## Ergebnis

Die lokalen Gegenpole sind deutlich sichtbar, aber nicht absolut.

Rollenverteilung:

| Gruppe | Rolle | Anzahl |
|---|---|---:|
| Ruhe | `reiz_aktiv_rekoppelnd` | 5 |
| Stress | `uebergang_bindend` | 4 |
| Stress | `last_memory_bindend` | 2 |
| Stress | `reiz_aktiv_rekoppelnd` | 1 |

Das bedeutet:

Alle Ruhe-/Entlastungssegmente wurden aktiv-rekoppelnd gelesen.

Die meisten Stresssegmente wurden bindungsnah gelesen.

Ein Stresssegment blieb aktiv-rekoppelnd.

Damit ist es kein Dogma und keine harte Regel.

Es ist aber ein klarer passiver Feldbefund.

## Gruppenvergleich

| Gruppe | Kontrast Bindung-Aktiv | Feldlast |
|---|---:|---:|
| Stress | `-0.0681` | `0.1938` |
| Ruhe | `-0.5462` | `0.0149` |

Lesart:

Der Kontrast bleibt bei beiden Gruppen im Mittel noch aktiv-rekoppelnd, aber Stress liegt deutlich naeher an Bindung.

Die Feldlast trennt die Gruppen stark:

```text
Stress-Feldlast: 0.1938
Ruhe-Feldlast:   0.0149
```

Das ist der staerkste Unterschied.

## Staerkste Bindung

Die klarsten bindenden lokalen Abschnitte:

| Welt | Rolle | Kontrast | Feldlast | Memorylast | Rekopplung |
|---|---|---:|---:|---:|---:|
| STRESS_2023_TEST4 | `last_memory_bindend` | `0.1294` | `0.2660` | `0.2447` | `0.596927` |
| STRESS_2025_STRESS | `last_memory_bindend` | `0.1203` | `0.2872` | `0.2234` | `0.594327` |
| STRESS_2024_REAL | `uebergang_bindend` | `0.0322` | `0.2340` | `0.2447` | `0.601652` |

Diese Abschnitte zeigen:

Feldlast und Memorylast koennen aktive Rekopplung ueberholen.

Das ist der lokale Lastpol.

## Staerkste aktive Rekopplung

Die klarsten aktiv-rekoppelnden lokalen Abschnitte:

| Welt | Gruppe | Rolle | Aktiv | Bindung |
|---|---|---|---:|---:|
| QUIET_2024_SIDEWAYS | Ruhe | `reiz_aktiv_rekoppelnd` | `0.7552` | `0.2023` |
| QUIET_2026_ANCHOR | Ruhe | `reiz_aktiv_rekoppelnd` | `0.7239` | `0.1409` |
| QUIET_2025_STRESS | Ruhe | `reiz_aktiv_rekoppelnd` | `0.7069` | `0.0940` |
| STRESS_2024_SIDEWAYS | Stress | `reiz_aktiv_rekoppelnd` | `0.6443` | `0.1773` |

Wichtig:

Auch ein Stresssegment kann aktiv-rekoppelnd bleiben.

Das spricht gegen eine mechanische Gleichung:

```text
Stresssegment = Lastbindung
```

Die bessere Lesung ist:

```text
Stresssegment erhoeht die Wahrscheinlichkeit von Bindung,
aber Rekopplung kann trotzdem tragen.
```

## MCM-Deutung

Der Befund passt zu einer organischen MCM-Landkarte:

```text
Ruhe / Entlastung
  -> hohe aktive Rekopplung
  -> niedrige Feldlast
  -> niedrige Memorylast

Stress / lokale Verdichtung
  -> erhoehte Feldlast
  -> erhoehte Memorylast
  -> Uebergang oder Lastbindung
```

Der relevante Punkt ist nicht der Name der Welt.

Der relevante Punkt ist:

```text
Wie stark bleibt die Weltwirkung im Feld gebunden?
```

## Bedeutung fuer MINI_DIO

MINI_DIO bekommt damit eine sinnvollere passive Innenfeld-Lesung:

- Nicht jede Unruhe ist Belastung.
- Nicht jede Ruhe ist leer.
- Nicht jeder Stress bindet.
- Aber lokale Stressverdichtung kann Feld und Memory deutlich naeher an Bindung bringen.

Das ist organischer als ein starrer Filter.

Es ist eine passive Landkarte:

```text
reiz_aktiv_rekoppelnd
  <-> uebergang_bindend
  <-> last_memory_bindend
```

## Forschungsstand

Umgesetzt als Diagnose:

- `tools/report_local_recoupling_poles.py`
- `docs/befunde/214_LOKALE_REKOPPLUNGSPOLE_DIAGNOSE.md`
- `docs/befunde/214_LOKALE_REKOPPLUNGSPOLE_DIAGNOSE.csv`

Der Befund liegt hier:

- `docs/befunde/215_LOKALE_REKOPPLUNGSPOLE_BEFUND.md`

## Wie es weitergeht

Als naechstes sollte die lokale Rekopplungslandkarte mit Rohweltmerkmalen verbunden werden.

Grundfrage:

Welche Weltmerkmale erzeugen den Uebergang von aktiv-rekoppelnd zu bindend?

Konkrete Unterpruefung:

1. lokale Segmente nach Bewegungsrichtung, Range, Volumenrhythmus und Richtungswechsel lesen,
2. diese Merkmale gegen Feldlast, Memorylast und Rekopplung legen,
3. pruefen, ob der Uebergang durch Weltstruktur, durch Nachhall oder durch Feldzustand entsteht.

Erst danach waere sinnvoll, ueber eine passive Rekopplungs-Vorstufe im Mini-DIO-Kern nachzudenken.
