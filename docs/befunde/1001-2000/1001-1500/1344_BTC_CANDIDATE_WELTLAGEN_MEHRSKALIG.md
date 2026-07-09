# Mehrskalige Weltlagen-Folgememory

Diese Auswertung vergleicht dieselben Lagefolgen ueber mehrere zeitliche Lesetiefen.

Verwendete Skalen:

- Block `100`: kurze Lagebewegung
- Block `200`: mittlere Lagefolge
- Block `400`: laengere Feldphase

## Profilverteilung

- `stabil_neutral`: `19`
- `skalenabhaengig_neutral_beruhigend`: `14`
- `stabil_beruhigend`: `8`
- `gemischt`: `1`

## Stabilste Folgen

| Lagefolge | Skalen | Profil | Vorkommen | 100 | 200 | 400 | dRand | dRekopplung |
|---|---:|---|---:|---|---|---|---:|---:|
| normale_weltspannung->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 144 | neutral | neutral | beruhigend | -0.0026 | 0.0008 |
| offen_suchend->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 60 | neutral | beruhigend | beruhigend | -0.0023 | 0.0008 |
| normale_weltspannung->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 58 | neutral | beruhigend | beruhigend | -0.0031 | 0.0011 |
| offen_suchend->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 49 | neutral | neutral | beruhigend | -0.0023 | 0.0012 |
| randlastige_sinneslage->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 33 | neutral | neutral | beruhigend | -0.0028 | 0.0008 |
| normale_weltspannung->lauter_feldkontakt | 3 | stabil_neutral | 32 | neutral | neutral | neutral | -0.0027 | 0.0009 |
| normale_weltspannung->randlastige_sinneslage | 3 | stabil_beruhigend | 31 | beruhigend | beruhigend | beruhigend | -0.0137 | 0.0013 |
| lauter_feldkontakt->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 30 | neutral | beruhigend | beruhigend | -0.0034 | 0.0008 |
| randlastige_sinneslage->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 29 | neutral | beruhigend | beruhigend | -0.0034 | 0.0013 |
| lauter_feldkontakt->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 27 | neutral | beruhigend | beruhigend | -0.0029 | 0.0008 |
| offen_suchend->randlastige_sinneslage | 3 | stabil_beruhigend | 26 | beruhigend | beruhigend | beruhigend | -0.0108 | 0.0015 |
| randlastige_sinneslage->randlastige_sinneslage | 3 | stabil_beruhigend | 22 | beruhigend | beruhigend | beruhigend | -0.0123 | 0.0012 |
| normale_weltspannung->ruhig_zentrumsnah | 3 | stabil_neutral | 16 | neutral | neutral | neutral | 0.0000 | 0.0005 |
| leise_duenn->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 15 | neutral | beruhigend | beruhigend | -0.0022 | 0.0008 |
| normale_weltspannung->leise_duenn | 3 | stabil_neutral | 11 | neutral | neutral | neutral | -0.0004 | 0.0008 |
| randlastige_sinneslage->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 9 | neutral | beruhigend | beruhigend | -0.0041 | 0.0008 |
| lauter_feldkontakt->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 7 | neutral | neutral | beruhigend | -0.0008 | 0.0012 |
| leise_duenn->leise_duenn | 3 | skalenabhaengig_neutral_beruhigend | 6 | neutral | beruhigend | beruhigend | -0.0028 | 0.0008 |
| lauter_feldkontakt->randlastige_sinneslage | 2 | stabil_beruhigend | 17 | beruhigend | beruhigend | - | -0.0120 | 0.0011 |
| ruhig_zentrumsnah->normale_weltspannung | 2 | skalenabhaengig_neutral_beruhigend | 15 | neutral | - | beruhigend | -0.0029 | 0.0007 |
| offen_suchend->leise_duenn | 2 | stabil_neutral | 7 | neutral | neutral | - | -0.0010 | 0.0008 |
| ruhig_zentrumsnah->lauter_feldkontakt | 2 | skalenabhaengig_neutral_beruhigend | 5 | neutral | beruhigend | - | -0.0029 | 0.0007 |
| lauter_feldkontakt->ruhig_zentrumsnah | 2 | stabil_neutral | 4 | neutral | neutral | - | -0.0017 | 0.0005 |
| normale_weltspannung->leise_scharf_duenn | 2 | stabil_neutral | 4 | neutral | neutral | - | 0.0000 | 0.0005 |
| leise_scharf_duenn->normale_weltspannung | 2 | stabil_neutral | 2 | neutral | neutral | - | 0.0000 | 0.0005 |

## Bewertung

Die mehrskalige Diagnose trennt drei Lesetiefen:

- kurze Lagebewegung
- mittlere Lagefolge
- laengere Feldphase

Wenn eine Lagefolge ueber alle Skalen gleich lesbar bleibt, ist sie ein robusterer Kandidat fuer Feldzeit-Ordnung.

Wenn sie je nach Skala kippt, ist sie nicht falsch, sondern zeitlich empfindlich: Die Wirkung entsteht erst ueber Dauer oder zerfaellt bei feiner Lesung.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung und keine Steuerung.

Wie es weitergeht: Als naechstes sollten die skalenabhaengigen Folgen gegen konkrete Rohweltfenster gelesen werden, damit sichtbar wird, welche Weltbewegung eine neutrale Kurzlage in eine beruhigende laengere Feldphase ueberfuehrt.
