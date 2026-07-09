# 013 - Passive Feldphasen-Signatur-Memory

Stand: 2026-07-09

## Zweck

Diese Mechanik speichert wiederkehrende Feldphasenqualität.

Sie entstand aus Befund 2012:

```text
Eine positive Feldphase kann in unterschiedlichen Welten wieder auftauchen,
auch wenn nicht dieselben alten Symbolnamen reifen.
```

Damit trennt MINI_DIO:

```text
Symbolbindung:
Welche konkrete Rolle wird wieder berührt?

Feldphasenbindung:
Welche innere Qualität kehrt wieder?
```

## Speicherort

Die Memory liegt in:

```text
passive_mcm_field_phase_signature_memory
```

Code:

```text
mini_dio/mcm_field_phase_signature_memory.py
```

## Was gespeichert wird

Pro Preview-Symbol werden passiv gespeichert:

```text
Trägerrolle
Weltbindung
Feldfunktion
Feldvariante
Weltzählung
Effektzählung
Familienzählung
Qualitätsvektor
Drift
Tiefe
Zustand der Feldphase
```

Der Qualitätsvektor enthält:

```text
carry
strain
rekopplung
sensory
visual_gap
hearing_gap
coherence
tension
asymmetry
```

## Zustände

Die aktuelle Lesung unterscheidet passiv:

```text
young_field_phase
stable_crossworld_field_phase
drifting_field_phase
positive_recoupling_field_phase
```

Diese Zustände sind Diagnose- und Memory-Zustände.

Sie sind keine Handlung, keine Richtung und kein Gate.

## Warum das wichtig ist

Vorher konnte MINI_DIO gut lesen:

```text
Dieses Preview-Symbol taucht wieder auf.
```

Mit dieser Erweiterung kann MINI_DIO zusätzlich passiv speichern:

```text
Diese Feldqualität taucht wieder auf,
auch wenn sie durch andere Trägerrollen erscheint.
```

Das ist ein Schritt weg von reiner Symbolzählung und hin zu Feldphasen-Gedächtnis.

## Grenze

Diese Mechanik beeinflusst keine Handlung.

Sie ist nicht dafür da, Einträge, Richtung oder Verhalten zu erzwingen.

Sie dient nur dazu, organische Feldentwicklung messbar zu machen:

```text
Was bleibt ähnlich?
Was driftet?
Welche Welt bindet die Qualität?
Welche Trägerrollen nehmen dieselbe Qualität auf?
```

## Wie es weitergeht

Als nächstes sollte diese Memory über mehrere bestehende Weltketten gelesen werden.

Entscheidend ist:

```text
Werden Feldphasen stabiler?
Driften sie kontrolliert?
Entstehen weltübergreifende Qualitätsfamilien?
Bleibt die Topologie trotz neuer Tiefe erhalten?
```
