# MCM-Reorganisation und Reifung in der Folgewelt

## Zweck

Diese Synthese fasst 935 und 936 zusammen.
Geprueft wurde, ob die in 927 isolierte Reorganisationsgruppe in einer weiteren Folgewelt verschwindet, jung bleibt oder tragendere Anschlussrollen bildet.

## Befund

Die Reorganisationsgruppe zerfaellt in vier Lesarten:

| Lesart | Token | Befund |
|---|---|---|
| junge Spur gehalten | `00dz86x`, `00nzcuc` | bleibt schwacher Anschluss, noch keine Reife |
| junge Spur reift | `00yl137`, `0om13wf` | wird in der Folgewelt Brueckenkern |
| Rolle gehalten | `0z748ck`, `1hdpu9s` | bleibt sichtbar, aber mit unterschiedlicher Feldqualitaet |
| Spur verschwindet | `0db07p4`, `1ahj81f` | verliert sichtbare Anschlussrolle |

## Segmentlesung

`00yl137` ist eine kurze junge Keimspur.
Sie erscheint in 3 Welten, hat nur 4 Segmente und kurze Dauer.
Innen steigt Rekopplung, Strain und Lautheit fallen, beim Austritt steigt jedoch Unschaerfe.
Das spricht fuer eine junge Reifung mit noch instabilem Austritt.

`0om13wf` ist ebenfalls kurz, aber sauberer rekoppelnd.
Es erscheint in 3 Welten, hat 11 Segmente und zeigt innen steigende Rekopplung, fallenden Strain und fallende Unschaerfe.
Der Austritt bleibt ebenfalls rekoppelnd.
Das ist der klarste Fall einer jungen Spur, die in der Folgewelt tragender wird.

`0z748ck` bleibt als lokaler Anschlussanker erhalten.
Es liegt in 5 Welten, hat 39 Segmente und koppelt haeufig von `0qzjuvj` nach `0e7qvj1`.
Innen stabilisiert es sich leicht; beim Austritt steigt Spannung etwas.
Das wirkt wie eine gehaltene Reorganisationsbruecke, nicht wie neue Oberflaeche.

`1hdpu9s` ist keine junge Spur, sondern eine lange belastete Kontaktphase.
Es liegt in 5 Welten, hat 114 Segmente und koppelt stark an `0e7qvj1`.
Gleichzeitig steigen Strain, Lautheit, Unschaerfe und Spannung.
Das wirkt weniger wie ruhige Reifung, sondern wie eine belastete Langphase nahe am Kernraum.

## Interpretation

Nicht jede Reorganisation ist gleich.
Ein Teil verschwindet, ein Teil bleibt jung, ein Teil reift, und ein Teil bleibt als belastete Kontaktphase sichtbar.

Das ist fuer MINI_DIO wichtig:

- Reorganisation darf nicht als Fehler gelesen werden.
- Junge Spuren koennen spaeter tragend werden.
- Belastete Langphasen koennen zentral gekoppelt sein, ohne dadurch automatisch stabil oder gesund zu sein.
- Eine MCM-Memory sollte daher nicht nur Token speichern, sondern Reifungsweg, Segmentdauer, Eintritt/Austritt und Achsenqualitaet.

## Arbeitsstand

Der Befund stuetzt die These, dass MINI_DIO im MCM-Feld nicht nur Wiederkehr erkennt, sondern Reifungsbewegungen unterscheiden kann:

- Keimspur
- gehaltene junge Spur
- Reifung zum Brueckenkern
- gehaltene Reorganisationsbruecke
- belastete Kernnaehe
- Verschwindende Oberflaeche

## Wie es weitergeht

Als naechstes sollte daraus eine passive Reifungsqualitaet fuer `dio_role_*` abgeleitet werden.
Diese darf keine Handlung steuern, sondern soll nur speichern, ob eine Reorganisationsspur jung, gereift, gehalten, belastet oder verschwunden ist.
