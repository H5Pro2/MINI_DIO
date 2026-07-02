# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| ueberstabil_extrem_leise_scharf->ueberstabil_extrem_leise_scharf | 152 | neutral | neutral:152 | 0.0000 | 0.0000 | 0.0000 | -0.0000 |
| normale_weltspannung->normale_weltspannung | 108 | neutral | neutral:91;beruhigend:17 | 0.0075 | -0.0016 | 0.0008 | -0.0011 |
| offen_suchend->offen_suchend | 64 | neutral | neutral:48;beruhigend:16 | 0.0089 | -0.0025 | 0.0013 | -0.0017 |
| offen_suchend->normale_weltspannung | 59 | neutral | neutral:47;beruhigend:11;verschiebend:1 | 0.0081 | -0.0019 | 0.0008 | -0.0011 |
| randlastige_sinneslage->randlastige_sinneslage | 55 | beruhigend | beruhigend:54;verschiebend:1 | 0.0042 | -0.0445 | 0.0013 | -0.0019 |
| normale_weltspannung->offen_suchend | 49 | neutral | neutral:34;beruhigend:15 | 0.0084 | -0.0031 | 0.0013 | -0.0017 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 43 | neutral | neutral:40;beruhigend:2;stabil_leicht:1 | 0.0053 | -0.0007 | 0.0005 | -0.0007 |
| normale_weltspannung->randlastige_sinneslage | 42 | beruhigend | beruhigend:37;neutral:5 | 0.0064 | -0.0140 | 0.0014 | -0.0019 |
| normale_weltspannung->ruhig_zentrumsnah | 42 | neutral | neutral:40;beruhigend:2 | 0.0069 | -0.0005 | 0.0005 | -0.0007 |
| randlastige_sinneslage->normale_weltspannung | 42 | neutral | neutral:36;beruhigend:5;verschiebend:1 | 0.0076 | -0.0014 | 0.0008 | -0.0010 |
| randlastige_sinneslage->offen_suchend | 40 | neutral | neutral:32;beruhigend:8 | 0.0080 | -0.0020 | 0.0014 | -0.0019 |
| ruhig_zentrumsnah->normale_weltspannung | 39 | neutral | neutral:32;beruhigend:6;stabil_leicht:1 | 0.0087 | -0.0018 | 0.0008 | -0.0012 |
| normale_weltspannung->lauter_feldkontakt | 33 | neutral | neutral:25;beruhigend:8 | 0.0088 | -0.0024 | 0.0011 | -0.0016 |
| lauter_feldkontakt->normale_weltspannung | 30 | neutral | neutral:20;beruhigend:10 | 0.0093 | -0.0033 | 0.0008 | -0.0010 |
| offen_suchend->randlastige_sinneslage | 28 | beruhigend | beruhigend:22;neutral:6 | 0.0061 | -0.0129 | 0.0016 | -0.0022 |
| lauter_feldkontakt->lauter_feldkontakt | 15 | neutral | neutral:11;beruhigend:4 | 0.0127 | -0.0027 | 0.0012 | -0.0016 |
| ruhig_zentrumsnah->lauter_feldkontakt | 14 | neutral | neutral:12;beruhigend:2 | 0.0107 | -0.0014 | 0.0012 | -0.0016 |
| offen_suchend->lauter_feldkontakt | 13 | neutral | neutral:10;beruhigend:3 | 0.0046 | -0.0023 | 0.0014 | -0.0019 |
| lauter_feldkontakt->offen_suchend | 12 | neutral | neutral:9;beruhigend:2;verschiebend:1 | 0.0075 | -0.0025 | 0.0012 | -0.0016 |
| lauter_feldkontakt->randlastige_sinneslage | 12 | beruhigend | beruhigend:11;neutral:1 | 0.0092 | -0.0142 | 0.0015 | -0.0021 |
| ruhig_zentrumsnah->offen_suchend | 10 | neutral | neutral:8;beruhigend:2 | 0.0090 | -0.0020 | 0.0011 | -0.0016 |
| lauter_feldkontakt->ruhig_zentrumsnah | 9 | neutral | neutral:9 | 0.0122 | 0.0000 | 0.0004 | -0.0006 |
| offen_suchend->ruhig_zentrumsnah | 9 | neutral | neutral:9 | 0.0067 | 0.0000 | 0.0006 | -0.0008 |
| leise_duenn->ruhig_zentrumsnah | 8 | neutral | neutral:8 | 0.0063 | 0.0000 | 0.0005 | -0.0007 |
| ueberstabil_leise_scharf->ueberstabil_extrem_leise_scharf | 7 | neutral | neutral:7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| leise_duenn->offen_suchend | 6 | neutral | neutral:4;beruhigend:2 | 0.0067 | -0.0033 | 0.0011 | -0.0014 |
| normale_weltspannung->leise_duenn | 6 | neutral | neutral:6 | 0.0067 | 0.0000 | 0.0008 | -0.0011 |
| offen_suchend->leise_duenn | 6 | neutral | neutral:5;beruhigend:1 | 0.0050 | -0.0017 | 0.0009 | -0.0013 |
| ruhig_zentrumsnah->leise_duenn | 6 | neutral | neutral:4;beruhigend:2 | 0.0067 | -0.0033 | 0.0007 | -0.0010 |
| ruhig_zentrumsnah->randlastige_sinneslage | 6 | beruhigend | beruhigend:6 | 0.0100 | -0.0200 | 0.0014 | -0.0019 |
| randlastige_sinneslage->lauter_feldkontakt | 5 | neutral | neutral:3;verschiebend:1;beruhigend:1 | 0.0180 | -0.0020 | 0.0015 | -0.0022 |
| leise_duenn->normale_weltspannung | 4 | neutral | neutral:4 | 0.0125 | 0.0000 | 0.0007 | -0.0010 |
| ueberstabil_gemischt->ueberstabil_gemischt | 4 | neutral | neutral:4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| leise_duenn->leise_duenn | 3 | neutral | neutral:3 | 0.0000 | 0.0000 | 0.0010 | -0.0012 |
| randlastige_sinneslage->ueberstabil_leise_scharf | 3 | neutral | neutral:3 | 0.0000 | -0.0067 | 0.0001 | -0.0002 |
| ruhig_zentrumsnah->ueberstabil_gemischt | 3 | neutral | neutral:3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| ueberstabil_extrem_leise_scharf->randlastige_sinneslage | 3 | beruhigend | beruhigend:3 | 0.0000 | -0.0533 | 0.0013 | -0.0020 |
| ueberstabil_extrem_leise_scharf->ueberstabil_leise_scharf | 3 | neutral | neutral:3 | 0.0000 | -0.0033 | 0.0001 | -0.0002 |
| ueberstabil_gemischt->ruhig_zentrumsnah | 3 | neutral | neutral:3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| leise_duenn->leise_scharf_duenn | 2 | neutral | neutral:2 | 0.0000 | 0.0000 | 0.0006 | -0.0009 |
| leise_scharf_duenn->leise_duenn | 2 | neutral | neutral:2 | 0.0050 | 0.0000 | 0.0007 | -0.0009 |
| normale_weltspannung->leise_scharf_duenn | 2 | neutral | neutral:2 | 0.0100 | 0.0000 | 0.0005 | -0.0007 |
| randlastige_sinneslage->ruhig_zentrumsnah | 2 | neutral | neutral:2 | 0.0050 | 0.0000 | 0.0005 | -0.0008 |
| lauter_feldkontakt->leise_duenn | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0010 | -0.0013 |
| leise_duenn->randlastige_sinneslage | 1 | beruhigend | beruhigend:1 | 0.0000 | -0.0100 | 0.0008 | -0.0011 |
| leise_scharf_duenn->normale_weltspannung | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0004 | -0.0005 |
| leise_scharf_duenn->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0005 | -0.0006 |
| randlastige_sinneslage->ueberstabil_mit_randreiz | 1 | beruhigend | beruhigend:1 | 0.0000 | -0.0500 | 0.0009 | -0.0014 |
| ruhig_zentrumsnah->ueberstabil_leise_scharf | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0001 | -0.0002 |
| ueberstabil_extrem_leise_scharf->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0000 | -0.0100 | 0.0003 | -0.0005 |
| ueberstabil_mit_randreiz->randlastige_sinneslage | 1 | beruhigend | beruhigend:1 | 0.0000 | -0.0600 | 0.0011 | -0.0017 |

## Haeufigste Rohfolgen

- `ueberstabil_extrem_leise_scharf->ueberstabil_extrem_leise_scharf`: `152`
- `normale_weltspannung->normale_weltspannung`: `108`
- `offen_suchend->offen_suchend`: `64`
- `offen_suchend->normale_weltspannung`: `59`
- `randlastige_sinneslage->randlastige_sinneslage`: `55`
- `normale_weltspannung->offen_suchend`: `49`
- `ruhig_zentrumsnah->ruhig_zentrumsnah`: `43`
- `randlastige_sinneslage->normale_weltspannung`: `42`
- `normale_weltspannung->randlastige_sinneslage`: `42`
- `normale_weltspannung->ruhig_zentrumsnah`: `42`
- `randlastige_sinneslage->offen_suchend`: `40`
- `ruhig_zentrumsnah->normale_weltspannung`: `39`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
