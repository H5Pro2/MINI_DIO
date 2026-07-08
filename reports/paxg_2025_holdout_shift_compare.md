# PAXG 2025 Holdout Gegen Shift1

## Zweck

Dieser Bericht vergleicht zwei PAXG-2025-Fenster:

```text
HOLDOUT = erster 2000er-Ausschnitt
SHIFT1  = verschobener 2000er-Folgeausschnitt
```

Geprüft wird, ob PAXG 2025 seine rekopplungsstarke Färbung auch in einem späteren Abschnitt hält.

## Topologie

| Zeitachse | Holdout Zustand | Shift1 Zustand | Holdout Zentrum | Shift1 Zentrum | Delta | Holdout Offen | Shift1 Offen | Delta | Rand/Kipp Holdout | Rand/Kipp Shift1 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 5m | stark_zentriert_wenig_rand | stark_zentriert_wenig_rand | 0.9950 | 0.9935 | -0.0015 | 0.0050 | 0.0065 | +0.0015 | 0.0000 | 0.0000 |
| 15m | stark_zentriert_wenig_rand | stark_zentriert_wenig_rand | 0.9900 | 0.9900 | +0.0000 | 0.0100 | 0.0100 | +0.0000 | 0.0000 | 0.0000 |
| 1h | stark_zentriert_wenig_rand | stark_zentriert_wenig_rand | 0.9935 | 0.9930 | -0.0005 | 0.0065 | 0.0070 | +0.0005 | 0.0000 | 0.0000 |

## Feldfärbung

| Zeitachse | Rekopplung Holdout | Rekopplung Shift1 | Delta | Dämpfung Holdout | Dämpfung Shift1 | Delta | Randdruck Holdout | Randdruck Shift1 | Delta |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5m | 0.3561 | 0.3410 | -0.0151 | 0.0777 | 0.0978 | +0.0201 | 0.4152 | 0.4147 | -0.0005 |
| 15m | 0.3250 | 0.3039 | -0.0211 | 0.1118 | 0.1274 | +0.0156 | 0.3932 | 0.3987 | +0.0055 |
| 1h | 0.3104 | 0.2954 | -0.0150 | 0.1264 | 0.1394 | +0.0130 | 0.3977 | 0.3932 | -0.0045 |

## Sinnesaufnahme

| Zeitachse | Strain Holdout | Strain Shift1 | Delta | Visual Gap Holdout | Visual Gap Shift1 | Delta | Hearing Gap Holdout | Hearing Gap Shift1 | Delta |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5m | 0.1565 | 0.1599 | +0.0034 | 0.1509 | 0.1629 | +0.0120 | 0.0828 | 0.0924 | +0.0096 |
| 15m | 0.1639 | 0.1660 | +0.0021 | 0.1802 | 0.1832 | +0.0030 | 0.0983 | 0.1028 | +0.0045 |
| 1h | 0.1665 | 0.1639 | -0.0026 | 0.1819 | 0.1758 | -0.0061 | 0.1050 | 0.1013 | -0.0037 |

## Lesart

Der Folgeabschnitt bestätigt die stabile Topologie:

```text
Holdout: stark_zentriert_wenig_rand
Shift1:  stark_zentriert_wenig_rand
```

Gleichzeitig verändert sich die lokale Feldfärbung:

- Rekopplung fällt im SHIFT1-Fenster auf allen drei Zeitachsen leicht ab.
- Dämpfung steigt auf allen drei Zeitachsen.
- Randdruck bleibt nah am Holdout und wird nicht zur Randdominanz.
- 15m und 1h werden im SHIFT1-Fenster etwas stärker gedämpft gelesen.

Damit bleibt PAXG 2025 als Milieu wiedererkennbar, aber nicht statisch.

## Schlussfolgerung

Die PAXG-Färbung ist im Folgefenster nicht verschwunden. Sie driftet lokal in Richtung mehr Schutzabstand/Dämpfung, ohne die zentrumsnahe MCM-Topologie zu brechen.

Das stützt die bisherige Trennung:

```text
Topologie = stabiler Rollenraum
Feldfärbung = phasenabhängige lokale Qualität
```

## Wie es weitergeht

Als nächstes sollte PAXG mit einem zweiten verschobenen Fenster oder mit einem längeren 10k-Gesamtfenster gelesen werden. Ziel ist zu prüfen, ob die Dämpfungszunahme eine lokale Phase oder eine längere PAXG-2025-Tendenz ist.
