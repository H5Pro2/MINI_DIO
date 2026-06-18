# Feldklassen-Refinement Methodik

Stand: 2026-06-18

## Zweck

Diese Datei dokumentiert die Verfeinerung der passiven Feldklassen-Diagnose.

Ausloeser war die 2k-Skalierung der negativen Welt.

Die alte Diagnose wertete hohe Episodenmemory-Zahl zu schnell als Stress-Gegenpol.

Das war methodisch ungenau.

## Anpassung

Die Diagnose beruecksichtigt jetzt zusaetzlich:

```text
field_carried
field_strained
field_carried_ratio
field_strained_ratio
relative Spannungs-/Kippwirkung
dominante Feldwirkung
Rekopplung
Tragqualitaet
```

Damit wird unterschieden zwischen:

```text
belastendem Memorydruck
und
tragender Bedeutungsverdichtung
```

## Neuer Befund Nach Refinement

| Welt | Alte Tendenz | Neue Klasse | Begruendung |
|---|---|---|---|
| negative_moderate_1k | ruhige Naehegruppe | ruhige Naehegruppe | hohe Rekopplung, hohe Tragqualitaet, field_carried 0.9738 |
| negative_moderate_2k | faelschlich Stress-Gegenpol | ruhige Naehegruppe | Memory steigt, aber Feld bleibt getragen: field_carried 0.9664 |
| sideways_2026_1k | Stress-Gegenpol | Stress-Gegenpol | geringe Rekopplung, geringere Tragqualitaet, field_carried 0.9135 |
| sideways_2026_2k | Stress-Gegenpol | angespannte Uebergangsgruppe | Feld bleibt unruhig, aber carried steigt auf 0.9398 |

## Bedeutung

Diese Anpassung ist keine Aenderung an MINI_DIO.

Sie betrifft nur die passive Leseschicht.

Fachlich bedeutet das:

```text
Das MCM-Feld darf nicht nach einem Einzelwert gelesen werden.
Eine Innenfeldklasse entsteht aus Relationen.
```

Wichtige Relation:

```text
Memory + hohe Tragung = Bedeutungsverdichtung
Memory + geringe Tragung = Belastungsdruck
```

## Forschungswert

Das verbessert die wissenschaftliche Lesbarkeit.

Vorher konnte laengere Weltzeit faelschlich als Stress erscheinen.

Jetzt wird klarer:

```text
Laengere Weltzeit kann Bedeutung verdichten,
ohne dass das Feld kollabiert.
```

Das passt zur bisherigen MINI_DIO-Beobachtung:

```text
Das Feld organisiert nicht nur Werte.
Es bildet getragene Bedeutungsraeume.
```

## Wie Es Weitergeht

Als naechstes sollten bestehende Mehrweltberichte mit dem verfeinerten Klassifikator neu erzeugt werden.

Hierarchie:

1. Grundfrage: Verschiebt die bessere Leseschicht die bisherige MCM-Topologie?
2. Unterpruefung: Welche Welten wechseln Klasse, welche bleiben stabil?
3. Folgeschritt: Danach wird entschieden, ob die Topologie-Dateien aktualisiert werden muessen.
