# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 51 | beruhigend | beruhigend:36;neutral:15 | 0.0071 | -0.0034 | 0.0009 | -0.0012 |
| offen_suchend->offen_suchend | 34 | beruhigend | beruhigend:29;neutral:5 | 0.0082 | -0.0040 | 0.0013 | -0.0017 |
| offen_suchend->normale_weltspannung | 16 | beruhigend | beruhigend:10;neutral:6 | 0.0086 | -0.0028 | 0.0009 | -0.0012 |
| normale_weltspannung->offen_suchend | 13 | beruhigend | beruhigend:11;neutral:2 | 0.0083 | -0.0044 | 0.0012 | -0.0016 |
| ruhig_zentrumsnah->normale_weltspannung | 9 | beruhigend | beruhigend:7;neutral:2 | 0.0086 | -0.0025 | 0.0008 | -0.0011 |
| normale_weltspannung->ruhig_zentrumsnah | 8 | neutral | neutral:8 | 0.0056 | 0.0000 | 0.0006 | -0.0008 |
| normale_weltspannung->lauter_feldkontakt | 5 | neutral | neutral:3;beruhigend:2 | 0.0105 | -0.0025 | 0.0011 | -0.0015 |
| randlastige_sinneslage->offen_suchend | 5 | beruhigend | beruhigend:5 | 0.0065 | -0.0060 | 0.0013 | -0.0017 |
| lauter_feldkontakt->offen_suchend | 4 | beruhigend | beruhigend:3;neutral:1 | 0.0044 | -0.0025 | 0.0012 | -0.0016 |
| offen_suchend->randlastige_sinneslage | 4 | beruhigend | beruhigend:4 | 0.0031 | -0.0112 | 0.0015 | -0.0021 |
| lauter_feldkontakt->lauter_feldkontakt | 3 | beruhigend | beruhigend:2;neutral:1 | 0.0125 | -0.0033 | 0.0013 | -0.0018 |
| lauter_feldkontakt->normale_weltspannung | 3 | beruhigend | beruhigend:2;neutral:1 | 0.0083 | -0.0050 | 0.0009 | -0.0012 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 3 | neutral | neutral:3 | 0.0117 | 0.0000 | 0.0008 | -0.0011 |
| normale_weltspannung->randlastige_sinneslage | 2 | beruhigend | beruhigend:2 | 0.0063 | -0.0088 | 0.0015 | -0.0020 |
| offen_suchend->lauter_feldkontakt | 2 | beruhigend | beruhigend:2 | 0.0163 | -0.0050 | 0.0014 | -0.0019 |
| leise_duenn->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0006 | -0.0008 |
| normale_weltspannung->leise_duenn | 1 | neutral | neutral:1 | 0.0025 | 0.0000 | 0.0007 | -0.0008 |
| offen_suchend->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0004 | -0.0005 |
| randlastige_sinneslage->normale_weltspannung | 1 | beruhigend | beruhigend:1 | 0.0050 | -0.0050 | 0.0007 | -0.0009 |
| ruhig_zentrumsnah->lauter_feldkontakt | 1 | beruhigend | beruhigend:1 | 0.0150 | -0.0050 | 0.0011 | -0.0016 |
| ruhig_zentrumsnah->offen_suchend | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0014 | -0.0020 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `51`
- `offen_suchend->offen_suchend`: `34`
- `offen_suchend->normale_weltspannung`: `16`
- `normale_weltspannung->offen_suchend`: `13`
- `ruhig_zentrumsnah->normale_weltspannung`: `9`
- `normale_weltspannung->ruhig_zentrumsnah`: `8`
- `randlastige_sinneslage->offen_suchend`: `5`
- `normale_weltspannung->lauter_feldkontakt`: `5`
- `offen_suchend->randlastige_sinneslage`: `4`
- `lauter_feldkontakt->offen_suchend`: `4`
- `lauter_feldkontakt->lauter_feldkontakt`: `3`
- `lauter_feldkontakt->normale_weltspannung`: `3`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
