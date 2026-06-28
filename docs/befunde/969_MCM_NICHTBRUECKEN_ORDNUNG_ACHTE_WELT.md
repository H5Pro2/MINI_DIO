# MCM-Nicht-Bruecken-Lesung

## Zweck

Diese Diagnose liest eine Weltgruppe, in der die bisherige Brueckenlogik keine Brueckenlandschaft bildet.
Sie fragt nicht nach Anschlussankern, sondern nach passiver Ordnung ohne Bruecke.

## Klassenprofil

| Klasse | Anzahl | mittlere Last | mittlere Sinnesaufnahme | mittlere Rekopplung |
|---|---:|---:|---:|---:|
| `nichtbruecke_offen` | 2753 | 0.2160 | 0.8083 | 0.6073 |
| `nichtbruecke_randspannung` | 1672 | 0.3272 | 0.7623 | 0.5787 |
| `nichtbruecke_zentrum_schwach` | 1445 | 0.1824 | 0.8642 | 0.6452 |
| `nichtbruecke_mehrdeutige_oberflaeche` | 91 | 0.1908 | 0.8270 | 0.6255 |
| `nichtbruecke_driftfeld` | 26 | 0.2129 | 0.7903 | 0.6100 |
| `nichtbruecke_rekopplungsfeld` | 5 | 0.1427 | 0.8758 | 0.6604 |
| `nichtbruecke_offene_wahrnehmungsinsel` | 3 | 0.2479 | 0.7885 | 0.5970 |

## Staerkste Nicht-Bruecken-Zeichen

| Token | Klasse | Zone | Rolle | Beobachtungen | Welten | Note |
|---|---|---|---|---:|---:|---|
| `0hx9wod` | `nichtbruecke_randspannung` | `hoeherer_cluster_uebergang` | `spannungsrand_kippnaehe` | 45 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1be7j1w` | `nichtbruecke_offene_wahrnehmungsinsel` | `hoeherer_cluster_uebergang` | `offene_variante` | 40 | 4 | offene Lage mit hoher Sinnesaufnahme |
| `0je96vc` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 28 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `128nsns` | `nichtbruecke_offene_wahrnehmungsinsel` | `hoeherer_cluster_uebergang` | `offene_variante` | 24 | 4 | offene Lage mit hoher Sinnesaufnahme |
| `1hngpuz` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 24 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1ov3cz9` | `nichtbruecke_offene_wahrnehmungsinsel` | `hoeherer_cluster_uebergang` | `offene_variante` | 22 | 4 | offene Lage mit hoher Sinnesaufnahme |
| `1pdseek` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 21 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1pns03j` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 20 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `0hnaaze` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 19 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1bna9pq` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 19 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1bo74qv` | `nichtbruecke_mehrdeutige_oberflaeche` | `hoeherer_cluster_uebergang` | `offene_variante` | 18 | 4 | Rollenmischung ohne stabile Anschlussrolle |
| `1cz6mbd` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 17 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1wq16f8` | `nichtbruecke_mehrdeutige_oberflaeche` | `hoeherer_cluster_uebergang` | `offene_variante` | 16 | 4 | Rollenmischung ohne stabile Anschlussrolle |
| `0jo8skb` | `nichtbruecke_randspannung` | `hoeherer_cluster_uebergang` | `spannungsrand_kippnaehe` | 16 | 3 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1hd5g2b` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 16 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1bdao0r` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 15 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1fgike5` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 15 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1rc968y` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 15 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1hdh460` | `nichtbruecke_randspannung` | `randnahe_verdichtung` | `spannungsrand_kippnaehe` | 14 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |
| `1tktg9t` | `nichtbruecke_randspannung` | `hoeherer_cluster_uebergang` | `spannungsrand_kippnaehe` | 14 | 4 | Rand- oder Lastnaehe ohne Brueckenbindung |

## Interpretation

Eine Welt ohne Brueckenlandschaft ist nicht automatisch ungeordnet.
Sie kann Verdichtung, Wiederkehr, Zentrumsnaehe, offene Wahrnehmungsinseln oder Randspannung tragen, ohne daraus stabile Anschlussanker zu bilden.

Fachlich ist das wichtig, weil MINI_DIO damit zwei Ordnungsarten unterscheiden kann:

- Ordnung mit Bruecken: Bedeutungen verbinden sich topologisch ueber Anschlussrollen.
- Ordnung ohne Bruecken: Bedeutungen bleiben als Inseln, Driftfelder oder Sinnesoberflaechen sichtbar, koppeln aber nicht stabil weiter.

## Schlussfolgerung

Diese Welt sollte nicht mit Brueckenlogik erzwungen werden.
Sie braucht eine eigene passive Lesung fuer Nicht-Bruecken-Ordnung.

## Wie es weitergeht

Als naechstes sollte diese Nicht-Bruecken-Karte gegen die zugehoerigen Verdichtungszonen und Pfadklassen synthetisiert werden.
Entscheidend ist, ob die Welt eher offene Wahrnehmungsinseln, Zentrumsinseln, Randspannung oder Sinnesrauschen bildet.