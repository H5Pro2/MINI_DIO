# 1809 - Dio 14Wj Feldfolgen Signatur

## Grundfrage

Die Prüfung verdichtet Tickfenster zu einer kompakten Feldfolgen-Signatur.

Gelesen werden Vorlauf, Ereignis und Nachlauf getrennt. Die Diagnose bleibt passiv.

Quelle: `reports/dio_14wj_bridge_tick_windows.csv`

## Signatur

| Muster | Phase | Zeilen | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Raw Intake | Adapt Intake | Lesung |
|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| `tragende_verarbeitung` | `vorlauf` | 32 | `wechselnde_form` | `geordnetes_hinhoeren` | `offen` | 0.0705 | 0.718772 | 0.135626 | 0.080696 | 0.0705 | `rekopplungspunkt_mit_nachhallpruefung` |
| `tragende_verarbeitung` | `ereignis` | 4 | `stabile_scharfe_form` | `geordnetes_hinhoeren` | `rekoppelt` | 0.014949 | 0.755055 | 0.10953 | 0.016468 | 0.014949 | `rekopplungspunkt_mit_nachhallpruefung` |
| `tragende_verarbeitung` | `nachlauf` | 32 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.119112 | 0.702717 | 0.148207 | 0.138797 | 0.119112 | `rekopplungspunkt_mit_nachhallpruefung` |

## Befund

`dio_14wj` zeigt in den geprüften Fenstern die folgenden Feldfolgen:

- tragende Verarbeitung: Vorlauf offen/wechselnd, Ereignis rekoppelt, Nachlauf prüft weiter zwischen offen, rekoppelt und belastet.
- Kippnähe: Ereignis bleibt offen, der Nachlauf trägt eher offene Spannung als stabile Rekopplung.

Damit ist `dio_14wj` nicht einfach ein einzelnes Symbol. Die konkrete Lesart entsteht aus Feldfolge, Weltfenster und Nachbarschaft.

## Wie es weitergeht

Als nächstes sollte diese Signatur mit der bisherigen Rollentaxonomie verglichen werden.
