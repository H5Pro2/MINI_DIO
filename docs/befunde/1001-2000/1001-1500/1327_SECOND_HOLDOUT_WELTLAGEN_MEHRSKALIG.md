# Mehrskalige Weltlagen-Folgememory

Diese Auswertung vergleicht dieselben Lagefolgen ueber mehrere zeitliche Lesetiefen.

Verwendete Skalen:

- Block `100`: kurze Lagebewegung
- Block `200`: mittlere Lagefolge
- Block `400`: laengere Feldphase

## Profilverteilung

- `stabil_neutral`: `21`
- `skalenabhaengig_neutral_beruhigend`: `13`
- `stabil_beruhigend`: `6`

## Stabilste Folgen

| Lagefolge | Skalen | Profil | Vorkommen | 100 | 200 | 400 | dRand | dRekopplung |
|---|---:|---|---:|---|---|---|---:|---:|
| normale_weltspannung->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 210 | neutral | neutral | beruhigend | -0.0027 | 0.0008 |
| offen_suchend->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 148 | neutral | neutral | beruhigend | -0.0032 | 0.0013 |
| offen_suchend->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 85 | neutral | beruhigend | beruhigend | -0.0027 | 0.0009 |
| normale_weltspannung->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 71 | neutral | beruhigend | beruhigend | -0.0040 | 0.0012 |
| randlastige_sinneslage->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 56 | neutral | neutral | beruhigend | -0.0040 | 0.0013 |
| ruhig_zentrumsnah->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 54 | neutral | neutral | beruhigend | -0.0014 | 0.0008 |
| normale_weltspannung->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 52 | neutral | beruhigend | neutral | -0.0025 | 0.0011 |
| normale_weltspannung->ruhig_zentrumsnah | 3 | stabil_neutral | 50 | neutral | neutral | neutral | -0.0002 | 0.0005 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 3 | stabil_neutral | 50 | neutral | neutral | neutral | -0.0004 | 0.0006 |
| offen_suchend->randlastige_sinneslage | 3 | stabil_beruhigend | 48 | beruhigend | beruhigend | beruhigend | -0.0110 | 0.0016 |
| normale_weltspannung->randlastige_sinneslage | 3 | stabil_beruhigend | 47 | beruhigend | beruhigend | beruhigend | -0.0111 | 0.0013 |
| randlastige_sinneslage->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 43 | neutral | neutral | beruhigend | -0.0026 | 0.0008 |
| lauter_feldkontakt->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 40 | neutral | neutral | beruhigend | -0.0032 | 0.0009 |
| lauter_feldkontakt->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 33 | neutral | neutral | beruhigend | -0.0025 | 0.0012 |
| lauter_feldkontakt->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 30 | neutral | beruhigend | beruhigend | -0.0038 | 0.0012 |
| offen_suchend->lauter_feldkontakt | 3 | stabil_beruhigend | 22 | beruhigend | beruhigend | beruhigend | -0.0053 | 0.0015 |
| offen_suchend->ruhig_zentrumsnah | 3 | stabil_neutral | 18 | neutral | neutral | neutral | -0.0004 | 0.0005 |
| ruhig_zentrumsnah->offen_suchend | 3 | stabil_neutral | 14 | neutral | neutral | neutral | -0.0019 | 0.0012 |
| leise_duenn->ruhig_zentrumsnah | 3 | stabil_neutral | 13 | neutral | neutral | neutral | 0.0000 | 0.0006 |
| ruhig_zentrumsnah->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 13 | neutral | beruhigend | beruhigend | -0.0028 | 0.0012 |
| normale_weltspannung->leise_duenn | 3 | stabil_neutral | 9 | neutral | neutral | neutral | 0.0000 | 0.0008 |
| randlastige_sinneslage->randlastige_sinneslage | 2 | stabil_beruhigend | 24 | beruhigend | beruhigend | - | -0.0128 | 0.0015 |
| lauter_feldkontakt->randlastige_sinneslage | 2 | stabil_beruhigend | 11 | beruhigend | beruhigend | - | -0.0179 | 0.0014 |
| ruhig_zentrumsnah->leise_duenn | 2 | stabil_neutral | 9 | neutral | neutral | - | -0.0017 | 0.0007 |
| lauter_feldkontakt->ruhig_zentrumsnah | 2 | stabil_neutral | 8 | neutral | neutral | - | 0.0000 | 0.0006 |

## Bewertung

Die mehrskalige Diagnose trennt drei Lesetiefen:

- kurze Lagebewegung
- mittlere Lagefolge
- laengere Feldphase

Wenn eine Lagefolge ueber alle Skalen gleich lesbar bleibt, ist sie ein robusterer Kandidat fuer Feldzeit-Ordnung.

Wenn sie je nach Skala kippt, ist sie nicht falsch, sondern zeitlich empfindlich: Die Wirkung entsteht erst ueber Dauer oder zerfaellt bei feiner Lesung.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung und keine Steuerung.

Wie es weitergeht: Als naechstes sollten die skalenabhaengigen Folgen gegen konkrete Rohweltfenster gelesen werden, damit sichtbar wird, welche Weltbewegung eine neutrale Kurzlage in eine beruhigende laengere Feldphase ueberfuehrt.
