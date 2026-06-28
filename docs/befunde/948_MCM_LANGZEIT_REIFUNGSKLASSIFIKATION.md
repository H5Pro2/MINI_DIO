# MCM-Langzeit-Reifungsklassifikation

## Zweck

Diese Auswertung verdichtet die passive `dio_mature_*`-Lesung aus 946 zu einer Langzeitklasse.
Sie bleibt diagnostisch: keine Handlung, kein Gate, keine Richtungsvorgabe.

## Klassen

- `abgeschwaecht_oder_verloren`: 1
- `kurzfristige_oberflaeche`: 2
- `langfristig_belastet_getragen`: 1
- `langfristig_getragen`: 1
- `verschwunden_bestaetigt`: 2
- `weltabhaengig_getragen`: 1

## Token-Lesung

| Token | Symbol | Langzeitklasse | Lesung | aktuelle Rolle | Note |
|---|---|---|---|---|---|
| `0z748ck` | `dio_mature_0yx0oq2` | `langfristig_getragen` | `bruecke_gehalten` | `lokaler_anschlussanker` | Reorganisationsbruecke bleibt auch in weiterer Welt sichtbar. |
| `00dz86x` | `dio_mature_0eigbm8` | `kurzfristige_oberflaeche` | `nicht_wiedergefunden` | `-` | Junge oder offene Spur bleibt nicht sichtbar. |
| `00nzcuc` | `dio_mature_0bf3x2q` | `kurzfristige_oberflaeche` | `nicht_wiedergefunden` | `-` | Junge oder offene Spur bleibt nicht sichtbar. |
| `00yl137` | `dio_mature_109zkut` | `abgeschwaecht_oder_verloren` | `nicht_wiedergefunden` | `-` | Vorherige junge Reifung wird in Folgewelt nicht getragen. |
| `0om13wf` | `dio_mature_1619pcd` | `weltabhaengig_getragen` | `reifung_abgeschwaecht` | `schwacher_anschluss` | Reifung bleibt sichtbar, verliert aber Zentralitaet. |
| `1hdpu9s` | `dio_mature_0w1iqyf` | `langfristig_belastet_getragen` | `rolle_gehalten_bestaetigt` | `schwacher_anschluss` | Rolle bleibt sichtbar, traegt aber belastete Kernnaehe. |
| `0db07p4` | `dio_mature_18eoltu` | `verschwunden_bestaetigt` | `verschwindung_bestaetigt` | `-` | Verschwinden wird erneut gelesen und ist selbst Information. |
| `1ahj81f` | `dio_mature_0nxg7f6` | `verschwunden_bestaetigt` | `verschwindung_bestaetigt` | `-` | Verschwinden wird erneut gelesen und ist selbst Information. |

## Interpretation

Die MCM-Reifung verhaelt sich nicht linear.
Ein Teil der Spuren bleibt ueber Folgewelten tragend, ein Teil wird weltabhaengig abgeschwaecht, und ein Teil verschwindet wieder.
Wichtig ist dabei: Auch Verschwinden ist kein Fehler, sondern Feldinformation.

Damit entsteht eine passive Reifungsordnung:

- stabile Reorganisationsbruecken
- belastet gehaltene Kernnaehe
- weltabhaengige Reifung
- bestaetigtes Verschwinden
- kurzfristige Oberflaeche

## Schlussfolgerung

`dio_mature_*` kann als passive Langzeit-Memory genutzt werden, um Reifung von Oberflaeche zu trennen.
Die Schicht beschreibt nicht, was MINI_DIO tun soll.
Sie beschreibt nur, welche inneren Feldrollen ueber mehrere Welten sichtbar bleiben.

## Wie es weitergeht

Als naechstes sollte diese Klassifikation gegen eine weitere Welt gelesen werden.
Entscheidend ist, ob `langfristig_getragen` stabil bleibt und ob `weltabhaengig_getragen` weiter driftet oder wieder rekoppelt.
