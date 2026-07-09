# 1816 - Kernfamilien Tickfenster-Rollenprüfung

## Grundfrage

Diese Prüfung kontrolliert, ob die Rollentaxonomie aus 1807 in konkreten Tickfenstern sichtbar bleibt.

Die Diagnose bleibt passiv: keine Handlung, kein Gate, keine Richtung.

## Übersicht

| Familie | Muster | Ereignisfelder | Nachlauffelder | Ton | Tick-Lesung |
|---|---|---|---|---|---|
| `dio_14wj` | `tragende_verarbeitung` | `tragende_verarbeitung:rekoppelt` | `tragende_verarbeitung:offen` | `geordnetes_hinhoeren;geordnetes_hinhoeren_mit_wechsel` | `tragend_mit_offener_nachprüfung` |
| `dio_1fll` | `tragende_verarbeitung` | `tragende_verarbeitung:rekoppelt` | `tragende_verarbeitung:rekoppelt` | `geordnetes_hinhoeren` | `tragend_mit_gehaltener_rekopplung` |
| `dio_0m9z` | `kippnaehe` | `kippnaehe:belastet_kippnah` | `kippnaehe:offen` | `geordnetes_hinhoeren_mit_wechsel` | `kippnaher_randkontakt` |
| `dio_155c` | `kippnaehe;tragende_verarbeitung` | `kippnaehe:offen;tragende_verarbeitung:rekoppelt` | `kippnaehe:offen;tragende_verarbeitung:rekoppelt` | `geordnetes_hinhoeren_mit_wechsel` | `duale_feldrolle` |

## Befund

Die konkrete Tickfensterprüfung bestätigt die Rollenkarte differenziert und macht die Unterschiede schärfer:

- `dio_14wj` trägt Rekopplung punktuell sehr sauber, fällt danach aber wieder in offenere Nachprüfung. Das passt zu einem breiten Übergangsknoten.
- `dio_1fll` bleibt über Vorlauf, Ereignis und Nachlauf rekoppelter. Das passt zu einer Sammelrolle mit stärker gehaltener Feldbindung als die reine Randnähe vermuten ließ.
- `dio_0m9z` erscheint in den geprüften Fenstern fast rein kippnah und belastet. Das stützt die Lesung als Hör-/Nachhallknoten mit Randkontakt.
- `dio_155c` trägt beide Seiten: Kippnähe und tragende Verarbeitung. Das wirkt wie eine duale Feldrolle zwischen Lastaufnahme und Rekopplung.

Damit wird die frühere Taxonomie präziser: Rollen sind nicht nur Kategorien, sondern Feldfolgen. Eine Familie kann Anschluss, Rand, Nachhall oder Brücke je nach Weltfenster verschieden ausprägen.
