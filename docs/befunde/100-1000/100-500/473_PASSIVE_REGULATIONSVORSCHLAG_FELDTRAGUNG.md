# 473 - Passive Regulationsvorschlag Feldtragung

Stand: 2026-06-21

## Fragestellung

Welche passive Vorschlagsrichtung wird vom MCM-Feld eher getragen, und welche liegt naeher an Druck oder kurzfristiger Entlastung?

Wichtig: Diese Diagnose erzeugt keine aktive Regulation. Sie liest nur vorhandene Vorschlags-Spuren gegen Rekopplung, Carry, Strain und Feldinput.

## Methode

Gelesen wurden die Vorschlagsdateien 459 bis 467 und 471.

- Quellen: 9
- Vorschlags-Spuren: 1749

Pro Vorschlagsrichtung werden die vorhandenen Felddaten ereignisgewichtet verdichtet:

```text
Feldtragung = Rekopplung + Carry + wenig Strain + wenig Feldinput
Felddruck   = Strain + Feldinput + schwächere Rekopplung
```

Das ist eine Lesart, keine Schwelle und keine Anweisung.

## Gesamtbild nach Vorschlagsrichtung

| Vorschlag | Lesart | Quellen | Spuren | Ereignisse | Support | Druck | Netto | Rekopplung | Strain | Feldinput |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhig hinhoeren | eher_getragen | 9 | 322 | 16237 | 0.6310 | 0.1502 | 0.4808 | 0.5708 | 0.1343 | 0.0635 |
| Sehen schaerfen | eher_getragen | 9 | 269 | 14666 | 0.6106 | 0.1724 | 0.4381 | 0.5480 | 0.1401 | 0.1039 |
| Fokus halten / vertiefen | eher_getragen | 9 | 81 | 14796 | 0.5819 | 0.1967 | 0.3852 | 0.5016 | 0.1649 | 0.1193 |
| leiser / weicher aufnehmen | eher_getragen | 9 | 200 | 5934 | 0.5448 | 0.2390 | 0.3058 | 0.4577 | 0.1787 | 0.1930 |
| Abstand bilden | eher_getragen | 9 | 654 | 3837 | 0.5021 | 0.2605 | 0.2415 | 0.3996 | 0.2066 | 0.1938 |
| Druck / Feldkontakt entlasten | eher_getragen | 9 | 223 | 6440 | 0.5039 | 0.2772 | 0.2267 | 0.4058 | 0.1993 | 0.2459 |

## Lesart

Die Vorschlaege trennen sich nicht in einfache Ja/Nein-Gruppen. Sie liegen auf einem Spannungsfeld:

- `ruhig hinhoeren`, `Sehen schaerfen` und `Fokus halten / vertiefen` liegen eher auf der getragenen Seite.
- `Abstand bilden`, `leiser / weicher aufnehmen` und `Druck / Feldkontakt entlasten` liegen naeher an Entlastung und Druckbearbeitung.
- Das ist fachlich passend: Entlastungsvorschlaege entstehen dort, wo das Feld mehr Abstand, weichere Aufnahme oder Kontaktentlastung braucht.

Damit wird die naechste Trennung sichtbar:

```text
getragenes Wahrnehmen
vs.
entlastendes Wahrnehmen
```

Beides kann wertvoll sein. Getragen heisst nicht automatisch besser. Entlastend kann eine notwendige Organismusfaehigkeit sein, wenn Weltkontakt Druck erzeugt.

## Mechanische Grenze

- keine Handlung
- kein Gate
- keine Strategie
- keine direkte MCM-Feldsteuerung
- keine harte Entscheidung aus diesen Werten

Die Diagnose zeigt nur, welche Wahrnehmungsfaehigkeit in welchen Feldlagen eher getragen oder eher drucknah gelesen wird.

## Wie es weitergeht

Als naechstes sollte diese Feldtragung pro Asset getrennt gelesen werden: BTC, SOL und KAS koennen dieselbe Vorschlagssprache nutzen, aber unterschiedliche Entlastungs- und Tragprofile besitzen.
