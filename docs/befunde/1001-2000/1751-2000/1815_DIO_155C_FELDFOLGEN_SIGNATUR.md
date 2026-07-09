# 1815 - Dio 155C Feldfolgen Signatur

## Grundfrage

Die Prüfung verdichtet Tickfenster zu einer kompakten Feldfolgen-Signatur.

Gelesen werden Vorlauf, Ereignis und Nachlauf getrennt. Die Diagnose bleibt passiv.

Quelle: `reports/dio_155c_bridge_tick_windows.csv`

## Signatur

| Muster | Phase | Zeilen | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Raw Intake | Adapt Intake | Lesung |
|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| `kippnaehe` | `vorlauf` | 32 | `stabile_scharfe_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.131687 | 0.684654 | 0.166654 | 0.155577 | 0.131687 | `offene_kippnaehe_mit_nachlaufspannung` |
| `kippnaehe` | `ereignis` | 4 | `stabile_scharfe_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.126299 | 0.675669 | 0.178307 | 0.146016 | 0.126299 | `offene_kippnaehe_mit_nachlaufspannung` |
| `kippnaehe` | `nachlauf` | 32 | `stabile_scharfe_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.13915 | 0.682757 | 0.167974 | 0.164859 | 0.13915 | `offene_kippnaehe_mit_nachlaufspannung` |
| `tragende_verarbeitung` | `vorlauf` | 32 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.101262 | 0.717203 | 0.146674 | 0.117264 | 0.101262 | `rekopplungspunkt_mit_nachhallpruefung` |
| `tragende_verarbeitung` | `ereignis` | 4 | `stabile_scharfe_form` | `geordnetes_hinhoeren_mit_wechsel` | `rekoppelt` | 0.099338 | 0.74648 | 0.133456 | 0.113924 | 0.099338 | `rekopplungspunkt_mit_nachhallpruefung` |
| `tragende_verarbeitung` | `nachlauf` | 32 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `rekoppelt` | 0.110771 | 0.71592 | 0.148045 | 0.12977 | 0.110771 | `rekopplungspunkt_mit_nachhallpruefung` |

## Befund

`dio_155c` zeigt in den geprüften Fenstern die folgenden Feldfolgen:

- tragende Verarbeitung: Vorlauf offen/wechselnd, Ereignis rekoppelt, Nachlauf prüft weiter zwischen offen, rekoppelt und belastet.
- Kippnähe: Ereignis bleibt offen, der Nachlauf trägt eher offene Spannung als stabile Rekopplung.

Damit ist `dio_155c` nicht einfach ein einzelnes Symbol. Die konkrete Lesart entsteht aus Feldfolge, Weltfenster und Nachbarschaft.
