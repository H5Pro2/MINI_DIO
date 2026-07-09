# 2005_MIXED_BINDING_ZIELWELTEN_PROBE - Passive Feldfunktions-Memory Mehrweltprüfung

## Zweck

Diese Diagnose liest die neue passive Feldfunktionsqualität aus einer Memory-Datei.

Geprüft wird nicht Handlung, sondern ob wiederkehrende Preview-Anker eine Feldfunktionsqualität mittragen:

- `milieu_island`
- `active_recoupling`
- `open_surface`
- `undetermined`

Die Lesung bleibt passiv.

## Datengrundlage

- Memory: `memory\2005_mixed_binding_targeted_probe.json`
- Preview-Anker gesamt: `512`
- Preview-Anker mit Feldfunktionslesung: `193`

## Klassen

- `active_recoupling`: `167`
- `milieu_island`: `23`
- `open_surface`: `3`

## Varianten

- `distributed_active_recoupling`: `123`
- `compact_carried_recoupling`: `44`
- `quiet_deep_recoupling`: `19`
- `local_milieu_seed`: `4`
- `unsettled_surface_trace`: `3`

## Weltbindung

- `realworld_bound`: `190`
- `mixed_binding`: `2`
- `field_internal_null_order`: `1`

## Bekannte Referenzrollen

- `dio_mcm_episode_05w9z7v`: `milieu_island` / `quiet_deep_recoupling`, Konfidenz `0.664993`, Depth `0.79936`, Bindung `realworld_bound` (`0.610317`), Welten `3`, Count `9`, Last `MB_TARGET_RUHIG_PAXG_REAL2024`
- `dio_mcm_episode_08g2xgt`: `milieu_island` / `quiet_deep_recoupling`, Konfidenz `0.652436`, Depth `0.850284`, Bindung `mixed_binding` (`0.634447`), Welten `4`, Count `6`, Last `MB_TARGET_RUHIG_PAXG_REAL2024`
- `dio_mcm_episode_0zkoaz0`: `active_recoupling` / `compact_carried_recoupling`, Konfidenz `0.499202`, Depth `0.569433`, Bindung `mixed_binding` (`0.553759`), Welten `2`, Count `2`, Last `WB_NULL_BTC_SHUFFLE_10K`
- `dio_mcm_episode_15jz0fg`: `milieu_island` / `quiet_deep_recoupling`, Konfidenz `0.685741`, Depth `0.817314`, Bindung `realworld_bound` (`0.616454`), Welten `3`, Count `9`, Last `MB_TARGET_RUHIG_PAXG_REAL2024`
- `dio_mcm_episode_1i07qau`: `milieu_island` / `quiet_deep_recoupling`, Konfidenz `0.691237`, Depth `0.8258`, Bindung `realworld_bound` (`0.618751`), Welten `3`, Count `3`, Last `MB_TARGET_RUHIG_PAXG_REAL2024`

## Top-Anker

- `dio_mcm_episode_0j5jlak`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.888243`, Bindung `realworld_bound`, Welten `6`, Count `10`
- `dio_mcm_episode_1k1vudq`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.888153`, Bindung `realworld_bound`, Welten `5`, Count `6`
- `dio_mcm_episode_1qmlwcr`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.874169`, Bindung `realworld_bound`, Welten `12`, Count `20`
- `dio_mcm_episode_103jy5j`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.869221`, Bindung `realworld_bound`, Welten `4`, Count `4`
- `dio_mcm_episode_1dxx3n8`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.867045`, Bindung `realworld_bound`, Welten `11`, Count `24`
- `dio_mcm_episode_08op00s`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.861975`, Bindung `realworld_bound`, Welten `17`, Count `52`
- `dio_mcm_episode_0pvq9jm`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.860662`, Bindung `realworld_bound`, Welten `5`, Count `10`
- `dio_mcm_episode_0s13pzp`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.860562`, Bindung `realworld_bound`, Welten `4`, Count `5`
- `dio_mcm_episode_07a7zoq`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.860212`, Bindung `realworld_bound`, Welten `8`, Count `21`
- `dio_mcm_episode_06eyd53`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.860179`, Bindung `realworld_bound`, Welten `8`, Count `15`
- `dio_mcm_episode_0uohah2`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.85807`, Bindung `realworld_bound`, Welten `4`, Count `52`
- `dio_mcm_episode_1avuyqc`: `active_recoupling` / `compact_carried_recoupling`, Depth `0.853125`, Bindung `realworld_bound`, Welten `8`, Count `24`

## Lesung

Die neue Memory-Lesung erzeugt keine reine Symboltabelle.
Sie zeigt, ob ein Symbol im aktuellen Mehrwelt-Kontext eher als Milieuinsel, aktive Rekopplung oder offene Oberfläche getragen wird.

Die Weltbindungsqualität ergänzt diese Lesung um Herkunft: realweltlich gebunden, nullweltlich/feldintern, synthetisch oder gemischt.
Damit bleibt die Qualität feldbezogen statt namensfixiert und Feldordnung wird nicht automatisch als Realweltbindung gelesen.
