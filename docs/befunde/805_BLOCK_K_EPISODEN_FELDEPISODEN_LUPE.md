# 805 - Block-K Episoden- und Feldepisoden-Lupe

## Fragestellung

Entsteht die hoehere 10k-Stabilisierung aus echter laengerer Feldintegration oder nur aus der kompakten Score-Formel?

## Matrix

| Gruppe | Reports | Kerzen | Top-Episodendauer | Top-Feldepisodendauer | Feldepisoden-Wiederkehr | lange Feldepisoden | Carry | Rekopplung | Strain | passive Flags |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| normal | 4 | 2000.0000 | 664.6667 | 664.6667 | 0 | 3 | 0.4465 | 0.6493 | 0.2158 | 1 |
| stress | 4 | 1500.0000 | 543.1818 | 543.1818 | 0 | 2 | 0.4402 | 0.6383 | 0.2225 | 1 |
| lang_10k | 4 | 10000.0000 | 1043.7500 | 1077.3871 | 7 | 15 | 0.5013 | 0.6811 | 0.1827 | 1 |

## Rollenprofile

### normal

- Episoden: `dio_episode_154cuzi:3; dio_episode_0a0pcz7:3; dio_episode_1n7gs82:2; dio_episode_0g204cb:1; dio_episode_1v79xv7:1; dio_episode_1850w4f:1`
- MCM-Feldepisoden: `dio_mcm_episode_0e7qvj1:3; dio_mcm_episode_1k2bqha:3; dio_mcm_episode_0ryrezu:2; dio_mcm_episode_19q1eac:1; dio_mcm_episode_1wra2fc:1; dio_mcm_episode_1be25y5:1`
- Transitionen: `field_strained->field_carried:7; field_carried->field_strained:4; start->field_carried:1`

### stress

- Episoden: `dio_episode_0ae78kk:2; dio_episode_0zrkavd:1; dio_episode_1dy41xd:1; dio_episode_1v79xv7:1; dio_episode_154cuzi:1; dio_episode_1d3kaw1:1`
- MCM-Feldepisoden: `dio_mcm_episode_1joiyc3:3; dio_mcm_episode_0kji539:1; dio_mcm_episode_0m58ev9:1; dio_mcm_episode_1wra2fc:1; dio_mcm_episode_0e7qvj1:1; dio_mcm_episode_0eghs1d:1`
- Transitionen: `field_strained->field_carried:4; field_carried->field_strained:3; start->field_carried:3; field_fragmented->field_strained:1; field_strained->field_fragmented:1`

### lang_10k

- Episoden: `dio_episode_1vqbxxj:4; dio_episode_1fmr12g:4; dio_episode_1jcdupo:3; dio_episode_1tn1mea:2; dio_episode_1yx0ipz:2; dio_episode_0vpcnca:2`
- MCM-Feldepisoden: `dio_mcm_episode_0mk4vj4:4; dio_mcm_episode_1gwfnz5:4; dio_mcm_episode_0qx4uth:3; dio_mcm_episode_0sjrih9:2; dio_mcm_episode_0d1w2c7:2; dio_mcm_episode_1wra2fc:2`
- Transitionen: `field_strained->field_carried:16; field_carried->field_carried:14; field_carried->field_strained:14`

## Befund

Die hoehere 10k-Stabilisierung ist nicht nur ein reines Formelartefakt.

Dafuer sprechen in dieser Lupe:

- deutlich laengere Top-Episoden und Top-Feldepisoden in der 10k-Gruppe,
- mehr wiederkehrende Feldepisoden innerhalb der Top-Feldepisoden,
- hoehere Carry- und Rekopplungswerte bei niedrigerem Strain,
- passive Flags bleiben sauber: keine Gate-, Motorik-, Entry- oder Richtungskopplung.

Gleichzeitig bleibt die Grenze wichtig: Die Lupe nutzt Top-Episoden aus Reports. Sie zeigt starke Evidenz fuer laengere Feldintegration, aber noch keine vollstaendige Ereignis-fuer-Ereignis-Zeitreihe.

## Wie es weitergeht

Als naechstes sollte fuer eine 10k-Welt eine Ereigniszeitreihe der Feldepisoden geschrieben werden. Dann kann man sehen, wann Integration entsteht, wann sie bricht und ob Nachhall/Feldzeit diese Phasen traegt.
