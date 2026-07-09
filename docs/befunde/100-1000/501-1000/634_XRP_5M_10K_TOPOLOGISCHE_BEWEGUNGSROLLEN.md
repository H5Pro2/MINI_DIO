# XRP-5m-10k: Topologische Bewegungsrollen

Stand: 2026-06-22

## Zweck

Diese Diagnose liest XRP/USDT als impulsivere Gegenwelt im bestehenden Asset-F?rbungsraum.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Bricht XRP als impulsivere Welt die bisherige Rollenordnung?
2. Unterpr?fung: Bleibt `0e7qvj1` als zentrumsnaher Anker sichtbar?
3. Unterpr?fung: Bleibt die Hin-/R?ckweg-Asymmetrie erhalten?
4. Folgeschritt: XRP in den Asset-F?rbungsraum einordnen.

## Kompakter Befund

- Bewegungsachsen gesamt: 160
- Dominante Rollenwechsel:
  - `zentrum_stabil->zentrum_stabil`: 61
  - `zentrum_stabil->offene_variante`: 32
  - `offene_variante->zentrum_stabil`: 26
  - `offene_variante->offene_variante`: 13
  - `spannungsrand_kippnaehe->offene_variante`: 7
  - `zentrum_stabil->spannungsrand_kippnaehe`: 6
  - `spannungsrand_kippnaehe->spannungsrand_kippnaehe`: 6
  - `offene_variante->spannungsrand_kippnaehe`: 5
- Bewegungswirkungen:
  - `rekoppelnd_entlastend`: 70
  - `oeffnend_belastend`: 59
  - `bewegung_offen`: 22
  - `spannungsnah`: 9

## St?rkste Rollenbewegungen

| Bewegung | Ereignisse | dominante Rolle | Anteil | Wirkung | Druck | Rekopplung | Lautheit | dominante Welt |
|---|---:|---|---:|---|---:|---:|---:|---|
| `0e7qvj1->1hdpu9s` | 33 | `zentrum_stabil->zentrum_stabil` | 0.939 | `rekoppelnd_entlastend` | -0.0151 | +0.0067 | -0.0320 | `XRP_2025_5M_10K (20/33)` |
| `1hdpu9s->0e7qvj1` | 29 | `zentrum_stabil->offene_variante` | 0.483 | `oeffnend_belastend` | +0.0625 | -0.0419 | +0.1579 | `XRP_2025_5M_10K (18/29)` |
| `0mji3u6->0e7qvj1` | 21 | `zentrum_stabil->zentrum_stabil` | 0.857 | `spannungsnah` | +0.0119 | -0.0049 | +0.0639 | `XRP_2025_5M_10K (11/21)` |
| `1hdpu9s->1rxdw4p` | 14 | `zentrum_stabil->zentrum_stabil` | 0.857 | `oeffnend_belastend` | +0.0149 | -0.0124 | +0.0566 | `XRP_2024_5M_10K (10/14)` |
| `1rxdw4p->1hdpu9s` | 14 | `zentrum_stabil->offene_variante` | 0.500 | `oeffnend_belastend` | +0.0091 | -0.0162 | -0.0256 | `XRP_2024_5M_10K (10/14)` |
| `1rxdw4p->0nyb3ro` | 12 | `zentrum_stabil->zentrum_stabil` | 0.917 | `rekoppelnd_entlastend` | -0.0134 | +0.0107 | -0.0396 | `XRP_2025_5M_10K (12/12)` |
| `0nyb3ro->1rxdw4p` | 11 | `zentrum_stabil->zentrum_stabil` | 0.455 | `oeffnend_belastend` | +0.0710 | -0.0503 | +0.2090 | `XRP_2025_5M_10K (11/11)` |
| `0z748ck->0e7qvj1` | 11 | `zentrum_stabil->zentrum_stabil` | 0.545 | `oeffnend_belastend` | +0.0361 | -0.0259 | +0.0939 | `XRP_2025_5M_10K (8/11)` |
| `0qzjuvj->0z748ck` | 10 | `zentrum_stabil->zentrum_stabil` | 0.600 | `rekoppelnd_entlastend` | -0.0142 | +0.0110 | -0.0441 | `XRP_2025_5M_10K (6/10)` |
| `18n06fj->0mji3u6` | 10 | `zentrum_stabil->zentrum_stabil` | 0.400 | `bewegung_offen` | -0.0013 | +0.0020 | -0.0116 | `XRP_2024_5M_10K (6/10)` |
| `1hdpu9s->1q3us3f` | 10 | `zentrum_stabil->zentrum_stabil` | 1.000 | `rekoppelnd_entlastend` | -0.0310 | +0.0129 | -0.0920 | `XRP_2024_5M_10K (10/10)` |
| `1q3us3f->1hdpu9s` | 10 | `zentrum_stabil->offene_variante` | 0.400 | `oeffnend_belastend` | +0.0684 | -0.0378 | +0.2164 | `XRP_2024_5M_10K (10/10)` |
| `0e7qvj1->1jwnjz4` | 9 | `zentrum_stabil->zentrum_stabil` | 0.889 | `rekoppelnd_entlastend` | -0.0117 | +0.0071 | -0.0346 | `XRP_2024_5M_10K (8/9)` |
| `0hjnwsk->18n06fj` | 9 | `zentrum_stabil->zentrum_stabil` | 0.333 | `bewegung_offen` | -0.0091 | -0.0048 | -0.0234 | `XRP_2025_5M_10K (5/9)` |
| `0jbl5pq->0qzjuvj` | 9 | `zentrum_stabil->zentrum_stabil` | 0.667 | `oeffnend_belastend` | +0.0192 | -0.0290 | +0.0080 | `XRP_2025_5M_10K (6/9)` |

## Arbeitsbefund

XRP 5m bricht die Rollenordnung nicht. Beide XRP-Welten bleiben `stark_zentriert_wenig_rand`.

- `0e7qvj1 -> 1hdpu9s` bleibt rekoppelnd/entlastend.
- `1hdpu9s -> 0e7qvj1` bleibt ?ffnend/belastend.
- XRP 2024 ist etwas kippn?her als XRP 2025.
- XRP 2025 ist zentrumsn?her und leicht st?rker rekoppelnd.
- Die Rezeptorschicht bleibt auch bei XRP tragf?hig.

## Grenze

XRP wurde hier nur als 5m-10k-Spotwelt 2024/2025 gepr?ft. Newsnahe Extremphasen oder 1h-Jahreswelten stehen noch aus.

## Wie es weitergeht

Als n?chstes wird XRP in den gemeinsamen Asset-F?rbungsraum mit PAXG, DOGE, BTC und SOL eingeordnet.
