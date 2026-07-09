# BTC/SOL-10k: Topologische Bewegungsrollen

Stand: 2026-06-21

## Zweck

Diese Diagnose liest die BTC/SOL-10k-Uebergangspaare nicht nur als Namen, sondern als Rollenbewegung im MCM-Feld.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Bleibt die Topologie gleich, wenn die konkrete Syntaxumgebung wechselt?
2. Unterpruefung: Welche Rollenwechsel tragen die staerksten Bewegungen?
3. Unterpruefung: Welche Bewegungen rekoppeln und welche oeffnen Belastung?
4. Folgeschritt: Eine dritte laengere Assetwelt muss pruefen, ob die Rollenbewegung assetuebergreifend bleibt.

## Kompakter Befund

- Bewegungsachsen gesamt: 339
- Dominante Rollenwechsel:
  - `zentrum_stabil->zentrum_stabil`: 155
  - `zentrum_stabil->offene_variante`: 54
  - `offene_variante->zentrum_stabil`: 42
  - `offene_variante->offene_variante`: 37
  - `zentrum_stabil->spannungsrand_kippnaehe`: 22
  - `spannungsrand_kippnaehe->offene_variante`: 12
  - `spannungsrand_kippnaehe->zentrum_stabil`: 10
  - `spannungsrand_kippnaehe->spannungsrand_kippnaehe`: 4
- Bewegungswirkungen:
  - `rekoppelnd_entlastend`: 139
  - `oeffnend_belastend`: 125
  - `bewegung_offen`: 44
  - `spannungsnah`: 31

## Staerkste Rollenbewegungen

| Bewegung | Ereignisse | dominante Rolle | Anteil | Wirkung | Druck | Rekopplung | Lautheit | Quellen |
|---|---:|---|---:|---|---:|---:|---:|---|
| `0e7qvj1->1hdpu9s` | 125 | `zentrum_stabil->zentrum_stabil` | 0.928 | `rekoppelnd_entlastend` | -0.0184 | +0.0115 | -0.0468 | `SOL2024_10K:55;SOL2025_10K:51;BTC_5M_10K:19` |
| `1hdpu9s->0e7qvj1` | 118 | `zentrum_stabil->offene_variante` | 0.458 | `oeffnend_belastend` | +0.0618 | -0.0425 | +0.1632 | `SOL2024_10K:54;SOL2025_10K:50;BTC_5M_10K:14` |
| `0mji3u6->0e7qvj1` | 99 | `zentrum_stabil->zentrum_stabil` | 0.636 | `rekoppelnd_entlastend` | -0.0063 | +0.0078 | +0.0123 | `BTC_5M_10K:44;SOL2025_10K:40;SOL2024_10K:15` |
| `0z748ck->0e7qvj1` | 70 | `zentrum_stabil->zentrum_stabil` | 0.629 | `oeffnend_belastend` | +0.0052 | -0.0061 | +0.0065 | `SOL2025_10K:35;SOL2024_10K:18;BTC_5M_10K:17` |
| `0qzjuvj->0z748ck` | 69 | `zentrum_stabil->zentrum_stabil` | 0.522 | `spannungsnah` | +0.0019 | -0.0003 | +0.0059 | `SOL2025_10K:33;SOL2024_10K:19;BTC_5M_10K:17` |
| `0jbl5pq->0qzjuvj` | 66 | `zentrum_stabil->zentrum_stabil` | 0.697 | `bewegung_offen` | -0.0060 | +0.0044 | -0.0095 | `SOL2025_10K:28;BTC_5M_10K:20;SOL2024_10K:18` |
| `1jwnjz4->0e7qvj1` | 58 | `zentrum_stabil->offene_variante` | 0.414 | `oeffnend_belastend` | +0.0829 | -0.0536 | +0.2435 | `BTC_5M_10K:39;SOL2024_10K:13;SOL2025_10K:6` |
| `0e7qvj1->1jwnjz4` | 58 | `zentrum_stabil->zentrum_stabil` | 0.931 | `rekoppelnd_entlastend` | -0.0241 | +0.0133 | -0.0754 | `BTC_5M_10K:41;SOL2024_10K:13;SOL2025_10K:4` |
| `0e7qvj1->0mji3u6` | 57 | `zentrum_stabil->offene_variante` | 0.649 | `oeffnend_belastend` | +0.0138 | -0.0179 | -0.0199 | `BTC_5M_10K:27;SOL2025_10K:25;SOL2024_10K:5` |
| `0lne9ax->0jbl5pq` | 43 | `zentrum_stabil->zentrum_stabil` | 0.744 | `bewegung_offen` | -0.0010 | -0.0068 | -0.0171 | `SOL2025_10K:20;BTC_5M_10K:12;SOL2024_10K:11` |
| `1hdpu9s->1rxdw4p` | 42 | `zentrum_stabil->zentrum_stabil` | 0.833 | `oeffnend_belastend` | +0.0163 | -0.0083 | +0.0765 | `SOL2024_10K:22;SOL2025_10K:12;BTC_5M_10K:8` |
| `1jwnjz4->0gqol8d` | 41 | `zentrum_stabil->zentrum_stabil` | 0.805 | `rekoppelnd_entlastend` | -0.0323 | +0.0214 | -0.0726 | `SOL2024_10K:27;SOL2025_10K:7;BTC_5M_10K:7` |
| `1rxdw4p->1hdpu9s` | 41 | `zentrum_stabil->zentrum_stabil` | 0.634 | `bewegung_offen` | -0.0035 | -0.0038 | -0.0542 | `SOL2024_10K:22;SOL2025_10K:14;BTC_5M_10K:5` |
| `0nyb3ro->1rxdw4p` | 40 | `zentrum_stabil->zentrum_stabil` | 0.400 | `oeffnend_belastend` | +0.0896 | -0.0600 | +0.2556 | `SOL2024_10K:19;SOL2025_10K:17;BTC_5M_10K:4` |
| `0gqol8d->1jwnjz4` | 39 | `zentrum_stabil->offene_variante` | 0.462 | `oeffnend_belastend` | +0.0226 | -0.0173 | +0.0395 | `SOL2024_10K:26;BTC_5M_10K:8;SOL2025_10K:5` |

