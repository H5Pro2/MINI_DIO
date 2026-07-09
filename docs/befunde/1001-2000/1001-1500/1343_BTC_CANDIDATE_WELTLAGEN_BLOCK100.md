# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 60 | neutral | neutral:48;beruhigend:12 | 0.0077 | -0.0020 | 0.0008 | -0.0011 |
| offen_suchend->normale_weltspannung | 32 | neutral | neutral:25;beruhigend:7 | 0.0063 | -0.0022 | 0.0007 | -0.0010 |
| offen_suchend->offen_suchend | 30 | neutral | neutral:25;beruhigend:4;verschiebend:1 | 0.0100 | -0.0013 | 0.0013 | -0.0017 |
| normale_weltspannung->offen_suchend | 29 | neutral | neutral:23;beruhigend:6 | 0.0069 | -0.0021 | 0.0011 | -0.0015 |
| lauter_feldkontakt->lauter_feldkontakt | 19 | neutral | neutral:16;beruhigend:3 | 0.0068 | -0.0016 | 0.0008 | -0.0012 |
| randlastige_sinneslage->normale_weltspannung | 19 | neutral | neutral:14;beruhigend:5 | 0.0047 | -0.0026 | 0.0007 | -0.0010 |
| normale_weltspannung->lauter_feldkontakt | 18 | neutral | neutral:11;beruhigend:7 | 0.0067 | -0.0039 | 0.0009 | -0.0013 |
| normale_weltspannung->randlastige_sinneslage | 17 | beruhigend | beruhigend:16;neutral:1 | 0.0035 | -0.0147 | 0.0015 | -0.0020 |
| randlastige_sinneslage->offen_suchend | 16 | neutral | neutral:11;beruhigend:5 | 0.0088 | -0.0031 | 0.0013 | -0.0018 |
| lauter_feldkontakt->normale_weltspannung | 14 | neutral | neutral:10;beruhigend:4 | 0.0079 | -0.0029 | 0.0007 | -0.0010 |
| offen_suchend->randlastige_sinneslage | 14 | beruhigend | beruhigend:13;neutral:1 | 0.0079 | -0.0143 | 0.0015 | -0.0021 |
| ruhig_zentrumsnah->normale_weltspannung | 14 | neutral | neutral:13;beruhigend:1 | 0.0079 | -0.0007 | 0.0008 | -0.0011 |
| normale_weltspannung->ruhig_zentrumsnah | 13 | neutral | neutral:13 | 0.0062 | 0.0000 | 0.0004 | -0.0006 |
| randlastige_sinneslage->randlastige_sinneslage | 13 | beruhigend | beruhigend:12;neutral:1 | 0.0062 | -0.0146 | 0.0014 | -0.0019 |
| lauter_feldkontakt->randlastige_sinneslage | 12 | beruhigend | beruhigend:11;stabil_leicht:1 | 0.0092 | -0.0150 | 0.0012 | -0.0017 |
| leise_duenn->normale_weltspannung | 9 | neutral | neutral:8;beruhigend:1 | 0.0033 | -0.0011 | 0.0007 | -0.0009 |
| normale_weltspannung->leise_duenn | 8 | neutral | neutral:7;beruhigend:1 | 0.0075 | -0.0013 | 0.0008 | -0.0011 |
| offen_suchend->ruhig_zentrumsnah | 8 | neutral | neutral:8 | 0.0075 | 0.0000 | 0.0005 | -0.0007 |
| leise_duenn->offen_suchend | 7 | neutral | neutral:4;beruhigend:3 | 0.0043 | -0.0043 | 0.0013 | -0.0017 |
| ruhig_zentrumsnah->offen_suchend | 6 | beruhigend | beruhigend:3;neutral:3 | 0.0017 | -0.0050 | 0.0013 | -0.0017 |
| offen_suchend->leise_duenn | 5 | neutral | neutral:4;beruhigend:1 | 0.0060 | -0.0020 | 0.0008 | -0.0011 |
| randlastige_sinneslage->lauter_feldkontakt | 5 | neutral | neutral:3;beruhigend:2 | 0.0080 | -0.0040 | 0.0008 | -0.0011 |
| lauter_feldkontakt->offen_suchend | 4 | neutral | neutral:4 | 0.0025 | 0.0000 | 0.0011 | -0.0015 |
| lauter_feldkontakt->ruhig_zentrumsnah | 3 | neutral | neutral:2;beruhigend:1 | 0.0033 | -0.0033 | 0.0005 | -0.0007 |
| leise_duenn->leise_duenn | 3 | neutral | neutral:2;beruhigend:1 | 0.0033 | -0.0033 | 0.0009 | -0.0011 |
| normale_weltspannung->leise_scharf_duenn | 3 | neutral | neutral:3 | 0.0033 | 0.0000 | 0.0005 | -0.0006 |
| offen_suchend->lauter_feldkontakt | 3 | beruhigend | beruhigend:3 | 0.0100 | -0.0100 | 0.0012 | -0.0017 |
| randlastige_sinneslage->leise_duenn | 3 | neutral | neutral:2;beruhigend:1 | 0.0167 | -0.0033 | 0.0009 | -0.0012 |
| randlastige_sinneslage->ruhig_zentrumsnah | 3 | neutral | neutral:3 | 0.0167 | 0.0000 | 0.0005 | -0.0007 |
| ruhig_zentrumsnah->lauter_feldkontakt | 3 | neutral | neutral:2;beruhigend:1 | 0.0033 | -0.0033 | 0.0009 | -0.0012 |
| ruhig_zentrumsnah->leise_duenn | 3 | neutral | neutral:2;beruhigend:1 | 0.0067 | -0.0033 | 0.0009 | -0.0012 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 3 | neutral | neutral:3 | 0.0100 | 0.0000 | 0.0004 | -0.0006 |
| leise_duenn->leise_scharf_duenn | 2 | stabil_leicht | stabil_leicht:1;neutral:1 | 0.0000 | -0.0050 | 0.0004 | -0.0006 |
| leise_duenn->randlastige_sinneslage | 2 | neutral | neutral:1;beruhigend:1 | 0.0150 | -0.0100 | 0.0011 | -0.0014 |
| leise_scharf_duenn->leise_duenn | 2 | neutral | neutral:2 | 0.0000 | 0.0000 | 0.0009 | -0.0012 |
| ruhig_zentrumsnah->randlastige_sinneslage | 2 | beruhigend | beruhigend:2 | 0.0150 | -0.0200 | 0.0011 | -0.0016 |
| leise_duenn->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0004 | -0.0006 |
| leise_scharf_duenn->lauter_feldkontakt | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0010 | -0.0014 |
| leise_scharf_duenn->normale_weltspannung | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0004 | -0.0005 |
| leise_scharf_duenn->offen_suchend | 1 | neutral | neutral:1 | 0.0000 | 0.0000 | 0.0011 | -0.0015 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `60`
- `offen_suchend->normale_weltspannung`: `32`
- `offen_suchend->offen_suchend`: `30`
- `normale_weltspannung->offen_suchend`: `29`
- `randlastige_sinneslage->normale_weltspannung`: `19`
- `lauter_feldkontakt->lauter_feldkontakt`: `19`
- `normale_weltspannung->lauter_feldkontakt`: `18`
- `normale_weltspannung->randlastige_sinneslage`: `17`
- `randlastige_sinneslage->offen_suchend`: `16`
- `lauter_feldkontakt->normale_weltspannung`: `14`
- `offen_suchend->randlastige_sinneslage`: `14`
- `ruhig_zentrumsnah->normale_weltspannung`: `14`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.

Wie es weitergeht: Wenn bestimmte Lagefolgen stabil beruhigend oder neutral bleiben, kann Mini-DIO spaeter lernen, welche Rezeptorhaltung in welcher Lagefolge tragfaehig war.
