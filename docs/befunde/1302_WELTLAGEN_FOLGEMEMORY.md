# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| ruhig_zentrumsnah->ruhig_zentrumsnah | 15 | neutral | neutral:14;beruhigend:1 | 0.0047 | -0.0007 | 0.0006 | -0.0008 |
| normale_weltspannung->normale_weltspannung | 14 | neutral | neutral:14 | 0.0086 | 0.0000 | 0.0009 | -0.0012 |
| offen_suchend->offen_suchend | 13 | neutral | neutral:10;beruhigend:3 | 0.0085 | -0.0023 | 0.0014 | -0.0019 |
| offen_suchend->normale_weltspannung | 11 | neutral | neutral:8;beruhigend:2;stabil_leicht:1 | 0.0082 | -0.0027 | 0.0008 | -0.0011 |
| normale_weltspannung->offen_suchend | 9 | neutral | neutral:8;beruhigend:1 | 0.0100 | -0.0011 | 0.0012 | -0.0016 |
| randlastige_sinneslage->offen_suchend | 6 | neutral | neutral:6 | 0.0100 | 0.0000 | 0.0012 | -0.0016 |
| randlastige_sinneslage->randlastige_sinneslage | 6 | beruhigend | beruhigend:5;neutral:1 | 0.0100 | -0.0150 | 0.0019 | -0.0026 |
| normale_weltspannung->ruhig_zentrumsnah | 5 | neutral | neutral:4;stabil_leicht:1 | 0.0020 | -0.0020 | 0.0006 | -0.0008 |
| randlastige_sinneslage->normale_weltspannung | 5 | neutral | neutral:4;beruhigend:1 | 0.0100 | -0.0020 | 0.0008 | -0.0011 |
| normale_weltspannung->randlastige_sinneslage | 4 | beruhigend | beruhigend:3;neutral:1 | 0.0150 | -0.0125 | 0.0012 | -0.0016 |
| offen_suchend->randlastige_sinneslage | 4 | beruhigend | beruhigend:4 | 0.0050 | -0.0150 | 0.0012 | -0.0017 |
| ruhig_zentrumsnah->normale_weltspannung | 4 | neutral | neutral:4 | 0.0075 | 0.0000 | 0.0007 | -0.0010 |
| lauter_feldkontakt->offen_suchend | 3 | neutral | neutral:2;beruhigend:1 | 0.0067 | -0.0033 | 0.0013 | -0.0018 |
| lauter_feldkontakt->lauter_feldkontakt | 2 | neutral | neutral:2 | 0.0050 | 0.0000 | 0.0010 | -0.0013 |
| lauter_feldkontakt->randlastige_sinneslage | 2 | beruhigend | beruhigend:1;verschiebend:1 | 0.0300 | -0.0150 | 0.0016 | -0.0023 |
| normale_weltspannung->lauter_feldkontakt | 2 | neutral | neutral:1;beruhigend:1 | 0.0100 | -0.0050 | 0.0012 | -0.0017 |
| offen_suchend->lauter_feldkontakt | 2 | beruhigend | beruhigend:1;verschiebend:1 | 0.0250 | -0.0050 | 0.0011 | -0.0016 |
| ruhig_zentrumsnah->randlastige_sinneslage | 2 | beruhigend | beruhigend:2 | 0.0100 | -0.0150 | 0.0010 | -0.0014 |
| lauter_feldkontakt->normale_weltspannung | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0010 | -0.0014 |
| leise_scharf_duenn->normale_weltspannung | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0008 | -0.0012 |
| normale_weltspannung->leise_scharf_duenn | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0009 | -0.0012 |
| randlastige_sinneslage->lauter_feldkontakt | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0015 | -0.0021 |
| ruhig_zentrumsnah->offen_suchend | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0010 | -0.0014 |

## Haeufigste Rohfolgen

- `ruhig_zentrumsnah->ruhig_zentrumsnah`: `15`
- `normale_weltspannung->normale_weltspannung`: `14`
- `offen_suchend->offen_suchend`: `13`
- `offen_suchend->normale_weltspannung`: `11`
- `normale_weltspannung->offen_suchend`: `9`
- `randlastige_sinneslage->randlastige_sinneslage`: `6`
- `randlastige_sinneslage->offen_suchend`: `6`
- `randlastige_sinneslage->normale_weltspannung`: `5`
- `normale_weltspannung->ruhig_zentrumsnah`: `5`
- `offen_suchend->randlastige_sinneslage`: `4`
- `normale_weltspannung->randlastige_sinneslage`: `4`
- `ruhig_zentrumsnah->normale_weltspannung`: `4`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
