# 1406-1409 - Frequenzreihe als Schwellenpruefung

## Zweck

Diese Pruefung variiert die Wechselrate bei gleicher Grundamplitude.

Ziel ist zu klaeren:

Entsteht `tragend_unruhig` linear mit steigender Richtungswechselrate oder zeigt das MCM-Feld eine nichtlineare Resonanz?

## Welten

| Welt | Richtungswechsel | Quiet Score |
|---|---:|---:|
| `HOLDOUT_FREQ25` | `250` | `0.406726` |
| `HOLDOUT_FREQ50` | `499` | `0.525593` |
| `HOLDOUT_FREQ75` | `748` | `0.665805` |
| `HOLDOUT_FREQ100` | `998` | `0.772034` |

Range, Amplitude und Volumen liegen vergleichbar. Der Hauptunterschied ist die Wechselverdichtung.

## MINI_DIO Befund

| Welt | Unique Symbols | Stabil | Tragend Unruhig | Carry | Rekopplung | Strain | Sensory Coupling | Afterimage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `HOLDOUT_FREQ25` | `80` | `745` | `249` | `0.538215` | `0.712426` | `0.133074` | `0.854111` | `0.190081` |
| `HOLDOUT_FREQ50` | `82` | `729` | `265` | `0.532277` | `0.706868` | `0.141215` | `0.837471` | `0.205770` |
| `HOLDOUT_FREQ75` | `66` | `792` | `202` | `0.539481` | `0.711414` | `0.139519` | `0.844552` | `0.255683` |
| `HOLDOUT_FREQ100` | `55` | `590` | `404` | `0.537480` | `0.704598` | `0.152934` | `0.820177` | `0.282405` |

Alle vier Welten erzeugen `tragend_unruhig`.

## Erkenntnis

Die Unruhe entsteht nicht erst bei maximaler Wechselrate.

Bereits `250` Richtungswechsel erzeugen eine deutliche tragend-unruhige Innenfeldwirkung. Die Entwicklung ist aber nicht linear:

- `50%` ist leicht unruhiger als `25%`,
- `75%` faellt wieder zurueck,
- `100%` erzeugt die staerkste tragend-unruhige Wirkung.

Das spricht gegen eine simple Regel "mehr Wechsel = mehr Unruhe".

Plausibler ist:

Das MCM-Feld reagiert auf zeitliche Wechselstruktur als Rhythmus- oder Resonanzqualitaet. Bestimmte Wechselmuster erzeugen mehr Innenfeldspannung als andere, obwohl die Rohamplitude aehnlich bleibt.

## Methodische Bedeutung

Die vorherige Annahme, dass grosse Range oder Drawdown die Hauptursache fuer Spannungsnaehe sind, wird geschwaecht.

Staerker wirkt derzeit:

- zeitliche Verdichtung,
- Frequenzwechsel,
- Rhythmusbruch,
- verringerter Nachhall,
- sinkende sensorische Kopplung.

## Grenze

Dieser Befund ist passiv.

Er zeigt eine Innenfeldreaktion, keine Handlung, keine Strategie und keine Zielentscheidung.

## Wie es weitergeht

Als naechstes sollte nicht nur die Wechselrate, sondern die Rhythmusform variiert werden: regelmaessiger Wechsel, unregelmaessiger Wechsel, Blockwechsel und Schwingungswechsel. Entscheidend ist, ob `tragend_unruhig` eher durch Rate oder durch rhythmische Form entsteht.
