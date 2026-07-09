# 1805 - `dio_104t` Feldfolgen-Signatur

## Grundfrage

Die Prüfung verdichtet die Tickfenster aus 1804 zu einer kompakten Feldfolgen-Signatur.

Gelesen werden Vorlauf, Ereignis und Nachlauf getrennt. Die Diagnose bleibt passiv.

Quelle: `reports/dio_104t_bridge_tick_windows.csv`

## Signatur

| Muster | Phase | Zeilen | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Raw Intake | Adapt Intake | Lesung |
|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| `kippnaehe` | `vorlauf` | 24 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.112212 | 0.671009 | 0.16074 | 0.129863 | 0.112212 | `offene_kippnaehe_mit_nachlaufspannung` |
| `kippnaehe` | `ereignis` | 4 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.08218 | 0.661925 | 0.169041 | 0.093981 | 0.08218 | `offene_kippnaehe_mit_nachlaufspannung` |
| `kippnaehe` | `nachlauf` | 32 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.113366 | 0.661821 | 0.170887 | 0.134798 | 0.113366 | `offene_kippnaehe_mit_nachlaufspannung` |
| `tragende_verarbeitung` | `vorlauf` | 32 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.108672 | 0.711421 | 0.152576 | 0.126692 | 0.108672 | `rekopplungspunkt_mit_nachhallpruefung` |
| `tragende_verarbeitung` | `ereignis` | 4 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `rekoppelt` | 0.065593 | 0.753815 | 0.131754 | 0.074539 | 0.065593 | `rekopplungspunkt_mit_nachhallpruefung` |
| `tragende_verarbeitung` | `nachlauf` | 32 | `wechselnde_form` | `geordnetes_hinhoeren` | `rekoppelt` | 0.078438 | 0.729946 | 0.13544 | 0.089709 | 0.078438 | `rekopplungspunkt_mit_nachhallpruefung` |

## Befund

`dio_104t` zeigt in den geprüften Fenstern zwei verschiedene Feldfolgen:

- tragende Verarbeitung: Vorlauf offen/wechselnd, Ereignis rekoppelt, Nachlauf prüft weiter zwischen offen, rekoppelt und belastet.
- Kippnähe: Ereignis bleibt offen, der Nachlauf trägt eher offene Spannung als stabile Rekopplung.

Damit ist `dio_104t` nicht einfach ein einzelnes Symbol. Es wirkt wie ein Anschluss-/Kohärenzknoten, dessen konkrete Lesart aus der Feldfolge entsteht.
