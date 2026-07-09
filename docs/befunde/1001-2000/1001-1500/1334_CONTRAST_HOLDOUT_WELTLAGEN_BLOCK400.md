# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 64 | beruhigend | beruhigend:43;neutral:21 | 0.0079 | -0.0027 | 0.0008 | -0.0012 |
| offen_suchend->offen_suchend | 30 | beruhigend | beruhigend:26;neutral:4 | 0.0091 | -0.0047 | 0.0013 | -0.0017 |
| offen_suchend->normale_weltspannung | 22 | beruhigend | beruhigend:15;neutral:7 | 0.0070 | -0.0032 | 0.0008 | -0.0011 |
| normale_weltspannung->offen_suchend | 20 | beruhigend | beruhigend:18;neutral:2 | 0.0074 | -0.0040 | 0.0012 | -0.0016 |
| normale_weltspannung->randlastige_sinneslage | 10 | beruhigend | beruhigend:10 | 0.0060 | -0.0092 | 0.0012 | -0.0016 |
| randlastige_sinneslage->offen_suchend | 10 | beruhigend | beruhigend:6;neutral:4 | 0.0065 | -0.0022 | 0.0013 | -0.0018 |
| normale_weltspannung->ruhig_zentrumsnah | 9 | neutral | neutral:6;beruhigend:3 | 0.0072 | -0.0011 | 0.0006 | -0.0008 |
| ruhig_zentrumsnah->normale_weltspannung | 9 | beruhigend | beruhigend:7;neutral:2 | 0.0078 | -0.0044 | 0.0008 | -0.0011 |
| lauter_feldkontakt->normale_weltspannung | 8 | beruhigend | beruhigend:5;neutral:3 | 0.0084 | -0.0019 | 0.0010 | -0.0013 |
| normale_weltspannung->lauter_feldkontakt | 7 | beruhigend | beruhigend:4;neutral:3 | 0.0086 | -0.0018 | 0.0010 | -0.0014 |
| offen_suchend->randlastige_sinneslage | 6 | beruhigend | beruhigend:6 | 0.0104 | -0.0104 | 0.0016 | -0.0022 |
| randlastige_sinneslage->normale_weltspannung | 5 | beruhigend | beruhigend:4;neutral:1 | 0.0090 | -0.0040 | 0.0008 | -0.0012 |
| randlastige_sinneslage->randlastige_sinneslage | 5 | beruhigend | beruhigend:5 | 0.0075 | -0.0105 | 0.0012 | -0.0017 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 5 | neutral | neutral:3;beruhigend:2 | 0.0040 | -0.0010 | 0.0006 | -0.0008 |
| lauter_feldkontakt->lauter_feldkontakt | 1 | beruhigend | beruhigend:1 | 0.0125 | -0.0050 | 0.0009 | -0.0012 |
| lauter_feldkontakt->offen_suchend | 1 | beruhigend | beruhigend:1 | 0.0175 | -0.0075 | 0.0016 | -0.0022 |
| offen_suchend->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0006 | -0.0008 |
| randlastige_sinneslage->lauter_feldkontakt | 1 | beruhigend | beruhigend:1 | 0.0025 | -0.0075 | 0.0010 | -0.0014 |
| ruhig_zentrumsnah->lauter_feldkontakt | 1 | beruhigend | beruhigend:1 | 0.0100 | -0.0025 | 0.0006 | -0.0009 |
| ruhig_zentrumsnah->offen_suchend | 1 | beruhigend | beruhigend:1 | 0.0050 | -0.0050 | 0.0012 | -0.0016 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `64`
- `offen_suchend->offen_suchend`: `30`
- `offen_suchend->normale_weltspannung`: `22`
- `normale_weltspannung->offen_suchend`: `20`
- `randlastige_sinneslage->offen_suchend`: `10`
- `normale_weltspannung->randlastige_sinneslage`: `10`
- `normale_weltspannung->ruhig_zentrumsnah`: `9`
- `ruhig_zentrumsnah->normale_weltspannung`: `9`
- `lauter_feldkontakt->normale_weltspannung`: `8`
- `normale_weltspannung->lauter_feldkontakt`: `7`
- `offen_suchend->randlastige_sinneslage`: `6`
- `randlastige_sinneslage->randlastige_sinneslage`: `5`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
