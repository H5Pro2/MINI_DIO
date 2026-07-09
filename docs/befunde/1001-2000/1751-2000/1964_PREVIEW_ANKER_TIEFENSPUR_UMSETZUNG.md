# 1964 - Preview-Anker-Tiefenspur Umsetzung

## Frage

Kann MINI_DIO wiederkehrende Preview-Anker nicht nur als Oberfläche lesen, sondern passiv als erste Tiefenspur speichern?

Wichtig: Diese Erweiterung darf keine Handlung, Richtung, Gate-Logik, Entry-Logik oder Motorik beeinflussen.

## Umsetzung

Ergänzt wurde eine passive Memory-Schicht:

- `passive_mcm_preview_anchor_depth_memory`
- Speicherung nach `preview_symbol`
- Verdichtung aus Profilnähe, Nachhall, Rekurrenz, Rekopplung, Strain und Sinneskopplung
- Statusformen: `surface_anchor`, `local_depth_seed`, `recurring_depth_seed`, `multiworld_depth_seed`

Die Schicht ist ausdrücklich passiv:

- `passive_only = 1`
- `read_by_mini_dio = 0`
- `influences_action = 0`
- `is_gate = 0`
- `is_motoric = 0`
- `is_entry_signal = 0`
- `is_direction_signal = 0`

## Probe

Isolierter Probelauf:

- Welt: `data\btc_2025_1h_follow_candidate_2000_3000.csv`
- Label: `PREVIEW_DEPTH_PROBE`
- Kerzen: `1000`
- Memory: `memory\preview_depth_probe.json`
- Debug: `debug\preview_depth_probe`

## Ergebnis

Der Probelauf erzeugte:

- `56` passive Preview-Anker-Tiefenspuren im Memory
- `899` Episoden mit `local_depth_seed`
- `95` Episoden mit `surface_anchor`
- durchschnittlicher Tiefenwert: `0.504173`
- maximaler Tiefenwert: `0.701278`
- durchschnittliche Profilnähe: `0.675063`

Die neuen Debug-Spalten werden geschrieben:

- `mcm_preview_anchor_depth_state`
- `mcm_preview_anchor_depth_score`
- `mcm_preview_anchor_world_count`
- `mcm_preview_anchor_profile_proximity`

## Befund

MINI_DIO kann Preview-Anker nun passiv als Tiefenspur speichern. Damit wird aus einem bloßen Oberflächenanker noch keine Rolle, aber ein prüfbarer Zwischenzustand:

> Diese Form taucht wieder auf und trägt genug Nähe, Nachhall oder Rekopplung, um als Tiefe beobachtet zu werden.

Das ist noch keine mehrweltliche Bestätigung. In dieser Probe ist `world_count = 1`; deshalb ist `local_depth_seed` korrekt und `multiworld_depth_seed` noch nicht belegt.

## Grenze

Die Erweiterung ist keine Strategie, keine Handlungsvorbereitung und keine Richtungsentscheidung. Sie verbessert nur die passive Lesbarkeit von wiederkehrenden Preview-Ankern.
