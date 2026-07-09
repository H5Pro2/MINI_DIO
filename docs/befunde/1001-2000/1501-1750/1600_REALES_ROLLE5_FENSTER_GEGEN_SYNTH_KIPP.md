# Reales 5-Rollen-Fenster Gegen Synthetisches Kippmilieu

Stand: 2026-07-06

## Grundfrage

Ist selektive Offline-Reorganisation eine Folge von 5 Rollen / 10 Kombinationen, oder liegt sie am speziellen Feldmilieu des synthetischen Rand-/Kippfensters?

## Unterpruefung

Verglichen werden zwei 5-Rollen-Fenster:

- `SYNTH_RAND_KIPP start0 size2000`
- `XRP_2024_5M start0 size2000`

Beide erzeugen 5 Rollen und 10 Sleep-Kombinationen. Damit ist die Rollenbreite formal gleich.

## Ergebnis

| Fenster | Rollen | Kombinationen | Rollen reaktiviert | Kombis voll | Kombis teilweise | Afterimage | Klasse |
|---|---:|---:|---:|---:|---:|---:|---|
| SYNTH_RAND_KIPP start0 | 5 | 10 | 4 / 5 | 6 / 10 | 4 / 10 | 0.6412 | selektiv_breit |
| XRP_2024_5M start0 | 5 | 10 | 5 / 5 | 10 / 10 | 0 / 10 | 0.1458 | voll_fokussiert |

## Lesung

5 Rollen / 10 Kombinationen reichen nicht aus, um selektive Offline-Reorganisation zu erklaeren.

Die entscheidende Trennung liegt aktuell eher im Feldmilieu:

- Das synthetische Rand-/Kippfenster hat deutlich hoeheren Nachhall und bleibt selektiv.
- Das reale XRP-Fenster hat dieselbe Rollenbreite, aber deutlich niedrigeren Nachhall und rekoppelt voll.

Kurz:

```text
Rollenbreite ist Material.
Feldmilieu entscheidet, ob die Offline-Rekopplung fokussiert oder selektiv wird.
```

## Bedeutung Fuer MINI_DIO

MINI_DIO behandelt Mehrrollennaehe nicht mechanisch nach Anzahl. Dieselbe Rollenbreite kann je nach Feldmilieu unterschiedlich reorganisiert werden.

Das spricht gegen eine einfache Schwellenlogik und fuer eine feldmilieuspezifische Offline-Reorganisation: Nachhall, Randnaehe, Strain-Verteilung und Co-Touch-Qualitaet muessen gemeinsam gelesen werden.

## Grenze

Die Stichprobe bleibt klein. Der Befund widerlegt aber die einfache Lesung:

```text
5 Rollen bedeuten automatisch selektive Reorganisation.
```

Diese Lesung ist nach dem XRP-Gegenbeispiel nicht haltbar.

## Quellen

- [1595 Sleep-Rollenbreiten-Karte](1595_SLEEP_ROLLENBREITEN_KARTE.md)
- [1597 XRP2024 2000 Rolle4 Sleep-Repro](1597_XRP2024_2000_ROLLE4_SLEEP_REPRO.md)
- [1599 XRP2024 2000 Rolle5 Sleep-Repro](1599_XRP2024_2000_ROLLE5_SLEEP_REPRO.md)

## Wie es weitergeht

Als naechstes sollten die beiden DOGE-5-Rollen-Fenster reproduziert werden. Wenn auch diese voll rekoppeln, liegt die bisherige Selektivitaet sehr wahrscheinlich nicht an Rollenbreite, sondern am synthetischen Rand-/Kippmilieu.
