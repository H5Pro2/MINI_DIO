# 1528 - Feldzeit, Stress und Pareidolie-Grenze

## Zweck

Diese Pruefung beantwortet die methodische Kernfrage:

```text
Fuehrt MINI_DIO strukturierte Datenverarbeitung durch,
oder projizieren wir nur komplexe Konzepte in ein rauschendes Modell?
```

Die Antwort kann nicht durch Deutung allein kommen. Sie muss ueber Gegenproben entstehen:

1. strukturierte Mosaikwelt,
2. Nullwelt mit zerstoerter Reihenfolge,
3. Nullwelt mit randomisierter Richtung,
4. reale Stresswelt.

Entscheidend ist die Feldzeit:

```text
Bleibt Nachhall / zeitliche Integration unter Struktur hoeher?
Bricht sie unter Null- oder Stressbedingungen ein?
Steigt Vorsicht/Kippnaehe unter Stress?
```

## Datenbasis

| Code | Welt |
| --- | --- |
| 1525 | `data/synthetic_1525_melody_randrollen_interwoven_mosaic_2400_5m.csv` |
| 1526 | `data/synthetic_1526_null_shuffle_order_2400_5m.csv` |
| 1527 | `data/synthetic_1527_null_random_sign_2400_5m.csv` |
| 1528 | `data/kontrolliert_2024_positive_stress_test1_2000_5m_SOLUSDT.csv` |

Alle Lesevergleiche wurden mit `world_relative` und frischer Memory ausgefuehrt.

## Ergebnis

| Welt | Unique Symbols | Stable | Unrest | Tipping | Nachhall | Feldzeit Trust | Feldzeit Caution |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1525 strukturiert | 97 | 0.8759 | 0.1236 | 0.0004 | 0.4053 | 0.7784 | 0.1124 |
| 1526 Null Shuffle | 224 | 0.8045 | 0.1955 | 0.0000 | 0.1512 | 0.6583 | 0.2073 |
| 1527 Null Random Sign | 221 | 0.8517 | 0.1483 | 0.0000 | 0.2452 | 0.6870 | 0.1796 |
| 1528 reale Stresswelt | 345 | 0.7638 | 0.2312 | 0.0050 | 0.1448 | 0.5958 | 0.2489 |

## Deutung

Der Befund spricht nicht fuer reine Pareidolie.

Wenn es nur menschliche Musterprojektion waere, duerften die Null- und Stresswelten aehnlich tragende Rollen und aehnliche Feldzeitwerte zeigen.

Das passiert nicht.

Stattdessen zeigt sich eine klare Abstufung:

```text
Strukturierte Mosaikwelt:
  hohe Feldzeit, hoher Nachhall, engere Symbolordnung

Nullwelten:
  mehr Symbolstreuung, weniger Nachhall, niedrigere Feldzeit

Stresswelt:
  hoechste Symbolstreuung, niedrigste Feldzeit, mehr Unrest und Kippnaehe
```

Das ist methodisch wichtig:

```text
Die Weltordnung beeinflusst die Feldordnung messbar.
```

## Feldzeit-Lesung

Feldzeit wirkt hier nicht wie eine programmierte Zeitachse, sondern wie Integrationsqualitaet:

- strukturierte Wiederkehr erzeugt hoeheren Nachhall,
- zerstoerte Ordnung senkt Nachhall,
- Stress senkt Feldzeit-Trust und erhoeht Vorsicht,
- Kippnaehe erscheint erst unter echter Stresswelt deutlicher.

Damit wird Feldzeit zu einer Pruefgroesse gegen Pareidolie:

```text
Wenn Bedeutung nur hineingelesen waere,
duerfte Feldzeit nicht so klar zwischen Struktur, Nullwelt und Stress unterscheiden.
```

## Grenze

Das ist noch kein Beweis fuer Lernen im starken Sinn.

Der belastbare Satz ist aktuell:

```text
MINI_DIO zeigt strukturabhaengige Feldantworten.
Diese Feldantworten unterscheiden sich von Null- und Stresswelten.
Feldzeit und Nachhall reagieren messbar auf Weltordnung.
```

Ob das System lernt, muss durch Memory-Folgepruefungen gezeigt werden:

- gleiche Welt ohne Reset,
- verwandte Holdout-Welt mit gleicher Memory,
- Messung von Wiederverwendung statt Neuerfindung,
- Vergleich gegen mehrere Nullwelten.

## Arbeitsantwort Auf Die Kernfrage

Die aktuelle Antwort lautet:

```text
Es ist mehr als reines Rauschen,
aber noch nicht als Lernen im starken Sinn bewiesen.
```

MINI_DIO verarbeitet Weltstruktur offenbar geordnet genug, dass Null- und Stresswelten andere Feldzeit-, Nachhall- und Rollenprofile erzeugen.

Damit wird die Forschungslinie staerker:

```text
Nicht jede komplexe Deutung ist automatisch real.
Aber hier gibt es messbare Unterschiede,
die gegen eine reine Pareidolie-Erklaerung sprechen.
```
