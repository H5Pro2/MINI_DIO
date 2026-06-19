# Befund: Reproduktion ueber Asset und 1h-Zeitebene

Stand: 2026-06-19

## Zweck

Diese Datei haelt die Reproduktion der Asset-/Zeitebenen-Pruefung aus Befund `278` fest.

Geprueft wurde:

```text
Gleiche 1h-Welten + frisches Memory -> gleiche passive Rollenmatrix?
```

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Testaufbau

Reproduziert wurden:

| Welt | Asset | Zeitebene | Kerzen |
|---|---|---|---:|
| BTC_2024_1H_2K_REPRO | BTCUSDT | 1h | 2000 |
| BTC_2025_1H_2K_REPRO | BTCUSDT | 1h | 2000 |
| SOL_2024_1H_2K_REPRO | SOLUSDT | 1h | 2000 |
| SOL_2025_1H_2K_REPRO | SOLUSDT | 1h | 2000 |

Die Matrix liegt in:

```text
docs/befunde/279_REPRO_ASSET_ZEITEBENE_TOPOLOGIE_MATRIX.md
```

Der Delta-Vergleich liegt in:

```text
docs/befunde/280_REPRO_ASSET_ZEITEBENE_DELTA.csv
```

## Befund

Alle Rollen- und Qualitaetswerte reproduzieren exakt:

```text
delta_share                 = 0.00000000
delta_avg_rekopplung        = 0.00000000
delta_avg_carry             = 0.00000000
delta_avg_strain            = 0.00000000
delta_avg_sensory           = 0.00000000
delta_rekopplung_top_share  = 0.00000000
delta_strain_top_share      = 0.00000000
```

Das gilt fuer alle vier Welten und fuer alle drei Rollen:

- zentrum_stabil,
- offene_variante,
- spannungsrand_kippnaehe.

## Interpretation

Die Asset-/1h-Zeitebenen-Pruefung ist unter gleicher Datenwelt und frischem Memory exakt reproduzierbar.

Damit wird die Trennung aus den vorherigen Befunden staerker:

```text
gleiche Welt -> gleiche Rollenmatrix
andere Welt  -> gleiche Rollenordnung mit anderer Gewichtung
```

## Grenze

Der Befund betrifft nur die aktuell getesteten 1h-Fenster.
Er sagt noch nicht, dass jede Zeitebene oder jedes Asset dieselbe Topologieklasse erzeugt.

## Wie es weitergeht

Als naechstes ist KASUSDT als Kleinpreis-Welt relevant.
Damit wird geprueft, ob MINI_DIO auch bei sehr anderem Preisniveau dieselbe weltrelative Rollenordnung bilden kann.
