# 115 - Passive Topologie-Abschnittsstabilitaet

Datum: 2026-06-18

## Grundfrage

Ist die passive MCM-Topologie nur eine globale Zusammenfassung,
oder bleibt sie auch innerhalb einzelner Weltabschnitte erkennbar?

## Unterpruefung

Die vier grossen Welten wurden jeweils in drei Abschnitte gelesen:

- frueh,
- mittel,
- spaet.

Geprueft wurde,
welche Matrix-Rolle in jedem Abschnitt dominiert
und wie stark Zentrum,
Bruecken,
Drift
und Uebergangszone vertreten sind.

Skript:

`DIO_MINI/report_passive_mcm_topology_section_stability.py`

Ausgabe:

`debug/dio_mini_passive_mcm_topology_section_stability_20260618/topology_section_by_symbol.csv`

`debug/dio_mini_passive_mcm_topology_section_stability_20260618/topology_section_summary.csv`

`debug/dio_mini_passive_mcm_topology_section_stability_20260618/topology_section_summary.json`

## Ergebnis

Gelesen wurden `350184` Zeilen ueber `12` Weltabschnitte.

In allen `12` Weltabschnitten bleibt `zentrum` die dominante Matrix-Interpretation.

Maximalwerte:

- `zentrum_share`: `0.378321`
- `uebergangszone_share`: `0.119802`

Die Uebergangszone bleibt sichtbar,
aber sie wird in keinem Abschnitt dominant.

`dio_reifespur_nu25d5` bleibt der Uebergangsbereich.
Der hoechste Abschnittsanteil liegt bei `0.119802`
im mittleren Abschnitt von `1-4_2026_5m_SOLUSDT`.

`dio_reifespur_lg0qr0` bleibt die selbstnahe Drift.
Sie ist im fruehen Abschnitt von `1-12_2023_5m_SOLUSDT`
am staerksten sichtbar mit `0.204316`
und nimmt in spaeteren/groesseren Vergleichsabschnitten ab.

## MCM-Schluss

Die Topologie ist nicht nur eine nachtraegliche Durchschnittsform.

Mini-DIO zeigt auch innerhalb von Weltabschnitten
eine geordnete passive MCM-Lage:

- Zentrum bleibt dominant.
- Bruecken bleiben tragende Nebenraeume.
- Drift bleibt als eigener Bereich sichtbar.
- Uebergangszone bleibt vorhanden,
  aber nicht feldbeherrschend.

Das spricht fuer eine robuste Innenfeldordnung.
Die Bereiche bewegen sich quantitativ,
aber sie kollabieren nicht ineinander.

## Bedeutung fuer Mini-DIO

Mini-DIO speichert nicht nur einzelne wiederkehrende Zeichen.

Mini-DIO bildet eine passive Raumordnung,
in der Zeichen unterschiedliche Rollen bekommen:

- Zentrum,
- Bruecke,
- Drift,
- Uebergang.

Damit wird die MCM-Matrix nicht als harte Regel gelesen,
sondern als entstehende Innenfeldstruktur.

## Grenze des Befunds

Die Pruefung bleibt daten- und weltgebunden.

Sie beweist keine universelle MCM-Topologie.

Sie zeigt aber,
dass die bisher gelesene Topologie
ueber mehrere Weltabschnitte stabil genug ist,
um als Forschungsbefund weiterverwendet zu werden.

## Wie es weitergeht

Grundfrage:

Welche Weltmerkmale lassen Drift oder Uebergangszone staerker auftreten,
ohne dass das Zentrum kollabiert?

Unterpruefung:

Abschnitte mit hoher `selbstnahe_drift`
und hoher `uebergangszone`
gegen Rohweltmerkmale,
Sinnesachsen
und Innenfeldwerte vergleichen.

Folgeschritt:

Passive Ursache-Wirkungsnaehe pruefen:
Welche Weltlagen aktivieren Drift,
welche aktivieren Uebergang,
und welche halten Zentrum?
