# 109 - MCM-Topologie Jahres-Haertetest

## Zweck

Diese Datei prueft,
ob die passive MCM-Topologie
auch auf groesseren Datenraeumen stabil bleibt.

Ausgangspunkt:

- `108_REPRODUZIERTE_MCM_TOPOLOGIE_ROLLENKARTE.md`

Die Diagnose bleibt passiv.
Sie ist keine Handlung,
kein Gate,
kein Entry-Signal
und keine Strategie.

## Eingabe

Groessere Datenraeume:

- `data/1-12_2023_5m_SOLUSDT.csv`
- `data/1-12_2024_5m_SOLUSDT.csv`
- `data/1-12_2025_5m_SOLUSDT.csv`
- `data/1-4_2026_5m_SOLUSDT.csv`

## Ausgabe

Ordner:

- `debug/dio_mini_passive_topology_year_hardtest_worlds_20260618/`
- `debug/dio_mini_passive_target_access_dynamics_year_hardtest_20260618/`
- `debug/dio_mini_passive_target_role_map_year_hardtest_20260618/`
- `debug/dio_mini_passive_target_role_year_hardtest_compare_20260618/`

## Ergebnis auf Symbol-/Varianzebene

Gepruefte Symbol-Welt-Kombinationen:

- `28`

Innerhalb bisheriger Varianz:

- `28`

Oberhalb oder unterhalb bisheriger Varianz:

- `0`

Das bedeutet:

Die passiven Reifespuren bleiben auf grossen Jahres- und Mehrmonatsdaten
vollstaendig innerhalb der bisher beobachteten Varianz.

## Ergebnis auf Rollenebene

Gepruefte Zielraumrollen:

- `7`

Stabile Rollen:

- `6`

Rollenstabilitaet:

- `0.857143`

Stabile dominante Bewegungsqualitaeten:

- `6`

## Stabile Rollen

`dio_reifespur_po4hjv`

- bleibt: `zentrum_nahe_stabilisierung`

`dio_reifespur_rj8h9z`

- bleibt: `offene_bruecke_tragend`

`dio_reifespur_nh7ss1`

- bleibt: `offene_bruecke_tragend`

`dio_reifespur_lrfx2u`

- bleibt: `offene_bruecke_entlastend`

`dio_reifespur_ack9wa`

- bleibt: `offene_bruecke_entlastend`

`dio_reifespur_lg0qr0`

- bleibt: `selbstnah_driftend`

## Rollenverschiebung

`dio_reifespur_nu25d5`

- vorher: `spannungsrand_belastend`
- im Jahres-Haertetest: `offene_bruecke_entlastend`

Wichtig:

Das ist kein Zusammenbruch der Topologie.

`nu25d5` bleibt eine belastungsnahe Spur,
aber in grossen Datenraeumen wirkt sie nicht mehr nur als Randspannung.
Sie bekommt eine entlastende Brueckenrolle.

## MCM-Lesung

Der Haertetest zeigt zwei Ebenen:

```text
1. Die Symbol-/Bedeutungsinseln bleiben stabil.
2. Eine Rollenqualitaet kann unter groesserer Weltvarianz wandern.
```

Das ist fachlich wichtig,
weil eine lebendige MCM-Topologie nicht starr sein muss.

Stabil ist:

- Zentrum
- tragende Bruecken
- entlastende offene Bruecken
- selbstnahe Drift

Variabel ist:

- ob eine belastungsnahe Spur nur Randspannung bleibt
  oder in groesseren Welten eine entlastende Brueckenfunktion uebernimmt.

## Schluss

Der beste aktuelle Befund lautet:

```text
topology_stable_with_one_role_drift
```

Die passive MCM-Topologie wird durch den Jahres-Haertetest nicht widerlegt.

Im Gegenteil:

Sie bleibt auf Symbol-/Varianzebene voll stabil
und auf Rollenebene weitgehend stabil.

Die Abweichung bei `nu25d5` ist als Rollen-Drift
unter groesserer Weltvarianz zu lesen,
nicht als Topologie-Kollaps.

## Wie es weitergeht

Grundfrage:

Ist `nu25d5` wirklich ein driftender Rollenbereich
oder ein Uebergangsbereich zwischen Randspannung und entlastender Bruecke?

Unterpruefung:

`nu25d5` isoliert untersuchen:

- wann wirkt es als belastender Spannungsrand?
- wann wirkt es als entlastende offene Bruecke?
- welche Weltmerkmale begleiten diesen Rollenwechsel?

Folgeschritt:

Passive `nu25d5` Rollen-Drift-Lupe bauen.
