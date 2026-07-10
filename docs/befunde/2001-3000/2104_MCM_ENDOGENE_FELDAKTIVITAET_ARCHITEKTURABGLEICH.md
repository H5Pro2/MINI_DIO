# 2104 - Architekturabgleich endogener MCM-Feldaktivitaet

## Zweck

Nach der Saettigung des Pareto-Selbstabweichungszweigs stellt sich eine
grundlegendere Frage: Besitzt MINI_DIO bereits einen inneren Prozess, der nach
beendetem Weltkontakt aus dem eigenen Feldzustand weiterlaeuft?

2104 fuehrt keinen neuen Feldtest aus. Der Befund gleicht die vorhandenen
Runtime-, Nachhall-, Sleep-, Reorganisations- und Konsolidierungspfade mit den
frueheren Befunden 1531 bis 1568 ab. Dabei werden vier Eigenschaften getrennt:

1. Abhaengigkeit vom eigenen vorherigen Feldzustand,
2. Bildung von Inhalten aus eigener Memory,
3. eigener Ausloeser und eigene zeitliche Fortsetzung,
4. kausale Rueckwirkung auf einen spaeteren Feldlauf.

Diese Trennung verhindert, dass ein extern gestarteter Offline-Test bereits
als autonome endogene Aktivitaet bezeichnet wird.

## Normaler Weltlauf

Der normale Lauf erzeugt in `run_once` fuer jede Welt ein neues
`MiniMCMField`. Das Feld arbeitet nur innerhalb der Schleife ueber vorhandene
Welt-Ticks. Nach Ende der Daten existiert kein weiterer Feldschritt.

Der `MiniTemporalTracker` traegt innerhalb dieses Laufs:

- Familienwiederkehr,
- zeitlichen Abstand,
- Formabstand,
- Nachhall,
- passive Trust- und Caution-Unterstuetzung.

Er wird jedoch ebenfalls bei jedem Lauf neu erzeugt. Die Semantic Memory
speichert nur zusammengefasste Familienwerte. Diese gespeicherten Werte werden
nicht zur Initialisierung des naechsten `MiniTemporalTracker` zurueckgelesen.

Damit ist der normale Nachhall kontaktgebundene Innenzeit innerhalb eines
laufenden Weltkontakts. Er setzt sich nach dessen Ende nicht selbst fort.

## Gleiches Feld Mit Leerem Input

Der Offline-Test aus 1531 behaelt dasselbe `MiniMCMField` nach der
Kontaktphase und ruft es fuer weitere Schritte mit leeren, gedaempften oder
zyklisch vorgegebenen Sinneswerten auf. Dabei wirken Aktivierung, neuronaler
Nachhall und Nachbarsignal weiter. Der Befund des stabilen Ausklingens bleibt
gueltig.

Die Fortsetzung besitzt jedoch keinen eigenen Ausloeser:

- das Tool startet die Offlinephase,
- das Tool setzt ihre Tickzahl,
- das Tool waehlt `empty`, `damped` oder `cyclic`,
- das Tool setzt Zerfall, Intensitaet, Zyklus und Restreiz,
- ohne weitere Aufrufe von `field.step` geschieht nichts.

Das ist echte Zustandskontinuitaet unter extern bereitgestellter Zeit, aber
keine autonom erzeugte Feldzeit.

## Sleep-Feldmilieu Aus Eigener Memory

Das Sleep-Feldmilieu aus 1535 liest gespeicherte MCM-Episodenrollen. Deren
Carry, Strain, Rekopplung, Sinneskopplung und Feldabstaende bestimmen den
Resonanzraum. Die aktuelle Sleep-Signatur wirkt auf die naechste Rollennahe
zurueck. Damit besitzt die Sequenz zwei innere Anteile:

- ihr Inhalt stammt aus eigener Episodenerfahrung,
- ihr jeweils naechster Resonanzzustand haengt vom vorherigen Sleep-Feld ab.

Die Umgebung bleibt dennoch von aussen gerahmt:

- sie erzeugt ein neues `MiniMCMField` statt das Realfeld fortzusetzen,
- Tickzahl, Intensitaet und Rollenlimit werden als Parameter gesetzt,
- die maximale Zahl aktiver Rollen und die Aktivierungsgrenze sind vorgegeben,
- die deterministische Rollenatmung wird aus Tick und Symbol berechnet,
- Start und Ende werden vom Tool bestimmt.

Getragen ist deshalb memory-getragene rekursive Offline-Resonanz. Nicht
getragen ist ein vom Organismus selbst begonnener, dauerbestimmter oder
beendeter Sleep-Prozess.

## Sleep-Memory Und Folgewelt

Die optionale Sleep-Reorganisation aus 1542 markiert beruehrte Rollen und
gemeinsame Kombinationen in der JSON-Memory. Ihre Grenzen stehen direkt im
Code:

```text
passive_only = 1
read_by_mini_dio = 0
influences_action = 0
writes_runtime_memory = 0
```

