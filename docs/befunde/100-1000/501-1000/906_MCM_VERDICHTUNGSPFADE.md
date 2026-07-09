# MCM-Verdichtungspfade

## Zweck

Diese Diagnose prueft, ob die Rollenwanderungen aus 904 als Reifepfade lesbar sind.
Es wird nicht behauptet, dass Mini-DIO eine feste Leiter benutzt. Geprueft wird nur, ob die beobachteten Rollenwechsel eine geordnete Verdichtungsrichtung tragen.

## Stufenprofil

| Stufe | Anzahl |
|---|---:|
| vorreifung_schwach_zu_lokal | 4 |
| kernverdichtung_stark_zu_kern | 2 |
| kernverdichtung_lokal_zu_kern | 2 |
| sprung_schwach_zu_stark | 2 |
| direktsprung_schwach_zu_kern | 1 |
| reifung_lokal_zu_stark | 1 |

## Uebergangsprofil

| Uebergang | Anzahl |
|---|---:|
| schwacher_anschluss_to_lokaler_anschlussanker | 4 |
| starker_anschlussanker_to_brueckenkern | 2 |
| lokaler_anschlussanker_to_brueckenkern | 2 |
| schwacher_anschluss_to_starker_anschlussanker | 2 |
| schwacher_anschluss_to_brueckenkern | 1 |
| lokaler_anschlussanker_to_starker_anschlussanker | 1 |

## Tokens

| Token | Stufe | Uebergang | Gewicht Delta | Dauer Delta |
|---|---|---|---:|---:|
| `0ykar6i` | direktsprung_schwach_zu_kern | schwacher_anschluss -> brueckenkern | 212 | -628.65 |
| `0b7nep9` | kernverdichtung_stark_zu_kern | starker_anschlussanker -> brueckenkern | 193 | -385.79 |
| `1jx2k4i` | kernverdichtung_stark_zu_kern | starker_anschlussanker -> brueckenkern | 82 | -66.83 |
| `1xx3u1e` | kernverdichtung_lokal_zu_kern | lokaler_anschlussanker -> brueckenkern | 37 | 110.08 |
| `0z748ck` | kernverdichtung_lokal_zu_kern | lokaler_anschlussanker -> brueckenkern | 4 | -50.30 |
| `1jwnjz4` | sprung_schwach_zu_stark | schwacher_anschluss -> starker_anschlussanker | 46 | 74.53 |
| `1ahj81f` | sprung_schwach_zu_stark | schwacher_anschluss -> starker_anschlussanker | 29 | -16.93 |
| `1q3us3f` | reifung_lokal_zu_stark | lokaler_anschlussanker -> starker_anschlussanker | 13 | 2.32 |
| `077r0df` | vorreifung_schwach_zu_lokal | schwacher_anschluss -> lokaler_anschlussanker | 15 | 7.00 |
| `0geqqo3` | vorreifung_schwach_zu_lokal | schwacher_anschluss -> lokaler_anschlussanker | 11 | 29.14 |
| `0w4x7xs` | vorreifung_schwach_zu_lokal | schwacher_anschluss -> lokaler_anschlussanker | 9 | -72.83 |
| `1al8fjz` | vorreifung_schwach_zu_lokal | schwacher_anschluss -> lokaler_anschlussanker | 8 | -0.10 |

## Befund

Die Verdichtungen verteilen sich auf mehrere Stufen. Besonders relevant sind direkte Kernverdichtungen und Vorreifungen:

- `schwach -> lokal`: erste lokale Stabilisierung.
- `schwach -> stark`: sprunghafte Anschlussverstaerkung.
- `lokal -> stark`: gereiftere Anschlussqualitaet.
- `lokal/stark -> Kern`: Einbindung in tragende Brueckenstruktur.

Damit ist die Rollenwanderung nicht nur chaotischer Wechsel. Sie zeigt eine Richtung: Feldspuren koennen aus schwacher Naehe zu lokaler, starker oder kernbildender Funktion verdichten.

## Grenze

Das ist noch kein Beweis einer vollstaendigen Entwicklungsleiter. Dafuer braucht es weitere Weltgruppen und eine zeitliche Folgepruefung. Aktuell ist es ein starker Hinweis auf geordnete Verdichtungsdynamik.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob diese Stufen in einer zeitlichen Reihenfolge auftreten oder ob sie nur zwischen zwei Landschaften sichtbar werden.