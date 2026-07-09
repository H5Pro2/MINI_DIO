# SYNTH_RAND_KIPP Mehrrollen-Reproduktion

Stand: 2026-07-06

## Grundfrage

War der 2000er-Mehrrollen-Kandidat `SYNTH_RAND_KIPP start0` stabil reproduzierbar, oder entstand er nur aus einem einmaligen langen Schnitt?

## Unterpruefung

Der Kandidat aus der 2000er-Fensterbreitenpruefung wurde als Real-Sleep-Real-Kette wiederholt:

```text
Real A: data/scan_synth-rand-kipp_start0_size2000.csv
Sleep: passive Offline-Reorganisation
Real B: dieselbe Welt erneut
```

Die Pruefung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.

## Ergebnis

Die Real-Welt wurde reproduziert:

- Episoden: `1994 -> 1994`
- Unique Syntax: `109 -> 109`
- Feldepisoden: `5 -> 5`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`
- MCM-Tragqualitaet: `0.580908 -> 0.580991`
- MCM-Rekopplung: `0.734612 -> 0.734537`

Damit ist die Mehrrollennaehe als Welt-/Feldbefund stabil reproduziert.

## Sleep-Reaktivierung

Die Sleep-Phase beruehrte alle 5 Rollen.

Im Real-B-Follow-up:

- `4 / 5` Rollen wurden reaktiviert,
- `6 / 10` Kombinationen wurden voll reaktiviert,
- `4 / 10` Kombinationen wurden teilweise reaktiviert.

Eine Rolle blieb unveraendert:

```text
dio_mcm_episode_0eghs1d
```

Diese Rolle war eine `field_strained`-Rolle. Sie wurde im Sleep beruehrt, aber im Folgelauf nicht erneut verstaerkt.

## Lesung

Der Befund trennt zwei Dinge:

```text
Die Welt-/Feldstruktur ist reproduzierbar.
Die Offline-Reorganisation ist selektiv.
```

Das ist fachlich wichtiger als eine perfekte Wiederholung aller Sleep-Spuren.

MINI_DIO zeigt hier keine wahllose Sleep-Verstaerkung. Die tragenden Rollen rekoppeln staerker, waehrend eine strainnahe Rolle unveraendert bleibt.

Damit entsteht eine vorsichtige Lesung:

```text
Mehrrollennaehe kann stabil wiederkehren,
aber nicht jede beruehrte Rolle wird gleich stark zurueckgetragen.
```

## Vergleich Zur XRP-Reproduktion

Die vorherige XRP-Mehrrollen-Reproduktion reaktivierte alle Rollen und alle Kombinationen voll.

`SYNTH_RAND_KIPP start0` ist anders:

- Real A / Real B bleibt voll stabil.
- Sleep-Reaktivierung bleibt teilweise.
- Strainnahe Rollen werden nicht automatisch gleich stark getragen.

Das spricht fuer unterschiedliche Offline-Kopplungsqualitaet je Feldmilieu.

## Bedeutung Fuer MINI_DIO

Dieser Befund stuetzt drei Punkte:

- Lange Feldzeit kann Mehrrollennaehe sichtbar machen.
- Mehrrollennaehe kann reproduzierbar sein.
- Offline-Feld-Reorganisation wirkt selektiv, nicht als starre Vollverstaerkung.

Damit wird die Sleep-/Offline-Schicht als diagnostische Reorganisationsspur konkreter: Sie markiert bestehende Rollen, aber deren spaetere Reaktivierung haengt von Rollenqualitaet und Feldmilieu ab.

## Quellen

- [1587 Weltarten 2000er Fenster](1587_FELDKLASSEN_FENSTERSUCHE_WELTARTEN_2000.md)
- [1588 Fensterbreite und Feldklassen-Verdichtung](1588_FENSTERBREITE_UND_FELDKLASSEN_VERDICHTUNG.md)
- [1589 SYNTH_RAND_KIPP 2000 Mehrrollen-Repro](1589_SYNTH_RAND_KIPP_2000_MEHRROLLEN_REPRO.md)
