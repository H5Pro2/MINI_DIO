# Synthetische Randdominanz - Topologische Bewegungsrollen

Passive Diagnose der Rollenbewegung aus den Preview-Uebergangspaaren. Die Rollen sind Auswertungssprache, keine Laufzeitregel.

## Rollenwechsel
- zentrum_stabil->zentrum_stabil: 30
- offene_variante->zentrum_stabil: 5
- offene_variante->offene_variante: 5
- zentrum_stabil->offene_variante: 3
- zentrum_stabil->spannungsrand_kippnaehe: 2
- spannungsrand_kippnaehe->zentrum_stabil: 1
- spannungsrand_kippnaehe->offene_variante: 1

## Bewegungswirkung
- bewegung_offen: 17
- spannungsnah_lauter: 12
- rekoppelnd_entlastend: 12
- oeffnend_belastend: 5
- spannungsnah: 1

## Dominante Weltfaerbung
- SYNTH_RAND_A: bewegung_offen=17, spannungsnah_lauter=12, rekoppelnd_entlastend=12, oeffnend_belastend=5, spannungsnah=1

## Befund
Die Randdominanz-Welt erzeugt mehr offene und spannungsnahe Bewegungen als die harmonische Welt, bleibt aber ueberwiegend in Zentrum und Rekopplungsnaehe organisiert. Ein dauerhafter Spannungsrand wird nicht dominant; Randlast wird bisher eher als oeffnende und rekoppelnde Bewegungsvarianz getragen.

Wie es weitergeht: Die Randdominanz-Phasenmatrix muss klaeren, in welchen Phasen die Randlast offen, rekoppelnd oder wirklich randnah gelesen wird.
