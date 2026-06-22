# Synthetische Randdominanz - Rezeptorlimit nach adaptierter Feldkopplung

Passive Differenzdiagnose: Welche Rezeptorachse traegt Randlast, und wo wird sie vor dem MCM-Feld begrenzt?

Die Diagnose ist kein Gate und keine Runtime-Regel. Sie liest nur vorhandene Episodenspuren.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Lautheit | Schaerfe | Rohfeld | Adaptfeld | Reduktion | Ratio | Druck | MCM-Spannung | staerkste Achse | Begrenzung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| ruhig_basis | 600 | 0.9783 | 0.0083 | 0.0017 | 0.0247 | 0.8384 | 0.0179 | 0.0163 | 0.0016 | 0.9095 | 0.0256 | 0.0163 | sehen | adaptation |
| druckaufbau | 600 | 0.9767 | 0.0117 | 0.0017 | 0.0284 | 0.8345 | 0.0213 | 0.0193 | 0.0020 | 0.9068 | 0.0316 | 0.0193 | sehen | adaptation |
| laute_randphase | 800 | 0.0650 | 0.7612 | 0.0288 | 0.2779 | 0.5375 | 0.1644 | 0.1353 | 0.0291 | 0.8229 | 0.1558 | 0.1353 | sehen | adaptation |
| asymmetrischer_bruch | 700 | 0.8429 | 0.0786 | 0.0000 | 0.1235 | 0.8051 | 0.0751 | 0.0670 | 0.0081 | 0.8922 | 0.0814 | 0.0670 | sehen | adaptation |
| gegenzerrung | 700 | 0.9471 | 0.0214 | 0.0000 | 0.0463 | 0.8247 | 0.0334 | 0.0303 | 0.0031 | 0.9082 | 0.0482 | 0.0303 | sehen | adaptation |
| ueberreizter_nachhall | 700 | 0.9100 | 0.0357 | 0.0014 | 0.0890 | 0.7771 | 0.0553 | 0.0494 | 0.0058 | 0.8942 | 0.0598 | 0.0494 | sehen | adaptation |
| rekopplungsversuch | 700 | 0.9929 | 0.0043 | 0.0014 | 0.0263 | 0.8381 | 0.0196 | 0.0179 | 0.0017 | 0.9118 | 0.0294 | 0.0179 | sehen | adaptation |
| ruhe_restspannung | 600 | 0.9950 | 0.0033 | 0.0017 | 0.0267 | 0.8387 | 0.0191 | 0.0174 | 0.0018 | 0.9077 | 0.0271 | 0.0174 | sehen | adaptation |
| zweiter_randstoss | 600 | 0.9500 | 0.0233 | 0.0033 | 0.1192 | 0.7990 | 0.0738 | 0.0656 | 0.0082 | 0.8893 | 0.0825 | 0.0656 | sehen | adaptation |
| schluss_rekopplung | 994 | 0.9970 | 0.0030 | 0.0000 | 0.0230 | 0.8369 | 0.0176 | 0.0161 | 0.0015 | 0.9152 | 0.0274 | 0.0161 | sehen | adaptation |

## Befund

- Staerkste lokale Rand/Kipp-Naehe: `laute_randphase` mit `0.0288`.
- Staerkste offene Variante: `laute_randphase` mit `0.7612`.
- Staerkste auditive Lautheit: `laute_randphase` mit `0.2779`.
- Staerkste rezeptorische Reduktion: `laute_randphase` mit `0.0291`.
- Niedrigste visuelle Schaerfe: `laute_randphase` mit `0.5375`.

## Ableitung

Rand-/Oeffnungslast entsteht in den geprueften synthetischen Welten nicht als reine MCM-Entgleisung. Sie steigt lokal dort, wo auditive Lautheit, Rohfeldaufnahme und fallende visuelle Schaerfe zusammenkommen.

Die Begrenzung liegt bisher vor allem in der rezeptorischen Adaptation: Rohfeldaufnahme wird in adaptierte Feldaufnahme uebersetzt, und die Randphase bleibt deshalb lokal statt global kollabierend.

Damit wirkt die Rezeptorschicht nicht nur als Vorfilter, sondern als organische Aufnahmegrenze: Sie laesst Weltspannung ins Feld, aber nicht als ungebremste Rohdatenflut.

Wie es weitergeht: Als naechstes sollte dieselbe Achsendiagnose gegen Bruch/Rand und Harmonie laufen, damit klar wird, ob die Begrenzung spezifisch fuer Randdominanz ist oder eine allgemeine MINI_DIO-Aufnahmeeigenschaft.
