# Nachhall allein reicht nicht als Selektivitaets-Erklaerung

Stand: 2026-07-06

## Grundfrage

Entsteht selektive Offline-Feld-Reorganisation schon durch hohen Nachhall, oder braucht es zusaetzlich ein breites Rand-/Kippmilieu?

## Unterpruefung

Nach der realen 5-Rollen-Gegenprobe wurde eine synthetische Milieu-Suche ausgefuehrt. Danach wurde der staerkste synthetische Hoch-Nachhall-Uebergang als Real-Sleep-Real-Kette reproduziert:

- Welt: `BRUCH_RAND_A`
- Fenster: `start0`, `2000` Zeilen
- Nachhall: `0.764528`
- Rollen: `3`
- Kombinationen: `3`

## Ergebnis

Der Lauf `synth_bruch_rand_a_2000_start0_high_afterimage_repro` rekoppelte vollstaendig:

- Sleep-Rollen-Reaktivierung: `3 / 3`
- Sleep-Kombinationen voll reaktiviert: `3 / 3`
- Sleep-Kombinationen teilweise reaktiviert: `0 / 3`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

Damit zeigt ein synthetisches Hoch-Nachhall-Fenster nicht automatisch selektive Offline-Reorganisation.

## Befund

Die bisherige Selektivitaet des synthetischen Rand-/Kippfensters kann nicht durch Nachhall allein erklaert werden.

Aktuell wirkt die Kombination entscheidend:

- hoher Nachhall,
- breitere Rollennaehe,
- Rand-/Kippmilieu,
- mehrere Co-Touch-Kombinationen,
- gespannte Rollen im gemeinsamen Feld.

Ein hoher Nachhall mit nur drei Rollen kann dagegen voll rekoppeln.

## Interpretation

Nachhall ist eine wichtige Feldzeit-Achse, aber kein isolierter Kippschalter.

Selektive Offline-Feld-Reorganisation entsteht bisher eher, wenn hoher Nachhall auf ein breiteres und randnaeheres Rollenmilieu trifft. Das passt zur Lesart, dass MINI_DIO nicht nur Mengen oder Einzelwerte liest, sondern ein Feldmilieu aus Zeitspur, Rollennaehe, Spannung und Rekopplungsqualitaet.

## Grenze

Das ist ein einzelner synthetischer Hoch-Nachhall-Gegenlauf. Er widerlegt keine allgemeine Nachhallwirkung, grenzt aber die bisherige Arbeitshypothese scharf ein: Nachhall allein reicht in dieser Probe nicht.

## Wie es weitergeht

Als naechstes sollte ein synthetisches 5-Rollen-Fenster mit niedrigerem Nachhall gesucht oder erzeugt werden. Dann laesst sich pruefen, ob Breite plus Rand/Kipp auch ohne extremen Nachhall selektiv bleibt.
