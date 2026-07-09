# 1381 - Feldfunktionskarte: globale passive Probe

## Zweck

Diese Diagnose liest groessere vorhandene `episodes.csv` rollenneutral in lokale Feldphasen.

Erst danach wird nur eine Naehe zu bekannten Feldfunktionen markiert:

- Brueckennaehe
- Zentrumsnaehe
- Randdrucknaehe
- Entlastungsnaehe
- Mischrolle

Wichtig: Diese Naehen sind keine neuen Rollen und keine Handlung. Sie sind eine passive Gegenprobe fuer `1378`.

## Datengrundlage

- gelesene Weltfenster: `340`

## Rollennaehe gesamt

- `keine_naehe`: `171`
- `brueckennaehe`: `67`
- `mischrolle_brueckennaehe_zentrumsnaehe`: `65`
- `zentrumsnaehe`: `21`
- `entlastungsnaehe`: `7`
- `randdrucknaehe`: `5`
- `mischrolle_brueckennaehe_entlastungsnaehe`: `4`

## Rollennaehe je Welt

- `BTC_2024_5M`: keine_naehe:11 | brueckennaehe:4 | mischrolle_brueckennaehe_zentrumsnaehe:3 | randdrucknaehe:1 | zentrumsnaehe:1
- `DOGE_2024_5M`: keine_naehe:51 | mischrolle_brueckennaehe_zentrumsnaehe:19 | brueckennaehe:18 | zentrumsnaehe:9 | mischrolle_brueckennaehe_entlastungsnaehe:2 | randdrucknaehe:1
- `PAXG_2024_5M`: keine_naehe:51 | mischrolle_brueckennaehe_zentrumsnaehe:20 | brueckennaehe:17 | entlastungsnaehe:6 | zentrumsnaehe:3 | mischrolle_brueckennaehe_entlastungsnaehe:2 | randdrucknaehe:1
- `SOL_2024_5M`: keine_naehe:11 | brueckennaehe:4 | mischrolle_brueckennaehe_zentrumsnaehe:4 | randdrucknaehe:1
- `XRP_2024_5M`: keine_naehe:47 | brueckennaehe:24 | mischrolle_brueckennaehe_zentrumsnaehe:19 | zentrumsnaehe:8 | randdrucknaehe:1 | entlastungsnaehe:1

## Nachhallhinweis

- `keine_naehe` mit Preview-Folgecarry: `140`
- `brueckennaehe` mit Preview-Folgecarry: `58`
- `mischrolle_brueckennaehe_zentrumsnaehe` mit Preview-Folgecarry: `56`
- `zentrumsnaehe` mit Preview-Folgecarry: `14`
- `entlastungsnaehe` mit Preview-Folgecarry: `5`
- `randdrucknaehe` mit Preview-Folgecarry: `3`
- `mischrolle_brueckennaehe_entlastungsnaehe` mit Preview-Folgecarry: `3`

## Lesung

Die globale Probe erzeugt bewusst keine harte Rollenentscheidung.

Wenn eine bekannte Naehe in groesseren Episodensets wieder auftaucht, spricht das fuer eine allgemeinere Feldfunktion.
Wenn Mischrollen oder `keine_naehe` dominieren, bleibt die bisherige Karte eher mikrophasen- oder weltspannungsgebunden.

Der Befund ist differenziert:

- Brueckennaehe erscheint deutlich und weltuebergreifend.
- Zentrumsnaehe erscheint, aber haeufig als Mischrolle mit Brueckennaehe.
- Randdrucknaehe erscheint selten und wirkt ausserhalb des Kandidatenraums spezieller.
- `keine_naehe` dominiert, was wichtig ist: Die Karte wird nicht wahllos auf jede Feldphase projiziert.

Damit wirkt Bruecke aktuell am ehesten wie eine allgemeinere Feldfunktion.
Zentrumskontakt wirkt global lesbar, aber oft mit Uebergangsnaehe verschraenkt.
Randdruck bleibt eher ein spezieller Rand-/Druckzustand.

## Grenze

Die Naeheklassifikation ist relativ je Welt kalibriert. Sie vergleicht also nicht BTC, SOL, PAXG usw. mit festen absoluten Werten.

Das verhindert eine mechanische Uebertragung, ersetzt aber keine spaetere Positiv-/Negativkontrolle.
