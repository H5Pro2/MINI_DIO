# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 83 | neutral | neutral:53;beruhigend:30 | 0.0072 | -0.0022 | 0.0008 | -0.0011 |
| ueberstabil_extrem_leise_scharf->ueberstabil_extrem_leise_scharf | 75 | neutral | neutral:75 | 0.0000 | -0.0001 | 0.0000 | -0.0000 |
| offen_suchend->offen_suchend | 37 | neutral | neutral:23;beruhigend:14 | 0.0095 | -0.0020 | 0.0012 | -0.0017 |
| offen_suchend->normale_weltspannung | 30 | beruhigend | beruhigend:15;neutral:15 | 0.0078 | -0.0030 | 0.0009 | -0.0012 |
| normale_weltspannung->offen_suchend | 25 | beruhigend | beruhigend:17;neutral:8 | 0.0076 | -0.0042 | 0.0012 | -0.0016 |
| randlastige_sinneslage->randlastige_sinneslage | 25 | beruhigend | beruhigend:25 | 0.0030 | -0.0390 | 0.0013 | -0.0019 |
| randlastige_sinneslage->offen_suchend | 23 | beruhigend | beruhigend:14;neutral:9 | 0.0083 | -0.0037 | 0.0012 | -0.0016 |
| offen_suchend->randlastige_sinneslage | 22 | beruhigend | beruhigend:20;neutral:2 | 0.0068 | -0.0102 | 0.0015 | -0.0021 |
| normale_weltspannung->ruhig_zentrumsnah | 20 | neutral | neutral:18;beruhigend:2 | 0.0065 | -0.0005 | 0.0005 | -0.0008 |
| normale_weltspannung->lauter_feldkontakt | 17 | beruhigend | beruhigend:9;neutral:8 | 0.0112 | -0.0038 | 0.0012 | -0.0017 |
| randlastige_sinneslage->normale_weltspannung | 17 | beruhigend | beruhigend:11;neutral:6 | 0.0094 | -0.0038 | 0.0009 | -0.0013 |
| ruhig_zentrumsnah->normale_weltspannung | 17 | neutral | neutral:15;beruhigend:2 | 0.0094 | -0.0006 | 0.0009 | -0.0012 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 15 | neutral | neutral:13;stabil_leicht:1;beruhigend:1 | 0.0057 | -0.0007 | 0.0005 | -0.0006 |
| normale_weltspannung->randlastige_sinneslage | 13 | beruhigend | beruhigend:12;neutral:1 | 0.0096 | -0.0088 | 0.0012 | -0.0017 |
| lauter_feldkontakt->normale_weltspannung | 9 | beruhigend | beruhigend:5;neutral:4 | 0.0078 | -0.0039 | 0.0010 | -0.0014 |
| lauter_feldkontakt->offen_suchend | 8 | beruhigend | beruhigend:5;neutral:3 | 0.0050 | -0.0044 | 0.0012 | -0.0016 |
| lauter_feldkontakt->lauter_feldkontakt | 7 | beruhigend | beruhigend:5;neutral:2 | 0.0107 | -0.0043 | 0.0013 | -0.0018 |
| ruhig_zentrumsnah->offen_suchend | 5 | beruhigend | beruhigend:3;neutral:2 | 0.0080 | -0.0040 | 0.0012 | -0.0016 |
| ruhig_zentrumsnah->randlastige_sinneslage | 5 | beruhigend | beruhigend:5 | 0.0050 | -0.0090 | 0.0012 | -0.0017 |
| lauter_feldkontakt->randlastige_sinneslage | 4 | beruhigend | beruhigend:4 | 0.0100 | -0.0100 | 0.0010 | -0.0014 |
| leise_duenn->ruhig_zentrumsnah | 4 | neutral | neutral:4 | 0.0037 | 0.0000 | 0.0006 | -0.0008 |
| offen_suchend->ruhig_zentrumsnah | 4 | neutral | neutral:3;beruhigend:1 | 0.0100 | -0.0013 | 0.0005 | -0.0007 |
| ruhig_zentrumsnah->lauter_feldkontakt | 4 | neutral | neutral:3;beruhigend:1 | 0.0100 | -0.0013 | 0.0011 | -0.0015 |
| randlastige_sinneslage->ruhig_zentrumsnah | 3 | neutral | neutral:3 | 0.0050 | 0.0000 | 0.0005 | -0.0007 |
| randlastige_sinneslage->ueberstabil_mit_randreiz | 3 | beruhigend | beruhigend:3 | 0.0000 | -0.0333 | 0.0006 | -0.0010 |
| ruhig_zentrumsnah->leise_duenn | 3 | neutral | neutral:3 | 0.0067 | 0.0000 | 0.0007 | -0.0010 |
| ueberstabil_extrem_leise_scharf->ueberstabil_mit_randreiz | 3 | beruhigend | beruhigend:3 | 0.0000 | -0.0267 | 0.0006 | -0.0010 |
| ueberstabil_mit_randreiz->randlastige_sinneslage | 3 | beruhigend | beruhigend:3 | 0.0000 | -0.0600 | 0.0011 | -0.0017 |
| ueberstabil_mit_randreiz->ueberstabil_extrem_leise_scharf | 3 | neutral | neutral:3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| leise_duenn->normale_weltspannung | 2 | neutral | neutral:2 | 0.0075 | 0.0000 | 0.0009 | -0.0012 |
| normale_weltspannung->leise_duenn | 2 | neutral | neutral:2 | 0.0025 | 0.0000 | 0.0008 | -0.0010 |
| offen_suchend->lauter_feldkontakt | 2 | beruhigend | beruhigend:2 | 0.0075 | -0.0050 | 0.0015 | -0.0020 |
| lauter_feldkontakt->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0250 | 0.0000 | 0.0007 | -0.0010 |
| leise_duenn->leise_duenn | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0006 | -0.0008 |
| offen_suchend->leise_duenn | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0007 | -0.0010 |
| ruhig_zentrumsnah->ueberstabil_extrem_leise_scharf | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0001 | -0.0001 |
| ruhig_zentrumsnah->ueberstabil_gemischt | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| ueberstabil_extrem_leise_scharf->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0000 | -0.0050 | 0.0002 | -0.0002 |
| ueberstabil_gemischt->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| ueberstabil_gemischt->ueberstabil_gemischt | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `83`
- `ueberstabil_extrem_leise_scharf->ueberstabil_extrem_leise_scharf`: `75`
- `offen_suchend->offen_suchend`: `37`
- `offen_suchend->normale_weltspannung`: `30`
- `normale_weltspannung->offen_suchend`: `25`
- `randlastige_sinneslage->randlastige_sinneslage`: `25`
- `randlastige_sinneslage->offen_suchend`: `23`
- `offen_suchend->randlastige_sinneslage`: `22`
- `normale_weltspannung->ruhig_zentrumsnah`: `20`
- `randlastige_sinneslage->normale_weltspannung`: `17`
- `normale_weltspannung->lauter_feldkontakt`: `17`
- `ruhig_zentrumsnah->normale_weltspannung`: `17`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
