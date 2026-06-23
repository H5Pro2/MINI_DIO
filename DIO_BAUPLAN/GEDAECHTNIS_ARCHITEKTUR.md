# MINI_DIO Gedächtnisarchitektur

Stand: 2026-06-23

## Zweck

Diese Datei beschreibt die Zielstruktur der MINI_DIO-Gedächtnismechanik.

MINI_DIO soll seine Welt nicht als Rohdatenstapel speichern, sondern als geordnete Innenfeld-Erfahrung:

```text
Sinneskontakt
  -> Wahrnehmungs-/Primingspur
  -> MCM-Feldwirkung
  -> Episode
  -> semantische Verdichtung
```

Die vier Gedächtnisschichten bleiben getrennt. Sie dürfen sich gegenseitig erklären, aber nicht ineinanderfallen.

## 1. Wahrnehmungsgedächtnis / Priming

Funktion:

```text
Was ist mir wieder begegnet?
Was hallt nach?
Welche Sinnesaufnahme beeinflusst die nächste Wahrnehmung?
```

Diese Schicht merkt keine Bedeutung im endgültigen Sinn.
Sie hält Wiederkehr, Nachhall, Nähe, Abstand, sensorische Aufnahmequalität und zeitliche Wiederbegegnung.

Aktueller Codebezug:

- `mini_dio/temporal_memory.py`
- `mini_dio/sensory_intake_memory.py`
- `visual_memory_recall` in `mini_dio/mini_world.py`

Soll-Struktur:

```text
perception_memory.py
  - Sinneswiederkehr
  - Nachhall / Afterimage
  - Priming
  - Rezeptoraufnahme über Zeit
  - Nähe/Distanz zu bereits gelesenen Formen
```

Grenze:

Diese Schicht darf keine Handlung ableiten.
Sie darf nur sagen:

```text
Diese Wahrnehmung ist nah, neu, wiederkehrend, nachhallend oder driftend.
```

## 2. Emotionales / MCM-Feldgedächtnis

Funktion:

```text
Was hat diese Weltlage mit meinem MCM-Feld gemacht?
```

Hier geht es nicht um menschliche Emotionen als Sprache, sondern um MCM-Feldwirkung:

- getragen,
- unruhig,
- kippend,
- angespannt,
- rekoppelnd,
- randnah,
- zentrumsnah,
- offen.

Aktueller Codebezug:

- `mini_dio/episode_memory.py`
- `mini_dio/mcm_effect_map.py`
- `mini_dio/mcm_field_movement_memory.py`
- `mcm_field_episode_memory` in `mini_dio/semantic_memory.py`

Soll-Struktur:

```text
mcm_field_memory.py
  - MCM-Feldepisoden
  - Feldwirkungsklassen
  - Rekopplung / Carry / Strain
  - Zentrum / Offenheit / Randnähe
  - Feldbewegung und Feldqualität
```

Grenze:

Diese Schicht ist keine Strategie.
Sie sagt nicht:

```text
Jetzt handeln.
```

Sie sagt:

```text
Diese Lage wirkt im Feld tragend, offen, belastet, kippnah oder rekoppelnd.
```

## 3. Episodisches Gedächtnis

Funktion:

```text
Welche konkrete Welt-/Feldphase habe ich erlebt?
Wie lange dauerte sie?
Was kam davor und danach?
Welche Feldfamilie war dominant?
```

Diese Schicht speichert zusammenhängende Erlebnisabschnitte.

Aktueller Codebezug:

- `mini_dio/episode_memory.py`
- `store_episode_memory()` in `mini_dio/semantic_memory.py`
- `store_mcm_field_episode_memory()` in `mini_dio/semantic_memory.py`

Soll-Struktur:

```text
episode_store.py
  - passive Episoden
  - Übergänge
  - Dauer
  - dominante Symbolfamilien
  - MCM-Feldwirkung pro Episode
```

Grenze:

Eine Episode ist nicht automatisch Bedeutung.
Sie ist zuerst:

```text
ein gelebter Abschnitt im Innenfeld.
```

## 4. Semantische Bedeutungsverdichtung

Funktion:

```text
Welche wiederkehrenden Episoden/Feldwirkungen bilden eine eigene DIO-Bedeutung?
```

Diese Schicht verdichtet Wiederkehr zu eigener Syntax:

- `dio_*`-Symbole,
- Symbolfamilien,
- Bedeutungsinseln,
- wiederkehrende Feldqualitäten,
- lesbare Innenfeldbedeutungen.

Aktueller Codebezug:

- `mini_dio/semantic_memory.py`
- `make_syntax_symbol()`
- `make_mcm_field_episode_symbol()`
- `build_passive_inner_effect_meaning_notes()` in `mini_dio/mcm_effect_map.py`

