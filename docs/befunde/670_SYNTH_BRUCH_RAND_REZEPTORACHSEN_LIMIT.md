# Synthetische Bruch/Rand-Welt - Rezeptorachsen-Limit

Passive Differenzdiagnose: Welche Rezeptorachse traegt Randlast, und wo wird sie vor dem MCM-Feld begrenzt?

Die Diagnose ist kein Gate und keine Runtime-Regel. Sie liest nur vorhandene Episodenspuren.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Lautheit | Schaerfe | Rohfeld | Adaptfeld | Reduktion | Ratio | Druck | MCM-Spannung | staerkste Achse | Begrenzung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| ruhig_vorlast | 700 | 0.9843 | 0.0057 | 0.0014 | 0.0227 | 0.8387 | 0.0173 | 0.0158 | 0.0015 | 0.9112 | 0.0265 | 0.0173 | sehen | adaptation |
| oeffnung | 700 | 0.9757 | 0.0114 | 0.0014 | 0.0287 | 0.8337 | 0.0221 | 0.0201 | 0.0020 | 0.9078 | 0.0344 | 0.0221 | sehen | adaptation |
| bruch_impuls | 700 | 0.8829 | 0.0543 | 0.0000 | 0.0684 | 0.8077 | 0.0478 | 0.0430 | 0.0048 | 0.8997 | 0.0662 | 0.0478 | sehen | adaptation |
| randflackern | 700 | 0.2871 | 0.4971 | 0.0043 | 0.1454 | 0.6242 | 0.0938 | 0.0808 | 0.0130 | 0.8618 | 0.1057 | 0.0938 | sehen | adaptation |
| gegenpol | 700 | 0.9729 | 0.0100 | 0.0014 | 0.0510 | 0.8210 | 0.0368 | 0.0333 | 0.0035 | 0.9046 | 0.0533 | 0.0368 | sehen | adaptation |
| rekopplung | 700 | 0.9914 | 0.0057 | 0.0014 | 0.0279 | 0.8355 | 0.0212 | 0.0193 | 0.0019 | 0.9120 | 0.0327 | 0.0212 | sehen | adaptation |
| ruhe_nachhall | 700 | 0.9929 | 0.0029 | 0.0014 | 0.0252 | 0.8375 | 0.0187 | 0.0170 | 0.0017 | 0.9089 | 0.0276 | 0.0187 | sehen | adaptation |
| zweiter_kippimpuls | 500 | 0.9800 | 0.0060 | 0.0040 | 0.0825 | 0.8027 | 0.0538 | 0.0482 | 0.0056 | 0.8958 | 0.0661 | 0.0538 | sehen | adaptation |
| zweite_rekopplung | 594 | 0.9865 | 0.0051 | 0.0000 | 0.0315 | 0.8349 | 0.0225 | 0.0205 | 0.0020 | 0.9124 | 0.0318 | 0.0225 | sehen | adaptation |

## Befund

- Staerkste lokale Rand/Kipp-Naehe: `randflackern` mit `0.0043`.
- Staerkste offene Variante: `randflackern` mit `0.4971`.
- Staerkste auditive Lautheit: `randflackern` mit `0.1454`.
- Staerkste rezeptorische Reduktion: `randflackern` mit `0.0130`.
- Niedrigste visuelle Schaerfe: `randflackern` mit `0.6242`.

## Ableitung

Rand-/Oeffnungslast entsteht in den geprueften synthetischen Welten nicht als reine MCM-Entgleisung. Sie steigt lokal dort, wo auditive Lautheit, Rohfeldaufnahme und fallende visuelle Schaerfe zusammenkommen.

Die Begrenzung liegt bisher vor allem in der rezeptorischen Adaptation: Rohfeldaufnahme wird in adaptierte Feldaufnahme uebersetzt, und die Randphase bleibt deshalb lokal statt global kollabierend.

Damit wirkt die Rezeptorschicht nicht nur als Vorfilter, sondern als organische Aufnahmegrenze: Sie laesst Weltspannung ins Feld, aber nicht als ungebremste Rohdatenflut.

Wie es weitergeht: Als naechstes sollte dieselbe Achsendiagnose gegen Bruch/Rand und Harmonie laufen, damit klar wird, ob die Begrenzung spezifisch fuer Randdominanz ist oder eine allgemeine MINI_DIO-Aufnahmeeigenschaft.
