# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 94 | neutral | neutral:73;beruhigend:21 | 0.0078 | -0.0022 | 0.0008 | -0.0011 |
| offen_suchend->offen_suchend | 72 | neutral | neutral:53;beruhigend:19 | 0.0090 | -0.0026 | 0.0013 | -0.0017 |
| offen_suchend->normale_weltspannung | 43 | neutral | neutral:34;beruhigend:9 | 0.0063 | -0.0021 | 0.0008 | -0.0012 |
| normale_weltspannung->offen_suchend | 36 | neutral | neutral:26;beruhigend:10 | 0.0067 | -0.0028 | 0.0013 | -0.0017 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 35 | neutral | neutral:32;beruhigend:3 | 0.0066 | -0.0009 | 0.0005 | -0.0007 |
| normale_weltspannung->randlastige_sinneslage | 34 | beruhigend | beruhigend:29;neutral:5 | 0.0076 | -0.0132 | 0.0014 | -0.0019 |
| normale_weltspannung->lauter_feldkontakt | 33 | neutral | neutral:26;beruhigend:7 | 0.0082 | -0.0021 | 0.0011 | -0.0015 |
| randlastige_sinneslage->offen_suchend | 33 | neutral | neutral:23;beruhigend:10 | 0.0079 | -0.0030 | 0.0013 | -0.0017 |
| ruhig_zentrumsnah->normale_weltspannung | 32 | neutral | neutral:28;beruhigend:3;stabil_leicht:1 | 0.0078 | -0.0013 | 0.0008 | -0.0011 |
| lauter_feldkontakt->normale_weltspannung | 29 | neutral | neutral:23;beruhigend:6 | 0.0100 | -0.0021 | 0.0008 | -0.0011 |
| randlastige_sinneslage->normale_weltspannung | 28 | neutral | neutral:24;beruhigend:4 | 0.0089 | -0.0014 | 0.0008 | -0.0011 |
| normale_weltspannung->ruhig_zentrumsnah | 27 | neutral | neutral:26;beruhigend:1 | 0.0078 | -0.0004 | 0.0005 | -0.0006 |
| offen_suchend->randlastige_sinneslage | 25 | beruhigend | beruhigend:21;neutral:4 | 0.0036 | -0.0120 | 0.0016 | -0.0022 |
| lauter_feldkontakt->offen_suchend | 21 | neutral | neutral:16;beruhigend:5 | 0.0057 | -0.0024 | 0.0012 | -0.0016 |
| offen_suchend->lauter_feldkontakt | 17 | beruhigend | beruhigend:9;neutral:7;verschiebend:1 | 0.0094 | -0.0059 | 0.0014 | -0.0020 |
| randlastige_sinneslage->randlastige_sinneslage | 16 | beruhigend | beruhigend:15;neutral:1 | 0.0056 | -0.0150 | 0.0015 | -0.0020 |
| lauter_feldkontakt->lauter_feldkontakt | 15 | neutral | neutral:9;beruhigend:6 | 0.0093 | -0.0040 | 0.0012 | -0.0017 |
| offen_suchend->ruhig_zentrumsnah | 13 | neutral | neutral:13 | 0.0069 | 0.0000 | 0.0005 | -0.0007 |
| ruhig_zentrumsnah->lauter_feldkontakt | 9 | neutral | neutral:9 | 0.0111 | 0.0000 | 0.0012 | -0.0017 |
| ruhig_zentrumsnah->offen_suchend | 9 | neutral | neutral:5;beruhigend:4 | 0.0089 | -0.0044 | 0.0011 | -0.0015 |
| lauter_feldkontakt->randlastige_sinneslage | 8 | beruhigend | beruhigend:8 | 0.0075 | -0.0175 | 0.0016 | -0.0022 |
| leise_duenn->ruhig_zentrumsnah | 8 | neutral | neutral:8 | 0.0063 | 0.0000 | 0.0005 | -0.0007 |
| lauter_feldkontakt->ruhig_zentrumsnah | 7 | neutral | neutral:7 | 0.0157 | 0.0000 | 0.0005 | -0.0006 |
| randlastige_sinneslage->lauter_feldkontakt | 7 | neutral | neutral:5;beruhigend:2 | 0.0129 | -0.0029 | 0.0014 | -0.0019 |
| normale_weltspannung->leise_duenn | 6 | neutral | neutral:6 | 0.0050 | 0.0000 | 0.0009 | -0.0011 |
| ruhig_zentrumsnah->leise_duenn | 6 | neutral | neutral:4;beruhigend:2 | 0.0067 | -0.0033 | 0.0007 | -0.0010 |
| leise_duenn->normale_weltspannung | 4 | neutral | neutral:3;beruhigend:1 | 0.0075 | -0.0025 | 0.0006 | -0.0008 |
| leise_duenn->offen_suchend | 4 | neutral | neutral:3;beruhigend:1 | 0.0075 | -0.0025 | 0.0014 | -0.0018 |
| offen_suchend->leise_duenn | 4 | neutral | neutral:4 | 0.0050 | 0.0000 | 0.0010 | -0.0013 |
| ruhig_zentrumsnah->randlastige_sinneslage | 4 | beruhigend | beruhigend:4 | 0.0150 | -0.0175 | 0.0014 | -0.0020 |
| leise_duenn->leise_duenn | 3 | neutral | neutral:3 | 0.0000 | 0.0000 | 0.0010 | -0.0012 |
| leise_duenn->leise_scharf_duenn | 2 | neutral | neutral:2 | 0.0000 | 0.0000 | 0.0006 | -0.0009 |
| leise_scharf_duenn->leise_duenn | 2 | neutral | neutral:2 | 0.0050 | 0.0000 | 0.0007 | -0.0009 |
| normale_weltspannung->leise_scharf_duenn | 2 | neutral | neutral:2 | 0.0100 | 0.0000 | 0.0005 | -0.0007 |
| lauter_feldkontakt->leise_duenn | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0010 | -0.0013 |
| leise_duenn->lauter_feldkontakt | 1 | neutral | neutral:1 | 0.0300 | 0.0000 | 0.0022 | -0.0030 |
| leise_scharf_duenn->normale_weltspannung | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0004 | -0.0005 |
| leise_scharf_duenn->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0005 | -0.0006 |
| randlastige_sinneslage->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0006 | -0.0008 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `94`
- `offen_suchend->offen_suchend`: `72`
- `offen_suchend->normale_weltspannung`: `43`
- `normale_weltspannung->offen_suchend`: `36`
- `ruhig_zentrumsnah->ruhig_zentrumsnah`: `35`
- `normale_weltspannung->randlastige_sinneslage`: `34`
- `randlastige_sinneslage->offen_suchend`: `33`
- `normale_weltspannung->lauter_feldkontakt`: `33`
- `ruhig_zentrumsnah->normale_weltspannung`: `32`
- `lauter_feldkontakt->normale_weltspannung`: `29`
- `randlastige_sinneslage->normale_weltspannung`: `28`
- `normale_weltspannung->ruhig_zentrumsnah`: `27`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
