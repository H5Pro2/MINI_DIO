# 1996_PASSIVE_FELDFUNKTIONS_MEMORY_MEHRWELT - Passive Feldfunktions-Memory Mehrweltprüfung

## Zweck

Diese Diagnose liest die neue passive Feldfunktionsqualität aus einer Memory-Datei.

Geprüft wird nicht Handlung, sondern ob wiederkehrende Preview-Anker eine Feldfunktionsqualität mittragen:

- `milieu_island`
- `active_recoupling`
- `open_surface`
- `undetermined`

Die Lesung bleibt passiv.

## Datengrundlage

- Memory: `memory\1996_field_function_multiworld_probe.json`
- Preview-Anker gesamt: `512`
- Preview-Anker mit Feldfunktionslesung: `200`

## Klassen

- `active_recoupling`: `162`
- `milieu_island`: `31`
- `open_surface`: `7`

## Varianten

- `distributed_active_recoupling`: `119`
- `compact_carried_recoupling`: `43`
- `quiet_deep_recoupling`: `20`
- `local_milieu_seed`: `11`
- `unsettled_surface_trace`: `7`

## Bekannte Referenzrollen

- `dio_mcm_episode_0hiolzy`: `active_recoupling` / `compact_carried_recoupling`, Konfidenz `0.652079`, Depth `0.830658`, Welten `5`, Count `54`, Last `FF_SOL_STABLE_2026_10K`
- `dio_mcm_episode_1yxc2ug`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.80289`, Depth `0.727123`, Welten `27`, Count `1642`, Last `FF_DOGE_2024_10K`
- `dio_mcm_episode_0hvxln3`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.818436`, Depth `0.697503`, Welten `41`, Count `371`, Last `FF_PAXG_2024_10K`
- `dio_mcm_episode_14sn1ov`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.807789`, Depth `0.711288`, Welten `34`, Count `387`, Last `FF_DOGE_2024_10K`

## Top-Anker

- `dio_mcm_episode_1k1vudq`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.888153`, Welten `5`, Count `6`
- `dio_mcm_episode_0j5jlak`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.888138`, Welten `6`, Count `11`
- `dio_mcm_episode_1qmlwcr`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.873017`, Welten `13`, Count `21`
- `dio_mcm_episode_1dxx3n8`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.87006`, Welten `10`, Count `26`
- `dio_mcm_episode_103jy5j`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.87006`, Welten `5`, Count `5`
- `dio_mcm_episode_1rf1k15`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.867487`, Welten `5`, Count `21`
- `dio_mcm_episode_0pvq9jm`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.86618`, Welten `6`, Count `13`
- `dio_mcm_episode_07a7zoq`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.862018`, Welten `8`, Count `25`
- `dio_mcm_episode_06eyd53`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.861702`, Welten `8`, Count `16`
- `dio_mcm_episode_159zeqh`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.860722`, Welten `8`, Count `23`
- `dio_mcm_episode_1amcian`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.859767`, Welten `5`, Count `8`
- `dio_mcm_episode_14xx81a`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.858038`, Welten `9`, Count `3177`

## Lesung

Die neue Memory-Lesung erzeugt keine reine Symboltabelle.
Sie zeigt, ob ein Symbol im aktuellen Mehrwelt-Kontext eher als Milieuinsel, aktive Rekopplung oder offene Oberfläche getragen wird.

Wichtig ist die Kontextabhängigkeit: Eine Rolle kann in einer engen Weltprüfung wie Milieu wirken und in breiterer Mehrweltprüfung als aktive Rekopplung gelesen werden.
Damit bleibt die Qualität feldbezogen statt namensfixiert.

## Wie es weitergeht

Als nächstes sollte dieselbe Auswertung mit frischer Memory gegen kontrollierte Nullwelten laufen. Dann wird sichtbar, ob die Feldfunktionslesung reale Weltstruktur braucht oder auch in entkoppelten Kontrollwelten ähnlich stark entsteht.
