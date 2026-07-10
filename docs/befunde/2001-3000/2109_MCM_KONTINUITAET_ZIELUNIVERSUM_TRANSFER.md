# 2109 - Transfer der MCM-Quellform zwischen getrennten Zieluniversen

## Zweck

Befund 2108 zeigt die Quellform in allen 35 ausgeglichenen Aufteilungen eines
festen datenblind gewaehlten Zieluniversums. Offen blieb, ob dieselbe
Vorweltform auch zwischen zwei vollstaendig getrennten Saetzen nachfolgender
Welten erkennbar bleibt.

2109 prueft deshalb:

```text
Vorwelt -> acht Zielwelten des Universums A

gegen

dieselbe Vorwelt -> acht andere Zielwelten des Universums B
```

Die Zielwelten ueberlappen nicht. Herkunftslabel, Asset, Jahr und Weltname
werden dem Feld nicht gegeben.

## Datenblinde Universumsbildung

Jeder Datenbestand wird erneut ausschliesslich nach SHA-256 des vorhandenen
Weltenschluessels geordnet:

- die ersten acht Welten bilden Zieluniversum A,
- die naechsten acht bilden Zieluniversum B,
- alle verbleibenden Welten bilden die Vorweltidentitaeten.

| Bestand | Universum A | Universum B | Vorwelten |
|---|---:|---:|---:|
| 2091-Bestand | 8 | 8 | 48 |
| 2092-Holdout | 8 | 8 | 44 |

Keine Zielwelt ist zugleich Vorwelt. Keine Zielwelt kommt in beiden Universen
vor.

## Unterschiedliche Kontextzusammensetzung

Die Hashauswahl erzeugt ohne Ergebniswissen deutlich verschiedene
Zielmischungen.

Im 2091-Bestand enthaelt Universum A:

- drei SOL-2024-, drei BTC-2025-, ein BTC-2024- und ein SOL-2025-Fenster.

Universum B enthaelt:

- vier SOL-2025-, drei BTC-2025- und ein BTC-2024-Fenster,
- kein SOL-2024-Ziel.

Im Holdout enthaelt Universum A:

- XRP 2024/2025 und PAXG 2024/2025,
- kein DOGE-Ziel.

Universum B enthaelt:

- DOGE 2024/2025, XRP 2025 und PAXG 2025,
- kein XRP-2024- oder PAXG-2024-Ziel.

Die Quellform muss damit ueber einen echten Wechsel der Zielzusammensetzung
tragen.

## Formprofil

Fuer jede Vorwelt werden die schwellenfreien gerichteten Rangwechsel aus 66
Neuronenpaaren getrennt in beiden Zieluniversen gesammelt. Jedes Universum
liefert acht Quell-Ziel-Pfade. Anschliessend wird jedes Profil durch seine
gesamte Wechselzahl geteilt.

Verglichen wird damit nur die relative Verteilung der Rangwechsel:

- keine absolute Nachhallstaerke,
- keine feste Rangbedeutung,
- keine Gewichtung der Neuronenpaare,
- kein Lernen oder Memory,
- keine Feld- oder Handlungsrueckwirkung.

Die Manhattan-Distanz, Identitaets-AUC und exakte Tiebehandlung bleiben
unveraendert zu 2107 und 2108.

## Globaler Universumstransfer

| Bestand | Richtung | Kandidaten | Median Identitaetsrang | mittlere AUC | eindeutig naechste Identitaet |
|---|---|---:|---:|---:|---:|
| 2091 | A nach B | 48 | 5 | 0,862 | 6 |
| 2091 | B nach A | 48 | 4 | 0,852 | 9 |
| 2092 | A nach B | 44 | 3 | 0,887 | 10 |
| 2092 | B nach A | 44 | 5,5 | 0,859 | 7 |

Die Quellform bleibt damit auch gegen alle anderen Assets und Jahre des
jeweiligen Bestands klar unterscheidbar.

## Strenge Kontrolle innerhalb Asset und Jahr

Die Vorwelt konkurriert zusaetzlich nur mit anderen Fenstern desselben Assets
und Jahres. Dadurch kann weder Asset- noch Jahreszugehoerigkeit die
Wiedererkennung tragen.

| Bestand | Richtung | Kandidaten je Gruppe | Median Identitaetsrang | mittlere AUC | eindeutig naechste Identitaet |
|---|---|---:|---:|---:|---:|
| 2091 | A nach B | 10 bis 14 | 2 | 0,866 | 21/48 |
| 2091 | B nach A | 10 bis 14 | 2 | 0,859 | 22/48 |
| 2092 | A nach B | 6 bis 9 | 1 | 0,888 | 24/44 |
| 2092 | B nach A | 6 bis 9 | 1,5 | 0,869 | 22/44 |

