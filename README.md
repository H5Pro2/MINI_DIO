# MINI_DIO

MINI_DIO ist ein eigenständiges Forschungsprojekt für ein kleines, [MCM](https://github.com/H5Pro2/Mental-Core-Matrix-MCM)-basiertes Innenfeldsystem.

DIO steht für Digitaler Organismus. Aus dem Forschungsprozess heraus entstand die Überlegung, einem solchen Organismus eine kontrollierte Außenwelt zu geben, die energiegeladen, ruhig, rhythmisch, brüchig oder wiederkehrend sein kann. Dafür wird eine zeitliche Datenreihe eines dynamischen Systems nicht als Handlungssignal gelesen, sondern als visuelle, tonale und energetische Spur in eine testbare Welt übersetzt. An dieser Welt kann ein künstliches MCM-Feld passiv reagieren, ordnen und Bedeutung verdichten.


![MINI_DIO](docs/bilder/MINI_DIO.PNG)

## Worum Es Geht

MINI_DIO untersucht eine einfache, aber weitreichende Frage:

Kann ein kleines künstliches [MCM-Feld](https://github.com/H5Pro2/Mental-Core-Matrix-MCM) aus wiederholtem Weltkontakt eine eigene innere Ordnung bilden?

Der Fokus liegt auf:

- [MCM](https://github.com/H5Pro2/Mental-Core-Matrix-MCM)-basierter Innenfeldreaktion,
- emergenter Bedeutungsverdichtung,
- wiederkehrenden semantischen Inseln,
- Zentrum-Peripherie-Topologie,
- Drift, Übergang und Rekopplung,
- passiver Eigenregulation des Feldes,
- zyklischer Feldbewegung,
- reproduzierbarer Ordnung bei gleicher Welt.

Die aktuelle Arbeitshypothese:

Das [MCM-Feld](https://github.com/H5Pro2/Mental-Core-Matrix-MCM) scheint passive Eigenregulation zu besitzen. Zentrum, Brücke, Drift und Übergang werden nicht als Regel programmiert, sondern als Rollen gelesen, die aus der Feldorganisation entstehen.

In den bisher geprüften Welten hat MINI_DIO wiederholt eine Feldform ausgebildet, die der hypothetischen MCM-Topologie nahekommt: zentrumsnahe Stabilisierung, offene Brücken, driftende Nähebereiche und belastete Randspannung. Nach erneuter Codeprüfung gibt es aktuell keinen Hinweis darauf, dass diese Form durch eine feste Vorgabe wie "das muss so aussehen" erzeugt wird. Die Topologiebegriffe entstehen in der nachgelagerten Diagnose und Beschreibung; die Laufstruktur selbst arbeitet mit Sehen, Hören, Fühlen, MCM-Feldwirkung und eigener `dio_*`-Syntax. Auch nach mehreren Memory-Neustarts blieb dieser Befund in den geprüften Welten auffällig reproduzierbar.

## Warum Das Interessant Ist

Viele technische Systeme speichern Rohdaten, berechnen Merkmale und leiten daraus eine Entscheidung ab. MINI_DIO geht bewusst anders vor.

Eine Weltlage wird nicht sofort Handlung. Sie wird zuerst Innenfeldwirkung:

```text
Weltkontakt
  -> Sehen / Hören
  -> Rezeptoren
  -> Fühlen
  -> MCM-Feldwirkung
  -> semantische Verdichtung
  -> passive Innenordnung
  -> spätere mögliche Regulation
```

Die aktuelle Wahrnehmungsarchitektur trennt damit bewusst:

- Sehen liest Form und Struktur.
- Hören liest Energie, Ton und Spannung.
- Sehen ist Distanzwahrnehmung: Eine Form wirkt nicht direkt wie Kontakt, sondern kann über Erfahrung/Memory Bedeutung koppeln.
- Hören kann als Frequenz, Ton und Rhythmus das Feld stimulieren.
- Fühlen/Spüren ist direkter Kontakt zur Welt; in den aktuellen Kurswelten ist dieser direkte Kontakt noch nicht aktiv.
- Rezeptoren bilden aus Sinnesaufnahme, Frequenzstimulation, möglicher Memory-Kopplung und direktem Kontakt eine geordnete Eingangswirkung.
- MCM-Feldwirkung entsteht aus dieser Eingangswirkung.

Die Außenwelt wirkt nicht direkt in das MCM-Feld. MINI_DIO verarbeitet zuerst Sinneskontakt,
dann Rezeptorkontakt und erst daraus eine MCM-Feldwirkung.

Damit ist die Rezeptorschicht ein fundamentaler Schutzbaustein:

```text
Sie schützt das MCM-Feld vor Rohdatenüberlagerung.
```

Das Feld wird nicht mit Außenwelt-Daten geflutet, sondern reagiert auf geordnete Kontaktqualität.

Wichtig bleibt die Trennung:

```text
Sehen + Hören ist nicht Fühlen.
```

Sehen, Hören und ein späteres Tasten sind eigene Sinnesachsen. Eine taktile Achse müsste separat entstehen, zum Beispiel über eine Mousepad- oder Kontaktflächen-Simulation mit Kontaktpunkt, Druck, Bewegung, Reibung, Stabilität und Nachhall.

MINI_DIO unterscheidet damit:

- Sinneswahrnehmung: Was kommt über einen Kanal an?
- Reflektive Innenwahrnehmung: Wie wirkt diese Wahrnehmung in mir?
- MCM-Feldwirkung: Was verändert diese Wahrnehmung in meiner Feldordnung?

Im Code wird diese Trennung kompatibel geführt:

```text
mcm_feldwirkung = fachlicher Name
fuehlen = alter Kompatibilitätsname
```

Neue Kernlogik liest bevorzugt `mcm_feldwirkung`. Alte `fuehlen_*`-Spalten bleiben erhalten, damit historische Befunde und Reports vergleichbar bleiben.

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

Damit ist MINI_DIO zuerst ein Forschungsinstrument für [MCM](https://github.com/H5Pro2/Mental-Core-Matrix-MCM)-basierte Wahrnehmung, kein Ausführungssystem.

## Visuelle Übersicht

Die folgenden Grafiken beschreiben MINI_DIO als Forschungsaufbau: von Wahrnehmungsreduktion über Zeichenbildung und semantische Kandidaten bis zur MCM-Topologie.

![Wahrnehmung Und Reduktion](docs/bilder/01_WAHRNEMUNG_UND_REDUKTION.PNG)

![Passive Zeichenbildung](docs/bilder/02_PASSIVE_ZEICHENBILDUNG.PNG)

![Semantik-Kandidatenkarte](docs/bilder/03_SEMANTIK_KANDIDATENKARTE.PNG)

![DOLU-Relevanz, MINI_DIO Und MCM](docs/bilder/04_DOLU_RELEVANZ_MINI_DIO_UND_MCM.PNG)

![Emergenzpfad](docs/bilder/05_EMERGENZPFAD.PNG)

![MCM-Topologie](docs/bilder/06_MCM_TOPOLOGIE.PNG)

![Abgrenzung](docs/bilder/07_ABGRENZUNG.PNG)

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

Andere Systeme fragen oft, wie ein Agent handelt, optimiert, plant oder schlussfolgert. MINI_DIO fragt zuerst, wie ein [MCM-Feld](https://github.com/H5Pro2/Mental-Core-Matrix-MCM) Weltkontakt innerlich organisiert, Bedeutung bildet und sich selbst stabilisiert.

## Aktueller Stand

MINI_DIO läuft als eigenständiges Python-Projekt.

Der aktuelle Forschungsstand zeigt:

- gleiche kontrollierte Welt erzeugt reproduzierbare Top-Syntax,
- gleiche kontrollierte Welt erzeugt reproduzierbare Top-Familien,
- passive Innenfeldzustände bilden unterscheidbare Wirkungsklassen,
- `field_carried` und `field_strained` treten als passive Episodenzustände auf,
- [MCM-Rekopplung](https://github.com/H5Pro2/Mental-Core-Matrix-MCM) und Sinnes-MCM-Kopplung sind messbar,
- Randspannung erscheint derzeit eher als Variantenfamilie als als einzelnes festes Zeichen,
- aktuelle Preview-Zeichen lassen sich passiv in Rollenfamilien wie Rekopplungsnähe, Randspannung und offene Variante lesen,
- eine neue Realwelt erweitert vor allem Rekopplungsnähe, ohne die bisherige Gruppenordnung aufzulösen,
- die Rollenrelation blieb in der ersten Stabilitätsmatrix nach neuer Welt stabil,
- die aktuelle Forschung zeigt, dass Sinnesberechnung selbst ein kritischer Faktor ist; ein weicher weltrelativer Wahrnehmungsadapter wird daher passiv geprüft,
- die Mehrweltprüfung dieses Adapters zeigt stark vereinheitlichte Aufnahme über SOL/BTC, 5m/1h und Stresswelten; das reduziert Rohdatenlast, muss aber weiter gegen echte Weltspannung geprüft werden,
- rohe Bruchfenster bleiben im weltrelativen Modus bisher sensorisch sichtbar und zeigen lokal erhöhte Kippnähe,
- eine frische Laufprüfung mit SOL 5m, SOL 1h, BTC 5m und BTC 1h bestätigt diesen Brucherhalt bei passiver Wahrnehmung,
- die weltrelative Topologie-Matrix liest Rollenqualität statt feste `dio_*`-Namen und zeigt in den geprüften SOL/BTC- und 5m/1h-Welten eine stabile Rollenordnung aus Zentrum, offener Variante und Rand/Kippnähe,
- die Rezeptorschicht trennt jetzt Außenweltkontakt von innerer MCM-Wirkung: Sehen liefert Formauffälligkeit, Hören liefert Ton-/Energie-Stimulation, direkter Kontakt bleibt ein eigener späterer Spürkanal; daraus entsteht geordnete MCM-Feldwirkung,
- die Rezeptorprüfung über SOL/BTC/KAS auf 5m und 1h zeigt weiterhin `zentrum_mit_rand_und_uebergang`,
- Öffnung aus dem Zentrum zeigt erhöhten `contact_pressure` und fallendes `contact_alignment`; Rekopplung zeigt sinkenden Druck und bessere Passung,
- längere 5k/10k-Rezeptorwelten bleiben bisher ebenfalls in `zentrum_mit_rand_und_uebergang`; neue Kontakt-Archetypen sind durch Dauer allein noch nicht zwingend sichtbar,
- lokale Rezeptor-Kontaktinseln entstehen in Dauerlastwelten, bleiben meist kurz und rekoppeln in vielen Fällen wieder,
- die Kontaktinseln zerstreuen sich auf der rohen `symbol_family`-Ebene stark, verdichten sich aber auf der `mcm_field_episode_preview`-Ebene in deutlich weniger MCM-Episodenfamilien,
- rekoppelnde und offen getragene Kontaktinseln sind dadurch als passive Innenfeld-Semantik unterscheidbar; sie bleiben Diagnose, keine Handlungssignale,
- die Rezeptorschicht ist damit als Schutzgrenze vor der MCM-Schicht zu behandeln: Weltkontakt wird erst rezeptorisch übersetzt, bevor daraus MCM-Fühlen entsteht,
- der erste Reproduktionstest der MCM-Episodenfamilien zeigt: Familien kehren weltübergreifend wieder, tragen aber keine starre 1:1-Bedeutung; ihre konkrete Kontaktqualität bleibt welt- und feldlageabhängig,
- `world_relative` ist jetzt passiver Standardmodus der Sinnesaufnahme, weil er im Systemabgleich Übersteuerung reduziert, Feld-Episoden deutlich weniger fragmentiert und die MCM-Rekopplung verbessert,
- die erste Topologieprüfung nach Umstellung auf `world_relative` zeigt in SOL/BTC und 5m/1h weiterhin `zentrum_mit_rand_und_uebergang`: Zentrum bleibt dominant, offene Variante und Rand/Kippnähe bleiben als Nebenrollen sichtbar,
- ruhige Kurzfenster, Stress-Kurzfenster und Expansionswelten bleiben ebenfalls in derselben Rollenordnung; Stress erhöht bisher lokal Rand/Kippnähe, erzwingt aber keine neue dominante Mischklasse,
- gleich lange Sideways- und negative Stresswelten relativieren den Kurzsegment-Befund: Stress erhöht Rand/Kippnähe nicht automatisch, sondern kann je nach Weltqualität zentrumsnah rekoppeln oder offener/variantenreicher werden,
- die Differenz zwischen negativen Stresswelten liegt bisher eher in Drift, Richtungswechsel, Persistenz und Rekopplung als in bloßer Weltlautstärke,
- lokal zeigt sich: `NEG_STRESS_2024` wird nicht randlastiger, sondern unterbricht zentrumsnahe Rekopplung häufiger und verschiebt mehr Episoden in offene Variante,
- die offene Variante ist auf roher `symbol_family`-Ebene stark fragmentiert, verdichtet sich aber auf MCM-Preview-Ebene; sie wirkt derzeit wie eine passive Bedeutungsspannweite um das Zentrum, nicht wie eine einzelne gereifte Bedeutungsinsel,
- `dio_mcm_episode_1t5bcxp` erscheint in der aktuellen 12-Welten-Prüfung über Stress, Ruhe, Expansion sowie SOL/BTC/KAS und 5m/1h als wiederkehrende dominante MCM-Preview-Familie; die darunterliegenden Rohsymbole bleiben stark variabel,
- im Assetprofil bleibt `dio_mcm_episode_1t5bcxp` bei SOL, BTC und KAS dominant, aber BTC verteilt deutlich mehr Gewicht auf andere Preview-Familien wie `dio_mcm_episode_0y50lf3` und `dio_mcm_episode_183drjy`; das spricht für gleiche Grundsprache bei unterschiedlicher Innenfeld-Gewichtung,
- als nächste passive Schicht wird Regulation als Wahrnehmungs-Einstellung gefasst: Fokus/Abstand, lauter/leiser, scharf/unscharf und Druck/Entspannung; diese Achsen beschreiben Aufnahmequalität, nicht Handlung,
- die erste Regulationsachsen-Prüfung liest `1t5bcxp`, `0y50lf3` und `183drjy` alle als nah, leise, eher unscharf und entspannend; die Trennung liegt damit bisher nicht in harten Regulationsklassen, sondern in Gewichtung, Häufigkeit, Streuung und Nachbarschaft,
- die Nachbarschaftsdiagnose zeigt diese Familien zuerst als stabile Selbstinseln; die Boundary-Diagnose trennt echte Kanten davon und liest besonders `1t5bcxp <-> 183drjy` als wiederkehrende passive Feldbewegung,
- die Übergangspaar-Diagnose zeigt wiederkehrende Feldbewegungen zwischen Bedeutungsinseln; besonders `1t5bcxp -> 183drjy` wirkt drucksenkend und leicht rekoppelnd, während der Rückweg nach `1t5bcxp` mehr Druck und offenere Variante tragen kann,
- die erste Paar-Klassifikation liest `1t5bcxp -> 183drjy` als rekoppelnden Grundinsel-Wechsel und `183drjy -> 1t5bcxp` als druckvollere Rückführung; diese Klassen sind Arbeitsklassen, keine starre Ontologie,
- die Validierung über Stress-, Seitwärts- und Expansionswelten hält diese Bewegungsarten lesbar: `1t5bcxp -> 183drjy` bleibt als ruhiger Grundinsel-Wechsel sichtbar, während `183drjy -> 1t5bcxp` weiterhin druckvoller zurückführt,
- die Rohwelt-Segmentlupe zeigt das Kontaktmilieu dieser Bewegungen: `1t5bcxp -> 183drjy` liegt überwiegend in rekoppelnder Lage, während der Rückweg im Wechsel selbst häufiger Drucklage und stärkeren Energiebruch trägt,
- die Kontaktmilieu-Wiederkehrprüfung zeigt bisher nur ein klar stabiles Milieu: `1t5bcxp -> 183drjy` erscheint überwiegend als `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage`; die anderen geprüften Übergänge bleiben variabler,
- die Langweltprüfung relativiert diese Stabilität: `1t5bcxp -> 183drjy` bleibt häufig, aber sein Milieu wird breiter; die rekoppelnde Signatur bleibt sichtbar, ist aber nicht mehr dominant genug, um als universell stabil zu gelten,
- die Driftqualitätsprüfung trennt tragbare Drift von Fragmentierung: `1t5bcxp -> 183drjy` wirkt breit driftend, während `183drjy -> 1t5bcxp` stark fragmentiert erscheint,
- die Rücklegung auf Weltmerkmale zeigt eine erste Milieu-Neigung: bei niedrigerer Passung erscheint `1t5bcxp -> 183drjy` eher `offen_stabil`, bei höherer Passung in den SOL-Welten eher `rekoppelnd_stabil`,
- daraus entsteht eine passive Regulationswahrnehmung: MINI_DIO liest nicht nur, dass eine Feldbewegung vorkommt, sondern auch, wie sie getragen wird: eng getragen, offen driftend, breit driftend oder fragmentiert,
- die erste Reproduktionsprüfung dieser Regulationsqualitäten zeigt: `1t5bcxp -> 183drjy` bleibt als Bewegung erhalten, trägt aber mehrere Qualitäten; `183drjy -> 1t5bcxp` bleibt deutlich fragmentierter,
- eine neue Asset-/Zeitgruppe aus SOL, BTC und KAS über 5m, 15m, 30m und 1h bestätigt keine starre Qualität, aber eine gerichtete Differenz: `1t5bcxp -> 183drjy` wirkt eher offen getragen, der Rückweg bleibt stärker fragmentiert,
- längere 4000er Teilwelten aus SOL/BTC 1h ziehen `1t5bcxp -> 183drjy` wieder näher an rekoppelnde Tragung, während `183drjy -> 1t5bcxp` fragmentiert bleibt; die Asymmetrie wirkt damit robuster als eine starre Symbolbedeutung,
- eine frische Memory-Reproduktion derselben 4000er Teilwelten wiederholt diese gerichtete Asymmetrie exakt in den Kernwerten: `1t5bcxp -> 183drjy` bleibt dominant `eng_getragen`, der Rückweg bleibt dominant `fragmentiert`,
- eine andere Jahreswelt aus SOL/BTC 2025 1h bestätigt die Richtung: `1t5bcxp -> 183drjy` bleibt eher eng getragen, `183drjy -> 1t5bcxp` bleibt stärker fragmentiert; die genaue Ausprägung driftet, die Bewegungsrichtung bleibt lesbar,
- die 15m-Zeitauflösung bestätigt die Asymmetrie ebenfalls: `1t5bcxp -> 183drjy` wird dort als `wiederkehrend_stabil` und dominant `eng_getragen` gelesen, während der Rückweg fragmentierter bleibt,
- die 5m-Zeitauflösung bestätigt den Befund trotz stärkerer Mikrostruktur: `1t5bcxp -> 183drjy` bleibt `rekoppelnd_stabil`/`eng_getragen`, der Rückweg bleibt fragmentierter,
- die gemeinsame Zeitauflösungs-Matrix zeigt: 1h, 15m und 5m tragen dieselbe gerichtete Grundbewegung; stabil ist nicht ein Einzelzeichen, sondern Richtung, Feldlage, Wiederkehr und Tragart,
- die Jahresmatrix 2024/2025 zeigt dieselbe Richtung über beide Jahreswelten: `1t5bcxp -> 183drjy` bleibt dominant `eng_getragen`, `183drjy -> 1t5bcxp` bleibt dominant `fragmentiert`; 2025 wirkt schärfer bruch-/drucknah, 2024 weicher,
- eine begrenzte KAS-Gegenprobe zeigt dieselbe Richtung, aber mit sehr kleiner Ereignisbasis: `1t5bcxp -> 183drjy` bleibt `eng_getragen`, der Rückweg bleibt `fragmentiert`; KAS braucht längere oder gezielter extrahierte Welten für eine belastbare Asset-Reproduktion,
- aus den bisherigen Befunden ist eine passive Feldbewegungs-Ableitung entstanden: Feldlage, Tragart, Richtung, Wiederkehr, Rekopplung und Fragmentierung bilden eine gewachsene Innenfeldspur, aber keine Handlung und kein Gate,
- die technische Skizze für `MCMFieldMovementMemory` definiert eine passive Speicherschicht für MCM-Feldbewegungen; sie speichert Wiederkehr, Tragart, Drift, Rekopplung und Fragmentierung, aber keine Wahrnehmungssteuerung,
- `MCMFieldMovementMemory` ist als erster passiver Code-Baustein umgesetzt: `mini_dio/mcm_field_movement_memory.py` verdichtet vorhandene Befundmatrizen zu gerichteten Innenfeldspuren; `tools/report_mcm_field_movement_memory.py` schreibt daraus eine Summary. Der erste Lauf liest `1t5bcxp -> 183drjy` als `recurrently_carried` und den Rückweg als `recurrently_fragmented`, weiterhin ohne Handlung, Gate oder Strategie,
- die erweiterte Mehrwelt-Feldbewegungs-Memory liest über die vorhandenen Bewegungsmatrizen und Reproduktionsbefunde dieselbe Grundasymmetrie: der Hinweg bleibt dominant getragen, der Rückweg dominant fragmentiert. Da sich Quellen teilweise aus denselben Grundbefunden ableiten, ist das ein Verdichtungsbefund, keine unabhängige Statistik,
- eine unabhängige 1000er Late-Shift-Welt erzeugt bewusst keine künstlich gereifte Qualität: `02xikfk -> 1t5bcxp` wird als junge, breit driftende Spur gelesen. Das bestätigt die Trennschärfe der Feldbewegungs-Memory: wiederkehrende Bewegung wird verdichtet, Einzelkontakt bleibt jung,
- die Achsen Fokus/Abstand, lauter/leiser, scharf/unscharf und Druck/Entspannung gehören nicht in diese Memory-Schicht; sie bilden eine getrennte rezeptorisch-regulatorische Wahrnehmungsschicht, die beschreibt, wie Informationen unterschiedlicher Asset- und Weltklassen in das MCM-Feld gelangen,
- ältere Dateien mit `REGULATIONSQUALITAET` im Namen bleiben als Befundhistorie erhalten. Für den aktuellen Bauzustand gilt die neue Trennung: Feldbewegungs-Memory speichert Feldwirkung; rezeptorisch-regulatorische Wahrnehmung beschreibt Aufnahmequalität,
- die strikte Trennung ist jetzt als Bauprinzip festgehalten: Das MCM-Feld bleibt einfach und behält seine passive Eigenregulation; reguliert wird nur die Aufnahme vor dem Feld, also wie Weltkontakt über Fokus/Abstand, lauter/leiser, scharf/unscharf und Druck/Entspannung am Feld ankommt,
- die Sinneswege sind fachlich korrigiert: `visual_form_salience` beschreibt sichtbare Formauffälligkeit, `auditory_stimulation` beschreibt Ton-/Energie-Stimulation, `direct_contact_pressure` bleibt der spätere direkte Kontaktkanal und `field_intake_pressure` ist der resultierende Eingangsdruck ins MCM-Feld. Alte Spalten wie `visual_contact`, `auditory_contact` und `contact_pressure` bleiben nur als Kompatibilitätsnamen erhalten,
- Fokus/Abstand, lauter/leiser, scharf/unscharf und Druck/Entspannung sind jetzt als Organismus-Eigenschaften gefasst. Technisch werden sie als `perception_regulation_state` und `organism_adaptation_state` sichtbar. Sie sind keine Regeln fuer das Feld, sondern Faehigkeiten, mit denen MINI_DIO lernt, Weltaufnahme anzupassen,
- die Anpassung ist jetzt sinnesgetrennt zu lesen: MINI_DIO kann theoretisch stärker sehen und gedämpfter hören, mehr Abstand halten und trotzdem genauer fokussieren, oder Fühlen/Spüren erst bei echtem Kontakt stärker zulassen. Welche Kombination trägt, muss über MCM-Feldrückmeldung und episodische Erfahrung entstehen,
- `field_intake_pressure` geht als tatsächliche Rezeptorwirkung in `mcm_tension` ein. `adaptation_potential`, `adapted_field_intake_pressure` und der alte Kompatibilitätsname `regulation_damping` bleiben Diagnosewerte; sie dämpfen das Feld nicht mehr heimlich global,
- die erste sinnesgetrennte Achspruefung ueber vier kurze Kontrollwelten zeigt: Die Achsen sind technisch sauber sichtbar, aber im Weltmittel noch eng beieinander. Der naechste sinnvolle Schritt ist deshalb lokale Episodenpruefung statt weiterer globaler Mittelwerte,
- die lokale Sinnesachsen-Episodenkarte zeigt: `hoeren_hin` in stabiler Innenfeldlage ist weltuebergreifend eine ruhige, haeufig rekoppelnde Achsenlage; lokaler `feldinput` liegt naeher an Strain und Kontaktlast,
- die Rekopplungsqualitaetspruefung verdichtet diesen Befund: Hoeren, Sehen und Feldkontakt muessen getrennt gelesen werden. Die naechste Frage ist nicht globale Daempfung, sondern welche Aufnahmeart in welcher Weltlage tragbar rekoppelt,
- die Gegenprobe ueber SOL/BTC/KAS sowie 5m/1h bestaetigt diese Richtung: `hoeren_hin` bleibt in allen geprueften Welten die ruhigste lokale Rekopplungsachse, waehrend `feldinput` weiter die kontaktlastigere Feldinput-Seite traegt,
- damit wird die rezeptorisch-regulatorische Wahrnehmungsschicht als Aufnahmequalitaet gestuetzt: MINI_DIO muss nicht das Feld global daempfen, sondern lernen, wie eine Weltlage ueber Hoeren, Sehen, Abstand oder Feldkontakt aufgenommen wird,
- die erste Faehigkeitslesung von `hoeren_hin` zeigt Rang 1 in allen geprueften Gegenwelten, einen sehr hohen stabilen Innenfeldanteil und deutlich weniger Strain/Feldinput als direkter Feldkontakt. Das spricht fuer Hinhoren als passive Aufnahmefaehigkeit, nicht fuer eine Handlungsregel,
- der Sinnesaufnahme-Vergleich trennt die Rollen klarer: `hoeren_hin` ist die ruhigste akustische Rekopplung, `sehen_fokus` bleibt visuell tragend, `feldinput` ist der kontaktlastige direkte Feldkontakt. Damit wird Aufnahmequalitaet als lokale Faehigkeit lesbar, nicht als globaler Daempfungswert,
- die Wiedererkennungspruefung zeigt 51 Signaturen, die in mindestens drei Gegenwelten wiederkehren; 6 davon lesen sich als reproduzierte ruhige Aufnahmen. Die staerkste Spur ist `hoeren_hin + inner_effect_stable + dio_mcm_episode_0e7qvj1`, gefolgt von `sehen_fokus + inner_effect_stable + dio_mcm_episode_0e7qvj1`,
- die assetgetrennte Feldtragungspruefung zeigt: BTC, SOL und KAS nutzen dieselbe passive Vorschlagssprache, bilden aber unterschiedliche Trag- und Entlastungsprofile. BTC wirkt balancierter, SOL und KAS zeigen staerkeren Abstandszug; `ruhig hinhoeren` bleibt uebergreifend die am staerksten getragene Aufnahmeart,
- das assetbezogene Organismusprofil trennt Bedarf von Tragung: BTC ruft eher Fokus auf, SOL/KAS rufen eher Abstand auf; in allen drei Assets traegt aber `ruhig hinhoeren` am staerksten. Das stuetzt die Trennung zwischen haeufig benoetigter Aufnahmefaehigkeit und tatsaechlich tragender Rekopplung,
- die Assetprofil-Stabilitaetspruefung zeigt: BTC bleibt in vier Quellen bei Fokusbedarf und getragener Hoerrekopplung; SOL bleibt in drei sehr unterschiedlichen Welten bei Abstandsbedarf und getragener Hoerrekopplung; KAS passt in die Richtung, ist aber bisher nur ein zusammengefasster Zeitebenenblock und daher noch keine echte Stabilitaetsreihe,
- die KAS-Einzelweltpruefung zerlegt KAS jetzt in 5m, 15m, 30m und 1h. Ergebnis: KAS bleibt in allen vier Einzelquellen bei Abstandsbedarf, getragener Hoerrekopplung und drucknaher Kontaktentlastung. Damit ist KAS nicht mehr nur als Block, sondern als eigene Stabilitaetsreihe gegen BTC und SOL lesbar,
- die Jahreserweiterung mit BTC/SOL 2025 zeigt: Die tragende Grundaufnahme bleibt ueber alle Assets `ruhig hinhoeren`. SOL und KAS bleiben auch im Bedarf stabil abstandsnah; BTC bleibt in der Tragung stabil, verschiebt den Bedarf aber in den 2025er Einzelquellen von Fokus zu Abstand,
- die lokale BTC-2025-Gegenlesung zeigt: Diese Verschiebung entsteht nicht grob aus mehr Roh-Abstandsaufnahme. Die lokalen Sinnesachsen bleiben relativ nah; die Aenderung liegt eher in der Bedeutungs-/Regulationsgewichtung nach der Aufnahme. BTC-2025 hoert weiter stabil, verarbeitet die aufgenommene Lage aber staerker als Abstand/Kontaktentlastung,
- damit entsteht eine passive Lernspur: gleiche Aufnahmeart, aehnliche Innenfeldlage und aehnliche MCM-Feldwirkung werden wiedererkennbar, ohne Handlung, Gate oder Strategie,
- `SensoryIntakeMemory` ist als passiver Speicherbaustein umgesetzt: die erste Memory-Summary liest 409 Aufnahme-Spuren, davon 6 reproduzierte ruhige Aufnahmen und 124 kontaktlastige Aufnahmen. Gespeichert wird Aufnahmequalitaet vor dem Feld, nicht Handlung, Gate oder Strategie,
- eine neue Gegenwelt `BTC_2024_5M_QUIET_4000` trifft 129 vorhandene Intake-Keys wieder; 86 davon behalten dieselbe passive Memory-Qualitaet. Das spricht fuer wiedererkennbare Aufnahmefamilien, nicht fuer Handlung oder Steuerung,
- eine deutlich andere Stress-Gegenwelt `SOL_2023_NEGATIVE_STRESS_10K` trifft 135 vorhandene Intake-Keys wieder; 90 davon behalten dieselbe passive Memory-Qualitaet. Damit bleibt die passive Sinnesaufnahme-Memory auch unter anderer Weltspannung teilweise stabil. Gleichzeitig entstehen junge und kontaktlastige Einzelspuren, die als Drift oder neue Aufnahmequalitaet weiter geprueft werden muessen,
- lokal bleibt `hoeren_hin` auch in der Stresswelt die ruhigste Rekopplungsachse. `sehen_fokus` bleibt nahe daran, waehrend `feldinput` mehr Strain und Kontaktlast traegt. Das stuetzt weiter die Trennung zwischen Hoeren, Sehen und direktem Feldkontakt,
- eine Seitwaerts-Gegenwelt `SOL_2026_SIDEWAYS_10K` trifft 125 vorhandene Intake-Keys wieder; 79 davon behalten dieselbe passive Memory-Qualitaet. Damit zeigt sich dieselbe Grundrichtung auch in einer ruhigeren, seitlichen Weltspannung,
- der direkte Gegenweltvergleich ueber Quiet, Stress und Sideways zeigt: `hoeren_hin` bleibt jeweils die ruhigste Rekopplungsachse, `sehen_fokus` bleibt nahe daran und `feldinput` bleibt die kontaktlastigere Feldinput-Seite. Damit wird Aufnahmequalitaet als passive Familienbildung vor dem Feld weiter gestuetzt,
- eine positive Expansionswelt `SOL_2023_POSITIVE_EXPANSION_10K` trifft 150 vorhandene Intake-Keys wieder; 101 davon behalten dieselbe passive Memory-Qualitaet. In dieser Pruefung zerlegt Expansion die Aufnahmefamilien nicht, sondern zeigt bisher die staerkste Anschlussfaehigkeit zur Basis-Memory,
- der Gegenweltvergleich ueber Quiet, Stress, Sideways und Expansion bestaetigt die Rollenaufteilung: `hoeren_hin` bleibt ruhig rekoppelnd, `sehen_fokus` bleibt formnah tragend und `feldinput` bleibt kontaktlastiger,
- eine unabhaengige BTC-5m-Gegenprobe mit 2000 Zeilen trifft 7 von 7 gebildeten Intake-Keys in der Basis-Memory wieder. Zwei behalten dieselbe Qualitaet, vier werden von reifer Basisqualitaet zu junger Spur gelesen und eine wird kontaktlastiger. Damit wirkt die Grundsignatur assetuebergreifend anschlussfaehig, aber bei kurzer Welt noch nicht gleich gereift,
- in dieser BTC-Gegenprobe bleibt `hoeren_hin` ebenfalls die beste Rekopplungsachse. `sehen_fokus` bleibt nahe daran, waehrend `feldinput` und `fuehlen_abstand` mehr Kontaktlast tragen,
- eine laengere BTC-5m-Gegenprobe mit 4000 Zeilen trifft erneut 7 von 7 gebildeten Intake-Keys in der Basis-Memory wieder. Zwei Kontaktqualitaeten bleiben reproduziert, fuenf ruhige/tragende Achsen bleiben aber junge Spuren. Das spricht fuer stabile Anschlussfaehigkeit der Signatur, aber gegen die vorschnelle Annahme, dass mehr Weltlaenge automatisch gleiche Reife erzeugt,
- die passive Regulationsvorschlagsschicht ist diagnostisch umgesetzt: sie liest aus der Sinnesaufnahme-Memory kontinuierliche Vorschlagsrichtungen wie ruhig hinhoeren, Sehen schaerfen, Abstand bilden, leiser/weicher aufnehmen und Druck/Feldkontakt entlasten. Sie greift nicht in Handlung, Strategie oder MCM-Feld ein,
- in den BTC-Gegenproben 5m/1h und Quiet/Stress bleibt die Vorschlagsverteilung identisch. Das stuetzt die rezeptorisch-regulatorische Wahrnehmungsschicht als stabile Faehigkeitsebene vor aktiver Regulation,
- die SOL/KAS-Gegenprüfung zeigt dieselbe Vorschlagssprache, aber mit anderer Gewichtung: SOL Stress, SOL Sideways, SOL Expansion und KAS-Zeitebenen tragen deutlich mehr `Abstand bilden`. Damit wirkt die Schicht nicht fix, sondern welt- und assetabhängig,
- die erste Feldtragungsprüfung der Vorschläge zeigt: alle Vorschlagsrichtungen bleiben grundsätzlich feldtragbar, aber mit unterschiedlicher Nähe zu Druckbearbeitung. `ruhig hinhoeren`, `Sehen schaerfen` und `Fokus halten / vertiefen` liegen stärker auf der getragenen Seite; `Abstand bilden`, `leiser / weicher aufnehmen` und `Druck / Feldkontakt entlasten` liegen näher an Entlastung und Druckverarbeitung,
- die MCM-Neuronen, die Episodendistanz, der Beobachtungsdruck, die neurochemische Spiegelung und die interne `dio_*`-Syntax lesen jetzt bevorzugt Rezeptoraufnahme plus MCM-Feldwirkung statt direkter Roh-Sinneswerte. Rohwerte bleiben sichtbar, aber nicht mehr der primäre innere Lernvektor,
- aktuelle Läufe bleiben bewusst ohne ausführende Handlung.

Beispiel aus dem aktuellen Forschungslauf:

```text
Top-Syntax-Überlappung:   1.0
Top-Familien-Überlappung: 1.0
Handlungen:              0 -> 0
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

- Ausführungsregeln,
- Gates,
- Entry-Signale,
- Motorik,
- Strategie,
- Beweise einer universellen [MCM-Topologie](https://github.com/H5Pro2/Mental-Core-Matrix-MCM).

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

Passiver Lauf mit weltrelativer Sinnesaufnahme:

```powershell
python -m mini_dio.run_mini --data data/kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv --sense-mode world_relative
```

Der Modus `world_relative` ist aktuell der passive Standard. `--sense-mode fixed` bleibt nur fuer
Vergleichslaeufe erhalten.

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
- `121_PASSIVE_FELDKLASSEN_DIAGNOSE.md`
- `122_STRESS_GEGENPOL_DIAGNOSE.md`
- `123_NATUERLICHE_MCM_MOEGLICHKEITEN.md`
- `124_FELDZEIT_DIAGNOSE.md`
- `125_FELDZEIT_GEGEN_FELDKLASSEN.md`
- `126_NEUE_WELT_FELDZEIT_KLASSENPRUEFUNG.md`
- `127_NEGATIVE_STRESS_WELT_KLASSENPRUEFUNG.md`
- `128_AUTO_STRESS_FENSTER_KLASSENPRUEFUNG.md`
- `129_AUTO_STRESS_ABSCHNITTSANALYSE.md`
- `130_LOKALE_STRESSINSEL_REPRODUKTION.md`
- `131_LOKALE_RUHEINSEL_GEGEN_STRESSINSEL.md`
- `132_PASSIVE_MCM_POLACHSEN.md`
- `133_KURZSEGMENT_LESER.md`
- `134_ZWEITE_RUHEINSEL_KURZSEGMENT_PRUEFUNG.md`
- `135_ZWEITE_STRESSINSEL_KURZSEGMENT_PRUEFUNG.md`
- `136_KURZSEGMENT_WERTEBEREICHE.md`
- `137_UNABHAENGIGES_JAHR_KURZSEGMENT_PRUEFUNG.md`
- `138_STRESSREGIME_KURZSEGMENT_PRUEFUNG.md`
- `139_SEITWAERTSREGIME_KURZSEGMENT_PRUEFUNG.md`
- `202_WELTLAUTSTAERKE_BTC_SOL_ZEITAUFLOESUNG.md`
- `204_VERDICHTUNGS_SENSITIVITAET_BTC_SOL.md`
- `205_VERDICHTUNGS_SENSITIVITAET_BEFUND.md`
- `206_ORGANISCHE_REIZADAPTATION_DIAGNOSE.md`
- `207_ORGANISCHE_REIZADAPTATION_BEFUND.md`
- `208_DAUERLAST_ZERLEGUNG_DIAGNOSE.md`
- `209_DAUERLAST_ZERLEGUNG_BEFUND.md`
- `210_REKOPPLUNGSQUALITAET_DIAGNOSE.md`
- `211_REKOPPLUNGSQUALITAET_BEFUND.md`
- `212_REKOPPLUNGSROLLEN_MEHRWELT_DIAGNOSE.md`
- `213_REKOPPLUNGSROLLEN_MEHRWELT_BEFUND.md`
- `214_LOKALE_REKOPPLUNGSPOLE_DIAGNOSE.md`
- `215_LOKALE_REKOPPLUNGSPOLE_BEFUND.md`
- `216_LOKALE_WELTMERKMALE_REKOPPLUNG_DIAGNOSE.md`
- `217_LOKALE_WELTMERKMALE_REKOPPLUNG_BEFUND.md`
- `218_FELDHISTORIE_GEGEN_WELTSTRUKTUR_DIAGNOSE.md`
- `219_FELDHISTORIE_GEGEN_WELTSTRUKTUR_BEFUND.md`
- `220_SOL5M_HARMONISCHE_REFERENZ_DIAGNOSE.md`
- `221_SOL5M_HARMONISCHE_REFERENZ_BEFUND.md`
- `222_ORGANISCHER_ADAPTIONSWEG_DIAGNOSE.md`
- `223_ORGANISCHER_ADAPTIONSWEG_BEFUND.md`
- `224_AUDITIVE_REGULATION_DIAGNOSE.md`
- `225_AUDITIVE_REGULATION_BEFUND.md`
- `226_AUDITIVE_FELDKOPPLUNG_DIAGNOSE.md`
- `227_AUDITIVE_FELDKOPPLUNG_BEFUND.md`
- `228_VISUELLE_REGULATION_DIAGNOSE.md`
- `229_VISUELLE_REGULATION_BEFUND.md`
- `230_VISUELLE_FELDKOPPLUNG_DIAGNOSE.md`
- `231_VISUELLE_FELDKOPPLUNG_BEFUND.md`
- `232_MULTISENSORISCHE_KOPPLUNG_DIAGNOSE.md`
- `233_MULTISENSORISCHE_KOPPLUNG_BEFUND.md`
- `234_LOKALE_MULTISENSORISCHE_KOPPLUNG_DIAGNOSE.md`
- `235_LOKALE_MULTISENSORISCHE_KOPPLUNG_BEFUND.md`
- `236_LOKALE_MULTISENSORISCHE_SYNTAX_DIAGNOSE.md`
- `237_LOKALE_MULTISENSORISCHE_SYNTAX_BEFUND.md`
- `238_LOKALE_FELD_EPISODEN_VORSCHAU_BEFUND.md`
- `239_LOKALE_MULTISENSORISCHE_KOPPLUNG_PREVIEW_DIAGNOSE.md`
- `240_LOKALE_FELD_EPISODEN_PREVIEW_SYNTAX_DIAGNOSE.md`
- `241_LOKALE_FELD_EPISODEN_PREVIEW_SYNTAX_BEFUND.md`
- `242_MEHRWELT_LOKALE_MULTISENSORISCHE_KOPPLUNG_PREVIEW_DIAGNOSE.md`
- `243_MEHRWELT_FELD_EPISODEN_PREVIEW_SYNTAX_DIAGNOSE.md`
- `244_MEHRWELT_FELD_EPISODEN_PREVIEW_SYNTAX_BEFUND.md`
- `245_PASSIVE_PREVIEW_REGULATIONSKARTE.md`
- `246_PREVIEW_SYMBOL_02XIKFK_ROLLENKONTRAST.md`
- `247_PREVIEW_KIPPVARIANTEN_GEGEN_REKOPPLUNGSFAMILIE.md`
- `248_FOLGEWELT_LOKALE_MULTISENSORISCHE_KOPPLUNG_PREVIEW_DIAGNOSE.md`
- `249_FOLGEWELT_FELD_EPISODEN_PREVIEW_SYNTAX_DIAGNOSE.md`
- `250_FOLGEWELT_KIPPVARIANTEN_GEGEN_REKOPPLUNGSFAMILIE.md`
- `251_FOLGEWELT_RANDSPANNUNG_BEFUND.md`
- `252_182Y_FOLGEWELTEN_LOKALE_KOPPLUNG_PREVIEW_DIAGNOSE.md`
- `253_182Y_FOLGEWELTEN_PREVIEW_SYNTAX_DIAGNOSE.md`
- `254_182Y_FOLGEWELTEN_KIPPVARIANTEN_KONTRAST.md`
- `255_182Y_FOLGEWELTEN_RANDSPANNUNG_GRUPPENBEFUND.md`
- `256_PASSIVE_SYMBOLGRUPPEN_ROLLENKARTE.md`
- `257_SYMBOLGRUPPEN_NEUE_WELT_LOKALE_KOPPLUNG_PREVIEW_DIAGNOSE.md`
- `258_SYMBOLGRUPPEN_NEUE_WELT_PREVIEW_SYNTAX_DIAGNOSE.md`
- `259_SYMBOLGRUPPEN_NEUE_WELT_ROLLENKARTE.md`
- `260_SYMBOLGRUPPEN_NEUE_WELT_BEFUND.md`
- `261_SYMBOLGRUPPEN_STABILITAETSMATRIX.md`
- `262_WELTUEBERGREIFENDE_INFORMATIONSAUFNAHME_DIAGNOSE.md`
- `263_WELTRELATIVER_WAHRNEHMUNGSADAPTER_VERGLEICH.md`
- `264_WEICHER_WELTRELATIVER_WAHRNEHMUNGSADAPTER_VERGLEICH.md`
- `265_WAHRNEHMUNGSADAPTER_LAUFVERGLEICH.md`
- `266_WELTRELATIVER_MEHRWELT_LAUFBEFUND.md`
- `267_WELTRELATIVER_BRUCHERHALT_DIAGNOSE.md`
- `268_SOL_BTC_5M_1H_WELTRELATIVER_BRUCHERHALT.md`
- `269_WELTRELATIVE_TOPOLOGIE_MATRIX.md`
- `270_AKTUELLER_STAND_WELTRELATIVE_TOPOLOGIE.md`
- `303_REZEPTORISCHE_MCM_TRENNUNG_UMSETZUNG.md`
- `304_REZEPTOR_TOPOLOGIE_MATRIX.md`
- `305_REZEPTOR_SINNESACHSE_MATRIX.csv`
- `306_REZEPTOR_TOPOLOGIE_BEFUND.md`
- `307_REZEPTOR_OEFFNUNG_REKOPPLUNG_MATRIX.csv`
- `307_REZEPTOR_UEBERGANG_AGGREGAT.csv`
- `307_REZEPTOR_UEBERGANG_EVENTS.csv`
- `308_REZEPTOR_OEFFNUNG_REKOPPLUNG_BEFUND.md`
- `309_REZEPTOR_DAUERLAST_TOPOLOGIE_MATRIX.md`
- `310_REZEPTOR_DAUERLAST_SINNESACHSE_MATRIX.csv`
- `311_REZEPTOR_DAUERLAST_BEFUND.md`
- `312_REZEPTOR_KONTAKTINSELN_EVENTS.csv`
- `312_REZEPTOR_KONTAKTINSELN_SUMMARY.csv`
- `313_REZEPTOR_KONTAKTINSELN_BEFUND.md`
- `314_REZEPTOR_KONTAKTINSEL_SYMBOL_FAMILIEN.csv`
- `314_REZEPTOR_KONTAKTINSEL_MCM_PREVIEW_FAMILIEN.csv`
- `314_REZEPTOR_KONTAKTINSEL_FAMILIEN_PAARE.csv`
- `315_REZEPTOR_KONTAKTINSEL_FAMILIEN_BEFUND.md`
- `316_REZEPTORSCHICHT_ALS_MCM_SCHUTZGRENZE.md`
- `317_REZEPTOR_EPISODENFAMILIEN_REPRO_EVENTS.csv`
- `317_REZEPTOR_EPISODENFAMILIEN_REPRO_MATRIX.csv`
- `318_REZEPTOR_EPISODENFAMILIEN_REPRO_BEFUND.md`
- `319_TAKTILE_REZEPTOR_SIMULATION_UND_GETRENNTE_SINNESWAHRNEHMUNG.md`
- `320_MCM_FELDWIRKUNG_ALIAS_UMSETZUNG.md`
- `321_WELTRELATIVER_STANDARD_UND_SYSTEMABGLEICH.md`
- `322_WELTRELATIVER_STANDARD_TOPOLOGIE_PRUEFUNG.md`
- `323_TOPOLOGIE_BEDINGUNGSWELTEN_PRUEFUNG.md`
- `324_GLEICH_LANGE_RUHE_STRESS_TOPOLOGIE_PRUEFUNG.md`
- `325_RUHE_STRESS_WELTMERKMALE_REKOPPLUNG_DIAGNOSE.md`
- `326_EPISODENROLLEN_WELTMERKMALE_DIAGNOSE.md`
- `327_OFFENE_VARIANTE_FAMILIEN_DIAGNOSE.md`
- `328_OFFENE_PREVIEW_FAMILIE_WELTEN_VERGLEICH.md`
- `329_ASSET_PREVIEW_FAMILIEN_PROFIL.md`
- `330_REGULATIONSACHSEN_WAHRNEHMUNGSSCHICHT.md`
- `331_PREVIEW_FAMILIEN_REGULATIONSACHSEN_PROFIL.md`
- `332_PREVIEW_FAMILIEN_NACHBARSCHAFT_DIAGNOSE.md`
- `333_PREVIEW_FAMILIEN_BOUNDARY_DIAGNOSE.md`
- `334_PREVIEW_UEBERGANGSPAARE_DIAGNOSE.md`
- `335_PREVIEW_UEBERGANGSPAARE_KLASSIFIKATION.md`
- `336_BEWEGUNGSARTEN_VALIDIERUNG.md`
- `337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE.md`
- `338_KONTAKTMILIEU_WIEDERKEHR_DRIFT.md`
- `339_LANGWELT_STABILES_MILIEU_SEGMENTE.md`
- `340_LANGWELT_KONTAKTMILIEU_WIEDERKEHR.md`
- `341_MILIEU_DRIFTQUALITAET.md`
- `342_MILIEU_DRIFT_WELTMERKMALE.md`
- `343_PASSIVE_REGULATIONSWAHRNEHMUNG.md`
- `344_PASSIVE_REGULATIONSQUALITAET_REPRODUKTION.md`
- `345_ASSET_ZEIT_REGULATIONSQUALITAET_SEGMENTE.md`
- `346_ASSET_ZEIT_KONTAKTMILIEU_WIEDERKEHR.md`
- `347_ASSET_ZEIT_MILIEU_DRIFTQUALITAET.md`
- `348_ASSET_ZEIT_MILIEU_WELTMERKMALE.md`
- `349_ASSET_ZEIT_PASSIVE_REGULATIONSQUALITAET.md`
- `350_LONG_ASSET_REGULATIONSQUALITAET_SEGMENTE.md`
- `351_LONG_ASSET_KONTAKTMILIEU_WIEDERKEHR.md`
- `352_LONG_ASSET_MILIEU_DRIFTQUALITAET.md`
- `353_LONG_ASSET_MILIEU_WELTMERKMALE.md`
- `354_LONG_ASSET_PASSIVE_REGULATIONSQUALITAET.md`
- `355_LONG_ASSET_REPRO_REGULATIONSQUALITAET_SEGMENTE.md`
- `356_LONG_ASSET_REPRO_KONTAKTMILIEU_WIEDERKEHR.md`
- `357_LONG_ASSET_REPRO_MILIEU_DRIFTQUALITAET.md`
- `358_LONG_ASSET_REPRO_MILIEU_WELTMERKMALE.md`
- `359_LONG_ASSET_REPRO_PASSIVE_REGULATIONSQUALITAET.md`
- `360_LONG_ASSET_2025_REGULATIONSQUALITAET_SEGMENTE.md`
- `361_LONG_ASSET_2025_KONTAKTMILIEU_WIEDERKEHR.md`
- `362_LONG_ASSET_2025_MILIEU_DRIFTQUALITAET.md`
- `363_LONG_ASSET_2025_MILIEU_WELTMERKMALE.md`
- `364_LONG_ASSET_2025_PASSIVE_REGULATIONSQUALITAET.md`
- `365_LONG_ASSET_2025_15M_REGULATIONSQUALITAET_SEGMENTE.md`
- `366_LONG_ASSET_2025_15M_KONTAKTMILIEU_WIEDERKEHR.md`
- `367_LONG_ASSET_2025_15M_MILIEU_DRIFTQUALITAET.md`
- `368_LONG_ASSET_2025_15M_MILIEU_WELTMERKMALE.md`
- `369_LONG_ASSET_2025_15M_PASSIVE_REGULATIONSQUALITAET.md`
- `370_LONG_ASSET_2025_5M_REGULATIONSQUALITAET_SEGMENTE.md`
- `371_LONG_ASSET_2025_5M_KONTAKTMILIEU_WIEDERKEHR.md`
- `372_LONG_ASSET_2025_5M_MILIEU_DRIFTQUALITAET.md`
- `373_LONG_ASSET_2025_5M_MILIEU_WELTMERKMALE.md`
- `374_LONG_ASSET_2025_5M_PASSIVE_REGULATIONSQUALITAET.md`
- `375_ZEITAUFLOESUNGS_MATRIX_GERICHTETE_FELDBEWEGUNG.md`
- `386_JAHRES_ZEITAUFLOESUNGS_MATRIX_GERICHTETE_FELDBEWEGUNG.md`
- `391_KAS_ASSET_GEGENPROBE_PASSIVE_REGULATIONSQUALITAET.md`
- `392_REGULATORISCHE_ABLEITUNG_AUS_DEN_BEFUNDEN.md`
- `393_MCM_FELDBEWEGUNGS_MEMORY_TECHNISCHE_SKIZZE.md`
- `394_MCM_FELDBEWEGUNGS_MEMORY_SUMMARY.md`
- `395_MCM_FELDBEWEGUNGS_MEMORY_MEHRWELT_SUMMARY.md`
- `396_MCM_FELDBEWEGUNG_LATE_SHIFT_2023_PASSIVE_FELDWIRKUNG.md`
- `397_MCM_FELDBEWEGUNGS_MEMORY_UNABHAENGIGE_WELT_SUMMARY.md`
- `398_REZEPTORISCH_REGULATORISCHE_WAHRNEHMUNGSSCHICHT.md`
- `399_STRIKTE_TRENNUNG_MCM_FELD_UND_WAHRNEHMUNGSREGULATION.md`
- `400_SINNESGETRENNTE_ANPASSUNGSFAEHIGKEIT.md`
- `401_SINNESGETRENNTE_ACHSPRUEFUNG.md`
- `402_LOKALE_SINNESACHSEN_EPISODENKARTE.md`
- `403_SINNESACHSEN_REKOPPLUNGSQUALITAET.md`
- `404_SINNESACHSEN_EPISODENKARTE_GEGENPROBE.md`
- `405_SINNESACHSEN_REKOPPLUNGSQUALITAET_GEGENPROBE.md`
- `406_HOEREN_HIN_REKOPPLUNGSFAEHIGKEIT.md`
- `407_SINNESAUFNAHME_FAEHIGKEITSVERGLEICH.md`
- `408_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `409_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `410_BTC2024_5M_QUIET_SINNESACHSEN_EPISODENKARTE.md`
- `411_BTC2024_5M_QUIET_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `412_BTC2024_5M_QUIET_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `413_BTC2024_5M_QUIET_INTAKE_MEMORY_ABGLEICH.md`
- `414_SOL2023_NEGATIVE_STRESS_10K_SINNESACHSEN_EPISODENKARTE.md`
- `415_SOL2023_NEGATIVE_STRESS_10K_SINNESACHSEN_REKOPPLUNG.md`
- `416_SOL2023_NEGATIVE_STRESS_10K_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `417_SOL2023_NEGATIVE_STRESS_10K_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `418_SOL2023_NEGATIVE_STRESS_10K_INTAKE_MEMORY_ABGLEICH.md`
- `419_SOL2026_SIDEWAYS_10K_SINNESACHSEN_EPISODENKARTE.md`
- `420_SOL2026_SIDEWAYS_10K_SINNESACHSEN_REKOPPLUNG.md`
- `421_SOL2026_SIDEWAYS_10K_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `422_SOL2026_SIDEWAYS_10K_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `423_SOL2026_SIDEWAYS_10K_INTAKE_MEMORY_ABGLEICH.md`
- `424_INTAKE_MEMORY_GEGENWELTEN_VERGLEICH.md`
- `425_SOL2023_POSITIVE_EXPANSION_10K_SINNESACHSEN_EPISODENKARTE.md`
- `426_SOL2023_POSITIVE_EXPANSION_10K_SINNESACHSEN_REKOPPLUNG.md`
- `427_SOL2023_POSITIVE_EXPANSION_10K_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `428_SOL2023_POSITIVE_EXPANSION_10K_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `429_SOL2023_POSITIVE_EXPANSION_10K_INTAKE_MEMORY_ABGLEICH.md`
- `430_BTC2024_5M_2K_SINNESACHSEN_EPISODENKARTE.md`
- `431_BTC2024_5M_2K_SINNESACHSEN_REKOPPLUNG.md`
- `432_BTC2024_5M_2K_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `433_BTC2024_5M_2K_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `434_BTC2024_5M_2K_INTAKE_MEMORY_ABGLEICH.md`
- `435_BTC2024_5M_QUIET_4K_LONG_SINNESACHSEN_EPISODENKARTE.md`
- `436_BTC2024_5M_QUIET_4K_LONG_SINNESACHSEN_REKOPPLUNG.md`
- `437_BTC2024_5M_QUIET_4K_LONG_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `438_BTC2024_5M_QUIET_4K_LONG_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `439_BTC2024_5M_QUIET_4K_LONG_INTAKE_MEMORY_ABGLEICH.md`
- `440_BTC2024_5M_STRESS_4K_SINNESACHSEN_EPISODENKARTE.md`
- `441_BTC2024_5M_STRESS_4K_SINNESACHSEN_REKOPPLUNG.md`
- `442_BTC2024_5M_STRESS_4K_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `443_BTC2024_5M_STRESS_4K_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `444_BTC2024_5M_STRESS_4K_INTAKE_MEMORY_ABGLEICH.md`
- `445_BTC2024_1H_STRESS_4K_SINNESACHSEN_EPISODENKARTE.md`
- `446_BTC2024_1H_STRESS_4K_SINNESACHSEN_REKOPPLUNG.md`
- `447_BTC2024_1H_STRESS_4K_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `448_BTC2024_1H_STRESS_4K_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `449_BTC2024_1H_STRESS_4K_INTAKE_MEMORY_ABGLEICH.md`
- `450_BTC2024_5M_VS_1H_STRESS_INTAKE_MEMORY_ABGLEICH.md`
- `451_BTC2024_1H_QUIET_4K_SINNESACHSEN_EPISODENKARTE.md`
- `452_BTC2024_1H_QUIET_4K_SINNESACHSEN_REKOPPLUNG.md`
- `453_BTC2024_1H_QUIET_4K_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `454_BTC2024_1H_QUIET_4K_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `455_BTC2024_1H_QUIET_4K_INTAKE_MEMORY_ABGLEICH.md`
- `456_BTC2024_1H_QUIET_VS_STRESS_INTAKE_MEMORY_ABGLEICH.md`
- `457_BTC2024_5M_QUIET_VS_STRESS_INTAKE_MEMORY_ABGLEICH.md`
- `458_BTC_TIMEFRAME_STRESS_SYNTHESE.md`
- `459_PASSIVE_REGULATIONSVORSCHLAG_BASIS.md`
- `460_BTC2024_5M_QUIET_REGULATIONSVORSCHLAG.md`
- `461_BTC2024_5M_STRESS_REGULATIONSVORSCHLAG.md`
- `462_BTC2024_1H_QUIET_REGULATIONSVORSCHLAG.md`
- `463_BTC2024_1H_STRESS_REGULATIONSVORSCHLAG.md`
- `464_PASSIVE_REGULATIONSVORSCHLAG_MEHRWELT_SYNTHESE.md`
- `465_SOL2023_NEGATIVE_STRESS_10K_REGULATIONSVORSCHLAG.md`
- `466_SOL2026_SIDEWAYS_10K_REGULATIONSVORSCHLAG.md`
- `467_SOL2023_POSITIVE_EXPANSION_10K_REGULATIONSVORSCHLAG.md`
- `468_KAS2024_ZEITEBENEN_SINNESACHSEN_EPISODENKARTE.md`
- `469_KAS2024_ZEITEBENEN_SINNESAUFNAHME_WIEDERERKENNUNG.md`
- `470_KAS2024_ZEITEBENEN_PASSIVE_SINNESAUFNAHME_MEMORY.md`
- `471_KAS2024_ZEITEBENEN_REGULATIONSVORSCHLAG.md`
- `472_SOL_KAS_REGULATIONSVORSCHLAG_SYNTHESE.md`
- `473_PASSIVE_REGULATIONSVORSCHLAG_FELDTRAGUNG.md`
- `AKTUELLER_FORSCHUNGSLAUF.md`
- `AKTUELLER_FORSCHUNGSLAUF_2024_01.md`
- `MEHRWELT_VERGLEICH.md`

Der stärkste aktuelle Befund ist die passive [MCM-Zykluskarte](https://github.com/H5Pro2/Mental-Core-Matrix-MCM):

- Zentrum kann halten.
- Brücken können Zentrum tragen.
- Drift kann zum Zentrum zurückführen.
- Übergang kann rekoppeln.
- Drift und Übergang können über Zentrum in Brückenzustände übergehen.

Wichtiger Topologie-Hinweis:

Die bisher beobachtete Topologie wurde nicht als Zielbild in MINI_DIO eingebaut. Der Code enthält im Kern keine feste Vorgabe für vier Felder, Zentrum, Brücken, Ring, Rand oder eine bestimmte geometrische Ordnung. Solche Begriffe werden in Reports und Befunden verwendet, um die entstandenen Feldrollen nachträglich lesbar zu machen. Der derzeitige Befund ist deshalb besonders interessant: In den geprüften Welten bildet MINI_DIO selbstständig eine Ordnung, die der hypothetischen MCM-Arbeit entspricht. Das ist noch kein universeller Beweis, aber ein reproduzierbarer Forschungsbefund innerhalb der bisherigen Testwelten und Memory-Neustarts.

Der aktuelle Mehrwelt-Vergleich zeigt zusätzlich:

- Innerhalb einzelner Welten reproduzieren sich Top-Syntax und Top-Familien stabil.
- Zwischen verschiedenen Welten verschieben sich Syntax und Familien deutlich.
- Das passive Feldprofil bleibt dennoch ähnlich.
- Die dominante Feldwirkung kann je nach Weltspannung wechseln, ohne dass die Feldordnung kollabiert.
- Aus mehreren Welten lassen sich vorläufige passive Feldklassen lesen: ruhige Nähegruppe, angespannte Übergangsgruppe und Stress-Gegenpol.
- Der Stress-Gegenpol entsteht bisher nicht durch ein einzelnes Rohweltmerkmal, sondern durch die Kopplung aus Weltunruhe, Kipp-/Spannungswirkung, Rekopplungsverlust und höherem Episodenmemory.
- Weltlautstärke, Verdichtungs-Sensitivität und organische Reizadaptation werden getrennt gelesen: Ein Reiz kann aufmerksamkeitsnah sein, ohne langfristig feldlastnah zu werden; umgekehrt kann Dauerlast feldseitig wirken, obwohl sie nicht als akuter Einzelreiz maximal auffällt.
- Die organische Reizadaptation ist aktuell Diagnose, keine Kernregel: Habituation, Sensitivierung, Aufmerksamkeit und allostatische Tragfähigkeit werden passiv gemessen, nicht als Handlung genutzt.
- Die Dauerlast-Zerlegung zeigt bisher: SOL 30m/1h wird vor allem durch Feldlast, Memorylast und Rekopplungsverlust schwer, während BTC 5m zwar aufmerksamkeitsnah ist, aber feldseitig gut getragen bleibt.
- Die Rekopplungsdiagnose liest daraus passive Rollen: `reiz_aktiv_rekoppelnd`, `nachhall_rekoppelnd`, `uebergang_bindend` und `last_memory_bindend`.
- Der Mehrwelt-Test zeigt: Viele gemischte Welten bleiben aktiv-rekoppelnd; lokale Stresssegmente koennen dagegen klar last-/memorybindend werden.
- Lokale Rekopplungspole sind sichtbar: Ruhe-/Entlastungssegmente wurden bisher aktiv-rekoppelnd gelesen, lokale Stresssegmente liegen deutlich naeher an Uebergang oder Last-/Memorybindung.
- Lokale Bindung folgt bisher eher Rohweltverdichtung, Range, Feldlast und Memorylast als einem einfachen Richtungswechsel.
- Aehnliche Rohweltverdichtung erzeugt nicht zwingend dieselbe Rekopplungsrolle: Feldlast, Memorylast und Rekopplungsverlust wirken als angenaeherte Feldhistorie mit.
- Der Vergleich `STRESS_2023_TEST4` gegen `STRESS_2024_REAL` ist der bisher scharfste Hinweis: fast gleiche Weltverdichtung, aber Wechsel von `last_memory_bindend` zu `uebergang_bindend`.
- SOL 5m wirkt in den bisherigen Diagnosen harmonischer, weil es nicht reizarm ist, sondern gut rekoppelbar bleibt: genug Aktivierung fuer Bedeutung, aber deutlich weniger Feldlast, Memorylast und Ueberbindung als SOL 30m/1h oder lokale Stresssegmente.
- Daraus folgt keine Bevorzugungsregel fuer 5m. SOL 5m dient als passives Referenzprofil fuer tragfaehige Weltwirkung.
- Organische Anpassungsfaehigkeit zeigt sich nicht als ein Limiter, sondern als mehrere passive Adaptionsachsen: Feldabstand bilden, Memory leichter tragen, Rekopplung vertiefen, Dauerlast abbauen, Nachhall loesbar machen und Reizbasis neu einpendeln.
- SOL 1h braucht in der aktuellen Diagnose vor allem Feldabstand und leichtere Memory-/Dauerlast-Kopplung; Stresssegmente zeigen je nach Weltwirkung andere Anpassungsachsen.
- Die auditive Achse liest Marktenergie als Hoerregulation: Hinhoeren, Rauschen filtern, Reiz abklingen lassen, genauer Anhoeren, Alarm, Hintergrund und Beruhigung. Diese Zustaende wirken nicht direkt als Bedeutung, sondern muessen mit MCM-Feldwirkung und Rekopplung zusammen gelesen werden.
- SOL 5m zeigt bisher eine tragfaehige Hoermischung: aktiv genug fuer Hinhoeren/genaueres Anhoeren, aber mit niedriger Feld- und Memorylast.
- Die auditive Feldkopplung zeigt: Hoerfilterung reicht allein nicht. Entscheidend ist, ob die gehoerte Tonspur leicht rekoppelt oder als Feld-/Memorylast bindet.
- SOL 1h wird auditiv naeher an Feldlast gelesen (`hoerlast_feldnah`), waehrend SOL 5m trotz aktiver Hoeranteile niedrige Feldbindung zeigt.
- Die visuelle Achse liest Formfluss, Formstabilitaet, Formwechsel und visuellen Feldabstand als eigene Sinnesregulation: Hintergrund halten, Rauschen filtern, stabile Form tragen, Alarmform erkennen oder genauer ansehen.
- Die BTC-5m-Stress-Gegenprobe zeigt: andere Weltspannung erzeugt nicht automatisch neue Rohspuren. Von 7 verdichteten Intake-Spuren treffen 6 bekannte Basis-Keys wieder, 4 behalten dieselbe Qualitaet. Das stuetzt die These stabiler Aufnahmefamilien unter veraenderter Spannung.
- Die BTC-1h-Stress-Gegenprobe zeigt: andere Zeitskala erhaelt die Keys, oeffnet aber die Qualitaet. Von 7 verdichteten Intake-Spuren treffen 7 bekannte Basis-Keys wieder, aber nur 2 behalten dieselbe Qualitaet. Damit wirkt Timeframe-Spannung eher als Reife-/Tragqualitaetsverschiebung, nicht als kompletter Bedeutungsbruch.
- Der direkte BTC-5m-gegen-1h-Stressvergleich zeigt: Nur 3 von 7 Keys werden direkt geteilt, aber diese 3 bleiben vollstaendig qualitaetsgleich. Timeframe verschiebt also Teile der Aufnahmefamilie, waehrend ein stabiler Kern erhalten bleibt.
- Der direkte BTC-1h-Quiet-gegen-1h-Stressvergleich zeigt maximale Naehe: 7 von 7 Keys und 7 von 7 Qualitaeten bleiben gleich. Die bisherige Verschiebung liegt damit eher im Wechsel der Zeitskala als in der ruhigen oder stressigen 1h-Weltspannung.
- Der direkte BTC-5m-Quiet-gegen-5m-Stressvergleich zeigt dagegen nur 3 von 7 gemeinsame Keys, aber diese 3 bleiben qualitaetsgleich. Ueber alle BTC-Direktvergleiche erscheint damit ein stabiler Kern aus `hoeren_hin`, `sehen_abstand` und `fuehlen_abstand`, waehrend die restliche Aufnahmeoberflaeche je nach Timeframe und Weltspannung variiert.
- Die visuelle Feldkopplung zeigt: Form ist nicht automatisch Feldlast. SOL 5m bleibt bisher `offene_sehkopplung` mit niedriger Feldbindung, waehrend SOL 1h und mehrere Stresssegmente naeher an `sehlast_feldnah` liegen.
- Daraus entsteht die naechste Pruefebene: Hoeren, Sehen und Fuehlen muessen multisensorisch zusammen gelesen werden, ohne dass eine Sinnesachse allein Handlung oder Bedeutung erzwingt.
- Die multisensorische Kopplung zeigt bisher vor allem `offene_multisensorik` und `rekoppelnde_sinnesnaehe`. SOL 5m bleibt mit niedriger Ueberlast offen getragen, SOL 30m zeigt eher rekoppelnde Naehe, SOL 1h liegt naeher an Last, aber noch ohne klaren Kollaps.
- Daraus folgt als naechste Hierarchie: erst gemeinsame Sinnesinnenlage pruefen, dann lokale Kippzonen innerhalb einzelner Welten suchen.
- Die lokale multisensorische Kopplung zeigt: Gesamtweltrollen sind zu grob. SOL 5m besitzt starke lokale Rekopplungsfenster, waehrend SOL 1h/30m staerkere lokale Kippfenster zeigen. Entscheidend ist dabei nicht die reine Anzahl der Fenster, sondern Staerke, Ort und Reproduktion gleicher Tickbereiche ueber Lauf 1 und Lauf 2.
- Die lokale Syntaxpruefung zeigt: lokale Kipp- und Rekopplungsfenster tragen bereits wiederkehrende `symbol_family`-Muster. Die tiefere `mcm_field_episode_symbol`-Spur bleibt dort aber noch weitgehend leer. Das spricht fuer lokale Wahrnehmungsfamilien, aber noch nicht fuer voll gereifte lokale Feld-Episoden.
- Die Ursache der leeren lokalen Feld-Episodenspur ist geklaert: `mcm_field_episode_symbol` wurde bisher nur beim Abschluss einer Episode geschrieben. MINI_DIO gibt nun zusaetzlich eine passive `mcm_field_episode_preview_symbol`-Spur pro Tick aus, damit lokale entstehende Feld-Episoden sichtbar werden, ohne Memory zu schreiben oder Handlung zu beeinflussen.
- Frische Preview-Laeufe zeigen jetzt: lokale Rekopplungsfenster tragen reproduzierbar starke `dio_mcm_episode_*`-Vorschau-Familien, besonders `dio_mcm_episode_02xikfk`. Lokale Kippfenster tragen andere Vorschau-Feldsymbole, etwa `dio_mcm_episode_037i64j`, mit unruhigerer Innenfeldwirkung. Das ist ein Hinweis auf entstehende lokale Feld-Episoden-Syntax, noch kein Beweis fuer gereifte lokale Bedeutungsinseln.
- Der fruehere Mehrwelt-Preview-Vergleich zeigte `dio_mcm_episode_02xikfk` als lokale Rekopplungsnaehe-Sprache. Die spaetere 12-Welten-Pruefung erweitert diesen Befund: `dio_mcm_episode_1t5bcxp` ist keine rein weltbezogene Einzelvariante mehr, sondern eine breit wiederkehrende MCM-Preview-Familie mit stark variabler Rohsyntax darunter. Daraus folgt vorlaeufig: MINI_DIO bildet nicht nur Einzelzeichen, sondern Feldsprache mit verdichteter Bedeutungsebene und lokaler Oberflaechenvarianz.
- Die passive Regulationskarte zeigt: dieselbe Vorschau-Feldlage kann je nach Rolle anders wirken. `dio_mcm_episode_02xikfk` ist in `lokal_rekoppelnd` stabil und entlastend, in `lokale_multisensorische_kippnaehe` dagegen tragend-unruhiger. Regulation wird damit als Kopplung gelesen: Feldsymbol plus lokale Rolle plus Innenfeldwirkung.
- Die seltenen Kippvarianten `dio_mcm_episode_037i64j`, `dio_mcm_episode_0e9ekzq`, `dio_mcm_episode_0eje6op` und `dio_mcm_episode_182yyt2` zeigen gegenueber der Rekopplungsfamilie mehr Kippnaehe, mehr Felddruck und weniger Entlastung. Bisher sind sie eine reproduzierte Rand-/Spannungsgruppe innerhalb `PREVIEW_REAL_2023`, aber noch keine mehrweltstabile Familie.
- Eine weitere Realwelt stuetzt erstmals `dio_mcm_episode_182yyt2` als wiederkehrendes Randspannungszeichen. Damit ist Anspannung nicht geloest, aber klarer differenziert: allgemeine Rekopplung bleibt haeufig und stabil, Randspannung bleibt seltener, kippnaeher und unruhiger, kann aber wiederkehren.
- Isolierte Stresssegmente können lokal denselben Stress-Gegenpol bilden, auch wenn Wiederkehr und Nachhall erst in längerer Einbettung sichtbar werden.
- Lokale Kurzsegmente müssen vorsichtig gelesen werden: bei ihnen sind Memorylast, Strain und Rekopplung belastbarer als ein globaler Feldklassenname.
- Passive Gegenpole wie Stress/Entlastung, Unruhe/Ruhe, Drift/Rekopplung oder Zerfall/Verdichtung werden nicht als Module modelliert, sondern als Polachsen der [MCM-Feldreaktion](https://github.com/H5Pro2/Mental-Core-Matrix-MCM) gelesen.
- Der Kurzsegment-Leser trennt lokale Lastnähe, Ruhenähe und Feldzeitnähe relativ zueinander; Feldzeitnähe ist dabei nicht automatisch Ruhe.
- Zwei lokale Ruheinseln aus unterschiedlichen ruhigen Welten werden `ruhig_feldzeitnah` gelesen: niedrige Memorylast, niedriger Strain, stärkere Rekopplung und trotzdem leichte Feldzeitspur.
- Eine zweite lokale Stressinsel aus einer anderen Stresswelt wird ebenfalls `lastnah` gelesen: hohe Memorylast, hoher Strain und schwächere Rekopplung.
- Die bisherigen Kurzsegment-Wertebereiche trennen `lastnah`, `ruhig_feldzeitnah` und `last_feldzeitnah` als Arbeitsformen; sie sind Diagnosebefunde, keine Schwellwerte.
- Ein unabhängiges 2024-Jahr bestätigt die Trennung: das automatisch extrahierte Stressfenster wird `last_feldzeitnah`, das automatisch extrahierte Ruhefenster ruhenah gelesen.
- Eine stressartige 2025-Welt enthält lokal beides: ein automatisch extrahiertes Stressfenster wird `lastnah`, ein Ruhefenster aus derselben Welt wird `ruhenah` gelesen.
- Eine moderate Seitwärtswelt erzeugt keine neue Lastklasse: aktiveres und ruhiges Seitwärtsfenster werden beide `ruhig_feldzeitnah` gelesen.

Das spricht für weltbezogene Innenfeldordnungen statt wahlloser Speicherung.

Die Feldklassen-Diagnose ist ausdrücklich ein Auswertungswerkzeug. Sie ist keine Runtime-Regel, kein Gate und keine Handlungsvorgabe für MINI_DIO.

Die nächsten Diagnosen sollen entlang der natürlichen [MCM-Möglichkeiten](https://github.com/H5Pro2/Mental-Core-Matrix-MCM) eingeordnet werden: Feldtopologie, Feldzeit, Bedeutungsverdichtung, Rekopplung, Lastwahrnehmung und getrennte Sinnesachsen.

## Was MINI_DIO Nicht Ist

MINI_DIO ist aktuell kein Ausführungssystem.

Es ist kein fertiges KI-System, kein autonomer Agent und kein Beweis für Bewusstsein. Es ist ein kontrollierter Forschungsaufbau, um zu untersuchen, ob ein kleines MCM-Feld reproduzierbare innere Bedeutungsräume aus Weltkontakt bilden kann.

Diese Vorsicht ist wichtig, weil der interessante Teil gerade darin liegt, nichts vorschnell als Handlung, Strategie oder Intelligenz zu verkaufen.

