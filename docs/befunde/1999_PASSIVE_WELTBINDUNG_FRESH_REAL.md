# 1999_PASSIVE_WELTBINDUNG_FRESH_REAL - Passive Feldfunktions-Memory Mehrweltprüfung

## Zweck

Diese Diagnose liest die neue passive Feldfunktionsqualität aus einer Memory-Datei.

Geprüft wird nicht Handlung, sondern ob wiederkehrende Preview-Anker eine Feldfunktionsqualität mittragen:

- `milieu_island`
- `active_recoupling`
- `open_surface`
- `undetermined`

Die Lesung bleibt passiv.

## Datengrundlage

- Memory: `memory\1999_world_binding_fresh_real_probe.json`
- Preview-Anker gesamt: `79`
- Preview-Anker mit Feldfunktionslesung: `79`

## Klassen

- `milieu_island`: `43`
- `open_surface`: `24`
- `active_recoupling`: `12`

## Varianten

- `quiet_deep_recoupling`: `27`
- `unsettled_surface_trace`: `24`
- `local_milieu_seed`: `16`
- `compact_carried_recoupling`: `12`

## Weltbindung

- `realworld_bound`: `79`

## Bekannte Referenzrollen

- `dio_mcm_episode_0hiolzy`: `-` / `-`, Konfidenz `-`, Depth `-`, Bindung `-` (`-`), Welten `-`, Count `-`, Last `-`
- `dio_mcm_episode_1yxc2ug`: `milieu_island` / `local_milieu_seed`, Konfidenz `0.519171`, Depth `0.524606`, Bindung `realworld_bound` (`0.647113`), Welten `1`, Count `31`, Last `WB_FRESH_REAL_BTC_10K`
- `dio_mcm_episode_0hvxln3`: `milieu_island` / `local_milieu_seed`, Konfidenz `0.511581`, Depth `0.533431`, Bindung `realworld_bound` (`0.647639`), Welten `1`, Count `6`, Last `WB_FRESH_REAL_BTC_10K`
- `dio_mcm_episode_14sn1ov`: `milieu_island` / `local_milieu_seed`, Konfidenz `0.521153`, Depth `0.53588`, Bindung `realworld_bound` (`0.64942`), Welten `1`, Count `14`, Last `WB_FRESH_REAL_BTC_10K`

## Top-Anker

- `dio_mcm_episode_1k1vudq`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.743068`, Bindung `realworld_bound`, Welten `1`, Count `1`
- `dio_mcm_episode_1dxx3n8`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.740047`, Bindung `realworld_bound`, Welten `1`, Count `3`
- `dio_mcm_episode_1amcian`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.73554`, Bindung `realworld_bound`, Welten `1`, Count `1`
- `dio_mcm_episode_0o47ti3`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.735332`, Bindung `realworld_bound`, Welten `1`, Count `1`
- `dio_mcm_episode_07a7zoq`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.733516`, Bindung `realworld_bound`, Welten `1`, Count `5`
- `dio_mcm_episode_14pd6eb`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.732376`, Bindung `realworld_bound`, Welten `1`, Count `3`
- `dio_mcm_episode_0y7hhur`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.73226`, Bindung `realworld_bound`, Welten `1`, Count `4`
- `dio_mcm_episode_1avuyqc`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.729843`, Bindung `realworld_bound`, Welten `1`, Count `3`
- `dio_mcm_episode_159zeqh`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.729117`, Bindung `realworld_bound`, Welten `1`, Count `1`
- `dio_mcm_episode_0bygq81`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.726291`, Bindung `realworld_bound`, Welten `1`, Count `3`
- `dio_mcm_episode_103jy5j`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.725809`, Bindung `realworld_bound`, Welten `1`, Count `1`
- `dio_mcm_episode_05upp98`: `milieu_island` / `quiet_deep_recoupling`, Depth `0.723162`, Bindung `realworld_bound`, Welten `1`, Count `3`

## Lesung

Die neue Memory-Lesung erzeugt keine reine Symboltabelle.
Sie zeigt, ob ein Symbol im aktuellen Mehrwelt-Kontext eher als Milieuinsel, aktive Rekopplung oder offene Oberfläche getragen wird.

Die Weltbindungsqualität ergänzt diese Lesung um Herkunft: realweltlich gebunden, nullweltlich/feldintern, synthetisch oder gemischt.
Damit bleibt die Qualität feldbezogen statt namensfixiert und Feldordnung wird nicht automatisch als Realweltbindung gelesen.

## Wie es weitergeht

Als nächstes sollten Realwelt- und Nullweltläufe mit frischer Memory getrennt geprüft werden. Entscheidend ist, ob die Feldfunktion ähnlich entstehen darf, die Weltbindungsqualität aber sauber unterscheidet.
