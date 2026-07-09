# Bewertung 1304 - Weltlagen-Folgememory

## Prueffrage

Nach der Weltlagen-Feintrennung war die naechste Frage:

```text
Ist eine Weltlage nur ein Zustand,
oder wird Aufnahmequalitaet erst ueber Lagefolgen sinnvoll lesbar?
```

Dafuer wurden Blockfolgen gebildet:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Ergebnis Standardwelten

Im ersten Lauf mit Standardwelten entstehen haeufige Folgen wie:

- `ruhig_zentrumsnah -> ruhig_zentrumsnah`
- `normale_weltspannung -> normale_weltspannung`
- `offen_suchend -> offen_suchend`
- `offen_suchend -> normale_weltspannung`
- `normale_weltspannung -> offen_suchend`
- `randlastige_sinneslage -> randlastige_sinneslage`

Ruhige oder stabile Folgen bleiben meist neutral.

Randlastige oder offen/randnahe Folgen zeigen haeufiger Beruhigung.

## Ergebnis Mehrwelten

Im breiteren Mehrweltenlauf werden die Folgen stabiler lesbar:

- `normale_weltspannung -> normale_weltspannung`: `83` Vorkommen, ueberwiegend neutral.
- `ueberstabil_extrem_leise_scharf -> ueberstabil_extrem_leise_scharf`: `75` Vorkommen, neutral.
- `offen_suchend -> offen_suchend`: `37` Vorkommen, neutral mit beruhigendem Anteil.
- `offen_suchend -> normale_weltspannung`: `30` Vorkommen, beruhigend/neutral.
- `randlastige_sinneslage -> randlastige_sinneslage`: `25` Vorkommen, klar beruhigend.
- `normale_weltspannung -> randlastige_sinneslage`: `13` Vorkommen, beruhigend.

Im Mehrweltenlauf tauchen keine verschiebenden Folgeklassen auf.

## Wichtigster Befund

Die Rezeptorhaltung wirkt nicht nur nach Einzelzustand.

Sie wirkt nach Lagefolge unterschiedlich:

```text
stabil -> stabil:
  meist neutral

offen -> offen / offen -> normal:
  neutral bis beruhigend

normal/offen -> randlastig:
  beruhigend

randlastig -> randlastig:
  deutlich beruhigend

ueberstabil -> ueberstabil:
  neutral
```

Damit wird Aufnahmequalitaet zeitlich lesbar.

## Bedeutung fuer MINI_DIO

Mini-DIO bekommt damit eine passive Vorform von zeitlicher Innenordnung:

```text
Diese Lage ist nicht nur jetzt so.
Sie kommt aus einer vorherigen Lage.
Die Rezeptorhaltung hat danach diese Feldfolge erzeugt.
```

Das ist wichtiger als ein einzelner Mittelwert.

Ein Organismus reagiert nicht nur auf einen Punkt, sondern auf Verlauf:

- bleibt etwas ruhig?
- driftet etwas?
- geht es in Rand/Kipp?
- kehrt es in Rekopplung zurueck?
- braucht es Aufnahmeberuhigung oder Neutralitaet?

## Grenze

Die Blockgroesse ist noch eine externe Diagnoseeinstellung.

Die Memory ist passiv.

Sie entscheidet nicht.

Sie zeigt nur, welche Lagefolgen welche Feldfolge nach Rezeptorhaltung tragen.

## Konsequenz

Die naechste sinnvolle Struktur ist:

```text
worldlage_sequence_memory
  Lage A -> Lage B
  Rezeptorhaltung
  Feldfolge
  Folgequalitaet
```

Damit kann Mini-DIO spaeter nicht nur Lagearten, sondern Lagebewegungen speichern.
