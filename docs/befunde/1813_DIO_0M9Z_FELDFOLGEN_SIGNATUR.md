# 1813 - Dio 0M9Z Feldfolgen Signatur

## Grundfrage

Die Prüfung verdichtet Tickfenster zu einer kompakten Feldfolgen-Signatur.

Gelesen werden Vorlauf, Ereignis und Nachlauf getrennt. Die Diagnose bleibt passiv.

Quelle: `reports/dio_0m9z_bridge_tick_windows.csv`

## Signatur

| Muster | Phase | Zeilen | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Raw Intake | Adapt Intake | Lesung |
|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| `kippnaehe` | `vorlauf` | 20 | `stabile_scharfe_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.089081 | 0.670645 | 0.158934 | 0.102759 | 0.089081 | `spannungsnahe_folge` |
| `kippnaehe` | `ereignis` | 4 | `stabile_scharfe_form` | `geordnetes_hinhoeren_mit_wechsel` | `belastet_kippnah` | 0.14388 | 0.645225 | 0.194976 | 0.167183 | 0.14388 | `spannungsnahe_folge` |
| `kippnaehe` | `nachlauf` | 32 | `stabile_scharfe_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.098303 | 0.673126 | 0.160252 | 0.113335 | 0.098303 | `spannungsnahe_folge` |

## Befund

`dio_0m9z` zeigt in den geprüften Fenstern die folgenden Feldfolgen:

- tragende Verarbeitung: Vorlauf offen/wechselnd, Ereignis rekoppelt, Nachlauf prüft weiter zwischen offen, rekoppelt und belastet.
- Kippnähe: Ereignis bleibt offen, der Nachlauf trägt eher offene Spannung als stabile Rekopplung.

Damit ist `dio_0m9z` nicht einfach ein einzelnes Symbol. Die konkrete Lesart entsteht aus Feldfolge, Weltfenster und Nachbarschaft.

## Wie es weitergeht

Als nächstes sollte diese Signatur mit der bisherigen Rollentaxonomie verglichen werden.
