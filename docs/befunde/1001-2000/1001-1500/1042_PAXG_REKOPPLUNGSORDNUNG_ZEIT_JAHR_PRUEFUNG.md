# 1042 - PAXG Rekopplungsordnung ueber Zeit und Jahr

## Zweck

Dieser Befund prueft, ob die PAXG-ruhige Rekopplungsordnung ueber mehrere PAXG-Zeitebenen und Jahre wiederkehrt.

Er bleibt passiv:

- keine Handlung
- kein Gate
- keine Strategie
- keine feste Bedeutungsaufnahme

## Hierarchie

1. Grundfrage: Ist PAXG eine eigene ruhige Rekopplungswelt?
2. Unterpruefung: Bleiben Rekopplung, Strain, Stabilanteil und dominante Familien ueber 5m/1h und 2024/2025 erhalten?
3. Folgeschritt: Pruefen, ob diese Ordnung PAXG-spezifisch ist oder eine allgemeinere ruhige Asset-Ordnung beschreibt.

## Artefakte

- `1042_PAXG_REKOPPLUNGSORDNUNG_ZEIT_JAHR_MATRIX.csv`
- `1042_PAXG_REKOPPLUNGSORDNUNG_TOP_KOPPLUNGEN.csv`

## Matrix

| Welt | Rekopplung | Strain | Sinneskopplung | Stabil | Tragend unruhig | Kipp/Spannung | Top-Familie 1 | Top-Familie 2 |
|---|---:|---:|---:|---:|---:|---:|---|---|
| `PAXG_2024_5M_SHORT` | 0.703694 | 0.152020 | 0.851128 | 0.831494 | 0.161484 | 0.007021 | `dio_104t` | `dio_14wj` |
| `PAXG_2024_5M_10K` | 0.713904 | 0.152510 | 0.854857 | 0.879628 | 0.114169 | 0.006204 | `dio_104t` | `dio_14wj` |
| `PAXG_2025_5M_10K` | 0.714382 | 0.151728 | 0.856090 | 0.872524 | 0.120172 | 0.007304 | `dio_104t` | `dio_14wj` |
| `PAXG_2024_1H_10K` | 0.704917 | 0.153514 | 0.841190 | 0.792208 | 0.201527 | 0.006266 | `dio_104t` | `dio_155c` |
| `PAXG_2025_1H_10K` | 0.706106 | 0.151946 | 0.843674 | 0.809801 | 0.185744 | 0.004455 | `dio_104t` | `dio_155c` |

## Wiederkehr

Die PAXG-Grundsignatur ist stabil:

```text
Top-Familie fast ueberall: dio_104t
5m-Erweiterung: dio_14wj
1h-Erweiterung: dio_155c
```

Die Feldqualitaet bleibt ebenfalls klar:

- hohe Rekopplung,
- niedrige Strain-Last,
- hohe Stabilanteile,
- geringe Kipp-/Spannungsanteile.

Besonders 5m-PAXG wirkt stark rekoppelnd:

```text
PAXG_2024_5M_10K: Rekopplung 0.713904, Stabil 0.879628
PAXG_2025_5M_10K: Rekopplung 0.714382, Stabil 0.872524
```

## Kopplungen

Die Top-Kopplungen zeigen zwei wiederkehrende PAXG-nahe Traeger:

```text
dio_104t = stabile Grundfamilie
dio_14wj = besonders ruhige/rekoppelnde 5m-Familie
```

Beispiele:

| Welt | Kopplung | Anzahl | Rekopplung | Strain | Sinneskopplung |
|---|---|---:|---:|---:|---:|
| `PAXG_2024_5M_10K` | `dio_104t + 1eju9g0` | 265 | 0.730856 | 0.149980 | 0.856634 |
| `PAXG_2024_5M_10K` | `dio_14wj + 1eju9g0` | 181 | 0.745533 | 0.130201 | 0.874833 |
| `PAXG_2025_5M_10K` | `dio_104t + 1hdpu9s` | 229 | 0.732063 | 0.148531 | 0.858677 |
| `PAXG_2025_5M_10K` | `dio_14wj + 1hdpu9s` | 188 | 0.743422 | 0.130462 | 0.873481 |

`dio_14wj` traegt in den PAXG-5m-Welten besonders hohe Rekopplung und deutlich niedrigere Strain-Last als viele andere Kopplungen.

## Befund

PAXG bildet ueber die geprueften PAXG-Welten eine eigene ruhige Rekopplungsordnung.

Diese Ordnung ist nicht identisch mit der KAS/BTC-nahen `rekopplung_nach_abverkauf`-Achse.

Sie wirkt eher so:

```text
PAXG = ruhige Rekopplung / Stabilitaetsnaehe
BTC/SOL/KAS = staerker bruch-, last- und rueckbindungsnah
```

Wichtig:

```text
Die Grundtopologie bleibt erhalten.
Die Bedeutungsfaerbung verschiebt sich.
```

## Deutung

PAXG ist damit nicht einfach ein weiteres Asset in derselben Bedeutungsachse.

PAXG wirkt als Kontrastwelt:

- weniger Kippnaehe,
- staerkere Rekopplung,
- niedrigere Strain,
- eigene stabile Kopplungen,
- andere dominante MCM-Episoden.

Das stuetzt die MCM-Lesart:

```text
Topologie ist allgemeiner.
Bedeutungsfamilien sind weltabhaengiger.
```

## Schluss

Die PAXG-Rekopplungsordnung ist als eigener Kandidat ernst zu nehmen.

Arbeitsname:

```text
PAXG-stabile Rekopplungsordnung
```

Kerntraeger:

- `dio_104t` als stabile Grundfamilie,
- `dio_14wj` als besonders ruhige/rekoppelnde 5m-Erweiterung,
- `dio_155c` als 1h-nahe Erweiterung.

## Wie es weitergeht

Als naechstes sollte diese PAXG-stabile Rekopplungsordnung gegen BTC/SOL/KAS in einer gleich langen und gleich gewaehlten Weltgruppe geprueft werden. Ziel ist zu trennen, was wirklich PAXG-spezifisch ist und was allgemeine ruhige Rekopplung im MCM-Feld ist.
