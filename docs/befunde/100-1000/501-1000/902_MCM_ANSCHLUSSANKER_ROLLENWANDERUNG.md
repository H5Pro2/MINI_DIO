# MCM-Anschlussanker Landschaftsvergleich

## Zweck

Diese Diagnose vergleicht die moderne Anschlussanker-Landschaft aus 894 mit einer zweiten, nach gleicher Pipeline erzeugten Vergleichsgruppe aus 864/898/899/900/901.
Damit wird Rollenanalogie durch echte Netzwerk-Topologie ergaenzt.

## Gesamtvergleich

| Landschaft | Tokens | Klassenprofil | Starke Anschlussanker | Brueckenkerne | Lokale Anschlussanker |
|---|---:|---|---:|---:|---:|
| 894 | 65 | schwacher_anschluss:50; brueckenkern:8; lokaler_anschlussanker:5; starker_anschlussanker:2 | 2 | 8 | 5 |
| 901 | 95 | schwacher_anschluss:70; brueckenkern:15; lokaler_anschlussanker:6; starker_anschlussanker:4 | 4 | 15 | 6 |

- Token-Ueberlappung: `48`

## Staerkste Rollen In 894

| Token | Klasse | Gewicht | Welten | Dauer | Pfadklasse | Bewegung |
|---|---|---:|---:|---:|---|---|
| `0e7qvj1` | brueckenkern | 165 | 5 | 174.21 | brueckenpfad | stabil |
| `18l3thm` | brueckenkern | 110 | 5 | 77.90 | brueckenpfad | reifung_oder_verdichtung |
| `1joiyc3` | brueckenkern | 74 | 5 | 138.82 | brueckenpfad | stabil |
| `0db07p4` | brueckenkern | 47 | 5 | 56.43 | brueckenpfad | reifung_oder_verdichtung |
| `0mji3u6` | brueckenkern | 43 | 5 | 180.37 | brueckenpfad | reifung_oder_verdichtung |
| `0b7nep9` | starker_anschlussanker | 35 | 2 | 470.94 | brueckenpfad | stabil |
| `1jx2k4i` | starker_anschlussanker | 33 | 5 | 133.18 | stabile_insel | stabil |

## Staerkste Rollen In 901

| Token | Klasse | Gewicht | Welten | Dauer | Pfadklasse | Bewegung |
|---|---|---:|---:|---:|---|---|
| `0e7qvj1` | brueckenkern | 276 | 6 | 123.33 | brueckenpfad | stabil |
| `0b7nep9` | brueckenkern | 228 | 4 | 85.15 | brueckenpfad | stabil |
| `0ykar6i` | brueckenkern | 215 | 4 | 71.02 | brueckenpfad | stabil |
| `18l3thm` | brueckenkern | 171 | 6 | 55.43 | brueckenpfad | reifung_oder_verdichtung |
| `1jx2k4i` | brueckenkern | 115 | 6 | 66.35 | brueckenpfad | reifung_oder_verdichtung |
| `1joiyc3` | brueckenkern | 101 | 6 | 146.90 | brueckenpfad | stabil |
| `0mji3u6` | brueckenkern | 97 | 6 | 94.06 | brueckenpfad | reifung_oder_verdichtung |
| `14coypf` | brueckenkern | 57 | 3 | 100.07 | brueckenpfad | reifung_oder_verdichtung |

## Interpretation

Die Anschlussanker-Familien tauchen in der Vergleichsgruppe nicht einfach identisch auf, sondern verschieben ihre Rolle.

- In 894 wirkt `0b7nep9` als starker verteilender Anschlussanker.
- In 901 ist `0b7nep9` Teil der Kernlandschaft und koppelt stark mit `0ykar6i`.
- `1jx2k4i` war in 894 kernnaher Inselanker; in 901 liegt es ebenfalls im Brueckenkernbereich.

Das ist ein wichtiger Befund: dieselben Feldzeichen koennen unter anderer Weltgruppe von Anschlussrolle in Kernrolle wandern.
Damit wird die MCM-Topologie nicht als starres Koordinatensystem gelesen, sondern als dynamische Feldordnung.

## Konsequenz

Die letzten Untersuchungen stuetzen drei Punkte:

1. Anschlussanker sind reproduzierbare Rollenformen.
2. Diese Rollen haben Unterfamilien: kernnah, verteilend, uebergangsartig.
3. Rollen koennen zwischen Weltgruppen wandern: ein Anschlussanker kann in einer anderen Weltgruppe zum Kernbestandteil werden.

Das spricht fuer eine lebendige Topologie: stabil genug, um wiederkehrende Rollen zu zeigen, aber flexibel genug, um Rollen je nach Weltspannung anders zu organisieren.

## Wie es weitergeht

Als naechstes sollte genau diese Rollenwanderung untersucht werden: Welche Weltmerkmale lassen `0b7nep9` vom verteilenden Anschlussanker zum Kernpartner von `0ykar6i` werden?