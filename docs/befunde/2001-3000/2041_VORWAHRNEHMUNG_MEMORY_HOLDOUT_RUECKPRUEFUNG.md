# 2041 - Vorwahrnehmungs-Memory Holdout-Rückprüfung

## Zweck

Diese Diagnose prüft die passive Vorwahrnehmungs-Memory aus `2040` gegen andere reale Weltfenster.

Geprüft wird nicht, ob eine Handlung entsteht. Geprüft wird nur, ob bekannte Feldkontaktrollen in fremden Welten wieder auftauchen, driften oder neue Oberflächen tragen.

## Holdout-Welten

- `btc2024`: `debug\1996_ff_btc_2024_10k`
- `doge2024`: `debug\1996_ff_doge_2024_10k`
- `paxg2024`: `debug\1996_ff_paxg_2024_10k`

## Übersicht

- Ereignisse: `315`
- Gruppen: `14`
- mittlere Feldkontakt-Rückerkennung: `0.640`
- mittlere Sinnesphasen-Rückerkennung: `0.688`
- mittlere Rohphasen-Rückerkennung: `0.198`

## Gruppenergebnis

| Gruppe | Quelle | Holdout | Ereignisse | erwartet | beobachtet | Feld | Sinn | Roh | MCM |
|---|---|---|---:|---|---|---:|---:|---:|---:|
| `oberflaeche_rekoppelt` | `long_btc_sol` | `btc2024` | 18 | `offene_rekopplung` | `tragende_rekopplung` (0.67) | 0.333 | 0.000 | 0.333 | 0.420/0.206/0.630 |
| `oberflaeche_rekoppelt` | `long_btc_sol` | `doge2024` | 12 | `offene_rekopplung` | `offene_rekopplung` (1.00) | 1.000 | 0.500 | 0.333 | 0.385/0.261/0.591 |
| `oberflaeche_rekoppelt` | `multiasset` | `btc2024` | 27 | `tragende_rekopplung` | `tragende_rekopplung` (0.67) | 0.556 | 0.111 | 0.222 | 0.420/0.206/0.630 |
| `oberflaeche_rekoppelt` | `multiasset` | `doge2024` | 18 | `tragende_rekopplung` | `offene_rekopplung` (1.00) | 0.333 | 0.167 | 0.111 | 0.385/0.261/0.591 |
| `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `doge2024` | 12 | `offene_rekopplung` | `offene_rekopplung` (1.00) | 1.000 | 1.000 | 0.167 | 0.376/0.267/0.590 |
| `oberflaeche_rekoppelt_spaet` | `long_btc_sol` | `paxg2024` | 6 | `offene_rekopplung` | `offene_rekopplung` (1.00) | 1.000 | 1.000 | 0.000 | 0.374/0.265/0.590 |
| `oberflaeche_rekoppelt_spaet` | `multiasset` | `doge2024` | 18 | `offene_rekopplung` | `offene_rekopplung` (1.00) | 1.000 | 1.000 | 0.056 | 0.376/0.267/0.590 |
| `oberflaeche_rekoppelt_spaet` | `multiasset` | `paxg2024` | 9 | `offene_rekopplung` | `offene_rekopplung` (1.00) | 1.000 | 1.000 | 0.111 | 0.374/0.265/0.590 |
| `rekopplung_oeffnet` | `long_btc_sol` | `btc2024` | 30 | `spannungsnahe_oeffnung` | `spannungsnahe_oeffnung` (0.80) | 0.800 | 1.000 | 0.267 | 0.368/0.288/0.576 |
| `rekopplung_oeffnet` | `long_btc_sol` | `doge2024` | 42 | `spannungsnahe_oeffnung` | `spannungsnahe_oeffnung` (0.57) | 0.571 | 0.429 | 0.381 | 0.364/0.283/0.578 |
| `rekopplung_oeffnet` | `long_btc_sol` | `paxg2024` | 6 | `spannungsnahe_oeffnung` | `offene_rekopplung` (1.00) | 0.000 | 1.000 | 0.333 | 0.421/0.272/0.602 |
| `rekopplung_oeffnet` | `multiasset` | `btc2024` | 45 | `spannungsnahe_oeffnung` | `spannungsnahe_oeffnung` (0.80) | 0.800 | 1.000 | 0.178 | 0.368/0.288/0.576 |
| `rekopplung_oeffnet` | `multiasset` | `doge2024` | 63 | `spannungsnahe_oeffnung` | `spannungsnahe_oeffnung` (0.57) | 0.571 | 0.429 | 0.063 | 0.364/0.283/0.578 |
| `rekopplung_oeffnet` | `multiasset` | `paxg2024` | 9 | `spannungsnahe_oeffnung` | `offene_rekopplung` (1.00) | 0.000 | 1.000 | 0.222 | 0.421/0.272/0.602 |

## Lesung

Die Rückprüfung trennt klar zwischen Feldrolle und Oberfläche.

Wenn die Feldkontakt-Rückerkennung höher bleibt als Sinnes- oder Rohphasen-Rückerkennung, spricht das dafür, dass die Vorwahrnehmungs-Memory keine bloße Kopie der Außenwelt speichert, sondern eine wiederkehrende MCM-Feldnähe.

Wenn sie fällt, ist das kein Fehler: Dann zeigt der Holdout, dass die Rolle an diese neue Weltspannung nicht stabil anschließt oder sich anders organisieren muss.

## Grenze

Auch diese Rückprüfung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keine Entry-Mechanik.

## Wie es weitergeht

Als nächstes sollte geprüft werden, welche Rollen trotz anderer Oberfläche feldnah wiederkehren. Daraus kann eine robuste Vorwahrnehmungs-Landkarte entstehen, ohne dass MINI_DIO hart programmiert wird.
