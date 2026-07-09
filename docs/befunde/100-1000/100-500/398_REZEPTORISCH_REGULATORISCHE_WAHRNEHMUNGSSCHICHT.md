# Rezeptorisch-regulatorische Wahrnehmungsschicht

Stand: 2026-06-20

## Zweck

Diese Datei trennt die Wahrnehmungsmechanik sauber von der MCM-Feldbewegungs-Memory.

Die rezeptorisch-regulatorische Wahrnehmungsschicht beschreibt, wie Informationen aus unterschiedlichen Welt- und Assetklassen im MCM-Feld ankommen duerfen.

Sie ist keine Memory-Schicht.
Sie ist keine Handlungsschicht.
Sie ist kein Gate.

## Hierarchie

1. Grundfrage: Wie verhindert MINI_DIO, dass unterschiedliche Welten das MCM-Feld uebersteuern oder falsch belasten?
2. Unterpruefung: Welche Wahrnehmungsachsen beschreiben Aufnahmequalitaet organisch?
3. Folgeschritt: Erst danach darf die Feldwirkung in `MCMFieldMovementMemory` als gewachsene Spur gespeichert werden.

## Position im System

```text
Aussenwelt / Asset
-> Sehen
-> Hoeren
-> Rezeptorkontakt
-> rezeptorisch-regulatorische Wahrnehmungsschicht
-> MCM-Feldwirkung
-> MCM-Feldbewegung
-> MCMFieldMovementMemory
```

Die Schicht sitzt vor der Feldwirkung.
Sie beschreibt die Aufnahmequalitaet.
Sie speichert keine gereifte Bedeutung.

## Fachliche Korrektur der Sinneswege

Die Sinnesachsen wirken nicht gleich.

```text
Sehen  = Form erkennen, Distanzwahrnehmung, spaetere Memory-Kopplung
Hoeren = Frequenz, Ton, Rhythmus, direkte Feldstimulation moeglich
Fuehlen / Spueren = direkter Kontakt zur Welt
```

Daraus folgt:

```text
Eine sichtbare Form ist kein direkter Kontakt.
Eine gehoerte Frequenz kann das Feld stimulieren.
Direkter Druck entsteht erst ueber Kontakt.
```

Beispiel:

```text
Ich sehe etwas Spitzes.
Das Sehen selbst tut nicht weh.
Erst Erfahrung/Memory koppelt daran: Das kann weh tun.
```

Im aktuellen Kurswelt-Setup gibt es noch keinen echten taktilen Direktkontakt.
Darum bleibt `direct_contact_pressure` dort bei `0.0`.

Kompatibilitaet:

```text
visual_contact = alter Reportname
visual_form_salience = fachlich sauberer Name
auditory_contact = alter Reportname
auditory_stimulation = fachlich sauberer Name
contact_pressure = alter Reportname
field_intake_pressure = fachlich sauberer Name
```

## Vier Achsen

### Fokus / Abstand

Beschreibt, wie nah eine Information an das Feld herangelassen wird.

```text
Fokus = naeher lesen, genauer aufnehmen
Abstand = lockerer halten, nicht voll koppeln
```

Fachliche Funktion:

```text
Schutz vor Ueberkopplung und Asset-Uebertragung.
```

### lauter / leiser

Beschreibt die auditive oder energetische Reizstaerke.

```text
lauter = staerkere Marktmelodie / staerkerer Energiekontakt
leiser = gedaempfter Hintergrund / weniger unmittelbare Reizbindung
```

Fachliche Funktion:

```text
Weltspannung wird nicht roh ins Feld gedrueckt, sondern in ihrer Wahrnehmungslautstaerke eingeordnet.
```

### scharf / unscharf

Beschreibt die visuelle/Form-Klarheit.

```text
scharf = Form ist klarer konturiert
unscharf = Form bleibt diffus, breiter oder noch nicht gebunden
```

Fachliche Funktion:

```text
Form wird als Wahrnehmungsqualitaet gelesen, nicht automatisch als Feldbedeutung.
```

### Druck / Entspannung

Beschreibt, wie stark der aufgenommene Kontakt oder die Stimulation das MCM-Feld belastet oder entlastet.

```text
Druck = Kontakt belastet oder spannt das Feld
Entspannung = Kontakt entlastet oder rekoppelt leichter
```

Fachliche Funktion:

```text
Die Feldwirkung entsteht erst ueber Sinnesaufnahme, Rezeptorwirkung und gegebenenfalls Erinnerungskopplung, nicht als ungefilterte Rohwelt.
```

## Warum diese Schicht noetig ist

