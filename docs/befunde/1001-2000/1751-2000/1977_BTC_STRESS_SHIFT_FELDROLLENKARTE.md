# 1977 - BTC-Stress/Shift-Feldrollenkarte

## Grundfrage

Wenn `1i3ov0z` nicht die Stress-/Shift-Rolle ist, welche Feldrollen übernehmen dort die Führung?

## Unterprüfung

Die fünf BTC-Stress-/Shift-Läufe aus `preview_depth_1i3ov0z_btc_stress_shift_probe` wurden pro Weltfenster aus den Episoden rückgelesen:

- `BTC_STRESS_2024_5M`
- `BTC_STRESS_2025_5M`
- `BTC_SHIFT_2025_15M_16000_17000`
- `BTC_SHIFT_2025_30M_10000_11000`
- `BTC_SHIFT_2025_1H_4000_5000`

Ausgewertet wurden:

- dominante Preview-Rollen
- dominante Familien
- Tiefenstatus
- Rekopplung, Carry, Strain, Sensorik
- Rohphasenlesung der führenden Rollen

## Ergebnis

### Stress-Kernrolle: `dio_mcm_episode_0icnf2v`

`0icnf2v` ist die stärkste Stressrolle:

- Gesamtvorkommen: `4749`
- Weltanzahl: `4`
- Hauptwelten:
  - `BTC_STRESS_2024_5M`: `2620`
  - `BTC_STRESS_2025_5M`: `2023`
  - `BTC_SHIFT_2025_30M_10000_11000`: `91`
  - `BTC_SHIFT_2025_1H_4000_5000`: `15`
- Tiefenwert: `0.827388`
- Profilnähe: `0.770198`
- Rohphase: `ruhig_getragene_nahe`

Das wirkt zunächst paradox, ist aber fachlich plausibel: Stress wird nicht als chaotischer Rand gelesen, sondern bildet eine getragene Innenfeldrolle, sobald das Feld ihn stabil verarbeitet.

### Shift-/Übergangsrolle: `dio_mcm_episode_1rj8742`

`1rj8742` ist die stärkste Shift-nahe Rolle:

- Gesamtvorkommen: `2411`
- Weltanzahl: `5`
- Hauptwelten:
  - `BTC_STRESS_2025_5M`: `870`
  - `BTC_SHIFT_2025_1H_4000_5000`: `545`
  - `BTC_SHIFT_2025_30M_10000_11000`: `498`
  - `BTC_SHIFT_2025_15M_16000_17000`: `435`
  - `BTC_STRESS_2024_5M`: `63`
- Tiefenwert: `0.727689`
- Profilnähe: `0.705377`
- Rohphase: `ruhig_getragene_nahe`

Diese Rolle verbindet Stress und Shift stärker als `0icnf2v`. Sie wirkt daher wie eine Übergangsrolle zwischen belasteterer und verschobener BTC-Weltlage.

### Zentrumsnahe Brückenrollen

Zwei Rollen bilden eher zentrumsnahe Brücken:

- `dio_mcm_episode_0wo0tz1`
  - Vorkommen: `1259`
  - Weltanzahl: `5`
  - Rohphase: `zentrumsnah_getragen`

- `dio_mcm_episode_1qlxgj7`
  - Vorkommen: `719`
  - Weltanzahl: `5`
  - Rohphase: `zentrumsnah_getragen`

Diese Rollen sind weniger Milieu-Kern als verbindende Innenfeldformen. Sie erscheinen in Stress und Shift, aber nicht so eindeutig spezialisiert wie `0icnf2v` und `1rj8742`.

## Vergleich zu `1i3ov0z`

`1i3ov0z` blieb in derselben Prüfung fast vollständig BTC-Quiet-nah:

- BTC-Quiet-Zählung: `1822`
- BTC-Stress/Shift-Zählung: `3`

Damit entsteht eine klare Rollenabgrenzung:

- `1i3ov0z`: ruhige BTC-Milieurolle
- `0icnf2v`: BTC-Stresskernrolle
- `1rj8742`: BTC-Shift-/Übergangsrolle
- `0wo0tz1` / `1qlxgj7`: zentrumsnahe Brückenrollen

## Befund

MINI_DIO presst Stress und Shift nicht einfach in die bereits gefundene Quiet-Rolle. Stattdessen entstehen andere Rollen mit anderer Verteilung.

Das ist wichtig für die MCM-Feldmechanik:

- ruhige Weltlage bildet eine eigene Rolle
- Stress bildet eine eigene, aber getragene Rolle
- Shift bildet eine Übergangsrolle
- Brückenrollen verbinden mehrere Weltlagen

Damit sieht die MCM-Ordnung nicht wie eine flache Symboltabelle aus, sondern wie ein Rollenraum.

## Grenze

Diese Rollen sind passive Bedeutungsrollen. Sie sind keine Handlungssignale, keine Strategie und keine Aussage über Marktverhalten.
