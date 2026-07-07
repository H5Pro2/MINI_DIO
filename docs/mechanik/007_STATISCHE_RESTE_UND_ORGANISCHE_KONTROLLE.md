# 007 - Statische Reste und organische Kontrolle

Stand: 2026-07-08

## Zweck

Diese Datei trennt statische Elemente im MINI_DIO-System nach ihrer Funktion.

Ziel ist nicht, jede Zahl aus dem Projekt zu entfernen.
Ziel ist, dass keine feste Zahl die Feldbedeutung oder Wahrnehmungsregulation als harte Regel bestimmt.

## Grundregel

```text
Diagnose darf klassifizieren.
Das MCM-Feld darf nicht durch starre Klassen gesteuert werden.
```

Damit gilt:

```text
Auswertungstools:
  duerfen Schwellen nutzen, um Befunde lesbar zu machen.

Runtime/Feldmechanik:
  soll ueber weiche Druckvergleiche, Erfahrung, Wiederkehr und Feldwirkung laufen.
```

## Erste Bereinigung

Zwei Runtime-Bereiche wurden von festen Grenzwerten auf dominante Druckvergleiche umgestellt.

### Adaptive Rekopplung

Vorher:

```text
experience < 0.20        -> adaptive_jung
delta > 0.025            -> adaptive_rekopplung_angehoben
delta < -0.025           -> adaptive_rekopplung_gedaempft
role_experience >= 0.55  -> milieu_rollennah
path_experience >= 0.35  -> milieu_pfadnah
```

Jetzt:

```text
adaptive_jung
adaptive_rekopplung_angehoben
adaptive_rekopplung_gedaempft
adaptive_rekopplung_nahe_statisch

entstehen aus konkurrierenden Druckanteilen.
Die staerkste Feldtendenz benennt den Zustand.
```

### Rezeptorische Achsenpraeferenz

Vorher:

```text
wenn ueberlastet:
  Hoeren runter
  Fuehlen runter

wenn zu duenn:
  Hoeren hoch
  Fuehlen hoch
```

Jetzt:

```text
Hoeren:
  up / down / soften / hold konkurrieren als Druckanteile

Sehen:
  up / down / soften / hold konkurrieren als Druckanteile

Fuehlen:
  up / down / soften / hold konkurrieren als Druckanteile
```

Die jeweilige Achse wird nicht mehr durch eine harte Bedingung gesetzt.
Die dominante innere Tendenz bestimmt die passive Praeferenz.

## Zweite Bereinigung

Zwei weitere Benennungsbereiche wurden von festen Grenzwert-Kaskaden auf Druckmodelle umgestellt.

### MCM-Wirkungskarte

Vorher:

```text
field_strained -> gespannt
rekopplung >= X und strain <= Y -> stabil / tragend_unruhig
bestimmter Uebergang -> rekoppelnd / kippend
```

Jetzt:

```text
rekoppelnd
kippend
gespannt
stabil
tragend_unruhig
diffus

entstehen als konkurrierende Feldwirkungsdruecke.
Die staerkste passive Wirkung benennt die aktuelle MCM-Lage.
```

### Weltlage

Vorher:

```text
zentrum >= X
rand >= Y
raw_field <= Z
auditory >= A
visual < B
```

Jetzt:

```text
ueberstabil_mit_randreiz
ueberstabil_leise_scharf
ueberstabil_visuell_weicher
randlastige_sinneslage
ruhig_zentrumsnah
leise_scharf_duenn
lauter_feldkontakt
offen_suchend
normale_weltspannung

entstehen als relative Weltlage-Profile.
Eine Weltlage wird nicht durch einen einzelnen festen Grenzwert entschieden,
sondern durch die staerkste Kombination aus Zentrum, Rand, Rekopplung,
Strain, Hoeren, Sehen und Rohfeld.
```

## Dritte Bereinigung

Fragmentierung und Rollenreifung wurden ebenfalls von festen Schwellenketten getrennt.

### Fragmentierung

Vorher:

```text
junge_spur >= X
offene_oberflaeche >= Y
randspannung >= Z
```

Jetzt:

```text
fragmentierung_offen_randnah_jung
fragmentierung_jung_mit_schwachem_zentrum
fragmentierung_randlastig
fragmentierung_offene_oberflaeche
fragmentierung_mit_rekopplungsresten
fragmentierung_jung
fragmentierung_gemischt

entstehen aus konkurrierenden Oberflaechendruecken.
Die Fragmentierung wird als relative Lage gelesen, nicht als Grenzwert-Sprung.
```

### Rollenreifung

