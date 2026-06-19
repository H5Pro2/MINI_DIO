# Befund: Anpassungsfaehigkeit ueber Asset und Zeitebene

Stand: 2026-06-19

## Zweck

Nach der exakten Reproduzierbarkeit gleicher 10k-Welten wurde eine andere Frage geprueft:

```text
Bleibt die passive Rollenordnung sichtbar,
wenn Asset und Zeitebene gewechselt werden?
```

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Testaufbau

Geprueft wurden vier frische `world_relative`-Laeufe mit jeweils 2000 Kerzen:

| Welt | Asset | Zeitebene | Episoden |
|---|---|---|---:|
| BTC_2024_1H_2K | BTCUSDT | 1h | 1994 |
| BTC_2025_1H_2K | BTCUSDT | 1h | 1994 |
| SOL_2024_1H_2K | SOLUSDT | 1h | 1994 |
| SOL_2025_1H_2K | SOLUSDT | 1h | 1994 |

Die Matrix liegt in:

```text
docs/befunde/277_ASSET_ZEITEBENE_ANPASSUNGS_TOPOLOGIE_MATRIX.md
```

## Kurzbefund

Alle vier Welten bilden denselben Topologiezustand:

```text
zentrum_mit_rand_und_uebergang
```

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| BTC_2024_1H_2K | 0.8119 | 0.1389 | 0.0491 | 0.6484 | 0.3981 | 0.1797 | 0.8657 |
| BTC_2025_1H_2K | 0.8385 | 0.1133 | 0.0481 | 0.6498 | 0.4004 | 0.1784 | 0.8666 |
| SOL_2024_1H_2K | 0.8059 | 0.1515 | 0.0426 | 0.6451 | 0.3952 | 0.1857 | 0.8636 |
| SOL_2025_1H_2K | 0.8064 | 0.1434 | 0.0502 | 0.6467 | 0.3976 | 0.1842 | 0.8647 |

## Interpretation

Die Topologieklasse bleibt erhalten, aber die Innenfeldanteile verschieben sich.

Lesart:

- BTC 2025 wirkt im aktuellen Fenster zentrumsnaeher.
- SOL 2024 und SOL 2025 tragen mehr offene Variante.
- Rand/Kipp bleibt in allen vier Welten klein, aber sichtbar.
- Sinnes-MCM-Kopplung bleibt eng beisammen.

Damit spricht der aktuelle Befund fuer Anpassungsfaehigkeit ohne Topologiekollaps:

```text
andere Welt -> gleiche Rollenordnung,
aber andere Gewichtsverteilung.
```

## Bedeutung fuer MINI_DIO

MINI_DIO scheint unter `world_relative` nicht nur dieselbe Welt exakt reproduzieren zu koennen.
Es kann auch andere Asset-/Zeitebenen-Fenster in dieselbe passive Rollenstruktur einordnen.

Das ist wichtig, weil es zwei Ebenen trennt:

1. Reproduzierbarkeit:
   gleiche Welt erzeugt dieselbe Matrix.
2. Anpassungsfaehigkeit:
   andere Welt erzeugt keine beliebige neue Ordnung, sondern verschiebt Rollenanteile.

## Forschungsgrenze

Dieser Befund beweist keine universelle MCM-Topologie.

Noch offen:

- Wiederholung dieser vier Welten mit frischem Memory,
- laengere 1h-Welten,
- 15m/30m-Zwischenebenen,
- extremere Bruchfenster,
- Vergleich gegen feste Aufnahme.

## Wie es weitergeht

Als naechstes sollte die Anpassungsfaehigkeit nicht breiter, sondern tiefer geprueft werden:

1. dieselben vier 1h-Welten reproduzieren,
2. Delta gegen `277` berechnen,
3. nur wenn diese stabil bleiben, auf 15m/30m-Zwischenebenen gehen.

Damit bleibt die Pruefhierarchie sauber:

```text
erst Reproduzierbarkeit,
dann Zeitebenenstaffelung,
dann neue Weltklassen.
```
