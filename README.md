# MINI_DIO

MINI_DIO ist ein eigenständiges Forschungsprojekt für ein kleines, MCM-basiertes Innenfeldsystem.

Der Kern ist nicht Trading. Marktdaten werden aktuell als kontrollierte Außenwelt genutzt, weil sie Zeit, Bewegung, Energie, Rhythmus, Bruch, Wiederkehr und strukturelle Varianz liefern. Damit entsteht eine testbare Welt, an der ein künstliches MCM-Feld passiv reagieren, ordnen und Bedeutung verdichten kann.

## Worum Es Geht

MINI_DIO untersucht eine einfache, aber weitreichende Frage:

Kann ein kleines künstliches MCM-Feld aus wiederholtem Weltkontakt eine eigene innere Ordnung bilden?

Der Fokus liegt auf:

- MCM-basierter Innenfeldreaktion,
- emergenter Bedeutungsverdichtung,
- wiederkehrenden semantischen Inseln,
- Zentrum-Peripherie-Topologie,
- Drift, Übergang und Rekopplung,
- passiver Eigenregulation des Feldes,
- zyklischer Feldbewegung,
- reproduzierbarer Ordnung bei gleicher Welt.

Die aktuelle Arbeitshypothese:

Das MCM-Feld scheint passive Eigenregulation zu besitzen. Zentrum, Brücke, Drift und Übergang werden nicht als Regel programmiert, sondern als Rollen gelesen, die aus der Feldorganisation entstehen.

## Warum Das Interessant Ist

Viele technische Systeme speichern Rohdaten, berechnen Merkmale und leiten daraus eine Entscheidung ab. MINI_DIO geht bewusst anders vor.

Eine Weltlage wird nicht sofort Handlung. Sie wird zuerst Innenfeldwirkung:

```text
Weltkontakt
  -> Sehen / Hören / Fühlen
  -> MCM-Feldwirkung
  -> semantische Verdichtung
  -> passive Innenordnung
  -> spätere mögliche Regulation
```

Das Projekt fragt nicht zuerst: "Was soll das System tun?"

Es fragt zuerst:

- Was entsteht im Inneren, wenn Welt auf Feld trifft?
- Welche Zustände kehren wieder?
- Welche Bedeutung verdichtet sich?
- Was bleibt stabil?
- Was driftet?
- Was kippt?
- Was rekoppelt?
- Kann daraus eine reproduzierbare innere Topologie entstehen?

Damit ist MINI_DIO zuerst ein Forschungsinstrument für MCM-basierte Wahrnehmung, nicht ein Bot.

## Abgrenzung Zu Ähnlichen Forschungsrichtungen

MINI_DIO steht nicht isoliert. Es berührt mehrere bekannte Forschungsfelder:

- **Active Inference / Free Energy Principle**  
  Modelliert Wahrnehmung, Handlung und Selbstorganisation über Vorhersage, Unsicherheit und Minimierung freier Energie.

- **Embodied AI und ökologische Wahrnehmung**  
  Untersucht Systeme, die über Sensorik, Körperbezug und Umweltkontakt lernen.

- **Neuromorphe Systeme und Spiking Neural Networks**  
  Arbeiten mit neuronennaher Verarbeitung, zeitlicher Dynamik und energieeffizienter Aktivität.

- **Kognitive Architekturen wie OpenCog / OpenCog Hyperon**  
  Versuchen künstliche Kognition über kombinierte Wissens-, Denk- und Entscheidungssysteme aufzubauen.

- **Neuronale Simulatoren wie Nengo**  
  Ermöglichen den Bau großer neuronaler und kognitiver Modelle.

- **Selbstorganisierende adaptive Systeme**  
  Untersuchen, wie Struktur, Gedächtnis und Verhalten aus interner Dynamik entstehen können.

MINI_DIO ist mit diesen Feldern verwandt, setzt aber einen anderen Schwerpunkt:

- Nicht Vorhersage steht im Zentrum, sondern Innenfeldreaktion.
- Nicht Belohnung steht im Zentrum, sondern Feldwirkung und Rekopplung.
- Nicht Symbol-Logik steht im Zentrum, sondern emergente Bedeutungsverdichtung.
- Nicht Handlung steht am Anfang, sondern passive Ordnung.
- Nicht harte Regeln erzeugen Verhalten, sondern wiederkehrende Feldzustände werden gelesen.

Kurz gesagt:

Andere Systeme fragen oft, wie ein Agent handelt, optimiert, plant oder schlussfolgert. MINI_DIO fragt zuerst, wie ein MCM-Feld Weltkontakt innerlich organisiert, Bedeutung bildet und sich selbst stabilisiert.

## Aktueller Stand

MINI_DIO läuft als eigenständiges Python-Projekt.

Der aktuelle Forschungsstand zeigt:

- gleiche kontrollierte Welt erzeugt reproduzierbare Top-Syntax,
- gleiche kontrollierte Welt erzeugt reproduzierbare Top-Familien,
- passive Innenfeldzustände bilden unterscheidbare Wirkungsklassen,
- `field_carried` und `field_strained` treten als passive Episodenzustände auf,
- MCM-Rekopplung und Sinnes-MCM-Kopplung sind messbar,
- aktuelle Läufe bleiben bewusst ohne Trading-Handlung.

Beispiel aus dem aktuellen Forschungslauf:

```text
Top-Syntax-Überlappung:   1.0
Top-Familien-Überlappung: 1.0
Trades:                  0 -> 0
Episoden:                994 -> 994
```

