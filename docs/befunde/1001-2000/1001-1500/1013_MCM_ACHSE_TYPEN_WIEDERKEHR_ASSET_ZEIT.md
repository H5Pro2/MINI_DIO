# 1013 - MCM-Achsentypen Wiederkehrpruefung

Passive Gegenprobe, ob die in 1012 gelesenen Chart-/MCM-Typen in weiteren Welten wiederkehren.

## Kurzbefund

- Referenztypen aus 1012: 8
- Gepruefte Achsenfenster: 17
- Bekannte Referenztypen: 10
- Neue oder erweiterte Typen: 7

## Typen

| Typ | Status | Anzahl | Quellen | Welten | Bewegung | Return % | Range % | Druck | Rekopplung | Deutung |
|---|---|---:|---|---|---|---:|---:|---:|---:|---|
| konsolidierung_mit_bruchnaehe | known_reference_type | 4 | ASSET_ZEIT:4 | BTC_2024_15M:1 <br> BTC_2024_5M:1 <br> SOL_2024_15M:1 <br> SOL_2024_5M:1 | offene_uebergangszone:4 | -0.378631 | 3.225641 | 0.054437 | 0.016644 | Konsolidierung zeigt Bruchnaehe oder gespannte Struktur. |
| getragene_expansion | known_reference_type | 3 | ASSET_ZEIT:3 | SOL_2024_1H:2 <br> KAS_2024_30M:1 | offene_uebergangszone:2 <br> bewegungsbruch_zone:1 | 37.631765 | 48.09308 | 0.099624 | 0.019943 | Expansion bleibt ueber das Fenster getragen. |
| abverkauf_mit_bruch | known_reference_type | 2 | ASSET_ZEIT:2 | SOL_2024_30M:2 | offene_uebergangszone:2 | -4.154253 | 5.655525 | 0.063338 | 0.01642 | Abverkauf wird als Bewegungsbruch oder Druckbruch gelesen. |
| konsolidierung_unter_druck | known_reference_type | 1 | ASSET_ZEIT:1 | BTC_2024_5M:1 | druck_uebergang:1 | 0.310162 | 2.863132 | 0.089113 | 0.010302 | Seitwaerts-/Ruhefenster traegt innere Druckspannung. |
| weite_volatilitaetszone | new_or_extended_type | 3 | ASSET_ZEIT:3 | BTC_2024_30M:2 <br> SOL_2024_15M:1 | offene_uebergangszone:2 <br> druck_uebergang:1 | 0.063656 | 14.243327 | 0.07438 | 0.013233 | Das Fenster traegt breite Bewegung ohne eindeutige Richtung. |
| gerichtete_uebergangsbewegung | new_or_extended_type | 2 | ASSET_ZEIT:2 | KAS_2024_30M:1 <br> SOL_2024_5M:1 | offene_uebergangszone:2 | 0.263176 | 2.351759 | 0.041639 | 0.012904 | Gerichtete Bewegung mit unspezifischer Uebergangsqualitaet. |
| rekopplung_nach_abverkauf | new_or_extended_type | 2 | ASSET_ZEIT:2 | BTC_2024_1H:2 | druck_uebergang:1 <br> offene_uebergangszone:1 | 72.160237 | 85.086081 | 0.097016 | 0.018237 | Nach einem Abverkauf entsteht ein lokales Rekopplungsfenster. |

## Einzelzuordnung

