# 2002_MIXED_BINDING_FOLGEWELT_PROBE - Passive Feldfunktions-Memory Mehrweltprüfung

## Zweck

Diese Diagnose liest die neue passive Feldfunktionsqualität aus einer Memory-Datei.

Geprüft wird nicht Handlung, sondern ob wiederkehrende Preview-Anker eine Feldfunktionsqualität mittragen:

- `milieu_island`
- `active_recoupling`
- `open_surface`
- `undetermined`

Die Lesung bleibt passiv.

## Datengrundlage

- Memory: `memory\2002_mixed_binding_follow_probe.json`
- Preview-Anker gesamt: `512`
- Preview-Anker mit Feldfunktionslesung: `178`

## Klassen

- `active_recoupling`: `156`
- `milieu_island`: `15`
- `open_surface`: `7`

## Varianten

- `distributed_active_recoupling`: `118`
- `compact_carried_recoupling`: `38`
- `quiet_deep_recoupling`: `13`
- `unsettled_surface_trace`: `7`
- `local_milieu_seed`: `2`

## Weltbindung

- `realworld_bound`: `172`
- `mixed_binding`: `5`
- `field_internal_null_order`: `1`

## Bekannte Referenzrollen

- `dio_mcm_episode_0hiolzy`: `-` / `-`, Konfidenz `-`, Depth `-`, Bindung `-` (`-`), Welten `-`, Count `-`, Last `-`
- `dio_mcm_episode_1yxc2ug`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.804771`, Depth `0.721273`, Bindung `realworld_bound` (`0.922497`), Welten `28`, Count `1592`, Last `MB_FOLLOW_XRP_2025_5K_6K`
- `dio_mcm_episode_0hvxln3`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.818614`, Depth `0.697197`, Bindung `realworld_bound` (`0.906657`), Welten `42`, Count `360`, Last `MB_FOLLOW_PAXG_2025_5K_6K`
- `dio_mcm_episode_14sn1ov`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.808147`, Depth `0.709526`, Bindung `realworld_bound` (`0.912394`), Welten `34`, Count `364`, Last `MB_FOLLOW_DOGE_2025_5K_6K`

## Top-Anker

- `dio_mcm_episode_1k1vudq`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.888153`, Bindung `realworld_bound`, Welten `5`, Count `6`
- `dio_mcm_episode_103jy5j`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.869221`, Bindung `realworld_bound`, Welten `4`, Count `4`
- `dio_mcm_episode_1dxx3n8`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.865984`, Bindung `realworld_bound`, Welten `9`, Count `22`
- `dio_mcm_episode_08op00s`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.861975`, Bindung `realworld_bound`, Welten `17`, Count `52`
- `dio_mcm_episode_0pvq9jm`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.860662`, Bindung `realworld_bound`, Welten `5`, Count `10`
- `dio_mcm_episode_0s13pzp`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.860562`, Bindung `realworld_bound`, Welten `4`, Count `5`
- `dio_mcm_episode_06eyd53`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.860179`, Bindung `realworld_bound`, Welten `8`, Count `15`
- `dio_mcm_episode_07a7zoq`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.859737`, Bindung `realworld_bound`, Welten `7`, Count `20`
- `dio_mcm_episode_159zeqh`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.85497`, Bindung `realworld_bound`, Welten `7`, Count `16`
- `dio_mcm_episode_1avuyqc`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.853123`, Bindung `realworld_bound`, Welten `7`, Count `22`
- `dio_mcm_episode_1amcian`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.851784`, Bindung `realworld_bound`, Welten `4`, Count `6`
- `dio_mcm_episode_1qv5i56`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.850099`, Bindung `realworld_bound`, Welten `17`, Count `110`

## Lesung

Die neue Memory-Lesung erzeugt keine reine Symboltabelle.
Sie zeigt, ob ein Symbol im aktuellen Mehrwelt-Kontext eher als Milieuinsel, aktive Rekopplung oder offene Oberfläche getragen wird.

Die Weltbindungsqualität ergänzt diese Lesung um Herkunft: realweltlich gebunden, nullweltlich/feldintern, synthetisch oder gemischt.
Damit bleibt die Qualität feldbezogen statt namensfixiert und Feldordnung wird nicht automatisch als Realweltbindung gelesen.
