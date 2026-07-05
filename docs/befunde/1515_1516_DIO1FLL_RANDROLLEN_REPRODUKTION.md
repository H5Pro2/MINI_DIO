# 1515/1516 - DIO_1FLL Randrollen-Reproduktion

## Zweck

Nach Befund 1514 war offen, ob `dio_1fll` nur eine Spezialantwort auf eine einzelne synthetische Randdominanz-Welt ist.

Diese Prüfung trennt zwei Unterfragen:

1. Reproduziert sich `dio_1fll` in einer zweiten Randdominanz-Welt?
2. Erscheint `dio_1fll` auch in einer anderen Rand-/Bruchwelt?

## Datenbasis

Geprüft wurden zwei Welten mit frischer Memory:

```text
1515: data/kontrolliert_synthetic_mcm_rand_dominanz_b_5m.csv
1516: data/kontrolliert_synthetic_mcm_bruch_rand_a_5m.csv
```

Beide wurden mit `world_relative` und je zwei Läufen ausgeführt.

## Ergebnis

`dio_1fll` erscheint in beiden Welten als dominante Familie.

| Welt | Top Symbol | Top Count pro Lauf | Unique Symbols | Stable Ratio | Carried Unrest | Avg Afterimage |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1515 Randdominanz B | `dio_1fllaqz` | 3695 | 226 | 0.9313 | 0.0680 | 0.6477 |
| 1516 Bruch/Rand A | `dio_1fllaqz` | 3236 | 170 | 0.9531 | 0.0464 | 0.6943 |

Die bisherigen Geschwisterrollen erscheinen in diesen Welten nicht:

| Welt | `dio_0l7p` | `dio_14wj` | `dio_1wdi` | `dio_1fll` |
| --- | ---: | ---: | ---: | ---: |
| 1515 Lauf 1 | 0 | 0 | 0 | 3695 |
| 1515 Lauf 2 | 0 | 0 | 0 | 7390 |
| 1516 Lauf 1 | 0 | 0 | 0 | 3236 |
| 1516 Lauf 2 | 0 | 0 | 0 | 6472 |

Der höhere Count in Lauf 2 ist wieder die kumulative Memory-Zählung. Die Top-Symbol-Zahl pro Lauf bleibt stabil.

## Deutung

`dio_1fll` ist keine Einzelantwort auf Randdominanz A.

Die Rolle reproduziert sich:

- in Randdominanz A,
- in Randdominanz B,
- in Bruch/Rand A.

Damit ist `dio_1fll` als passive Rand-/Bruch-Tragungsrolle zu behandeln.

Wichtig: Diese Rolle wirkt nicht wie ein Kollaps.

Trotz synthetischer Rand-/Bruchstruktur bleiben die Läufe überwiegend stabil und rekoppelt:

- hohe stabile Innenfeldwirkung,
- hoher Nachhall,
- niedriger Strain,
- sehr geringe Kipp-/Strain-Anteile.

Das bedeutet:

```text
Rand/Bruch wird von MINI_DIO nicht einfach als Überlast gelesen.
Rand/Bruch kann als eigene tragende Feldrolle verdichtet werden.
```

## Abgrenzung Zu DIO_14WJ

`dio_14wj` bleibt die Rolle ruhiger sensorischer Rekopplungsnähe in Realwelten wie PAXG, SOL und DOGE.

`dio_1fll` übernimmt dagegen synthetische Rand-/Bruchwelten.

Die Grenze wird dadurch sauberer:

```text
dio_14wj = ruhige Rekopplungsnähe bei realweltlicher Färbung
dio_1fll = synthetische Rand-/Bruch-Tragung mit starkem Nachhall
```

## MCM-Deutung

Der Rollenatlas gewinnt dadurch eine neue wichtige Differenzierung.

Eine Randlage kann im MCM-Feld unterschiedlich erscheinen:

1. als ruhige Rekopplungsnähe,
2. als fokussierte Wechselnähe,
3. als nachhallender Randbruch,
4. als dominante Rand-/Bruch-Tragung.

`dio_1fll` gehört derzeit zur vierten Kategorie.

Damit zeigt MINI_DIO nicht nur, dass Rand und Zentrum getrennt werden. Es zeigt auch, dass verschiedene Arten von Randkontakt eigene reproduzierbare Feldrollen bilden können.

## Grenze

Noch offen ist, ob `dio_1fll` auch in weiteren synthetischen Varianten stabil bleibt:

- Bruch/Rand B,
- stark permutierte Bruch-/Randsequenz,
- zufallsnahe Bruch-/Randsequenz,
- Zeitdehnung der Randdominanz.

## Wie es weitergeht

Als nächstes sollte `dio_1fll` gegen eine permutierte oder zufallsnahe Bruch-/Randsequenz geprüft werden.

Die konkrete Frage:

```text
Braucht dio_1fll geordnete Rand-/Bruchstruktur,
oder erscheint die Rolle auch bei zerstörter Sequenzordnung?
```
