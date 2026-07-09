# Lokale multisensorische Kopplung - Befund

Stand: 2026-06-19

## Kurzbefund

Die lokale multisensorische Kopplung ist lesbar.

Die Diagnose zerlegt eine Welt in kurze Abschnitte und prueft dort:

- Hoerlast,
- Sehlast,
- Felddruck,
- Entlastung,
- Sinneskonflikt,
- Rekopplung.

Damit wird sichtbar, dass eine Gesamtwelt offen oder rekoppelnd wirken kann, waehrend einzelne Abschnitte lokal deutlich naeher an Kippnaehe liegen.

## Wichtige methodische Grenze

Die Rollen werden relativ innerhalb der jeweiligen Welt gelesen.

Deshalb ist die Anzahl der lokalen Kippfenster nicht allein beweiskraeftig.
Die Klassifikation markiert bewusst die oberen lokalen Bereiche einer Welt.

Der belastbare Befund liegt in:

1. der Staerke der lokalen Kippnaehe,
2. der Wiederholung gleicher Tickbereiche in Lauf 1 und Lauf 2,
3. dem Vergleich gegen lokale Rekopplungs-/Entlastungsfenster.

## Staerkste lokale Kippnaehe

Die staerksten lokalen Kippfenster liegen vor allem in:

- `SOL_2025_1H`
- `SOL_2024_1H`
- `SOL_2025_30M`

Beispiele:

- `SOL_2025_1H`, Ticks `401-480`, Kippnaehe `0.3664`
- `SOL_2024_1H`, Ticks `1761-1840`, Kippnaehe `0.3547`
- `SOL_2025_30M`, Ticks `881-960`, Kippnaehe `0.3530`

Diese Abschnitte treten in Lauf 1 und Lauf 2 fast identisch wieder auf.

Das spricht gegen zufaelliges Einzelrauschen.
Es spricht fuer wiederkehrende lokale Innenfeldabschnitte bei gleicher Welt.

## Staerkste lokale Rekopplung

Die staerksten lokalen Entlastungs-/Rekopplungsfenster liegen klar bei:

- `SOL_2025_5M`

Beispiele:

- Ticks `1521-1600`, Entlastung `0.7214`, Rekopplung `0.647802`
- Ticks `561-640`, Entlastung `0.7204`, Rekopplung `0.643751`
- Ticks `1801-1880`, Entlastung `0.7192`, Rekopplung `0.646882`

Auch diese Bereiche reproduzieren sich ueber Lauf 1 und Lauf 2.

Das passt zum bisherigen SOL-5m-Befund:
Diese Welt ist nicht reizarm, aber sie besitzt lokale Abschnitte, die vom Feld gut rekoppelt und getragen werden.

## Fachliche Schlussfolgerung

Die lokale Ebene bestaetigt die Hierarchie:

```text
Gesamtwelt lesen
  -> lokale Abschnitte lesen
  -> wiederkehrende Kipp-/Rekopplungsinseln suchen
  -> erst danach ueber stabile Innenfeldmuster sprechen
```

Damit wird verhindert, dass eine Gesamtrolle zu grob gelesen wird.

Eine Welt kann insgesamt offen wirken, aber lokal belastende oder tragende Abschnitte besitzen.

## Bedeutung fuer MINI_DIO

MINI_DIO braucht diese lokale Lesung, weil Wahrnehmung nicht gleichmaessig ueber eine ganze Welt verteilt ist.

Organisch gelesen:

- manche Abschnitte wirken wie lokale Spannung,
- manche wie lokale Entlastung,
- manche bleiben offen,
- manche reiben zwischen Hoeren und Sehen.

Das ist ein Schritt von Weltprofil zu Innenfeldkarte.

## Kritische Einordnung

Die aktuelle lokale Diagnose ist noch eine Lupe, kein Beweis.

Besonders vorsichtig zu lesen:

- Stresssegmente sind teils kurz und daher schwer mit 2k-Welten vergleichbar.
- Die Rollenanzahl entsteht relativ zur jeweiligen Welt.
- Lokale Kippnaehe ist noch keine stabile Bedeutungsinsel.

Belastbarer ist bisher:

- gleiche starke Tickbereiche reproduzieren sich in Lauf 1 und Lauf 2,
- SOL 5m zeigt wiederholt lokale Rekopplungsfenster,
- SOL 1h/30m zeigen staerkere lokale Kippfenster.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob lokale Kipp- und Rekopplungsfenster eigene wiederkehrende Syntax/Familien tragen.

Hierarchie:

1. Grundfrage: Werden lokale multisensorische Innenlagen semantisch wiedererkannt?
2. Unterpruefung: Top-Kippfenster und Top-Rekopplungsfenster gegen `symbol`, `symbol_family` und MCM-Episodensymbole legen.
3. Folgeschritt: Nur wenn sich dort wiederkehrende Syntax zeigt, kann man von lokalen multisensorischen Bedeutungsinseln sprechen.
