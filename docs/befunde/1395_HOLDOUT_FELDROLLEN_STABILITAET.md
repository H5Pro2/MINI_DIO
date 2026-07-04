# 1395 - Holdout Feldrollen-Stabilitaet

## Zweck

Diese Diagnose prueft eine neue Holdout-Welt gegen die in `1394` gebildeten Feldrollen-Familien.

Die Diagnose bleibt passiv. Sie prueft Wiederkehr, Nachbarschaft oder neue Lage.

## Befund

- Holdout-Fenster: `200`
- Zustaende: `neue_holdout_lage:103, rolle_schwach_beruehrt:79, rolle_als_nachbarschaft:18`
- beruehrte Rollen: `offene_nachbarschaftsrolle:76, ruhige_feldnaehe:61, weite_weltspannungsnaehe:52, gerichtete_spannungsrolle:11`
- Innenwirkungen: `stabil:200`
- Welt/Zustand: `HOLDOUT_QUIET_SOL2025:rolle_schwach_beruehrt:14, HOLDOUT_HIGH_FREQUENCY_SWITCH:neue_holdout_lage:10, HOLDOUT_FREQ25:neue_holdout_lage:10, HOLDOUT_FREQ50:neue_holdout_lage:10, HOLDOUT_FREQ75:neue_holdout_lage:10, HOLDOUT_FREQ100:neue_holdout_lage:10, HOLDOUT_RHYTHM_REGULAR:neue_holdout_lage:10, HOLDOUT_RHYTHM_IRREGULAR:neue_holdout_lage:10, HOLDOUT_2024_BRIDGE_TEST1:rolle_schwach_beruehrt:9, HOLDOUT_RHYTHM_WAVE:neue_holdout_lage:9, HOLDOUT_POSITIVE_EXPANSION:rolle_schwach_beruehrt:8, HOLDOUT_NOISY_DRIFT:rolle_schwach_beruehrt:8, HOLDOUT_2024_BRIDGE_TEST2:rolle_schwach_beruehrt:7, HOLDOUT_QUIET_DRIFT:rolle_schwach_beruehrt:7, HOLDOUT_QUIET_SOL2025:rolle_als_nachbarschaft:6, HOLDOUT_HIGH_NOISY_DRIFT:rolle_schwach_beruehrt:6, HOLDOUT_SMOOTH_CONTROL:rolle_schwach_beruehrt:5, HOLDOUT_MEDIUM_QUIET_DRIFT:rolle_schwach_beruehrt:5, HOLDOUT_COMBINED_STRESS:rolle_schwach_beruehrt:5, HOLDOUT_RHYTHM_BLOCK:rolle_schwach_beruehrt:5, HOLDOUT_SMOOTH_CONTROL:neue_holdout_lage:4, HOLDOUT_MEDIUM_QUIET_DRIFT:neue_holdout_lage:4, HOLDOUT_HIGH_NOISY_DRIFT:neue_holdout_lage:4, HOLDOUT_COMBINED_STRESS:neue_holdout_lage:4, HOLDOUT_2024_BRIDGE_TEST2:rolle_als_nachbarschaft:3, HOLDOUT_QUIET_DRIFT:neue_holdout_lage:3, HOLDOUT_RHYTHM_BLOCK:neue_holdout_lage:3, HOLDOUT_POSITIVE_EXPANSION:rolle_als_nachbarschaft:2, HOLDOUT_NOISY_DRIFT:neue_holdout_lage:2, HOLDOUT_RHYTHM_BLOCK:rolle_als_nachbarschaft:2, HOLDOUT_2024_BRIDGE_TEST1:rolle_als_nachbarschaft:1, HOLDOUT_SMOOTH_CONTROL:rolle_als_nachbarschaft:1, HOLDOUT_MEDIUM_QUIET_DRIFT:rolle_als_nachbarschaft:1, HOLDOUT_COMBINED_STRESS:rolle_als_nachbarschaft:1, HOLDOUT_RHYTHM_WAVE:rolle_als_nachbarschaft:1`

## Starke Wiederkehr / Nachbarschaft

- `HOLDOUT_2024_BRIDGE_TEST1:401-500` -> `gerichtete_spannungsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:66|tragend_unruhig:34`
- `HOLDOUT_2024_BRIDGE_TEST2:501-600` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:75|tragend_unruhig:24|kippend:1`
- `HOLDOUT_2024_BRIDGE_TEST2:601-700` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:77|tragend_unruhig:23`
- `HOLDOUT_2024_BRIDGE_TEST2:901-994` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:73|tragend_unruhig:20|kippend:1`
- `HOLDOUT_QUIET_SOL2025:101-200` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:71|tragend_unruhig:27|kippend:2`
- `HOLDOUT_QUIET_SOL2025:601-700` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:67|tragend_unruhig:32|gespannt:1`
- `HOLDOUT_QUIET_SOL2025:701-800` -> `gerichtete_spannungsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:79|tragend_unruhig:20|kippend:1`
- `HOLDOUT_QUIET_SOL2025:901-1000` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:69|tragend_unruhig:31`
- `HOLDOUT_QUIET_SOL2025:1301-1400` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:90|tragend_unruhig:10`
- `HOLDOUT_QUIET_SOL2025:1401-1500` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:78|tragend_unruhig:20|kippend:2`
- `HOLDOUT_SMOOTH_CONTROL:301-400` -> `offene_nachbarschaftsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:100`
- `HOLDOUT_POSITIVE_EXPANSION:501-600` -> `weite_weltspannungsnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:80|tragend_unruhig:20`
- `HOLDOUT_POSITIVE_EXPANSION:701-800` -> `gerichtete_spannungsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:72|tragend_unruhig:28`
- `HOLDOUT_MEDIUM_QUIET_DRIFT:301-400` -> `offene_nachbarschaftsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:100`
- `HOLDOUT_COMBINED_STRESS:201-300` -> `ruhige_feldnaehe` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:100`
- `HOLDOUT_RHYTHM_BLOCK:1-100` -> `offene_nachbarschaftsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:89|tragend_unruhig:11`
- `HOLDOUT_RHYTHM_BLOCK:501-600` -> `offene_nachbarschaftsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:89|tragend_unruhig:11`
- `HOLDOUT_RHYTHM_WAVE:901-994` -> `offene_nachbarschaftsrolle` / `rolle_als_nachbarschaft` / Naehe `0.600000` / Wirkung `stabil` / Mix `stabil:94`

## Lesung

Der Holdout prueft nicht, ob Mini-DIO eine alte Tabelle kopiert.
Entscheidend ist, ob neue Weltfenster in die Naehe vorhandener Feldrollen fallen.

## Wie es weitergeht

Als naechstes sollte nicht nur mehr Rauschen geprueft werden. Entscheidend ist die Kombination aus Range, Wechselrate, Tonverdichtung und Rezeptoraufnahme: dort liegt vermutlich die Schwelle, ab der stabile Oberflaechenvarianz in echte Spannungsnaehe kippt.
