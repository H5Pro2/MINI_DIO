# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 50 | neutral | neutral:31;beruhigend:19 | 0.0072 | -0.0023 | 0.0008 | -0.0011 |
| offen_suchend->normale_weltspannung | 20 | beruhigend | beruhigend:10;neutral:10 | 0.0077 | -0.0027 | 0.0008 | -0.0011 |
| normale_weltspannung->offen_suchend | 19 | beruhigend | beruhigend:11;neutral:8 | 0.0063 | -0.0032 | 0.0011 | -0.0015 |
| offen_suchend->offen_suchend | 12 | neutral | neutral:6;beruhigend:6 | 0.0079 | -0.0025 | 0.0012 | -0.0015 |
| randlastige_sinneslage->offen_suchend | 11 | beruhigend | beruhigend:6;neutral:5 | 0.0100 | -0.0032 | 0.0013 | -0.0017 |
| normale_weltspannung->lauter_feldkontakt | 10 | neutral | neutral:6;beruhigend:4 | 0.0070 | -0.0035 | 0.0009 | -0.0013 |
| normale_weltspannung->randlastige_sinneslage | 10 | beruhigend | beruhigend:10 | 0.0095 | -0.0125 | 0.0011 | -0.0016 |
| randlastige_sinneslage->normale_weltspannung | 10 | neutral | neutral:8;beruhigend:2 | 0.0025 | -0.0015 | 0.0008 | -0.0011 |
| lauter_feldkontakt->normale_weltspannung | 9 | beruhigend | beruhigend:6;neutral:3 | 0.0056 | -0.0039 | 0.0008 | -0.0011 |
| offen_suchend->randlastige_sinneslage | 9 | beruhigend | beruhigend:8;neutral:1 | 0.0061 | -0.0089 | 0.0015 | -0.0021 |
| lauter_feldkontakt->lauter_feldkontakt | 7 | beruhigend | beruhigend:5;neutral:2 | 0.0043 | -0.0043 | 0.0008 | -0.0012 |
| randlastige_sinneslage->randlastige_sinneslage | 7 | beruhigend | beruhigend:7 | 0.0050 | -0.0136 | 0.0014 | -0.0019 |
| lauter_feldkontakt->randlastige_sinneslage | 5 | beruhigend | beruhigend:5 | 0.0060 | -0.0090 | 0.0010 | -0.0014 |
| leise_duenn->normale_weltspannung | 5 | beruhigend | beruhigend:3;neutral:2 | 0.0080 | -0.0030 | 0.0009 | -0.0013 |
| randlastige_sinneslage->lauter_feldkontakt | 3 | beruhigend | beruhigend:2;neutral:1 | 0.0150 | -0.0033 | 0.0008 | -0.0011 |
| leise_duenn->leise_duenn | 2 | beruhigend | beruhigend:1;neutral:1 | 0.0050 | -0.0025 | 0.0008 | -0.0011 |
| normale_weltspannung->leise_duenn | 2 | neutral | neutral:2 | 0.0100 | 0.0000 | 0.0008 | -0.0010 |
| normale_weltspannung->ruhig_zentrumsnah | 2 | neutral | neutral:2 | 0.0100 | 0.0000 | 0.0006 | -0.0008 |
| offen_suchend->leise_duenn | 2 | neutral | neutral:2 | 0.0025 | 0.0000 | 0.0008 | -0.0010 |
| ruhig_zentrumsnah->lauter_feldkontakt | 2 | beruhigend | beruhigend:1;neutral:1 | 0.0025 | -0.0025 | 0.0005 | -0.0008 |
| lauter_feldkontakt->offen_suchend | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0013 | -0.0017 |
| lauter_feldkontakt->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0004 | -0.0006 |
| leise_scharf_duenn->normale_weltspannung | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0007 | -0.0010 |
| normale_weltspannung->leise_scharf_duenn | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0006 | -0.0008 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `50`
- `offen_suchend->normale_weltspannung`: `20`
- `normale_weltspannung->offen_suchend`: `19`
- `offen_suchend->offen_suchend`: `12`
- `randlastige_sinneslage->offen_suchend`: `11`
- `normale_weltspannung->lauter_feldkontakt`: `10`
- `normale_weltspannung->randlastige_sinneslage`: `10`
- `randlastige_sinneslage->normale_weltspannung`: `10`
- `offen_suchend->randlastige_sinneslage`: `9`
- `lauter_feldkontakt->normale_weltspannung`: `9`
- `lauter_feldkontakt->lauter_feldkontakt`: `7`
- `randlastige_sinneslage->randlastige_sinneslage`: `7`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.
