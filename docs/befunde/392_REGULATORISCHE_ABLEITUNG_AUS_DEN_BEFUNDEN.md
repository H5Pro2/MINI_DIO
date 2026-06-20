# Regulatorische Ableitung aus den Befunden

Stand: 2026-06-20

## Zweck

Diese Datei ordnet die bisherigen MINI_DIO-Befunde regulatorisch ein.
Sie beschreibt, welche Regulationsachsen aus den passiven Befunden fachlich begruendet sind und welche Grenzen fuer eine spaetere Umsetzung gelten.

Wichtig:

```text
Das ist keine Runtime-Regel.
Das ist kein Gate.
Das ist keine Handlungsschicht.
Das ist keine Strategie.
```

Regulation wird hier zuerst als Wahrnehmung der Innenfeldqualitaet verstanden.

## Hierarchie

1. Grundfrage: Welche Form von Regulation folgt aus den bisherigen MCM-Feldbefunden?
2. Unterpruefung: Welche Befunde tragen welche Regulationsachsen?
3. Folgeschritt: Welche Achsen duerfen spaeter in Code uebersetzt werden, ohne wieder mechanisch zu werden?

## Ausgangspunkt

Die bisherigen Befunde zeigen nicht einfach einzelne Zeichen mit fester Bedeutung.
Sie zeigen gerichtete Feldbewegungen, deren Tragart wiederkehrt.

Besonders wichtig ist die wiederholt gepruefte Bewegung:

```text
1t5bcxp -> 183drjy
```

Sie wurde ueber SOL/BTC, 2024/2025 und mehrere Zeitaufloesungen dominant `eng_getragen` gelesen.
Der Rueckweg:

```text
183drjy -> 1t5bcxp
```

wurde dominant `fragmentiert` gelesen.

Daraus folgt:

```text
Regulation darf nicht nur auf ein Symbol schauen.
Regulation muss Richtung, Feldlage, Wiederkehr und Tragart lesen.
```

## Was regulatorisch belastbar ist

### 1. Feldlage

MINI_DIO kann passive MCM-Feldlagen unterscheiden:

- rekoppelnde Lage,
- offene Lage,
- Drucklage,
- Bewegungsbruch,
- bruchnahe Lage.

Regulatorische Ableitung:

```text
Die Feldlage beschreibt, wie die Innenwelt eine Weltbewegung aktuell traegt.
```

Moegliche spaetere Achse:

```text
feldlage_lesung
```

Status:

```text
belastbar als Diagnose
noch nicht als Handlung
```

### 2. Tragart

Die Reports unterscheiden passive Qualitaeten:

- `eng_getragen`,
- `breit_driftend`,
- `fragmentiert`,
- `offen_driftend`.

Regulatorische Ableitung:

```text
Tragart beschreibt, ob eine Innenfeldbewegung stabil, offen, driftend oder zerfallend wirkt.
```

Moegliche spaetere Achse:

```text
tragart_wahrnehmung
```

Status:

```text
belastbar als passive Regulationswahrnehmung
```

### 3. Richtung

Die gleiche beteiligte Feldfamilie kann je nach Richtung anders wirken.

Beispiel:

```text
1t5bcxp -> 183drjy = eher getragen
183drjy -> 1t5bcxp = eher fragmentiert
```

Regulatorische Ableitung:

```text
Regulation muss Bewegung lesen, nicht nur Zustand.
```

Moegliche spaetere Achse:

```text
gerichtete_feldbewegung
```

Status:

```text
stark diagnostisch gestuetzt
noch passiv halten
```

### 4. Wiederkehr

Eine Feldbewegung wird relevanter, wenn sie ueber Welten, Jahre oder Zeitaufloesungen wiederkehrt.

Regulatorische Ableitung:

```text
Wiederkehr erzeugt keine Regel, aber eine reifere Innenfeldspur.
```

Moegliche spaetere Achse:

```text
wiederkehr_reife
```

Status:

```text
belastbar fuer Memory- und Reifungsschicht
```

### 5. Fragmentierung

Fragmentierung bedeutet nicht automatisch Fehler.
Sie beschreibt eine breitere, weniger gebundene Innenfeldbewegung.

Regulatorische Ableitung:

```text
Fragmentierung braucht nicht sofort Blockade.
Sie braucht zuerst Abstand, Beobachtung oder leichtere Kopplung.
```

Moegliche spaetere Achsen:

