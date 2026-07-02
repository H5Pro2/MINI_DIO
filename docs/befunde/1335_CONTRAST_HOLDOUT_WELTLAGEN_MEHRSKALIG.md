# Mehrskalige Weltlagen-Folgememory

Diese Auswertung vergleicht dieselben Lagefolgen ueber mehrere zeitliche Lesetiefen.

Verwendete Skalen:

- Block `100`: kurze Lagebewegung
- Block `200`: mittlere Lagefolge
- Block `400`: laengere Feldphase

## Profilverteilung

- `skalenabhaengig_neutral_beruhigend`: `18`
- `stabil_neutral`: `15`
- `stabil_beruhigend`: `6`

## Stabilste Folgen

| Lagefolge | Skalen | Profil | Vorkommen | 100 | 200 | 400 | dRand | dRekopplung |
|---|---:|---|---:|---|---|---|---:|---:|
| normale_weltspannung->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 300 | neutral | neutral | beruhigend | -0.0027 | 0.0008 |
| offen_suchend->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 150 | neutral | neutral | beruhigend | -0.0033 | 0.0013 |
| offen_suchend->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 119 | neutral | neutral | beruhigend | -0.0028 | 0.0008 |
| normale_weltspannung->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 100 | neutral | beruhigend | beruhigend | -0.0036 | 0.0012 |
| normale_weltspannung->ruhig_zentrumsnah | 3 | stabil_neutral | 82 | neutral | neutral | neutral | -0.0007 | 0.0005 |
| randlastige_sinneslage->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 76 | neutral | beruhigend | beruhigend | -0.0025 | 0.0013 |
| ruhig_zentrumsnah->ruhig_zentrumsnah | 3 | stabil_neutral | 73 | neutral | neutral | neutral | -0.0010 | 0.0005 |
| ruhig_zentrumsnah->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 70 | neutral | neutral | beruhigend | -0.0025 | 0.0008 |
| normale_weltspannung->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 67 | neutral | beruhigend | beruhigend | -0.0030 | 0.0011 |
| lauter_feldkontakt->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 64 | neutral | beruhigend | beruhigend | -0.0029 | 0.0009 |
| normale_weltspannung->randlastige_sinneslage | 3 | stabil_beruhigend | 63 | beruhigend | beruhigend | beruhigend | -0.0112 | 0.0013 |
| offen_suchend->randlastige_sinneslage | 3 | stabil_beruhigend | 58 | beruhigend | beruhigend | beruhigend | -0.0125 | 0.0016 |
| randlastige_sinneslage->normale_weltspannung | 3 | skalenabhaengig_neutral_beruhigend | 57 | neutral | neutral | beruhigend | -0.0028 | 0.0008 |
| randlastige_sinneslage->randlastige_sinneslage | 3 | stabil_beruhigend | 41 | beruhigend | beruhigend | beruhigend | -0.0124 | 0.0015 |
| lauter_feldkontakt->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 25 | neutral | beruhigend | beruhigend | -0.0044 | 0.0008 |
| lauter_feldkontakt->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 25 | neutral | beruhigend | beruhigend | -0.0048 | 0.0014 |
| ruhig_zentrumsnah->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 16 | neutral | neutral | beruhigend | -0.0022 | 0.0007 |
| offen_suchend->ruhig_zentrumsnah | 3 | stabil_neutral | 11 | neutral | neutral | neutral | -0.0010 | 0.0005 |
| ruhig_zentrumsnah->offen_suchend | 3 | skalenabhaengig_neutral_beruhigend | 11 | neutral | beruhigend | beruhigend | -0.0046 | 0.0012 |
| randlastige_sinneslage->lauter_feldkontakt | 3 | skalenabhaengig_neutral_beruhigend | 7 | neutral | beruhigend | beruhigend | -0.0042 | 0.0009 |
| ruhig_zentrumsnah->randlastige_sinneslage | 2 | stabil_beruhigend | 18 | beruhigend | beruhigend | - | -0.0123 | 0.0012 |
| offen_suchend->lauter_feldkontakt | 2 | skalenabhaengig_neutral_beruhigend | 16 | neutral | beruhigend | - | -0.0041 | 0.0014 |
| lauter_feldkontakt->randlastige_sinneslage | 2 | stabil_beruhigend | 13 | beruhigend | beruhigend | - | -0.0104 | 0.0012 |
| leise_duenn->normale_weltspannung | 2 | skalenabhaengig_neutral_beruhigend | 12 | neutral | beruhigend | - | -0.0028 | 0.0008 |
| leise_duenn->offen_suchend | 2 | stabil_neutral | 12 | neutral | neutral | - | -0.0015 | 0.0012 |

## Bewertung

Die mehrskalige Diagnose trennt drei Lesetiefen:

- kurze Lagebewegung
- mittlere Lagefolge
- laengere Feldphase

Wenn eine Lagefolge ueber alle Skalen gleich lesbar bleibt, ist sie ein robusterer Kandidat fuer Feldzeit-Ordnung.

Wenn sie je nach Skala kippt, ist sie nicht falsch, sondern zeitlich empfindlich: Die Wirkung entsteht erst ueber Dauer oder zerfaellt bei feiner Lesung.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung und keine Steuerung.

Wie es weitergeht: Als naechstes sollten die skalenabhaengigen Folgen gegen konkrete Rohweltfenster gelesen werden, damit sichtbar wird, welche Weltbewegung eine neutrale Kurzlage in eine beruhigende laengere Feldphase ueberfuehrt.
