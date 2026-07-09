# MCM-Brueckenkerne Vergleich

## Zweck

Diese Diagnose vergleicht alle internen Brueckenpaare aus dem Brueckennetz.
Ziel ist zu pruefen, ob es einen zentralen Brueckenkern oder mehrere getrennte Brueckenkerne gibt.

## Kernklassen

| Klasse | Anzahl |
|---|---:|
| lokaler_brueckenpfad | 4 |
| schwache_brueckenkante | 3 |
| zentraler_brueckenkern | 2 |

## Brueckenpaare

| Klasse | Token A | Token B | Gewicht | Welten | bidirektional | A->B | B->A | Dauer | Exitphase |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| zentraler_brueckenkern | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 110 | 6 | 1 | 2 | 2 | 61.71 | oeffnend_belastender_austritt |
| zentraler_brueckenkern | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 74 | 6 | 1 | 2 | 2 | 119.65 | oeffnend_belastender_austritt |
| lokaler_brueckenpfad | dio_mcm_episode_0mji3u6 | dio_mcm_episode_18n06fj | 20 | 5 | 0 | 0 | 2 | 6.70 | rekoppelnder_austritt |
| lokaler_brueckenpfad | dio_mcm_episode_0db07p4 | dio_mcm_episode_1joiyc3 | 18 | 3 | 1 | 2 | 2 | 68.56 | rekoppelnder_austritt |
| lokaler_brueckenpfad | dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | 18 | 6 | 0 | 2 | 0 | 2.61 | oeffnend_belastender_austritt |
| lokaler_brueckenpfad | dio_mcm_episode_0hjnwsk | dio_mcm_episode_18n06fj | 16 | 4 | 0 | 2 | 0 | 2.81 | rekoppelnder_austritt |
| schwache_brueckenkante | dio_mcm_episode_0hjnwsk | dio_mcm_episode_0qzjuvj | 4 | 2 | 0 | 0 | 2 | 1.50 | rekoppelnder_austritt |
| schwache_brueckenkante | dio_mcm_episode_0b7nep9 | dio_mcm_episode_17c7qwp | 2 | 1 | 0 | 0 | 2 | 188.50 | gemischter_austritt |
| schwache_brueckenkante | dio_mcm_episode_0jbl5pq | dio_mcm_episode_0l3i7ey | 2 | 1 | 0 | 0 | 2 | 2.00 | gemischter_austritt |

## Befund

Der staerkste Kern ist `dio_mcm_episode_0e7qvj1` <-> `dio_mcm_episode_18l3thm` mit Gewicht `110` und Weltspanne `6`.
Es gibt mehrere zentrale Brueckenkerne. Das wuerde fuer eine verteilte Uebergangstopologie sprechen.

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