Soll-Struktur:

```text
semantic_memory.py
  - DIO-Syntax
  - Bedeutungsfamilien
  - semantische Verdichtung
  - passive Bedeutungskarten
```

Grenze:

Semantik darf nicht zur vorprogrammierten Strategie werden.
Sie beschreibt verdichtete Bedeutung:

```text
Diese Innenfeldlage kommt wieder und trägt eine ähnliche Wirkung.
```

## Zieltrennung

Die Zielarchitektur:

```text
perception_memory.py
  -> erinnert Wahrnehmungsnähe, Nachhall, Priming

mcm_field_memory.py
  -> erinnert Feldwirkung, Rekopplung, Carry, Strain

episode_store.py
  -> erinnert konkrete Erlebnisabschnitte

semantic_memory.py
  -> verdichtet wiederkehrende Erfahrung zu DIO-Syntax und Bedeutung
```

`semantic_memory.py` bleibt vorerst eine Kompatibilitätsfassade.
Bestehende JSON-Strukturen und Reports dürfen nicht gebrochen werden.

## Aktueller Befund

Die Mechanik ist bereits teilweise vorhanden.
Sie ist aber noch nicht sauber genug getrennt.

Aktuell bündelt `semantic_memory.py` zu viel:

- Syntaxbildung,
- Symbolfamilien,
- Action-/Observation-Reste,
- temporale Familien,
- Episodenmemory,
- MCM-Feldepisoden,
- passive Reflexionskarten,
- passive Bedeutungsnotizen.

Das ist funktional brauchbar, aber architektonisch zu breit.

## Umsetzungsregel

Beim Umbau gilt:

```text
Erst trennen.
Dann prüfen.
Dann erst Verhalten ändern.
```

Keine neue Handlungsschicht.
Keine Gates.
Keine Strategie.
Keine Vermischung von Hypothese und Realität.

## Erster umgesetzter Schritt

Die reine DIO-Syntaxbildung wurde in ein eigenes Modul ausgelagert:

```text
mini_dio/dio_syntax.py
```

Damit ist die erste Grenze gezogen:

```text
Syntax erzeugen != Memory speichern
```

`semantic_memory.py` importiert die Syntaxfunktionen weiter als Kompatibilitätsfassade.
`run_mini.py` nutzt die Syntaxfunktionen direkt aus `dio_syntax.py`.

Der Kontrolllauf `790_DIO_SYNTAX_AUSLAGERUNG_CHECK.md` zeigt keine fachliche Abweichung.

## Zweiter umgesetzter Schritt

Die Episodenpersistenz wurde in ein eigenes Modul ausgelagert:

```text
mini_dio/episode_store.py
```

Damit ist die zweite Grenze gezogen:

```text
Episode speichern != semantische Bedeutung bilden
```

`semantic_memory.py` delegiert:

- `store_episode_memory`
- `compact_episode_memory`
- Top-Episodenlisten

weiter an `episode_store.py`.

Der Kontrolllauf `791_EPISODE_STORE_AUSLAGERUNG_CHECK.md` zeigt keine fachliche Abweichung.

## Dritter umgesetzter Schritt

Die MCM-Feldepisoden wurden aus der allgemeinen Episodenpersistenz herausgeloest:

```text
mini_dio/mcm_field_memory_store.py
```

Damit ist die dritte Grenze gezogen:

```text
Konkrete Episode speichern != MCM-Feldwirkung erinnern
```

`semantic_memory.py` delegiert:

- `store_mcm_field_episode_memory`
- `compact_mcm_field_episode_memory`
- Top-MCM-Feldepisodenlisten

weiter an `mcm_field_memory_store.py`.

`episode_store.py` bleibt damit auf konkrete passive Episoden beschraenkt.

Der Kontrolllauf `792_MCM_FIELD_STORE_AUSLAGERUNG_CHECK.md` zeigt keine fachliche Abweichung.

## Vierter umgesetzter Schritt

Die temporalen Wahrnehmungs- und Primingspuren wurden in ein eigenes Modul ausgelagert:

```text
mini_dio/perception_memory_store.py
```

Damit ist die vierte Grenze gezogen:

```text
Wahrnehmungsnachhall erinnern != MCM-Feldwirkung speichern
```

`semantic_memory.py` delegiert:

- `store_temporal_family`
- `compact_temporal_families`

weiter an `perception_memory_store.py`.

Diese Schicht traegt Wiederkehr, Nachhall, zeitliche Naehe und passive Vorsicht/Vertrauensstuetzung. Sie ist keine Handlungsschicht.

