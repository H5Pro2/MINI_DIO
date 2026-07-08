# 1843 - MCM-Feldrollen-Memory: 2025-Offset-Nullkontrolle

## Grundfrage

Bleibt der Realwelt-Vorsprung sichtbar, wenn BTC und SOL nicht am Jahresanfang, sondern ab Zeile 17.000 gelesen werden?

## Gruppenvergleich

| Gruppe | Welten | Kernfamilien Ø | Quellennähe Ø | Kernnähe Ø | Nachhall-Delta Ø | Feldzeit-Delta Ø | Zustände |
|---|---:|---:|---:|---:|---:|---:|---|
| `real` | 2 | 10.50 | 0.714 | 0.313 | 0.1675 | 0.0841 | `reifungsrolle_teilweise_reproduziert:2` |
| `null_random` | 2 | 8.50 | 0.732 | 0.235 | 0.1656 | 0.0831 | `reifungsrolle_teilweise_reproduziert:2` |
| `null_shuffle` | 2 | 9.00 | 0.680 | 0.207 | 0.1575 | 0.0791 | `reifungsrolle_teilweise_reproduziert:2` |

## Einzelwelten

| Welt | Art | Kern | Quellennähe | Kernnähe | Nachhall-Delta | Feldzeit-Delta | Lesung |
|---|---|---:|---:|---:|---:|---:|---|
| BTC offset17000_random_17k | `null_random` | 10 | 0.714 | 0.269 | 0.1725 | 0.0863 | `reifungsrolle_teilweise_reproduziert` |
| BTC offset17000_real_17k | `real` | 9 | 0.714 | 0.280 | 0.1704 | 0.0853 | `reifungsrolle_teilweise_reproduziert` |
| BTC offset17000_shuffle_17k | `null_shuffle` | 11 | 0.680 | 0.259 | 0.1577 | 0.0793 | `reifungsrolle_teilweise_reproduziert` |
| SOL offset17000_random_17k | `null_random` | 7 | 0.750 | 0.200 | 0.1588 | 0.0800 | `reifungsrolle_teilweise_reproduziert` |
| SOL offset17000_real_17k | `real` | 12 | 0.714 | 0.346 | 0.1646 | 0.0830 | `reifungsrolle_teilweise_reproduziert` |
| SOL offset17000_shuffle_17k | `null_shuffle` | 7 | 0.680 | 0.154 | 0.1573 | 0.0789 | `reifungsrolle_teilweise_reproduziert` |

## Befund

- Offset-Realwelten liegen in Quellennähe um `-0.018` über der stärksten Nullgruppe.
- Offset-Realwelten liegen in Kernnähe um `0.078` über der stärksten Nullgruppe.
- Der Test ist kleiner als 1842, weil hier nur BTC und SOL als lange 2025-Jahresdateien verfügbar waren.
- Der Realwelt-Vorsprung bleibt nicht einfach identisch; er muss je Fenster geprüft werden.

Damit ist die bisherige Lesung vorsichtiger zu formulieren:
Die Reifungsbahn bleibt sichtbar, aber die Trennung Realwelt/Nullwelt ist eine graduelle Feldqualität, kein harter Schnitt.

## Wie es weitergeht

Als nächstes sollte keine neue Mechanik eingebaut werden.
Sinnvoll ist eine kompakte Gesamtübersicht aus 1841 bis 1843: was reproduziert, was nur graduell ist, und welche Aussage wissenschaftlich haltbar bleibt.
