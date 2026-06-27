# MCM-Brueckenkerne Vergleich

## Zweck

Diese Diagnose vergleicht alle internen Brueckenpaare aus dem Brueckennetz.
Ziel ist zu pruefen, ob es einen zentralen Brueckenkern oder mehrere getrennte Brueckenkerne gibt.

## Kernklassen

| Klasse | Anzahl |
|---|---:|
| lokaler_brueckenpfad | 2 |
| schwache_brueckenkante | 1 |
| sekundaerer_brueckenkern | 2 |
| zentraler_brueckenkern | 1 |

## Brueckenpaare

| Klasse | Token A | Token B | Gewicht | Welten | bidirektional | A->B | B->A | Dauer | Exitphase |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| zentraler_brueckenkern | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 84 | 5 | 1 | 2 | 2 | 84.29 | oeffnend_belastender_austritt |
| sekundaerer_brueckenkern | dio_mcm_episode_0db07p4 | dio_mcm_episode_1joiyc3 | 34 | 5 | 1 | 2 | 2 | 69.15 | rekoppelnder_austritt |
| sekundaerer_brueckenkern | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 34 | 5 | 1 | 2 | 2 | 226.06 | oeffnend_belastender_austritt |
| lokaler_brueckenpfad | dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | 14 | 5 | 0 | 2 | 0 | 2.57 | rekoppelnder_austritt |
| lokaler_brueckenpfad | dio_mcm_episode_0mji3u6 | dio_mcm_episode_18n06fj | 8 | 3 | 0 | 0 | 2 | 6.25 | oeffnend_belastender_austritt |
| schwache_brueckenkante | dio_mcm_episode_0qzjuvj | dio_mcm_episode_18n06fj | 2 | 1 | 0 | 2 | 0 | 3.00 | oeffnend_belastender_austritt |

## Befund

Der staerkste Kern ist `dio_mcm_episode_0e7qvj1` <-> `dio_mcm_episode_18l3thm` mit Gewicht `84` und Weltspanne `5`.
Es gibt genau einen zentralen Brueckenkern. Die uebrigen Paare wirken als sekundaere Kerne oder lokale Pfade.
Sekundaere Kerne sind vorhanden. Sie bilden wahrscheinlich lokale Uebergangsbereiche um den Hauptkern herum.

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
