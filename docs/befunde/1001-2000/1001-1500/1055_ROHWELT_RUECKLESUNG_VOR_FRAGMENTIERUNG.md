# Rohwelt-Ruecklesung vor belasteter Fragmentierung

## Zweck

Diese Diagnose liest passiv zurueck, welche Weltspannung, Ton-/Energieform und sichtbare Form vor spaeterer belasteter Fragmentierung lag.
Sie nutzt Episode-Dateien und betrachtet das Vorfenster vor belasteten Fragmentierungszustandsmomenten.

## Methodische Grenze

- passive Diagnose
- keine Handlung
- kein Gate
- keine Strategie
- Der Zielzustand wird pro Lauf aus der jeweiligen Verteilung gelesen, nicht als feste globale Schwelle

## Befund

- Ausgewertete Laeufe: `20`
- Zielereignisse: `47`
- Dominante sichtbare Vorformen: `offene_formaufnahme:16 | sichtbar_stabile_form:2 | sichtbarer_formwechsel:2`
- Dominante Ton-/Energie-Vorformen: `gedaempfte_energie:16 | tonaler_wechsel:4`
- Dominante Weltspannungs-Vorformen: `entlastete_weltspannung:20`

## Laufprofile

| Quelle | Events | Sicht davor | Ton davor | Spannung davor | Formstabilitaet | dForm | Energie-Ton | dTon | Feldaufnahme | dFeld | Ziel-Rekopplung | Ziel-Strain |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `adapted_field_doge_2024_5m_10k` | 4 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.092692 | 0.045957 | 0.006282 | 0.012385 | 0.099774 | -0.007178 | 0.551766 | 0.339431 |
| `adapted_field_doge_2024_5m_10k` | 4 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.092692 | 0.045957 | 0.006282 | 0.012385 | 0.099774 | -0.007178 | 0.551328 | 0.339199 |
| `adapted_field_xrp_2024_5m_10k` | 4 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.010479 | -0.04026 | -0.027625 | -0.0199 | 0.11115 | 0.005782 | 0.542566 | 0.335913 |
| `adapted_time_xrp_2024_1h_10k` | 4 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.016654 | -0.048645 | -0.001881 | 0.001986 | 0.134894 | 0.029405 | 0.537946 | 0.340845 |
| `adapted_time_xrp_2024_1h_10k` | 4 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.016654 | -0.048645 | -0.001881 | 0.001986 | 0.134894 | 0.029405 | 0.537284 | 0.340496 |
| `adapted_field_xrp_2024_5m_10k` | 3 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.03352 | -0.017219 | -0.037856 | -0.030131 | 0.111976 | 0.006608 | 0.541203 | 0.337585 |
| `adapted_time_kas_2024_1h_2k` | 3 | `offene_formaufnahme` | `tonaler_wechsel` | `entlastete_weltspannung` | 0.092077 | 0.067726 | 0.103418 | 0.106638 | 0.145118 | 0.036121 | 0.53807 | 0.340732 |
| `adapted_time_kas_2024_1h_2k` | 3 | `offene_formaufnahme` | `tonaler_wechsel` | `entlastete_weltspannung` | 0.092077 | 0.067726 | 0.103418 | 0.106638 | 0.145118 | 0.036121 | 0.537852 | 0.34062 |
| `adapted_field_sol_2024_5m_2k` | 2 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.01986 | -0.066221 | -0.095294 | -0.088826 | 0.090587 | -0.017907 | 0.538067 | 0.342591 |
| `adapted_field_sol_2024_5m_2k` | 2 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.01986 | -0.066221 | -0.095294 | -0.088826 | 0.090587 | -0.017907 | 0.537692 | 0.342395 |
| `adapted_time_doge_2024_1h_10k` | 2 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.013907 | -0.020228 | 0.05312 | 0.055152 | 0.131028 | 0.02482 | 0.53808 | 0.34245 |
| `adapted_time_doge_2024_1h_10k` | 2 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.013907 | -0.020228 | 0.05312 | 0.055152 | 0.131028 | 0.02482 | 0.537755 | 0.342267 |
| `adapted_time_paxg_2024_1h_10k` | 2 | `sichtbarer_formwechsel` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.057946 | -0.062539 | 0.001598 | 0.004085 | 0.132466 | 0.024666 | 0.534397 | 0.344082 |
| `adapted_time_paxg_2024_1h_10k` | 2 | `sichtbarer_formwechsel` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.057946 | -0.062539 | 0.001598 | 0.004085 | 0.132466 | 0.024666 | 0.534122 | 0.343925 |
| `adapted_field_btc_2024_5m_2k` | 1 | `sichtbar_stabile_form` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.307622 | 0.2802 | 0.001165 | 0.008175 | 0.124667 | 0.018899 | 0.536703 | 0.341942 |
| `adapted_field_btc_2024_5m_2k` | 1 | `sichtbar_stabile_form` | `gedaempfte_energie` | `entlastete_weltspannung` | 0.307622 | 0.2802 | 0.001165 | 0.008175 | 0.124667 | 0.018899 | 0.536231 | 0.341702 |
| `adapted_time_btc_2024_1h_2k` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.204883 | -0.231106 | -0.182934 | -0.180557 | 0.08525 | -0.021219 | 0.528872 | 0.35248 |
| `adapted_time_btc_2024_1h_2k` | 1 | `offene_formaufnahme` | `gedaempfte_energie` | `entlastete_weltspannung` | -0.204883 | -0.231106 | -0.182934 | -0.180557 | 0.08525 | -0.021219 | 0.528602 | 0.352343 |
| `adapted_time_sol_2024_1h_2k` | 1 | `offene_formaufnahme` | `tonaler_wechsel` | `entlastete_weltspannung` | -0.057634 | -0.087098 | 0.270784 | 0.27318 | 0.155383 | 0.046496 | 0.543408 | 0.335304 |
| `adapted_time_sol_2024_1h_2k` | 1 | `offene_formaufnahme` | `tonaler_wechsel` | `entlastete_weltspannung` | -0.057634 | -0.087098 | 0.270784 | 0.27318 | 0.155383 | 0.046496 | 0.54298 | 0.335065 |

## Arbeitsableitung

```text
Spaetere Zielbindung (belastete Fragmentierung) entsteht nicht aus einem einzelnen Rohwert.
Ruecklesbar ist ein Vorfeld aus sichtbarer Formlage, tonaler Energieform und regulierter Feldaufnahme.
Die relativen Delta-Spalten zeigen, ob dieses Vorfeld gegen die jeweilige Weltbasis abweicht.
Damit liegt die Ursache nicht direkt in der Rohwelt, sondern in der Art, wie die Rohwelt vorher sinnlich aufgenommen wurde.
```

## Wie es weitergeht

Als naechstes sollten Rekopplungs- und Fragmentierungsruecklesung direkt nebeneinander gelegt werden.
Dann wird sichtbar, welche Vorwelt eher Bindung vorbereitet und welche eher Last/Fragmentierung vorbereitet.