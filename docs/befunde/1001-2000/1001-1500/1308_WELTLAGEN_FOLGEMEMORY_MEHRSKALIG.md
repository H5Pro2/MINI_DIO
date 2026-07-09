# Mehrskalige Weltlagen-Folgememory

Diese Auswertung vergleicht dieselben Lagefolgen ueber mehrere zeitliche Lesetiefen.

Verwendete Skalen:

- Block `100`: kurze Lagebewegung
- Block `200`: mittlere Lagefolge
- Block `400`: laengere Feldphase

## Profilverteilung

- `stabil_neutral`: `32`
- `skalenabhaengig_neutral_beruhigend`: `14`
- `stabil_beruhigend`: `9`

## Stabilste Folgen

| Lagefolge | Skalen | Profil | Vorkommen | 100 | 200 | 400 | dRand | dRekopplung |
|---|---:|---|---:|---|---|---|---:|---:|
| ueberstabil_extrem_leise_scharf->ueberstabil_extrem_leise_scharf | 3 | stabil_neutral | 260 | neutral | neutral | neutral | -0.0000 | 0.0000 |
| normale_weltspannung->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 255 | neutral | neutral | beruhigend | -0.0023 | 0.0008 |
| offen_suchend->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 130 | neutral | neutral | beruhigend | -0.0029 | 0.0013 |
| offen_suchend->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 106 | neutral | beruhigend | beruhigend | -0.0026 | 0.0008 |
| normale_weltspannung->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 89 | neutral | beruhigend | beruhigend | -0.0039 | 0.0012 |
| randlastige_sinneslage->randlastige_sinneslage | 3 | stabil_beruhigend | 86 | beruhigend | beruhigend | beruhigend | -0.0447 | 0.0013 |
| randlastige_sinneslage->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 71 | neutral | beruhigend | beruhigend | -0.0030 | 0.0013 |
| normale_weltspannung->ruhig_zentrumsnah | 3 | stabil_neutral | 70 | neutral | neutral | neutral | -0.0005 | 0.0005 |
| ruhig_zentrumsnah->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 66 | neutral | neutral | beruhigend | -0.0018 | 0.0008 |
| normale_weltspannung->randlastige_sinneslage | 3 | stabil_beruhigend | 63 | beruhigend | beruhigend | beruhigend | -0.0101 | 0.0013 |
| randlastige_sinneslage->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 63 | neutral | beruhigend | beruhigend | -0.0032 | 0.0008 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 3 | stabil_neutral | 61 | neutral | neutral | neutral | -0.0005 | 0.0006 |
| normale_weltspannung->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 57 | neutral | beruhigend | neutral | -0.0023 | 0.0011 |
| offen_suchend->randlastige_sinneslage | 3 | stabil_beruhigend | 54 | beruhigend | beruhigend | beruhigend | -0.0112 | 0.0016 |
| lauter_feldkontakt->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 43 | neutral | beruhigend | beruhigend | -0.0037 | 0.0009 |
| lauter_feldkontakt->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 24 | neutral | beruhigend | neutral | -0.0036 | 0.0013 |
| lauter_feldkontakt->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 22 | neutral | beruhigend | beruhigend | -0.0027 | 0.0012 |
| ruhig_zentrumsnah->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 17 | neutral | beruhigend | beruhigend | -0.0028 | 0.0012 |
| offen_suchend->ruhig_zentrumsnah | 3 | stabil_neutral | 15 | neutral | neutral | neutral | -0.0004 | 0.0005 |
| leise_duenn->ruhig_zentrumsnah | 3 | stabil_neutral | 13 | neutral | neutral | neutral | 0.0000 | 0.0006 |
| normale_weltspannung->leise_duenn | 3 | stabil_neutral | 9 | neutral | neutral | neutral | 0.0000 | 0.0007 |
| randlastige_sinneslage->ueberstabil_mit_randreiz | 3 | skalenabhaengig_neutral_beruhigend | 7 | beruhigend | beruhigend | neutral | -0.0333 | 0.0006 |
| ueberstabil_mit_randreiz->randlastige_sinneslage | 3 | stabil_beruhigend | 7 | beruhigend | beruhigend | beruhigend | -0.0600 | 0.0011 |
| ueberstabil_gemischt->ueberstabil_gemischt | 3 | stabil_neutral | 6 | neutral | neutral | neutral | 0.0000 | 0.0000 |
| ueberstabil_gemischt->ruhig_zentrumsnah | 3 | stabil_neutral | 5 | neutral | neutral | neutral | 0.0000 | 0.0000 |

## Bewertung

Die mehrskalige Diagnose trennt drei Lesetiefen:

- kurze Lagebewegung
- mittlere Lagefolge
- laengere Feldphase

Wenn eine Lagefolge ueber alle Skalen gleich lesbar bleibt, ist sie ein robusterer Kandidat fuer Feldzeit-Ordnung.

Wenn sie je nach Skala kippt, ist sie nicht falsch, sondern zeitlich empfindlich: Die Wirkung entsteht erst ueber Dauer oder zerfaellt bei feiner Lesung.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung und keine Steuerung.

Wie es weitergeht: Als naechstes sollten die skalenabhaengigen Folgen gegen konkrete Rohweltfenster gelesen werden, damit sichtbar wird, welche Weltbewegung eine neutrale Kurzlage in eine beruhigende laengere Feldphase ueberfuehrt.
