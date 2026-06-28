# 1010 - Achsenzonen gegen OHLCV-Chart

Passive Gegenlesung aktiver MCM-Achsenfenster gegen den echten Kerzenverlauf.

## Chartzonen

| Welt | Paar | Ticks | Chartzone | Vorher % | Fenster % | Nachher % | Range % | Bewegung |
|---|---|---|---|---:|---:|---:|---:|---|
| EXT_EXPANSION_2023 | `183drjy->1t5bcxp` | 506-526 | `gerichtete_uebergangsbewegung` | 0.360036 | 1.345291 | 0.530973 | 3.318386 | `rekopplungs_uebergang` |
| EXT_EXPANSION_2023 | `1t5bcxp->183drjy` | 503-517 | `ruhige_konsolidierung` | 0.269784 | -0.089767 | 1.705566 | 0.897666 | `rekopplungs_uebergang` |
| EXT_EXPANSION_2023 | `02xikfk->1t5bcxp` | 394-660 | `expansion_getragen` | 12.349398 | 5.183199 | 0.254669 | 10.455764 | `offene_uebergangszone` |
| EXT_EXPANSION_2023 | `1t5bcxp->02xikfk` | 396-655 | `gerichtete_uebergangsbewegung` | 12.012012 | 5.903399 | -0.759494 | 10.375671 | `bewegungsbruch_zone` |
| NEG_STRESS_2023 | `183drjy->1t5bcxp` | 802-816 | `ruhige_konsolidierung` | 0.3861 | -0.683761 | -0.516351 | 0.769231 | `druck_uebergang` |
| NEG_STRESS_2023 | `1t5bcxp->183drjy` | 771-815 | `ruhige_konsolidierung` | 0.085985 | 0.128921 | -0.858001 | 0.816502 | `rekopplungs_uebergang` |
| NEG_STRESS_2024 | `02xikfk->1t5bcxp` | 700-977 | `abverkauf_getragen` | 0.263073 | -4.359002 | -0.87346 | 4.985541 | `rekopplungs_uebergang` |
| NEG_STRESS_2024 | `1t5bcxp->02xikfk` | 760-975 | `abverkauf_getragen` | -1.389941 | -2.435145 | -0.477823 | 3.987276 | `bewegungsbruch_zone` |
| POS_EXPANSION_2023 | `02xikfk->1t5bcxp` | 228-356 | `gerichtete_uebergangsbewegung` | 1.140351 | 1.603814 | 1.023891 | 3.164283 | `bewegungsbruch_zone` |
| POS_EXPANSION_2023 | `1t5bcxp->02xikfk` | 235-355 | `konsolidierung_mit_spannung` | 1.080847 | 0.299401 | 1.023454 | 2.010265 | `bewegungsbruch_zone` |
| POS_EXPANSION_2023 | `183drjy->1t5bcxp` | 572-653 | `gerichtete_uebergangsbewegung` | -0.429738 | 1.511226 | -0.340136 | 2.115717 | `rekopplungs_uebergang` |
| POS_EXPANSION_2023 | `1t5bcxp->183drjy` | 571-651 | `gerichtete_uebergangsbewegung` | -0.643777 | 1.036717 | 0.34188 | 1.382289 | `rekopplungs_uebergang` |
| SIDEWAYS_2024 | `02xikfk->1t5bcxp` | 608-665 | `konsolidierung_mit_spannung` | 0.369999 | 0.01536 | 1.174754 | 2.979802 | `rekopplungs_uebergang` |
| SIDEWAYS_2024 | `183drjy->1t5bcxp` | 920-934 | `ruhige_konsolidierung` | -0.354244 | -0.8221 | -0.19416 | 1.096134 | `druck_uebergang` |
| SIDEWAYS_2024 | `1t5bcxp->183drjy` | 917-927 | `ruhige_konsolidierung` | -0.662983 | -0.645209 | -0.403075 | 0.889944 | `rekopplungs_uebergang` |

## Befund

Die aktiven MCM-Achsen liegen in realen Chartfenstern mit lokaler Uebergangsqualitaet. Das sind nicht nur abstrakte Feldzeichen, sondern zeitlich lokalisierbare Abschnitte im Kerzenverlauf.

Wichtig ist die Unterscheidung:

- Expansionen zeigen haeufig Bewegungsbruch oder Rekopplung im mittleren Verlauf.
- Negative Stresswelten zeigen Achsen eher spaet, in Druck- oder Rekopplungsfenstern.
- Sideways zeigt spaete, kleinere Druck-/Rekopplungsfenster.

## Wie es weitergeht

Als naechstes sollte fuer die wichtigsten Fenster eine kleine Chartgrafik erzeugt werden: Kerzenfenster plus markierte Achsenticks. Dann sieht man visuell, ob die Achse an Bruch, Reversal, Konsolidierung oder Fortsetzung sitzt.