Der Kontrolllauf `793_PERCEPTION_STORE_AUSLAGERUNG_CHECK.md` zeigt keine fachliche Abweichung.

## Fuenfter umgesetzter Schritt

Die passive semantische Bedeutungsablage wurde in ein eigenes Modul ausgelagert:

```text
mini_dio/semantic_meaning_store.py
```

Damit ist die fuenfte Grenze gezogen:

```text
Bedeutung erklaeren != Grundgedaechtnis tragen
```

`semantic_memory.py` delegiert:

- passive Innenfeld-Reflexionsnotizen
- passive Meaning-Notes
- passive Innenfeldkarten
- Kartenvergleiche
- Bridge-/Archetypen-/Matrix-Ablagen

weiter an `semantic_meaning_store.py`.

Diese Schicht bleibt diagnostisch und erklaerend. Sie liest nicht in Handlung, Entry, Gate, Richtung oder Motorik hinein.

Der Kontrolllauf `794_SEMANTIC_MEANING_STORE_AUSLAGERUNG_CHECK.md` zeigt keine fachliche Abweichung.

## Sechster umgesetzter Schritt

Die passiven Beziehungs- und Reflexionsspuren wurden in ein eigenes Modul ausgelagert:

```text
mini_dio/passive_trace_store.py
```

Damit ist die sechste Grenze gezogen:

```text
Passive Spur speichern != aktive Action-Kompatibilitaet tragen
```

`semantic_memory.py` delegiert:

- Sensorrelationen
- Nachbarschaftskonsequenzen
- Kontaktlagen
- Satzspuren
- Reflexionsseeds
- Reflexionsmaps

weiter an `passive_trace_store.py`.

Diese Spuren bleiben passiv. Sie dokumentieren Wiederkehr, Kontakt, Naehe, Reflexion und Vergleich, ohne selbst Handlung, Entry oder Gate zu werden.

Der Kontrolllauf `795_PASSIVE_TRACE_STORE_AUSLAGERUNG_CHECK.md` zeigt keine fachliche Abweichung.

## Siebter umgesetzter Schritt

Die aktive Action-/Observation-Kompatibilitaet wurde in ein eigenes Modul ausgelagert:

```text
mini_dio/action_memory_store.py
```

Damit ist die siebte Grenze gezogen:

```text
Aktive Kompatibilitaetsstatistik != passive MCM-Gedaechtnisarchitektur
```

`semantic_memory.py` delegiert:

- `symbol_record`
- `family_record`
- `action_diagnostics`
- `action_bias`
- `action_readiness`
- `learn`
- `learn_observation`
- Symbol-/Familien-Kompaktierungsranking

weiter an `action_memory_store.py`.

Diese Schicht ist kein Zielmodell fuer die passive MINI_DIO-Forschung. Sie bleibt nur erhalten, damit alte Laufpfade und JSON-Strukturen nicht brechen.

Der Kontrolllauf `796_ACTION_MEMORY_STORE_AUSLAGERUNG_CHECK.md` zeigt keine fachliche Abweichung.

## Verbleibende Restlast in `semantic_memory.py`

Nach den Auslagerungen verbleiben bewusst:

- `SemanticMemory` als JSON-kompatible Fassade,
- `load`
- `save`
- `mark_run`
- Delegationsmethoden auf die getrennten Store-Module,
- JSON-Schema-Kompatibilitaet.

`semantic_memory.py` ist damit wieder naeher an der vorgesehenen Rolle:

```text
Memory-Dokument verwalten
Store-Module verbinden
alte API stabil halten
```

## Achter umgesetzter Schritt

Die aktive Aktionsauswahl wurde aus `run_mini.py` ausgelagert:

```text
mini_dio/action_selection.py
```

Damit ist die achte Grenze gezogen:

```text
Laufpfad / Wahrnehmungsschleife != aktive Aktionsauswahl
```

`run_mini.py` delegiert jetzt:

- `choose_action`
- weiche Action-Pressure-Berechnung
- Score-Erweiterung mit aktiver Memory-Kompatibilitaet

weiter an `action_selection.py`.

Diese Auslagerung aendert keine Handlung, kein Gate und keine MCM-Feldwirkung.
Sie macht nur sichtbar, dass aktive Aktionswahl eine getrennte Kompatibilitaetsschicht ist.

Der Kontrolllauf `797_ACTION_SELECTION_AUSLAGERUNG_CHECK.md` zeigt keine fachliche Abweichung.

## Wie es weitergeht

Als naechstes wird der Laufpfad weiter kartiert: Was ist passive Wahrnehmung, was ist neuronale Feldreaktion, was ist aktive Auswahl, und was ist nur Reporting/Debug?
