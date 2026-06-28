# MCM-Brueckenkerne Vergleich

## Zweck

Diese Diagnose vergleicht alle internen Brueckenpaare aus dem Brueckennetz.
Ziel ist zu pruefen, ob es einen zentralen Brueckenkern oder mehrere getrennte Brueckenkerne gibt.

## Kernklassen

| Klasse | Anzahl |
|---|---:|
| lokaler_brueckenpfad | 4 |
| schwache_brueckenkante | 3 |
| sekundaerer_brueckenkern | 1 |
| zentraler_brueckenkern | 2 |

## Brueckenpaare

| Klasse | Token A | Token B | Gewicht | Welten | bidirektional | A->B | B->A | Dauer | Exitphase |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| sekundaerer_brueckenkern | dio_mcm_episode_0b7nep9 | dio_mcm_episode_0ykar6i | 176 | 4 | 1 | 2 | 2 | 74.02 | rekoppelnder_austritt |
| zentraler_brueckenkern | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 110 | 6 | 1 | 2 | 2 | 61.71 | oeffnend_belastender_austritt |
| zentraler_brueckenkern | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_0mji3u6 | 74 | 6 | 1 | 2 | 2 | 119.65 | oeffnend_belastender_austritt |
| lokaler_brueckenpfad | dio_mcm_episode_14coypf | dio_mcm_episode_18l3thm | 24 | 3 | 1 | 2 | 2 | 95.29 | oeffnend_belastender_austritt |
| lokaler_brueckenpfad | dio_mcm_episode_0mji3u6 | dio_mcm_episode_18n06fj | 20 | 5 | 0 | 0 | 2 | 6.70 | rekoppelnder_austritt |
| lokaler_brueckenpfad | dio_mcm_episode_0jbl5pq | dio_mcm_episode_0qzjuvj | 18 | 6 | 0 | 2 | 0 | 2.61 | oeffnend_belastender_austritt |
| lokaler_brueckenpfad | dio_mcm_episode_0hjnwsk | dio_mcm_episode_18n06fj | 16 | 4 | 0 | 2 | 0 | 2.81 | rekoppelnder_austritt |
| schwache_brueckenkante | dio_mcm_episode_02ujuqf | dio_mcm_episode_1xx3u1e | 6 | 3 | 0 | 2 | 0 | 207.67 | oeffnend_belastender_austritt |
| schwache_brueckenkante | dio_mcm_episode_0e7qvj1 | dio_mcm_episode_14coypf | 4 | 1 | 1 | 2 | 2 | 15.25 | oeffnend_belastender_austritt |
| schwache_brueckenkante | dio_mcm_episode_0hjnwsk | dio_mcm_episode_0qzjuvj | 4 | 2 | 0 | 0 | 2 | 1.50 | rekoppelnder_austritt |

## Befund

Der staerkste Kern ist `dio_mcm_episode_0b7nep9` <-> `dio_mcm_episode_0ykar6i` mit Gewicht `176` und Weltspanne `4`.
Es gibt mehrere zentrale Brueckenkerne. Das wuerde fuer eine verteilte Uebergangstopologie sprechen.
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
