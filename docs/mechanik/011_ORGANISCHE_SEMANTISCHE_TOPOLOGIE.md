# 011 - Organische semantische Topologie

## Ziel

MINI_DIO soll aus der zeitlichen Folge seiner eigenen MCM-Feldwirkungen ein wachsendes inneres Netz bilden.

Programmiert wird nur die Möglichkeit, Beobachtungen zu verbinden. Die konkrete Zahl, Wiederkehr und Richtung der Knoten und Kanten entsteht aus dem Feldlauf.

## Untersuchungsrichtung

```text
vollständige Außenwelt
-> Aufnahme und Rezeptoren
-> MCM-Feldwirkung
-> abgeschlossene innere Episode
-> Knoten im topologischen Gedächtnis
-> gerichtete Kante zur vorherigen inneren Episode
```

Weltname und äußere Merkmale sind keine Knotenidentität. Der Weltname bleibt ausschließlich Herkunft einer Beobachtung.

## Knoten

Ein Knoten verwendet die bestehende `dio_mcm_episode_*`-Identität. Sie entsteht aus:

- innerem Episodenzustand,
- vorherigem und folgendem inneren Zustand,
- gerichteter innerer Übergangsfolge,
- Episodendauer,
- Carry, Strain und Rekopplung,
- sensorischer Kopplung und inneren Feldabständen.

Bei Wiederkehr wird kein neuer semantischer Name vergeben. Der vorhandene Knoten erhält zusätzliche numerische Erfahrung und Herkunft.

## Gerichtete Kanten

Eine Kante entsteht nur aus der tatsächlich beobachteten Reihenfolge abgeschlossener Episoden.

```text
A -> B ist nicht B -> A
```

Wiederholt sich dieselbe Folge, wächst ihre Beobachtungszahl. Eine bisher ungesehene Folge erweitert das Netz um eine neue Kante.

## Passive Grenze

Die erste Umsetzung ist vollständig passiv:

```text
read_by_mini_dio: 0
influences_field: 0
influences_action: 0
is_gate: 0
is_motoric: 0
is_entry_signal: 0
is_direction_signal: 0
```

Das Netz beschreibt Wachstum. Es entscheidet noch nicht, was das Feld wahrnimmt oder wie DIO handelt.

## Noch nicht umgesetzt

- weiche Resonanz zwischen ähnlichen, aber nicht identischen Knoten,
- organische Verschmelzung oder Teilung,
- Alterung und Vergessen,
- ressourcenbezogene Konkurrenz,
- Sleep-Konsolidierung,
- passive Rücklesung in eine spätere Feldregulation.

Diese Schritte dürfen erst folgen, wenn Mehrweltprüfungen zeigen, welche Knoten und Kanten tatsächlich wiederkehren, driften oder nur lauflokal entstehen.

## Mehrweltstand 2076

Die erste Vierweltprüfung mit umgekehrter Reihenfolgenkontrolle endet in beiden Läufen bei 33 Knoten und 65 Kanten. Alle 33 Knoten und 64 von 65 Kanten sind global identisch. Das Netz besitzt damit einen reihenfolgenstabilen Grundträger.

Diese Stabilität ist noch keine semantische Weltbindung. Der reale Anker teilt in der aktuellen Identität mehr Knoten mit seiner Shuffle-Nullwelt als mit dem direkt folgenden Realfenster. Deshalb bleiben Resonanzverschmelzung, Sleep-Konsolidierung und Feldrückwirkung gesperrt. Zuerst muss die innere zeitliche Struktur über längere Motive und kontinuierliche Profilnähe genauer gelesen werden.

## Auflösungsstand 2077

Die Prüfung der inneren zeitlichen Struktur zeigt eine Lücke zwischen zwei Ebenen. Die grobe Zustandsfolge besitzt in allen vier Welten nur zwei alternierende Motive und ist damit gesättigt. Die exakte Episodenidentität wird bei längeren Folgen dagegen so spezifisch, dass keine Viererfolge weltübergreifend wiederkehrt.

Kontinuierliche Feldprofile erhalten mehr Nähe, tragen aber ebenfalls noch keine Realfolgebindung. In drei getrennten Profilräumen liegt der reihenfolgensensitive Verlauf des Realankers näher an der Shuffle-Nullwelt als am direkt folgenden Realfenster. Die Topologie bleibt deshalb ein passiver innerer Träger. Verdichtung, Verschmelzung, Konsolidierung und Feldrückwirkung sind aus diesem Stand nicht begründet.

## Nachbarschaftsstand 2078

Die schwellenfreie Mehrweltprüfung liest verschiedene exakte Episodenidentitäten als provisorische Nachbarn, wenn ihre kontinuierlichen Profile in zwei frischen Weltläufen gegenseitig die nächsten sind. Von 2.116 beobachteten Relationen werden 594 in allen drei internen Profilräumen getragen. 26 Relationen bleiben zugleich innerhalb 2025, über die Jahresgrenze und innerhalb 2024 mit Dreiprofil-Unterstützung sichtbar.

Damit liegt erstmals eine mittlere Auflösung zwischen grobem Zustand und exakter Gleichheit vor. Sie ist organisch anschlussfähig, weil die konkreten Beziehungen aus wiederholter Nähe entstehen und nicht als Liste vorgegeben werden. Die Ebene ist dennoch keine fertige Semantik: Nach Normierung an der Topologiegröße besitzen Real-Real-Paare keine allgemein höhere Nachbarschaftsdichte als die Kontrollen. Alle Beziehungen bleiben passiv und ohne Feldrückwirkung.

## Integrationsstand 2079

Die mittlere Nachbarschaftsebene ist nun als passive Memory integriert. Abgeschlossene Weltläufe hinterlassen kompakte innere Episodenprofile. Jede neue Welt wird einmal mit allen früheren Welten verglichen; gegenseitige nächste Nachbarn sammeln Profilraum-, Weltpaar- und Kontextevidenz. Keine der in Befund 2078 beobachteten Beziehungen ist im Code vorgegeben.

Unter zwei vollständig gegensätzlichen 81-Welten-Reihenfolgen entstehen alle 26 strengen Kernrelationen erneut. Die Gesamtgraphen überlappen mit Jaccard 0,881, die in allen drei Profilräumen getragenen Links mit 0,867. Damit trägt die Wachstumsbedingung einen stabilen inneren Kern, aber noch keine Semantik oder Feldrückwirkung. Die fehlende Verdichtungs-, Alterungs- und Vergessensdynamik bleibt eine technische und organische Grenze.
