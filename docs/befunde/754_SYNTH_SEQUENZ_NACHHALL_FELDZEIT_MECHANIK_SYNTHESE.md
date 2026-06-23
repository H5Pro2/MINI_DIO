# Synthetische Sequenz-Nachhall Feldzeit-Mechanik Synthese

Stand: 2026-06-22

## Zweck

Diese Synthese fasst die Sequenzpruefungen zusammen.

Geprueft wurden vier Varianten derselben `bruch_rand`-Grundwelt:

1. Originalreihenfolge
2. `randflackern` vor `bruch_impuls`
3. kurze `rekopplung` vor `randflackern`
4. lange `rekopplung` vor `randflackern`

Die Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Grundfrage

Die zentrale Frage war:

```text
Liest MINI_DIO nur einzelne Phasen,
oder liest das Feld Sequenzordnung, Nachhall und Gegenwartswirkung?
```

## Gesamtbefund

MINI_DIO zeigt eine klare Trennung:

```text
Globale Topologie bleibt stabil.
Lokale Phasenrollen veraendern sich durch Reihenfolge.
Vorherige Feldlage wirkt als Kontext.
Aktuelle Weltqualitaet bleibt eigenstaendig wirksam.
```

Das ist der wichtigste mechanische Befund:

```text
Nachhall ist Kontext, nicht Kontrolle.
```

## Variantenvergleich

| Variante | Globaler Effekt | Lokaler Randbefund | Lesart |
|---|---|---|---|
| Original | stabil zentriert | `randflackern` offen dominant, aber mit Zentrum/Rekopplung | Basisfolge |
| Rand vor Bruch | global fast gleich | `randflackern` offener, folgender Bruch zentrumsnaeher | Reihenfolge veraendert lokale Rolle |
| Kurze Rekopplung vor Rand | global fast gleich | `randflackern` wird nicht abgefedert, eher offener | Rekopplung davor ist keine automatische Beruhigung |
| Lange Rekopplung vor Rand | global tragfaehiger | `randflackern` etwas weniger offen als kurze Rekopplung, aber nicht besser als Original | laengere Rekopplung stabilisiert global, nicht lokal absolut |

## Zahlenkern: `randflackern`

| Variante | Zentrum | Offen | Rekopplungsnaehe | Rand/Kipp |
|---|---:|---:|---:|---:|
| Original | 0.2700 | 0.5186 | 0.2100 | 0.0014 |
| Rand vor Bruch | 0.1857 | 0.5714 | 0.2429 | 0.0000 |
| Kurze Rekopplung vor Rand | 0.2329 | 0.5486 | 0.2143 | 0.0043 |
| Lange Rekopplung vor Rand | 0.2557 | 0.5371 | 0.2029 | 0.0043 |

Ableitung:

- `randflackern` bleibt in allen Varianten offen dominant.
- Die Reihenfolge veraendert die lokale Rolle sichtbar.
- Lange Rekopplung wirkt besser als kurze Rekopplung, aber nicht besser als Original.
- Die aktuelle Randqualitaet wird nicht durch den Vorzustand geloescht.

## Zahlenkern: globale Topologie

| Variante | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry |
|---|---:|---:|---:|---:|---:|
| Original | 0.9539 | 0.0456 | 0.0005 | 0.7461 | 0.5985 |
| Rand vor Bruch | 0.9524 | 0.0471 | 0.0005 | 0.7462 | 0.5985 |
| Kurze Rekopplung vor Rand | 0.9541 | 0.0450 | 0.0010 | 0.7460 | 0.5982 |
| Lange Rekopplung vor Rand | 0.9590 | 0.0403 | 0.0007 | 0.7485 | 0.6030 |

Ableitung:

- Topologie bleibt ueber alle Varianten stabil.
- Lange Rekopplung erhoeht globale Zentrumsnaehe.
- Die globale Ordnung ist robuster als die lokale Rollenlesung.

## Mechanische Folgerung

Die Sequenzbefunde sprechen fuer eine dreiteilige Feldzeit-Mechanik:

```text
1. Vorzustand
   Welche Feldlage war vorher aktiv?

2. Gegenwart
   Welche Weltqualitaet wirkt jetzt?

3. Integrationsgeschichte
   Wie wird die aktuelle Wirkung im Feld gehalten, geoeffnet, rekoppelt oder zentriert?
```

Wichtig:

```text
Der Vorzustand beeinflusst die Gegenwart.
Er ersetzt sie aber nicht.
```

## MCM-Lesart

Fuer die MCM-Deutung ist dieser Befund relevant:

```text
Zeit im Feld ist nicht nur Dauer.
Zeit im Feld ist geordnete Wirkungsgeschichte.
```

Das Feld bildet keine starre Regel:

```text
wenn vorher Rekopplung, dann naechste Lage ruhig
```

Sondern eine Kontextlesung:

```text
vorher war Rekopplung,
jetzt wirkt Rand,
beides zusammen ergibt die aktuelle Innenfeldrolle
```

## Bedeutung fuer MINI_DIO

MINI_DIO sollte Sequenz nicht als harte Logik bekommen.

Stattdessen sollte die passive Analyse weiter lesen:

- welche Feldlage vorher aktiv war,
- wie lange sie wirkte,
- welche lokale Weltqualitaet danach kam,
- ob die neue Lage rekoppelt, oeffnet oder kippt,
- ob Bedeutungsfamilien stabil bleiben oder neue lokale Varianten bilden.

Damit bleibt MINI_DIO organisch:

```text
Erinnerung und Nachhall wirken,
aber Gegenwart bleibt real.
```

## Grenze

Die Befunde stammen aus synthetischen kontrollierten Welten.

Gesichert im aktuellen Stand:

- Sequenzordnung veraendert lokale Phasenrollen.
- Globale Topologie bleibt stabil.
- Nachhall ist sichtbar, aber nicht deterministisch.
- Rekopplung ist keine automatische Schutzwirkung.

Noch offen:

- reale Sequenzgegenproben,
- staerkere Permutationen,
- mehrphasige Nachhallketten,
- Vergleich gegen vollstaendig zufaellige Phasenfolge.

## Schlussfolgerung

Die Sequenzreihe staerkt die Feldzeit-Hypothese:

```text
Feldzeit = Integrationsgeschichte aus Vorzustand, Gegenwart und Nachhall.
```

Und sie begrenzt sie gleichzeitig:

```text
Feldzeit kontrolliert die Gegenwart nicht.
Sie gibt ihr Kontext.
```

## Wie es weitergeht

Als naechstes sollte eine vollstaendig permutierte oder zufaellig geordnete Phasenfolge gegen die Originalfolge laufen. Ziel: pruefen, ab welchem Punkt die lokale Nachhallstruktur nicht mehr nur verschoben, sondern wirklich zerlegt wird.
