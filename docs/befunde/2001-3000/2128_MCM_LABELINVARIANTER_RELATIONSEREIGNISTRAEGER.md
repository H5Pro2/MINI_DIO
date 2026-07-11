# 2128 - Labelinvarianter MCM-Relationsereignistraeger

## Zweck

2126 lokalisierte eine offene Bruecke zwischen feldlokaler Eigenform und
erfahrungsgebildeter beweglicher Relevanz. 2127 zeigte anschliessend, dass der
globale Mittelwert eines Mikrofeldes als Informationsuebergang zu arm ist.

2128 sucht deshalb keine staerkere Kopplung, sondern prueft zuerst einen
kleineren feldlokalen Informationstraeger. Er muss waehrend des Kontakts
entstehen und darf weder Neuronenidentitaet noch feste Rolle, Schwelle,
Weltlabel oder globalen Feldmittelwert benoetigen.

## Relationsereignis

Zwischen zwei unmittelbar aufeinanderfolgenden Feldzustaenden bestehen bei
zwoelf Neuronen 66 paarweise Rangrelationen. Das Ereignis `C_t` ist exakt die
Anzahl der Relationen, deren Ordnung sich im aktuellen Tick geaendert hat:

```text
C_t = Anzahl geaenderter paarweiser Rangrelationen
```

Seine zeitliche Bewegung ist:

```text
D_t = C_t - C_(t-1)
```

`C_t` besitzt die natuerlichen Grenzen 0 bis 66. `D_t` besitzt die
natuerlichen Grenzen -66 bis +66. Es werden keine Werte gebinnt, geglaettet,
gewichtet oder semantisch benannt.

Die gleichzeitige beliebige Umbenennung aller Neuronen vertauscht nur die 66
Paare. Ihre Anzahl und damit `C_t` und `D_t` bleiben exakt gleich. Alle 94.208
gelesenen Zielpfad-Ticks bestehen die Relabel-Gegenprobe.

## Kontinuierliche Erfahrungsgrenze

Das Quellfeld wird ohne Reset in die Zielwelt fortgesetzt. Fuer den ersten
Zieltick wird `D_t` gegen das letzte tatsaechliche Relationsereignis der
Vorwelt gebildet. Es wird kein Parallel-, Reset- oder Nullfeld erzeugt.

Die Diagnose liest getrennt:

- nur die Verteilung von `C_t`,
- nur die Verteilung von `D_t`,
- beide Verteilungen gemeinsam.

Je Quelle werden acht Ziele in Universum A und acht disjunkte Ziele in
Universum B zusammengefasst. Verglichen wird die relative Ereignisform nach
1, 2, 4, 8, 16, 32 und 64 Kontaktticks.

## Umfang

- 48 Quellen und 768 Quell-Ziel-Pfade im Entwicklungsbestand,
- 44 Quellen und 704 Quell-Ziel-Pfade im unabhaengigen Holdout,
- insgesamt 1.472 kontinuierliche Pfade,
- 4.096 Herkunftslabelnullen je Richtung, Bestand, Praefix und Komponente,
- anonyme gegenseitige Naechste-Nachbar-Graphen ohne Quellenlabel.

## Staerkster Traeger

Die signierte Ereignisaenderung `D_t` ist die staerkste einzeln tragende
Komponente:

| Bestand | Ticks | A nach B AUC | B nach A AUC | hoechste Null A/B |
| --- | ---: | ---: | ---: | ---: |
| 2091 Basis | 1 | 0,828 | 0,831 | 0,654 / 0,629 |
| 2091 Basis | 2 | 0,834 | 0,817 | 0,660 / 0,620 |
| 2091 Basis | 4 | 0,704 | 0,665 | 0,615 / 0,617 |
| 2092 Holdout | 1 | 0,657 | 0,662 | 0,640 / 0,635 |
| 2092 Holdout | 2 | 0,659 | 0,649 | 0,643 / 0,624 |
| 2092 Holdout | 4 | 0,601 | 0,624 | 0,592 / 0,620 |

