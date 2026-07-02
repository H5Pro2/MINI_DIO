# Vergleich MCM-Bedeutungsstruktur Basis/Holdout

Diese Diagnose vergleicht `1317_MCM_BEDEUTUNGSSTRUKTUR_MEMORY.csv` mit `1338_CONTRAST_HOLDOUT_MCM_BEDEUTUNGSSTRUKTUR_MEMORY.csv`.

Geprueft wird:

- wiedererkannt
- erweitert
- veraendert
- nicht wieder aufgetreten

## Statusverteilung

- `feldform_wiedererkannt_faerbung_veraendert`: `3`
- `stabil_wiedererkannt`: `2`

## Vergleich

| Asset | Status | Basis-Folge | Holdout-Folge | Basis-Sinnesprofil | Holdout-Sinnesprofil |
|---|---|---|---|---|---|
| BTC | `feldform_wiedererkannt_faerbung_veraendert` | `offen_suchend->offen_suchend` | `normale_weltspannung->normale_weltspannung` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` |
| DOGE | `feldform_wiedererkannt_faerbung_veraendert` | `normale_weltspannung->normale_weltspannung` | `offen_suchend->offen_suchend` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` |
| PAXG | `feldform_wiedererkannt_faerbung_veraendert` | `ruhig_zentrumsnah->normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_niedrig` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_niedrig` |
| SOL | `stabil_wiedererkannt` | `normale_weltspannung->normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` |
| XRP | `stabil_wiedererkannt` | `normale_weltspannung->normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` |

## Bewertung

Die gemeinsame Feldform bleibt im Holdout erhalten:

```text
zwischenlage_gemischte_rohwelt
```

Gleichzeitig ist die Assetfaerbung nicht starr.

Ein Teil wird stabil wiedererkannt, ein Teil veraendert die dominante Folge, und neue Assetfaerbungen koennen erscheinen.

Das spricht fuer eine passive Bedeutungsstruktur, die weder alles neu erfindet noch alles festnagelt.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.

Wie es weitergeht: Als naechstes sollte die Veraenderung der Faerbung untersucht werden: Welche Rohweltmerkmale verschieben einzelne Assets gegenueber der Basisstruktur?
