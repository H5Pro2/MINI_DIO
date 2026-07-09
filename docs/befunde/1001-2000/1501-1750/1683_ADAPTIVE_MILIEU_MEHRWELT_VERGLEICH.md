# 1683 - Adaptive Milieu-Mehrweltpruefung

## Fragestellung

Geprueft wurde, ob die erweiterte adaptive Rekopplung mit Rollen- und Pfaderfahrung nur im BTC-Kontrolllauf sichtbar bleibt oder ob sie in weiteren Welten ebenfalls unterscheidbare Milieus bildet.

Untersuchte Welten:

- DOGE 2024 5m, 1000er Fenster
- XRP 2024 5m, 1000er Fenster
- PAXG 2024 5m, 2000er Fenster
- Stress-Gegenwelt, 1000er Fenster

Alle Laeufe wurden mit frischer Memory und `calibrated_relative` Sinnesmodus ausgefuehrt.

## Kompakter Befund

| Welt | Ticks | statische Rekopplung | adaptive Rekopplung | Rollenerfahrung | Pfaderfahrung |
|---|---:|---:|---:|---:|---:|
| DOGE | 994 | 0.685038 | 0.729084 | 0.577213 | 0.313380 |
| XRP | 994 | 0.676695 | 0.721852 | 0.643528 | 0.349346 |
| PAXG | 1994 | 0.700467 | 0.743298 | 0.628678 | 0.362149 |
| Stress | 994 | 0.686648 | 0.731231 | 0.574111 | 0.301056 |

Die adaptive Rekopplung liegt in allen vier Gegenwelten ueber der statischen Referenz. Damit ist die Schicht nicht BTC-spezifisch.

## Milieu-Verteilung

| Welt | offen | rollennah | pfadnah | Rolle und Pfad getragen | untrainiert |
|---|---:|---:|---:|---:|---:|
| DOGE | 412 | 243 | 42 | 285 | 12 |
| XRP | 383 | 257 | 19 | 329 | 6 |
| PAXG | 775 | 459 | 97 | 657 | 6 |
| Stress | 441 | 244 | 37 | 268 | 4 |

Wichtig ist nicht nur die Anhebung der Rekopplung, sondern die Aufteilung in Milieus:

- `milieu_offen` bleibt in allen Welten stark vertreten.
- `milieu_rollennah` und `milieu_rolle_und_pfad_getragen` treten ebenfalls stabil auf.
- `milieu_pfadnah` bleibt kleiner, aber nicht leer.
- `milieu_untrained` faellt nach wenigen Kontakten fast weg.

Damit wirkt die adaptive Rekopplung nicht wie ein starres globales Hochsetzen, sondern wie eine passive Lesung von Erfahrungsnaehe.

## Rollen-/Familienbefund

Die gleichen Symbolfamilien tauchen weltuebergreifend auf, aber nicht mit identischer Milieuqualitaet.

Beispiele:

- `field_stabil::dio_104t` erscheint in DOGE, XRP, PAXG und Stress, wechselt aber zwischen `milieu_rollennah` und `milieu_offen`.
- `field_stabil::dio_0m9z` kann in DOGE eher pfadnah, in XRP gemeinsam getragen und in Stress wieder pfadnah gelesen werden.
- PAXG bildet deutlich mehr Rollen-/Familienkombinationen als DOGE, XRP und Stress. Das spricht fuer eine breitere, ruhigere Leseflaeche, nicht fuer eine identische Kopie.

## Interpretation

Die adaptive Rekopplung liest zwei Ebenen:

```text
Diese Rolle kenne ich.
Dieser Uebergangspfad ist mir getragen oder noch offen.
```

Das ist fachlich wichtig, weil dadurch nicht jede wiederkehrende Symbolfamilie automatisch gleich behandelt wird. Die gleiche Syntax kann in einer Welt rollennah, in einer anderen offen oder pfadnah erscheinen.

Damit entsteht eine erste passive Milieulesung:

```text
Symbolfamilie
  -> Feldrolle
  -> Uebergangspfad
  -> Erfahrungsnaehe
  -> adaptive Rekopplungsqualitaet
```

## Grenze

Dieser Befund sagt noch nicht:

```text
MINI_DIO handelt besser.
MINI_DIO entscheidet.
MINI_DIO besitzt Strategie.
```

Sauberer ist:

```text
MINI_DIO kann gleiche oder aehnliche Feldzeichen in unterschiedlichen Weltmilieus verschieden rekoppeln.
```

Das ist eine Grundlage fuer spaetere organische Regulation, aber noch keine Handlungsschicht.

## Detailberichte

- [1683_ADAPTIVE_MILIEU_MEHRWELT_DOGE.md](1683_ADAPTIVE_MILIEU_MEHRWELT_DOGE.md)
- [1683_ADAPTIVE_MILIEU_MEHRWELT_XRP.md](1683_ADAPTIVE_MILIEU_MEHRWELT_XRP.md)
- [1683_ADAPTIVE_MILIEU_MEHRWELT_PAXG.md](1683_ADAPTIVE_MILIEU_MEHRWELT_PAXG.md)
- [1683_ADAPTIVE_MILIEU_MEHRWELT_STRESS.md](1683_ADAPTIVE_MILIEU_MEHRWELT_STRESS.md)
