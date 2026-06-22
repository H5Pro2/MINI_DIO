# Synthetische Harmonie - Rezeptorachsen-Limit

Passive Differenzdiagnose: Welche Rezeptorachse traegt Randlast, und wo wird sie vor dem MCM-Feld begrenzt?

Die Diagnose ist kein Gate und keine Runtime-Regel. Sie liest nur vorhandene Episodenspuren.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Lautheit | Schaerfe | Rohfeld | Adaptfeld | Reduktion | Ratio | Druck | MCM-Spannung | staerkste Achse | Begrenzung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| ruhig | 900 | 0.9911 | 0.0022 | 0.0011 | 0.0155 | 0.8400 | 0.0144 | 0.0131 | 0.0012 | 0.9139 | 0.0271 | 0.0144 | sehen | adaptation |
| expansion | 900 | 0.9889 | 0.0078 | 0.0000 | 0.0231 | 0.8367 | 0.0212 | 0.0194 | 0.0018 | 0.9136 | 0.0403 | 0.0212 | sehen | adaptation |
| unruhe | 900 | 0.9800 | 0.0111 | 0.0000 | 0.0194 | 0.8341 | 0.0207 | 0.0189 | 0.0018 | 0.9136 | 0.0437 | 0.0207 | sehen | adaptation |
| kippnaehe | 900 | 0.9589 | 0.0167 | 0.0011 | 0.0286 | 0.8272 | 0.0278 | 0.0253 | 0.0026 | 0.9081 | 0.0554 | 0.0278 | sehen | adaptation |
| rekopplung | 900 | 0.9933 | 0.0033 | 0.0011 | 0.0207 | 0.8366 | 0.0197 | 0.0180 | 0.0017 | 0.9127 | 0.0386 | 0.0197 | sehen | adaptation |
| ruhe_rueckkehr | 894 | 0.9966 | 0.0022 | 0.0000 | 0.0160 | 0.8390 | 0.0148 | 0.0136 | 0.0012 | 0.9179 | 0.0280 | 0.0148 | sehen | adaptation |

## Befund

- Staerkste lokale Rand/Kipp-Naehe: `ruhig` mit `0.0011`.
- Staerkste offene Variante: `kippnaehe` mit `0.0167`.
- Staerkste auditive Lautheit: `kippnaehe` mit `0.0286`.
- Staerkste rezeptorische Reduktion: `kippnaehe` mit `0.0026`.
- Niedrigste visuelle Schaerfe: `kippnaehe` mit `0.8272`.

## Ableitung

Rand-/Oeffnungslast entsteht in den geprueften synthetischen Welten nicht als reine MCM-Entgleisung. Sie steigt lokal dort, wo auditive Lautheit, Rohfeldaufnahme und fallende visuelle Schaerfe zusammenkommen.

Die Begrenzung liegt bisher vor allem in der rezeptorischen Adaptation: Rohfeldaufnahme wird in adaptierte Feldaufnahme uebersetzt, und die Randphase bleibt deshalb lokal statt global kollabierend.

Damit wirkt die Rezeptorschicht nicht nur als Vorfilter, sondern als organische Aufnahmegrenze: Sie laesst Weltspannung ins Feld, aber nicht als ungebremste Rohdatenflut.

Wie es weitergeht: Als naechstes sollte dieselbe Achsendiagnose gegen Bruch/Rand und Harmonie laufen, damit klar wird, ob die Begrenzung spezifisch fuer Randdominanz ist oder eine allgemeine MINI_DIO-Aufnahmeeigenschaft.
