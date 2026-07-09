# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 100 | neutral | neutral:57;beruhigend:43 | 0.0073 | -0.0027 | 0.0008 | -0.0012 |
| offen_suchend->offen_suchend | 49 | neutral | neutral:25;beruhigend:24 | 0.0098 | -0.0028 | 0.0013 | -0.0017 |
| offen_suchend->normale_weltspannung | 35 | neutral | neutral:19;beruhigend:16 | 0.0074 | -0.0029 | 0.0008 | -0.0011 |
| normale_weltspannung->offen_suchend | 33 | beruhigend | beruhigend:21;neutral:12 | 0.0076 | -0.0036 | 0.0012 | -0.0016 |
| normale_weltspannung->ruhig_zentrumsnah | 22 | neutral | neutral:19;beruhigend:3 | 0.0084 | -0.0007 | 0.0005 | -0.0007 |
| randlastige_sinneslage->offen_suchend | 21 | beruhigend | beruhigend:11;neutral:10 | 0.0079 | -0.0029 | 0.0012 | -0.0017 |
| offen_suchend->randlastige_sinneslage | 20 | beruhigend | beruhigend:19;neutral:1 | 0.0083 | -0.0115 | 0.0016 | -0.0022 |
| ruhig_zentrumsnah->normale_weltspannung | 18 | neutral | neutral:14;beruhigend:4 | 0.0083 | -0.0011 | 0.0007 | -0.0010 |
| randlastige_sinneslage->normale_weltspannung | 17 | neutral | neutral:9;beruhigend:8 | 0.0076 | -0.0026 | 0.0009 | -0.0012 |
| lauter_feldkontakt->normale_weltspannung | 16 | beruhigend | beruhigend:9;neutral:7 | 0.0091 | -0.0034 | 0.0009 | -0.0013 |
| normale_weltspannung->lauter_feldkontakt | 16 | beruhigend | beruhigend:10;neutral:6 | 0.0116 | -0.0044 | 0.0011 | -0.0016 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 15 | neutral | neutral:12;beruhigend:2;stabil_leicht:1 | 0.0050 | -0.0010 | 0.0006 | -0.0008 |
| normale_weltspannung->randlastige_sinneslage | 14 | beruhigend | beruhigend:12;neutral:2 | 0.0068 | -0.0096 | 0.0013 | -0.0017 |
| randlastige_sinneslage->randlastige_sinneslage | 14 | beruhigend | beruhigend:14 | 0.0071 | -0.0132 | 0.0016 | -0.0022 |
| ruhig_zentrumsnah->randlastige_sinneslage | 7 | beruhigend | beruhigend:6;neutral:1 | 0.0100 | -0.0100 | 0.0011 | -0.0016 |
| lauter_feldkontakt->offen_suchend | 6 | beruhigend | beruhigend:4;neutral:2 | 0.0067 | -0.0042 | 0.0013 | -0.0017 |
| lauter_feldkontakt->randlastige_sinneslage | 4 | beruhigend | beruhigend:4 | 0.0063 | -0.0075 | 0.0010 | -0.0014 |
| randlastige_sinneslage->ruhig_zentrumsnah | 4 | neutral | neutral:4 | 0.0063 | 0.0000 | 0.0005 | -0.0008 |
| ruhig_zentrumsnah->lauter_feldkontakt | 4 | neutral | neutral:3;beruhigend:1 | 0.0088 | -0.0013 | 0.0007 | -0.0009 |
| leise_duenn->normale_weltspannung | 3 | beruhigend | beruhigend:2;neutral:1 | 0.0017 | -0.0033 | 0.0009 | -0.0012 |
| normale_weltspannung->leise_duenn | 3 | neutral | neutral:3 | 0.0117 | 0.0000 | 0.0008 | -0.0011 |
| offen_suchend->lauter_feldkontakt | 3 | beruhigend | beruhigend:3 | 0.0067 | -0.0067 | 0.0014 | -0.0019 |
| offen_suchend->ruhig_zentrumsnah | 3 | neutral | neutral:3 | 0.0050 | -0.0017 | 0.0005 | -0.0007 |
| lauter_feldkontakt->lauter_feldkontakt | 2 | beruhigend | beruhigend:2 | 0.0000 | -0.0050 | 0.0007 | -0.0010 |
| leise_duenn->offen_suchend | 2 | neutral | neutral:2 | 0.0050 | 0.0000 | 0.0011 | -0.0016 |
| leise_scharf_duenn->normale_weltspannung | 2 | neutral | neutral:1;beruhigend:1 | 0.0100 | -0.0025 | 0.0008 | -0.0010 |
| randlastige_sinneslage->lauter_feldkontakt | 2 | beruhigend | beruhigend:1;neutral:1 | 0.0150 | -0.0025 | 0.0007 | -0.0010 |
| ruhig_zentrumsnah->offen_suchend | 2 | beruhigend | beruhigend:2 | 0.0075 | -0.0075 | 0.0014 | -0.0020 |
| normale_weltspannung->leise_scharf_duenn | 1 | beruhigend | beruhigend:1 | 0.0000 | -0.0050 | 0.0007 | -0.0009 |
| offen_suchend->leise_duenn | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0005 | -0.0007 |
| offen_suchend->leise_scharf_duenn | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0007 | -0.0009 |
| randlastige_sinneslage->leise_duenn | 1 | beruhigend | beruhigend:1 | 0.0000 | -0.0100 | 0.0010 | -0.0013 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `100`
- `offen_suchend->offen_suchend`: `49`
- `offen_suchend->normale_weltspannung`: `35`
- `normale_weltspannung->offen_suchend`: `33`
- `normale_weltspannung->ruhig_zentrumsnah`: `22`
- `randlastige_sinneslage->offen_suchend`: `21`
- `offen_suchend->randlastige_sinneslage`: `20`
- `ruhig_zentrumsnah->normale_weltspannung`: `18`
- `randlastige_sinneslage->normale_weltspannung`: `17`
- `lauter_feldkontakt->normale_weltspannung`: `16`
- `normale_weltspannung->lauter_feldkontakt`: `16`
- `ruhig_zentrumsnah->ruhig_zentrumsnah`: `15`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.
