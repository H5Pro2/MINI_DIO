# SemanticMemory Zerlegekarte

Stand: 2026-06-23

## Zweck

Diese Notiz prüft, welche Bestandteile aus `mini_dio/semantic_memory.py` in eigene Gedächtnisschichten ausgelagert werden sollten.

Ziel ist keine neue Mechanik.
Ziel ist saubere Trennung:

```text
Wahrnehmungsgedächtnis
MCM-Feldgedächtnis
episodisches Gedächtnis
semantische Bedeutungsverdichtung
```

## Aktueller Zustand

`semantic_memory.py` ist aktuell eine große Sammeldatei.

Sie enthält:

- DIO-Syntaxbildung,
- Symbol- und Familienrecords,
- Action-/Observation-Statistiken,
- sensorische Relationen,
- Nachbarschaftsfolgen,
- Kontaktlagen,
- Reflexionsspuren,
- temporale Familien,
- Episodenmemory,
- MCM-Feldepisoden,
- passive Innenfeldbedeutungen,
- Kompaktierungslogik,
- JSON-Persistenz.

Das ist historisch verständlich, aber inzwischen fachlich zu breit.

## Zielmodul 1: `dio_syntax.py`

Status: umgesetzt.

Auslagern:

- `_base36`
- `make_syntax_vector`
- `make_syntax_symbol`
- `make_contact_lage_symbol`
- `make_reflection_seed_symbol`
- `make_reflection_map_symbol`
- `make_episode_memory_symbol`
- `make_mcm_field_episode_symbol`

Funktion:

```text
DIO-eigene Syntax erzeugen.
Keine Memory-Persistenz.
Keine Handlung.
Keine Feldentscheidung.
```

Grund:

Syntaxbildung ist eine eigene Fähigkeit.
Sie darf nicht an eine bestimmte Speicherdatei gebunden sein.

## Zielmodul 2: `perception_memory_store.py`

Auslagern:

- `temporal_families`
- `store_temporal_family`
- `_temporal_family_rank`
- Wahrnehmungsnähe / Afterimage-Verweise

Funktion:

```text
Wahrnehmungswiederkehr, Priming und Nachhall speichern.
```

Aktueller Anschluss:

- `mini_dio/temporal_memory.py` erzeugt die In-Run-Spur.
- `perception_memory_store.py` sollte die persistente Spur aufnehmen.

## Zielmodul 3: `episode_store.py`

Status: umgesetzt.

Auslagern:

- `episode_memory`
- `store_episode_memory`
- `_episode_memory_rank`
- `compact_episode_memory`
- `compact_top_episode_memory`

Funktion:

```text
konkrete Erlebnisabschnitte speichern.
```

Grenze:

Episode ist nicht automatisch Bedeutung.
Episode beschreibt zuerst Verlauf, Dauer, Übergang und dominante Familie.

## Zielmodul 4: `mcm_field_memory_store.py`

Auslagern:

- `mcm_field_episode_memory`
- `store_mcm_field_episode_memory`
- `_mcm_field_episode_rank`
- `compact_mcm_field_episode_memory`
- `compact_top_mcm_field_episode_memory`
- passive MCM-Feldwirkungsdaten

Funktion:

```text
Feldwirkung speichern: Carry, Strain, Rekopplung, Sinneskopplung, Randnähe.
```

Grenze:

Diese Schicht speichert keine Strategie.
Sie beschreibt nur:

```text
Wie hat eine Weltlage im MCM-Feld gewirkt?
```

## Zielmodul 5: `semantic_meaning_store.py`

Auslagern:

- `passive_inner_effect_reflection_notes`
- `passive_inner_effect_reflection_history`
- `passive_inner_effect_meaning_notes`
- `passive_inner_field_maps`
- `passive_inner_field_map_comparison`
- `passive_inner_field_bridge_stable_contrast`
- `passive_inner_field_archetypes`
- `passive_inner_field_archetype_matrix`
- zugehörige Store-Methoden

Funktion:

```text
wiederkehrende Feldwirkungen zu Bedeutungsräumen verdichten.
```

Grenze:

Bedeutung bleibt passiv und erklärend.
Sie darf kein Gate und kein Entry-Signal werden.

## In `semantic_memory.py` vorerst behalten

Vorerst behalten:

- `SemanticMemory` als Kompatibilitätsfassade,
- `load`
- `save`
- `mark_run`
- `symbol_record`
- `family_record`
- JSON-Schema-Kompatibilität,
- bestehende Action-/Observation-Felder, solange alte Reports sie erwarten.

Grund:

Bestehende Forschungsläufe, Reports und JSON-Memory-Dateien dürfen nicht brechen.

## Historische Altlasten

Diese Bereiche sind für MINI_DIO fachlich kritisch und müssen später gesondert bewertet werden:

