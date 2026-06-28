# 1009 - Aktive Achsen und Chartzonen

Passive Diagnose, wo aktive MCM-Uebergangsachsen im Verlauf auftreten.

Diese Lesung nutzt vorhandene Ereignisse mit Weltname und Tickposition. Sie ist keine Handlungsschicht und kein Signal.

## Kurzbefund

- Ausgewertete aktive Achsenzonen: 15
- Welten mit aktiven Zonen: 5
- Dominante Bewegungsarten: rekopplungs_uebergang:8 | bewegungsbruch_zone:4 | druck_uebergang:2 | offene_uebergangszone:1

## Staerkste Achsenzonen

| Welt | Paar | Events | Tickbereich | Schwerpunkt | Bewegungsart | Druck | Rekopplung |
|---|---|---:|---|---|---|---:|---:|
| EXT_EXPANSION_2023 | `183drjy->1t5bcxp` | 4 | 506-526 | spaet_mitte | rekopplungs_uebergang | 0.040209 | 0.006682 |
| EXT_EXPANSION_2023 | `1t5bcxp->183drjy` | 4 | 503-517 | spaet_mitte | rekopplungs_uebergang | 0.05399 | 0.020894 |
| EXT_EXPANSION_2023 | `02xikfk->1t5bcxp` | 3 | 394-660 | frueh_mitte | offene_uebergangszone | 0.024754 | 0.010769 |
| EXT_EXPANSION_2023 | `1t5bcxp->02xikfk` | 3 | 396-655 | frueh_mitte | bewegungsbruch_zone | 0.050122 | 0.014597 |
| NEG_STRESS_2023 | `183drjy->1t5bcxp` | 2 | 802-816 | spaet | druck_uebergang | 0.072906 | 0.025184 |
| NEG_STRESS_2023 | `1t5bcxp->183drjy` | 2 | 771-815 | spaet | rekopplungs_uebergang | 0.041473 | 0.016539 |
| NEG_STRESS_2024 | `02xikfk->1t5bcxp` | 5 | 700-977 | spaet | rekopplungs_uebergang | 0.070313 | 0.018908 |
| NEG_STRESS_2024 | `1t5bcxp->02xikfk` | 3 | 760-975 | spaet | bewegungsbruch_zone | 0.081516 | 0.020171 |
| POS_EXPANSION_2023 | `02xikfk->1t5bcxp` | 6 | 228-356 | frueh_mitte | bewegungsbruch_zone | 0.074446 | 0.019902 |
| POS_EXPANSION_2023 | `1t5bcxp->02xikfk` | 5 | 235-355 | frueh_mitte | bewegungsbruch_zone | 0.036181 | 0.011746 |
| POS_EXPANSION_2023 | `183drjy->1t5bcxp` | 3 | 572-653 | spaet_mitte | rekopplungs_uebergang | 0.10574 | 0.025239 |
| POS_EXPANSION_2023 | `1t5bcxp->183drjy` | 3 | 571-651 | spaet_mitte | rekopplungs_uebergang | 0.090003 | 0.022843 |
| SIDEWAYS_2024 | `02xikfk->1t5bcxp` | 3 | 608-665 | spaet_mitte | rekopplungs_uebergang | 0.018927 | 0.007954 |
| SIDEWAYS_2024 | `183drjy->1t5bcxp` | 2 | 920-934 | spaet | druck_uebergang | 0.040909 | 0.025331 |
| SIDEWAYS_2024 | `1t5bcxp->183drjy` | 2 | 917-927 | spaet | rekopplungs_uebergang | 0.021714 | 0.005346 |

## Interpretation

Aktive Achsen liegen nicht gleichmaessig im gesamten Verlauf. Sie konzentrieren sich in bestimmten Tickfenstern und tragen dort meistens rekoppelnde Uebergaenge, Druckuebergaenge oder Bewegungsbruchzonen.

Fachlich bedeutet das: Die MCM-Achse ist wahrscheinlich keine reine Symbolbeziehung. Sie entsteht dort, wo der Chartverlauf eine lokale Uebergangsqualitaet liefert: Bruch, Druckwechsel, Rekopplung oder erneute Stabilisierung.

## Naechster konkreter Schritt

Die naechste Diagnose sollte die Tickfenster dieser Achsenzonen gegen die echten OHLCV-Kerzen lesen. Dann sehen wir direkt: laeuft der Chart dort in Expansion, Abverkauf, Seitwaertsphase, Reversal oder Konsolidierung.
