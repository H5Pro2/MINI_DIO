# Befund 290 - Asset- und Zeitebenenvergleich

Stand: 2026-06-19

## Zweck

Diese Prüfung vergleicht KAS, SOL und BTC über dieselben Zeitebenen:

- 5m
- 15m
- 30m
- 1h

Alle Läufe nutzen 2024-Daten, 2000 Zeilen, frisches Memory und `world_relative`.

Die Frage ist nicht, ob MINI_DIO handelt. Die Frage ist, ob das MCM-Innenfeld bei unterschiedlichen Außenwelten dieselbe Rollenordnung hält oder ob bestimmte Assets oder Zeitebenen die Topologie verschieben.

## Datengrundlage

Matrix:

- `docs/befunde/289_ASSET_ZEITEBENEN_VERGLEICH_TOPOLOGIE_MATRIX.md`
- `docs/befunde/289_ASSET_ZEITEBENEN_VERGLEICH_TOPOLOGIE_MATRIX.csv`

Verwendete Läufe:

- `debug/adapt_kas_2024_5m_2k`
- `debug/adapt_kas_2024_15m_2k`
- `debug/adapt_kas_2024_30m_2k`
- `debug/adapt_kas_2024_1h_2k`
- `debug/adapt_sol_2024_5m_2k`
- `debug/adapt_sol_2024_15m_2k`
- `debug/adapt_sol_2024_30m_2k`
- `debug/adapt_sol_2024_1h_2k`
- `debug/adapt_btc_2024_5m_2k`
- `debug/adapt_btc_2024_15m_2k`
- `debug/adapt_btc_2024_30m_2k`
- `debug/adapt_btc_2024_1h_2k`

## Kernergebnis

Alle 12 geprüften Welten bilden denselben Topologiezustand:

`zentrum_mit_rand_und_uebergang`

Das ist wichtig: Die Topologie kollabiert nicht, wenn Asset und Zeitebene wechseln. MINI_DIO bleibt nicht bei einer einzelnen Welt hängen, sondern hält eine wiedererkennbare Rollenordnung aus Zentrum, offener Variante und Spannungsrand.

## Zeitebenenwirkung

KAS:

- 5m: Zentrum `0.8004`, Offen `0.1575`
- 15m: Zentrum `0.8004`, Offen `0.1545`
- 30m: Zentrum `0.7894`, Offen `0.1680`
- 1h: Zentrum `0.7984`, Offen `0.1560`

KAS zeigt bei 30m die stärkste Öffnung. Das wirkt wie eine lokale Zwischenebenenreaktion, nicht wie ein Bruch.

SOL:

- 5m: Zentrum `0.8074`, Offen `0.1454`
- 15m: Zentrum `0.8059`, Offen `0.1489`
- 30m: Zentrum `0.8014`, Offen `0.1605`
- 1h: Zentrum `0.8059`, Offen `0.1515`

SOL zeigt denselben Grundzug wie KAS: 30m öffnet stärker als 5m, 15m und 1h.

BTC:

- 5m: Zentrum `0.8280`, Offen `0.1324`
- 15m: Zentrum `0.8415`, Offen `0.1113`
- 30m: Zentrum `0.8220`, Offen `0.1284`
- 1h: Zentrum `0.8119`, Offen `0.1389`

BTC bleibt insgesamt zentrumsnäher. Hier ist nicht 30m die stärkste Öffnung, sondern 1h. BTC wirkt in dieser Prüfung stabiler und weniger offen als KAS und SOL.

## Interpretation

Die 30m-Öffnung ist nicht rein KAS-spezifisch, weil SOL dasselbe Muster zeigt. Sie ist aber auch kein universelles Gesetz, weil BTC anders reagiert.

Fachlich sauberer Befund:

MINI_DIO zeigt eine assetabhängige Zeitebenenreaktion. Bei KAS und SOL öffnet die 30m-Welt stärker. Bei BTC bleibt das Feld zentrumsnäher und verschiebt seine stärkere Öffnung eher in Richtung 1h.

Das spricht dafür, dass die MCM-Feldordnung nicht nur Rohdaten skaliert, sondern die Weltspannung asset- und zeitebenenbezogen unterschiedlich aufnimmt.

## Bedeutung für MINI_DIO

Dieser Befund hilft an drei Stellen:

1. Die Topologie bleibt robust.
2. Die Öffnung ist messbar, aber weltabhängig.
3. Die Feldreaktion wirkt nicht starr, sondern adaptiv.

Damit wird die bisherige Hypothese gestützt:

MINI_DIO bildet keine fest programmierte Topologie ab. Das Feld liest unterschiedliche Außenwelten und hält dabei eine wiederkehrende innere Rollenordnung, deren Gewichtung sich je nach Weltspannung verschiebt.

## Grenze des Befunds

Das ist noch kein endgültiger Beweis. Es ist ein reproduzierbarer Befund innerhalb der aktuellen Daten, des aktuellen Codes und der geprüften 2024-Welten.

Für eine stärkere Aussage braucht es:

- Reproduktion der 12-Welten-Matrix
- Vergleich mit 2023 und 2025
- Prüfung längerer Ausschnitte
- Prüfung, ob die Zeitebenenöffnung mit konkreten Sinnesachsen zusammenhängt

## Wie es weitergeht

Als nächstes sollte die 12-Welten-Matrix reproduziert werden. Wenn sie stabil bleibt, prüfen wir, welche Sinnesachse die Öffnung trägt: Sehen, Hören, Feldwirkung oder deren Rekopplung.
