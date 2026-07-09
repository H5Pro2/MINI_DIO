# DOGE-1h-Jahr: Topologische Bewegungsrollen

Stand: 2026-06-22

## Zweck

Diese Diagnose liest DOGE/USDT auf 1h-Jahreswelten als Zeitaufl?sungs-Gegenpr?fung zur DOGE-5m-Rauschwelt.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Verst?rkt DOGE 1h offene Variante, Randn?he oder Strain gegen?ber DOGE 5m?
2. Unterpr?fung: Bleibt `0e7qvj1` als zentrumsnaher Anker sichtbar?
3. Unterpr?fung: Bleibt die Hin-/R?ckweg-Asymmetrie erhalten?
4. Folgeschritt: DOGE 5m gegen DOGE 1h synthetisieren.

## Kompakter Befund

- Bewegungsachsen gesamt: 160
- Dominante Rollenwechsel:
  - `zentrum_stabil->zentrum_stabil`: 72
  - `zentrum_stabil->offene_variante`: 22
  - `offene_variante->zentrum_stabil`: 19
  - `offene_variante->offene_variante`: 16
  - `zentrum_stabil->spannungsrand_kippnaehe`: 12
  - `spannungsrand_kippnaehe->offene_variante`: 8
  - `spannungsrand_kippnaehe->zentrum_stabil`: 6
  - `offene_variante->spannungsrand_kippnaehe`: 3
- Bewegungswirkungen:
  - `rekoppelnd_entlastend`: 67
  - `oeffnend_belastend`: 55
  - `bewegung_offen`: 24
  - `spannungsnah`: 14

## St?rkste Rollenbewegungen

| Bewegung | Ereignisse | dominante Rolle | Anteil | Wirkung | Druck | Rekopplung | Lautheit | dominante Welt |
|---|---:|---|---:|---|---:|---:|---:|---|
| `0e7qvj1->1hdpu9s` | 34 | `zentrum_stabil->zentrum_stabil` | 0.971 | `rekoppelnd_entlastend` | -0.0150 | +0.0068 | -0.0403 | `DOGE_2024_1H_YEAR (21/34)` |
| `1hdpu9s->0e7qvj1` | 33 | `zentrum_stabil->offene_variante` | 0.424 | `oeffnend_belastend` | +0.0623 | -0.0410 | +0.1628 | `DOGE_2025_1H_YEAR (17/33)` |
| `0qzjuvj->0z748ck` | 22 | `zentrum_stabil->zentrum_stabil` | 0.773 | `oeffnend_belastend` | +0.0152 | -0.0095 | +0.0409 | `DOGE_2024_1H_YEAR (11/22)` |
| `0z748ck->0e7qvj1` | 21 | `zentrum_stabil->zentrum_stabil` | 0.857 | `bewegung_offen` | -0.0086 | +0.0014 | -0.0354 | `DOGE_2025_1H_YEAR (11/21)` |
| `0mji3u6->0e7qvj1` | 17 | `zentrum_stabil->zentrum_stabil` | 0.529 | `rekoppelnd_entlastend` | -0.0092 | +0.0080 | +0.0153 | `DOGE_2025_1H_YEAR (10/17)` |
| `0jbl5pq->0qzjuvj` | 15 | `zentrum_stabil->zentrum_stabil` | 0.800 | `rekoppelnd_entlastend` | -0.0191 | +0.0062 | -0.0666 | `DOGE_2024_1H_YEAR (9/15)` |
| `0e7qvj1->0mji3u6` | 11 | `offene_variante->offene_variante` | 0.727 | `bewegung_offen` | -0.0119 | -0.0004 | -0.0741 | `DOGE_2025_1H_YEAR (8/11)` |
| `1rxdw4p->1hs3jsa` | 10 | `zentrum_stabil->zentrum_stabil` | 1.000 | `rekoppelnd_entlastend` | -0.0107 | +0.0078 | -0.0368 | `DOGE_2024_1H_YEAR (10/10)` |
| `0l3i7ey->0aztxel` | 9 | `zentrum_stabil->zentrum_stabil` | 0.333 | `oeffnend_belastend` | +0.0187 | -0.0164 | +0.0521 | `DOGE_2025_1H_YEAR (7/9)` |
| `0lne9ax->0jbl5pq` | 9 | `zentrum_stabil->zentrum_stabil` | 0.778 | `spannungsnah` | +0.0001 | +0.0024 | +0.0160 | `DOGE_2024_1H_YEAR (7/9)` |
| `18l3thm->0e7qvj1` | 9 | `zentrum_stabil->zentrum_stabil` | 0.444 | `oeffnend_belastend` | +0.0505 | -0.0307 | +0.1604 | `DOGE_2024_1H_YEAR (8/9)` |
| `1q3us3f->1hdpu9s` | 9 | `zentrum_stabil->offene_variante` | 0.778 | `oeffnend_belastend` | +0.0856 | -0.0635 | +0.2239 | `DOGE_2025_1H_YEAR (7/9)` |
| `0e7qvj1->18l3thm` | 8 | `zentrum_stabil->zentrum_stabil` | 0.875 | `rekoppelnd_entlastend` | -0.0215 | +0.0110 | -0.0597 | `DOGE_2024_1H_YEAR (8/8)` |
| `1hdpu9s->1q3us3f` | 8 | `zentrum_stabil->zentrum_stabil` | 0.875 | `rekoppelnd_entlastend` | -0.0144 | +0.0086 | -0.0301 | `DOGE_2025_1H_YEAR (5/8)` |
| `0aztxel->0hjnwsk` | 7 | `zentrum_stabil->offene_variante` | 0.429 | `oeffnend_belastend` | +0.0376 | -0.0339 | +0.0940 | `DOGE_2025_1H_YEAR (5/7)` |

## Arbeitsbefund

DOGE 1h bleibt zentriert, verschiebt aber die DOGE-F?rbung leicht in mehr offene Variante und etwas mehr Randn?he.

- `0e7qvj1 -> 1hdpu9s` bleibt rekoppelnd/entlastend.
- `1hdpu9s -> 0e7qvj1` bleibt ?ffnend/belastend.
- 2025 ist etwas offener und randn?her als 2024.
- Ein Randkollaps entsteht nicht.
- Die Rezeptorschicht bleibt auch in DOGE 1h tragf?hig, zeigt aber st?rkere Anpassungsanforderung als bei PAXG.

## Grenze

DOGE 1h wurde als Spot-Jahreswelt 2024/2025 gepr?ft. Der Befund sagt noch nichts ?ber Extremfenster oder nicht-marktbasierte Rauschwelten.

## Wie es weitergeht

Als n?chstes wird DOGE 5m gegen DOGE 1h synthetisiert. Ziel ist zu kl?ren, ob Zeitaufl?sung bei DOGE nur F?rbung erzeugt oder eine neue Anpassungsqualit?t andeutet.
