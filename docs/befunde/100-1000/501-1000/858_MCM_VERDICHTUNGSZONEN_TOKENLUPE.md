# MCM-Verdichtungszonen Tokenlupe

## Zweck

Diese Lupe liest die staerksten Zonenwechsel aus `857_MCM_VERDICHTUNGSZONEN_DRIFTLUPE`.
Ziel ist zu unterscheiden, ob ein Zonenwechsel eher aus Weltgruppe, Sinnesaufnahme, Rekopplung oder echter MCM-Drift entsteht.

## Gepruefte Tokens

| Token | Bewegung | Basiszone | Folgezone |
|---|---|---|---|
| `dio_mcm_episode_0v5p8er` | Oeffnung/Drift | hoeherer Clusteruebergang | Driftzone |
| `dio_mcm_episode_14l8khu` | Oeffnung/Drift | hoeherer Clusteruebergang | Driftzone |
| `dio_mcm_episode_1xx3u1e` | Reifung/Verdichtung | hoeherer Clusteruebergang | stabile Bedeutungsinsel |
| `dio_mcm_episode_1q3us3f` | Reifung/Verdichtung | stabile Bedeutungsinsel | Rekopplungszone |

## Weltbindung

### `0v5p8er`

Basis:

```text
DOGE_2025_5M, SYNTH_BRUCH_RAND, SYNTH_RAND, XRP_2025_5M
```

Folge:

```text
SYNTH_BRUCH_RAND, SYNTH_RAND
```

Befund:

`0v5p8er` verliert in der Folgewelt reale Asset-Breite und bleibt vor allem synthetisch/randnah gebunden.
Gleichzeitig kippt die dominante Rolle von `zentrum_stabil` zu `offene_variante`.

Wichtige Achsen:

```text
Rekopplung: -0.0274
Strain:     +0.0187
Lautheit:   +0.0369
Unschaerfe: +0.1194
```

Lesart:

Das sieht nach Weltfaerbung plus echter Oeffnung aus. Die Zone driftet nicht willkuerlich, sondern wenn die reale Breite abnimmt und die Sinnesaufnahme lauter/unschaerfer wird.

### `14l8khu`

Basis:

```text
DOGE_2025_5M, SYNTH_RAND, XRP_2025_5M
```

Folge:

```text
SYNTH_RAND
```

Befund:

`14l8khu` wird in der Folgewelt fast vollstaendig auf `SYNTH_RAND` reduziert.
Auch hier kippt die dominante Rolle von `zentrum_stabil` zu `offene_variante`.

Wichtige Achsen:

```text
Rekopplung: -0.0319
Strain:     +0.0250
Lautheit:   +0.0480
Unschaerfe: +0.1134
```

Lesart:

Das ist der klarste Driftfall: weniger Weltbreite, mehr Lautheit, mehr Unschaerfe, weniger Rekopplung.
Die Drift ist damit an eine veraenderte Rezeptor- und Weltlage gekoppelt.

### `1xx3u1e`

Basis:

```text
PAXG_2025_5M, XRP_2025_5M
```

Folge:

```text
DOGE_2024_5M, PAXG_2024_5M, XRP_2024_5M
```

Befund:

`1xx3u1e` bleibt zentrumsnah und gewinnt Weltbreite.
Die Zone verschiebt sich vom hoeheren Clusteruebergang zur stabilen Bedeutungsinsel.

Wichtige Achsen:

```text
Rekopplung: -0.0003
Strain:     +0.0024
Lautheit:   +0.0202
Unschaerfe: +0.0054
```

Lesart:

Das wirkt nicht wie ein Belastungskipp, sondern wie eine stabilere, weniger verzweigte Oberflaeche.
Der Token wird nicht schwach, sondern eindeutiger.

### `1q3us3f`

Basis:

```text
DOGE_2025_5M, SYNTH_RAND, XRP_2025_5M
```

Folge:

```text
DOGE_2024_5M, SYNTH_RAND, XRP_2024_5M
```

Befund:

`1q3us3f` behaelt Weltbreite und bleibt zentrumsnah.
Die Zone verschiebt sich von stabiler Bedeutungsinsel zu Rekopplungszone.

Wichtige Achsen:

```text
Rekopplung: +0.0064
Strain:     -0.0067
Lautheit:   -0.0298
Unschaerfe: -0.0612
```

Lesart:

Das ist ein Gegenpol zu `0v5p8er` und `14l8khu`.
Hier wird die Aufnahme leiser, schaerfer und rekoppelnder.
Der Zonenwechsel ist deshalb eher eine Rueckbindung als eine Drift.

## Gesamtbefund

Die staerksten Zonenwechsel teilen sich in zwei Muster:

1. **Oeffnung/Drift**
   - reale Weltbreite nimmt ab,
   - synthetische Randbindung nimmt zu,
   - Lautheit und visuelle Unschaerfe steigen,
   - Rekopplung faellt,
   - dominante Rolle kippt Richtung `offene_variante`.

2. **Reifung/Rekopplung**
   - Weltbreite bleibt gleich oder nimmt zu,
   - Zentrum bleibt dominant,
   - Lautheit/Unschaerfe bleiben stabil oder sinken,
   - Rekopplung steigt oder bleibt stabil,
   - der Token wird eindeutiger oder rueckbindender.

Damit wirkt der Zonenwechsel nicht wie zufaellige Tokenoberflaeche.
Er folgt einer lesbaren MCM-Feldbewegung: Weltbreite, Rezeptorlage und Rekopplungsqualitaet bestimmen, ob ein Zeichen driftet, reift oder rekoppelt.

## Bedeutung Fuer MINI_DIO

MINI_DIO bildet nicht nur wiederkehrende Tokens.
Es entstehen Bewegungsqualitaeten zwischen Bedeutungszonen:

```text
zentrumsnah -> offen/driftend
zentrumsnah -> stabiler
stabil -> rekoppelnd
```

Das stuetzt die aktuelle Arbeitsthese:

```text
MCM-Bedeutung ist nicht nur ein Punkt.
MCM-Bedeutung ist auch eine Bewegung im Feld.
```

## Wie es weitergeht

Als naechstes sollte eine Rohwelt-Segmentlupe fuer genau diese vier Tokens entstehen.
Dabei wird je Token geprueft, welche konkreten Weltphasen vor, waehrend und nach dem Tokenkontakt auftreten.
Ziel: unterscheiden, ob die Feldbewegung aus Sequenzbruch, Randspannung, Assetprofil oder Rezeptoraufnahme entsteht.
