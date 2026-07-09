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
| normale_weltspannung->normale_weltspannung | 100 | 88 | gemischte_rohwelt | 0.2092 | 0.2364 | 0.4173 | 0.6717 | 0.1051 |
| normale_weltspannung->normale_weltspannung | 200 | 72 | gemischte_rohwelt | 0.8606 | 0.2378 | 0.4189 | 0.6715 | 0.1055 |
| offen_suchend->offen_suchend | 100 | 52 | gemischte_rohwelt | 0.5314 | 0.5743 | 0.4160 | 0.6244 | 0.1068 |
| offen_suchend->offen_suchend | 200 | 43 | gemischte_rohwelt | 0.2904 | 0.5045 | 0.4154 | 0.6250 | 0.1065 |
| normale_weltspannung->normale_weltspannung | 400 | 38 | gemischte_rohwelt | 0.8091 | 0.2275 | 0.4184 | 0.6698 | 0.1055 |
| normale_weltspannung->offen_suchend | 100 | 34 | gemischte_rohwelt | 0.5917 | 0.3635 | 0.4261 | 0.6378 | 0.1084 |
| offen_suchend->normale_weltspannung | 100 | 34 | gemischte_rohwelt | -0.2187 | 0.2466 | 0.4091 | 0.6646 | 0.1034 |
| ruhig_zentrumsnah->normale_weltspannung | 100 | 25 | gemischte_rohwelt | 0.0108 | 0.1770 | 0.4102 | 0.6692 | 0.1042 |
| lauter_feldkontakt->normale_weltspannung | 100 | 23 | gemischte_rohwelt | 0.4159 | 0.2906 | 0.4245 | 0.6691 | 0.1071 |
| offen_suchend->normale_weltspannung | 200 | 22 | gemischte_rohwelt | -0.4956 | 0.2791 | 0.4074 | 0.6633 | 0.1031 |
| normale_weltspannung->lauter_feldkontakt | 100 | 21 | gemischte_rohwelt | 0.6880 | 0.2714 | 0.4785 | 0.6657 | 0.1186 |
| randlastige_sinneslage->normale_weltspannung | 100 | 21 | gemischte_rohwelt | 0.1717 | 0.2607 | 0.4140 | 0.6655 | 0.1043 |
| normale_weltspannung->offen_suchend | 200 | 19 | gemischte_rohwelt | 0.5650 | 0.3820 | 0.4260 | 0.6380 | 0.1085 |
| offen_suchend->offen_suchend | 400 | 19 | bewegungsreiche_rohwelt | 1.8666 | 0.5131 | 0.4193 | 0.6328 | 0.1069 |
| offen_suchend->normale_weltspannung | 400 | 16 | gemischte_rohwelt | -0.0142 | 0.2725 | 0.4085 | 0.6625 | 0.1035 |
| lauter_feldkontakt->lauter_feldkontakt | 100 | 13 | gemischte_rohwelt | -0.2448 | 0.1649 | 0.4927 | 0.6794 | 0.1215 |
| normale_weltspannung->offen_suchend | 400 | 13 | bewegungsreiche_rohwelt | -1.3008 | 0.3265 | 0.4137 | 0.6349 | 0.1060 |
| randlastige_sinneslage->offen_suchend | 100 | 13 | gemischte_rohwelt | 0.5586 | 0.3873 | 0.4262 | 0.6369 | 0.1085 |
| lauter_feldkontakt->offen_suchend | 100 | 11 | gemischte_rohwelt | 0.8871 | 0.4442 | 0.4095 | 0.6117 | 0.1069 |
| lauter_feldkontakt->normale_weltspannung | 200 | 7 | gemischte_rohwelt | 0.3918 | 0.2153 | 0.4447 | 0.6733 | 0.1113 |
| leise_duenn->normale_weltspannung | 100 | 7 | gemischte_rohwelt | 0.3112 | 0.1635 | 0.4174 | 0.6732 | 0.1049 |
| normale_weltspannung->lauter_feldkontakt | 200 | 7 | gemischte_rohwelt | 1.0517 | 0.2892 | 0.4785 | 0.6631 | 0.1188 |
| randlastige_sinneslage->normale_weltspannung | 200 | 7 | gemischte_rohwelt | 0.0129 | 0.2522 | 0.4066 | 0.6540 | 0.1037 |
| ruhig_zentrumsnah->normale_weltspannung | 200 | 7 | gemischte_rohwelt | -0.6883 | 0.1510 | 0.3988 | 0.6749 | 0.1023 |
| randlastige_sinneslage->offen_suchend | 200 | 6 | bewegungsreiche_rohwelt | -1.2684 | 0.3492 | 0.4120 | 0.6453 | 0.1048 |
| ruhig_zentrumsnah->lauter_feldkontakt | 100 | 6 | gemischte_rohwelt | 0.8224 | 0.1628 | 0.4784 | 0.6890 | 0.1181 |
| normale_weltspannung->lauter_feldkontakt | 400 | 5 | bewegungsreiche_rohwelt | 4.2144 | 0.3185 | 0.4738 | 0.6624 | 0.1179 |
| ruhig_zentrumsnah->normale_weltspannung | 400 | 5 | gemischte_rohwelt | -0.8200 | 0.0964 | 0.3897 | 0.6762 | 0.1005 |
| lauter_feldkontakt->lauter_feldkontakt | 200 | 3 | bewegungsreiche_rohwelt | 3.8089 | 0.2962 | 0.4909 | 0.6797 | 0.1207 |
| lauter_feldkontakt->normale_weltspannung | 400 | 3 | gemischte_rohwelt | 0.7399 | 0.1924 | 0.4373 | 0.6653 | 0.1095 |
| lauter_feldkontakt->offen_suchend | 200 | 3 | gemischte_rohwelt | 1.3135 | 0.4718 | 0.4451 | 0.6358 | 0.1128 |
| lauter_feldkontakt->offen_suchend | 400 | 3 | bewegungsreiche_rohwelt | 3.1913 | 0.5648 | 0.4367 | 0.6365 | 0.1112 |
| leise_duenn->normale_weltspannung | 200 | 3 | gemischte_rohwelt | -0.8169 | 0.1600 | 0.3994 | 0.6620 | 0.1013 |
| offen_suchend->ruhig_zentrumsnah | 100 | 2 | gemischte_rohwelt | 1.6603 | 0.2204 | 0.3897 | 0.6833 | 0.0982 |
| randlastige_sinneslage->normale_weltspannung | 400 | 2 | gemischte_rohwelt | -1.7831 | 0.1660 | 0.4365 | 0.6717 | 0.1093 |
| randlastige_sinneslage->offen_suchend | 400 | 2 | bewegungsreiche_rohwelt | 8.9596 | 0.5654 | 0.4049 | 0.6225 | 0.1046 |
| ruhig_zentrumsnah->lauter_feldkontakt | 200 | 2 | gemischte_rohwelt | -0.1190 | 0.0902 | 0.4695 | 0.7018 | 0.1160 |
| lauter_feldkontakt->lauter_feldkontakt | 400 | 1 | gemischte_rohwelt | 0.8372 | 0.1068 | 0.4985 | 0.6840 | 0.1220 |
| offen_suchend->ruhig_zentrumsnah | 200 | 1 | gemischte_rohwelt | 0.8065 | 0.2199 | 0.3574 | 0.6758 | 0.0928 |
| ruhig_zentrumsnah->lauter_feldkontakt | 400 | 1 | gemischte_rohwelt | 0.6077 | 0.1030 | 0.4653 | 0.7014 | 0.1154 |

## Bewertung

Skalenabhaengige Folgen sind nicht beliebig.

Sie treten dort auf, wo Rohwelt, Hoeren, Sicht und Felddruck ueber Zeit anders getragen werden als im kurzen Einzelblock.

Damit wird der Unterschied zwischen kurzer Lagebewegung und laengerer Feldphase konkreter ruecklesbar.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.

Wie es weitergeht: Als naechstes sollten die Rohklassen der skalenabhaengigen Folgen mit stabil neutralen und stabil beruhigenden Folgen verglichen werden.
