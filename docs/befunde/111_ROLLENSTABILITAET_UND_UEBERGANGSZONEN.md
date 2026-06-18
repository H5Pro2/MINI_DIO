# 111 - Rollenstabilitaet und Uebergangszonen

## Zweck

Diese Datei vergleicht die Zielraumrollen
ueber drei Pruefstufen:

1. Basis-10k-Welten
2. Folgewelten
3. Jahres-Haertetest

Ziel ist,
stabile Zielraeume von Uebergangszonen zu trennen.

Die Diagnose bleibt passiv.
Sie ist keine Handlung,
kein Gate,
kein Entry-Signal
und keine Strategie.

## Skript

`DIO_MINI/report_passive_role_stability_transition_map.py`

## Eingabe

Verglichen wurden:

- `debug/dio_mini_passive_target_role_map_20260618/target_role_map.csv`
- `debug/dio_mini_passive_target_role_map_reproduction_20260618/target_role_map.csv`
- `debug/dio_mini_passive_target_role_map_year_hardtest_20260618/target_role_map.csv`

## Ausgabe

Ordner:

`debug/dio_mini_passive_role_stability_transition_map_20260618/`

Dateien:

- `role_stability_transition_map.csv`
- `role_stability_transition_map_summary.json`

## Ergebnis

Gepruefte Zielraeume:

- `7`

Stabile Rollen:

- `6`

Uebergangszonen:

- `1`

Stabilitaetsklassen:

- `stabile_rolle`: `6`
- `jahresdrift_rolle`: `1`

Uebergangshinweise:

- `kein_uebergangsverdacht`: `6`
- `spannung_zu_bruecke_uebergang`: `1`

## Stabile Rollen

`dio_reifespur_po4hjv`

- stabil: `zentrum_nahe_stabilisierung`
- Qualitaet stabil: `tragend_steigend`

`dio_reifespur_rj8h9z`

- stabil: `offene_bruecke_tragend`
- Qualitaet stabil: `tragend_steigend`

`dio_reifespur_nh7ss1`

- stabil: `offene_bruecke_tragend`
- Qualitaet stabil: `tragend_steigend`

`dio_reifespur_lrfx2u`

- stabil: `offene_bruecke_entlastend`
- Qualitaet stabil: `tragend_fallend`

`dio_reifespur_ack9wa`

- stabil: `offene_bruecke_entlastend`
- Qualitaet stabil: `tragend_fallend`

`dio_reifespur_lg0qr0`

- stabil: `selbstnah_driftend`
- Qualitaet stabil: `tragend_fallend`

## Uebergangszone

`dio_reifespur_nu25d5`

Basis:

- Rolle: `spannungsrand_belastend`
- Qualitaet: `belastend`

Folgewelten:

- Rolle: `spannungsrand_belastend`
- Qualitaet: `belastend`

Jahres-Haertetest:

- Rolle: `offene_bruecke_entlastend`
- Qualitaet: `tragend_fallend`

Lesung:

```text
spannung_zu_bruecke_uebergang
```

## MCM-Lesung

Die MCM-Topologie wirkt nicht beliebig.

Sie zeigt:

- stabile Zentren
- stabile Bruecken
- stabile Driftbereiche
- eine erkennbare Uebergangszone

Das ist wichtig:

Eine lebendige MCM-Topologie darf nicht komplett starr sein.
Stabilitaet und Uebergang muessen gemeinsam vorkommen.

`nu25d5` wirkt hier wie ein Grenzbereich,
der unter groesserer Weltvarianz
von Randspannung in entlastende Brueckenfunktion kippen kann.

## Schluss

Der beste aktuelle Befund lautet:

```text
topology_has_stable_roles_and_one_transition_zone
```

Damit wird die passive MCM-Topologie weiter belastbarer:

- die meisten Rollen bleiben stabil
- eine Rolle zeigt kontrollierte Drift
- die Drift ist gerichtet lesbar
  und nicht chaotisch

## Wie es weitergeht

Grundfrage:

Hat die Uebergangszone `nu25d5`
eine eigene Schwelle im Feld,
an der Randspannung in Brueckenfunktion kippt?

Unterpruefung:

Die `nu25d5`-Kippbereiche in den Jahresdaten lokalisieren:

- vor dem Kippen
- im Kippbereich
- nach dem Kippen

Folgeschritt:

Passive `nu25d5` Kippzonen-Zeitlupe bauen.
