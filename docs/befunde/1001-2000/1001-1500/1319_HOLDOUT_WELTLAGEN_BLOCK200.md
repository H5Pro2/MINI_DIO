# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 72 | neutral | neutral:45;beruhigend:27 | 0.0092 | -0.0023 | 0.0008 | -0.0011 |
| offen_suchend->offen_suchend | 43 | beruhigend | beruhigend:23;neutral:20 | 0.0079 | -0.0034 | 0.0014 | -0.0018 |
| offen_suchend->normale_weltspannung | 22 | beruhigend | beruhigend:11;neutral:11 | 0.0082 | -0.0032 | 0.0008 | -0.0011 |
| normale_weltspannung->offen_suchend | 19 | beruhigend | beruhigend:10;neutral:9 | 0.0089 | -0.0029 | 0.0013 | -0.0017 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 14 | neutral | neutral:12;beruhigend:2 | 0.0054 | -0.0007 | 0.0006 | -0.0009 |
| normale_weltspannung->ruhig_zentrumsnah | 9 | neutral | neutral:8;beruhigend:1 | 0.0094 | -0.0006 | 0.0006 | -0.0009 |
| lauter_feldkontakt->normale_weltspannung | 7 | beruhigend | beruhigend:5;neutral:2 | 0.0079 | -0.0036 | 0.0008 | -0.0011 |
| normale_weltspannung->lauter_feldkontakt | 7 | neutral | neutral:4;beruhigend:3 | 0.0121 | -0.0029 | 0.0011 | -0.0016 |
| randlastige_sinneslage->normale_weltspannung | 7 | beruhigend | beruhigend:4;neutral:3 | 0.0079 | -0.0036 | 0.0010 | -0.0014 |
| ruhig_zentrumsnah->normale_weltspannung | 7 | neutral | neutral:6;beruhigend:1 | 0.0086 | -0.0007 | 0.0008 | -0.0011 |
| normale_weltspannung->randlastige_sinneslage | 6 | beruhigend | beruhigend:5;neutral:1 | 0.0033 | -0.0108 | 0.0012 | -0.0016 |
| randlastige_sinneslage->offen_suchend | 6 | neutral | neutral:3;beruhigend:3 | 0.0183 | -0.0025 | 0.0011 | -0.0015 |
| offen_suchend->randlastige_sinneslage | 4 | beruhigend | beruhigend:4 | 0.0063 | -0.0163 | 0.0015 | -0.0021 |
| lauter_feldkontakt->lauter_feldkontakt | 3 | neutral | neutral:2;beruhigend:1 | 0.0050 | -0.0017 | 0.0008 | -0.0011 |
| lauter_feldkontakt->offen_suchend | 3 | neutral | neutral:2;beruhigend:1 | 0.0050 | -0.0017 | 0.0013 | -0.0018 |
| leise_duenn->normale_weltspannung | 3 | beruhigend | beruhigend:2;neutral:1 | 0.0017 | -0.0033 | 0.0009 | -0.0012 |
| normale_weltspannung->leise_duenn | 3 | neutral | neutral:3 | 0.0117 | 0.0000 | 0.0008 | -0.0011 |
| randlastige_sinneslage->randlastige_sinneslage | 3 | beruhigend | beruhigend:3 | 0.0100 | -0.0133 | 0.0018 | -0.0024 |
| ruhig_zentrumsnah->randlastige_sinneslage | 3 | beruhigend | beruhigend:3 | 0.0150 | -0.0117 | 0.0012 | -0.0017 |
| lauter_feldkontakt->randlastige_sinneslage | 2 | beruhigend | beruhigend:2 | 0.0025 | -0.0075 | 0.0010 | -0.0015 |
| randlastige_sinneslage->lauter_feldkontakt | 2 | beruhigend | beruhigend:1;neutral:1 | 0.0150 | -0.0025 | 0.0008 | -0.0012 |
| ruhig_zentrumsnah->lauter_feldkontakt | 2 | beruhigend | beruhigend:1;neutral:1 | 0.0100 | -0.0025 | 0.0005 | -0.0007 |
| lauter_feldkontakt->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0005 | -0.0007 |
| leise_duenn->offen_suchend | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0012 | -0.0016 |
| leise_scharf_duenn->normale_weltspannung | 1 | neutral | neutral:1 | 0.0150 | 0.0000 | 0.0008 | -0.0011 |
| offen_suchend->lauter_feldkontakt | 1 | neutral | neutral:1 | 0.0150 | 0.0000 | 0.0008 | -0.0011 |
| offen_suchend->leise_duenn | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0005 | -0.0007 |
| offen_suchend->leise_scharf_duenn | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0007 | -0.0009 |
| offen_suchend->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0007 | -0.0009 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `72`
- `offen_suchend->offen_suchend`: `43`
- `offen_suchend->normale_weltspannung`: `22`
- `normale_weltspannung->offen_suchend`: `19`
- `ruhig_zentrumsnah->ruhig_zentrumsnah`: `14`
- `normale_weltspannung->ruhig_zentrumsnah`: `9`
- `lauter_feldkontakt->normale_weltspannung`: `7`
- `normale_weltspannung->lauter_feldkontakt`: `7`
- `randlastige_sinneslage->normale_weltspannung`: `7`
- `ruhig_zentrumsnah->normale_weltspannung`: `7`
- `normale_weltspannung->randlastige_sinneslage`: `6`
- `randlastige_sinneslage->offen_suchend`: `6`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.
