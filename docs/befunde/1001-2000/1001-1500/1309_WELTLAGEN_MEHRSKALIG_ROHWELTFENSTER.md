# Mehrskalige Weltlagen-Folgen Rohweltfenster

Diese Diagnose liest skalenabhaengige Weltlagen-Folgen gegen konkrete Rohweltfenster zurueck.

Ziel:

```text
Welche Weltbewegung macht eine kurze neutrale Lage
zu einer laenger beruhigenden Feldphase?
```

## Verdichtung nach Folge und Skala

| Lagefolge | Skala | Fenster | Rohklasse | Bewegung % | Range % | Hoeren | Sicht | Felddruck |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 100 | 108 | gemischte_rohwelt | -0.1018 | 0.2741 | 0.4185 | 0.6687 | 0.1055 |
| normale_weltspannung->normale_weltspannung | 200 | 83 | gemischte_rohwelt | -0.0375 | 0.2432 | 0.4145 | 0.6687 | 0.1048 |
| normale_weltspannung->normale_weltspannung | 400 | 64 | gemischte_rohwelt | 0.0763 | 0.2619 | 0.4172 | 0.6663 | 0.1055 |
| offen_suchend->offen_suchend | 100 | 64 | gemischte_rohwelt | -0.9821 | 0.4703 | 0.4144 | 0.6308 | 0.1064 |
| offen_suchend->normale_weltspannung | 100 | 59 | gemischte_rohwelt | 0.4169 | 0.3015 | 0.4028 | 0.6594 | 0.1025 |
| normale_weltspannung->offen_suchend | 100 | 49 | gemischte_rohwelt | -0.0049 | 0.3600 | 0.4220 | 0.6334 | 0.1079 |
| randlastige_sinneslage->normale_weltspannung | 100 | 42 | gemischte_rohwelt | 0.3105 | 0.3011 | 0.4097 | 0.6681 | 0.1036 |
| randlastige_sinneslage->offen_suchend | 100 | 40 | gemischte_rohwelt | 0.3329 | 0.5639 | 0.4115 | 0.6224 | 0.1060 |
| ruhig_zentrumsnah->normale_weltspannung | 100 | 39 | gemischte_rohwelt | -0.1410 | 0.2218 | 0.4183 | 0.6727 | 0.1058 |
| offen_suchend->offen_suchend | 200 | 37 | gemischte_rohwelt | -0.6601 | 0.4999 | 0.4109 | 0.6304 | 0.1055 |
| normale_weltspannung->lauter_feldkontakt | 100 | 33 | gemischte_rohwelt | -0.8301 | 0.2574 | 0.4882 | 0.6624 | 0.1210 |
| lauter_feldkontakt->normale_weltspannung | 100 | 30 | gemischte_rohwelt | 0.4478 | 0.2250 | 0.4220 | 0.6700 | 0.1066 |
| offen_suchend->normale_weltspannung | 200 | 30 | gemischte_rohwelt | 0.9748 | 0.3040 | 0.4104 | 0.6600 | 0.1040 |
| offen_suchend->offen_suchend | 400 | 29 | bewegungsreiche_rohwelt | -0.0774 | 0.4985 | 0.4201 | 0.6309 | 0.1074 |
| normale_weltspannung->offen_suchend | 200 | 25 | bewegungsreiche_rohwelt | -0.9774 | 0.4000 | 0.4261 | 0.6408 | 0.1084 |
| randlastige_sinneslage->offen_suchend | 200 | 23 | gemischte_rohwelt | -0.3497 | 0.4759 | 0.4141 | 0.6343 | 0.1059 |
| normale_weltspannung->lauter_feldkontakt | 200 | 17 | gemischte_rohwelt | -1.1646 | 0.2388 | 0.4782 | 0.6592 | 0.1188 |
| offen_suchend->normale_weltspannung | 400 | 17 | gemischte_rohwelt | 1.2567 | 0.2622 | 0.4073 | 0.6632 | 0.1032 |
| randlastige_sinneslage->normale_weltspannung | 200 | 17 | gemischte_rohwelt | 0.7168 | 0.2816 | 0.4146 | 0.6626 | 0.1049 |
| ruhig_zentrumsnah->normale_weltspannung | 200 | 17 | gemischte_rohwelt | -0.4434 | 0.2158 | 0.4291 | 0.6705 | 0.1091 |
| lauter_feldkontakt->lauter_feldkontakt | 100 | 15 | laute_oder_druckvolle_rohwelt | 0.0217 | 0.2149 | 0.5079 | 0.6675 | 0.1254 |
| normale_weltspannung->offen_suchend | 400 | 15 | bewegungsreiche_rohwelt | -0.8201 | 0.4231 | 0.4294 | 0.6369 | 0.1090 |
| offen_suchend->lauter_feldkontakt | 100 | 13 | gemischte_rohwelt | 1.2305 | 0.3561 | 0.4852 | 0.6386 | 0.1205 |
| lauter_feldkontakt->offen_suchend | 100 | 12 | bewegungsreiche_rohwelt | 1.0478 | 0.5174 | 0.4018 | 0.6280 | 0.1040 |
| ruhig_zentrumsnah->normale_weltspannung | 400 | 10 | gemischte_rohwelt | -3.4739 | 0.2071 | 0.4001 | 0.6656 | 0.1032 |
| ruhig_zentrumsnah->offen_suchend | 100 | 10 | gemischte_rohwelt | -1.7492 | 0.3551 | 0.4426 | 0.6579 | 0.1111 |
| lauter_feldkontakt->normale_weltspannung | 200 | 9 | gemischte_rohwelt | 0.9439 | 0.2745 | 0.4240 | 0.6649 | 0.1069 |
| lauter_feldkontakt->offen_suchend | 200 | 8 | gemischte_rohwelt | 0.2385 | 0.3848 | 0.4122 | 0.6385 | 0.1051 |
| randlastige_sinneslage->offen_suchend | 400 | 8 | bewegungsreiche_rohwelt | -2.2959 | 0.5114 | 0.4149 | 0.6316 | 0.1062 |
| lauter_feldkontakt->lauter_feldkontakt | 200 | 7 | laute_oder_druckvolle_rohwelt | -0.4138 | 0.1648 | 0.5207 | 0.6732 | 0.1288 |
| normale_weltspannung->lauter_feldkontakt | 400 | 7 | gemischte_rohwelt | -0.8085 | 0.2085 | 0.4740 | 0.6708 | 0.1178 |
| ruhig_zentrumsnah->offen_suchend | 200 | 5 | gemischte_rohwelt | -1.3841 | 0.2104 | 0.4198 | 0.6476 | 0.1081 |
| lauter_feldkontakt->normale_weltspannung | 400 | 4 | bewegungsreiche_rohwelt | 2.3636 | 0.3592 | 0.4318 | 0.6644 | 0.1085 |
| randlastige_sinneslage->normale_weltspannung | 400 | 4 | gemischte_rohwelt | -2.9826 | 0.3007 | 0.4010 | 0.6636 | 0.1017 |
| randlastige_sinneslage->ueberstabil_mit_randreiz | 200 | 3 | bewegungsreiche_rohwelt | 2.0976 | 1.1992 | 0.2000 | 0.8258 | 0.0568 |
| randlastige_sinneslage->ueberstabil_mit_randreiz | 400 | 3 | bewegungsreiche_rohwelt | 8.1828 | 0.7057 | 0.1096 | 0.8335 | 0.0354 |
| lauter_feldkontakt->lauter_feldkontakt | 400 | 2 | laute_oder_druckvolle_rohwelt | -0.3567 | 0.0558 | 0.5569 | 0.6753 | 0.1375 |
| lauter_feldkontakt->offen_suchend | 400 | 2 | bewegungsreiche_rohwelt | -1.5619 | 0.3615 | 0.4348 | 0.6484 | 0.1098 |
| offen_suchend->lauter_feldkontakt | 200 | 2 | gemischte_rohwelt | 0.4984 | 0.3495 | 0.4638 | 0.6312 | 0.1163 |
| ruhig_zentrumsnah->offen_suchend | 400 | 2 | gemischte_rohwelt | -0.1444 | 0.1551 | 0.4466 | 0.6539 | 0.1138 |

## Bewertung

Skalenabhaengige Folgen sind nicht beliebig.

Sie treten dort auf, wo Rohwelt, Hoeren, Sicht und Felddruck ueber Zeit anders getragen werden als im kurzen Einzelblock.

Damit wird der Unterschied zwischen kurzer Lagebewegung und laengerer Feldphase konkreter ruecklesbar.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.
