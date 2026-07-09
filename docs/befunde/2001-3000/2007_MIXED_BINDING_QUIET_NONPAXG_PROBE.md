# 2007_MIXED_BINDING_QUIET_NONPAXG_PROBE - Passive Feldfunktions-Memory Mehrweltprüfung

## Zweck

Diese Diagnose liest die neue passive Feldfunktionsqualität aus einer Memory-Datei.

Geprüft wird nicht Handlung, sondern ob wiederkehrende Preview-Anker eine Feldfunktionsqualität mittragen:

- `milieu_island`
- `active_recoupling`
- `open_surface`
- `undetermined`

Die Lesung bleibt passiv.

## Datengrundlage

- Memory: `memory\2007_mixed_binding_quiet_nonpaxg_probe.json`
- Preview-Anker gesamt: `512`
- Preview-Anker mit Feldfunktionslesung: `161`

## Klassen

- `active_recoupling`: `142`
- `milieu_island`: `16`
- `open_surface`: `3`

## Varianten

- `distributed_active_recoupling`: `108`
- `compact_carried_recoupling`: `34`
- `quiet_deep_recoupling`: `15`
- `unsettled_surface_trace`: `3`
- `local_milieu_seed`: `1`

## Weltbindung

- `realworld_bound`: `155`
- `mixed_binding`: `5`
- `field_internal_null_order`: `1`

## Bekannte Referenzrollen

- `dio_mcm_episode_05w9z7v`: `milieu_island` / `quiet_deep_recoupling`, Konfidenz `0.687569`, Depth `0.760059`, Bindung `mixed_binding` (`0.622023`), Welten `2`, Count `6`, Last `WB_NULL_BTC_SHUFFLE_10K`
- `dio_mcm_episode_08g2xgt`: `milieu_island` / `quiet_deep_recoupling`, Konfidenz `0.67605`, Depth `0.810279`, Bindung `mixed_binding` (`0.566224`), Welten `3`, Count `5`, Last `WB_NULL_BTC_SHUFFLE_10K`
- `dio_mcm_episode_0zkoaz0`: `active_recoupling` / `compact_carried_recoupling`, Konfidenz `0.499202`, Depth `0.569433`, Bindung `mixed_binding` (`0.553759`), Welten `2`, Count `2`, Last `WB_NULL_BTC_SHUFFLE_10K`
- `dio_mcm_episode_15jz0fg`: `milieu_island` / `quiet_deep_recoupling`, Konfidenz `0.701`, Depth `0.770993`, Bindung `mixed_binding` (`0.626359`), Welten `2`, Count `6`, Last `WB_NULL_BTC_SHUFFLE_10K`
- `dio_mcm_episode_1i07qau`: `milieu_island` / `quiet_deep_recoupling`, Konfidenz `0.705057`, Depth `0.777121`, Bindung `mixed_binding` (`0.628233`), Welten `2`, Count `2`, Last `WB_NULL_BTC_SHUFFLE_10K`

## Top-Anker

- `dio_mcm_episode_1k1vudq`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.888153`, Bindung `realworld_bound`, Welten `5`, Count `6`
- `dio_mcm_episode_103jy5j`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.869221`, Bindung `realworld_bound`, Welten `4`, Count `4`
- `dio_mcm_episode_1dxx3n8`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.866045`, Bindung `realworld_bound`, Welten `10`, Count `23`
- `dio_mcm_episode_08op00s`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.861975`, Bindung `realworld_bound`, Welten `17`, Count `52`
- `dio_mcm_episode_0pvq9jm`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.860662`, Bindung `realworld_bound`, Welten `5`, Count `10`
- `dio_mcm_episode_0s13pzp`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.860562`, Bindung `realworld_bound`, Welten `4`, Count `5`
- `dio_mcm_episode_07a7zoq`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.860212`, Bindung `realworld_bound`, Welten `8`, Count `21`
- `dio_mcm_episode_159zeqh`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.85497`, Bindung `realworld_bound`, Welten `7`, Count `16`
- `dio_mcm_episode_06eyd53`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.853305`, Bindung `realworld_bound`, Welten `9`, Count `17`
- `dio_mcm_episode_1avuyqc`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.853123`, Bindung `realworld_bound`, Welten `7`, Count `22`
- `dio_mcm_episode_1amcian`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.851784`, Bindung `realworld_bound`, Welten `4`, Count `6`
- `dio_mcm_episode_1qv5i56`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.850337`, Bindung `realworld_bound`, Welten `18`, Count `111`

## Lesung

Die neue Memory-Lesung erzeugt keine reine Symboltabelle.
Sie zeigt, ob ein Symbol im aktuellen Mehrwelt-Kontext eher als Milieuinsel, aktive Rekopplung oder offene Oberfläche getragen wird.

Die Weltbindungsqualität ergänzt diese Lesung um Herkunft: realweltlich gebunden, nullweltlich/feldintern, synthetisch oder gemischt.
Damit bleibt die Qualität feldbezogen statt namensfixiert und Feldordnung wird nicht automatisch als Realweltbindung gelesen.
