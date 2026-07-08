# 1811 - Dio 1Fll Feldfolgen Signatur

## Grundfrage

Die Prüfung verdichtet Tickfenster zu einer kompakten Feldfolgen-Signatur.

Gelesen werden Vorlauf, Ereignis und Nachlauf getrennt. Die Diagnose bleibt passiv.

Quelle: `reports/dio_1fll_bridge_tick_windows.csv`

## Signatur

| Muster | Phase | Zeilen | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Raw Intake | Adapt Intake | Lesung |
|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| `tragende_verarbeitung` | `vorlauf` | 32 | `stabile_scharfe_form` | `geordnetes_hinhoeren` | `rekoppelt` | 0.062283 | 0.743598 | 0.123714 | 0.070155 | 0.062283 | `rekopplungspunkt_mit_nachhallpruefung` |
| `tragende_verarbeitung` | `ereignis` | 4 | `stabile_scharfe_form` | `geordnetes_hinhoeren` | `rekoppelt` | 0.009432 | 0.77941 | 0.107528 | 0.010275 | 0.009432 | `rekopplungspunkt_mit_nachhallpruefung` |
| `tragende_verarbeitung` | `nachlauf` | 32 | `wechselnde_form` | `geordnetes_hinhoeren` | `rekoppelt` | 0.108537 | 0.734161 | 0.147561 | 0.128811 | 0.108537 | `rekopplungspunkt_mit_nachhallpruefung` |

## Befund

`dio_1fll` zeigt in den geprüften Fenstern die folgenden Feldfolgen:

- tragende Verarbeitung: Vorlauf offen/wechselnd, Ereignis rekoppelt, Nachlauf prüft weiter zwischen offen, rekoppelt und belastet.
- Kippnähe: Ereignis bleibt offen, der Nachlauf trägt eher offene Spannung als stabile Rekopplung.

Damit ist `dio_1fll` nicht einfach ein einzelnes Symbol. Die konkrete Lesart entsteht aus Feldfolge, Weltfenster und Nachbarschaft.

## Wie es weitergeht

Als nächstes sollte diese Signatur mit der bisherigen Rollentaxonomie verglichen werden.
