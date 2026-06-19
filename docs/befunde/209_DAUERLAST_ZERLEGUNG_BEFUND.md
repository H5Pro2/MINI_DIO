# Dauerlast-Zerlegung - Befund

Stand: 2026-06-19

## Zweck

Diese Notiz beantwortet die Frage, woher Dauerlast in den aktuellen MINI_DIO-Welten kommt.

Sie baut auf der organischen Reizadaptation auf und trennt:

- sensorische Last,
- Nachhall,
- Aufmerksamkeit,
- Adaptionskapazitaet,
- Distanzbedarf,
- Feldlast,
- Memorylast,
- Rekopplungsverlust.

## Hierarchie der Pruefung

1. Grundfrage: Ist Dauerlast eine Sensorikfrage, eine Distanzierungsfrage oder eine MCM-Feldfrage?
2. Unterpruefung: Welche Lastanteile dominieren bei BTC und SOL?
3. Folgeschritt: Entscheiden, ob MINI_DIO eher einen Reizfilter, eine Distanzierungsdiagnose oder eine Feld-Rekopplungsdiagnose braucht.

## Kernergebnis

Dauerlast entsteht in den bisherigen Daten nicht einfach aus einem lauten Einzelreiz.

Der staerkste Befund ist:

```text
SOL 30m / 1h -> hohe Feldlast + hohe Memorylast + Rekopplungsverlust
BTC 5m       -> hohe Aufmerksamkeit / Nachhallnaehe, aber geringe Feldlast
```

Damit ist die Dauerlast bei SOL 1h eher eine MCM-Feld- und Memory-Kopplung als eine reine Sensorik-Uebersteuerung.

## Staerkste Dauerlast

| Welt | Dauerlast | Feldlast | Memorylast | Rekopplungsverlust | Nachhall |
|---|---:|---:|---:|---:|---:|
| SOL 2024 1h | `0.2213` | `0.3159` | `0.3225` | `0.0530` | `0.1614` |
| SOL 2025 1h | `0.2084` | `0.2944` | `0.2964` | `0.0509` | `0.1707` |
| SOL 2025 30m | `0.1530` | `0.2016` | `0.2177` | `0.0391` | `0.1573` |
| SOL 2024 30m | `0.1477` | `0.1830` | `0.2212` | `0.0398` | `0.1565` |

## Distanzierungsfrage

Die Distanzierungsfrage ist berechtigt, aber anders als zuerst vermutet.

BTC 5m zeigt die groesste Distanzluecke:

| Welt | Distanzluecke | Distanzbedarf | Adaptionskapazitaet | Feldlast |
|---|---:|---:|---:|---:|
| BTC 2025 5m | `0.1117` | `0.6948` | `0.5831` | `0.0221` |
| BTC 2024 5m | `0.0565` | `0.6674` | `0.6109` | `0.0211` |

Aber:

Diese Welten erzeugen kaum Feldlast.

Das bedeutet:

Akute Aufmerksamkeit oder Distanzbedarf ist nicht automatisch MCM-Dauerlast.

## Interpretation

### 1. BTC 5m ist reiznah, aber nicht feldlastnah

BTC 5m erzeugt:

- hohe Aufmerksamkeit,
- hohen Nachhall,
- sichtbare Distanzluecke,
- aber niedrige Feldlast,
- niedrige Memorylast,
- sehr geringe Rekopplungsverluste.

Deutung:

Das Feld sieht und hoert aktiv, wird aber nicht dauerhaft besetzt.

### 2. SOL 1h ist feldlastnah

SOL 1h erzeugt:

- hohe Feldlast,
- hohe Memorylast,
- den groessten Rekopplungsverlust,
- aber keine dominante Distanzluecke.

Deutung:

Das Problem ist nicht nur:

```text
Ich brauche Abstand.
```

Sondern eher:

```text
Diese Weltlage wird in meinem Feld schwerer rekoppelt und schreibt mehr belastete Episodenspuren.
```

### 3. Dauerlast ist ein Kopplungsproblem

Dauerlast entsteht, wenn drei Dinge zusammenkommen:

1. Feld bleibt haeufig strained.
2. Episodenmemory steigt.
3. Rekopplung sinkt.

Sensorik und Nachhall wirken mit, sind aber nicht der alleinige Ursprung.

## MCM-Deutung

Fachlich ist das wichtig:

Ein organisches MCM-System braucht nicht nur Reizfilterung.

Es braucht eine passive Lesung von:

```text
Weltreiz
  -> sensorische Vorform
  -> MCM-Feldwirkung
  -> Episodenspur
  -> Rekopplung oder Lastbindung
```

Die Frage ist also nicht nur:

```text
Wie laut ist die Welt?
```

Sondern:

```text
Wie tief schreibt sich diese Welt in mein Feld ein?
Wie gut kann ich danach rekoppeln?
Bleibt daraus eine tragende oder belastete Spur?
```

## Bedeutung fuer MINI_DIO

MINI_DIO sollte Dauerlast nicht als einfache Ueberreizung interpretieren.

Die bessere Richtung ist:

- Sensorik normalisieren,
- Nachhall lesen,
- Feldlast getrennt lesen,
- Memorylast getrennt lesen,
- Rekopplungsverlust getrennt lesen,
- erst danach entscheiden, ob Distanzierung ueberhaupt der passende Begriff ist.

Damit bleibt das System organischer.

Es wird nicht mechanisch:

```text
laut -> Abstand
```

Sondern:

```text
laut, aber tragbar
leise, aber belastend
aufmerksamkeitsnah, aber rekoppelnd
dauerlastnah, weil Memory und Feld nicht sauber loesen
```

## Forschungsstand

Umgesetzt als passive Diagnose:

- `tools/report_duration_load_decomposition.py`
- `docs/befunde/208_DAUERLAST_ZERLEGUNG_DIAGNOSE.md`

Noch nicht in den Kern eingebaut.

Das ist richtig so.

Die Diagnose zeigt erst, welche Lastquelle wirklich relevant ist.

## Wie es weitergeht

Als naechstes sollte die Rekopplungsqualitaet genauer untersucht werden.

Grundfrage:

Warum kann BTC 5m trotz hoher Aufmerksamkeit gut rekoppeln, waehrend SOL 1h staerker in Feld- und Memorylast geht?

Konkrete Unterpruefung:

1. Welche Welten verlieren Rekopplung trotz moderater Sensorik?
2. Welche Welten bleiben rekoppelnd trotz hoher Aufmerksamkeit?
3. Gibt es eine passive Feldsignatur fuer `last_bindend` gegen `reiz_aktiv_rekoppelnd`?

Erst danach ist sinnvoll zu entscheiden, ob eine organische Distanzierungs-Vorstufe in den MINI_DIO-Kern gehoert.
