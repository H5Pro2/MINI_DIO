# 1045 - PAXG: `dio_14wj` ueber 5m und 1h

## Zweck

Diese Pruefung klaert die offene Frage aus Befund 1044:

```text
Ist `dio_14wj` eine echte PAXG-5m-Rolle,
oder bleibt dieselbe Rolle auch auf 1h erhalten?
```

Dabei wurde `dio_14wj` gegen `dio_104t` und `dio_155c` in PAXG 2024/2025 5m und PAXG 2024/2025 1h gelesen.

## Datengrundlage

Erzeugte Messdatei:

- `1045_PAXG_DIO14WJ_ZEITAUFLOESUNG_VERGLEICH.csv`

Gepruefte Welten:

- `PAXG2024_5M_10K`
- `PAXG2025_5M_10K`
- `PAXG2024_1H_YEAR`
- `PAXG2025_1H_YEAR`

Verglichene Familien:

- `dio_104t`
- `dio_14wj`
- `dio_155c`

## Befund 1: `dio_14wj` bleibt auch auf 1h ruhig

| Welt | Familie | Anteil | Rekopplung | Carry | Strain | Sinnes-MCM |
|---|---:|---:|---:|---:|---:|---:|
| PAXG2024_1H_YEAR | `dio_104t` | 0.078264 | 0.725057 | 0.574478 | 0.150750 | 0.850949 |
| PAXG2024_1H_YEAR | `dio_14wj` | 0.023240 | 0.733846 | 0.575857 | 0.125828 | 0.869240 |
| PAXG2024_1H_YEAR | `dio_155c` | 0.042151 | 0.717026 | 0.560926 | 0.159381 | 0.853796 |
| PAXG2025_1H_YEAR | `dio_104t` | 0.088874 | 0.725202 | 0.577151 | 0.150840 | 0.851960 |
| PAXG2025_1H_YEAR | `dio_14wj` | 0.027645 | 0.733964 | 0.578391 | 0.126437 | 0.869401 |
| PAXG2025_1H_YEAR | `dio_155c` | 0.042723 | 0.716013 | 0.561548 | 0.159535 | 0.852616 |

Lesung:

`dio_14wj` bleibt auch auf 1h die ruhigere Familie:

- hoehere Rekopplung als `dio_104t` und `dio_155c`,
- niedrigerer Strain,
- staerkere Sinnes-MCM-Kopplung.

Damit ist `dio_14wj` keine reine 5m-Zufallsoberflaeche.

## Befund 2: Die Dominanz von `dio_14wj` ist zeitebenenabhaengig

| Welt | `dio_14wj` Anteil |
|---|---:|
| PAXG2024_5M_10K | 0.053032 |
| PAXG2025_5M_10K | 0.070843 |
| PAXG2024_1H_YEAR | 0.023240 |
| PAXG2025_1H_YEAR | 0.027645 |

Lesung:

`dio_14wj` bleibt als ruhige Rolle sichtbar, verliert auf 1h aber deutlich an Dominanz.

Die Rolle verschwindet nicht, aber sie wird weniger haeufig aktiviert.

Das spricht fuer:

```text
Rollenqualitaet bleibt erhalten.
Rollenaktivierung ist zeitebenenabhaengig.
```

## Befund 3: `dio_155c` ist keine ruhigere Ersatzrolle

`dio_155c` ist auf 1h haeufiger als `dio_14wj`, aber feldqualitativ nicht ruhiger:

- niedrigere Rekopplung,
- niedrigerer Carry,
- hoeherer Strain,
- deutlich hoehere Kontaktspannung.

Beispiel PAXG2025 1h:

| Familie | Rekopplung | Strain | Kontaktspannung |
|---|---:|---:|---:|
| `dio_14wj` | 0.733964 | 0.126437 | 0.038186 |
| `dio_155c` | 0.716013 | 0.159535 | 0.138960 |

Lesung:

`dio_155c` ist auf 1h eher eine groessere beziehungsweise breitere Erweiterungsfamilie, aber nicht der gleiche Ruhetraeger wie `dio_14wj`.

## Befund 4: Nachhall und Vertrauen sind bei `dio_14wj` auf 5m staerker

| Welt | Familie | Afterimage | Trust Support |
|---|---:|---:|---:|
| PAXG2024_5M_10K | `dio_14wj` | 0.466400 | 0.856297 |
| PAXG2025_5M_10K | `dio_14wj` | 0.522133 | 0.870774 |
| PAXG2024_1H_YEAR | `dio_14wj` | 0.290439 | 0.800757 |
| PAXG2025_1H_YEAR | `dio_14wj` | 0.317456 | 0.810282 |

Lesung:

Die ruhige Rolle bleibt auf 1h erhalten, aber der innere Nachhall ist schwacher.

Auf 5m bildet `dio_14wj` eine staerkere zeitliche Spur. Auf 1h bleibt die Rolle messbar, aber weniger innerlich gebunden.

## Schlussfolgerung

`dio_14wj` ist keine reine Oberflaechenvariante und keine reine 5m-Zufallsbildung.

Praeziser:

```text
`dio_14wj` ist eine PAXG-nahe ruhige Rekopplungsrolle.
Ihre Feldqualitaet bleibt ueber 5m und 1h erhalten.
Ihre Dominanz und ihr Nachhall sind auf 5m deutlich staerker.
```

Damit wird die PAXG-Lesung stabiler:

```text
Topologie bleibt gleich.
Rolle bleibt wiedererkennbar.
Aktivierungsstaerke haengt von der Zeitebene ab.
```

## Bedeutung fuer MINI_DIO

MINI_DIO zeigt hier drei Ebenen:

1. stabile Grundfamilie: `dio_104t`
2. ruhige Rekopplungsrolle: `dio_14wj`
3. breitere 1h-Erweiterungsfamilie: `dio_155c`

Das ist wichtig fuer die Forschung:

Eine Bedeutung muss nicht entweder stabil oder verschwunden sein.

Sie kann:

- als Rolle erhalten bleiben,
- in der Dominanz sinken,
- in anderer Zeitebene anders nachhallen,
- neben anderen Erweiterungsfamilien bestehen.

## Wie es weitergeht

Als naechstes sollte `dio_14wj` gegen Nicht-PAXG-Welten geprueft werden. Ziel: Klaeren, ob diese ruhige Rekopplungsrolle PAXG-spezifisch ist oder ob sie auch in BTC, SOL oder KAS unter bestimmten Weltspannungen dieselbe Funktion uebernimmt.
