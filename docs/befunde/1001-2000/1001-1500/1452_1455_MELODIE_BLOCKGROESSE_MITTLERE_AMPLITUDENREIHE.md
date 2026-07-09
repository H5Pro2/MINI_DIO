# 1452-1455 - Melodie, Blockgroesse und mittlere Amplitudenreihe

## Zweck

Diese Pruefung ergaenzt den Befund `1448-1451`.

Die Grundfrage war:

Kann der Umschlag zwischen `dio_0ein` und `dio_1fll` durch eine mittlere Weltlautstaerke genauer eingegrenzt werden?

## Aufbau

Es wurden vier synthetische Welten erzeugt:

- `block_size 12`, Amplitude `0.00095`
- `block_size 13`, Amplitude `0.00095`
- `block_size 12`, Amplitude `0.00105`
- `block_size 13`, Amplitude `0.00105`

Die Welten wurden aus den vorherigen quiet/loud-Referenzen interpoliert. Dadurch bleiben die Richtungswechsel der Referenzstruktur erhalten:

- `block_size 12`: `458` Richtungswechsel
- `block_size 13`: `455` Richtungswechsel

Die Amplitudenwerte sind Pruefwerte, keine festen Regeln.

## Ergebnis

| Welt | Block | Amp | Symbole | stabil | unruhig | dominant | zweit | Rekopplung | Nachhall |
|---|---:|---:|---:|---:|---:|---|---|---:|---:|
| 1452 | 12 | 0.00095 | 47 | 1146 | 48 | `dio_0ein` 188 | `dio_1fll` 173 | 0.733961 | 0.582416 |
| 1453 | 13 | 0.00095 | 46 | 1150 | 44 | `dio_0ein` 186 | `dio_1fll` 173 | 0.734215 | 0.584327 |
| 1454 | 12 | 0.00105 | 48 | 1140 | 54 | `dio_0ein` 181 | `dio_1fll` 174 | 0.732953 | 0.573465 |
| 1455 | 13 | 0.00105 | 48 | 1144 | 50 | `dio_0ein` 179 | `dio_1fll` 174 | 0.733182 | 0.574922 |

## Befund

Im mittleren Lautstaerkebereich bleibt `dio_0ein` dominant.

`dio_1fll` liegt aber sehr nahe dahinter:

- bei `0.00095`: Abstand `13-15` Zaehler,
- bei `0.00105`: Abstand `5-7` Zaehler.

Damit liegt der Kippraum nicht einfach zwischen `block_size 12` und `13`, sondern in einer gekoppelten Flaeche aus:

- Blockdauer,
- Weltlautstaerke,
- Nachhall,
- Rekopplung,
- Symbolstreuung.

## Vergleich Zu Quiet Und Loud

Die quiet-Welten `0.00080` hatten `dio_1fll` dominant.

Die mittleren Welten `0.00095` und `0.00105` kippen wieder knapp zu `dio_0ein`.

Die loud-Welten `0.00150` hatten erneut `dio_1fll` dominant, aber mit hoeherer Fragmentierung.

Das ist wichtig:

Die Lautstaerke wirkt nicht linear.

Leiser bedeutet nicht automatisch `dio_1fll`, lauter bedeutet nicht automatisch `dio_0ein`. Stattdessen entsteht ein gekruemmter Schwellenraum.

## Lesung

MINI_DIO reagiert nicht nur auf eine einzelne Achse.

Die Symbolbildung wirkt wie eine Feldantwort auf kombinierte Bedingungen:

- wie lange ein Block gehalten wird,
- wie laut die Welt wirkt,
- wie stark der Nachhall bleibt,
- wie sauber die Rekopplung gelingt,
- ob die Topologie eng bleibt oder streut.

Die mittlere Reihe zeigt deshalb keine harte Grenze, sondern einen Naehebereich.

## Schlussfolgerung

Der bisherige Befund `Blockdauer x Weltlautstaerke` wird bestaetigt, aber verfeinert:

Es handelt sich nicht um eine lineare Schwelle, sondern um einen gekruemmten Kippraum.

`dio_0ein` und `dio_1fll` liegen hier als nahe Feldnachbarn im gleichen Bedeutungsraum. Die Dominanz wechselt nicht sauber mechanisch, sondern in Abhaengigkeit der gekoppelten Feldbedingungen.

## Grenze

Diese Pruefung beweist keine allgemeine Topologieform.

Sie zeigt aber, dass die gleiche synthetische Melodiestruktur bei kontrollierter Lautstaerkevariation unterschiedliche, aber nachvollziehbare Dominanznaehen erzeugt.
