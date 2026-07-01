# Befund 1198 - Getrennte Desync-Teilwelten

## Grundfrage

Befund 1196 zeigte: Widerspruch zwischen Sinnesachsen erzeugt mehr Rand-/Kippnaehe als reine Lautstaerke. Die naechste Frage war daher:

```text
Welche Sinnesachse erzeugt diese Randnaehe staerker?
```

Dafuer wurden zwei Teilwelten gebaut:

1. `Sehen stabil / Hoeren chaotisch`
2. `Sehen chaotisch / Hoeren stabil`

## Datengrundlage

- Builder: `data_builder/synthetic_desync_world_builder.py`
- Welt 1: `data/synthetic_mcm_visual_stable_hearing_chaotic_5m.csv`
- Welt 2: `data/synthetic_mcm_visual_chaotic_hearing_stable_5m.csv`
- Lauf 1: `debug/1197_visual_stable_hearing_chaotic/dio_mini_lauf_2/`
- Lauf 2: `debug/1197_visual_chaotic_hearing_stable/dio_mini_lauf_2/`
- Matrix: `docs/befunde/1197_GETRENNTE_DESYNC_TEILWELTEN_TOPOLOGIE_MATRIX.md`
- CSV: `docs/befunde/1197_GETRENNTE_DESYNC_TEILWELTEN_TOPOLOGIE_MATRIX.csv`

Beide Laeufe wurden mit frischem Memory im Modus `world_relative` ausgefuehrt.

## Kerndaten

### Sehen stabil / Hoeren chaotisch

- Kerzen: `7400`
- Episoden: `7394`
- eindeutige Symbole: `25`
- Rekopplung: `0.7539`
- Carry: `0.6057`
- Strain: `0.1296`
- Sinneskopplung: `0.9087`
- Nachhall: `0.7756`
- Trust-Stuetze: `0.9368`
- Caution-Stuetze: `0.0329`

Innenfeldklassen:

- `stabil`: `7034`
- `tragend_unruhig`: `180`
- `kippend`: `179`
- `gespannt`: `1`

Topologische Rollen:

| Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|
| `zentrum_stabil` | `0.9513` | `0.7603` | `0.6133` | `0.1224` | `0.9199` |
| `offene_variante` | `0.0243` | `0.6472` | `0.4728` | `0.2481` | `0.7274` |
| `spannungsrand_kippnaehe` | `0.0243` | `0.6112` | `0.4414` | `0.2923` | `0.6558` |

### Sehen chaotisch / Hoeren stabil

- Kerzen: `6400`
- Episoden: `6394`
- eindeutige Symbole: `19`
- Rekopplung: `0.7590`
- Carry: `0.6208`
- Strain: `0.1182`
- Sinneskopplung: `0.9179`
- Nachhall: `0.8688`
- Trust-Stuetze: `0.9603`
- Caution-Stuetze: `0.0147`

Innenfeldklassen:

- `stabil`: `6392`
- `tragend_unruhig`: `2`

Topologische Rollen:

| Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|
| `zentrum_stabil` | `0.9997` | `0.7590` | `0.6209` | `0.1182` | `0.9179` |
| `offene_variante` | `0.0003` | `0.6493` | `0.4266` | `0.1883` | `0.8138` |

## Bewertung

Die Teilung zeigt eine klare Richtung:

```text
Chaotisches Hoeren bei stabiler Form erzeugt deutlich mehr Rand-/Kippnaehe
als chaotischere visuelle Form bei stabilem Hoeren.
```

Das ist fuer MINI_DIO relevant, weil Hoeren im aktuellen System die energetische bzw. tonale Stimulation traegt. Sehen bleibt eher Formaufnahme und Strukturnaehe. Wenn das Hoeren chaotisch wird, steigt die Feldspannung staerker. Wenn das Sehen unruhiger wird, aber die tonale Achse stabil bleibt, kann das Feld die Lage fast vollstaendig rueckkoppeln.

## Schlussfolgerung

Die MCM-Feldwirkung scheint im aktuellen Aufbau nicht gleich stark von allen Sinnesachsen belastet zu werden:

- `Hoeren` wirkt naehr an energetischer Stimulation.
- `Sehen` wirkt naehr an Form- und Strukturaufnahme.
- `Rezeptorik` entscheidet, wie stark daraus MCM-Feldwirkung wird.
- Randnaehe entsteht besonders dort, wo tonale Energie und Feldpassung auseinanderlaufen.

Das spricht gegen ein reines Rohdatenmodell. MINI_DIO bildet keine einfache Summe aus Weltwerten, sondern eine rezeptorische Felduebersetzung.

## Bedeutung fuer die naechste Mechanik

Die naechste Verbesserung sollte nicht das MCM-Feld selbst veraendern. Das Feld zeigt weiterhin stabile Rueckfuehrung. Der wichtigere Punkt liegt vor dem Feld:

```text
Sinnesachse -> Rezeptorik -> Feldwirkung
```

Vor allem die Hoerachse braucht eine klarere Untersuchung:

- Wann wird tonale Energie als tragend gelesen?
- Wann wird sie als Randnaehe gelesen?
- Wann wird sie durch Rezeptorik gedämpft?
- Wann bleibt sie als Nachhall aktiv?

## Wie es weitergeht

Als naechstes sollte die Hoerachse isoliert untersucht werden. Dazu reicht keine weitere allgemeine Welt. Sinnvoll ist eine reine Hoer-Gegenprobe: stabile Form, aber systematisch steigende, fallende und pulsierende Energie. Danach kann entschieden werden, ob MINI_DIO eine eigene passive Hoer-Topologie ausbildet.
