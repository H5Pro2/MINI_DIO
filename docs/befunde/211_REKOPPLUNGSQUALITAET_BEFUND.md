# Rekopplungsqualitaet - Befund

Stand: 2026-06-19

## Zweck

Diese Notiz fasst die passive Rekopplungsdiagnose zusammen.

Ausgangspunkt war der Befund der Dauerlast-Zerlegung:

SOL 30m / 1h wird nicht vor allem durch akute Sensorik schwer, sondern durch Feldlast, Memorylast und Rekopplungsverlust.

## Hierarchie der Pruefung

1. Grundfrage: Warum rekoppeln manche Welten besser als andere?
2. Unterpruefung: Welche passiven Rollen entstehen aus Reizaktivitaet, Nachhall, Lastbindung und Memorybindung?
3. Folgeschritt: Pruefen, ob diese Rollen ueber weitere Welten stabil bleiben.

## Ergebnis

Die Rekopplungsdiagnose zeigt vier passive Rollen:

| Rolle | Bedeutung |
|---|---|
| `reiz_aktiv_rekoppelnd` | Reiz ist aktiv, aber das Feld kommt gut zurueck. |
| `nachhall_rekoppelnd` | Nachhall bleibt sichtbar, aber Rekopplung traegt noch. |
| `uebergang_bindend` | Bindung steigt, aber aktive Rekopplung ist noch nicht gebrochen. |
| `last_memory_bindend` | Feldlast und Memorylast ueberholen die aktive Rekopplung. |

Diese Rollen sind Diagnosebegriffe.

Sie sind keine Runtime-Regeln.

## Rollenverteilung

In der BTC/SOL-Zeitauflosungspruefung entsteht:

- `reiz_aktiv_rekoppelnd`: 4 Welten
- `nachhall_rekoppelnd`: 8 Welten
- `uebergang_bindend`: 2 Welten
- `last_memory_bindend`: 2 Welten

## Wichtigste Beobachtung

Die Rollen bilden eine nachvollziehbare Ordnung:

```text
5m        -> reiz_aktiv_rekoppelnd
15m/30m   -> nachhall_rekoppelnd oder uebergang_bindend
SOL 1h    -> last_memory_bindend
```

Das ist fachlich relevant.

Es zeigt keine simple Lautstaerkeregel, sondern eine passive Feldentwicklung:

Aktiver Reiz kann rekoppeln.

Nachhall kann tragbar bleiben.

Verdichtung kann in Bindung kippen.

Memory kann Weltwirkung im Feld halten.

## BTC gegen SOL

### BTC

BTC bleibt ueberwiegend rekoppelnd.

BTC 5m ist aktiv-rekoppelnd:

- hohe Aufmerksamkeit,
- starke Rekopplung,
- geringe Feldlast,
- geringe Memorylast.

BTC 15m / 30m / 1h driftet eher in `nachhall_rekoppelnd`.

Das bedeutet:

Die Welt hinterlaesst Spuren, aber diese Spuren bleiben noch loesbar.

### SOL

SOL zeigt eine deutlich haertere Verdichtungsrampe.

SOL 5m bleibt noch aktiv-rekoppelnd.

SOL 30m wird `uebergang_bindend`.

SOL 1h wird `last_memory_bindend`.

Das bedeutet:

Die Weltspannung schreibt sich tiefer ins Feld ein.

Rekopplung bleibt vorhanden, wird aber von Feldlast und Memorylast ueberholt.

## MCM-Deutung

Rekopplung ist nicht nur ein Wert.

Sie beschreibt, ob eine Weltwirkung wieder vom Feld geloest und neu getragen werden kann.

Die aktuelle Diagnose legt nahe:

```text
reiz_aktiv_rekoppelnd
  -> Welt wirkt, Feld bleibt beweglich

nachhall_rekoppelnd
  -> Welt bleibt als Spur, Feld kann noch loesen

uebergang_bindend
  -> Spur und Last naehern sich einer Bindung

last_memory_bindend
  -> Weltwirkung bleibt im Feld und im Memory haften
```

Damit wird Rekopplung zu einer zentralen MCM-Feldeigenschaft.

Nicht die Reizstaerke allein entscheidet.

Entscheidend ist:

```text
Kann das Feld nach Weltkontakt wieder in tragbare Ordnung zurueckfinden?
```

## Bedeutung fuer MINI_DIO

MINI_DIO sollte nicht zuerst eine Distanzierungsmechanik bekommen.

Der naechste saubere Schritt ist eine passive Rekopplungslandkarte.

Diese Landkarte unterscheidet:

- aktive, aber loesbare Welt,
- nachhallende, aber tragbare Welt,
- uebergangshaft bindende Welt,
- last-/memorybindende Welt.

Das hilft spaeter, ohne harte Regeln zu erkennen:

Welche Weltlagen sind nur aktiv?

Welche Weltlagen schreiben sich in das Feld ein?

Welche Weltlagen erzeugen Bedeutung, aber bleiben loesbar?

Welche Weltlagen erzeugen belastete Bindung?

## Forschungsstand

Umgesetzt als passive Diagnose:

- `tools/report_recoupling_quality.py`
- `docs/befunde/210_REKOPPLUNGSQUALITAET_DIAGNOSE.md`

Der Befund liegt hier:

- `docs/befunde/211_REKOPPLUNGSQUALITAET_BEFUND.md`

## Wie es weitergeht

Als naechstes sollte diese Rollenkarte gegen weitere Welten laufen.

Grundfrage:

Bleibt die Reihenfolge stabil?

```text
reiz_aktiv_rekoppelnd
nachhall_rekoppelnd
uebergang_bindend
last_memory_bindend
```

Konkrete Unterpruefung:

1. Drittes Asset pruefen.
2. Ruhige Seitwaertswelt pruefen.
3. Harte Expansionswelt pruefen.
4. Negative Stresswelt pruefen.

Wenn die Rollen dort wieder sinnvoll entstehen, ist das ein belastbarer Hinweis auf eine passive Rekopplungsordnung im MCM-Feld.
