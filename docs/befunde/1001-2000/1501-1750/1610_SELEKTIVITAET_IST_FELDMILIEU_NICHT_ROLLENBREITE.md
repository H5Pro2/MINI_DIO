# Selektivitaet ist Feldmilieu, nicht Rollenbreite

Stand: 2026-07-06

## Grundfrage

Welche Bedingung laesst Offline-Feld-Reorganisation selektiv werden?

## Unterpruefung

Nach mehreren Real- und Synth-Gegenproben wurden drei Achsen getrennt:

1. Rollenbreite: 5 Rollen / 10 Kombinationen.
2. Nachhall: niedrig, mittel, hoch.
3. Weltmilieu: real, synthetisch harmonisch, synthetisch Rand/Kipp, synthetisch gedaempfte Randdominanz.

## Ergebnis

| Fall | Rollen | Kombinationen | Nachhall | Reaktion |
|---|---:|---:|---:|---|
| reale 5-Rollen-Fenster XRP/DOGE | 5 | 10 | ca. `0.14` | voll rekoppelt |
| synthetisch `BRUCH_RAND_A start0` | 3 | 3 | `0.7645` | voll rekoppelt |
| synthetisch `RAND_DOMINANZ_GEDAEMPFT start0` | 5 | 10 | `0.5175` | voll rekoppelt |
| synthetisch `SYNTH_RAND_KIPP start0` | 5 | 10 | `0.6412` | selektiv |

## Befund

Die Selektivitaet kann bisher nicht durch eine einzelne Achse erklaert werden:

- Nicht Rollenbreite allein: mehrere 5-Rollen-Fenster rekoppeln voll.
- Nicht Nachhall allein: ein 3-Rollen-Fenster mit sehr hohem Nachhall rekoppelt voll.
- Nicht synthetisch allein: eine gedaempfte synthetische 5-Rollen-Welt rekoppelt voll.

Selektivitaet erscheint bisher als Feldmilieu-Effekt. Sie entsteht wahrscheinlich dort, wo mehrere Bedingungen zusammenfallen:

- breite Rollennaehe,
- Rand-/Kippnaehe,
- hoher oder mittlerer Nachhall,
- gespannte Rollen im gemeinsamen Feld,
- spezifische Co-Touch-Qualitaet zwischen Rollen.

## Interpretation

MINI_DIO behandelt Offline-Reorganisation nicht als reine Mengenlogik. Das Feld liest offenbar nicht nur, wie viele Rollen vorhanden sind, sondern wie diese Rollen im Feldmilieu zueinander stehen.

Das ist ein wichtiger Schritt fuer die MCM-Forschung: Es spricht dafuer, dass Bedeutung im Feld nicht nur durch Symbolanzahl oder Signalstaerke entsteht, sondern durch Relation, Spannung, Nachhall und Rekopplungsqualitaet.

## Grenze

Die Befunde sind weiterhin diagnostisch. Die Selektivitaetsursache ist eingegrenzt, aber noch nicht isoliert.

## Wie es weitergeht

Als naechstes sollte `SYNTH_RAND_KIPP` systematisch variiert werden: gleiche Rollenbreite, aber veraenderte Randphase, veraenderte Co-Touch-Qualitaet oder veraenderte Strain-Verteilung. Ziel ist, die konkrete Feldmilieu-Komponente der selektiven Offline-Reorganisation zu isolieren.