Alle zwoelf gerichteten Werte liegen ueber jeder ihrer 4.096 Labelnullen
(`p = 1/4097`). Ab Tick 8 traegt diese Richtung im Holdout nicht mehr
durchgehend. Die Quelleninformation ist damit frueh, reproduziert und
selbstbegrenzend.

Die reine Umbildungsbreite `C_t` traegt bei Tick 1 ebenfalls, verliert die
gemeinsame Reproduktion aber frueher. Der Befund der Deltaform haengt somit
nicht davon ab, dass beide Komponenten kombiniert werden.

## Topologische Grenze

Die verteilte Quelleninformation bildet noch keine reproduzierte lokale
Topologie. Fuer `D_t` entstehen im Entwicklungsbestand:

| Ticks | gegenseitige Kanten | gleiche Quelle | Labelnull-p |
| ---: | ---: | ---: | ---: |
| 1 | 56 | 8 | 0,000488 |
| 2 | 39 | 11 | 0,000244 |
| 4 | 31 | 4 | 0,00439 |

Im Holdout entstehen fuer dieselben Praefixe 3 von 46, 1 von 34 und 1 von 19
gleichquellige Kanten. Keine dieser drei Kantenlesungen liegt ueber ihrer
Labelnull (`p = 0,0959`, `0,5355`, `0,3612`).

Damit ist die Ereignisform ueber viele Quellen verteilt wiedererkennbar, aber
noch nicht lokal scharf genug fuer einen anonym gewachsenen
Nachbarschaftsgraphen.

## Befund

Getragen sind:

- eine feldlokale Relationsereigniszeit aus aufeinanderfolgenden Zustaenden,
- vollstaendige Invarianz gegen Neuronen-Umbenennung,
- ein schwellenfreier und mittelwertfreier Ereignisraum,
- reproduzierte Vorwelterfahrung in `D_t` bis Tick 4,
- natuerlicher Zerfall unter weiterer Zielerfahrung.

Nicht getragen sind:

- bereits erfolgter Informationsaustausch zwischen Mikrofeldern,
- ein reproduzierter anonymer Holdout-Graph,
- organisch gewachsene Feldmitglieder oder Kopplungen,
- Semantik, Memory, Feldrueckwirkung, Handlung oder Viranz.

2128 lokalisiert damit erstmals einen feldlokalen und indexfreien
Informationskandidaten. Er schliesst die Bruecke aus 2126 noch nicht: Die
bewegliche erfahrungsgebildete Relevanz zwischen mehreren Feldern fehlt
weiterhin.

## Architekturentscheidung

- keine Aenderung an `MiniMCMField` oder `MiniMCMNeuron`,
- kein neuer Runtime-Beobachter,
- kein Ereignis-Memory,
- keine Triadenkopplung,
- kein Handlungsdurchgriff und kein Viranzparameter.

## Reproduzierbarkeit

Ausgaben:

- `2128_MCM_LABELINVARIANTER_RELATIONSEREIGNISTRAEGER.paths.csv`
- `2128_MCM_LABELINVARIANTER_RELATIONSEREIGNISTRAEGER.edges.csv`
- `2128_MCM_LABELINVARIANTER_RELATIONSEREIGNISTRAEGER.summary.csv`

SHA-256:

- `paths`: `8023AF6714B946CE0E5FE01B1DE04FFC7EB74FC7D4789FAFCD7F58A0F586CDCC`
- `edges`: `77ACC6AB26CC2F594FAFBF0F10F620490FC3AD92D3C1B8CFBB1E9DBE0D23F34E`
- `summary`: `58140A9E0D18B377A6CD79632569AFC3B073EE26AE8B562D29333856AC439987`

Runner: `tools/run_mcm_label_invariant_relational_event_carrier.py`

Test: `tests/test_mcm_label_invariant_relational_event_carrier.py`
