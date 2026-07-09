# 1999_PASSIVE_WELTBINDUNG_FRESH_NULL - Passive Feldfunktions-Memory Mehrweltprüfung

## Zweck

Diese Diagnose liest die neue passive Feldfunktionsqualität aus einer Memory-Datei.

Geprüft wird nicht Handlung, sondern ob wiederkehrende Preview-Anker eine Feldfunktionsqualität mittragen:

- `milieu_island`
- `active_recoupling`
- `open_surface`
- `undetermined`

Die Lesung bleibt passiv.

## Datengrundlage

- Memory: `memory\1999_world_binding_fresh_null_probe.json`
- Preview-Anker gesamt: `76`
- Preview-Anker mit Feldfunktionslesung: `76`

## Klassen

- `milieu_island`: `40`
- `open_surface`: `24`
- `active_recoupling`: `12`

## Varianten

- `quiet_deep_recoupling`: `28`
- `unsettled_surface_trace`: `24`
- `local_milieu_seed`: `12`
- `compact_carried_recoupling`: `12`

## Weltbindung

- `field_internal_null_order`: `76`

## Bekannte Referenzrollen

- `dio_mcm_episode_0hiolzy`: `-` / `-`, Konfidenz `-`, Depth `-`, Bindung `-` (`-`), Welten `-`, Count `-`, Last `-`
- `dio_mcm_episode_1yxc2ug`: `-` / `-`, Konfidenz `-`, Depth `-`, Bindung `-` (`-`), Welten `-`, Count `-`, Last `-`
- `dio_mcm_episode_0hvxln3`: `milieu_island` / `local_milieu_seed`, Konfidenz `0.559591`, Depth `0.573987`, Bindung `field_internal_null_order` (`0.687509`), Welten `1`, Count `12`, Last `WB_FRESH_NULL_BTC_10K`
- `dio_mcm_episode_14sn1ov`: `milieu_island` / `quiet_deep_recoupling`, Konfidenz `0.711204`, Depth `0.716138`, Bindung `field_internal_null_order` (`0.725604`), Welten `1`, Count `7`, Last `WB_FRESH_NULL_BTC_10K`

## Top-Anker

- `dio_mcm_episode_05w9z7v`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.742123`, Bindung `field_internal_null_order`, Welten `1`, Count `3`
- `dio_mcm_episode_0uohah2`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.739579`, Bindung `field_internal_null_order`, Welten `1`, Count `1`
- `dio_mcm_episode_01h2hhh`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.739517`, Bindung `field_internal_null_order`, Welten `1`, Count `1`
- `dio_mcm_episode_08g2xgt`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.739493`, Bindung `field_internal_null_order`, Welten `1`, Count `3`
- `dio_mcm_episode_1xlv7yw`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.738012`, Bindung `field_internal_null_order`, Welten `1`, Count `2`
- `dio_mcm_episode_12fuh1y`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.736879`, Bindung `field_internal_null_order`, Welten `1`, Count `1`
- `dio_mcm_episode_1dnxhy9`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.732668`, Bindung `field_internal_null_order`, Welten `1`, Count `2`
- `dio_mcm_episode_15jz0fg`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.731981`, Bindung `field_internal_null_order`, Welten `1`, Count `3`
- `dio_mcm_episode_06eyd53`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.731202`, Bindung `field_internal_null_order`, Welten `1`, Count `2`
- `dio_mcm_episode_1i07qau`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.731029`, Bindung `field_internal_null_order`, Welten `1`, Count `1`
- `dio_mcm_episode_0s13pzp`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.729192`, Bindung `field_internal_null_order`, Welten `1`, Count `1`
- `dio_mcm_episode_1kvungn`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.728138`, Bindung `field_internal_null_order`, Welten `1`, Count `1`

## Lesung

Die neue Memory-Lesung erzeugt keine reine Symboltabelle.
Sie zeigt, ob ein Symbol im aktuellen Mehrwelt-Kontext eher als Milieuinsel, aktive Rekopplung oder offene Oberfläche getragen wird.

Die Weltbindungsqualität ergänzt diese Lesung um Herkunft: realweltlich gebunden, nullweltlich/feldintern, synthetisch oder gemischt.
Damit bleibt die Qualität feldbezogen statt namensfixiert und Feldordnung wird nicht automatisch als Realweltbindung gelesen.

## Wie es weitergeht

Als nächstes sollten Realwelt- und Nullweltläufe mit frischer Memory getrennt geprüft werden. Entscheidend ist, ob die Feldfunktion ähnlich entstehen darf, die Weltbindungsqualität aber sauber unterscheidet.
