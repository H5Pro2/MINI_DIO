# 2043 - Passive Zustandsqualität der Vorwahrnehmung

## Zweck

Diese Auswertung führt die 2042-Landkarte passiv in eine Vorwahrnehmungs-Zustandsmemory zurück.

Gespeichert wird nicht, was MINI_DIO tun soll. Gespeichert wird nur, wie eine bekannte Feldnähe in Holdout-Welten wieder auftaucht: stabil, teilstabil, umorganisiert oder driftend.

## Übersicht

- Memory-Zustand: `preawareness_state_qualities_present`
- Zustände: `14`
- Detail-Zeilen aus 2042: `14`
- lokaler Speicher: `memory\preawareness\passive_preawareness_state_quality_memory.json`
- Zustandsverteilung: `{'stabil_wiederkehrend': 7, 'teilstabil_wiederkehrend': 3, 'umorganisierte_rekopplung': 2, 'verschobene_rekopplungsqualitaet': 2}`
- Feldrelationsverteilung: `{'feldrolle_identisch': 10, 'rekopplungsqualitaet_verschoben': 2, 'spannung_rekoppelt_um': 2}`
- Holdout-Assets: `{'BTC': 4, 'DOGE': 6, 'PAXG': 4}`

## Zustände

| Zustand | Gruppe | Kette | Holdout | Erwartet | Beobachtet | Relation | Rücklesung | MCM |
|---|---|---|---|---|---|---|---:|---:|
| `verschobene_rekopplungsqualitaet` | `oberflaeche_rekoppelt` | `long_btc_sol` | `btc2024/BTC` | `offene_rekopplung` | `tragende_rekopplung` | `rekopplungsqualitaet_verschoben` | 0.333/0.000/0.333 | 0.420/0.206/0.630 |
| `stabil_wiederkehrend` | `oberflaeche_rekoppelt` | `long_btc_sol` | `doge2024/DOGE` | `offene_rekopplung` | `offene_rekopplung` | `feldrolle_identisch` | 1.000/0.500/0.333 | 0.385/0.261/0.591 |
| `teilstabil_wiederkehrend` | `oberflaeche_rekoppelt` | `multiasset` | `btc2024/BTC` | `tragende_rekopplung` | `tragende_rekopplung` | `feldrolle_identisch` | 0.556/0.111/0.222 | 0.420/0.206/0.630 |
| `verschobene_rekopplungsqualitaet` | `oberflaeche_rekoppelt` | `multiasset` | `doge2024/DOGE` | `tragende_rekopplung` | `offene_rekopplung` | `rekopplungsqualitaet_verschoben` | 0.333/0.167/0.111 | 0.385/0.261/0.591 |
| `stabil_wiederkehrend` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `doge2024/DOGE` | `offene_rekopplung` | `offene_rekopplung` | `feldrolle_identisch` | 1.000/1.000/0.167 | 0.376/0.267/0.590 |
| `stabil_wiederkehrend` | `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `paxg2024/PAXG` | `offene_rekopplung` | `offene_rekopplung` | `feldrolle_identisch` | 1.000/1.000/0.000 | 0.374/0.265/0.590 |
| `stabil_wiederkehrend` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `doge2024/DOGE` | `offene_rekopplung` | `offene_rekopplung` | `feldrolle_identisch` | 1.000/1.000/0.056 | 0.376/0.267/0.590 |
| `stabil_wiederkehrend` | `oberflaeche_rekoppelt_spaet` | `multiasset` | `paxg2024/PAXG` | `offene_rekopplung` | `offene_rekopplung` | `feldrolle_identisch` | 1.000/1.000/0.111 | 0.374/0.265/0.590 |
| `stabil_wiederkehrend` | `rekopplung_oeffnet` | `long_btc_sol` | `btc2024/BTC` | `spannungsnahe_oeffnung` | `spannungsnahe_oeffnung` | `feldrolle_identisch` | 0.800/1.000/0.267 | 0.368/0.288/0.576 |
| `teilstabil_wiederkehrend` | `rekopplung_oeffnet` | `long_btc_sol` | `doge2024/DOGE` | `spannungsnahe_oeffnung` | `spannungsnahe_oeffnung` | `feldrolle_identisch` | 0.571/0.429/0.381 | 0.364/0.283/0.578 |
| `umorganisierte_rekopplung` | `rekopplung_oeffnet` | `long_btc_sol` | `paxg2024/PAXG` | `spannungsnahe_oeffnung` | `offene_rekopplung` | `spannung_rekoppelt_um` | 0.000/1.000/0.333 | 0.421/0.272/0.602 |
| `stabil_wiederkehrend` | `rekopplung_oeffnet` | `multiasset` | `btc2024/BTC` | `spannungsnahe_oeffnung` | `spannungsnahe_oeffnung` | `feldrolle_identisch` | 0.800/1.000/0.178 | 0.368/0.288/0.576 |
| `teilstabil_wiederkehrend` | `rekopplung_oeffnet` | `multiasset` | `doge2024/DOGE` | `spannungsnahe_oeffnung` | `spannungsnahe_oeffnung` | `feldrolle_identisch` | 0.571/0.429/0.063 | 0.364/0.283/0.578 |
| `umorganisierte_rekopplung` | `rekopplung_oeffnet` | `multiasset` | `paxg2024/PAXG` | `spannungsnahe_oeffnung` | `offene_rekopplung` | `spannung_rekoppelt_um` | 0.000/1.000/0.222 | 0.421/0.272/0.602 |

## Lesung

MINI_DIO bekommt damit keine neue Entscheidungslogik, sondern eine passive Erinnerung an Zustandsqualität. Eine Rolle kann also später nicht nur als bekannt gelesen werden, sondern als bekannt-stabil, bekannt-teilstabil, bekannt-umorganisiert oder bekannt-driftend.

Der wichtige Punkt ist die Trennung: Die Feldrolle bleibt Wahrnehmung und Gedächtnis. Sie wird nicht automatisch zu Handlung.

## Grenze

Diese Zustandsmemory ist keine Vorhersage, kein Signal, kein Gate, keine Richtung und kein Entry. Sie beschreibt ausschließlich die wiederholte oder veränderte Qualität einer Feldnähe.
