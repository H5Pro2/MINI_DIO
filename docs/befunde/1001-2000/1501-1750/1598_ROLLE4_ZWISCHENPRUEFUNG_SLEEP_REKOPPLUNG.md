# 4-Rollen-Zwischenpruefung Der Sleep-Rekopplung

Stand: 2026-07-06

## Grundfrage

Kippt Offline-Feld-Reorganisation bereits bei 4 Rollen in selektive Rueckkopplung, oder bleibt sie noch voll rekoppelbar?

## Unterpruefung

Aus der Asset-Fenstersuche wurde `XRP_2024_5M start2000 size2000` gewaehlt, weil dieses Fenster zwischen den bisherigen Polen liegt:

- 3 Rollen / 3 Kombinationen: reale Uebergangsfenster, bisher voll rekoppelt.
- 5 Rollen / 10 Kombinationen: synthetisches Rand-/Kippfenster, bisher selektiv rekoppelt.
- 4 Rollen / 6 Kombinationen: gesuchte Zwischenklasse.

## Ergebnis

Der Real-Sleep-Real-Lauf `xrp2024_2000_start2000_role4_repro` zeigt:

| Merkmal | Wert |
|---|---:|
| Rollen im Sleep-Pool | 4 |
| Kombinationen | 6 |
| Rollen reaktiviert | 4 / 4 |
| Kombinationen voll reaktiviert | 6 / 6 |
| Kombinationen teilweise reaktiviert | 0 / 6 |
| Top-Syntax-Ueberlappung Real A/B | 1.0 |
| Top-Familien-Ueberlappung Real A/B | 1.0 |

Damit bleibt die 4-Rollen-Zwischenklasse voll fokussiert rekoppelbar.

## Lesung

Die aktuelle Rollenbreitenreihe lautet:

```text
3 Rollen / 3 Kombinationen -> voll fokussierte Rekopplung.
4 Rollen / 6 Kombinationen -> voll fokussierte Rekopplung.
5 Rollen / 10 Kombinationen -> selektive breite Reorganisation.
```

Der vorlaeufige Kipppunkt liegt daher nicht einfach bei Mehrrolligkeit. Entscheidend scheint zu sein, wann Rollenbreite, Kombinationenzahl und Strain-Verteilung eine zu breite Offline-Naehe erzeugen.

## Bedeutung Fuer MINI_DIO

MINI_DIO behandelt mehrere Feldrollen nicht automatisch als Rauschen. Bis 4 Rollen bleiben die Rollen in dieser Stichprobe klar genug, um offline voll rekoppelt zu werden.

Das synthetische 5-Rollen-Fenster ist anders: Es enthaelt mehr Rollen, mehr Kombinationen, mehr Strain-Rollen und deutlich hoeheren Nachhall. Dort wird Offline-Reorganisation selektiv.

## Grenze

Das ist eine kleine Stichprobe. Die Diagnose beweist keinen festen Schwellenwert. Sie liefert aber eine konkrete naechste Pruefachse:

```text
Ist selektive Offline-Reorganisation an 5+ Rollen,
an 2+ Strain-Rollen,
an hoeheren Nachhall
oder an die Kombination dieser Faktoren gebunden?
```

## Quellen

- [1595 Sleep-Rollenbreiten-Karte](1595_SLEEP_ROLLENBREITEN_KARTE.md)
- [1596 Rollenbreiten-Fenstersuche Assets 2000](1596_ROLLENBREITEN_FENSTERSUCHE_ASSETS_2000.md)
- [1597 XRP2024 2000 Rolle4 Sleep-Repro](1597_XRP2024_2000_ROLLE4_SLEEP_REPRO.md)
