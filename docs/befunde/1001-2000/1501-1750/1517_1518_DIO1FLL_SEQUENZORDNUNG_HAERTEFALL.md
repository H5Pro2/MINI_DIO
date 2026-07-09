# 1517/1518 - DIO_1FLL Sequenzordnung-Härtefall

## Zweck

Nach 1515/1516 war offen, ob `dio_1fll` eine geordnete Rand-/Bruchstruktur braucht.

Diese Prüfung trennt die Frage hierarchisch:

1. Bleibt `dio_1fll` bei stark permutierter Bruch-/Randsequenz erhalten?
2. Bleibt `dio_1fll` auch bei zufallsnaher Bruch-/Randsequenz erhalten?

## Datenbasis

Geprüft wurden zwei synthetische Welten mit frischer Memory:

```text
1517: data/kontrolliert_synthetic_mcm_sequenz_bruch_rand_stark_permutiert_5m.csv
1518: data/kontrolliert_synthetic_mcm_sequenz_bruch_rand_zufallsnah_5m.csv
```

Beide wurden mit `world_relative` und je zwei Läufen ausgeführt.

## Ergebnis

`dio_1fllaqz` bleibt in beiden Welten das dominante Symbol.

| Welt | Top Symbol | Top Count pro Lauf | Unique Symbols | Stable Ratio | Carried Unrest | Avg Afterimage |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1517 stark permutiert | `dio_1fllaqz` | 3089 | 173 | 0.9539 | 0.0455 | 0.6963 |
| 1518 zufallsnah | `dio_1fllaqz` | 3030 | 167 | 0.9517 | 0.0473 | 0.6883 |

Die bisherigen Geschwisterrollen erscheinen erneut nicht:

| Welt | `dio_0l7p` | `dio_14wj` | `dio_1wdi` | `dio_1fll` |
| --- | ---: | ---: | ---: | ---: |
| 1517 Lauf 1 | 0 | 0 | 0 | 3089 |
| 1517 Lauf 2 | 0 | 0 | 0 | 6178 |
| 1518 Lauf 1 | 0 | 0 | 0 | 3030 |
| 1518 Lauf 2 | 0 | 0 | 0 | 6060 |

Die höheren Counts in Lauf 2 sind kumulative Memory-Zählungen. Der Top-Count pro Lauf bleibt stabil.

## Deutung

`dio_1fll` braucht nach aktuellem Stand keine sauber geordnete Rand-/Bruchsequenz.

Die Rolle bleibt erhalten bei:

- Randdominanz A,
- Randdominanz B,
- Bruch/Rand A,
- stark permutierter Bruch-/Randsequenz,
- zufallsnaher Bruch-/Randsequenz.

Damit ist `dio_1fll` nicht nur als Antwort auf Sequenzordnung zu lesen, sondern als robuste passive Rand-/Bruch-Feldrolle.

Wichtig ist die Qualität der Innenfeldantwort:

```text
viel Stable,
wenig Carried Unrest,
kaum Strain,
kaum Tipping,
starker Nachhall.
```

Das spricht dafür, dass MINI_DIO in diesen Welten nicht die konkrete Reihenfolge als Hauptanker liest, sondern eine übergeordnete Rand-/Bruch-Feldqualität.

## MCM-Deutung

Der Befund verschiebt die Bedeutung von `dio_1fll`.

Vorher:

```text
dio_1fll = synthetische Rand-/Bruch-Tragung
```

Jetzt präziser:

```text
dio_1fll = robuste Rand-/Bruch-Feldqualität, die auch bei zerstörter Sequenzordnung tragend bleibt
```

Das ist für die MCM-Forschung wichtig, weil hier nicht nur Wiederholung einer Folge sichtbar wird. Sichtbar wird eine Feldrolle, die trotz veränderter Oberfläche erhalten bleibt.

## Grenze

Das ist kein Beweis für allgemeine Invarianz.

Noch offen:

- Wie weit darf die Rand-/Bruchqualität abgeschwächt werden?
- Kippt `dio_1fll`, wenn Rand/Bruch mit ruhigen Zentrumspassagen gemischt wird?
- Entsteht eine Mischrolle, wenn Rand-/Bruchqualität und reale Asset-Spuren kombiniert werden?
