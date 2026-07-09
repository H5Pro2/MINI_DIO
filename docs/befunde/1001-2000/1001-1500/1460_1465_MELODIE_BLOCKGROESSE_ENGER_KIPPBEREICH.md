# 1460-1465 - Melodie, Blockgroesse und enger Kippbereich

## Zweck

Diese Pruefung verengt den zuvor gefundenen Uebergangsbereich zwischen `dio_0ein` und `dio_1fll`.

Die konkrete Unterfrage war:

Kippt die Dominanz im Bereich `0.00108` bis `0.00116` sprunghaft, oder bildet MINI_DIO ein weiches Schwellenband?

## Aufbau

Getestet wurden sechs synthetische Welten:

- `block_size 12`, Amplitude `0.00108`
- `block_size 13`, Amplitude `0.00108`
- `block_size 12`, Amplitude `0.00112`
- `block_size 13`, Amplitude `0.00112`
- `block_size 12`, Amplitude `0.00116`
- `block_size 13`, Amplitude `0.00116`

Alle Welten wurden aus den vorherigen quiet/loud-Referenzen gleicher Blockgroesse interpoliert.

Damit bleibt die Melodiestruktur vergleichbar:

- `block_size 12`: `458` Richtungswechsel
- `block_size 13`: `455` Richtungswechsel

## Ergebnis

| Welt | Block | Amp | Symbole | stabil | unruhig | dominant | zweit | Abstand | Rekopplung | Nachhall |
|---|---:|---:|---:|---:|---:|---|---|---:|---:|---:|
| 1460 | 12 | 0.00108 | 50 | 1138 | 56 | `dio_0ein` 177 | `dio_1fll` 174 | 3 | 0.732602 | 0.570801 |
| 1461 | 13 | 0.00108 | 49 | 1142 | 52 | `dio_0ein` 175 | `dio_1fll` 174 | 1 | 0.732864 | 0.572406 |
| 1462 | 12 | 0.00112 | 54 | 1136 | 58 | `dio_0ein` 174 | `dio_1fll` 173 | 1 | 0.732079 | 0.567573 |
| 1463 | 13 | 0.00112 | 51 | 1140 | 54 | Gleichlage | Gleichlage | 0 | 0.732461 | 0.570924 |
| 1464 | 12 | 0.00116 | 53 | 1133 | 61 | `dio_0ein` 175 | `dio_1fll` 173 | 2 | 0.731768 | 0.567403 |
| 1465 | 13 | 0.00116 | 52 | 1137 | 57 | `dio_1fll` 173 | `dio_0ein` 172 | 1 | 0.732065 | 0.569554 |

## Befund

Der Uebergang ist kein harter Sprung.

Im engen Kippbereich liegen `dio_0ein` und `dio_1fll` fast deckungsgleich:

- `0.00108`: `dio_0ein` liegt noch knapp vorne.
- `0.00112 / block_size 13`: beide Bedeutungen liegen exakt gleich.
- `0.00116 / block_size 13`: `dio_1fll` uebernimmt knapp.

Bei `block_size 12` haelt `dio_0ein` etwas laenger.

Damit wirkt die Blockgroesse wie ein zweiter Feldzeitparameter, der die Lautstaerke-Schwelle verschiebt.

## Lesung

MINI_DIO bildet hier kein mechanisches Wenn-Dann-Verhalten.

Das Feld zeigt ein Schwellenband:

`dio_0ein` und `dio_1fll` liegen als direkte Bedeutungsnachbarn nebeneinander. Die Dominanz wechselt erst, wenn Lautstaerke und Blockdauer gemeinsam genug Feldnaehe verschieben.

Die Gleichlage bei `0.00112 / block_size 13` ist dabei der bisher klarste Hinweis auf einen Uebergangspunkt innerhalb dieses konstruierten Melodieraums.

## Schlussfolgerung

Der Kippbereich liegt in dieser Pruefreihe nicht als Einzelwert vor, sondern als weiches Band:

`0.00108` bis `0.00116`

Innerhalb dieses Bands entscheidet nicht nur die Lautstaerke, sondern auch die Blockdauer.

Fachlich sauberer ist deshalb:

`Blockdauer x Weltlautstaerke` erzeugt ein Schwellenband, nicht eine harte Grenze.

## Grenze

Die Amplitudenwerte sind Pruefwerte, keine Regeln.

Der Befund gilt fuer diese synthetische Melodiestruktur. Er zeigt eine reproduzierbare Naehe im Feld, aber noch keine allgemeine MCM-Gesetzmaessigkeit.
