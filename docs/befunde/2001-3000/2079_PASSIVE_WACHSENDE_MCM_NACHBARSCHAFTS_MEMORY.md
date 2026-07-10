# 2079 - Passive wachsende MCM-Nachbarschafts-Memory

## Zweck

Befund 2078 fand eine reproduzierbare mittlere Auflösung zwischen grobem Episodenzustand und exakter Episodengleichheit. Diese Prüfung integriert erstmals nur die dafür notwendige Wachstumsbedingung in MINI_DIO.

Keine der 26 zuvor gefundenen Kernrelationen wird übernommen. MINI_DIO erhält ausschließlich die Möglichkeit, aus seinen eigenen abgeschlossenen Episodenprofilen gegenseitige nächste Nachbarschaften zu bilden und deren Wiederkehr zu akkumulieren.

## Integration

Die neue `passive_mcm_neighborhood_memory` besitzt zwei Ebenen:

- **Weltprofile:** kompakte Profile der in einem vollständigen Lauf entstandenen exakten MCM-Episodenidentitäten,
- **Nachbarschaftsevidenz:** Beziehungen zwischen zwei verschiedenen Identitäten, die in mindestens einem Weltpaar gegenseitig nächste Profile waren.

Nach jedem Weltabschluss wird das neue Weltprofil genau einmal mit allen früheren Weltprofilen verglichen. Für jede entstandene Relation werden ausschließlich numerische Erfahrungsspuren ergänzt:

- Tragung in den drei inneren Profilräumen,
- Zahl tragender Weltpaare,
- Kontextbreite über verschiedene Weltläufe,
- mittlerer Profilabstand,
- erstes und letztes Auftreten.

Es gibt keine Distanzschwelle, keine feste Nachbarzahl und keine vorgegebene Beziehungsliste. Die standardisierte Profilsicht wird innerhalb jedes Weltpaares normiert, damit spätere Welten frühere Nähebelege nicht rückwirkend umskalieren.

## Passive Grenze

Die Memory ist Bestandteil des Runtime-Dokuments, aber kein wirksamer Teil der Runtime-Regulation:

```text
read_by_mini_dio = 0
influences_field = 0
influences_action = 0
is_gate = 0
is_motoric = 0
is_entry_signal = 0
is_direction_signal = 0
```

Weder Feldwirkung noch Handlung lesen Nachbarschaft, Tragung oder Profilabstand zurück. Weltbezeichnungen bleiben Herkunft und werden nicht Teil der Episoden- oder Nachbarschaftsidentität.

## Mechanische Prüfungen

Acht Unit-Tests sichern die bisherige Topologie und die neue Ebene gemeinsam ab. Für die Nachbarschafts-Memory wird geprüft:

- Beziehungen entstehen ohne vordefinierte Paare,
- selbst große Abstände werden nicht durch eine versteckte Schwelle ausgeschlossen,
- derselbe Erfahrungssatz erzeugt bei umgekehrter Ankunftsfolge denselben Endgraphen,
- die passive Grenze bleibt nach Speichern und Laden erhalten.

## Online-Mehrweltprüfung

Die 81 Welten aus Befund 2078 werden in zwei getrennten fortlaufenden Memories erlebt:

```text
forward: W001 -> W002 -> ... -> W081
reverse: W081 -> W080 -> ... -> W001
```

Anders als in Befund 2078 startet nicht jede Welt mit leerer Gesamtmemory. Frühere MINI_DIO-Erfahrung darf die später entstehenden inneren Episodenprofile mitprägen. Nur die neue Nachbarschafts-Memory bleibt ohne Rückwirkung.

## Wachstum

| Position | aktive Links vorwärts/rückwärts | Dreiprofil-Links vorwärts/rückwärts | Weltpaarbeobachtungen vorwärts/rückwärts |
|---:|---:|---:|---:|
| 2 | 10 / 9 | 4 / 2 | 10 / 9 |
| 10 | 240 / 190 | 54 / 50 | 754 / 617 |
| 20 | 482 / 421 | 120 / 122 | 2.849 / 2.455 |
| 40 | 952 / 928 | 247 / 269 | 11.310 / 10.327 |
| 60 | 1.591 / 1.541 | 399 / 404 | 25.242 / 24.126 |
| 81 | 2.046 / 2.085 | 541 / 542 | 45.029 / 45.092 |

