# MCM Gegenformen Tickfenster Bewertung

Stand: 2026-07-02

## Grundfrage

Welche konkreten Feldfolgen stehen hinter Nachlast und gebrochener Rekopplung?

## Ergebnis

Die Diagnose `1262_MCM_GEGENFORMEN_TICKFENSTER` isolierte `92` Gegenfenster.

Die Gegenformarten:

- `61` schwache Entlastung / gebrochene Rekopplung
- `14` aktive Nachlast
- `9` Rueckfall nach kurzer Rekopplung
- `7` gemischte Gegenform
- `1` Last bleibt

## Wichtigster Befund

Die staerksten Rueckfaelle kommen fast alle aus:

```text
spannungsrand_kippnaehe -> zentrum_stabil -> spannungsrand_kippnaehe
```

Lesart:

```text
Das Feld findet kurz Zentrum,
kann diese Stabilisierung aber nicht halten,
und faellt erneut in Rand/Kipp.
```

Das ist fachlich anders als:

```text
Rand/Kipp -> Offenheit
```

Dort entsteht meist Entlastung.

## Zweite Gegenform

Viele aktive Nachlast-Fenster liegen in:

```text
spannungsrand_kippnaehe -> zentrum_stabil -> rekopplungsnaehe
```

Hier ist die Sequenz oberflaechlich positiver, aber die Folgewerte zeigen:

- Rekopplung faellt,
- Strain steigt,
- das Fenster bleibt nicht sauber entlastend.

Lesart:

```text
Das Feld bewegt sich Richtung Anschluss,
aber der Anschluss wird nicht stabil genug getragen.
```

## Bedeutung

Die Gegenformen zeigen:

```text
Zentrum ist nicht automatisch Stabilitaet.
Rekopplung ist nicht automatisch Entlastung.
```

Entscheidend ist, ob die Folgebewegung tragend bleibt.

## MCM-Lesung

Damit wird die bisherige Mechanik praeziser:

```text
Rohweltbruch -> Randkontakt -> Feldfolge
```

reicht noch nicht ganz.

Genauer:

```text
Rohweltbruch -> Randkontakt -> kurze Stabilisierung? -> Folgehalt
```

Die kritische Stelle ist der Folgehalt.

## Schluss

Die Gegenformen sind keine zufaelligen Ausreisser.

Sie wirken wie Feldmomente, in denen MINI_DIO kurz Zentrum oder Rekopplung erreicht, diese aber nicht stabil halten kann.

Das ist eine wichtige Innenfeldinformation:

```text
Nicht jede Rueckkehr zum Zentrum ist bereits Ordnung.
Ordnung braucht Folgehalt.
```

## Wie es weitergeht

Als naechstes sollte `Folgehalt` als passive Diagnose gemessen werden: Wie lange bleibt Zentrum/Rekopplung nach einem Randkontakt erhalten, bevor erneut Rand/Kipp entsteht?
