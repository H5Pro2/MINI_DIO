# MCM-Brueckenkerne Vergleich

## Zweck

Diese Diagnose vergleicht alle internen Brueckenpaare aus dem Brueckennetz.
Ziel ist zu pruefen, ob es einen zentralen Brueckenkern oder mehrere getrennte Brueckenkerne gibt.

## Kernklassen

| Klasse | Anzahl |
|---|---:|
| lokaler_brueckenpfad | 1 |
| schwache_brueckenkante | 2 |

## Brueckenpaare

| Klasse | Token A | Token B | Gewicht | Welten | bidirektional | A->B | B->A | Dauer | Exitphase |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| lokaler_brueckenpfad | dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | 18 | 6 | 0 | 2 | 0 | 2.61 | oeffnend_belastender_austritt |
| schwache_brueckenkante | dio_mcm_episode_0hjnwsk | dio_mcm_episode_0qzjuvj | 4 | 2 | 0 | 0 | 2 | 1.50 | rekoppelnder_austritt |
| schwache_brueckenkante | dio_mcm_episode_0jbl5pq | dio_mcm_episode_0l3i7ey | 2 | 1 | 0 | 0 | 2 | 2.00 | gemischter_austritt |

## Befund

Der staerkste Kern ist `dio_mcm_episode_0jbl5pq` <-> `dio_mcm_episode_0qzjuvj` mit Gewicht `18` und Weltspanne `6`.
Es gibt keinen einzelnen dominanten zentralen Kern. Das Feld waere eher verteilt oder lokal organisiert.

## Bedeutung

Die Brueckentopologie wirkt hier hierarchisch:

```text
zentraler Brueckenkern
sekundaere Brueckenkerne
lokale Brueckenpfade
schwache Brueckenkanten
```

Damit entsteht keine flache Verbindungsliste, sondern eine strukturierte Uebergangstopologie.

## Wie es weitergeht

Als naechstes sollte die Rolle des zentralen Kerns gegen Randpfade und stabile Inseln gelesen werden: fuehrt der Kern eher in Zentrum, Rand oder offene Feldlagen?
