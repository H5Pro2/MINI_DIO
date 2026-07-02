# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 88 | neutral | neutral:68;beruhigend:20 | 0.0088 | -0.0023 | 0.0008 | -0.0011 |
| offen_suchend->offen_suchend | 52 | neutral | neutral:42;beruhigend:10 | 0.0081 | -0.0019 | 0.0014 | -0.0019 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 36 | neutral | neutral:35;beruhigend:1 | 0.0061 | -0.0003 | 0.0005 | -0.0008 |
| normale_weltspannung->offen_suchend | 34 | neutral | neutral:22;beruhigend:10;verschiebend:2 | 0.0129 | -0.0029 | 0.0012 | -0.0017 |
| offen_suchend->normale_weltspannung | 34 | neutral | neutral:20;beruhigend:14 | 0.0071 | -0.0041 | 0.0008 | -0.0012 |
| normale_weltspannung->ruhig_zentrumsnah | 30 | neutral | neutral:30 | 0.0077 | 0.0000 | 0.0005 | -0.0007 |
| ruhig_zentrumsnah->normale_weltspannung | 25 | neutral | neutral:19;beruhigend:5;verschiebend:1 | 0.0092 | -0.0020 | 0.0008 | -0.0011 |
| lauter_feldkontakt->normale_weltspannung | 23 | neutral | neutral:20;beruhigend:3 | 0.0078 | -0.0013 | 0.0008 | -0.0011 |
| normale_weltspannung->lauter_feldkontakt | 21 | neutral | neutral:16;beruhigend:5 | 0.0086 | -0.0024 | 0.0010 | -0.0015 |
| randlastige_sinneslage->normale_weltspannung | 21 | neutral | neutral:16;beruhigend:5 | 0.0067 | -0.0024 | 0.0008 | -0.0012 |
| normale_weltspannung->randlastige_sinneslage | 19 | beruhigend | beruhigend:19 | 0.0079 | -0.0142 | 0.0015 | -0.0021 |
| lauter_feldkontakt->lauter_feldkontakt | 13 | neutral | neutral:9;beruhigend:4 | 0.0115 | -0.0031 | 0.0010 | -0.0014 |
| randlastige_sinneslage->offen_suchend | 13 | neutral | neutral:10;beruhigend:3 | 0.0077 | -0.0023 | 0.0014 | -0.0018 |
| offen_suchend->randlastige_sinneslage | 12 | beruhigend | beruhigend:9;neutral:3 | 0.0050 | -0.0142 | 0.0015 | -0.0020 |
| lauter_feldkontakt->offen_suchend | 11 | neutral | neutral:6;beruhigend:5 | 0.0100 | -0.0045 | 0.0015 | -0.0020 |
| offen_suchend->lauter_feldkontakt | 11 | neutral | neutral:8;beruhigend:2;verschiebend:1 | 0.0127 | -0.0018 | 0.0015 | -0.0021 |
| randlastige_sinneslage->randlastige_sinneslage | 8 | beruhigend | beruhigend:7;neutral:1 | 0.0075 | -0.0125 | 0.0015 | -0.0020 |
| leise_duenn->normale_weltspannung | 7 | neutral | neutral:6;beruhigend:1 | 0.0086 | -0.0014 | 0.0007 | -0.0010 |
| leise_duenn->offen_suchend | 6 | neutral | neutral:4;beruhigend:2 | 0.0067 | -0.0033 | 0.0012 | -0.0016 |
| offen_suchend->leise_duenn | 6 | neutral | neutral:5;verschiebend:1 | 0.0083 | 0.0000 | 0.0008 | -0.0010 |
| ruhig_zentrumsnah->lauter_feldkontakt | 6 | neutral | neutral:4;beruhigend:2 | 0.0017 | -0.0033 | 0.0008 | -0.0012 |
| normale_weltspannung->leise_duenn | 5 | neutral | neutral:4;beruhigend:1 | 0.0120 | -0.0020 | 0.0007 | -0.0009 |
| randlastige_sinneslage->leise_duenn | 5 | neutral | neutral:4;beruhigend:1 | 0.0120 | -0.0020 | 0.0008 | -0.0011 |
| ruhig_zentrumsnah->offen_suchend | 4 | neutral | neutral:3;beruhigend:1 | 0.0075 | -0.0025 | 0.0011 | -0.0015 |
| lauter_feldkontakt->randlastige_sinneslage | 3 | beruhigend | beruhigend:3 | 0.0033 | -0.0133 | 0.0014 | -0.0020 |
| leise_scharf_duenn->normale_weltspannung | 3 | neutral | neutral:3 | 0.0200 | 0.0000 | 0.0008 | -0.0011 |
| normale_weltspannung->leise_scharf_duenn | 3 | neutral | neutral:3 | 0.0000 | 0.0000 | 0.0006 | -0.0008 |
| ruhig_zentrumsnah->randlastige_sinneslage | 3 | verschiebend | verschiebend:2;beruhigend:1 | 0.0267 | -0.0167 | 0.0012 | -0.0017 |
| lauter_feldkontakt->ruhig_zentrumsnah | 2 | neutral | neutral:2 | 0.0050 | 0.0000 | 0.0004 | -0.0005 |
| leise_duenn->leise_duenn | 2 | neutral | neutral:2 | 0.0050 | 0.0000 | 0.0008 | -0.0011 |
| leise_duenn->ruhig_zentrumsnah | 2 | neutral | neutral:2 | 0.0100 | 0.0000 | 0.0004 | -0.0005 |
| offen_suchend->ruhig_zentrumsnah | 2 | beruhigend | beruhigend:1;neutral:1 | 0.0100 | -0.0050 | 0.0007 | -0.0010 |
| leise_duenn->randlastige_sinneslage | 1 | neutral | neutral:1 | 0.0200 | 0.0000 | 0.0014 | -0.0018 |
| leise_scharf_duenn->leise_scharf_duenn | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0006 | -0.0007 |
| leise_scharf_duenn->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0008 | -0.0010 |
| offen_suchend->leise_scharf_duenn | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0005 | -0.0007 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `88`
- `offen_suchend->offen_suchend`: `52`
- `ruhig_zentrumsnah->ruhig_zentrumsnah`: `36`
- `normale_weltspannung->offen_suchend`: `34`
- `offen_suchend->normale_weltspannung`: `34`
- `normale_weltspannung->ruhig_zentrumsnah`: `30`
- `ruhig_zentrumsnah->normale_weltspannung`: `25`
- `lauter_feldkontakt->normale_weltspannung`: `23`
- `normale_weltspannung->lauter_feldkontakt`: `21`
- `randlastige_sinneslage->normale_weltspannung`: `21`
- `normale_weltspannung->randlastige_sinneslage`: `19`
- `lauter_feldkontakt->lauter_feldkontakt`: `13`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