Der Real-Sleep-Real-Runner kopiert die Memory zwischen drei getrennten
Phasen. Real A, Sleep und Real B besitzen jeweils neu erzeugte MCM-Felder. Die
Sleep-Memory kann vor Real B in der JSON-Datei vorhanden sein, wird vom
normalen `run_mini` aber nicht konsumiert.

Die spaetere Rollenreaktivierung aus 1542 bis 1568 ist eine passive
Nachher-Lesung: Das Tool vergleicht, ob im Sleep beruehrte alte Rollen in der
Folgewelt erneut gezaehlt wurden. Es prueft keine kausale Veraenderung von Real
B durch die Sleep-Spur.

Auch die Zwischenrollen-Memory bleibt ein separates diagnostisches Dokument
mit `read_by_mini_dio = 0` und `writes_runtime_memory = 0`.

## Offline-Konsolidierung

Die passive Nachbarschaftskonsolidierung aus 2082 und 2083 bewahrt
Pareto-Reifungshistorien verlustfrei. Sie wird durch ein externes Tool
aufgerufen und traegt ausdruecklich:

```text
offline_only = 1
read_by_mini_dio = 0
influences_field = 0
influences_action = 0
```

Sie ist eine kompakte Erfahrungsablage, keine laufende innere Aktivitaet. Das
gleiche gilt fuer die nachgelagerten Relationsansichten aus 2090 bis 2103.

## Architekturmatrix

| Eigenschaft | Normaler Weltlauf | Leerlauf-Nachhall 1531 | Sleep-Feldmilieu 1535+ | Offline-Konsolidierung |
|---|---|---|---|---|
| eigener vorheriger Zustand wirkt weiter | innerhalb eines Weltlaufs | ja, im selben Feld | ja, innerhalb des neu gestarteten Sleep-Feldes | nein, nur gespeicherte Daten |
| Inhalte aus eigener Memory | nur passive Teilruecklesungen | nein | ja, Episodenrollen | ja, bestehende Relationsdaten |
| Feld bleibt ueber Real-Sleep-Real identisch | nein | nur innerhalb des Einzeltools | nein | kein aktives Feld |
| eigener Startausloeser | nein | nein | nein | nein |
| eigene Dauer oder Beendigung | nein | nein | nein | nein |
| laeuft ohne externen Tick weiter | nein | nein | nein | nein |
| Ergebnis beeinflusst naechsten Feldlauf | nicht als Offlineprozess | nein | nein | nein |
| Handlungseinfluss | getrennte alte Aktionsmechanik, nicht dieser Pfad | nein | nein | nein |

## Was Die Bisherigen Sleep-Befunde Weiterhin Tragen

Weiterhin getragen sind:

- passives Ausklingen eines bestehenden Feldnachhalls bei leerem Input,
- stabile Offline-Rekopplung statt freier Symbolstreuung,
- Aktivierbarkeit gespeicherter Episodenrollen ohne neue Chartwerte,
- feldzustandsabhaengige Auswahl und Kombination alter Rollen,
- selektive Wiederlesbarkeit dieser Rollen und Kombinationen in Folgewelten,
- reproduzierbare diagnostische Zwischenrollen-Kandidaten,
- verlustfreie passive Offline-Konsolidierung.

Diese Befunde zeigen, dass gespeicherte Innenordnung in einem entkoppelten
Milieu strukturierte Dynamik tragen kann.

## Was Nicht Getragen Ist

Nicht getragen sind:

- ein autonomer Uebergang vom Weltkontakt in eine Offlinephase,
- eine vom Feld selbst erzeugte Zeitfolge ohne externen Takt,
- ein organisch entstandenes Ende der Offlinephase,
- Kontinuitaet desselben MCM-Feldes durch Real A, Sleep und Real B,
- kausale Rueckwirkung der Sleep-Reorganisationsmemory auf Real B,
- selbststaendige neue Semantik aus Sleep-Kombinationen,
- autonome Feldaktivitaet, Selbstregulation oder Handlung.

## Befund

MINI_DIO besitzt innere Zustandsdynamik und teilweise memory-getragene
Offline-Inhalte. Es besitzt aktuell aber keine autonome endogene
Feldaktivitaet. Jeder Offlineprozess benoetigt einen externen Aufruf, einen
externen Takt und extern gesetzte Laufgrenzen. Seine gespeicherten Ergebnisse
werden nicht in den naechsten normalen Feldzustand zurueckgelesen.

Der fachlich belastbare Begriff fuer den aktuellen Stand lautet daher:

```text
extern bereitgestelltes Offline-Milieu
mit innerer Zustands- und Memory-Dynamik
```

Nicht belastbar waere:

```text
MINI_DIO beginnt selbst zu schlafen
oder verarbeitet autonom ohne Weltkontakt weiter.
```

2104 aendert keine Runtime, Memory oder Aktionslogik. Der Befund korrigiert
ausschliesslich die Architekturlesung der vorhandenen Mechaniken.
