# 10k-Segmente: Rollenbreite und Feldzeit

Stand: 2026-07-06

## Zweck

Die 10k-Prüfung zeigte, dass Rollenbreite über längere Weltzeit nicht fest bleibt.
Diese Segmentdiagnose zerlegt die drei 10k-Welten in je fünf 2000er-Abschnitte.

Grundfrage:

```text
Welche Binnenabschnitte verschieben die Rollenbreite?
```

Unterprüfung:

```text
Seitwärtswelt 2026
negative Stresswelt 2023
positive Expansionswelt 2023
```

Alle Segmente wurden mit derselben passiven Real-Sleep-Real-Kette geprüft:

```text
Sinnesmodus: calibrated_relative
Segmentgröße: 2000 Zeilen
Sleep-Ticks: 300
```

## Segmenttabelle

| Welt | Start | Rollen | Kombinationen | Syntax | stabil | tragend_unruhig | kippend | gespannt | Rekopplung | Nachhall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| negative_stress_2023_10k | 0 | 2/2 | 1/1 | 383 | 1472 | 504 | 18 | 0 | 0.692433 | 0.126551 |
| negative_stress_2023_10k | 2000 | 4/4 | 6/6 | 314 | 1681 | 303 | 9 | 1 | 0.700541 | 0.159969 |
| negative_stress_2023_10k | 4000 | 2/2 | 1/1 | 274 | 1703 | 276 | 15 | 0 | 0.702411 | 0.181988 |
| negative_stress_2023_10k | 6000 | 3/3 | 3/3 | 330 | 1560 | 422 | 11 | 1 | 0.696504 | 0.138270 |
| negative_stress_2023_10k | 8000 | 4/4 | 6/6 | 441 | 1437 | 528 | 28 | 1 | 0.689311 | 0.109644 |
| positive_expansion_2023_10k | 0 | 4/4 | 6/6 | 312 | 1605 | 371 | 18 | 0 | 0.698394 | 0.148830 |
| positive_expansion_2023_10k | 2000 | 3/3 | 3/3 | 437 | 1433 | 532 | 28 | 1 | 0.688532 | 0.107891 |
| positive_expansion_2023_10k | 4000 | 5/5 | 10/10 | 394 | 1393 | 580 | 20 | 1 | 0.689427 | 0.100488 |
| positive_expansion_2023_10k | 6000 | 5/5 | 10/10 | 415 | 1472 | 498 | 24 | 0 | 0.689402 | 0.118277 |
| positive_expansion_2023_10k | 8000 | 3/3 | 3/3 | 304 | 1633 | 346 | 15 | 0 | 0.697626 | 0.155083 |
| sideways_2026_10k | 0 | 7/7 | 19/19 | 274 | 1745 | 240 | 8 | 1 | 0.702821 | 0.174799 |
| sideways_2026_10k | 2000 | 5/5 | 10/10 | 330 | 1555 | 425 | 14 | 0 | 0.694790 | 0.139279 |
| sideways_2026_10k | 4000 | 2/2 | 1/1 | 348 | 1604 | 376 | 14 | 0 | 0.695582 | 0.138300 |
| sideways_2026_10k | 6000 | 3/3 | 3/3 | 335 | 1510 | 467 | 16 | 1 | 0.694012 | 0.139838 |
| sideways_2026_10k | 8000 | 6/6 | 14/14 | 331 | 1616 | 361 | 16 | 1 | 0.696020 | 0.145656 |

## Befund je Welt

### Negative Stresswelt

Die Stresswelt bleibt nicht gleichmäßig eng.
Sie pendelt zwischen Einzelkopplung und mittlerer Rollenbreite:

```text
Start 0: 1 Kombination
Start 2000: 6 Kombinationen
Start 4000: 1 Kombination
Start 6000: 3 Kombinationen
Start 8000: 6 Kombinationen
```

Damit entsteht die 10k-Breite nicht aus einem durchgehenden Stressfeld,
sondern aus einzelnen Stressabschnitten, die mehr Rollenraum öffnen.

### Positive Expansionswelt

Expansion zeigt eine mittlere Binnenstruktur.
Die breitesten Abschnitte liegen in der Mitte:

```text
Start 4000: 10 Kombinationen
Start 6000: 10 Kombinationen
```

Anfang und Ende sind geordneter oder fokussierter.
Die Expansionswelt wirkt dadurch wie ein Feld mit mittlerer Ausdehnung und späterer Rückbindung.

### Seitwärtswelt

Seitwärts zeigt die stärkste Segmentdifferenz.
Das erste Segment ist sehr breit:

```text
Start 0: 19 Kombinationen
```

Danach fällt die Rollenbreite deutlich ab und steigt am Ende wieder:

```text
Start 4000: 1 Kombination
Start 8000: 14 Kombinationen
```

Das erklärt, warum die 10k-Gesamtwelt fokussierter wirken kann als der 1000er-Ausschnitt:
Breite und Fokussierung wechseln innerhalb derselben Welt.

## Hauptschluss

Rollenbreite ist abschnittsweise organisiert.

Nicht:

```text
Eine Weltklasse besitzt eine feste Rollenbreite.
```

Sondern:

```text
Eine Welt bildet über Feldzeit Binnenphasen,
die Rollenbreite öffnen, fokussieren oder erneut verbreitern.
```

Damit wird Feldzeit konkreter:

```text
Feldzeit = gewirkte Binnenfolge aus Kontakt, Nachhall, Rekopplung und Rollenverschiebung.
```

## Bedeutung für MINI_DIO

MINI_DIO liest nicht nur eine Gesamtwelt.
Das Feld trägt eine Binnenstruktur:

- Abschnitte mit breitem Rollenraum,
- Abschnitte mit enger Einzelkopplung,
- Abschnitte mit mittlerer Übergangsbreite,
- wiederkehrende Rekopplung trotz wechselnder Rollenbreite.

Damit wird die MCM-Feldorganisation dynamischer lesbar.
Die wichtigste neue Achse ist nicht nur Rolle, sondern Rollenbreite über Feldzeit.

## Grenze

Die Segmentdiagnose zeigt passive Innenfeldstruktur.
Sie zeigt noch keine Handlung, keine Strategie und keine bewusste Auswahl.

## Nächster Prüfpunkt

Als nächstes sollte geprüft werden, welche Rohweltmerkmale den Wechsel der Rollenbreite begleiten.
Besonders relevant sind die breitesten und engsten Abschnitte:

```text
sideways Start 0 gegen Start 4000
negative_stress Start 2000 gegen Start 4000
positive_expansion Start 4000 gegen Start 8000
```
