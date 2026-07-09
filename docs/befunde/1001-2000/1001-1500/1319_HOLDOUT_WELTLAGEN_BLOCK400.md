# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 38 | beruhigend | beruhigend:24;neutral:14 | 0.0088 | -0.0024 | 0.0008 | -0.0012 |
| offen_suchend->offen_suchend | 19 | beruhigend | beruhigend:11;neutral:8 | 0.0072 | -0.0025 | 0.0013 | -0.0017 |
| offen_suchend->normale_weltspannung | 16 | beruhigend | beruhigend:10;neutral:6 | 0.0083 | -0.0039 | 0.0008 | -0.0012 |
| normale_weltspannung->offen_suchend | 13 | beruhigend | beruhigend:11;neutral:2 | 0.0085 | -0.0046 | 0.0013 | -0.0017 |
| normale_weltspannung->lauter_feldkontakt | 5 | beruhigend | beruhigend:4;neutral:1 | 0.0105 | -0.0025 | 0.0011 | -0.0016 |
| normale_weltspannung->ruhig_zentrumsnah | 5 | neutral | neutral:4;beruhigend:1 | 0.0110 | -0.0005 | 0.0007 | -0.0009 |
| ruhig_zentrumsnah->normale_weltspannung | 5 | beruhigend | beruhigend:3;neutral:2 | 0.0085 | -0.0030 | 0.0008 | -0.0011 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 5 | neutral | neutral:3;beruhigend:2 | 0.0040 | -0.0010 | 0.0006 | -0.0008 |
| lauter_feldkontakt->normale_weltspannung | 3 | neutral | neutral:2;beruhigend:1 | 0.0075 | -0.0008 | 0.0009 | -0.0013 |
| lauter_feldkontakt->offen_suchend | 3 | beruhigend | beruhigend:3 | 0.0100 | -0.0042 | 0.0013 | -0.0018 |
| normale_weltspannung->randlastige_sinneslage | 2 | beruhigend | beruhigend:2 | 0.0088 | -0.0075 | 0.0011 | -0.0015 |
| offen_suchend->randlastige_sinneslage | 2 | beruhigend | beruhigend:2 | 0.0138 | -0.0088 | 0.0016 | -0.0022 |
| randlastige_sinneslage->normale_weltspannung | 2 | beruhigend | beruhigend:2 | 0.0088 | -0.0050 | 0.0008 | -0.0011 |
| randlastige_sinneslage->offen_suchend | 2 | beruhigend | beruhigend:2 | 0.0100 | -0.0037 | 0.0014 | -0.0018 |
| randlastige_sinneslage->randlastige_sinneslage | 2 | beruhigend | beruhigend:2 | 0.0050 | -0.0088 | 0.0010 | -0.0013 |
| lauter_feldkontakt->lauter_feldkontakt | 1 | beruhigend | beruhigend:1 | 0.0125 | -0.0050 | 0.0009 | -0.0012 |
| ruhig_zentrumsnah->lauter_feldkontakt | 1 | beruhigend | beruhigend:1 | 0.0100 | -0.0025 | 0.0006 | -0.0009 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `38`
- `offen_suchend->offen_suchend`: `19`
- `offen_suchend->normale_weltspannung`: `16`
- `normale_weltspannung->offen_suchend`: `13`
- `normale_weltspannung->lauter_feldkontakt`: `5`
- `normale_weltspannung->ruhig_zentrumsnah`: `5`
- `ruhig_zentrumsnah->normale_weltspannung`: `5`
- `ruhig_zentrumsnah->ruhig_zentrumsnah`: `5`
- `lauter_feldkontakt->normale_weltspannung`: `3`
- `lauter_feldkontakt->offen_suchend`: `3`
- `offen_suchend->randlastige_sinneslage`: `2`
- `randlastige_sinneslage->randlastige_sinneslage`: `2`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
