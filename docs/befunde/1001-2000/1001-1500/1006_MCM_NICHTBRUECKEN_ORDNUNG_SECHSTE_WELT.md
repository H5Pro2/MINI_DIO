# MCM-Nicht-Bruecken-Lesung

## Zweck

Diese Diagnose liest eine Weltgruppe, in der die bisherige Brueckenlogik keine Brueckenlandschaft bildet.
Sie fragt nicht nach Anschlussankern, sondern nach passiver Ordnung ohne Bruecke.

## Klassenprofil

| Klasse | Anzahl | mittlere Last | mittlere Sinnesaufnahme | mittlere Rekopplung |
|---|---:|---:|---:|---:|
| `nichtbruecke_zentrum_schwach` | 63 | 0.1535 | 0.8601 | 0.6867 |
| `nichtbruecke_sinnesrauschen` | 20 | 0.2161 | 0.7805 | 0.6367 |
| `nichtbruecke_randspannung` | 19 | 0.3270 | 0.6725 | 0.5611 |
| `nichtbruecke_offen` | 12 | 0.2000 | 0.7774 | 0.6512 |
| `nichtbruecke_mehrdeutige_oberflaeche` | 8 | 0.1779 | 0.8111 | 0.6656 |
| `nichtbruecke_driftfeld` | 6 | 0.1862 | 0.8149 | 0.6512 |
| `nichtbruecke_zentrum_getragen` | 5 | 0.1557 | 0.8519 | 0.6975 |
| `nichtbruecke_rekopplungsfeld` | 4 | 0.1589 | 0.8424 | 0.6891 |

## Staerkste Nicht-Bruecken-Zeichen

| Token | Klasse | Zone | Rolle | Beobachtungen | Welten | Note |
|---|---|---|---|---:|---:|---|
| `0e7qvj1` | `nichtbruecke_zentrum_getragen` | `rekopplungszone` | `zentrum_stabil` | 5462 | 4 | zentral, wiederkehrend, geringe Last |
| `1hdpu9s` | `nichtbruecke_zentrum_getragen` | `rekopplungszone` | `zentrum_stabil` | 524 | 4 | zentral, wiederkehrend, geringe Last |
| `1joiyc3` | `nichtbruecke_zentrum_schwach` | `hoeherer_cluster_uebergang` | `zentrum_stabil` | 424 | 2 | Zentrumsrolle vorhanden, aber nicht brueckenbildend |
| `1ahj81f` | `nichtbruecke_zentrum_schwach` | `stabile_bedeutungsinsel` | `zentrum_stabil` | 358 | 2 | Zentrumsrolle vorhanden, aber nicht brueckenbildend |
| `1q3us3f` | `nichtbruecke_zentrum_getragen` | `rekopplungszone` | `zentrum_stabil` | 228 | 3 | zentral, wiederkehrend, geringe Last |
| `1rxdw4p` | `nichtbruecke_zentrum_getragen` | `rekopplungszone` | `zentrum_stabil` | 215 | 3 | zentral, wiederkehrend, geringe Last |
| `0mji3u6` | `nichtbruecke_zentrum_schwach` | `hoeherer_cluster_uebergang` | `zentrum_stabil` | 123 | 3 | Zentrumsrolle vorhanden, aber nicht brueckenbildend |
| `0db07p4` | `nichtbruecke_zentrum_schwach` | `stabile_bedeutungsinsel` | `zentrum_stabil` | 98 | 2 | Zentrumsrolle vorhanden, aber nicht brueckenbildend |
| `1jx2k4i` | `nichtbruecke_zentrum_getragen` | `stabile_bedeutungsinsel` | `zentrum_stabil` | 67 | 3 | zentral, wiederkehrend, geringe Last |
| `0z748ck` | `nichtbruecke_rekopplungsfeld` | `rekopplungszone` | `zentrum_stabil` | 44 | 4 | Rekopplung sichtbar, aber nicht als Bruecke organisiert |
| `0qzjuvj` | `nichtbruecke_rekopplungsfeld` | `rekopplungszone` | `zentrum_stabil` | 40 | 4 | Rekopplung sichtbar, aber nicht als Bruecke organisiert |
| `0jbl5pq` | `nichtbruecke_zentrum_schwach` | `hoeherer_cluster_uebergang` | `zentrum_stabil` | 28 | 4 | Zentrumsrolle vorhanden, aber nicht brueckenbildend |
| `1hs3jsa` | `nichtbruecke_zentrum_schwach` | `rekopplungszone` | `zentrum_stabil` | 19 | 1 | Zentrumsrolle vorhanden, aber nicht brueckenbildend |
| `0lne9ax` | `nichtbruecke_rekopplungsfeld` | `rekopplungszone` | `zentrum_stabil` | 18 | 4 | Rekopplung sichtbar, aber nicht als Bruecke organisiert |
| `0lfde2c` | `nichtbruecke_mehrdeutige_oberflaeche` | `stabile_bedeutungsinsel` | `zentrum_stabil` | 16 | 1 | Rollenmischung ohne stabile Anschlussrolle |
| `0aztxel` | `nichtbruecke_zentrum_schwach` | `hoeherer_cluster_uebergang` | `zentrum_stabil` | 11 | 3 | Zentrumsrolle vorhanden, aber nicht brueckenbildend |
| `1rylps5` | `nichtbruecke_zentrum_schwach` | `stabile_bedeutungsinsel` | `zentrum_stabil` | 10 | 1 | Zentrumsrolle vorhanden, aber nicht brueckenbildend |
| `0hjnwsk` | `nichtbruecke_zentrum_schwach` | `hoeherer_cluster_uebergang` | `zentrum_stabil` | 8 | 4 | Zentrumsrolle vorhanden, aber nicht brueckenbildend |
| `0l3i7ey` | `nichtbruecke_zentrum_schwach` | `hoeherer_cluster_uebergang` | `zentrum_stabil` | 8 | 4 | Zentrumsrolle vorhanden, aber nicht brueckenbildend |
| `07llqq8` | `nichtbruecke_randspannung` | `hoeherer_cluster_uebergang` | `zentrum_stabil` | 7 | 2 | Rand- oder Lastnaehe ohne Brueckenbindung |

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