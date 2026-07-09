# Expansionsachse Als MCM-Feldbefund

Stand: 2026-06-18

## Zweck

Diese Datei fasst die bisherigen Expansionsprüfungen zusammen.

Geprüft wurden vier verschiedene Weltlagen:

```text
Positive Expansion
Extreme Expansion
Recovery Expansion
Late Positive
```

Ziel war nicht, eine Handelslogik zu finden.

Ziel war:

```text
Wie liest MINI_DIO unterschiedliche Formen von Expansion im MCM-Innenfeld?
```

## Kernergebnis

MINI_DIO liest Expansion nicht als starre Kategorie.

Die geprüften Welten bilden eine erkennbare Achse:

```text
ruhig_feldzeitnah
  -> last_feldzeitnah
  -> ruhig_feldzeitnah mit Restspannung
  -> last_feldzeitnah als Übergangsform
```

Das bedeutet:

```text
Expansion ist nicht automatisch Last.
Expansion ist nicht automatisch Ruhe.
Expansion wird über Tragfähigkeit, Rekopplung, Feldzeit und Innenlast gelesen.
```

## Werteübersicht

| Welt | Lesung | Rekopplung | Tragqualität | Strain/Kippung | Memory | Dominante Wirkung |
|---|---|---:|---:|---:|---:|---|
| Positive Expansion | ruhig_feldzeitnah | 0.633577 | 0.357946 | 40 | 40 | stabil |
| Extreme Expansion | lastnah / last_feldzeitnah | 0.623022 | 0.353039 | 129 | 86 | stabil, aber deutlich belasteter |
| Recovery Expansion | ruhig_feldzeitnah | 0.630474 | 0.359369 | 62 | 56 | stabil |
| Late Positive | last_feldzeitnah | 0.626417 | 0.357191 | 78 | 56 | tragend_unruhig |

## Stufe 1: Positive Expansion

Positive Expansion wurde als:

```text
ruhig_feldzeitnah
```

gelesen.

Das Feld bleibt überwiegend getragen:

```text
field_carried: 972
field_strained: 22
```

Die Wirkung ist stark stabil:

```text
stabil: 565
tragend_unruhig: 384
```

MCM-Lesung:

```text
Bewegung ist vorhanden,
aber sie überlastet das Feld nicht.
Die Expansion trägt Feldzeit, bleibt aber ruhig genug rekoppelt.
```

## Stufe 2: Extreme Expansion

Extreme Expansion kippt in:

```text
lastnah / last_feldzeitnah
```

Das Feld bleibt zwar reproduzierbar und größtenteils getragen:

```text
field_carried: 934
field_strained: 60
```

aber Strain/Kippung und Memorylast steigen deutlich:

```text
Strain/Kippung: 129
Memory: 86
```

MCM-Lesung:

```text
Die Bewegung bleibt als Ordnung lesbar,
aber ihre Feldzeit wird belastet.
```

## Stufe 3: Recovery Expansion

Recovery Expansion wird wieder:

```text
ruhig_feldzeitnah
```

gelesen.

Sie ist nicht ganz so glatt wie positive Expansion, aber deutlich ruhiger als extreme Expansion:

```text
Rekopplung: 0.630474
Strain/Kippung: 62
Memory: 56
```

MCM-Lesung:

```text
Das Feld kann nach stärkerer Bewegung wieder in tragendere Kopplung zurückfinden.
```

Das ist wichtig, weil hier nicht nur Belastung sichtbar wird, sondern auch Rückführung.

## Stufe 4: Late Positive

Late Positive wird als:

```text
last_feldzeitnah
```

und im Feldklassen-Report als:

```text
angespannte Übergangsgruppe
```

gelesen.

Die dominante Wirkung ist nicht mehr `stabil`, sondern:

```text
tragend_unruhig
```

MCM-Lesung:

```text
Das Feld kollabiert nicht,
aber es trägt die Bewegung unruhiger.
```

Das wirkt wie eine echte Übergangsform zwischen ruhiger Expansion und belasteter Feldzeit.

## Forschungsbefund

Die Expansionsachse zeigt eine organische Feldbewegung:

```text
getragene Bewegung
-> überlastete Bewegung
-> rekoppelnde Erholung
-> unruhig getragener Übergang
```

Das ist für die MCM-Forschung wichtig, weil daraus folgt:

```text
Die MCM-Feldwirkung liest nicht nur Bewegung.
Sie liest die Belastbarkeit der Bewegung.
```

Ein äußerlich positives oder expansives Weltmuster ist nicht automatisch ruhig.
Ein starkes Weltmuster ist nicht automatisch schlecht.
Entscheidend ist, wie das Innenfeld rekoppelt.

## Bedeutung Für MINI_DIO

MINI_DIO zeigt hier keine einfache Reizklassifikation.

Es entsteht eine differenzierte Innenfeldlesung:

- stabile getragene Bewegung,
- belastete Feldzeit,
- Rückführung in tragendere Kopplung,
- unruhig getragene Übergangsbewegung.

Diese Differenzierung entsteht in passiver Beobachtung.

Keine der Lesungen ist ein Gate, eine Runtime-Regel oder eine Handlungsvorgabe.

## Bedeutung Für Die MCM

Die Expansionsachse stützt die bisherige Arbeitshypothese:

```text
Das MCM-Feld bildet aus Weltkontakt eine eigene Innenordnung.
```

Diese Innenordnung ist nicht nur:

```text
ruhig / stressig
```

sondern feiner:

```text
ruhig
ruhig_feldzeitnah
last_feldzeitnah
tragend_unruhig
rekoppelnd
Übergang
```

Damit wird Feldzeit nicht als einzelner Messwert verstanden, sondern als Tiefe der Feldwirkung.

## Grenze

Alle vier Befunde beruhen auf 1000-Zeilen-Fenstern.

Sie sind starke Arbeitsbefunde, aber noch keine vollständige Aussage über alle möglichen Expansionswelten.

Die volle 10k-Prüfung steht für spätere Läufe offen.

## Wie Es Weitergeht

Als nächstes sind zwei Wege sinnvoll:

1. Weitere Expansionsfenster prüfen, um die Achse zu stabilisieren.
2. Eine andere Bewegungsfamilie prüfen, zum Beispiel Seitwärtsdruck oder Abverkauf-Erholung.

Die wichtigste Folgefrage lautet:

```text
Bildet MINI_DIO auch bei anderen Bewegungsfamilien solche organischen Achsen,
oder ist die Expansionsachse ein Sonderfall?
```

