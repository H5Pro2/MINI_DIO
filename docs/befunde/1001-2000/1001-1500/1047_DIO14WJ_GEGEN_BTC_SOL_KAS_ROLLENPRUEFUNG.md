# 1047 - `dio_14wj` gegen BTC, SOL und KAS: Rollenpruefung

## Zweck

Diese Pruefung nimmt die vorgemerkte Frage aus 1046 wieder auf:

```text
Ist `dio_14wj` eine PAXG-spezifische Rolle
oder eine allgemeinere ruhige Rekopplungsrolle,
die in anderen Welten ebenfalls auftreten kann?
```

Wichtig:

Es wurde nicht nur geprueft, ob das Zeichen `dio_14wj` vorkommt.

Geprueft wurde auch, ob eine vergleichbare ruhige Rekopplungsrolle durch andere Familien getragen wird.

## Datengrundlage

Erzeugte Messdateien:

- `1047_DIO14WJ_ASSET_ROLLENPRUEFUNG.csv`
- `1047_RUHIGE_REKOPPLUNGSROLLEN_ASSET_KANDIDATEN.csv`
- `1047_ALLE_FAMILIEN_ASSET_ROLLENMATRIX.csv`

Gepruefte Welten:

- `BTC_2024_5M`
- `SOL_2024_5M`
- `KAS_2024_5M`
- `PAXG_2024_5M`
- `PAXG_2024_5M_10K`
- `PAXG_2025_5M_10K`

## Befund 1: `dio_14wj` existiert auch in BTC, SOL und KAS

| Welt | Anzahl | Anteil | Rekopplung | Carry | Strain | Sinnes-MCM | Ruhe-Score |
|---|---:|---:|---:|---:|---:|---:|---:|
| BTC_2024_5M | 50 | 0.025075 | 0.727446 | 0.561839 | 0.122479 | 0.869906 | 0.792676 |
| SOL_2024_5M | 31 | 0.015547 | 0.722582 | 0.550603 | 0.125499 | 0.863187 | 0.787237 |
| KAS_2024_5M | 41 | 0.020562 | 0.725265 | 0.557212 | 0.123504 | 0.867425 | 0.790559 |
| PAXG_2024_5M | 109 | 0.054664 | 0.739869 | 0.573728 | 0.129651 | 0.874041 | 0.797899 |
| PAXG_2024_5M_10K | 530 | 0.053032 | 0.743973 | 0.582428 | 0.130787 | 0.874362 | 0.800094 |
| PAXG_2025_5M_10K | 708 | 0.070843 | 0.743199 | 0.586935 | 0.131257 | 0.873902 | 0.800702 |

Lesung:

`dio_14wj` ist nicht PAXG-exklusiv.

Die Familie erscheint auch in BTC, SOL und KAS als stabile Feldlage.

Aber:

In PAXG ist sie deutlich haeufiger, traegt mehr Rekopplung, mehr Carry und mehr Nachhall.

## Befund 2: Die Rolle bleibt gleich, die Dominanz aendert sich

In allen geprueften Welten ist `dio_14wj`:

- dominant `stabil`,
- mit niedriger Kontaktspannung,
- mit sehr niedrigem Hoer-Feld-Gap,
- mit niedriger gefuehlter Druckwirkung,
- mit guter Sinnes-MCM-Kopplung.

Die Rolle bleibt also erkennbar.

Was sich aendert, ist ihre Dominanz:

```text
BTC/SOL/KAS: seltenere ruhige Rolle
PAXG: deutlich breitere und staerker nachhallende ruhige Rolle
```

Damit ist `dio_14wj` keine reine PAXG-Erfindung, aber PAXG scheint diese Rolle staerker zu tragen.

## Befund 3: Andere Familien koennen lokal aehnlich ruhige Rollen tragen

Die Kandidatenmatrix zeigt:

In BTC, SOL und KAS gibt es andere Familien, die lokal hoehere oder aehnliche Ruhe-Rekopplungswerte erreichen.

Beispiele:

- BTC: `dio_1fll`, `dio_0ly7`, `dio_0nlj`
- SOL: `dio_0kx9`, `dio_0nlj`, `dio_1jc2`
- KAS: `dio_1492`, `dio_0nlj`, `dio_0kx9`
- PAXG: `dio_1fll`, `dio_0g3b`, `dio_13o0`, neben `dio_14wj`

Das ist entscheidend:

```text
Rolle ist allgemeiner als Token.
Syntax ist weltabhaengig.
Feldfunktion kann von mehreren Familien getragen werden.
```

## Befund 4: `dio_14wj` ist kein reiner Top-Score-Sieger

`dio_14wj` ist nicht in jeder Welt der hoechstbewertete Ruhekandidat.

Trotzdem ist es relevant, weil es:

- assetuebergreifend erscheint,
- in PAXG deutlich breiter wird,
- in PAXG 2024 und 2025 reproduzierbar bleibt,
- auf 5m und 1h sichtbar ist,
- eine klare niedrige Kontakt-/Hoerlast traegt.

Das unterscheidet `dio_14wj` von kleinen lokalen Top-Score-Familien, die zwar sehr ruhig wirken, aber oft nur wenige Beobachtungen tragen.

## Schlussfolgerung

Die bisherige PAXG-Lesung muss praezisiert werden:

```text
`dio_14wj` ist keine PAXG-exklusive Familie.
`dio_14wj` ist eine allgemeiner auftretende ruhige Rekopplungsrolle.
PAXG aktiviert und verbreitert diese Rolle deutlich staerker.
```

Damit ergibt sich:

```text
PAXG-Spezifik liegt nicht im exklusiven Zeichen.
PAXG-Spezifik liegt in der Dominanz, Breite, Rekopplung und Nachhallstaerke dieser Rolle.
```

## Bedeutung fuer MINI_DIO

Dieser Befund stuetzt die Richtung aus 1046:

Nicht das einzelne Zeichen allein ist entscheidend.

Entscheidend ist die wiederkehrende Feldrolle.

MINI_DIO muss deshalb in der weiteren Forschung unterscheiden:

- Syntaxzeichen,
- Familienbreite,
- Feldrolle,
- Weltfaerbung,
- Zeitauflösung,
- Nachhall,
- Reproduktionsnaehe.

## Forschungskonsequenz

Die naechste Ebene sollte nicht lauten:

```text
Wo kommt `dio_14wj` vor?
```

Sondern:

```text
Welche Familien tragen die ruhige Rekopplungsrolle je Welt?
Welche davon sind lokal, welche weltuebergreifend, welche zeitebenenstabil?
```

## Wie es weitergeht

Als naechstes sollte eine Rollenbibliothek fuer `ruhige_rekopplung` aufgebaut werden. Diese Bibliothek liest nicht ein einzelnes `dio_*`-Zeichen, sondern sammelt Familien, die wiederholt niedrige Kontaktlast, hohe Rekopplung, stabile Wirkung und tragenden Nachhall zeigen.
