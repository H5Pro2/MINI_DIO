# Negative Bewegung Und MCM-Tragfaehigkeit

Stand: 2026-06-18

## Zweck

Nach Expansion und Seitwaertsdruck wurde negative Bewegung geprueft.

Verwendete Welten:

```text
data\kontrolliert_2023_moderate_negative_test1_1000_5m_SOLUSDT.csv
data\kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv
```

Die Grundfrage war:

```text
Liest MINI_DIO negative Bewegung automatisch als belastend,
oder entscheidet die MCM-Feldwirkung ueber Tragfaehigkeit?
```

## Ergebnis

Negative Bewegung ist nicht automatisch Stress.

Beide geprueften negativen Welten bleiben in getragenen Feldbereichen:

```text
negative_moderate -> ruhige Naehegruppe
negative_stress   -> mittlere Feldlage
```

Damit trennt MINI_DIO:

```text
Richtung der Welt
von
Innenfeldbelastung
```

## Messwerte

| Welt | Feldklasse | Rekopplung | Tragqualitaet | Strain/Kippung | Memory | Dominante Wirkung |
|---|---|---:|---:|---:|---:|---|
| negative_moderate | ruhige Naehegruppe | 0.631065 | 0.362044 | 65 | 45 | stabil |
| negative_stress | mittlere Feldlage | 0.630398 | 0.356899 | 66 | 59 | stabil |

Reproduktion:

```text
negative_moderate Top-Syntax-Ueberlappung: 1.0
negative_moderate Top-Familien-Ueberlappung: 1.0

negative_stress Top-Syntax-Ueberlappung: 1.0
negative_stress Top-Familien-Ueberlappung: 1.0
```

## Interpretation

Die negative Richtung allein erzeugt keinen MCM-Gegenpol.

Die Feldwirkung bleibt getragen, wenn:

```text
Rekopplung ausreichend hoch bleibt,
Tragqualitaet nicht kollabiert,
Strain/Kippung begrenzt bleibt,
und die Sinnes-MCM-Kopplung nicht stark abfaellt.
```

Das bedeutet:

```text
MINI_DIO liest nicht "rot/abwaerts = schlecht".
MINI_DIO liest "wie wirkt diese Bewegung im Innenfeld?"
```

Das ist fachlich wichtig, weil es gegen eine triviale Labelmaschine spricht.

## Vergleich Zu Sideways

Die zweite Seitwaertswelt `sideways_2026` war belasteter als beide negativen Welten:

```text
sideways_2026:
Rekopplung: 0.615214
Tragqualitaet: 0.351964
Strain/Kippung: 192
Memory: 117
Feldklasse: Stress-Gegenpol
```

Damit ist nicht die sichtbare Richtung entscheidend.

Entscheidend ist:

```text
Wie stark die Welt das MCM-Feld aus tragender Kopplung herauszieht.
```

## Feldzeit

Beide negativen Welten bleiben ueberwiegend in:

```text
temporal_first_contact
```

negative_moderate:

```text
temporal_first_contact: 927
temporal_far_return: 67
```

negative_stress:

```text
temporal_first_contact: 925
temporal_far_return: 66
```

Das zeigt:

```text
Die negative Bewegung erzeugt in diesen Fenstern keine tiefe neue Feldzeit,
aber sie bleibt stabil genug lesbar.
```

## Forschungswert

Der Befund erweitert die bisherige MCM-Feldordnung:

```text
Positive Expansion kann ruhig oder belastet sein.
Seitwaerts kann ruhig oder stark belastet sein.
Negative Bewegung kann getragen bleiben.
```

Die MCM-Feldwirkung haengt also nicht einfach am Oberflaechenlabel der Welt.

Sie entsteht aus:

```text
Weltspannung,
Sinneskopplung,
Rekopplung,
Tragqualitaet,
Kippnaehe,
Memorydruck,
und Feldzeit.
```

## Wie Es Weitergeht

Als naechstes sollte eine bewusst laengere negative Welt oder ein anderes Jahr geprueft werden.

Hierarchie:

1. Grundfrage: Bleibt negative Bewegung auch ueber laengere Sequenzen getragen?
2. Unterpruefung: Entsteht bei 10k Zeilen mehr Feldzeit, Drift oder Memorydruck?
3. Folgeschritt: Wenn negative Welten stabil getragen bleiben, wird die MCM-Topologie nicht nach Richtung, sondern nach Feldbelastbarkeit beschrieben.
