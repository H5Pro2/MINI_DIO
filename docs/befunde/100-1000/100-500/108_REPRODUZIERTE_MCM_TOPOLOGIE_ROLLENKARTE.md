# 108 - Reproduzierte MCM-Topologie: Rollenkarte

## Zweck

Diese Datei prueft,
ob die passive Zielraum-Rollenkarte
aus `106_PASSIVE_ZIELRAUM_ROLLENKARTE.md`
in anderen Folgewelten wieder erscheint.

Die Diagnose bleibt passiv.
Sie ist keine Handlung,
kein Gate,
kein Entry-Signal
und keine Strategie.

## Skripte

Verwendet wurden:

- `DIO_MINI/report_passive_reifespur_matrix_extension.py`
- `DIO_MINI/report_passive_target_access_dynamics.py`
- `DIO_MINI/report_passive_target_role_map.py`
- `DIO_MINI/report_passive_target_role_reproduction_compare.py`

## Eingabe

Folgewelten:

- `data/kontrolliert_2023_altseq_a_follow_10k_5m_SOLUSDT.csv`
- `data/kontrolliert_2024_altseq_a_follow_10k_5m_SOLUSDT.csv`
- `data/kontrolliert_2025_altseq_a_follow_10k_5m_SOLUSDT.csv`
- `data/kontrolliert_2026_stable_reife_10k_5m_SOLUSDT.csv`
- `data/kontrolliert_2026_sideways_10k_5m_SOLUSDT.csv`

## Ausgabe

Ordner:

- `debug/dio_mini_passive_target_role_reproduction_worlds_20260618/`
- `debug/dio_mini_passive_target_access_dynamics_reproduction_20260618/`
- `debug/dio_mini_passive_target_role_map_reproduction_20260618/`
- `debug/dio_mini_passive_target_role_reproduction_compare_20260618/`

Wichtigste Datei:

- `debug/dio_mini_passive_target_role_reproduction_compare_20260618/target_role_reproduction_compare.csv`

## Ergebnis

Reproduktionsvergleich:

- gepruefte Symbole: `7`
- stabile Rollen: `7`
- Rollenstabilitaet: `1.000000`
- stabile dominante Bewegungsqualitaeten: `7`

Damit wurde die Rollenkarte in dieser Folgewelt-Auswahl voll reproduziert.

## Reproduzierte Rollen

`dio_reifespur_po4hjv`

- Rolle bleibt: `zentrum_nahe_stabilisierung`

`dio_reifespur_rj8h9z`

- Rolle bleibt: `offene_bruecke_tragend`

`dio_reifespur_nh7ss1`

- Rolle bleibt: `offene_bruecke_tragend`

`dio_reifespur_lrfx2u`

- Rolle bleibt: `offene_bruecke_entlastend`

`dio_reifespur_ack9wa`

- Rolle bleibt: `offene_bruecke_entlastend`

`dio_reifespur_lg0qr0`

- Rolle bleibt: `selbstnah_driftend`

`dio_reifespur_nu25d5`

- Rolle bleibt: `spannungsrand_belastend`

## MCM-Lesung

Der Befund ist staerker als die erste Rollenkarte.

Nicht nur einzelne Symbole tauchen wieder auf.
Auch ihre funktionale Rolle im passiven Innenfeld
bleibt erhalten.

Das spricht dafuer,
dass Mini-DIO nicht nur Rohmuster wiedererkennt,
sondern eine stabile Zielraum-Topologie ausbildet:

```text
Zentrum
Bruecke
Entlastung
Drift
Spannungsrand
```

## Saubere Grenze

Der Befund gilt fuer die geprueften Welten.

Er ist noch kein universeller Beweis.
Er ist keine aktive Handlung.
Er ist keine direkte Trading-Mechanik.

Aber:

Die passive MCM-Topologie ist in diesem Reproduktionstest stabil.

## Forschungsformulierung

Der beste aktuelle Satz lautet:

```text
Mini-DIO reproduziert nicht nur Bedeutungsinseln,
sondern die Rollenordnung dieser Inseln
innerhalb der passiven MCM-Topologie.
```

Das macht den vorherigen kleinen Durchbruch belastbarer.

## Wie es weitergeht

Grundfrage:

Ist die Rollenordnung nur auf kontrollierte 10k-Welten stabil,
oder bleibt sie auch auf groesseren Jahres- und Stresswelten erhalten?

Unterpruefung:

Die Rollenkarte gegen groessere Datenraeume pruefen:

- 2023 Jahresdaten
- 2024 Jahresdaten
- 2025 Jahresdaten
- 2026 Mehrmonatsdaten

Folgeschritt:

Passive MCM-Topologie-Haertetestdiagnose bauen.