Vorher:

```text
segments >= X
worlds >= Y
duration >= Z
exit_strain > A
exit_loud > B
```

Jetzt:

```text
Segmentqualitaet:
  lange_mehrweltphase
  mehrwelt_segmentbruecke
  kurze_mehrweltspur
  kurze_einzelspur

Feldqualitaet:
  feld_rekoppelnd_schaerfend
  feld_jung_instabiler_austritt
  feld_belastete_kernnaehe
  feld_leicht_stabilisierend
  feld_austritt_belastet
  feld_gemischt

entstehen aus weichen Evidenzdruecken.
```

## Vierte Bereinigung

Die Sinnesaufnahme wurde ebenfalls von festen Klassifikationsgrenzen getrennt.

### Marktmelodie

Vorher:

```text
relative_energy >= X -> spannungston
roughness >= Y       -> bruchton
direction > Z        -> aufhellungston
direction < Z        -> abdunklungston
```

Jetzt:

```text
bruchton
spannungston
ruheton
aufhellungston
abdunklungston
trageton

entstehen aus konkurrierenden Ton- und Energiedruecken.
Hoeren liest damit relative Klangwirkung statt feste Lautheitsgrenzen.
```

### Rezeptor-Adaptation

Vorher:

```text
delta_rand < X
delta_strain < Y
delta_zentrum > Z
delta_rekopplung > A
```

Jetzt:

```text
verschiebend
beruhigend
stabil_leicht
neutral

entstehen aus Adaptionsdruecken:
Verschiebung, Beruhigung, Stabilitaet und Neutralitaet konkurrieren.
```

### Sinnesaufnahme-Gedaechtnis

Vorher:

```text
world_count >= X
total_events >= Y
avg_balance >= Z
avg_strain >= A
```

Jetzt:

```text
reproduced_quiet_intake
recurrently_carried_intake
contact_loaded_intake
strained_intake
drifting_intake
open_recurrent_intake
young_intake_trace

entstehen aus Gedächtnis-, Welt-, Balance-, Drift- und Felddruck.
```

## Fuenfte Bereinigung

Die Feldbewegungs-Memory wurde von harten Vorzeichen- und Zaehlwertketten geloest.

### Feldbewegung

Vorher:

```text
rekopplung_delta > 0 und pressure_delta < 0 -> rekoppelnd_entlastend
rekopplung_delta < 0 und pressure_delta > 0 -> oeffnend_belastend
seen_count > 1 oder total_events > 1       -> recurrent
dominant_count == seen_count               -> consistent
```

Jetzt:

```text
rekoppelnd_entlastend
oeffnend_belastend
rekoppelnd
spannungsnah
bewegung_offen

entstehen aus Bewegungsdruecken:
Rekopplung, Druck, Entlastung, Spannung, Lautheit und Schaerfebewegung
wirken relativ zusammen.
```

Auch die Speicherqualitaet wurde umgestellt:

```text
young
recurrently_reconnecting
recurrently_opening_strain
mixed_unstable
recurrently_carried
recurrently_fragmented
open_drifting
asset_sensitive
timeframe_sensitive
world_specific

entstehen aus Exposition, Dominanz, Varianz, Assetnaehe und Zeitrahmennaehe.
```

## Sechste Bereinigung

Feldphase, Rollenbewegung, Feldzeit und Offline-Reorganisation wurden von festen Reife- und Naehefenstern getrennt.

### Feldphase

Vorher:

```text
seen_count <= 1       -> young_phase_trace
world_count > 1
seen_count >= 3       -> cross_world_phase_family
```

Jetzt:

```text
young_phase_trace
cross_world_phase_family
cross_world_open_phase
recurrent_world_phase
local_phase_trace

entstehen aus Seen-Druck, Weltdruck, Dauer und bindender Phasenwirkung.
```

### Rollenbewegung

Vorher:

```text
max_rank >= 4
ranks[-1] >= 3
weights[-1] > weights[0]
```

Jetzt:

```text
stable_core
core_near_retained
stable_surface
gaining_weight
losing_role_weight
variable_but_carried

entstehen aus Rangdruck, Stabilitaetsdruck, Gewichtsdruck und Driftspanne.
```

### Feldzeit

Vorher:

```text
ticks_since_seen <= 1 -> immediate_afterimage
ticks_since_seen <= 8 -> near_return
sonst                 -> far_return
```

Jetzt:

```text
temporal_first_contact
temporal_immediate_afterimage
temporal_near_return
temporal_far_return

entstehen aus Zeitdruck, Nachhall, Wiederkehr und Formdistanz.
```

