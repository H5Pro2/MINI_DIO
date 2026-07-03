# 1395 - Holdout Feldrollen-Stabilitaet

## Zweck

Diese Diagnose prueft eine neue Holdout-Welt gegen die in `1394` gebildeten Feldrollen-Familien.

Die Diagnose bleibt passiv. Sie prueft Wiederkehr, Nachbarschaft oder neue Lage.

## Befund

- Holdout-Fenster: `60`
- Zustaende: `rolle_schwach_beruehrt:43, rolle_als_nachbarschaft:13, neue_holdout_lage:4`
- beruehrte Rollen: `weite_weltspannungsnaehe:40, offene_nachbarschaftsrolle:10, gerichtete_spannungsrolle:7, ruhige_feldnaehe:3`
- Innenwirkungen: `stabil:60`
- Welt/Zustand: `HOLDOUT_QUIET_SOL2025:rolle_schwach_beruehrt:14, HOLDOUT_2024_BRIDGE_TEST1:rolle_schwach_beruehrt:9, HOLDOUT_POSITIVE_EXPANSION:rolle_schwach_beruehrt:8, HOLDOUT_2024_BRIDGE_TEST2:rolle_schwach_beruehrt:7, HOLDOUT_QUIET_SOL2025:rolle_als_nachbarschaft:6, HOLDOUT_SMOOTH_CONTROL:rolle_schwach_beruehrt:5, HOLDOUT_SMOOTH_CONTROL:neue_holdout_lage:4, HOLDOUT_2024_BRIDGE_TEST2:rolle_als_nachbarschaft:3, HOLDOUT_POSITIVE_EXPANSION:rolle_als_nachbarschaft:2, HOLDOUT_2024_BRIDGE_TEST1:rolle_als_nachbarschaft:1, HOLDOUT_SMOOTH_CONTROL:rolle_als_nachbarschaft:1`

## Starke Wiederkehr / Nachbarschaft

- `HOLDOUT_2024_BRIDGE_TEST1:401-500` -> `gerichtete_spannungsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_2024_BRIDGE_TEST2:501-600` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_2024_BRIDGE_TEST2:601-700` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_2024_BRIDGE_TEST2:901-994` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_QUIET_SOL2025:101-200` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_QUIET_SOL2025:601-700` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_QUIET_SOL2025:701-800` -> `gerichtete_spannungsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_QUIET_SOL2025:901-1000` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_QUIET_SOL2025:1301-1400` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_QUIET_SOL2025:1401-1500` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_SMOOTH_CONTROL:301-400` -> `offene_nachbarschaftsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_POSITIVE_EXPANSION:501-600` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`
- `HOLDOUT_POSITIVE_EXPANSION:701-800` -> `gerichtete_spannungsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil`

## Lesung

Der Holdout prueft nicht, ob Mini-DIO eine alte Tabelle kopiert.
Entscheidend ist, ob neue Weltfenster in die Naehe vorhandener Feldrollen fallen.

## Wie es weitergeht

Als naechstes sollte eine ruhige Driftwelt gegen Smooth und Expansion gestellt werden. Entscheidend ist, ob ruhige Bewegung weiter bei `offene_nachbarschaftsrolle` bleibt oder langsam in Spannungsnaehe wandert.