In drei der vier Pruefungen liegt die gleiche Vorwelt fuer mindestens die
Haelfte aller Quellen als eindeutig naechstes Profil oder direkt an dieser
Grenze. Die mittlere Trennung ist in beiden Bestaenden und Richtungen hoch.

## Labelnull

Die Herkunftslabels werden 4.096-mal zwischen unveraenderten Profilen
vertauscht. In der strengen Kontrolle geschieht dies nur innerhalb desselben
Assets und Jahres.

| Bestand | Richtung | beobachtete AUC | mittlere Null-AUC | hoechste Null-AUC | empirisches p |
|---|---|---:|---:|---:|---:|
| 2091 | A nach B | 0,866 | 0,499 | 0,658 | 0,000244 |
| 2091 | B nach A | 0,859 | 0,500 | 0,671 | 0,000244 |
| 2092 | A nach B | 0,888 | 0,501 | 0,664 | 0,000244 |
| 2092 | B nach A | 0,869 | 0,499 | 0,663 | 0,000244 |

Jeder beobachtete Wert liegt ueber allen 4.096 zugehoerigen Labelnullen. Auch
die Zahl eindeutig naechster Identitaeten liegt in allen acht globalen und
gruppeninternen Auswertungen oberhalb jeder Null.

## Breite und Ausnahmen

Innerhalb gleicher Assets und Jahre liegen ueber AUC 0,5:

- 44 von 48 und 45 von 48 Vorwelten im 2091-Bestand,
- 42 von 44 Vorwelten in beiden Holdout-Richtungen.

Die individuellen AUC-Werte reichen dennoch bis 0,269 beziehungsweise 0,385
im 2091-Bestand und bis 0,333 im Holdout. Einige konkrete Vorzustaende verlieren
ihre Formtrennung beim Wechsel des Zieluniversums.

Die Quellform ist deshalb breit und universumsuebergreifend, aber weiterhin
keine unveraenderliche Signatur jeder einzelnen Vorwelt.

## Mechanische Selbstbegrenzung

Es entstehen 768 Quell-Ziel-Pfade im 2091-Bestand und 704 im Holdout. 767 von
768 beziehungsweise 704 von 704 enthalten mindestens einen neuronalen
Rangwechsel. Kein Universumsprofil bleibt leer.

Alle 1.472 Feldpfade konvergieren bitgenau zum Resetfeld. Der spaeteste
Konvergenztick liegt bei 305 beziehungsweise 316. Der Transfer beruht damit auf
voruebergehender Feldform, nicht auf dauerhaft getrennten Endzustaenden.

## Befund

Getragen sind:

- Wiedererkennung derselben Vorwelt zwischen zwei disjunkten Zieluniversen,
- Transfer trotz deutlich verschiedener Asset- und Jahreszusammensetzung,
- hohe Trennung nach Entfernung der absoluten Nachhallstaerke,
- Erhalt innerhalb gleicher Assets und Jahre,
- breite Beteiligung der Vorwelten in Entwicklungsbestand und Holdout,
- vollstaendige spaetere Konvergenz aller 1.472 Feldpfade.

Nicht getragen sind:

- universelle Erkennbarkeit jeder einzelnen Vorwelt,
- ein festes oder dauerhaftes Identitaetssymbol,
- Stabilitaet ausserhalb der vorhandenen historischen Datenbestaende,
- eine vom Feld selbst ausgefuehrte Wiedererkennung,
- episodisches Memory, Semantik, autonome Aktivitaet oder Handlung.

2109 zeigt, dass die quellgebundene Mikrotopologie nicht an einen einzelnen
Satz nachfolgender Welten gebunden ist. Der Vorzustand traegt eine relationale
Form, die auch unter einem anderen Zieluniversum wiedererkennbar bleibt.

Damit liegt eine deutlich staerkere mechanische Grundlage fuer organisch
entstehende Innenidentitaet vor als nach 2107. Die Identitaet ist jedoch noch
nur von aussen im Feldverlauf messbar. DIO selbst bildet daraus weder ein Wort
noch eine Erinnerung oder Handlung.

## Reproduzierbare Ausgaben

- `2109_MCM_KONTINUITAET_ZIELUNIVERSUM_TRANSFER.sources.csv`
- `2109_MCM_KONTINUITAET_ZIELUNIVERSUM_TRANSFER.summary.csv`

Der Runner ist `tools/run_mcm_continuity_target_universe_transfer.py`. Er
erzeugt keine Welt-, Runtime-, Memory- oder Debugdateien.
