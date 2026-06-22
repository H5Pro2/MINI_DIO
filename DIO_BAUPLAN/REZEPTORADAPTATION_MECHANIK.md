# Rezeptoradaptation - Mechanik

## Zweck

Diese Datei beschreibt die aktuelle mechanische Leitgrenze fuer MINI_DIO:

```text
Nicht die Aussenwelt beruehrt direkt das MCM-Feld.
Nur rezeptorisch aufgenommene und adaptierte Wirkung wird als MCM-Feldwirkung gelesen.
```

Damit bleibt das Feld ein Innenfeld und wird nicht zu einem Sammelbecken fuer Rohdaten.

## Grundkette

```text
Aussenwelt
  -> Sinnesaufnahme
  -> Rezeptorkontakt
  -> adaptierte Feldaufnahme
  -> MCM-Feldwirkung
  -> Nachhall / Bedeutung / Topologie
```

Diese Kette ist keine Handlungskette. Sie beschreibt Wahrnehmungsaufnahme.

## Ebenen

### 1. Aussenwelt

Die Aussenwelt liefert Veraenderung, Rhythmus, Energie, Richtung, Bruch und Wiederkehr.

Sie darf nicht direkt als MCM-Feldzustand behandelt werden.

### 2. Sinnesaufnahme

Sinnesaufnahme ist kanalgetrennt:

- Sehen liest Formauffaelligkeit, Stabilitaet, Wechsel und Schaerfe.
- Hoeren liest Ton, Lautheit, Frequenzwirkung und Energieverschiebung.
- Direkter Kontakt ist ein eigener Spuerkanal und bleibt getrennt von Sehen und Hoeren.

Wichtig:

```text
Sehen + Hoeren ist nicht automatisch Fuehlen.
```

### 3. Rezeptorkontakt

Rezeptoren uebersetzen Sinnesaufnahme in Kontaktqualitaet.

Dabei entsteht noch nicht automatisch ein fertiger MCM-Zustand. Es entsteht eine Frage an das Feld:

```text
Wie stark, wie nah, wie geordnet und wie tragfaehig darf diese Aufnahme das Feld beruehren?
```

### 4. Adaptierte Feldaufnahme

Die adaptierte Feldaufnahme ist die aktuelle Aufnahmegrenze.

Sie entsteht aus:

- Rohfeldaufnahme,
- Rezeptorlast,
- sensorischer Lautheit,
- visueller Schaerfe / Unschaerfe,
- Adaptionspotential,
- Daempfung.

Leitformel als Fachbild:

```text
Rohfeldaufnahme > adaptierte Feldaufnahme
```

Wenn diese Differenz sichtbar ist, wirkt die Rezeptorschicht als Schutz- und Uebersetzungsschicht.

### 5. MCM-Feldwirkung

Erst die adaptierte Feldaufnahme wird als MCM-Feldwirkung gelesen.

MCM-Feldwirkung bedeutet aktuell:

- Kohärenznahe oder spannungsnahe Feldlage,
- Tragwirkung,
- Belastung,
- Rekopplung,
- Randnaehe,
- offene Variante,
- Zentrumnaehe,
- Nachhall.

Das Feld verarbeitet nicht alle Einzelwerte. Es reagiert auf die verdichtete Kontaktwirkung.

### 6. Nachhall

Nachhall ist keine neue Rohinformation.

Nachhall ist Restwirkung im Innenfeld:

```text
Eine vergangene Feldwirkung bleibt kurz oder laenger als innere Spur erhalten.
```

Nachhall darf spaetere Wahrnehmung faerben, aber er darf nicht als aktuelle Aussenwelt verwechselt werden.

## Was in das MCM-Feld darf

In das MCM-Feld darf:

- adaptierte Feldaufnahme,
- MCM-Kohärenzwirkung,
- MCM-Spannungswirkung,
- MCM-Asymmetrie,
- tragende oder belastende Kontaktwirkung,
- Nachhall als innere Restspur,
- gereifte Bedeutungswirkung aus wiederkehrender Feldreaktion.

## Was vor dem Feld bleiben muss

Vor dem MCM-Feld bleiben:

- Rohdaten,
- rohe Kerzen-/Weltwerte,
- reine Lautheit ohne Rezeptoruebersetzung,
- reine visuelle Formwerte ohne Kontaktwirkung,
- Debugwerte,
- Auswertungsrollen,
- Topologiebegriffe,
- harte Schwellen als Runtime-Wahrheit.

Topologiebegriffe wie Zentrum, Rand, Bruecke oder offene Variante sind Diagnosebegriffe. Sie beschreiben gelesene Feldrollen, aber sie sind keine Vorgabe an das Feld.

## Was als Nachhall getragen werden darf

Als Nachhall darf getragen werden:

- Restspannung,
- Restentlastung,
- wiederkehrende Feldnaehe,
- verblassende Bedeutungsinsel,
- Driftspur,
- Rekopplungsspur.

Nicht als Nachhall tragen:

- neue Rohdaten,
- ungepruefte Aussenweltannahmen,
- Handlungshypothesen,
- starre Strategieannahmen.

## Organische Bedeutung

Die Rezeptorschicht ist kein starrer Limiter.

Sie ist eine organische Aufnahmefaehigkeit:

```text
MINI_DIO nimmt Welt nicht vollstaendig auf.
MINI_DIO nimmt Welt so auf, wie sie rezeptorisch tragbar in Feldwirkung uebersetzt werden kann.
```

Damit kann dieselbe Welt je nach Lautheit, Schaerfe, Rohfeldaufnahme und Adaptation anders wirken.

## Aktueller Forschungsstand

Die bisherigen Befunde zeigen:

- synthetische Harmonie bleibt fast rein zentrumsnah,
- synthetische Bruch-/Randwelt oeffnet lokal,
- synthetische Randdominanz erzeugt lokale Randnaehe, aber keinen globalen Kollaps,
- echte PAXG/DOGE/XRP-Welten zeigen dieselbe Hochlastlogik,
- nachgezogene BTC/SOL/KAS-Welten zeigen dieselbe Adaptionsrichtung,
- die Adaptionsratio bleibt in mehreren echten 5m-Welten eng um etwa `0.85`.

Das ist kein allgemeiner Beweis. Es ist eine belastbare aktuelle Arbeitsmechanik.

## Entwicklungsregel

Wenn neue Wahrnehmungsdaten in MINI_DIO eingefuehrt werden, muessen sie zuerst dieser Frage standhalten:

```text
Ist das Sinnesaufnahme, Rezeptorkontakt, adaptierte Feldaufnahme, MCM-Feldwirkung oder Nachhall?
```

Erst danach darf entschieden werden, ob und wie diese Information gespeichert, verglichen oder beschrieben wird.

Wie es weitergeht: Als naechstes sollte diese Mechanik gegen den Code geprueft werden: Welche Spalten und Funktionen gehoeren zu Sinnesaufnahme, Rezeptorkontakt, adaptierter Feldaufnahme, MCM-Feldwirkung und Nachhall?