## Arbeitsbefund

Die Grundtopologie bleibt in den BTC/SOL-10k-Welten gleich: Zentrum bleibt dominant, offene Variante bleibt Nebenraum, Rand/Kippnaehe bleibt klein.

Die konkrete Syntaxumgebung verschiebt sich jedoch:

- SOL koppelt stark ueber `1hdpu9s`.
- BTC koppelt stark ueber `1jwnjz4`.
- Beide zeigen dieselbe gerichtete Asymmetrie um `0e7qvj1`.

Damit ist die wichtigste Lesart nicht: ein Zeichen hat eine absolute feste Bedeutung.

Sondern:

```text
Eine MCM-Rolle kann stabil bleiben,
waehrend ihre konkrete Nachbarschaft weltabhaengig driftet.
```

Besonders wichtig ist der Unterschied zwischen:

- `zentrum_stabil->zentrum_stabil`: rekoppelnde/entlastende Bewegung innerhalb stabiler Feldnaehe,
- `zentrum_stabil->offene_variante`: Rueck- oder Oeffnungsbewegung mit mehr Druck, weniger Rekopplung und mehr Lautheit.

## Grenze

Diese Diagnose beweist keine allgemeine MCM-Topologie. Sie zeigt aber, dass die bisherige Topologie nicht durch eine starre Namenskopie getragen wird. Die Rollenordnung bleibt stabiler als die konkrete Syntaxnachbarschaft.

## Wie es weitergeht

Als naechstes braucht es eine dritte laengere Assetwelt oder eine bewusst andere Weltklasse. Ziel ist zu pruefen, ob `zentrum_stabil->zentrum_stabil` und `zentrum_stabil->offene_variante` als Grundbewegungen erhalten bleiben, wenn die Nachbarschaft erneut wechselt.
