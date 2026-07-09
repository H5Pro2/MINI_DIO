# 1684 - Adaptive Milieu-Langfensterpruefung

## Fragestellung

Nach der 1683-Mehrweltpruefung wurde geprueft, ob `milieu_offen` bei laengerem Weltkontakt verschwindet oder ob offene Milieus neben gereifter Rollen- und Pfadnaehe bestehen bleiben.

Untersuchte Langfenster:

- DOGE 2024 5m, 5000er Fenster
- XRP 2024 5m, 5000er Fenster
- PAXG 2024 5m, 5000er Fenster
- Stress-Gegenwelt, 2000er Fenster

Alle Laeufe wurden mit frischer Memory und `calibrated_relative` Sinnesmodus ausgefuehrt.

## Kompakter Befund

| Welt | Ticks | statische Rekopplung | adaptive Rekopplung | Rollenerfahrung | Pfaderfahrung |
|---|---:|---:|---:|---:|---:|
| DOGE | 4994 | 0.697275 | 0.737187 | 0.514167 | 0.158766 |
| XRP | 4994 | 0.691239 | 0.731611 | 0.516370 | 0.206948 |
| PAXG | 4994 | 0.706663 | 0.747072 | 0.590058 | 0.218712 |
| Stress | 1994 | 0.688442 | 0.730818 | 0.588599 | 0.298646 |

Die adaptive Rekopplung bleibt in allen Langfenstern ueber der statischen Referenz.

## Milieu-Verteilung

| Welt | offen | rollennah | pfadnah | Rolle und Pfad getragen | untrainiert |
|---|---:|---:|---:|---:|---:|
| DOGE | 2319 | 1832 | 359 | 472 | 12 |
| XRP | 2322 | 1604 | 412 | 650 | 6 |
| PAXG | 2134 | 1695 | 234 | 925 | 6 |
| Stress | 834 | 537 | 109 | 507 | 7 |

`milieu_offen` bleibt in allen Welten erhalten. Laengere Feldzeit fuehrt also nicht einfach zu vollstaendiger Schliessung oder Reifung.

Gleichzeitig wachsen rollennahe und gemeinsam getragene Bereiche deutlich mit. Das Feld bildet dadurch eine Koexistenz:

```text
offener Bedeutungsraum
  + rollennahe Erfahrung
  + pfadnahe Teilspur
  + gemeinsam getragene Rekopplung
```

## Innenfeldwirkung

| Welt | stabil | tragend_unruhig | kippend | gespannt |
|---|---:|---:|---:|---:|
| DOGE | 3587 | 1362 | 44 | 1 |
| XRP | 3306 | 1621 | 64 | 3 |
| PAXG | 4026 | 939 | 26 | 3 |
| Stress | 1403 | 563 | 28 | 0 |

PAXG bleibt in diesem Langfenster am staerksten stabil und am wenigsten unruhig. XRP traegt mehr `tragend_unruhig` und mehr Kippnaehe. DOGE liegt dazwischen. Stress bleibt belasteter als PAXG, kollabiert aber nicht.

## Interpretation

Der wichtigste Befund:

```text
Mehr Feldzeit macht offene Milieus nicht automatisch geschlossen.
```

Stattdessen entsteht eine mehrschichtige Lesung:

- Ein Teil des Feldes bleibt offen.
- Ein Teil wird rollennah.
- Ein kleinerer Teil wird pfadnah.
- Ein weiterer Teil koppelt Rolle und Pfad gemeinsam.

Das ist fachlich wertvoll, weil es gegen eine zu einfache Reifungslogik spricht. Reifung bedeutet hier nicht, dass Unsicherheit verschwindet. Reifung bedeutet, dass neben offener Bedeutungsvarianz tragende Milieunähe entsteht.

## Grenze

Dieser Befund bleibt passiv.

Er sagt nicht:

```text
MINI_DIO soll handeln.
MINI_DIO hat eine Strategie.
Offene Milieus sind schlecht.
```

Sauberer ist:

```text
MINI_DIO bildet ueber laengere Feldzeit eine Koexistenz aus offener Varianz und getragener Rekopplungsnaehe.
```

## Detailberichte

- [1684_ADAPTIVE_MILIEU_LANGFENSTER_DOGE.md](1684_ADAPTIVE_MILIEU_LANGFENSTER_DOGE.md)
- [1684_ADAPTIVE_MILIEU_LANGFENSTER_XRP.md](1684_ADAPTIVE_MILIEU_LANGFENSTER_XRP.md)
- [1684_ADAPTIVE_MILIEU_LANGFENSTER_PAXG.md](1684_ADAPTIVE_MILIEU_LANGFENSTER_PAXG.md)
- [1684_ADAPTIVE_MILIEU_LANGFENSTER_STRESS.md](1684_ADAPTIVE_MILIEU_LANGFENSTER_STRESS.md)
