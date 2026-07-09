# Bewertung 1301 - Feintrennung ueberstabiler Weltlagen

## Prueffrage

Die fruehere Klasse `ueberstabil_sinnesdominant` war zu grob.

Sie vermischte:

- extrem leise/scharfe Ueberstabilitaet
- leise/scharfe Ueberstabilitaet
- visuell weichere Ueberstabilitaet
- gemischte Ueberstabilitaet
- Ueberstabilitaet mit Randreiz

Die neue Pruefung trennt diese Formen aus Messwerten.

## Ergebnis

Die neue Feintrennung erzeugt folgende Weltlagen:

| Weltlage | Welten | Folge |
|---|---:|---|
| normale_weltspannung | 16 | beruhigend |
| offen_suchend | 5 | beruhigend |
| ruhig_zentrumsnah | 1 | neutral |
| ueberstabil_extrem_leise_scharf | 1 | neutral |
| ueberstabil_leise_scharf | 2 | neutral |
| ueberstabil_visuell_weicher | 1 | neutral |
| ueberstabil_gemischt | 1 | neutral |
| ueberstabil_mit_randreiz | 2 | stabil leicht / neutral |

## Wichtigster Befund

Die Rezeptorhaltung bleibt lageabhaengig:

```text
normale_weltspannung:
  beruhigend

offen_suchend:
  beruhigend

ruhig / ueberstabil / sinnesdominant:
  neutral oder nur stabil leicht
```

Damit wird die vorherige Aussage schaerfer:

```text
Die Rezeptorhaltung wirkt nicht global.
Sie wirkt vor allem dort, wo die Weltlage noch offen oder normal dynamisch ist.
Wenn das Feld bereits stark ueberstabil oder sehr zentrumsnah ist, greift sie kaum.
```

## Bedeutung fuer MINI_DIO

Das passt zur organischen Zielrichtung.

Eine Rezeptorschicht sollte nicht immer staerker regulieren.

Sie sollte erkennen:

```text
Hier ist Aufnahmeordnung hilfreich.
Hier ist die Lage bereits ruhig oder ueberstabil.
Hier reicht Neutralitaet.
```

Das ist keine Handlungslogik.

Es ist eine passive Innenlesung der Aufnahmequalitaet.

## Methodische Grenze

Die Feintrennung ist noch heuristisch.

Sie nutzt Mittelwerte aus A/B-Reports.

Fuer eine belastbarere interne Mechanik braucht Mini-DIO spaeter Verlaufssignale:

- Varianz innerhalb der Weltlage
- Dauer der Lage
- Uebergang in andere Lage
- Nachhall der Lage
- Rueckfall oder Rekopplung nach der Lage

## Konsequenz

Die Rezeptor-Adaptationsmemory sollte kuenftig nicht nur den Durchschnitt speichern.

Sie sollte pro gemessener Weltlage auch den Verlauf speichern:

```text
Lage erkannt
Haltung angewendet
Feldfolge beobachtet
Lage stabil / driftend / kippend / entlastend
```
