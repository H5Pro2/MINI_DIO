# 1846 - MCM-Feldrollen-Memory: Mehrasset-Zwischenlagen

## Grundfrage

Bleibt der Realwelt-Vorsprung ueber mehrere Startpunkte hinweg sichtbar, oder ist er nur ein Fensterartefakt?

## Methode

- Pro Asset und Startpunkt wird ein Realfenster geschnitten.
- Daraus entstehen zwei assetnahe Nullwelten: Random-Sign und Shuffle-Order.
- Alle Laeufe bleiben passiv und nutzen `world_relative`.
- Bewertet werden Quellennaehe, Kernnaehe, Nachhall-Delta und Feldzeit-Delta.

## Gruppenvergleich

| Gruppe | Welten | Kernfamilien Ø | Quellennähe Ø | Kernnähe Ø | Nachhall-Delta Ø | Feldzeit-Delta Ø | Zustände |
|---|---:|---:|---:|---:|---:|---:|---|
| `real` | 10 | 22.80 | 0.708 | 0.337 | 0.2478 | 0.1202 | `reifungsrolle_reproduziert:10` |
| `null_random` | 10 | 22.60 | 0.671 | 0.283 | 0.2406 | 0.1168 | `reifungsrolle_reproduziert:10` |
| `null_shuffle` | 10 | 24.00 | 0.651 | 0.280 | 0.2391 | 0.1159 | `reifungsrolle_reproduziert:10` |

## Fensterlesung

| Asset | Start | Quellenvorsprung | Kernvorsprung | Nachhallvorsprung | Feldzeitvorsprung | Feldvorsprung | Lesung |
|---|---:|---:|---:|---:|---:|---:|---|
| BTC | 0 | -0.0357 | 0.0000 | 0.0131 | 0.0062 | -0.0060 | `graduell_realer_nachhall_ohne_kern` |
| BTC | 6000 | 0.0000 | -0.0212 | -0.0079 | -0.0045 | -0.0114 | `graduell_gemischt` |
| DOGE | 0 | 0.0700 | 0.1221 | 0.0050 | 0.0028 | 0.0736 | `realwelt_kernnaehe_staerker` |
| DOGE | 6000 | 0.0343 | 0.0294 | -0.0075 | -0.0028 | 0.0203 | `graduell_kernnaehe_ohne_feldzeitvorsprung` |
| PAXG | 0 | 0.0951 | 0.1301 | 0.0103 | 0.0029 | 0.0843 | `realwelt_kernnaehe_staerker` |
| PAXG | 6000 | 0.0000 | 0.0146 | 0.0147 | 0.0056 | 0.0096 | `graduell_gemischt` |
| SOL | 0 | 0.0357 | 0.0194 | 0.0023 | 0.0007 | 0.0181 | `graduell_gemischt` |
| SOL | 6000 | 0.0000 | 0.0294 | 0.0108 | 0.0064 | 0.0158 | `graduell_gemischt` |
| XRP | 0 | 0.0343 | 0.0092 | 0.0033 | 0.0024 | 0.0136 | `graduell_gemischt` |
| XRP | 6000 | 0.0343 | 0.0262 | 0.0002 | -0.0011 | 0.0202 | `graduell_kernnaehe_ohne_feldzeitvorsprung` |

## Befund

Fensterzustände:
- `graduell_gemischt`: 5
- `realwelt_kernnaehe_staerker`: 2
- `graduell_kernnaehe_ohne_feldzeitvorsprung`: 2
- `graduell_realer_nachhall_ohne_kern`: 1

Der Test trennt Reifung nicht mehr an einem einzelnen Lauf.
Er liest, ob Realwelt-Vorsprung als wiederkehrender Fenstereffekt erscheint oder ob Nullwelten gleich stark anschließen.

## Einordnung

Die Mehrasset-Prüfung bestätigt den Befund aus `1845`, aber mit mehr Breite.
Alle zehn Realfenster werden als `reifungsrolle_reproduziert` gelesen.
Auch Nullwelten reproduzieren Rollen, wodurch die Trennung weiterhin nicht hart ist.

Der Unterschied liegt in der Qualität der Zwischenlagen:

- DOGE und PAXG zeigen im Startfenster `0` klare Realwelt-Kernnähe.
- DOGE und XRP zeigen im späteren Fenster `6000` Kernnähe ohne Feldzeitvorsprung.
- BTC zeigt im Startfenster realen Nachhall ohne Kernnähe.
- SOL bleibt in beiden Fenstern graduell gemischt, aber mit positivem Feldvorsprung.

Damit wirken die Zwischenlagen nicht BTC/SOL-spezifisch.
Sie erscheinen assetübergreifend, aber je nach Weltmilieu unterschiedlich gefärbt.
MINI_DIO liest also nicht nur `real` gegen `null`, sondern mehrere Arten von Feldanschluss:
Kernnähe, Nachhallnähe, Feldzeitnähe und offene Mischung.

Fachlich ist das wichtig, weil daraus keine harte Regel entstehen muss.
Die Feldrollen-Memory kann organisch erweitert werden, indem sie diese Zwischenlagen als Reifungsqualität speichert:
`kernnah`, `nachhallnah`, `feldzeitnah`, `offen_gemischt`, `nullnah`.
Das bleibt passiv und beschreibt nur, wie stark eine Rolle im Feld getragen wird.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Zwischenlagen direkt in die passive Feldrollen-Memory aufgenommen werden können.
Ziel ist keine neue Steuerung, sondern eine tiefere Reifungsbeschreibung jeder Feldrolle.
