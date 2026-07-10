# 2075 - Passive wachsende MCM-Feldtopologie

## Zweck

Nach der Rückkehr zum gültigen Forschungsstand 2074 wird erstmals kein neuer äußerer Chartaspekt geprüft. Stattdessen werden vorhandene innere MCM-Episoden während des normalen Laufs zu einem gerichteten Netz verbunden.

Die Außenwelt bleibt vollständiger Weltkontakt. Knoten und Kanten entstehen ausschließlich aus der inneren Feldfolge.

## Umsetzung

- Knoten: bestehende `dio_mcm_episode_*`-Identitäten.
- Kanten: beobachtete Reihenfolge abgeschlossener innerer Episoden.
- Wiederkehr: ergänzt Beobachtungszahl und gleitende Feldwerte.
- Weltkontext: wird nur als Herkunft gezählt und verändert die Identität nicht.
- Rückwirkung: keine.

## Kontrolllauf

Geprüft wurde dieselbe vollständige 1000-Zeilen-Welt zweimal nacheinander mit derselben frischen Memory:

```text
data/kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv
sense_mode: world_relative
world_label: TOPOLOGY_SMOKE
```

| Stand | Knotenbeobachtungen | Knoten | Wiederanschlüsse | Kantenbeobachtungen | Kanten | Wiederanschlüsse |
|---|---:|---:|---:|---:|---:|---:|
| nach Lauf 1 | 29 | 23 | 6 | 28 | 27 | 1 |
| nach Lauf 2 | 58 | 24 | 34 | 56 | 28 | 28 |

Im zweiten Lauf fanden damit 28 von 29 Knotenbeobachtungen und 27 von 28 Kantenbeobachtungen Anschluss an bereits vorhandene Topologie. Je eine neue Knoten- und Kantenvariante erweiterte das Netz.

## Grenzprüfungen

Automatische Tests bestätigen:

- dieselbe innere Episode behält in unterschiedlichen Weltkontexten dieselbe Knotenidentität,
- `A -> B` und `B -> A` bleiben getrennte Kanten,
- wiederkehrende Folgen verdichten bestehende Kanten,
- die passive Grenze bleibt nach Speichern und Laden erhalten.

## Befund

Die vorhandene innere Episodenfolge kann ohne vorgegebene Semantik als wachsendes gerichtetes Netz gespeichert werden. Der Wiederholungslauf erzeugt keine bloße Kopie: Der größte Teil schließt an vorhandene Struktur an, während einzelne neue Varianten entstehen können.

Das ist noch kein selbstregulierendes semantisches Netzwerk. Es ist der erste technische Träger, auf dem spätere Resonanz, Drift, Konsolidierung und schließlich vorsichtige Feldrückwirkung erforscht werden können.

## Grenze

Die aktuelle Topologie wird weder vom Feld noch von Handlungscode gelesen. Aus Wiederkehr entsteht keine Bedeutungsklasse, kein Gate, keine Richtung und keine Strategie.
