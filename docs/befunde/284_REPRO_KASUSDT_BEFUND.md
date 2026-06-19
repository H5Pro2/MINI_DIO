# Befund: Reproduktion KASUSDT Kleinpreis-Welt

Stand: 2026-06-19

## Zweck

Diese Datei haelt die Reproduktion des KASUSDT-Kleinpreis-Tests fest.

Geprueft wurde:

```text
KASUSDT mit kleinem Preisniveau + frisches Memory -> gleiche passive Rollenmatrix?
```

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Testaufbau

Reproduziert wurden:

| Welt | Markt | Zeitebene | Kerzen |
|---|---|---|---:|
| KAS_2024_5M_2K_REPRO | futures_um | 5m | 2000 |
| KAS_2024_1H_2K_REPRO | futures_um | 1h | 2000 |

Die Repro-Matrix liegt in:

```text
docs/befunde/283_REPRO_KASUSDT_TOPOLOGIE_MATRIX.md
```

Der Delta-Vergleich liegt in:

```text
docs/befunde/284_REPRO_KASUSDT_DELTA.csv
```

## Befund

KASUSDT reproduziert exakt.

Fuer beide Welten und alle drei Rollen gilt:

```text
delta_share                 = 0.00000000
delta_avg_rekopplung        = 0.00000000
delta_avg_carry             = 0.00000000
delta_avg_strain            = 0.00000000
delta_avg_sensory           = 0.00000000
delta_rekopplung_top_share  = 0.00000000
delta_strain_top_share      = 0.00000000
```

## Interpretation

KASUSDT war ein relevanter Test, weil der Preisbereich deutlich kleiner ist als bei SOL oder BTC.

Der aktuelle Befund:

```text
Auch eine Kleinpreis-Welt erzeugt unter world_relative
dieselbe passive Rollenmatrix bei Wiederholung.
```

Das spricht dafuer, dass MINI_DIO die Welt nicht nur ueber absolute Preisgroesse liest.
Die weltrelative Aufnahme stabilisiert die Wahrnehmung ueber stark unterschiedliche Preisniveaus.

## Bedeutung fuer MINI_DIO

Die bisherigen Befunde lassen sich jetzt sauberer trennen:

1. gleiche Welt:
   exakte Reproduktion.
2. andere Welt:
   gleiche Rollenordnung mit anderen Anteilen.
3. kleines Preisniveau:
   keine Zerlegung der passiven Topologie.

## Grenze

KAS wurde bisher nur mit 2024, 5m und 1h, je 2000 Kerzen geprueft.

Noch offen:

- KAS 15m/30m,
- KAS 2025,
- laengere KAS-Fenster,
- Vergleich gegen feste Aufnahme.

## Wie es weitergeht

Als naechstes sollte nicht weiter dieselbe Ebene wiederholt werden.
Der naechste hierarchische Schritt ist die Zeitebenenstaffelung:

```text
KAS 5m / 15m / 30m / 1h
```

Ziel:

- bleibt die Topologieklasse gleich?
- verschiebt sich Offen/Zentrum systematisch mit Zeitebene?
- bleibt KAS auch bei Zwischenebenen preisniveauunabhaengig stabil?
