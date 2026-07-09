# Passive MCM-Bedeutungsstruktur

Diese Datei verdichtet den balancierten Zwischenlagenbefund in eine passive Bedeutungsstruktur.

Getrennt gespeichert werden:

- Feldform
- Assetfaerbung
- dominante Lagefolge
- Rohweltprofil
- mehrskaliges Profil
- Sinnesprofil

Die Struktur ist passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.

## Feldformen

- `zwischenlage_gemischte_rohwelt`

## Bedeutungszeilen

| Bedeutung | Feldform | Faerbung | Folge | Rohprofil | Sinnesprofil | Fenster |
|---|---|---|---|---|---|---:|
| `mcm_meaning_zwischenlage_gemischte_rohwelt_btc` | `zwischenlage_gemischte_rohwelt` | `btc_lauter_feldkontakt_zu_lauter_feldkontakt` | `lauter_feldkontakt->lauter_feldkontakt` | `gemischte_rohwelt` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_niedrig` | 26 |
| `mcm_meaning_zwischenlage_gemischte_rohwelt_doge` | `zwischenlage_gemischte_rohwelt` | `doge_normale_weltspannung_zu_normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` | 26 |
| `mcm_meaning_zwischenlage_gemischte_rohwelt_kas` | `zwischenlage_gemischte_rohwelt` | `kas_normale_weltspannung_zu_normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_hoch` | 26 |
| `mcm_meaning_zwischenlage_gemischte_rohwelt_paxg` | `zwischenlage_gemischte_rohwelt` | `paxg_normale_weltspannung_zu_normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_niedrig` | 26 |
| `mcm_meaning_zwischenlage_gemischte_rohwelt_sol` | `zwischenlage_gemischte_rohwelt` | `sol_normale_weltspannung_zu_normale_weltspannung` | `normale_weltspannung->normale_weltspannung` | `gemischte_rohwelt` | `hoeren_mittel|sehen_mittel|felddruck_mittel|range_mittel` | 26 |

## Bewertung

Die Zwischenlage wird nicht als ein einzelner Rohwert gespeichert.

Sie wird als zusammengesetzte Bedeutung gehalten:

```text
Feldform + Assetfaerbung + Folge + Rohprofil + Sinnesprofil
```

Damit kann MINI_DIO eine gemeinsame Feldbedeutung halten, ohne die Weltoberflaeche zu verlieren.

Wie es weitergeht: Als naechstes sollte geprueft werden, ob diese Bedeutungsstruktur bei neuen Weltfenstern wiedererkannt oder erweitert wird.