| Status | Typ | Quelle | Welt | Paar | Ticks | Chartzone | MCM-Bewegung | Fenster % | Range % |
|---|---|---|---|---|---|---|---|---:|---:|
| known_reference_type | abverkauf_mit_bruch | ASSET_ZEIT | SOL_2024_30M | `183drjy->1t5bcxp` | 1603-1721 | `abverkauf_getragen` | `offene_uebergangszone` | -3.229713 | 5.308841 |
| known_reference_type | abverkauf_mit_bruch | ASSET_ZEIT | SOL_2024_30M | `1t5bcxp->183drjy` | 1594-1724 | `abverkauf_getragen` | `offene_uebergangszone` | -5.078792 | 6.002208 |
| known_reference_type | getragene_expansion | ASSET_ZEIT | KAS_2024_30M | `183drjy->1t5bcxp` | 1528-1897 | `expansion_getragen` | `bewegungsbruch_zone` | 33.575069 | 39.063113 |
| known_reference_type | getragene_expansion | ASSET_ZEIT | SOL_2024_1H | `183drjy->1t5bcxp` | 929-1674 | `expansion_getragen` | `offene_uebergangszone` | 40.518749 | 52.613173 |
| known_reference_type | getragene_expansion | ASSET_ZEIT | SOL_2024_1H | `1t5bcxp->183drjy` | 933-1671 | `expansion_getragen` | `offene_uebergangszone` | 38.801476 | 52.602953 |
| known_reference_type | konsolidierung_mit_bruchnaehe | ASSET_ZEIT | BTC_2024_15M | `1t5bcxp->183drjy` | 1175-1195 | `ruhige_konsolidierung` | `offene_uebergangszone` | -0.844699 | 1.456743 |
| known_reference_type | konsolidierung_mit_bruchnaehe | ASSET_ZEIT | BTC_2024_5M | `1t5bcxp->183drjy` | 1313-1816 | `konsolidierung_mit_spannung` | `offene_uebergangszone` | 0.250338 | 2.862767 |
| known_reference_type | konsolidierung_mit_bruchnaehe | ASSET_ZEIT | SOL_2024_15M | `183drjy->1t5bcxp` | 1521-1698 | `konsolidierung_mit_spannung` | `offene_uebergangszone` | -0.845797 | 7.828778 |
| known_reference_type | konsolidierung_mit_bruchnaehe | ASSET_ZEIT | SOL_2024_5M | `1t5bcxp->183drjy` | 1979-1982 | `ruhige_konsolidierung` | `offene_uebergangszone` | -0.074365 | 0.754276 |
| known_reference_type | konsolidierung_unter_druck | ASSET_ZEIT | BTC_2024_5M | `183drjy->1t5bcxp` | 1314-1815 | `konsolidierung_mit_spannung` | `druck_uebergang` | 0.310162 | 2.863132 |
| new_or_extended_type | gerichtete_uebergangsbewegung | ASSET_ZEIT | KAS_2024_30M | `1t5bcxp->183drjy` | 1527-1589 | `gerichtete_uebergangsbewegung` | `offene_uebergangszone` | 1.634149 | 2.882044 |
| new_or_extended_type | gerichtete_uebergangsbewegung | ASSET_ZEIT | SOL_2024_5M | `183drjy->1t5bcxp` | 1980-1987 | `gerichtete_uebergangsbewegung` | `offene_uebergangszone` | -1.107797 | 1.821474 |
| new_or_extended_type | rekopplung_nach_abverkauf | ASSET_ZEIT | BTC_2024_1H | `183drjy->1t5bcxp` | 446-1767 | `rekopplung_nach_abverkauf` | `druck_uebergang` | 71.149405 | 85.091518 |
| new_or_extended_type | rekopplung_nach_abverkauf | ASSET_ZEIT | BTC_2024_1H | `1t5bcxp->183drjy` | 442-1766 | `rekopplung_nach_abverkauf` | `offene_uebergangszone` | 73.171069 | 85.080644 |
| new_or_extended_type | weite_volatilitaetszone | ASSET_ZEIT | BTC_2024_30M | `183drjy->1t5bcxp` | 605-1526 | `weite_volatilitaetszone` | `druck_uebergang` | 0.528746 | 12.480933 |
| new_or_extended_type | weite_volatilitaetszone | ASSET_ZEIT | BTC_2024_30M | `1t5bcxp->183drjy` | 604-1552 | `weite_volatilitaetszone` | `offene_uebergangszone` | 0.693814 | 12.464824 |
| new_or_extended_type | weite_volatilitaetszone | ASSET_ZEIT | SOL_2024_15M | `1t5bcxp->183drjy` | 1181-1944 | `weite_volatilitaetszone` | `offene_uebergangszone` | -1.031593 | 17.784225 |

## Befund

Die Pruefung trennt bekannte Referenztypen von neu entstehenden oder erweiterten Typen. Bekannte Typen sprechen fuer Wiederkehr der Feld-/Chart-Lesung. Neue Typen sind nicht automatisch Fehler; sie koennen echte Erweiterungen durch andere Weltspannung, Assetklasse oder Zeitebene sein.

## Wie es weitergeht

Als naechstes sollten die neuen oder erweiterten Typen getrennt gelesen werden: Welche entstehen durch andere Assetspannung, welche durch Zeitebene, und welche durch echte neue MCM-Uebergangsqualitaet.
