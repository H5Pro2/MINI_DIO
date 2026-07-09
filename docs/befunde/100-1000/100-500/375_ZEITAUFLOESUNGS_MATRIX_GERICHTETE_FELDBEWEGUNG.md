# Zeitaufloesungs-Matrix gerichtete Feldbewegung

Stand: 2026-06-20

## Zweck

Diese Diagnose fasst die 2025er SOL/BTC-Pruefungen ueber drei Zeitaufloesungen zusammen:

- 1h
- 15m
- 5m

Sie prueft, ob die bisher beobachtete gerichtete Asymmetrie nur eine einzelne Zeitaufloesung betrifft oder ob sie ueber verschiedene Aufloesungen hinweg lesbar bleibt.

Die Diagnose bleibt passiv:

```text
keine Handlung
kein Gate
keine Strategie
keine Runtime-Regel
```

## Hierarchie

1. Grundfrage: Bleibt eine gerichtete passive Feldbewegung ueber mehrere Zeitaufloesungen erkennbar?
2. Unterpruefung: `1t5bcxp -> 183drjy` und `183drjy -> 1t5bcxp` in 1h, 15m und 5m vergleichen.
3. Folgeschritt: pruefen, ob die stabile Richtung aus Rohweltmerkmalen, Rezeptorkontakt oder MCM-Feldlage besser erklaert werden kann.

## Matrix

| Aufloesung | Paar | Events | Top-Qualitaet | Anteil | Top-Signatur | Signaturanteil | Driftlabel |
|---|---|---:|---|---:|---|---:|---|
| 1h | `1t5bcxp -> 183drjy` | 103 | `eng_getragen` | 0.5534 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.5534 | `wiederkehrend_variabel` |
| 1h | `183drjy -> 1t5bcxp` | 97 | `fragmentiert` | 0.6392 | `rekoppelnde_lage -> bewegungsbruch -> rekoppelnde_lage` | 0.1340 | `lokal_offen` |
| 15m | `1t5bcxp -> 183drjy` | 91 | `eng_getragen` | 0.6374 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.6374 | `wiederkehrend_stabil` |
| 15m | `183drjy -> 1t5bcxp` | 80 | `fragmentiert` | 0.4750 | `rekoppelnde_lage -> offene_lage -> rekoppelnde_lage` | 0.1500 | `lokal_offen` |
| 5m | `1t5bcxp -> 183drjy` | 79 | `eng_getragen` | 0.6076 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.6076 | `wiederkehrend_stabil` |
| 5m | `183drjy -> 1t5bcxp` | 69 | `fragmentiert` | 0.5362 | `rekoppelnde_lage -> druck_lage -> bewegungsbruch` | 0.1304 | `lokal_offen` |

## Befund

Die Richtung bleibt ueber alle drei Aufloesungen erhalten.

`1t5bcxp -> 183drjy` wird in 1h, 15m und 5m dominant `eng_getragen` gelesen.
Die wiederkehrende Signatur bleibt in allen drei Faellen:

```text
rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage
```

Der Rueckweg `183drjy -> 1t5bcxp` wird in allen drei Aufloesungen dominant `fragmentiert` gelesen.
Seine Top-Signatur bleibt niedrig und offen:

```text
1h:  rekoppelnde_lage -> bewegungsbruch -> rekoppelnde_lage
15m: rekoppelnde_lage -> offene_lage -> rekoppelnde_lage
5m:  rekoppelnde_lage -> druck_lage -> bewegungsbruch
```

Damit ist die Asymmetrie nicht nur eine 1h-Erscheinung und nicht nur ein Effekt einer groben Weltaufloesung.
Sie bleibt auch unter feinerer Mikrostruktur sichtbar.

## Fachliche Lesart

MINI_DIO scheint hier keine starre Bedeutung eines Symbols zu speichern.
Stabil ist vielmehr die passive Tragart einer gerichteten Feldbewegung:

```text
Hinweg:  rekoppelnd getragen
Rueckweg: offener, bruechiger, fragmentierter
```

Das ist wichtig fuer die MCM-Lesart:

```text
Die Bedeutung liegt nicht im Einzelzeichen.
Die Bedeutung liegt in Feldlage, Richtung, Wiederkehr und Tragart.
```

## Grenze

Dieser Befund ist kein Beweis fuer eine universelle MCM-Gesetzmaessigkeit.
Er ist aber ein reproduzierbarer Befund innerhalb der geprueften SOL/BTC-2025-Welten und ihrer Zeitaufloesungen.

## Wie es weitergeht

Als naechstes sollte die stabile Richtung auf andere Weltarten gelegt werden:

1. andere Assets,
2. andere Jahre,
3. gezielt gegenteilige Regime,
4. danach erst eine Rueckfuehrung auf Weltmerkmale und Rezeptorkontakt.

Ziel ist zu klaeren, ob die Asymmetrie eine allgemeine passive Feldbewegung ist oder eine Eigenschaft dieser konkreten SOL/BTC-2025-Welten.
