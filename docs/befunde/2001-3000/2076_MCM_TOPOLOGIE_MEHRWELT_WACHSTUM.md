# 2076 - MCM-Topologie im Mehrwelt-Wachstum

## Zweck

Befund 2075 zeigte, dass abgeschlossene innere MCM-Episoden online Knoten und gerichtete Kanten bilden können. Diese Prüfung untersucht erstmals, wie dieselbe gemeinsame Topologie durch mehrere vollständige Real-, Folge- und Nullwelten wächst.

Untersucht wird das innere Netz. Die Welten bleiben vollständige Herkunftskontexte und werden nicht in Komponenten zerlegt.

## Welten

Alle Welten besitzen 1000 Beobachtungen derselben BTC-2025-1h-Basis:

- reales Ausgangsfenster `5000_6000`,
- direkt folgendes Realfenster `6000_7000`,
- Shuffle-Order-Nullwelt des Folgefensters,
- Random-Sign-Nullwelt des Folgefensters.

Die Realwelten stammen aus `data/2070_role_family_followworlds.zip`, die Nullwelten aus `data/2073_role_family_null_controls.zip`. Entpackte Welten, Laufmemory und Debugdaten bleiben lokal.

## Reihenfolgenkontrolle

Zwei getrennte frische Memories erhielten dieselben vier Welten in entgegengesetzter Reihenfolge:

```text
real_first:
  Realanker -> Realfolge -> Null-Shuffle -> Null-Random

null_first:
  Null-Shuffle -> Null-Random -> Realanker -> Realfolge
```

## Wachstum

| Reihenfolge | Welt | Knotenbeobachtungen | neue Knoten | Anschlüsse | Kantenbeobachtungen | neue Kanten | Anschlüsse |
|---|---|---:|---:|---:|---:|---:|---:|
| real_first | Realanker | 29 | 19 | 10 | 28 | 27 | 1 |
| real_first | Realfolge | 23 | 7 | 16 | 22 | 16 | 6 |
| real_first | Null-Shuffle | 25 | 4 | 21 | 24 | 14 | 10 |
| real_first | Null-Random | 21 | 3 | 18 | 20 | 8 | 12 |
| null_first | Null-Shuffle | 25 | 16 | 9 | 24 | 24 | 0 |
| null_first | Null-Random | 21 | 6 | 15 | 20 | 12 | 8 |
| null_first | Realanker | 29 | 6 | 23 | 28 | 16 | 12 |
| null_first | Realfolge | 23 | 5 | 18 | 22 | 13 | 9 |

Jede zuerst gelesene Welt legt mehr neue Struktur an. Spätere Welten schließen überwiegend an vorhandene Knoten an, erzeugen aber weiterhin neue gerichtete Folgen.

Beide Reihenfolgen enden exakt bei:

```text
98 Knotenbeobachtungen auf 33 Knoten
94 Kantenbeobachtungen auf 65 Kanten
```

## Reihenfolgenstabilität

| Ebene | real_first | null_first | gemeinsam | Jaccard | unterschiedliche Beobachtungszahlen |
|---|---:|---:|---:|---:|---:|
| globale Knoten | 33 | 33 | 33 | 1.000 | 4 |
| globale Kanten | 65 | 65 | 64 | 0.970 | 4 |

Die Gesamtstruktur ist damit weitgehend unabhängig davon, ob Real- oder Nullwelten zuerst gelesen werden. Die Gewichtung einzelner Elemente bleibt bei vier Knoten und vier Kanten reihenfolgensensitiv.

Auf Weltkontextebene sind die Nullwelten in beiden Reihenfolgen identisch zugeordnet. Realanker und Realfolge zeigen geringe lokale Reihenfolgeneffekte: Der Realanker teilt 25 von 29 über beide Reihenfolgen vorkommenden Kanten, die Realfolge 18 von 20.

## Weltüberlappung

Die innere Identitätsüberlappung ist noch keine belastbare Weltbindung:

| Vergleich | Knoten-Jaccard real_first/null_first | Kanten-Jaccard real_first/null_first |
|---|---:|---:|
| Realanker - Realfolge | 0.231 / 0.280 | 0.070 / 0.095 |
| Realanker - Null-Shuffle | 0.458 / 0.458 | 0.186 / 0.244 |
| Realanker - Null-Random | 0.304 / 0.304 | 0.154 / 0.154 |
| Null-Shuffle - Null-Random | 0.227 / 0.227 | 0.167 / 0.167 |

Der Realanker liegt der Shuffle-Nullwelt in der aktuellen Knotenidentität näher als dem direkt folgenden Realfenster. Das widerlegt eine vorschnelle Lesung, nach der gemeinsame Knoten bereits reale zeitliche Bedeutung tragen.

## Befund

Die erste wachsende Topologie trägt drei wichtige Eigenschaften:

- neue vollständige Welten können bestehende innere Struktur wiederverwenden,
- neue Varianten und gerichtete Folgen können weiter wachsen,
- der globale Graph bleibt unter umgekehrter Weltreihenfolge nahezu gleich.

Noch nicht getragen ist eine semantische Welttrennung. Die derzeitige Episodenidentität bildet allgemeine Feldordnung und wiederkehrende Folgen ab, aber der direkte Realfolge-Anschluss hebt sich nicht von Nullweltähnlichkeit ab.

## Grenze

Aus diesem Stand darf keine Resonanz auf das Feld zurückwirken. Der nächste Forschungsschritt muss innerhalb der inneren Folge prüfen, ob längere gerichtete Motive und kontinuierliche Feldprofilabstände den Realfolge-Anschluss sichtbar machen, ohne äußere Chartmerkmale zur Identität zu erheben.

Reproduzierbare Ausgaben:

- `2076_MCM_TOPOLOGIE_MEHRWELT_WACHSTUM.summary.csv`
- `2076_MCM_TOPOLOGIE_MEHRWELT_WACHSTUM.overlap.csv`
- `2076_MCM_TOPOLOGIE_MEHRWELT_WACHSTUM.order.csv`