- `actions`
- `observations`
- `action_diagnostics`
- `action_bias`
- `action_readiness`
- `learn`
- `learn_observation`
- `_associative_signal`
- `_action_signal`
- `_observation_signal`

Sie stammen aus einer handlungsnäheren Phase.
Für den aktuellen passiven MINI_DIO-Forschungsstand dürfen sie nicht wieder zur dominanten Mechanik werden.

Sie bleiben vorerst aus Kompatibilitätsgründen im Code, werden aber nicht als Kern der neuen Gedächtnisarchitektur betrachtet.

## Priorisierte Auslagerung

1. `dio_syntax.py`
   - umgesetzt.
   - niedriges Risiko, reine Funktionsauslagerung.
   - Kontrolllauf: `790_DIO_SYNTAX_AUSLAGERUNG_CHECK.md`.

2. `episode_store.py`
   - umgesetzt.
   - mittleres Risiko, klare fachliche Grenze.
   - Kontrolllauf: `791_EPISODE_STORE_AUSLAGERUNG_CHECK.md`.

3. `mcm_field_memory_store.py`
   - umgesetzt.
   - hoher fachlicher Wert, weil es MCM-Feldgedaechtnis sauber trennt.
   - Kontrolllauf: `792_MCM_FIELD_STORE_AUSLAGERUNG_CHECK.md`.

4. `perception_memory_store.py`
   - umgesetzt.
   - trennt Wahrnehmungsnaehe, Nachhall und Priming von MCM-Feldwirkung.
   - Kontrolllauf: `793_PERCEPTION_STORE_AUSLAGERUNG_CHECK.md`.

5. `semantic_meaning_store.py`
   - umgesetzt.
   - trennt passive Bedeutungsnotizen, Innenfeldkarten und Archetypen-Ablagen von den Grundspeichern.
   - Kontrolllauf: `794_SEMANTIC_MEANING_STORE_AUSLAGERUNG_CHECK.md`.

6. `passive_trace_store.py`
   - umgesetzt.
   - trennt passive Relationen, Kontaktlagen, Satzspuren, Reflexionsseeds und Reflexionsmaps von aktiver Action-/Observation-Kompatibilitaet.
   - Kontrolllauf: `795_PASSIVE_TRACE_STORE_AUSLAGERUNG_CHECK.md`.

7. `action_memory_store.py`
   - umgesetzt.
   - isoliert alte aktive Symbol-/Familien-, Action- und Observation-Kompatibilitaet.
   - Kontrolllauf: `796_ACTION_MEMORY_STORE_AUSLAGERUNG_CHECK.md`.

8. `action_selection.py`
   - umgesetzt.
   - isoliert aktive Aktionsauswahl und weiche Action-Pressure-Berechnung aus `run_mini.py`.
   - Kontrolllauf: `797_ACTION_SELECTION_AUSLAGERUNG_CHECK.md`.

## Prüfregel nach jeder Auslagerung

Nach jedem Schritt:

```powershell
python .\tools\check_project.py
python .\tools\run_research_chain.py
```

Zusätzlich prüfen:

- gleiche Anzahl Episoden,
- gleiche Top-Syntax-Überlappung,
- gleiche Top-Familien-Überlappung,
- keine Änderung der passiven MCM-Wirkungsklassen,
- keine neue Handlungskopplung.

## Schlussfolgerung

Die vier Gedächtnisschichten existieren bereits als Mechanikansätze.
Sie sind aber noch nicht sauber genug als Architektur getrennt.

Die acht sicheren Trennungen sind umgesetzt:

- Syntaxbildung,
- konkrete Episodenpersistenz,
- MCM-Feldgedaechtnis,
- Wahrnehmungs-/Priming-Gedaechtnis,
- semantische Bedeutungsablage,
- passive Beziehungs- und Reflexionsspuren,
- aktive Action-/Observation-Kompatibilitaet,
- aktive Aktionsauswahl.

Damit wird `semantic_memory.py` schrittweise wieder zur Fassade und zur spaeteren semantischen Verdichtung zurueckgefuehrt.

Die aktive Restlast ist nicht geloescht, aber fachlich gekapselt:

```text
mini_dio/action_memory_store.py
mini_dio/action_selection.py
```

Diese Schicht ist aktuell aktive Kompatibilitaet mit `run_mini.py`, nicht Kern der passiven MINI_DIO-Gedaechtnisarchitektur.
`semantic_memory.py` bleibt dadurch JSON-Fassade und API-Bruecke.

## Wie es weitergeht

Als naechstes sollte der Laufpfad selbst weiter kartiert werden: passive Wahrnehmung, neuronale Feldreaktion, aktive Auswahl und Reporting/Debug muessen im Code klar unterscheidbar bleiben.
