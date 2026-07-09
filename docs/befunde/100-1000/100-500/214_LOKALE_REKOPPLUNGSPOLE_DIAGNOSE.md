# Lokale Rekopplungspole - Diagnose

Stand: 2026-06-19 04:53:39

## Zweck

Diese Diagnose prueft lokale Stresssegmente gegen lokale Ruhe-/Entlastungssegmente.
Sie nutzt die bestehende Rekopplungsrollen-Lesung und erzeugt keine neue Runtime-Mechanik.

Hierarchie der Pruefung:

1. Grundfrage: Treten `last_memory_bindend` und `reiz_aktiv_rekoppelnd` als lokale Gegenpole auf?
2. Unterpruefung: Stresssegmente gegen Quiet-Segmente vergleichen.
3. Folgeschritt: Entscheiden, ob lokale Rekopplungspole eine stabile passive MCM-Landkarte bilden.

## Rollen nach Gruppe

| Gruppe | Rolle | Anzahl |
|---|---|---:|
| ruhe | reiz_aktiv_rekoppelnd | 5 |
| stress | uebergang_bindend | 4 |
| stress | last_memory_bindend | 2 |
| stress | reiz_aktiv_rekoppelnd | 1 |

## Einzelwerte

| Welt | Gruppe | Rolle | Rekopplung | Feldlast | Memorylast | Aufmerksamkeit | aktiv-rekoppelnd | Bindungssumme | Kontrast Bindung-Aktiv |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| QUIET_2024_REAL | ruhe | reiz_aktiv_rekoppelnd | 0.630744 | 0.0213 | 0.0532 | 0.3329 | 0.6152 | 0.1277 | -0.4875 |
| QUIET_2024_SIDEWAYS | ruhe | reiz_aktiv_rekoppelnd | 0.639653 | 0.0213 | 0.0532 | 0.5941 | 0.7552 | 0.2023 | -0.5529 |
| QUIET_2025_CORE | ruhe | reiz_aktiv_rekoppelnd | 0.628376 | 0.0106 | 0.0319 | 0.3603 | 0.6213 | 0.1269 | -0.4944 |
| QUIET_2025_STRESS | ruhe | reiz_aktiv_rekoppelnd | 0.639352 | 0.0000 | 0.0106 | 0.4693 | 0.7069 | 0.0940 | -0.6129 |
| QUIET_2026_ANCHOR | ruhe | reiz_aktiv_rekoppelnd | 0.639974 | 0.0213 | 0.0532 | 0.5169 | 0.7239 | 0.1409 | -0.5830 |
| AUTO_STRESS_SEGMENT5 | stress | uebergang_bindend | 0.607085 | 0.2151 | 0.2258 | 0.4492 | 0.5371 | 0.4729 | -0.0642 |
| AUTO_STRESS_SEGMENT5_6 | stress | uebergang_bindend | 0.606201 | 0.1719 | 0.2344 | 0.4235 | 0.5337 | 0.4420 | -0.0917 |
| AUTO_STRESS_SEGMENT6 | stress | uebergang_bindend | 0.606419 | 0.1290 | 0.2473 | 0.5096 | 0.5809 | 0.4452 | -0.1357 |
| STRESS_2023_TEST4 | stress | last_memory_bindend | 0.596927 | 0.2660 | 0.2447 | 0.1409 | 0.3609 | 0.4903 | 0.1294 |
| STRESS_2024_REAL | stress | uebergang_bindend | 0.601652 | 0.2340 | 0.2447 | 0.4807 | 0.5274 | 0.5596 | 0.0322 |
| STRESS_2024_SIDEWAYS | stress | reiz_aktiv_rekoppelnd | 0.629551 | 0.0532 | 0.0532 | 0.4299 | 0.6443 | 0.1773 | -0.4669 |
| STRESS_2025_STRESS | stress | last_memory_bindend | 0.594327 | 0.2872 | 0.2234 | 0.3284 | 0.4257 | 0.5460 | 0.1203 |

## Staerkste Bindung

- `STRESS_2024_REAL` (stress): Rolle `uebergang_bindend`, Bindung `0.5596`, Aktiv `0.5274`, Kontrast `0.0322`
- `STRESS_2025_STRESS` (stress): Rolle `last_memory_bindend`, Bindung `0.5460`, Aktiv `0.4257`, Kontrast `0.1203`
- `STRESS_2023_TEST4` (stress): Rolle `last_memory_bindend`, Bindung `0.4903`, Aktiv `0.3609`, Kontrast `0.1294`
- `AUTO_STRESS_SEGMENT5` (stress): Rolle `uebergang_bindend`, Bindung `0.4729`, Aktiv `0.5371`, Kontrast `-0.0642`
- `AUTO_STRESS_SEGMENT6` (stress): Rolle `uebergang_bindend`, Bindung `0.4452`, Aktiv `0.5809`, Kontrast `-0.1357`
- `AUTO_STRESS_SEGMENT5_6` (stress): Rolle `uebergang_bindend`, Bindung `0.4420`, Aktiv `0.5337`, Kontrast `-0.0917`

## Staerkste aktive Rekopplung

- `QUIET_2024_SIDEWAYS` (ruhe): Rolle `reiz_aktiv_rekoppelnd`, Aktiv `0.7552`, Bindung `0.2023`
- `QUIET_2026_ANCHOR` (ruhe): Rolle `reiz_aktiv_rekoppelnd`, Aktiv `0.7239`, Bindung `0.1409`
- `QUIET_2025_STRESS` (ruhe): Rolle `reiz_aktiv_rekoppelnd`, Aktiv `0.7069`, Bindung `0.0940`
- `STRESS_2024_SIDEWAYS` (stress): Rolle `reiz_aktiv_rekoppelnd`, Aktiv `0.6443`, Bindung `0.1773`
- `QUIET_2025_CORE` (ruhe): Rolle `reiz_aktiv_rekoppelnd`, Aktiv `0.6213`, Bindung `0.1269`
- `QUIET_2024_REAL` (ruhe): Rolle `reiz_aktiv_rekoppelnd`, Aktiv `0.6152`, Bindung `0.1277`

## Gruppenvergleich

- Stress-Kontrast Bindung-Aktiv: `-0.0681`
- Ruhe-Kontrast Bindung-Aktiv: `-0.5462`
- Stress-Feldlast: `0.1938`
- Ruhe-Feldlast: `0.0149`

## Befund

Lokale Rekopplungspole sind nur dann plausibel, wenn Stresssegmente systematisch mehr Bindung und Ruhe-/Entlastungssegmente systematisch mehr aktive Rekopplung zeigen.

Der Kontrast `Bindung-Aktiv` ist dabei die einfache passive Lesegroesse:

```text
negativ -> aktive Rekopplung dominiert
positiv -> Feld-/Memorybindung dominiert
```

## Wie es weitergeht

Als naechstes wird aus dieser Diagnose ein Befund geschrieben.
Darin wird bewertet, ob lokale Stress- und Ruheabschnitte wirklich als MCM-Gegenpole gelesen werden koennen.
