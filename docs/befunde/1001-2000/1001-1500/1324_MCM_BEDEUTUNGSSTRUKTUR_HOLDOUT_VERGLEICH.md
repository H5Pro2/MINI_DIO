# Vergleich MCM-Bedeutungsstruktur Basis/Holdout

Diese Diagnose vergleicht die passive Bedeutungsstruktur aus `1317` mit der Holdout-Struktur aus `1323`.

Geprueft wird:

- wiedererkannt
- erweitert
- veraendert
- nicht wieder aufgetreten

## Statusverteilung

- `feldform_wiedererkannt_faerbung_veraendert`: `2`
- `stabil_wiedererkannt`: `2`
- `neue_assetfaerbung`: `1`
- `nicht_wieder_aufgetreten`: `1`

## Vergleich

| Asset | Status | Basis-Folge | Holdout-Folge | Basis-Sinnesprofil | Holdout-Sinnesprofil |
|---|---|---|---|---|---|
| BTC | `feldform_wiedererkannt_faerbung_veraendert` | `offen_suchend->offen_suchend` | `lauter_feldkontakt->lauter_feldkontakt` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_niedrig` |
| DOGE | `stabil_wiedererkannt` | `normale_weltspannung->normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` |
| KAS | `neue_assetfaerbung` | `-` | `normale_weltspannung->normale_weltspannung` | `-` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_hoch` |
| PAXG | `feldform_wiedererkannt_faerbung_veraendert` | `ruhig_zentrumsnah->normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_niedrig` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_niedrig` |
| SOL | `stabil_wiedererkannt` | `normale_weltspannung->normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` |
| XRP | `nicht_wieder_aufgetreten` | `normale_weltspannung->normale_weltspannung` | `-` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` | `-` |

## Bewertung

Die gemeinsame Feldform bleibt im Holdout erhalten:

```text
zwischenlage_gemischte_rohwelt
```

Gleichzeitig ist die Assetfaerbung nicht starr.

Ein Teil wird stabil wiedererkannt, ein Teil veraendert die dominante Folge, und KAS erscheint als neue Assetfaerbung.

Das spricht fuer eine passive Bedeutungsstruktur, die weder alles neu erfindet noch alles festnagelt.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.
