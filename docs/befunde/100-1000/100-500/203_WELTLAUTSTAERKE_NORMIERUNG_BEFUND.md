# Weltlautstaerke und Normierungsfrage

Stand: 2026-06-18

## Zweck

Diese Notiz beantwortet die Frage, ob die staerkere SOL-Belastung wahrscheinlich aus den Daten selbst kommt oder aus einem Berechnungs-/Normierungsproblem.

Hierarchie der Pruefung:

1. Grundfrage: Warum kippt SOL frueher in Feldlast als BTC?
2. Unterpruefung: Ist SOL in der Rohwelt lauter/intensiver als BTC?
3. Folgeschritt: Entscheiden, ob eine Weltlautstaerke-Normierung notwendig ist.

## Befund

SOL ist in den geprueften Segmenten tatsaechlich deutlich lauter als BTC.

Die Weltlautstaerke steigt bei SOL schneller und hoeher:

| Welt | Lautstaerke | field_strained | Rekopplung | Tragqualitaet |
|---|---:|---:|---:|---:|
| BTC 2024 5m | `2.453` | `42` | `0.636577` | `0.366108` |
| BTC 2024 15m | `4.622` | `83` | `0.631196` | `0.362364` |
| BTC 2024 30m | `5.741` | `129` | `0.626156` | `0.359372` |
| BTC 2024 1h | `9.779` | `277` | `0.610376` | `0.345005` |
| SOL 2024 5m | `5.735` | `105` | `0.622776` | `0.358038` |
| SOL 2024 15m | `9.731` | `266` | `0.606542` | `0.343678` |
| SOL 2024 30m | `11.939` | `365` | `0.600205` | `0.341420` |
| SOL 2024 1h | `18.874` | `630` | `0.587027` | `0.333433` |

Das gleiche Muster erscheint auch 2025.

## Interpretation

Die staerkere SOL-Feldlast ist nicht nur zufaellig.

SOL kommt in diesen Welten mit hoeherer Rohwelt-Lautstaerke ins System:

- hoehere durchschnittliche Bewegung,
- hoehere Range,
- staerkere p95-Bewegung,
- hoehere verdichtete Kerzenpakete bei groesserer Zeitaufloesung.

Damit ist die fruehere SOL-Belastung fachlich plausibel.

## Normierungsrisiko

Trotzdem bleibt ein wichtiger Punkt:

Wenn Lautstaerke direkt zu stark in das MCM-Feld wirkt, kann MINI_DIO eine Welt nicht sauber genug zwischen Struktur und Intensitaet trennen.

Dann liest das Feld nicht nur:

- welche Form entsteht,
- wie sie wiederkehrt,
- wie sie koppelt,

sondern auch zu stark:

- wie laut das Rohsignal gerade ist.

Das waere kein klassischer Fehler, aber eine unsaubere Sensorik-Kopplung.

## Arbeitsunterscheidung

Wir brauchen deshalb drei getrennte Ebenen:

1. Struktur
   - Was bildet die Welt formal?
   - Welche Richtung, Verdichtung, Wiederkehr, Brueche?

2. Lautstaerke
   - Wie intensiv wirkt die Welt?
   - Wie stark sind Bewegung, Range, Frequenz und Volumenrhythmus?

3. MCM-Feldwirkung
   - Was macht diese Welt mit dem Innenfeld?
   - Traegt sie, kippt sie, spannt sie, rekoppelt sie?

Nur wenn diese Ebenen getrennt lesbar sind, kann MINI_DIO spaeter organisch unterscheiden:

- Das ist eine tragende Struktur, aber laut.
- Das ist eine leise Struktur, aber innerlich instabil.
- Das ist eine laute Welt, die trotzdem gut rekoppelt.
- Das ist eine verdichtete Welt, die mein Feld ueberlastet.

## Konsequenz fuer MINI_DIO

Die aktuelle Diagnose spricht fuer eine passive Weltlautstaerke-Karte.

Diese Karte darf nicht regulieren und keine Handlung ausloesen.

Sie soll nur sichtbar machen:

- wie laut eine Welt in das System kommt,
- wie stark das MCM-Feld darauf reagiert,
- ob die Reaktion proportional oder ueberempfindlich ist.

## Wie es weitergeht

Als naechstes sollte eine `Verdichtungs-Sensitivitaet` berechnet werden.

Nicht als Regel, sondern als passive Forschungskennzahl:

- Lautstaerkeanstieg pro Zeitaufloesung,
- Rekopplungsverlust pro Zeitaufloesung,
- Strain-Anstieg pro Lautstaerke,
- Memory-Anstieg pro Lautstaerke.

Ziel:

Wir pruefen, ob MINI_DIO nur lautere Welten staerker fuehlt oder ob bestimmte Welten bei gleicher Lautstaerke ueberproportional viel Innenfeldlast erzeugen.
