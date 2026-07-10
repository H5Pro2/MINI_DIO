# 2105 - Kontinuierliche MCM-Feldinstanz ueber Kontaktgrenzen

## Zweck

Befund 2104 zeigte, dass normale Weltlaeufe, Sleep-Milieu und Folgewelt
jeweils neue MCM-Felder erzeugen. 2105 prueft isoliert, welche Information
durch diesen Reset verloren geht.

Verglichen werden zwei Felder mit identischer Folgewelt:

```text
Resetpfad:
neues Feld -> Folgewelt

Kontinuitaetspfad:
Kontaktwelt -> reizfreie Luecke -> dieselbe Feldinstanz -> Folgewelt
```

Nur die Feldinstanz unterscheidet beide Pfade. Es gibt keine Aktion, kein
Lernen, keine Memory-Ruecklesung, keine Sleep-Klasse und kein zusaetzliches
Signal.

## Reale Kontaktpaare

Die Pruefung verwendet alle natuerlich benachbarten 1.000-Zeilen-Fenster aus
den beiden unabhaengigen Bestaenden:

- 60 Nachbarpaare aus BTC und SOL 2024/2025 auf `30m`,
- 54 Nachbarpaare aus DOGE, PAXG und XRP 2024/2025 auf `5m`.

Jedes Paar wird vorwaerts und rueckwaerts geprueft. Daraus entstehen 120
gerichtete Vergleiche im 2091-Bestand und 108 im 2092-Holdout.

Die realen Fenster liefern in Reset- und Kontinuitaetspfad exakt dieselbe
Sinnesfolge. Asset, Preis, Richtung und Volumen werden nicht als
Feldbedeutungen oder Vergleichsziele ausgewertet.

## Reizfreie Lueckenskala

Statt eine einzelne Pausenlaenge als Organismusregel festzulegen, wird die
Skalenreihe

```text
0, 1, 2, 4, 8, 16, 32, 64 Leerticks
```

geprueft. Ein frisches Feld bleibt unter allen Leerticks exakt im
Nullzustand. Die Leerticks erzeugen damit keinen kuenstlichen Feldinhalt; sie
lassen nur vorhandene Aktivierung und neuronalen Nachhall weiterlaufen.

## Schwellenfreie Konvergenz

Eine Kontinuitaetswirkung gilt erst als beendet, wenn beide Felder in

- Feldsignatur,
- allen Neuronenaktivierungen und
- allen neuronalen Nachhallwerten

bitgenau identisch sind. Es gibt keine Epsilon- oder Reifeschwelle. Sobald die
Zustaende bei gleicher Folgereizfolge identisch sind, bleiben alle spaeteren
Zustaende ebenfalls identisch.

Zusaetzlich werden die kontinuierlichen Differenzbetraege bewahrt. Dadurch
wird eine lange sehr kleine Spur nicht mit einer starken Feldwirkung
verwechselt.

## Gesamtbefund Der Kontinuitaetsdauer

| Leerticks | Median betroffene Folgeticks 2091 | Median betroffene Folgeticks 2092 | mittlerer Anteil der Folgewelt 2091 | mittlerer Anteil der Folgewelt 2092 |
|---:|---:|---:|---:|---:|
| 0 | 297,0 | 297,0 | 29,87 % | 30,07 % |
| 1 | 294,5 | 296,5 | 29,79 % | 30,01 % |
| 2 | 293,0 | 295,5 | 29,65 % | 29,94 % |
| 4 | 292,0 | 292,5 | 29,53 % | 29,72 % |
| 8 | 287,0 | 288,0 | 29,04 % | 29,27 % |
| 16 | 280,0 | 280,0 | 28,25 % | 28,60 % |
| 32 | 265,0 | 266,0 | 26,72 % | 26,90 % |
| 64 | 235,0 | 232,5 | 23,73 % | 23,44 % |

Ohne Leerluecke reicht die bitgenaue Vorzustandsspur je nach Paar 282 bis 332
Ticks in die Folgewelt. Nach 64 Leerticks liegt die Spanne noch bei 218 bis
284 Ticks.

Alle 1.824 Einzelvergleiche konvergieren innerhalb der jeweiligen Folgewelt
exakt zum Resetpfad. Es bleibt kein alternativer Endzustand bestehen.

## Staerke Der Kontinuitaetswirkung

