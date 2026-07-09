# 1748 - DOGE/XRP 2025 Übergangsphase-Suche

Stand: 2026-07-08

## Zweck

Nach der DOGE/XRP-2024-Gegenprobe sollte geprüft werden, ob die zuvor bei SOL 2025 sichtbare `mittlere_uebergangsphase` auch in anderen 2025-Assetfenstern auftaucht.

Die Prüfung bleibt passiv:

- keine Handlung,
- kein Gate,
- keine Strategie,
- keine Richtungsvorgabe.

## Geprüfte Welten

| Welt | Datenfenster | Lesart |
|---|---|---|
| `REAL_DRIFT_DOGE_2025_A` | DOGE 2025, Startfenster 5000 Zeilen | Startwelt |
| `REAL_DRIFT_DOGE_2025_FOLLOW` | DOGE 2025, Folgefenster 5000 Zeilen | Folgewelt |
| `REAL_DRIFT_XRP_2025_A` | XRP 2025, Startfenster 5000 Zeilen | Startwelt |
| `REAL_DRIFT_XRP_2025_FOLLOW` | XRP 2025, Folgefenster 5000 Zeilen | Folgewelt |

## Topologischer Befund

Alle vier Fenster bleiben global `stark_zentriert_wenig_rand`.

Das bedeutet:

- die Zentrumstopologie bricht nicht,
- offene Varianten bleiben klein,
- Rand/Kippnähe bleibt global nicht dominant,
- lokale Randdruckspitzen sind trotzdem sichtbar.

Die globale Feldform bleibt damit stabil, während die innere Rollenbreite und Achsenklasse variiert.

## Achsenbefund

| Welt | Rollen | Kombinationen | Achsenklasse | Rollenbreite |
|---|---:|---:|---|---|
| DOGE 2025 | 2 | 1 | `kompakt_nachhallend` | kompakt |
| XRP 2025 | 4 | 6 | `mittlere_uebergangsphase` | mittel |

DOGE 2025 bleibt damit nahe bei DOGE/XRP 2024: kompakt, nachhallend, zentrumsnah.

XRP 2025 zeigt dagegen wieder eine mittlere Übergangsphase. Diese Klasse ist damit nicht mehr nur in SOL 2025 sichtbar. Sie erscheint aber auch nicht automatisch in jedem 2025-Asset.

## Randdruck

Die Randdruck-Lupe zeigt in allen vier Fenstern lokale Spitzen. Diese Spitzen tragen überwiegend `tragend_unruhig`, nicht `kippend`.

Kurz gelesen:

```text
Global: Zentrum bleibt stabil.
Lokal: Randdruck flackert in einzelnen Weltstellen auf.
Feldwirkung: lokale Spannung wird rekoppelt, nicht zum globalen Kollaps.
```

## Erkenntnis

Die bisherige Trennung wird schärfer:

- `kompakt_nachhallend` wirkt assetübergreifend plausibel.
- `mittlere_uebergangsphase` ist keine reine SOL-Spezialität, da XRP 2025 sie ebenfalls zeigt.
- DOGE 2025 zeigt sie nicht, obwohl es ebenfalls 2025 ist.

Daraus folgt vorläufig:

```text
Übergangsphase = weltphasen- und assetmilieuabhängige Feldbreite,
nicht einfach Jahr, Asset oder Topologiebruch.
```

Die MCM-Grundtopologie bleibt stabiler als die Achsenklasse. Die Achsenklasse beschreibt eher das Feldmilieu innerhalb dieser Topologie.

## Zugehörige Reports

- `reports/real_drift_asset_doge_xrp_2025_topology.md`
- `reports/real_drift_asset_doge_xrp_2025_randdruck.md`
- `reports/real_drift_asset_doge_xrp_2025_axis_map.md`

## Wie es weitergeht

Als nächstes sollte geprüft werden, welche konkreten Rohweltphasen in XRP 2025 die mittlere Übergangsphase tragen. Entscheidend ist, ob Rollenbreite durch Sicht-, Hör-, Spannungs- oder Nachhalllage entsteht.
