# 1456-1459 - Melodie, Blockgroesse und obere Amplitudenreihe

## Zweck

Diese Pruefung setzt die Amplitudenreihe fort.

Die konkrete Unterfrage war:

Uebernimmt `dio_1fll` zwischen `0.00105` und `0.00150` graduell wieder, oder entsteht eine neue Zwischeninsel?

## Aufbau

Es wurden vier synthetische Welten erzeugt:

- `block_size 12`, Amplitude `0.00120`
- `block_size 13`, Amplitude `0.00120`
- `block_size 12`, Amplitude `0.00135`
- `block_size 13`, Amplitude `0.00135`

Die Welten wurden aus den quiet/loud-Referenzen gleicher Blockgroesse interpoliert.

Damit bleibt die Melodiestruktur vergleichbar:

- `block_size 12`: `458` Richtungswechsel
- `block_size 13`: `455` Richtungswechsel

## Ergebnis

| Welt | Block | Amp | Symbole | stabil | unruhig | dominant | zweit | Rekopplung | Nachhall |
|---|---:|---:|---:|---:|---:|---|---|---:|---:|
| 1456 | 12 | 0.00120 | 53 | 1131 | 63 | `dio_1fll` 173 | `dio_0ein` 172 | 0.731447 | 0.564035 |
| 1457 | 13 | 0.00120 | 52 | 1136 | 58 | `dio_1fll` 173 | `dio_0ein` 169 | 0.731707 | 0.565224 |
| 1458 | 12 | 0.00135 | 60 | 1116 | 78 | `dio_1fll` 172 | `dio_0ein` 162 | 0.730254 | 0.563986 |
| 1459 | 13 | 0.00135 | 58 | 1120 | 74 | `dio_1fll` 172 | `dio_0ein` 159 | 0.730477 | 0.563764 |

## Befund

Ab `0.00120` uebernimmt `dio_1fll` wieder.

Der Uebergang ist aber zuerst extrem knapp:

- bei `0.00120 / block_size 12`: `dio_1fll` liegt nur `1` Zaehler vor `dio_0ein`,
- bei `0.00120 / block_size 13`: `dio_1fll` liegt `4` Zaehler vor `dio_0ein`.

Bei `0.00135` wird die Dominanz klarer:

- Abstand `10` bei `block_size 12`,
- Abstand `13` bei `block_size 13`.

Gleichzeitig steigen Symbolstreuung und tragende Unruhe.

## Lesung

Die obere Amplitudenreihe zeigt keinen neuen Hauptanker.

Stattdessen wirkt `dio_1fll` wie die wiederkehrende Bedeutung fuer lautere, staerker fokussierende Melodieabschnitte.

`dio_0ein` bleibt aber als direkter Nachbar sichtbar. Das spricht gegen eine harte Umschaltung und fuer einen Uebergangsraum, in dem beide Bedeutungen eng gekoppelt sind.

## Vergleich Mit Vorreihe

Die mittlere Reihe `0.00095 / 0.00105` hielt `dio_0ein` knapp dominant.

Die obere Reihe `0.00120 / 0.00135` kippt wieder zu `dio_1fll`.

Damit liegt der beobachtete Dominanzwechsel zwischen `0.00105` und `0.00120`.

Dieser Bereich ist kein fixer Grenzwert, sondern ein Prueffenster.

## Schlussfolgerung

Die Amplitudenreihe bestaetigt einen gekruemmten Schwellenraum:

`Blockdauer x Weltlautstaerke x Nachhall x Rekopplung`

Die Feldantwort bildet keine einfache lineare Lautstaerkeordnung.

Stattdessen entstehen nahe Bedeutungsnachbarn, die je nach Weltspannung und Feldzeit die Dominanz wechseln koennen.

## Grenze

Die Werte sind Pruefwerte, keine Regeln.

Der Befund sagt nicht, dass `0.00120` generell eine feste Kante ist. Er zeigt nur, dass in dieser kontrollierten Melodiekonstruktion dort der beobachtete Uebergang zwischen `dio_0ein` und `dio_1fll` beginnt.

## Wie es weitergeht

Als naechstes sollte der enge Bereich `0.00108` bis `0.00118` geprueft werden. Ziel ist, den unmittelbaren Dominanzwechsel feiner zu lokalisieren und zu sehen, ob die Umschaltung weich oder sprunghaft wirkt.