### Offline-Feld-Reorganisation

Vorher:

```text
touched_count <= 0
role_set_count <= 1
touched_count <= 3
```

Jetzt:

```text
sleep_no_touch
sleep_single_rekopplung_trace
sleep_focused_role_touch
sleep_broad_role_touch

entstehen aus Beruehrungsdruck, Rollenset-Druck und Fokus/Breite der Offline-Aktivierung.
```

## Siebte Bereinigung und Gesamtaudit

Der Suchlauf ueber `mini_dio/` zeigt nach den Bereinigungen drei Restgruppen.

### Technische Schutzlogik

Diese Stellen bleiben erlaubt, weil sie keine Bedeutung setzen:

```text
Division durch 0 vermeiden
leere Listen pruefen
Frame-Laenge pruefen
ungueltige Preise oder Distanzen abfangen
Indexzugriff absichern
```

Beispiele:

```text
weight_sum <= 0
seen_count <= 1
frame_samples <= 1
entry_price <= 0
len(sample) < 2
```

Das sind technische Stabilitaetsbedingungen, keine MCM-Regulation.

### Passive Diagnose und Bericht

Diese Stellen bleiben ebenfalls erlaubt, solange sie nur auswerten:

```text
seltene Innenfeldzustaende
Top-Ratio eines Reports
Karten-Aehnlichkeit
Clusteranzahl
Archetypen-Sichtbarkeit
Sleep-Topscore-Auswahl
```

Sie erzeugen Befundsprache, aber keine Feldsteuerung.

### Getrennte Lern- und Konsequenzkompatibilitaet

Einige Stellen gehoeren nicht zum passiven MCM-Forschungskern:

```text
mini_dio/mcm_neuron.py
mini_dio/mini_world.py
mini_dio/run_mini.py
mini_dio/action_memory_store.py
```

Sie enthalten einfache Konsequenz-, Aktions- oder Testweltlogik.
Diese Logik darf nicht als MCM-Feldmechanik gelesen werden.

Fuer den Forschungskern gilt:

```text
MCM-Feldordnung, Sinnesaufnahme, Feldzeit, Nachhall, Topologie,
Rekopplung, Fragmentierung, Rollenreifung und Offline-Reorganisation
laufen jetzt ueber relative Druckprofile statt harte Runtime-Grenzen.
```

Wenn spaeter ein reines Forschungsprofil ohne Aktionskompatibilitaet entstehen soll,
muessen diese Kompatibilitaetsdateien getrennt oder deaktivierbar gemacht werden.

## Noch vorhandene statische Bereiche

### Diagnose

Viele Dateien unter `tools/` nutzen Schwellen fuer:

```text
zu_duenn
bruch_mit_range_aufweitung
oeffnung_getragen
Rand / Zentrum / Bruecke
```

Das ist akzeptabel, solange diese Werte nur Berichte erzeugen.

Auch `mini_dio/mcm_effect_map.py` enthaelt weiterhin reine Berichtswerte fuer:

```text
seltene Innenfeldzustaende
Vergleichsaehnlichkeit zwischen Feldkarten
Archetypen-Reife in Auswertungen
```

Diese Werte sind Diagnose und duerfen nicht als Feldsteuerung gelesen werden.

### Benennung

Die bisher geprueften Benennungsbereiche wurden auf Druckvergleiche umgestellt.
Weitere Kandidaten muessen bei Bedarf gezielt gesucht werden, statt pauschal
alle Zahlen im Projekt zu entfernen.

### Kompatibilitaet

`mini_dio/action_selection.py` enthaelt noch aktive Kompatibilitaet.
Dieser Bereich gehoert nicht zum passiven MCM-Forschungskern und muss getrennt bleiben.

## Forschungsgrenze

`volle Kontrolle` bedeutet hier nicht:

```text
DIO bekommt beliebige Handlungsmacht.
```

Gemeint ist:

```text
Das Feld und seine Erfahrungsstruktur duerfen Bedeutung, Aufnahme und Regulation aus ihrer eigenen Lage heraus bilden.
```

Die Kontrolle liegt also nicht in harten Regeln, sondern in:

```text
Wiederkehr
Feldwirkung
Nachhall
Kopplung
Drift
erfahrungsgewichteter Rueckfuehrung
```

## Wie es weitergeht

Als naechstes sollte ein kurzer Kontrolllauf mit bestehenden Welten zeigen, ob die weichere Drucklogik die bisherigen Topologie- und Bedeutungsbefunde stabil haelt oder ob sich neue Varianz bildet.
