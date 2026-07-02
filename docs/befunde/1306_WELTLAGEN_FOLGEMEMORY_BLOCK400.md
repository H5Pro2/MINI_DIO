# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 64 | beruhigend | beruhigend:44;neutral:20 | 0.0073 | -0.0030 | 0.0009 | -0.0012 |
| ueberstabil_extrem_leise_scharf->ueberstabil_extrem_leise_scharf | 33 | neutral | neutral:33 | 0.0000 | -0.0001 | 0.0000 | -0.0000 |
| offen_suchend->offen_suchend | 29 | beruhigend | beruhigend:26;neutral:3 | 0.0091 | -0.0043 | 0.0013 | -0.0017 |
| offen_suchend->normale_weltspannung | 17 | beruhigend | beruhigend:10;neutral:7 | 0.0078 | -0.0028 | 0.0008 | -0.0012 |
| normale_weltspannung->offen_suchend | 15 | beruhigend | beruhigend:14;neutral:1 | 0.0080 | -0.0043 | 0.0012 | -0.0016 |
| ruhig_zentrumsnah->normale_weltspannung | 10 | beruhigend | beruhigend:8;neutral:2 | 0.0088 | -0.0030 | 0.0008 | -0.0011 |
| normale_weltspannung->randlastige_sinneslage | 8 | beruhigend | beruhigend:8 | 0.0091 | -0.0075 | 0.0013 | -0.0018 |
| normale_weltspannung->ruhig_zentrumsnah | 8 | neutral | neutral:7;beruhigend:1 | 0.0056 | -0.0006 | 0.0006 | -0.0008 |
| randlastige_sinneslage->offen_suchend | 8 | beruhigend | beruhigend:5;neutral:3 | 0.0069 | -0.0034 | 0.0012 | -0.0017 |
| normale_weltspannung->lauter_feldkontakt | 7 | neutral | neutral:5;beruhigend:2 | 0.0118 | -0.0007 | 0.0010 | -0.0014 |
| randlastige_sinneslage->randlastige_sinneslage | 6 | beruhigend | beruhigend:6 | 0.0029 | -0.0504 | 0.0012 | -0.0017 |
| lauter_feldkontakt->normale_weltspannung | 4 | beruhigend | beruhigend:3;neutral:1 | 0.0112 | -0.0037 | 0.0010 | -0.0015 |
| offen_suchend->randlastige_sinneslage | 4 | beruhigend | beruhigend:4 | 0.0037 | -0.0106 | 0.0015 | -0.0020 |
| randlastige_sinneslage->normale_weltspannung | 4 | beruhigend | beruhigend:4 | 0.0094 | -0.0044 | 0.0008 | -0.0011 |
| randlastige_sinneslage->ueberstabil_mit_randreiz | 3 | neutral | neutral:2;stabil_leicht:1 | 0.0000 | -0.0167 | 0.0003 | -0.0005 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 3 | neutral | neutral:3 | 0.0117 | 0.0000 | 0.0008 | -0.0011 |
| ueberstabil_extrem_leise_scharf->ueberstabil_mit_randreiz | 3 | beruhigend | beruhigend:2;neutral:1 | 0.0000 | -0.0333 | 0.0007 | -0.0011 |
| ueberstabil_mit_randreiz->randlastige_sinneslage | 3 | beruhigend | beruhigend:3 | 0.0000 | -0.0600 | 0.0011 | -0.0017 |
| ueberstabil_mit_randreiz->ueberstabil_extrem_leise_scharf | 3 | neutral | neutral:3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| lauter_feldkontakt->lauter_feldkontakt | 2 | neutral | neutral:1;beruhigend:1 | 0.0138 | -0.0037 | 0.0014 | -0.0020 |
| lauter_feldkontakt->offen_suchend | 2 | beruhigend | beruhigend:1;neutral:1 | 0.0025 | -0.0013 | 0.0011 | -0.0015 |
| offen_suchend->ruhig_zentrumsnah | 2 | neutral | neutral:2 | 0.0050 | 0.0000 | 0.0005 | -0.0007 |
| ruhig_zentrumsnah->offen_suchend | 2 | beruhigend | beruhigend:1;neutral:1 | 0.0075 | -0.0025 | 0.0013 | -0.0018 |
| leise_duenn->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0006 | -0.0008 |
| normale_weltspannung->leise_duenn | 1 | neutral | neutral:1 | 0.0025 | 0.0000 | 0.0007 | -0.0008 |
| ruhig_zentrumsnah->ueberstabil_extrem_leise_scharf | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0000 | -0.0000 |
| ueberstabil_extrem_leise_scharf->ueberstabil_gemischt | 1 | neutral | neutral:1 | 0.0000 | -0.0025 | 0.0001 | -0.0001 |
| ueberstabil_gemischt->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| ueberstabil_gemischt->ueberstabil_gemischt | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `64`
- `ueberstabil_extrem_leise_scharf->ueberstabil_extrem_leise_scharf`: `33`
- `offen_suchend->offen_suchend`: `29`
- `offen_suchend->normale_weltspannung`: `17`
- `normale_weltspannung->offen_suchend`: `15`
- `ruhig_zentrumsnah->normale_weltspannung`: `10`
- `normale_weltspannung->randlastige_sinneslage`: `8`
- `randlastige_sinneslage->offen_suchend`: `8`
- `normale_weltspannung->ruhig_zentrumsnah`: `8`
- `normale_weltspannung->lauter_feldkontakt`: `7`
- `randlastige_sinneslage->randlastige_sinneslage`: `6`
- `offen_suchend->randlastige_sinneslage`: `4`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
