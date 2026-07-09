# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 136 | neutral | neutral:101;beruhigend:34;stabil_leicht:1 | 0.0082 | -0.0026 | 0.0008 | -0.0011 |
| offen_suchend->offen_suchend | 71 | neutral | neutral:54;beruhigend:17 | 0.0083 | -0.0024 | 0.0013 | -0.0018 |
| offen_suchend->normale_weltspannung | 62 | neutral | neutral:47;beruhigend:14;verschiebend:1 | 0.0074 | -0.0023 | 0.0008 | -0.0012 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 53 | neutral | neutral:47;beruhigend:4;stabil_leicht:2 | 0.0058 | -0.0011 | 0.0005 | -0.0007 |
| normale_weltspannung->ruhig_zentrumsnah | 51 | neutral | neutral:49;beruhigend:2 | 0.0069 | -0.0004 | 0.0005 | -0.0007 |
| normale_weltspannung->offen_suchend | 47 | neutral | neutral:31;beruhigend:15;verschiebend:1 | 0.0094 | -0.0032 | 0.0013 | -0.0018 |
| randlastige_sinneslage->offen_suchend | 45 | neutral | neutral:34;beruhigend:11 | 0.0084 | -0.0024 | 0.0014 | -0.0018 |
| normale_weltspannung->lauter_feldkontakt | 44 | neutral | neutral:32;beruhigend:12 | 0.0077 | -0.0027 | 0.0011 | -0.0015 |
| ruhig_zentrumsnah->normale_weltspannung | 43 | neutral | neutral:33;beruhigend:9;verschiebend:1 | 0.0086 | -0.0021 | 0.0008 | -0.0011 |
| lauter_feldkontakt->normale_weltspannung | 40 | neutral | neutral:27;beruhigend:13 | 0.0065 | -0.0032 | 0.0007 | -0.0010 |
| normale_weltspannung->randlastige_sinneslage | 39 | beruhigend | beruhigend:36;neutral:3 | 0.0067 | -0.0146 | 0.0014 | -0.0019 |
| randlastige_sinneslage->normale_weltspannung | 35 | neutral | neutral:29;beruhigend:6 | 0.0069 | -0.0017 | 0.0008 | -0.0011 |
| offen_suchend->randlastige_sinneslage | 32 | beruhigend | beruhigend:26;neutral:6 | 0.0059 | -0.0156 | 0.0016 | -0.0023 |
| lauter_feldkontakt->lauter_feldkontakt | 22 | neutral | neutral:15;beruhigend:7 | 0.0109 | -0.0032 | 0.0009 | -0.0013 |
| randlastige_sinneslage->randlastige_sinneslage | 22 | beruhigend | beruhigend:21;neutral:1 | 0.0105 | -0.0136 | 0.0018 | -0.0024 |
| lauter_feldkontakt->offen_suchend | 18 | neutral | neutral:13;beruhigend:4;verschiebend:1 | 0.0128 | -0.0028 | 0.0014 | -0.0019 |
| offen_suchend->lauter_feldkontakt | 13 | neutral | neutral:11;beruhigend:2 | 0.0069 | -0.0015 | 0.0014 | -0.0019 |
| ruhig_zentrumsnah->lauter_feldkontakt | 11 | neutral | neutral:8;beruhigend:3 | 0.0055 | -0.0027 | 0.0010 | -0.0014 |
| ruhig_zentrumsnah->randlastige_sinneslage | 11 | beruhigend | beruhigend:6;neutral:3;verschiebend:2 | 0.0109 | -0.0145 | 0.0013 | -0.0018 |
| leise_duenn->offen_suchend | 10 | neutral | neutral:7;beruhigend:3 | 0.0050 | -0.0030 | 0.0012 | -0.0016 |
| lauter_feldkontakt->randlastige_sinneslage | 9 | beruhigend | beruhigend:9 | 0.0056 | -0.0133 | 0.0014 | -0.0020 |
| leise_duenn->normale_weltspannung | 9 | neutral | neutral:7;beruhigend:2 | 0.0100 | -0.0022 | 0.0008 | -0.0011 |
| normale_weltspannung->leise_duenn | 9 | neutral | neutral:8;beruhigend:1 | 0.0089 | -0.0011 | 0.0007 | -0.0009 |
| offen_suchend->leise_duenn | 9 | neutral | neutral:7;verschiebend:1;beruhigend:1 | 0.0078 | -0.0011 | 0.0009 | -0.0012 |
| ruhig_zentrumsnah->offen_suchend | 8 | neutral | neutral:7;beruhigend:1 | 0.0075 | -0.0013 | 0.0011 | -0.0015 |
| offen_suchend->ruhig_zentrumsnah | 7 | neutral | neutral:6;beruhigend:1 | 0.0057 | -0.0014 | 0.0005 | -0.0007 |
| lauter_feldkontakt->ruhig_zentrumsnah | 5 | neutral | neutral:5 | 0.0020 | 0.0000 | 0.0004 | -0.0005 |
| randlastige_sinneslage->leise_duenn | 5 | neutral | neutral:4;beruhigend:1 | 0.0100 | -0.0020 | 0.0008 | -0.0010 |
| randlastige_sinneslage->lauter_feldkontakt | 4 | neutral | neutral:3;beruhigend:1 | 0.0100 | -0.0025 | 0.0011 | -0.0015 |
| randlastige_sinneslage->ruhig_zentrumsnah | 4 | neutral | neutral:4 | 0.0000 | 0.0000 | 0.0004 | -0.0006 |
| offen_suchend->leise_scharf_duenn | 3 | neutral | neutral:3 | 0.0000 | 0.0000 | 0.0006 | -0.0008 |
| leise_duenn->leise_duenn | 2 | neutral | neutral:2 | 0.0050 | 0.0000 | 0.0008 | -0.0011 |
| leise_duenn->randlastige_sinneslage | 2 | neutral | neutral:1;beruhigend:1 | 0.0200 | -0.0150 | 0.0015 | -0.0020 |
| leise_duenn->ruhig_zentrumsnah | 2 | neutral | neutral:2 | 0.0100 | 0.0000 | 0.0004 | -0.0005 |
| leise_scharf_duenn->normale_weltspannung | 2 | neutral | neutral:2 | 0.0200 | 0.0000 | 0.0009 | -0.0012 |
| leise_scharf_duenn->ruhig_zentrumsnah | 2 | neutral | neutral:1;beruhigend:1 | 0.0000 | -0.0050 | 0.0007 | -0.0009 |
| normale_weltspannung->leise_scharf_duenn | 2 | neutral | neutral:2 | 0.0000 | 0.0000 | 0.0007 | -0.0010 |
| leise_scharf_duenn->leise_scharf_duenn | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0006 | -0.0007 |
| leise_scharf_duenn->offen_suchend | 1 | beruhigend | beruhigend:1 | 0.0000 | -0.0100 | 0.0016 | -0.0021 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `136`
- `offen_suchend->offen_suchend`: `71`
- `offen_suchend->normale_weltspannung`: `62`
- `ruhig_zentrumsnah->ruhig_zentrumsnah`: `53`
- `normale_weltspannung->ruhig_zentrumsnah`: `51`
- `normale_weltspannung->offen_suchend`: `47`
- `randlastige_sinneslage->offen_suchend`: `45`
- `normale_weltspannung->lauter_feldkontakt`: `44`
- `ruhig_zentrumsnah->normale_weltspannung`: `43`
- `lauter_feldkontakt->normale_weltspannung`: `40`
- `normale_weltspannung->randlastige_sinneslage`: `39`
- `randlastige_sinneslage->normale_weltspannung`: `35`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.
