# Rohwelt-Gegenlesung der Rollenbreite

Stand: 2026-07-06

## Zweck

Nach der 10k-Segmentdiagnose wurde geprüft, welche Rohweltmerkmale mit breiten oder engen MCM-Rollenräumen zusammenfallen.

Verglichen wurden gezielt breite gegen enge Abschnitte:

```text
sideways Start 0 gegen Start 4000
negative_stress Start 2000 gegen Start 4000
positive_expansion Start 4000 gegen Start 8000
```

Die Frage:

```text
Kommt Rollenbreite eher aus Volatilität, Richtung, Wiederholung, Nachhall oder Rekopplung?
```

## Vergleichstabelle

| Fall | Start | Rollen | Kombis | Net% | Pfad% | Range% | AvgRange% | Fliprate | Up/Down | Rekopplung | Nachhall | Effektrollen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| sideways breit | 0 | 7/7 | 19/19 | -13.150 | 495.206 | 29.644 | 0.4913 | 0.484 | 973/986 | 0.702821 | 0.174799 | gespannt=1; kippend=8; stabil=1745; tragend_unruhig=240 |
| sideways eng | 4000 | 2/2 | 1/1 | 1.345 | 286.268 | 13.441 | 0.2875 | 0.459 | 969/939 | 0.695582 | 0.138300 | kippend=14; stabil=1604; tragend_unruhig=376 |
| stress breit | 2000 | 4/4 | 6/6 | 13.158 | 401.559 | 21.784 | 0.3931 | 0.425 | 916/894 | 0.700541 | 0.159969 | gespannt=1; kippend=9; stabil=1681; tragend_unruhig=303 |
| stress eng | 4000 | 2/2 | 1/1 | -2.885 | 475.065 | 21.964 | 0.4501 | 0.463 | 928/959 | 0.702411 | 0.181988 | kippend=15; stabil=1703; tragend_unruhig=276 |
| expansion breit | 4000 | 5/5 | 10/10 | 25.280 | 658.280 | 36.920 | 0.6469 | 0.462 | 1009/906 | 0.689427 | 0.100488 | gespannt=1; kippend=20; stabil=1393; tragend_unruhig=580 |
| expansion eng | 8000 | 3/3 | 3/3 | 12.795 | 488.716 | 24.008 | 0.4970 | 0.475 | 973/955 | 0.697626 | 0.155083 | kippend=15; stabil=1633; tragend_unruhig=346 |

## Befund

Rollenbreite folgt nicht einfach der stärksten Rohvolatilität.

Beispiele:

- `stress eng` hat mehr Pfadbewegung, mehr durchschnittliche Kerzenrange, höhere Rekopplung und höheren Nachhall als `stress breit`, bleibt aber enger.
- `expansion breit` ist klar bewegungsstärker und rollt breiter aus.
- `sideways breit` ist deutlich bewegungsreicher als `sideways eng` und trägt entsprechend mehr Kombinationen.

Damit reicht keine einzelne Rohgröße als Erklärung.

## Arbeitslesung

Rollenbreite entsteht eher dort, wo Rohweltbewegung und Feldkopplung nicht nur laut sind, sondern eine offene Binnenphase bilden.

Aktuell wirkt diese Kombination relevant:

```text
gerichtete oder ausgreifende Bewegung
+ ausreichend Rollenvarianz
+ nicht zu stark fokussierender Nachhall
+ nicht nur Einzelrekopplung
= breiter Rollenraum
```

Engere Rollenräume entstehen eher dort, wo das Feld trotz Bewegung in eine klare Rekopplung oder stabile Bindung zurückfällt.

## Gegen einfache Fehlannahmen

Nicht bestätigt:

```text
mehr Volatilität = mehr Rollenbreite
mehr Nachhall = mehr Rollenbreite
mehr Rekopplung = mehr Rollenbreite
```

Stärker bestätigt:

```text
Rollenbreite ist ein Feldzustand aus Rohweltbewegung und innerer Bindungsqualität.
```

## Bedeutung für MINI_DIO

MINI_DIOs MCM-Feld liest nicht nur laute Rohwelt.
Es unterscheidet offenbar:

- bewegte, aber fokussierende Lage,
- bewegte und öffnende Lage,
- stabile Rekopplung,
- tragend-unruhige Rollenbreite,
- dünne Kipp-/Spannungskontakte.

Damit wird die Rohwelt erst durch Feldwirkung interpretierbar.

## Grenze

Diese Diagnose ist korrelativ.
Sie zeigt noch nicht kausal, welches Rohweltmerkmal eine Rolle öffnet.
Sie zeigt aber, dass Rollenbreite nicht aus Rauschen allein erklärbar ist.

## Nächster Prüfpunkt

Als nächstes sollte die lokale Ereignisstruktur innerhalb der breitesten und engsten Segmente betrachtet werden:

```text
Welche Übergänge liegen vor der Rollenöffnung?
Welche Phasen führen zurück zur Einzelkopplung?
Welche Ton-/Energieform begleitet diese Umschaltung?
```
