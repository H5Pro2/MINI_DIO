# 1802 - `dio_0l7p` Feldfolgen-Signatur

## Grundfrage

Die Prüfung verdichtet die Tickfenster aus 1801 zu einer kompakten Feldfolgen-Signatur.

Gelesen werden Vorlauf, Ereignis und Nachlauf getrennt. Die Diagnose bleibt passiv.

Quelle: `reports/dio_0l7p_bridge_tick_windows.csv`

## Signatur

| Muster | Phase | Zeilen | Visual | Ton | Feld | Spannung | Rekopplung | Strain | Raw Intake | Adapt Intake | Lesung |
|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| `kippnaehe` | `vorlauf` | 4 | `stabile_scharfe_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.105865 | 0.67779 | 0.152372 | 0.120994 | 0.105865 | `offene_kippnaehe_mit_nachlaufspannung` |
| `kippnaehe` | `ereignis` | 2 | `stabile_scharfe_form` | `geordnetes_hinhoeren` | `offen` | 0.047781 | 0.666355 | 0.16161 | 0.05422 | 0.047781 | `offene_kippnaehe_mit_nachlaufspannung` |
| `kippnaehe` | `nachlauf` | 16 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.096739 | 0.663851 | 0.167836 | 0.111105 | 0.096739 | `offene_kippnaehe_mit_nachlaufspannung` |
| `tragende_verarbeitung` | `vorlauf` | 32 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.105634 | 0.706711 | 0.153771 | 0.127272 | 0.105634 | `rekopplungspunkt_mit_nachhallpruefung` |
| `tragende_verarbeitung` | `ereignis` | 4 | `wechselnde_form` | `geordnetes_hinhoeren` | `rekoppelt` | 0.040351 | 0.760132 | 0.127542 | 0.0451 | 0.040351 | `rekopplungspunkt_mit_nachhallpruefung` |
| `tragende_verarbeitung` | `nachlauf` | 32 | `wechselnde_form` | `geordnetes_hinhoeren_mit_wechsel` | `offen` | 0.107838 | 0.708654 | 0.14971 | 0.126746 | 0.107838 | `rekopplungspunkt_mit_nachhallpruefung` |

## Befund

`dio_0l7p` zeigt in den geprüften Fenstern zwei verschiedene Feldfolgen:

- tragende Verarbeitung: Vorlauf offen/wechselnd, Ereignis rekoppelt, Nachlauf prüft weiter zwischen offen, rekoppelt und belastet.
- Kippnähe: Ereignis bleibt offen, der Nachlauf trägt eher offene Spannung als stabile Rekopplung.

Damit ist `dio_0l7p` nicht einfach ein einzelnes Symbol. Es wirkt wie ein Brückenträger, dessen konkrete Lesart aus der Feldfolge entsteht.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob `dio_104t` eine ähnliche Feldfolgen-Signatur zeigt oder ob es stärker als Anschluss-/Kohärenzknoten wirkt.