| Leerticks | erste Signaturdifferenz 2091 | erste Signaturdifferenz 2092 | mittlere Signaturdifferenz 2091 | mittlere Signaturdifferenz 2092 |
|---:|---:|---:|---:|---:|
| 0 | 0,0032463 | 0,0032431 | 0,000027392 | 0,000027445 |
| 8 | 0,0011372 | 0,0011369 | 0,000009649 | 0,000009671 |
| 16 | 0,0004033 | 0,0004034 | 0,000003433 | 0,000003442 |
| 32 | 0,0000518 | 0,0000519 | 0,000000443 | 0,000000444 |
| 64 | 0,00000091 | 0,00000091 | 0,0000000078 | 0,0000000079 |

Zwischen null und 64 Leerticks sinkt die mittlere Signaturwirkung um rund
Faktor 3.500. Die bitgenaue Kontinuitaetsdauer sinkt im selben Vergleich nur
um rund ein Fuenftel. Dauer allein waere deshalb eine irrefuehrende
Staerkelesung: Ein langer Rest kann numerisch vorhanden, aber praktisch sehr
klein sein.

## Afterimage Als Traeger

Ohne Leerluecke korreliert der mittlere neuronale Nachhall der Kontaktwelt mit
der ersten Signaturdifferenz der Folgewelt:

| Bestand | Pearson-`r` |
|---|---:|
| 2091-Bestand | 0,9730 |
| 2092-Holdout | 0,9628 |

Die Beziehung bleibt ueber die gesamte Lueckenskala hoch. Bei 64 Leerticks
liegt sie noch bei 0,9488 und 0,9559. Die Kontinuitaetswirkung wird damit
direkt von der bestehenden neuronalen Nachhallmechanik getragen; sie ist kein
Artefakt eines leeren Kontrollfeldes.

## Reihenfolgekontrolle

Vorwaerts- und Rueckwaertskontakt liefern nahezu dieselbe qualitative Form.
Ohne Leerluecke liegen die mittleren betroffenen Ticks im 2091-Bestand bei
296,48 und 297,28, im Holdout bei 299,09 und 298,70. Auch Effektstaerke und
exakte Konvergenz sind richtungsgleich.

Damit traegt Feldkontinuitaet einen allgemeinen, quellenabhaengig verschieden
starken Nachhall. Sie traegt in dieser Pruefung keine besondere Bedeutung der
natuerlichen Kontaktrichtung.

## Befund

Getragen sind:

- ein realer deterministischer Vorzustandseinfluss derselben Feldinstanz,
- Nachhallwirkung in allen 228 gerichteten realen Kontaktpaaren,
- dieselbe qualitative Form in Entwicklungsbestand und unabhaengigem Holdout,
- kontinuierliche Abschwaechung ueber die reizfreie Lueckenskala,
- starke Bindung der ersten Folgewirkung an den neuronalen Afterimage-Zustand,
- bitgenaue Konvergenz aller Kontinuitaetspfade zum Resetfeld,
- exakte Neutralitaet eines frischen Feldes unter Leerticks.

Nicht getragen sind:

- ein dauerhaft anderer Feldzustand durch Kontinuitaet,
- eine starke Restwirkung nach laengerer reizfreier Luecke,
- besondere Semantik der natuerlichen Kontaktrichtung,
- Memory-Bildung oder Lernen aus der Kontinuitaet,
- ein eigener Takt, Ausloeser oder autonomer Offlineprozess,
- Feldintelligenz, Selbstregulation oder Handlung.

2105 zeigt, dass der bisherige Feldreset eine echte Innenzustandsspur entfernt.
Diese Spur ist breit reproduzierbar und mechanisch sauber durch Nachhall
getragen. Sie ist zugleich selbstbegrenzend: Unter weiterem Kontakt wird sie
in jedem Paar vollstaendig vom neuen Feldverlauf aufgenommen.

Der Befund rechtfertigt noch keine Aenderung der normalen Runtime. Er zeigt
zunaechst nur, dass Feldkontinuitaet eine reale organische Grundbedingung und
nicht bloss eine theoretische Annahme ist.

## Reproduzierbare Ausgaben

- `2105_MCM_KONTINUIERLICHE_FELDINSTANZ.pairs.csv`
- `2105_MCM_KONTINUIERLICHE_FELDINSTANZ.summary.csv`

Der Runner ist `tools/run_mcm_continuous_field_instance.py`. Er erzeugt keine
Welt-, Runtime-, Memory- oder Debugdateien.