Das ist wichtig: Die Reproduzierbarkeit bezieht sich hier nicht auf Profit, sondern auf innere Ordnung bei gleicher Welt.

## Projektstruktur

```text
mini_dio/      Kernpaket: Welt, MCM-Neuron, Feldwirkung, Memory, Runner
reports/       Passive Forschungsreports und Diagnose-Skripte
docs/befunde/  Aktuelle Befunde und Forschungsläufe
DIO_BAUPLAN/   Abhandlungen und Theorieanker
data/          Kontrollierte Außenwelten
memory/        Lokale Memory-Dateien, nicht für Git
debug/         Lokale Run- und Report-Ausgaben, nicht für Git
tools/         Prüf- und Forschungsketten
tests/         Platz für spätere Tests
```

## Wichtige Grenze

MINI_DIO ist aktuell passive Forschungsinfrastruktur.

Reports sind keine:

- Trading-Regeln,
- Gates,
- Entry-Signale,
- Motorik,
- Strategie,
- Beweise einer universellen MCM-Topologie.

Sie sind Beobachtungen passiver Feldorganisation.

Handlung darf erst wieder Thema werden, wenn passive Innenordnung, Rekopplung, Bedeutung und Konsequenz stabil genug verstanden sind.

## Starten

Projekt prüfen:

```powershell
python tools\check_project.py
```

Ein einzelner passiver Lauf:

```powershell
python -m mini_dio.run_mini --data data/kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv
```

Standard-Forschungskette:

```powershell
python tools\run_research_chain.py
```

Diese Kette führt zwei passive Läufe auf derselben kontrollierten Welt aus, vergleicht beide Reports und schreibt:

- `debug/research_chain/research_chain_summary.json`
- `docs/befunde/AKTUELLER_FORSCHUNGSLAUF.md`

Mehrwelt-Vergleich:

```powershell
python tools\compare_research_chains.py
```

Dieses Werkzeug vergleicht mehrere `research_chain_summary.json`-Dateien und schreibt:

- `docs/befunde/MEHRWELT_VERGLEICH.md`

Erwartetes CSV-Format:

```text
timestamp_ms,open,high,low,close,volume
```

## Aktuelle Befundkette

Die aktuellen Befunde liegen unter:

```text
docs/befunde/
```

Besonders relevant sind:

- `107_KLEINER_DURCHBRUCH_MCM_TOPOLOGIE_BEFUND.md`
- `108_REPRODUZIERTE_MCM_TOPOLOGIE_ROLLENKARTE.md`
- `114_PASSIVE_MCM_TOPOLOGIE_MATRIX.md`
- `119_MCM_FELD_EIGENREGULATION_BEFUND.md`
- `120_PASSIVE_MCM_ZYKLUSKARTE.md`
- `AKTUELLER_FORSCHUNGSLAUF.md`
- `AKTUELLER_FORSCHUNGSLAUF_2024_01.md`
- `MEHRWELT_VERGLEICH.md`

Der stärkste aktuelle Befund ist die passive MCM-Zykluskarte:

- Zentrum kann halten.
- Brücken können Zentrum tragen.
- Drift kann zum Zentrum zurückführen.
- Übergang kann rekoppeln.
- Drift und Übergang können über Zentrum in Brückenzustände übergehen.

Der aktuelle Mehrwelt-Vergleich zeigt zusätzlich:

- Innerhalb einzelner Welten reproduzieren sich Top-Syntax und Top-Familien stabil.
- Zwischen verschiedenen Welten verschieben sich Syntax und Familien deutlich.
- Das passive Feldprofil bleibt dennoch ähnlich.
- Die dominante Feldwirkung kann je nach Weltspannung wechseln, ohne dass die Feldordnung kollabiert.

Das spricht für weltbezogene Innenfeldordnungen statt wahlloser Speicherung.

## Was MINI_DIO Nicht Ist

MINI_DIO ist aktuell kein Tradingbot.

Es ist kein fertiges KI-System, kein autonomer Agent und kein Beweis für Bewusstsein. Es ist ein kontrollierter Forschungsaufbau, um zu untersuchen, ob ein kleines MCM-Feld reproduzierbare innere Bedeutungsräume aus Weltkontakt bilden kann.

Diese Vorsicht ist wichtig, weil der interessante Teil gerade darin liegt, nichts vorschnell als Handlung, Strategie oder Intelligenz zu verkaufen.

## Nächste Forschungsrichtung

Der nächste Schritt ist die Prüfung über mehrere kontrollierte Außenwelten.

Dabei wird untersucht, ob die beobachtete Innenfeldordnung nur an eine einzelne Welt gebunden ist oder ob MINI_DIO auch bei veränderten Weltsequenzen stabile, driftende oder neu entstehende Bedeutungsräume bildet.

Leitfragen:

- bleiben Bedeutungsinseln stabil?
- welche neuen Bedeutungsinseln entstehen?
- wann beginnt eine vorhandene Bedeutung zu driften?
- wann bildet sich eine neue Brücke zwischen Feldbereichen?
- wie verändert sich die Zentrum-Peripherie-Ordnung?
- bleibt passive Eigenregulation auch unter veränderter Weltspannung erkennbar?

Wenn diese Befunde über mehrere Welten reproduzierbar bleiben, entsteht daraus die Grundlage für eine sauberere wissenschaftliche Beschreibung der MCM-Feldorganisation in MINI_DIO.
