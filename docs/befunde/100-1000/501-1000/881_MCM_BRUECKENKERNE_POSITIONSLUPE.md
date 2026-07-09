# MCM-Brueckenkerne Positionslupe

## Zweck

Diese Diagnose prueft, ob die Brueckenkerne selbst zentrumsnah liegen oder ob ihre Zentrumsnaehe nur indirekt durch stabile Anschlussinseln entsteht.

## Befund

### zentraler_kern_0e7qvj1_18l3thm

- Tokens: 2
- Mittlerer Positionswert: `0.7368`
- Rollenlabel: `zentrumsnahe_bruecke=1, zentrumsnaher_uebergang=1`

| Token | Klasse | Zone vorher | Zone nachher | Rolle | Positionslabel | Score |
|---|---|---|---|---|---|---:|
| `0e7qvj1` | brueckenpfad | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | zentrum_stabil -> zentrum_stabil | zentrumsnahe_bruecke | 0.7105 |
| `18l3thm` | brueckenpfad | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | zentrum_stabil -> zentrum_stabil | zentrumsnaher_uebergang | 0.7632 |

### sekundaerer_anschlusskern_0db07p4_1joiyc3

- Tokens: 2
- Mittlerer Positionswert: `0.7368`
- Rollenlabel: `zentrumsnahe_bruecke=1, zentrumsnaher_uebergang=1`

| Token | Klasse | Zone vorher | Zone nachher | Rolle | Positionslabel | Score |
|---|---|---|---|---|---|---:|
| `1joiyc3` | brueckenpfad | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | zentrum_stabil -> zentrum_stabil | zentrumsnahe_bruecke | 0.7105 |
| `0db07p4` | brueckenpfad | stabile_bedeutungsinsel | hoeherer_cluster_uebergang | zentrum_stabil -> zentrum_stabil | zentrumsnaher_uebergang | 0.7632 |

### seitenarm_0e7qvj1_0mji3u6

- Tokens: 2
- Mittlerer Positionswert: `0.7368`
- Rollenlabel: `zentrumsnahe_bruecke=1, zentrumsnaher_uebergang=1`

| Token | Klasse | Zone vorher | Zone nachher | Rolle | Positionslabel | Score |
|---|---|---|---|---|---|---:|
| `0e7qvj1` | brueckenpfad | hoeherer_cluster_uebergang | hoeherer_cluster_uebergang | zentrum_stabil -> zentrum_stabil | zentrumsnahe_bruecke | 0.7105 |
| `0mji3u6` | brueckenpfad | hoeherer_cluster_uebergang | stabile_bedeutungsinsel | zentrum_stabil -> zentrum_stabil | zentrumsnaher_uebergang | 0.7632 |

## Interpretation

Die untersuchten Brueckenkerne sind in der Pfadklassifikation nicht randnah.
Ihre Tokens tragen durchgehend `zentrum_stabil` als Rollenlage.

Der Unterschied liegt in der Zonenbewegung:

- reine Bruecken-Tokens bleiben im hoeheren Clusteruebergang,
- reifende Bruecken-Tokens verbinden Uebergang und stabile Bedeutungsinsel,
- der stabile Anschlusskern koppelt enger an stabile Inselbereiche.

Damit wirkt die Zentrumsnaehe nicht nur indirekt durch stabile Inseln.
Die Brueckenkerne selbst tragen bereits eine zentrumsnahe Rollenlage, unterscheiden sich aber in ihrer Anschlussfunktion.

Wichtig:

Der numerische Positionswert ist hier nur eine grobe Lesegroesse.
Er faellt bei den drei Kernen gleich aus, weil alle untersuchten Kern-Tokens dieselbe Rollenlage `zentrum_stabil` tragen.
Die fachliche Differenz entsteht nicht aus dem Score, sondern aus der Zonenbewegung und aus der Netzwerkfunktion:

```text
Bruecke bleibt Bruecke,
Bruecke koppelt an stabile Insel,
Bruecke wirkt als Seitenarm eines zentralen Kerns.
```

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob Randpfade eigene Gegenkerne bilden oder ob sie nur kurzlebige Oberflaechen- und Austrittsphaenomene bleiben.
