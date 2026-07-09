# 1997_PASSIVE_FELDFUNKTIONS_MEMORY_NULLWELT - Passive Feldfunktions-Memory Mehrweltprüfung

## Zweck

Diese Diagnose liest die neue passive Feldfunktionsqualität aus einer Memory-Datei.

Geprüft wird nicht Handlung, sondern ob wiederkehrende Preview-Anker eine Feldfunktionsqualität mittragen:

- `milieu_island`
- `active_recoupling`
- `open_surface`
- `undetermined`

Die Lesung bleibt passiv.

## Datengrundlage

- Memory: `memory\1997_field_function_nullworld_probe.json`
- Preview-Anker gesamt: `512`
- Preview-Anker mit Feldfunktionslesung: `169`

## Klassen

- `active_recoupling`: `141`
- `milieu_island`: `25`
- `open_surface`: `3`

## Varianten

- `distributed_active_recoupling`: `101`
- `compact_carried_recoupling`: `40`
- `quiet_deep_recoupling`: `22`
- `local_milieu_seed`: `3`
- `unsettled_surface_trace`: `3`

## Bekannte Referenzrollen

- `dio_mcm_episode_0hiolzy`: `-` / `-`, Konfidenz `-`, Depth `-`, Welten `-`, Count `-`, Last `-`
- `dio_mcm_episode_1yxc2ug`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.802288`, Depth `0.727625`, Welten `26`, Count `1473`, Last `FF_NULL_XRP_SHUFFLE_10K`
- `dio_mcm_episode_0hvxln3`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.817624`, Depth `0.699068`, Welten `41`, Count `374`, Last `FF_NULL_XRP_SHUFFLE_10K`
- `dio_mcm_episode_14sn1ov`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.805977`, Depth `0.716821`, Welten `34`, Count `357`, Last `FF_NULL_XRP_SHUFFLE_10K`

## Top-Anker

- `dio_mcm_episode_0j5jlak`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.885067`, Welten `6`, Count `11`
- `dio_mcm_episode_1k1vudq`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.88307`, Welten `5`, Count `8`
- `dio_mcm_episode_103jy5j`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.874928`, Welten `4`, Count `5`
- `dio_mcm_episode_1qmlwcr`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.874118`, Welten `12`, Count `21`
- `dio_mcm_episode_06eyd53`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.868585`, Welten `8`, Count `13`
- `dio_mcm_episode_0pvq9jm`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.86574`, Welten `5`, Count `10`
- `dio_mcm_episode_1dxx3n8`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.864082`, Welten `9`, Count `25`
- `dio_mcm_episode_08op00s`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.862531`, Welten `19`, Count `59`
- `dio_mcm_episode_0s13pzp`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.860563`, Welten `4`, Count `5`
- `dio_mcm_episode_01116gq`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.858163`, Welten `8`, Count `19`
- `dio_mcm_episode_07a7zoq`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.857893`, Welten `8`, Count `21`
- `dio_mcm_episode_02ixe4y`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.854587`, Welten `10`, Count `23`

## Lesung

Die neue Memory-Lesung erzeugt keine reine Symboltabelle.
Sie zeigt, ob ein Symbol im aktuellen Mehrwelt-Kontext eher als Milieuinsel, aktive Rekopplung oder offene Oberfläche getragen wird.

Wichtig ist die Kontextabhängigkeit: Eine Rolle kann in einer engen Weltprüfung wie Milieu wirken und in breiterer Mehrweltprüfung als aktive Rekopplung gelesen werden.
Damit bleibt die Qualität feldbezogen statt namensfixiert.

## Wie es weitergeht

Als nächstes sollte dieselbe Auswertung mit frischer Memory gegen kontrollierte Nullwelten laufen. Dann wird sichtbar, ob die Feldfunktionslesung reale Weltstruktur braucht oder auch in entkoppelten Kontrollwelten ähnlich stark entsteht.