```text
feldabstand
kopplungsleichtigkeit
beobachtungsnaehe
```

Status:

```text
belastbar als Warn- und Distanzierungswahrnehmung
keine harte Sperre
```

### 6. Rekopplung

Rekopplung zeigt, dass das Feld nach Kontakt wieder in eine tragendere Ordnung findet.

Regulatorische Ableitung:

```text
Rekopplung ist kein Zielbefehl, sondern ein Hinweis auf innere Tragfaehigkeit.
```

Moegliche spaetere Achse:

```text
rekopplungsfaehigkeit
```

Status:

```text
belastbar als Kernachse fuer organische Regulation
```

## Was noch nicht belastbar genug ist

### Handlung

Aus keinem der aktuellen Befunde folgt eine Handlung.

Nicht ableiten:

```text
Wenn eng_getragen, dann handeln.
Wenn fragmentiert, dann sperren.
```

Das waere mechanisch und wuerde den aktuellen Forschungsstand verfälschen.

### Feste Schwellwerte

Die bisherigen Prozentwerte und Anteile sind Befundwerte.
Sie duerfen nicht als starre Regeln in den Code uebernommen werden.

Nicht ableiten:

```text
ab X Prozent tragend
unter Y Prozent blockieren
```

### Symbol-Ontologie

`1t5bcxp` und `183drjy` sind keine festen Bedeutungswoerter.
Sie sind Feldfamilien innerhalb einer Bewegung.

Nicht ableiten:

```text
1t5bcxp bedeutet immer X.
183drjy bedeutet immer Y.
```

## Regulatorische Grundachsen

Aus den bisherigen Befunden sind folgende Achsen fachlich sinnvoll:

| Achse | Bedeutung | Status |
|---|---|---|
| Feldlage | Welche Innenfeldlage liegt aktuell vor? | Diagnose belastbar |
| Tragart | Traegt, driftet oder fragmentiert die Bewegung? | Diagnose belastbar |
| Richtung | Wohin bewegt sich die Feldfamilie? | Stark gestuetzt |
| Wiederkehr | Kehrt die Bewegung ueber Welten wieder? | Reifung belastbar |
| Rekopplung | Findet das Feld wieder tragendere Ordnung? | Kernachse |
| Fragmentierung | Wird die Bewegung breit/offen/zerfallend? | Distanzachse |
| Feldabstand | Muss das Feld leichter koppeln? | Umsetzungshypothese |
| Beobachtungsnaehe | Soll die Lage weiter passiv verfolgt werden? | Umsetzungshypothese |

## Regulatorischer Leitsatz

```text
Regulation entsteht nicht durch harte Kontrolle.
Regulation entsteht durch Wahrnehmung der Innenfeldqualitaet,
durch Wiederkehr, Rekopplung, Abstand und tragfaehige Verdichtung.
```

## Konsequenz fuer Code

Eine spaetere regulatorische Schicht sollte nicht entscheiden:

```text
handeln / nicht handeln
```

Sie sollte zuerst protokollieren und verdichten:

```text
Diese Bewegung traegt oft.
Diese Bewegung fragmentiert oft.
Diese Lage rekoppelt.
Diese Lage bleibt offen.
Diese Welt braucht mehr Abstand.
Diese Kopplung wirkt zu eng.
```

Erst danach kann eine organische Regulationsschicht entstehen.

## Minimaler spaeterer Code-Baustein

Wenn diese Ableitung in Code ueberfuehrt wird, sollte der erste Baustein passiv bleiben:

```text
RegulationsMemory
  liest Feldbewegung
  liest Tragart
  liest Wiederkehr
  liest Rekopplung
  speichert keine Handlung
  gibt nur Innenfeldqualitaet zurueck
```

Keine Motorik, keine Entry-Logik, keine Strategy.

## Aktueller Stand

Wir sind analytisch weit genug, um eine passive Regulationswahrnehmung zu bauen.
Wir sind noch nicht so weit, daraus Handlung abzuleiten.

Der naechste saubere Schritt ist daher:

```text
passive Regulations-Memory-Schicht
```

nicht:

```text
aktive Entscheidungs-Regulation
```

## Wie es weitergeht

Als naechstes sollte eine technische Skizze fuer `RegulationsMemory` entstehen:

1. Eingaben,
2. gespeicherte Qualitaeten,
3. Reifungslogik ohne Schwellen-Gates,
4. Ausgabe als passive Innenfeldqualitaet,
5. klare Grenze gegen Handlung.
