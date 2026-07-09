# Fensterbreite Und Feldklassen-Verdichtung

Stand: 2026-07-06

## Grundfrage

War die `7/2`-Struktur der 1000er-Fenster eine stabile Feldordnung, oder entsteht sie durch die gewaehlte Fensterbreite?

## Unterpruefung

Dieselben vier Weltarten wurden mit drei Fensterbreiten passiv gelesen:

- `500` Zeilen pro Fenster,
- `1000` Zeilen pro Fenster,
- `2000` Zeilen pro Fenster.

Die Weltarten blieben gleich:

- `RUHIG_SIDEWAYS_2026`
- `STRESS_NEGATIV_2024`
- `EXPANSION_POSITIV_2023`
- `SYNTH_RAND_KIPP`

Die Pruefung bleibt passiv. Sie erzeugt keine Handlung und keine Richtung.

## Ergebnis

| Fensterbreite | Fenster | Einzelrekopplung | Uebergang | Mehrrollen |
|---:|---:|---:|---:|---:|
| 500 | 72 | 62 | 10 | 0 |
| 1000 | 36 | 28 | 8 | 0 |
| 2000 | 16 | 9 | 6 | 1 |

Die `7/2`-Struktur der 1000er-Fenster ist damit nicht als feste Regel zu lesen.

Stattdessen zeigt sich:

```text
Je groesser das Fenster, desto eher verdichtet Einzelrekopplung zu Uebergang oder Mehrrollennaehe.
```

## Lesung

Kleinere Fenster lesen staerker dominante Momentnaehe. Dadurch entsteht mehr Einzelrekopplung.

Groessere Fenster enthalten mehr Feldzeit, Nachhall und Rollenwechsel. Dadurch werden Uebergaenge und Mehrrollennaehe sichtbarer.

Das passt zur bisherigen MCM-Lesung:

```text
Feldklasse ist nicht nur Weltart.
Feldklasse ist Weltphase ueber Feldzeit.
```

## Auffaellige Punkte

Bei `500`er-Fenstern:

- Einzelrekopplung dominiert stark.
- Uebergaenge bleiben sichtbar, aber seltener.
- Keine breite Mehrrollennaehe.

Bei `1000`er-Fenstern:

- jede Weltart zeigte 7 Einzelrekopplungen und 2 Uebergaenge.
- diese Struktur war auffaellig, aber noch schnittabhaengig.

Bei `2000`er-Fenstern:

- Uebergang nimmt deutlich zu.
- `SYNTH_RAND_KIPP` bildet einen Mehrrollen-Kandidaten.
- laengere Ausschnitte koennen mehrere lokale Rollen gemeinsam tragen.

## Bedeutung Fuer MINI_DIO

Dieser Befund ist wichtig, weil er die Feldklassen aus der Ecke starrer Etiketten herausnimmt.

MINI_DIO liest nicht nur:

```text
Diese Welt ist Einzelrekopplung.
```

Sondern eher:

```text
In diesem Ausschnitt dominiert Einzelrekopplung.
In laengerer Feldzeit koennen Uebergang und Mehrrollennaehe sichtbar werden.
```

Damit wird Feldzeit als Verdichtungsraum konkreter:

- kurzer Ausschnitt: Momentdominanz,
- mittlerer Ausschnitt: lokale Uebergangsphaenomenik,
- langer Ausschnitt: Rollenverdichtung und Mehrrollennaehe.

## Quellen

- [1586 Weltarten 500er Fenster](1586_FELDKLASSEN_FENSTERSUCHE_WELTARTEN_500.md)
- [1584 Weltarten 1000er Fenster](1584_FELDKLASSEN_FENSTERSUCHE_WELTARTEN.md)
- [1587 Weltarten 2000er Fenster](1587_FELDKLASSEN_FENSTERSUCHE_WELTARTEN_2000.md)

## Wie es weitergeht

Als naechstes sollte der 2000er-Mehrrollen-Kandidat `SYNTH_RAND_KIPP start0` reproduziert werden. Ziel: pruefen, ob diese Mehrrollennaehe bei frischem Lauf wieder auftaucht oder nur aus einem einmaligen langen Schnitt entstanden ist.
