# 113 - Passive Uebergangsqualitaet in der Landkarte

## Zweck

Diese Datei fuehrt eine passive `uebergangsqualitaet`
in die Mini-DIO-Landkarte ein.

Ausgangspunkt:

- `112_NU25D5_KIPPZONEN_ZEITLUPE.md`

Die Diagnose bleibt passiv.
Sie ist keine Handlung,
kein Gate,
kein Entry-Signal
und keine Strategie.

## Skript

`DIO_MINI/report_passive_transition_quality_landkarte.py`

## Eingabe

`debug/dio_mini_passive_topology_year_hardtest_worlds_20260618/`

## Ausgabe

Ordner:

`debug/dio_mini_passive_transition_quality_landkarte_20260618/`

Dateien:

- `transition_quality_landkarte_rows_sample.csv`
- `transition_quality_by_world.csv`
- `transition_quality_by_symbol.csv`
- `transition_quality_landkarte_summary.json`

## Uebergangsqualitaeten

Die passive Landkarte unterscheidet:

- `stabil`
- `brueckenfaehig`
- `randspannungsnah`
- `weich_kippend`
- `uebergang_entlastend`
- `uebergang_belastend`
- `offen_gemischt`

Diese Begriffe sind keine Regeln.
Sie beschreiben nur,
wie ein Feldbereich passiv gelesen wird.

## Gesamtergebnis

Gepruefte Zeilen:

- `350184`

Dominante Uebergangsqualitaet:

- `brueckenfaehig`

Verteilung:

- `brueckenfaehig`: `0.737766`
- `offen_gemischt`: `0.159913`
- `randspannungsnah`: `0.037946`
- `uebergang_belastend`: `0.021829`
- `uebergang_entlastend`: `0.021240`
- `weich_kippend`: `0.021240`
- `stabil`: `0.000066`

## Weltvergleich

Alle vier grossen Welten bleiben dominant `brueckenfaehig`.

`2023` zeigt mehr Randspannung und mehr offene Gemischtheit.

`2025` zeigt die hoechste Brueckenfaehigkeit:

- `2023`: `0.710938`
- `2024`: `0.734398`
- `2025`: `0.768727`
- `2026`: `0.735459`

## Symbolvergleich

`nu25d5` ist der wichtigste Befund:

- `brueckenfaehig`: `0.489511`
- `offen_gemischt`: `0.308420`
- `weich_kippend`: `0.094417`
- `randspannungsnah`: `0.043158`
- `uebergang_belastend`: `0.040220`

Damit hat `nu25d5`
die deutlich staerkste weiche Kippqualitaet
unter den geprueften Symbolen.

Weitere auffaellige Rollen:

`lrfx2u`

- sehr stark `brueckenfaehig`: `0.926808`
- sehr wenig offen gemischt: `0.041722`

`lg0qr0`

- stark `brueckenfaehig`: `0.825548`
- relativ wenig randspannungsnah: `0.014755`

`ack9wa`

- brueckenfaehig: `0.684921`
- offen gemischt: `0.229786`

## MCM-Lesung

Die Uebergangsqualitaet bestaetigt die Rollenkarte.

Die weiche Kippqualitaet verteilt sich nicht zufaellig.
Sie konzentriert sich am staerksten bei `nu25d5`,
also genau bei der Spur,
die bereits als Uebergangszone erkannt wurde.

Das bedeutet:

```text
Rollen-Drift
und passive Uebergangsqualitaet
zeigen auf denselben Feldbereich.
```

Das ist ein wichtiger Konsistenzbefund.

## Schluss

Der beste aktuelle Befund lautet:

```text
transition_quality_confirms_nu25d5_transition_zone
```

Mini-DIO kann eine weiche Uebergangsqualitaet
als passive Innenfeldqualitaet lesen,
ohne daraus Handlung abzuleiten.

Damit wird die MCM-Topologie um eine weitere Ebene erweitert:

```text
Zielraum
+ Rolle
+ Zugangsdynamik
+ Uebergangsqualitaet
```

## Wie es weitergeht

Grundfrage:

Kann Mini-DIO aus Zielraum, Rolle, Zugangsdynamik
und Uebergangsqualitaet
eine kompakte passive Topologie-Matrix bilden?

Unterpruefung:

Alle bisherigen Ebenen zusammenfuehren:

- Zielraumrolle
- Rollenstabilitaet
- Uebergangshinweis
- Uebergangsqualitaet
- Symbolanteile

Folgeschritt:

Passive MCM-Topologie-Matrix konsolidieren.
