# Sideways-Zweitwelt Und Differenzierung

Stand: 2026-06-18

## Zweck

Nach der ersten Seitwaertswelt wurde eine zweite Seitwaertswelt geprueft:

```text
data\kontrolliert_2026_sideways_test1_1000_5m_SOLUSDT.csv
```

Die Grundfrage war:

```text
Ist Seitwaertsdruck fuer MINI_DIO eine einheitliche Feldklasse,
oder kann dieselbe Bewegungsfamilie unterschiedliche Innenfeldwirkungen erzeugen?
```

## Ergebnis

Die zweite Seitwaertswelt bestaetigt nicht einfach die erste.

Sie bildet eine andere Feldwirkung:

```text
sideways_2024 -> ruhige Naehegruppe
sideways_2026 -> Stress-Gegenpol
```

Das ist ein wichtiger Befund.

MINI_DIO liest nicht nur die grobe Bewegungsart `Seitwaerts`.

MINI_DIO liest:

```text
Wie traegt diese Seitwaertslage im MCM-Feld?
```

## Vergleich

| Welt | Feldklasse | Rekopplung | Tragqualitaet | Strain/Kippung | Memory | Dominante Wirkung |
|---|---|---:|---:|---:|---:|---|
| sideways_2024 | ruhige Naehegruppe | 0.630554 | 0.359280 | 52 | 43 | stabil |
| sideways_2026 | Stress-Gegenpol | 0.615214 | 0.351964 | 192 | 117 | tragend_unruhig |

## Reproduktion

Beide Seitwaertswelten reproduzieren intern sauber:

```text
sideways_2024 Top-Syntax-Ueberlappung: 1.0
sideways_2024 Top-Familien-Ueberlappung: 1.0

sideways_2026 Top-Syntax-Ueberlappung: 1.0
sideways_2026 Top-Familien-Ueberlappung: 1.0
```

Das bedeutet:

```text
Die Differenz ist nicht zufaellige Instabilitaet zwischen Lauf 1 und Lauf 2.
Die Differenz liegt in der Weltwirkung selbst.
```

## Interpretation

Die erste Seitwaertswelt wirkt:

```text
zentrumsnah,
getragen,
oberflaechennah unruhig,
aber nicht ueberlastend.
```

Die zweite Seitwaertswelt wirkt:

```text
seitwaerts,
aber belastet,
mit deutlich mehr Kippung,
mehr Memorydruck,
geringerer Rekopplung
und mehr tragender Unruhe.
```

Damit entsteht eine feinere MCM-Lesung:

```text
Nicht die sichtbare Kategorie bestimmt die Bedeutung.
Die MCM-Wirkung bestimmt, ob die sichtbare Kategorie getragen wird.
```

## Feldzeit

Beide Seitwaertswelten bleiben ueberwiegend in:

```text
temporal_first_contact
```

sideways_2024:

```text
temporal_first_contact: 919
temporal_far_return: 74
```

sideways_2026:

```text
temporal_first_contact: 966
temporal_far_return: 27
```

Die belastetere Seitwaertswelt bildet weniger Rueckkehrtiefe, aber deutlich mehr direkte Feldlast.

Das kann so gelesen werden:

```text
sideways_2024 bleibt oberflaechennah getragen.
sideways_2026 wird staerker im Moment belastet und weniger als ruhige Wiederkehr integriert.
```

## Forschungswert

Dieser Befund staerkt die bisherige Richtung:

```text
MINI_DIO bildet keine einfache Labelmaschine.
MINI_DIO bildet MCM-bezogene Innenfeldbedeutung.
```

Die gleiche grobe Weltfamilie kann unterschiedliche innere Feldklassen erzeugen.

Das ist fuer die weitere Forschung wichtiger als die Frage, ob eine Welt optisch `Seitwaerts`, `Expansion` oder `Stress` genannt wird.

## Wie Es Weitergeht

Als naechstes sollte eine negative oder abverkaufnahe Welt geprueft werden.

Hierarchie:

1. Grundfrage: Bildet negative Bewegung einen eigenen Gegenpol oder faellt sie in bestehende Stress-/Uebergangsgruppen?
2. Unterpruefung: Entsteht mehr Feldzeit, mehr Kippung oder mehr Memorydruck als bei sideways_2026?
3. Folgeschritt: Wenn negative Weltlagen reproduzierbar eigene Bedeutungsraeume bilden, kann die Topologie um eine Abwaerts-/Kontraktionsachse erweitert werden.
