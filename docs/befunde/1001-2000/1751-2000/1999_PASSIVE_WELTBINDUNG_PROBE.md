# 1999_PASSIVE_WELTBINDUNG_PROBE - Passive Feldfunktions-Memory Mehrweltprüfung

## Zweck

Diese Diagnose liest die neue passive Feldfunktionsqualität aus einer Memory-Datei.

Geprüft wird nicht Handlung, sondern ob wiederkehrende Preview-Anker eine Feldfunktionsqualität mittragen:

- `milieu_island`
- `active_recoupling`
- `open_surface`
- `undetermined`

Die Lesung bleibt passiv.

## Datengrundlage

- Memory: `memory\1999_world_binding_probe.json`
- Preview-Anker gesamt: `512`
- Preview-Anker mit Feldfunktionslesung: `123`

## Klassen

- `active_recoupling`: `108`
- `milieu_island`: `14`
- `open_surface`: `1`

## Varianten

- `distributed_active_recoupling`: `77`
- `compact_carried_recoupling`: `31`
- `quiet_deep_recoupling`: `13`
- `local_milieu_seed`: `1`
- `unsettled_surface_trace`: `1`

## Weltbindung

- `realworld_bound`: `117`
- `mixed_binding`: `5`
- `field_internal_null_order`: `1`

## Bekannte Referenzrollen

- `dio_mcm_episode_0hiolzy`: `-` / `-`, Konfidenz `-`, Depth `-`, Bindung `-` (`-`), Welten `-`, Count `-`, Last `-`
- `dio_mcm_episode_1yxc2ug`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.802867`, Depth `0.726196`, Bindung `realworld_bound` (`0.923117`), Welten `25`, Count `1495`, Last `WB_REAL_BTC_2024_10K`
- `dio_mcm_episode_0hvxln3`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.818227`, Depth `0.698127`, Bindung `realworld_bound` (`0.906581`), Welten `39`, Count `355`, Last `WB_NULL_BTC_SHUFFLE_10K`
- `dio_mcm_episode_14sn1ov`: `active_recoupling` / `distributed_active_recoupling`, Konfidenz `0.807778`, Depth `0.71112`, Bindung `realworld_bound` (`0.912487`), Welten `33`, Count `358`, Last `WB_NULL_BTC_SHUFFLE_10K`

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
