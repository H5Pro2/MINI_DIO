# 1514 - Synthetische Randdominanz als Härtefall für DIO_14WJ

## Zweck

Nach DOGE als rauschiger Realwelt wurde ein gezielter synthetischer Härtefall geprüft:

`data/kontrolliert_synthetic_mcm_rand_dominanz_a_5m.csv`

Der Lauf wurde frisch mit eigener Memory ausgeführt:

`debug/1514_synth_randdominanz_a_dio14wj_hardcheck`

Ziel war zu prüfen:

```text
Bleibt dio_14wj auch bei echter Randdominanz ruhige Rekopplungsnähe,
oder entsteht eine andere Randrolle?
```

## Laufdaten

Ausgeführt wurden zwei Läufe mit `world_relative`:

```powershell
python -m mini_dio.run_mini --data data\kontrolliert_synthetic_mcm_rand_dominanz_a_5m.csv --runs 2 --reset-memory --debug-root debug\1514_synth_randdominanz_a_dio14wj_hardcheck --world-label 1514_synth_randdominanz_a --sense-mode world_relative
```

## Ergebnis

Die Läufe sind stark reproduzierbar.

| Kennwert | Lauf 1 | Lauf 2 |
| --- | ---: | ---: |
| Unique Symbols | 226 | 226 |
| Avg MCM Carry | 0.5904 | 0.5906 |
| Avg MCM Rekopplung | 0.7411 | 0.7410 |
| Avg MCM Strain | 0.1298 | 0.1297 |
| Avg Afterimage | 0.6477 | 0.6477 |
| Stable Inner Effect | 0.9314 | 0.9312 |
| Carried Unrest | 0.0679 | 0.0681 |
| Strained | 0.0001 | 0.0001 |
| Tipping | 0.0006 | 0.0006 |

Die Zielrollen `dio_0l7p` und `dio_14wj` erscheinen in dieser Welt nicht:

| Familie | Lauf 1 Count | Lauf 2 Count |
| --- | ---: | ---: |
| `dio_0l7p` | 0 | 0 |
| `dio_14wj` | 0 | 0 |
| `dio_1wdi` | 0 | 0 |
| `dio_1fll` | 3695 | 7390 |

Die dominante Symbolfamilie ist:

```text
dio_1fll
```

## Deutung

Dieser Härtefall zeigt keine Drift von `dio_14wj` in Randspannung.

Stattdessen passiert etwas anderes:

```text
Die Welt erzeugt eine eigene dominante Randdominanz-Rolle.
```

`dio_14wj` bleibt damit nicht als ruhige Rekopplungsnähe in einer Welt sichtbar, deren synthetische Struktur stark randdominant ist.

Wichtig ist die Unterscheidung:

- DOGE war rauschiger, aber realweltlich verteilt. Dort blieb `dio_14wj` sichtbar.
- Synthetische Randdominanz ist strukturell anders. Dort verschwindet `dio_14wj` und `dio_1fll` übernimmt.

Das spricht nicht gegen `dio_14wj`. Es grenzt die Rolle präziser ein:

```text
dio_14wj = ruhige sensorische Rekopplungsnähe
dio_1fll = dominante synthetische Rand-/Nachhall-Tragung
```

## MCM-Deutung

Die MCM-Rollenkarte wird dadurch schärfer.

Es gibt nicht nur:

```text
ruhig / unruhig
stabil / randnah
```

Sondern mindestens zwei verschiedene Weisen, wie Randnähe getragen werden kann:

1. Eine ruhige sensorische Rekopplungsnähe, die in Realwelten wie PAXG, SOL und DOGE wiedererkennbar bleibt.
2. Eine synthetisch erzeugte Randdominanz, die eine eigene sehr starke Feldrolle bildet.

Der zentrale Befund:

```text
Echte Randdominanz ersetzt die ruhige Rekopplungsrolle,
statt sie nur zu verfärben.
```

Damit ist der Rollenatlas nicht widerlegt. Er wird differenzierter:

- Weltfärbung kann Rollen modulieren.
- Starke Strukturänderung kann Rollen ersetzen.
- Neue Rollen entstehen nicht wahllos, sondern mit eigener hoher Reproduzierbarkeit.

## Grenze

`dio_1fll` ist aktuell als neue dominante Randdominanz-Rolle zu behandeln, aber noch nicht vollständig verstanden.

Offen bleibt:

- Ist `dio_1fll` spezifisch für diese synthetische Randdominanz?
- Taucht `dio_1fll` auch in anderen Rand-/Bruchwelten auf?
- Ist `dio_1fll` eine Randrolle, eine Nachhallrolle oder eine randdominante Stabilisierung?

## Wie es weitergeht

Als nächstes sollte `dio_1fll` gegen andere synthetische Rand- und Bruchwelten geprüft werden.

Die konkrete Prüffrage:

```text
Ist dio_1fll eine stabile Randdominanz-Rolle,
oder nur eine Spezialantwort auf diese eine synthetische Welt?
```