Unterschiedliche Assets und Weltklassen tragen verschiedene Rohspannungen:

- SOL 5m kann harmonischer wirken,
- BTC 1h kann schwerer und lauter wirken,
- KAS kann durch Preisstruktur und Skala anders ankommen.

Wenn diese Rohunterschiede direkt ins MCM-Feld gelangen, wird das Feld ueberlagert.

Die rezeptorisch-regulatorische Wahrnehmungsschicht soll deshalb nicht entscheiden, sondern die Aufnahme organisch lesbar machen:

```text
Wie nah?
Wie laut?
Wie klar?
Wie druckvoll?
```

Wichtig:

```text
Diese Achsen sind Eigenschaften des Organismus.
```

Sie sind keine externen Regeln und kein Steuerblock, der dem Feld sagt, was es
zu tun hat. Sie beschreiben Faehigkeiten, mit denen MINI_DIO lernt, mit
Weltaufnahme umzugehen:

- Fokus bilden oder Abstand halten,
- laute Reize tragen oder leiser aufnehmen,
- klare Formen schaerfer lesen oder Unschaerfe zulassen,
- Druck wahrnehmen oder Entspannung herstellen.

Damit entsteht Anpassung als Organismus-Eigenschaft, nicht als harte Mechanik.

## Sinnesgetrennte Anpassung

Die Anpassung darf nicht global gelesen werden.

MINI_DIO kann in einer Weltlage theoretisch:

- gedämpfter hören, aber genauer sehen,
- stärker fühlen, aber Abstand zur Form halten,
- Ton stärker zulassen, aber direkten Feldkontakt vorsichtiger tragen,
- eine Form nur sehen, ohne daraus sofort starke Feldwirkung zu machen.

Diese Möglichkeiten sind Fähigkeiten des Organismus.
Sie sind noch keine gelernte Entscheidung.

Die direkte Rückmeldung kommt aus dem MCM-Feld:

```text
trägt die Aufnahme?
kippt sie?
rekoppelt sie?
überlagert sie?
bildet sie Nachhall?
```

Daraus kann MINI_DIO episodisch lernen, wie viel Sinneswirkung es in ähnlichen Lagen zulässt.

## Grenze zu MCMFieldMovementMemory

Diese Schicht beschreibt:

```text
Wie kommt Information im Feld an?
```

`MCMFieldMovementMemory` beschreibt:

```text
Welche Feldbewegung wurde ueber Wiederkehr als Spur verdichtet?
```

Keine Vermischung:

```text
Wahrnehmungsachsen sind Aufnahmequalitaet.
Feldbewegungs-Memory ist gewachsene Innenfeldgeschichte.
```

## Aktueller technischer Stand

Die Rezeptorschicht ist nicht nur dokumentiert, sondern im Kernpfad angebunden:

```text
MCM-Neuronen
DIO-Syntax
Episodendistanz
Beobachtungsdruck
neurochemische Spiegelung
```

Diese Bereiche lesen jetzt bevorzugt:

```text
rezeptorische Aufnahme + MCM-Feldwirkung
```

Rohes Sehen und rohes Hoeren bleiben als Welt- und Debugbeschreibung sichtbar.
Sie sind aber nicht mehr der primaere innere Lernvektor.

Technisch wird diese Eigenschaftsschicht als `perception_regulation_state`
ausgegeben und zusaetzlich als `organism_adaptation_state` gespiegelt. Beide
beschreiben dieselbe passive Organismus-Faehigkeit.

Wichtig:

```text
field_intake_pressure geht als Rezeptorwirkung in das MCM-Feld.
adaptation_potential beschreibt nur moegliche Anpassung.
```

`regulation_damping` bleibt aus Kompatibilitaetsgruenden sichtbar, darf aber
nicht als versteckte globale Daempfung des MCM-Feldes verstanden werden.

## Umsetzungshinweis

Die vier Achsen sollten als eigene passive Diagnoseschicht weiter sichtbar werden.

Sie duerfen nicht direkt:

- handeln,
- sperren,
- Entries erzeugen,
- Memory-Reife ersetzen,
- Tragart als Regel festlegen.

Sie duerfen:

- Welt-/Assetaufnahme vergleichbarer machen,
- Ueberkopplung sichtbar machen,
- Sinnesaufnahme organischer kalibrieren,
- erklaeren, warum eine Welt harmonisch oder belastend ankommt.

## Wie es weitergeht

Als naechstes sollte geprueft werden, welche vorhandenen Reports bereits Messwerte fuer diese vier Achsen liefern und welche davon in eine eigene passive Datei `perception_regulation_state` ueberfuehrt werden koennen.
