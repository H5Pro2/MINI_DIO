# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 34 | beruhigend | beruhigend:26;neutral:8 | 0.0070 | -0.0035 | 0.0008 | -0.0012 |
| normale_weltspannung->offen_suchend | 10 | beruhigend | beruhigend:9;neutral:1 | 0.0060 | -0.0040 | 0.0012 | -0.0016 |
| offen_suchend->normale_weltspannung | 8 | beruhigend | beruhigend:4;neutral:4 | 0.0075 | -0.0019 | 0.0008 | -0.0011 |
| offen_suchend->offen_suchend | 7 | beruhigend | beruhigend:7 | 0.0086 | -0.0032 | 0.0012 | -0.0017 |
| lauter_feldkontakt->lauter_feldkontakt | 4 | beruhigend | beruhigend:3;neutral:1 | 0.0069 | -0.0044 | 0.0008 | -0.0012 |
| lauter_feldkontakt->normale_weltspannung | 4 | beruhigend | beruhigend:2;neutral:2 | 0.0063 | -0.0019 | 0.0008 | -0.0011 |
| normale_weltspannung->lauter_feldkontakt | 4 | neutral | neutral:3;beruhigend:1 | 0.0088 | -0.0006 | 0.0008 | -0.0011 |
| normale_weltspannung->randlastige_sinneslage | 4 | beruhigend | beruhigend:4 | 0.0063 | -0.0138 | 0.0012 | -0.0017 |
| randlastige_sinneslage->normale_weltspannung | 4 | beruhigend | beruhigend:4 | 0.0081 | -0.0044 | 0.0009 | -0.0013 |
| offen_suchend->randlastige_sinneslage | 3 | beruhigend | beruhigend:3 | 0.0075 | -0.0092 | 0.0015 | -0.0021 |
| lauter_feldkontakt->offen_suchend | 2 | beruhigend | beruhigend:2 | 0.0025 | -0.0025 | 0.0011 | -0.0015 |
| randlastige_sinneslage->offen_suchend | 2 | beruhigend | beruhigend:2 | 0.0050 | -0.0037 | 0.0013 | -0.0017 |
| randlastige_sinneslage->randlastige_sinneslage | 2 | beruhigend | beruhigend:2 | 0.0050 | -0.0088 | 0.0010 | -0.0013 |
| lauter_feldkontakt->leise_duenn | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0006 | -0.0008 |
| leise_duenn->lauter_feldkontakt | 1 | beruhigend | beruhigend:1 | 0.0000 | -0.0100 | 0.0008 | -0.0012 |
| leise_duenn->leise_duenn | 1 | beruhigend | beruhigend:1 | 0.0025 | -0.0025 | 0.0008 | -0.0010 |
| leise_duenn->normale_weltspannung | 1 | beruhigend | beruhigend:1 | 0.0075 | -0.0025 | 0.0009 | -0.0012 |
| normale_weltspannung->leise_duenn | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0007 | -0.0010 |
| normale_weltspannung->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0150 | 0.0000 | 0.0005 | -0.0006 |
| randlastige_sinneslage->lauter_feldkontakt | 1 | beruhigend | beruhigend:1 | 0.0050 | -0.0050 | 0.0010 | -0.0014 |
| ruhig_zentrumsnah->normale_weltspannung | 1 | beruhigend | beruhigend:1 | 0.0100 | -0.0050 | 0.0006 | -0.0008 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `34`
- `normale_weltspannung->offen_suchend`: `10`
- `offen_suchend->normale_weltspannung`: `8`
- `offen_suchend->offen_suchend`: `7`
- `normale_weltspannung->lauter_feldkontakt`: `4`
- `lauter_feldkontakt->lauter_feldkontakt`: `4`
- `lauter_feldkontakt->normale_weltspannung`: `4`
- `randlastige_sinneslage->normale_weltspannung`: `4`
- `normale_weltspannung->randlastige_sinneslage`: `4`
- `offen_suchend->randlastige_sinneslage`: `3`
- `randlastige_sinneslage->offen_suchend`: `2`
- `lauter_feldkontakt->offen_suchend`: `2`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
