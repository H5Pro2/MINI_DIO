# MCM-Verdichtungspfade Zeitordnung

## Zweck

Diese Diagnose prueft, ob die Verdichtungsstufen aus 906 zeitlich als Folge sichtbar werden oder ob sie erst im Vergleich zweier Landschaften auftreten.

## Profil

- Verdichtende Tokens gesamt: `12`
- In beiden Landschaften vorhanden: `3`
- Erst in Vergleichslandschaft sichtbar: `3`
- In den Detaildaten nicht zeitlich pruefbar: `6`

## Tokens

| Token | Stufe | Basis Segmente | Vergleich Segmente | Basis Erste | Vergleich Erste | Vergleich Dominante Welt | Lesung |
|---|---|---:|---:|---:|---:|---|---|
| `0b7nep9` | kernverdichtung_stark_zu_kern | 18 | 70 | 2951 | 2063 | DOGE_2024_5M | Rollenumbau vorhandener Spur |
| `1al8fjz` | vorreifung_schwach_zu_lokal | 3 | 7 | 6 | 6 | BTC_2024_5M | Rollenumbau vorhandener Spur |
| `1xx3u1e` | kernverdichtung_lokal_zu_kern | 6 | 23 | 8821 | 4817 | PAXG_2025_5M | Rollenumbau vorhandener Spur |
| `0ykar6i` | direktsprung_schwach_zu_kern | 0 | 64 | 0 | 2063 | DOGE_2024_5M | neue Verdichtung in Folgelandschaft |
| `0z748ck` | kernverdichtung_lokal_zu_kern | 0 | 7 | 0 | 418 | DOGE_2024_5M | neue Verdichtung in Folgelandschaft |
| `1jx2k4i` | kernverdichtung_stark_zu_kern | 0 | 40 | 0 | 15 | KAS_2024_5M | neue Verdichtung in Folgelandschaft |
| `077r0df` | vorreifung_schwach_zu_lokal | 0 | 0 | 0 | 0 |  | nicht zeitlich pruefbar |
| `0geqqo3` | vorreifung_schwach_zu_lokal | 0 | 0 | 0 | 0 |  | nicht zeitlich pruefbar |
| `0w4x7xs` | vorreifung_schwach_zu_lokal | 0 | 0 | 0 | 0 |  | nicht zeitlich pruefbar |
| `1ahj81f` | sprung_schwach_zu_stark | 0 | 0 | 0 | 0 |  | nicht zeitlich pruefbar |
| `1jwnjz4` | sprung_schwach_zu_stark | 0 | 0 | 0 | 0 |  | nicht zeitlich pruefbar |
| `1q3us3f` | reifung_lokal_zu_stark | 0 | 0 | 0 | 0 |  | nicht zeitlich pruefbar |

## Befund

Die pruefbaren Detaildaten zeigen keine einfache interne Zeitreihe im Sinne einer festen Leiter innerhalb einer einzelnen Landschaft.
Stattdessen gibt es zwei pruefbare Muster:

1. vorhandene Spuren werden in der Vergleichslandschaft anders organisiert und rollenhaft verdichtet.
2. neue Spuren treten erst in der Vergleichslandschaft auf und erscheinen dort bereits als verdichtete Rolle.

Ein Teil der 906-Kandidaten ist in diesen Detaildaten nicht zeitlich pruefbar. Fuer diese Tokens bleibt die Rollenwanderung ein Landschaftsvergleich, keine Zeitfolgen-Aussage.

Damit ist die Verdichtung in den pruefbaren Faellen eher landschafts- und nachbarschaftsabhaengig als eine starre lineare Entwicklungsfolge.

## Konsequenz

Mini-DIO sollte Rollenreifung nicht als feste Leiter speichern.
Besser ist eine dynamische Reifelesung:

```text
Diese Spur war vorhanden.
Unter anderer Welt- und Nachbarschaftsspannung traegt sie eine andere Rolle.
Manche Spuren entstehen erst in neuer Weltspannung und sind dort direkt verdichtet.
```

## Wie es weitergeht

Als naechstes sollte eine echte Mehrlandschafts-Folge gebaut werden: nicht nur Basis vs. Vergleich, sondern drei oder mehr Landschaften in Reihenfolge, um Rollenreife und Rollendrift als Verlauf zu messen.