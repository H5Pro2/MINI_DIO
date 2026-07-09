# Weltlagen-Folgememory

Passive Blockfolgen der gemessenen Weltlage.

Diese Diagnose speichert nicht nur Mittelwerte, sondern Lagefolgen:

```text
vorherige Weltlage -> aktuelle Weltlage -> Feldfolge nach Rezeptorhaltung
```

## Verdichtete Folgen

| Lagefolge | Vorkommen | Folge | Outcomes | dZentrum | dRand | dRekopplung | dStrain |
|---|---:|---|---|---:|---:|---:|---:|
| normale_weltspannung->normale_weltspannung | 65 | neutral | neutral:39;beruhigend:26 | 0.0075 | -0.0026 | 0.0008 | -0.0011 |
| offen_suchend->offen_suchend | 42 | neutral | neutral:21;beruhigend:21 | 0.0082 | -0.0029 | 0.0013 | -0.0017 |
| offen_suchend->normale_weltspannung | 26 | beruhigend | beruhigend:14;neutral:12 | 0.0073 | -0.0033 | 0.0009 | -0.0012 |
| normale_weltspannung->offen_suchend | 22 | beruhigend | beruhigend:16;neutral:6 | 0.0059 | -0.0048 | 0.0011 | -0.0015 |
| offen_suchend->randlastige_sinneslage | 19 | beruhigend | beruhigend:18;neutral:1 | 0.0039 | -0.0097 | 0.0015 | -0.0021 |
| randlastige_sinneslage->offen_suchend | 18 | neutral | neutral:10;beruhigend:8 | 0.0092 | -0.0031 | 0.0012 | -0.0016 |
| normale_weltspannung->ruhig_zentrumsnah | 15 | neutral | neutral:14;beruhigend:1 | 0.0073 | -0.0003 | 0.0006 | -0.0008 |
| normale_weltspannung->lauter_feldkontakt | 14 | beruhigend | beruhigend:7;neutral:7 | 0.0082 | -0.0029 | 0.0011 | -0.0016 |
| randlastige_sinneslage->normale_weltspannung | 14 | neutral | neutral:10;beruhigend:4 | 0.0086 | -0.0014 | 0.0009 | -0.0012 |
| ruhig_zentrumsnah->normale_weltspannung | 13 | neutral | neutral:12;beruhigend:1 | 0.0088 | -0.0004 | 0.0009 | -0.0013 |
| lauter_feldkontakt->lauter_feldkontakt | 12 | beruhigend | beruhigend:9;neutral:3 | 0.0108 | -0.0042 | 0.0012 | -0.0017 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 12 | neutral | neutral:11;beruhigend:1 | 0.0071 | -0.0004 | 0.0005 | -0.0007 |
| normale_weltspannung->randlastige_sinneslage | 11 | beruhigend | beruhigend:11 | 0.0095 | -0.0114 | 0.0012 | -0.0016 |
| lauter_feldkontakt->normale_weltspannung | 8 | neutral | neutral:5;beruhigend:3 | 0.0069 | -0.0025 | 0.0009 | -0.0012 |
| lauter_feldkontakt->offen_suchend | 8 | neutral | neutral:5;beruhigend:3 | 0.0063 | -0.0025 | 0.0011 | -0.0015 |
| randlastige_sinneslage->randlastige_sinneslage | 8 | beruhigend | beruhigend:8 | 0.0094 | -0.0106 | 0.0016 | -0.0021 |
| leise_duenn->ruhig_zentrumsnah | 4 | neutral | neutral:4 | 0.0037 | 0.0000 | 0.0006 | -0.0008 |
| offen_suchend->ruhig_zentrumsnah | 4 | neutral | neutral:3;beruhigend:1 | 0.0100 | -0.0013 | 0.0005 | -0.0007 |
| ruhig_zentrumsnah->offen_suchend | 4 | neutral | neutral:3;beruhigend:1 | 0.0075 | -0.0013 | 0.0011 | -0.0015 |
| lauter_feldkontakt->randlastige_sinneslage | 3 | beruhigend | beruhigend:3 | 0.0117 | -0.0183 | 0.0012 | -0.0017 |
| leise_duenn->normale_weltspannung | 3 | neutral | neutral:2;beruhigend:1 | 0.0083 | -0.0017 | 0.0010 | -0.0013 |
| offen_suchend->lauter_feldkontakt | 3 | beruhigend | beruhigend:3 | 0.0117 | -0.0050 | 0.0015 | -0.0022 |
| ruhig_zentrumsnah->lauter_feldkontakt | 3 | beruhigend | beruhigend:2;neutral:1 | 0.0133 | -0.0033 | 0.0012 | -0.0017 |
| ruhig_zentrumsnah->leise_duenn | 3 | neutral | neutral:3 | 0.0067 | 0.0000 | 0.0007 | -0.0010 |
| normale_weltspannung->leise_duenn | 2 | neutral | neutral:2 | 0.0025 | 0.0000 | 0.0008 | -0.0010 |
| ruhig_zentrumsnah->randlastige_sinneslage | 2 | beruhigend | beruhigend:2 | 0.0000 | -0.0075 | 0.0014 | -0.0019 |
| lauter_feldkontakt->ruhig_zentrumsnah | 1 | neutral | neutral:1 | 0.0250 | 0.0000 | 0.0007 | -0.0010 |
| leise_duenn->leise_duenn | 1 | neutral | neutral:1 | 0.0100 | 0.0000 | 0.0006 | -0.0008 |
| offen_suchend->leise_duenn | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0007 | -0.0010 |
| randlastige_sinneslage->lauter_feldkontakt | 1 | beruhigend | beruhigend:1 | 0.0100 | -0.0050 | 0.0010 | -0.0014 |
| randlastige_sinneslage->leise_duenn | 1 | neutral | neutral:1 | 0.0050 | 0.0000 | 0.0005 | -0.0006 |

## Haeufigste Rohfolgen

- `normale_weltspannung->normale_weltspannung`: `65`
- `offen_suchend->offen_suchend`: `42`
- `offen_suchend->normale_weltspannung`: `26`
- `normale_weltspannung->offen_suchend`: `22`
- `offen_suchend->randlastige_sinneslage`: `19`
- `randlastige_sinneslage->offen_suchend`: `18`
- `normale_weltspannung->ruhig_zentrumsnah`: `15`
- `normale_weltspannung->lauter_feldkontakt`: `14`
- `randlastige_sinneslage->normale_weltspannung`: `14`
- `ruhig_zentrumsnah->normale_weltspannung`: `13`
- `lauter_feldkontakt->lauter_feldkontakt`: `12`
- `ruhig_zentrumsnah->ruhig_zentrumsnah`: `12`

## Bewertung

Die Folge-Memory ist passiv. Sie zeigt, ob eine Lagefolge nach der Rezeptorhaltung eher beruhigt, neutral bleibt oder verschoben wird.

Wichtig ist: Damit wird Aufnahmequalitaet zeitlich lesbar. Eine Weltlage ist nicht nur ein Zustand, sondern Teil einer Folge.