Das Netz wächst nicht durch eingefügte Links, sondern ausschließlich durch neu beobachtete gegenseitige Nähe. Beide Erfahrungswege enden trotz unterschiedlicher Zwischenentwicklung nahezu gleich groß.

## Reihenfolgenstabilität

| Ebene | vorwärts | rückwärts | gemeinsam | Jaccard |
|---|---:|---:|---:|---:|
| alle aktiven Nachbarschaften | 2.046 | 2.085 | 1.935 | 0,881 |
| in allen drei Profilräumen getragen | 541 | 542 | 503 | 0,867 |

Die fortlaufende übrige MINI_DIO-Memory macht die Endgraphen nicht identisch. Dennoch bleibt der größte Teil der Beziehungen trotz vollständig umgekehrtem Erfahrungsweg erhalten.

## Wiederkehr des 2078-Kerns

Der Abgleich mit der frischen Offline-Prüfung aus Befund 2078 ergibt:

- 1.705 beziehungsweise 1.716 aktive Online-Links sind auch im damaligen Gesamtgraphen vorhanden,
- 436 beziehungsweise 431 Dreiprofil-Links kehren in derselben Auflösung wieder,
- **alle 26 strengen profil- und jahresübergreifenden Kernrelationen entstehen in beiden Online-Memories erneut**,
- der Kernabgleich zwischen vorwärts und rückwärts beträgt damit 26 von 26 und Jaccard 1,000.

Das ist der zentrale Befund: Die 26 Relationen wurden nicht programmiert, erscheinen aber unter zwei gegensätzlichen fortlaufenden Erfahrungswegen vollständig erneut.

## Technische Korrektur

Ein vollständiger Neuaufbau aller bisherigen Weltpaare nach jedem Weltabschluss erwies sich als nicht skalierbar und wurde nicht beibehalten. Die integrierte Form verarbeitet jedes neue Weltpaar genau einmal und akkumuliert seine Evidenz. Dadurch sinkt der Vergleichsaufwand von kumulativ kubischem auf quadratisches Wachstum über die Zahl der Welten.

Nach 81 Welten besitzen die vollständigen lokalen Runtime-Memories ungefähr 12,6 MB. Diese Dateien bleiben lokal und werden nicht veröffentlicht. Eine organische Verdichtung, Alterung oder Vergessensdynamik ist in dieser Ebene noch nicht umgesetzt; deshalb ist die aktuelle Memory ein Forschungsstand und keine unbegrenzt skalierende Endform.

## Befund

Die passive Nachbarschafts-Memory erfüllt erstmals drei Bedingungen gemeinsam:

- konkrete Beziehungen entstehen aus Erfahrung statt aus einer festen Liste,
- ein kleiner zuvor gefundener Kern wächst unter gegensätzlicher Erfahrung vollständig erneut,
- die Beziehungsebene bleibt vollständig von Feld und Handlung getrennt.

Damit ist eine organisch wachsende mittlere Topologie technisch und empirisch getragen. Noch nicht getragen sind semantische Bedeutung, Rückwirkung, aktive Auswahl sowie eigenständige Verdichtung oder Vergessen.

Reproduzierbare Ausgaben:

- `2079_PASSIVE_WACHSENDE_MCM_NACHBARSCHAFTS_MEMORY.growth.csv`
- `2079_PASSIVE_WACHSENDE_MCM_NACHBARSCHAFTS_MEMORY.summary.csv`
- `2079_PASSIVE_WACHSENDE_MCM_NACHBARSCHAFTS_MEMORY.comparison.csv`
- `2079_PASSIVE_WACHSENDE_MCM_NACHBARSCHAFTS_MEMORY.top.csv`
