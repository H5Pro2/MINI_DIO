# 1724 - PAXG Feldzeit: Daempfung und Rekopplung

## Frage

Aus dem Asset-Vergleich entstand die Frage, ob der aktuelle MINI_DIO-Stand
methodisch besser oder schlechter geworden ist.

Die konkrete Unterpruefung:

```text
Was bedeutet die PAXG-Verschiebung von 5m zu 1h?
Ist es verlorene Kopplung oder geregelter Abstand?
```

## Ausgangsbefund

PAXG 5m:

```text
Randdruck   0.4222
Offen       0.1469
Rekopplung  0.3566
Daempfung   0.0743
```

PAXG 1h:

```text
Randdruck   0.4147
Offen       0.1486
Rekopplung  0.3268
Daempfung   0.1099
```

Der erste Eindruck war:

```text
1h rekoppelt weniger und daempft mehr.
```

## Ruecklesung

Die Abschnittsanalyse zeigt aber, dass Daempfung und Rekopplung keine
einfachen Gegensaetze sind.

Bei PAXG 5m:

```text
Daempfung dominant mit hohem Rekopplungs-Score:
561 Episoden
Anteil 0.0561
```

Bei PAXG 1h:

```text
Daempfung dominant mit hohem Rekopplungs-Score:
801 Episoden
Anteil 0.0913
```

Das bedeutet:

```text
PAXG 1h verliert nicht einfach Kontakt.
PAXG 1h bildet haeufiger gedämpfte Rekopplung.
```

## Beispielhafte Spitzen

PAXG 1h zeigt in den staerksten Daempfungsstellen:

```text
tick 6357  dio_0g3b  stabil  daempfung 0.9665  rekopplung 0.9134
tick 3057  dio_13o0  stabil  daempfung 0.9646  rekopplung 0.9210
tick 1211  dio_0g3b  stabil  daempfung 0.9606  rekopplung 0.8298
tick 3584  dio_13o0  stabil  daempfung 0.9599  rekopplung 0.9402
tick 6218  dio_0g3b  stabil  daempfung 0.9598  rekopplung 0.9494
```

Die Wirkungsklasse bleibt dabei `stabil`.

## Interpretation

Der aktuelle MINI_DIO-Stand ist methodisch besser als die fruehere starre
Lesung, weil er nicht mehr erzwingt:

```text
Daempfung = schlecht
Rekopplung = gut
Randdruck = Randrolle
```

Stattdessen wird sichtbar:

```text
Daempfung kann Schutzkontakt sein.
Rekopplung kann in gedämpfter Form weiter bestehen.
Weltzeit veraendert die Art der Kopplung.
```

Das ist fuer die MCM-Forschung wichtig, weil eine organische Feldlesung nicht
nur maximale Bindung sucht. Sie muss auch erkennen koennen, wann Abstand eine
tragende Form ist.

## Aussage zum aktuellen Stand

Die letzten Erweiterungen machen MINI_DIO nicht automatisch "besser" im
produktiven Sinn.

Sie machen das System aber methodisch besser lesbar:

```text
mehr Differenzierung
weniger harte Klassen
mehr Reproduzierbarkeit
bessere Trennung von globaler Rolle und lokalem Druck
bessere Trennung von Kontaktverlust und gedämpfter Kopplung
```

Damit ist die aktuelle Richtung fachlich staerker als eine einfache
Topologieklasse.
