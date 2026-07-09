# 1012 - MCM-Achsen Chartzonen-Typologie

Passive Verdichtung der aktiven Achsenfenster in Chart-/MCM-Typen.

## Typologie

| Typ | Anzahl | Welten | Bewegung | Return % | Range % | Druck | Rekopplung | Deutung |
|---|---:|---|---|---:|---:|---:|---:|---|
| konsolidierung_mit_rekopplung | 4 | SIDEWAYS_2024:2 | EXT_EXPANSION_2023:1 | NEG_STRESS_2023:1 | rekopplungs_uebergang:4 | -0.147674 | 1.395979 | 0.034026 | 0.012683 | Seitwaerts-/Ruhefenster traegt Rekopplung statt reiner Ruhe. |
| gerichtete_bewegung_mit_rekopplung | 3 | POS_EXPANSION_2023:2 | EXT_EXPANSION_2023:1 | rekopplungs_uebergang:3 | 1.297745 | 2.272131 | 0.078651 | 0.018255 | Richtung laeuft und koppelt im Feld wieder an. |
| gerichtete_bewegung_mit_bruch | 2 | EXT_EXPANSION_2023:1 | POS_EXPANSION_2023:1 | bewegungsbruch_zone:2 | 3.753607 | 6.769977 | 0.062284 | 0.01725 | Richtung laeuft, aber das MCM-Feld liest Bruch oder Umordnung. |
| konsolidierung_unter_druck | 2 | NEG_STRESS_2023:1 | SIDEWAYS_2024:1 | druck_uebergang:2 | -0.75293 | 0.932682 | 0.056907 | 0.025258 | Seitwaerts-/Ruhefenster traegt innere Druckspannung. |
| abverkauf_mit_bruch | 1 | NEG_STRESS_2024:1 | bewegungsbruch_zone:1 | -2.435145 | 3.987276 | 0.081516 | 0.020171 | Abverkauf wird als Bewegungsbruch oder Druckbruch gelesen. |
| abverkauf_mit_rekopplung | 1 | NEG_STRESS_2024:1 | rekopplungs_uebergang:1 | -4.359002 | 4.985541 | 0.070313 | 0.018908 | Abverkauf wird nicht nur als Fall gelesen, sondern mit Rekopplungsanteil getragen. |
| getragene_expansion | 1 | EXT_EXPANSION_2023:1 | offene_uebergangszone:1 | 5.183199 | 10.455764 | 0.024754 | 0.010769 | Expansion bleibt ueber das Fenster getragen. |
| konsolidierung_mit_bruchnaehe | 1 | POS_EXPANSION_2023:1 | bewegungsbruch_zone:1 | 0.299401 | 2.010265 | 0.036181 | 0.011746 | Konsolidierung zeigt Bruchnaehe oder gespannte Struktur. |

## Einzelzuordnung

| Typ | Welt | Paar | Ticks | Chartzone | MCM-Bewegung | Fenster % | Range % |
|---|---|---|---|---|---|---:|---:|
| gerichtete_bewegung_mit_rekopplung | EXT_EXPANSION_2023 | `183drjy->1t5bcxp` | 506-526 | `gerichtete_uebergangsbewegung` | `rekopplungs_uebergang` | 1.345291 | 3.318386 |
| konsolidierung_mit_rekopplung | EXT_EXPANSION_2023 | `1t5bcxp->183drjy` | 503-517 | `ruhige_konsolidierung` | `rekopplungs_uebergang` | -0.089767 | 0.897666 |
| getragene_expansion | EXT_EXPANSION_2023 | `02xikfk->1t5bcxp` | 394-660 | `expansion_getragen` | `offene_uebergangszone` | 5.183199 | 10.455764 |
| gerichtete_bewegung_mit_bruch | EXT_EXPANSION_2023 | `1t5bcxp->02xikfk` | 396-655 | `gerichtete_uebergangsbewegung` | `bewegungsbruch_zone` | 5.903399 | 10.375671 |
| konsolidierung_unter_druck | NEG_STRESS_2023 | `183drjy->1t5bcxp` | 802-816 | `ruhige_konsolidierung` | `druck_uebergang` | -0.683761 | 0.769231 |
| konsolidierung_mit_rekopplung | NEG_STRESS_2023 | `1t5bcxp->183drjy` | 771-815 | `ruhige_konsolidierung` | `rekopplungs_uebergang` | 0.128921 | 0.816502 |
| abverkauf_mit_rekopplung | NEG_STRESS_2024 | `02xikfk->1t5bcxp` | 700-977 | `abverkauf_getragen` | `rekopplungs_uebergang` | -4.359002 | 4.985541 |
| abverkauf_mit_bruch | NEG_STRESS_2024 | `1t5bcxp->02xikfk` | 760-975 | `abverkauf_getragen` | `bewegungsbruch_zone` | -2.435145 | 3.987276 |
| gerichtete_bewegung_mit_bruch | POS_EXPANSION_2023 | `02xikfk->1t5bcxp` | 228-356 | `gerichtete_uebergangsbewegung` | `bewegungsbruch_zone` | 1.603814 | 3.164283 |
| konsolidierung_mit_bruchnaehe | POS_EXPANSION_2023 | `1t5bcxp->02xikfk` | 235-355 | `konsolidierung_mit_spannung` | `bewegungsbruch_zone` | 0.299401 | 2.010265 |
| gerichtete_bewegung_mit_rekopplung | POS_EXPANSION_2023 | `183drjy->1t5bcxp` | 572-653 | `gerichtete_uebergangsbewegung` | `rekopplungs_uebergang` | 1.511226 | 2.115717 |
| gerichtete_bewegung_mit_rekopplung | POS_EXPANSION_2023 | `1t5bcxp->183drjy` | 571-651 | `gerichtete_uebergangsbewegung` | `rekopplungs_uebergang` | 1.036717 | 1.382289 |
| konsolidierung_mit_rekopplung | SIDEWAYS_2024 | `02xikfk->1t5bcxp` | 608-665 | `konsolidierung_mit_spannung` | `rekopplungs_uebergang` | 0.01536 | 2.979802 |
| konsolidierung_unter_druck | SIDEWAYS_2024 | `183drjy->1t5bcxp` | 920-934 | `ruhige_konsolidierung` | `druck_uebergang` | -0.8221 | 1.096134 |
| konsolidierung_mit_rekopplung | SIDEWAYS_2024 | `1t5bcxp->183drjy` | 917-927 | `ruhige_konsolidierung` | `rekopplungs_uebergang` | -0.645209 | 0.889944 |

## Befund

Die Achsenfenster zerfallen nicht in beliebige Chartstellen. Sie bilden wiederkehrende Typen: gerichtete Bewegung mit Rekopplung, gerichtete Bewegung mit Bruch, Konsolidierung unter Druck, Konsolidierung mit Rekopplung, getragene Expansion und Abverkauf mit Rekopplung oder Bruch.

Damit wird die bisherige Regimewechsel-Lesung konkreter: Das MCM-Feld reagiert nicht nur auf Richtung, sondern auf Uebergangsqualitaet. Entscheidend ist, ob ein Chartfenster Druck, Bruch, Rekopplung oder tragende Fortsetzung erzeugt.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob diese Typen ueber neue Welten wiederkehren oder ob neue Typen entstehen. Besonders wichtig ist die Frage, ob `gerichtete_bewegung_mit_rekopplung` und `abverkauf_mit_rekopplung` stabile MCM-Archetypen werden.
