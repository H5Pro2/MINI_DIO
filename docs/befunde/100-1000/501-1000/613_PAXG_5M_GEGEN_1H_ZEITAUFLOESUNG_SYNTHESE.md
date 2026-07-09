# PAXG 5m gegen 1h: Zeitaufl?sungs-Synthese

Stand: 2026-06-22

## Zweck

Diese Synthese vergleicht PAXG/USDT als goldnahe Assetwelt auf zwei Zeitaufl?sungen:

- PAXG 5m 10k,
- PAXG 1h Jahreswelt.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Bricht eine andere Zeitaufl?sung die PAXG-MCM-Topologie?
2. Unterpr?fung: Bleibt die Kernachse `0e7qvj1 <-> 1hdpu9s` erhalten?
3. Unterpr?fung: Ver?ndert sich die Rollenf?rbung zwischen 5m und 1h?
4. Folgeschritt: Weitere Assetwelten oder bewusst andere Nicht-Markt-Welten pr?fen.

## Laufvergleich

| Welt | Rekopplung | Carry | Sinnes-MCM-Kopplung | Stabil | Tragend unruhig | Kippend | Gespannt | Field Strained |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG2024 5m 10k | 0.7135 | 0.5386 | 0.8545 | 8792 | 1141 | 54 | 7 | 7 |
| PAXG2025 5m 10k | 0.7140 | 0.5414 | 0.8557 | 8719 | 1203 | 62 | 10 | 10 |
| PAXG2024 1h Jahr | 0.7032 | 0.5310 | 0.8434 | 7194 | 1484 | 82 | 18 | 18 |
| PAXG2025 1h Jahr | 0.7045 | 0.5344 | 0.8458 | 7297 | 1378 | 66 | 13 | 13 |

## Rollenvergleich

| Rollenbewegung | PAXG 5m | PAXG 1h | Lesart |
|---|---:|---:|---|
| `zentrum_stabil->zentrum_stabil` | 93 | 78 | bleibt dominant, aber 1h ist weniger rein zentriert |
| `zentrum_stabil->offene_variante` | 24 | 21 | bleibt zweite Hauptbewegung |
| `offene_variante->zentrum_stabil` | 15 | 17 | R?ckbindung aus offener Variante bleibt sichtbar |
| `zentrum_stabil->spannungsrand_kippnaehe` | 10 | 13 | 1h tr?gt etwas mehr Rand-/Kippn?he |
| `offene_variante->offene_variante` | 9 | 8 | offene Selbstn?he bleibt klein, aber vorhanden |

## Bewegungswirkung

| Wirkung | PAXG 5m | PAXG 1h | Lesart |
|---|---:|---:|---|
| `rekoppelnd_entlastend` | 76 | 69 | Rekopplung bleibt stark, f?llt 1h etwas niedriger aus |
| `oeffnend_belastend` | 64 | 54 | ?ffnung bleibt, aber 1h verteilt mehr in offene Bewegung |
| `bewegung_offen` | 12 | 26 | 1h erzeugt mehr nicht eindeutig abgeschlossene Bewegung |
| `spannungsnah` | 8 | 11 | 1h bringt etwas mehr Spannungsn?he |

## Kernachse

```text
0e7qvj1 -> 1hdpu9s
  bleibt rekoppelnd / entlastend

1hdpu9s -> 0e7qvj1
  bleibt ?ffnend / belastend
```

PAXG 5m:

- `0e7qvj1 -> 1hdpu9s`: 43 Ereignisse, rekoppelnd/entlastend.
- `1hdpu9s -> 0e7qvj1`: 35 Ereignisse, ?ffnend/belastend.

PAXG 1h:

- `0e7qvj1 -> 1hdpu9s`: 54 Ereignisse, rekoppelnd/entlastend.
- `1hdpu9s -> 0e7qvj1`: 57 Ereignisse, ?ffnend/belastend.

Die gr?bere Zeitaufl?sung schw?cht die Achse also nicht. Sie macht sie sogar ereignisdichter, aber auch spannungsreicher.

## Arbeitsbefund

PAXG 1h bricht die PAXG-5m-Topologie nicht.

Der Unterschied liegt in der F?rbung:

- 5m wirkt ruhiger, zentrumsn?her und sensorisch st?rker rekoppelt.
- 1h bleibt stabil, tr?gt aber mehr offene Bewegung, mehr Randn?he und etwas niedrigere Rekopplung.
- Die Kernasymmetrie bleibt in beiden Aufl?sungen erhalten.
- Zeitaufl?sung wirkt damit bisher wie eine Feldf?rbung, nicht wie ein Topologiebruch.

## Bedeutung f?r MINI_DIO

Der Befund st?rkt die bisherige Lesart:

```text
MINI_DIO bildet keinen starren Symbolnamen ab.
Es bildet Rollenbewegungen im MCM-Feld.
Diese Rollenbewegungen k?nnen je Welt und Zeitaufl?sung anders gef?rbt werden.
```

Das ist wichtig, weil PAXG eine andersartige Assetwelt darstellt und 1h eine andere zeitliche Spannung tr?gt. Wenn beide die Kernachse erhalten, spricht das f?r eine robuste passive Feldbewegungsordnung innerhalb der bisherigen Testgrenzen.

## Grenze

Der Befund ist stark, aber begrenzt:

- PAXG wurde als Spotwelt gepr?ft.
- 5m umfasst 10k-Segmente, 1h umfasst Jahreswelten.
- Die Topologie ist nicht universell bewiesen.
- Die Rollenbegriffe sind Diagnosebegriffe, keine Runtime-Vorgaben.

## Wie es weitergeht

Als n?chstes ist ein st?rker andersartiger Gegenfall sinnvoll: DOGE als rauschendere Assetwelt, XRP als impulsivere Welt oder eine nicht-marktbasierte Kontrollwelt. Ziel ist zu pr?fen, ob die Kernachse auch bei anderer Weltqualit?t bestehen bleibt oder ob neue Rollenr?ume entstehen.
