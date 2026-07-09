# Mehrskalige Weltlagen-Folgememory

Diese Auswertung vergleicht dieselben Lagefolgen ueber mehrere zeitliche Lesetiefen.

Verwendete Skalen:

- Block `100`: kurze Lagebewegung
- Block `200`: mittlere Lagefolge
- Block `400`: laengere Feldphase

## Profilverteilung

- `stabil_neutral`: `17`
- `skalenabhaengig_neutral_beruhigend`: `14`
- `stabil_beruhigend`: `5`
- `skalenabhaengig_mit_verschiebung`: `1`

## Stabilste Folgen

| Lagefolge | Skalen | Profil | Vorkommen | 100 | 200 | 400 | dRand | dRekopplung |
|---|---:|---|---:|---|---|---|---:|---:|
| normale_weltspannung->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 198 | neutral | neutral | beruhigend | -0.0023 | 0.0008 |
| offen_suchend->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 114 | neutral | beruhigend | beruhigend | -0.0026 | 0.0014 |
| offen_suchend->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 72 | neutral | beruhigend | beruhigend | -0.0037 | 0.0008 |
| normale_weltspannung->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 66 | neutral | beruhigend | beruhigend | -0.0035 | 0.0013 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 3 | stabil_neutral | 55 | neutral | neutral | neutral | -0.0007 | 0.0006 |
| normale_weltspannung->ruhig_zentrumsnah | 3 | stabil_neutral | 44 | neutral | neutral | neutral | -0.0004 | 0.0006 |
| ruhig_zentrumsnah->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 37 | neutral | neutral | beruhigend | -0.0019 | 0.0008 |
| lauter_feldkontakt->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 33 | neutral | beruhigend | neutral | -0.0019 | 0.0008 |
| normale_weltspannung->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 33 | neutral | neutral | beruhigend | -0.0026 | 0.0011 |
| randlastige_sinneslage->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 30 | neutral | beruhigend | beruhigend | -0.0037 | 0.0009 |
| normale_weltspannung->randlastige_sinneslage | 3 | stabil_beruhigend | 27 | beruhigend | beruhigend | beruhigend | -0.0108 | 0.0013 |
| randlastige_sinneslage->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 21 | neutral | neutral | beruhigend | -0.0029 | 0.0013 |
| offen_suchend->randlastige_sinneslage | 3 | stabil_beruhigend | 18 | beruhigend | beruhigend | beruhigend | -0.0131 | 0.0015 |
| lauter_feldkontakt->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 17 | neutral | neutral | beruhigend | -0.0032 | 0.0009 |
| lauter_feldkontakt->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 17 | neutral | neutral | beruhigend | -0.0035 | 0.0014 |
| randlastige_sinneslage->randlastige_sinneslage | 3 | stabil_beruhigend | 13 | beruhigend | beruhigend | beruhigend | -0.0115 | 0.0014 |
| ruhig_zentrumsnah->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 9 | neutral | beruhigend | beruhigend | -0.0028 | 0.0006 |
| offen_suchend->lauter_feldkontakt | 2 | stabil_neutral | 12 | neutral | neutral | - | -0.0009 | 0.0011 |
| leise_duenn->normale_weltspannung | 2 | skalenabhaengig_neutral_beruhigend | 10 | neutral | beruhigend | - | -0.0024 | 0.0008 |
| normale_weltspannung->leise_duenn | 2 | stabil_neutral | 8 | neutral | neutral | - | -0.0010 | 0.0008 |
| leise_duenn->offen_suchend | 2 | stabil_neutral | 7 | neutral | neutral | - | -0.0017 | 0.0012 |
| offen_suchend->leise_duenn | 2 | stabil_neutral | 7 | neutral | neutral | - | 0.0000 | 0.0007 |
| ruhig_zentrumsnah->randlastige_sinneslage | 2 | skalenabhaengig_mit_verschiebung | 6 | verschiebend | beruhigend | - | -0.0142 | 0.0012 |
| lauter_feldkontakt->randlastige_sinneslage | 2 | stabil_beruhigend | 5 | beruhigend | beruhigend | - | -0.0104 | 0.0012 |
| leise_scharf_duenn->normale_weltspannung | 2 | stabil_neutral | 4 | neutral | neutral | - | 0.0000 | 0.0008 |

## Bewertung

Die mehrskalige Diagnose trennt drei Lesetiefen:

- kurze Lagebewegung
- mittlere Lagefolge
- laengere Feldphase

Wenn eine Lagefolge ueber alle Skalen gleich lesbar bleibt, ist sie ein robusterer Kandidat fuer Feldzeit-Ordnung.

Wenn sie je nach Skala kippt, ist sie nicht falsch, sondern zeitlich empfindlich: Die Wirkung entsteht erst ueber Dauer oder zerfaellt bei feiner Lesung.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung und keine Steuerung.
