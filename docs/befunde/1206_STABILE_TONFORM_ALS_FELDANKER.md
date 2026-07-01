# Befund 1206 - Stabile Tonform als Feldanker

## Grundfrage

Nach Befund 1204 war offen:

```text
Kann stabile Tonform visuelle Formbrueche abfedern?
```

Dafuer wurde eine synthetische Welt gebaut, in der die Hoerachse stabil pulsiert, waehrend die visuelle Form gezielt bricht.

## Datengrundlage

- Builder: `data_builder/synthetic_desync_world_builder.py`
- Variant: `visual_breaks_stable_pulse`
- Welt: `data/synthetic_mcm_visual_breaks_stable_pulse_5m.csv`
- Lauf: `debug/1205_visual_breaks_stable_pulse/dio_mini_lauf_2/`
- Topologiematrix: `docs/befunde/1205_VISUELLE_BRUECHE_STABILER_PULS_TOPOLOGIE_MATRIX.md`
- Phasenruecklesung: `docs/befunde/1205_VISUELLE_BRUECHE_STABILER_PULS_PHASEN_RUECKLESUNG.md`

## Kerndaten

- Episoden: `6594`
- Topologiezustand: `stark_zentriert_wenig_rand`
- `zentrum_stabil`: `0.9848`
- `offene_variante`: `0.0149`
- `spannungsrand_kippnaehe`: `0.0003`
- Rekopplung: `0.7336`
- Carry: `0.5772`
- Strain: `0.1398`
- Sinneskopplung: `0.8917`

## Phasenbefund

| Phase | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Hoer-Gap |
|---|---:|---:|---:|---:|---:|---:|---:|
| ruhige_form_leiser_ton | `0.9988` | `0.0000` | `0.0013` | `0.7615` | `0.6188` | `0.1197` | `0.0036` |
| stabiler_puls_klare_form | `0.9983` | `0.0017` | `0.0000` | `0.7223` | `0.5574` | `0.1483` | `0.1201` |
| formbruch_stabiler_puls | `0.9321` | `0.0679` | `0.0000` | `0.7204` | `0.5556` | `0.1457` | `0.1115` |
| rekopplung_stabiler_puls | `0.9989` | `0.0011` | `0.0000` | `0.7309` | `0.5753` | `0.1469` | `0.1175` |
| zweiter_formbruch_stabiler_puls | `0.9993` | `0.0000` | `0.0007` | `0.7239` | `0.5646` | `0.1467` | `0.1124` |
| stille_schlussrekopplung | `1.0000` | `0.0000` | `0.0000` | `0.7626` | `0.6219` | `0.1195` | `0.0036` |

## Interpretation

Der erste visuelle Formbruch erzeugt noch Uebergangsraum:

```text
formbruch_stabiler_puls -> offene_variante ca. 6.79%
```

Der zweite Formbruch bei gleicher stabiler Tonform erzeugt fast keine offene Variante mehr:

```text
zweiter_formbruch_stabiler_puls -> zentrum_stabil ca. 99.93%
```

Das spricht dafuer, dass MINI_DIO die Welt nicht nur punktuell liest. Die Feldwirkung scheint sich ueber die Sequenz zu organisieren:

- erster Bruch: Uebergangsraum,
- Rekopplungsphase: Rueckbindung,
- zweiter Bruch: staerker integriert,
- stille Schlussphase: volle Zentrierung.

## MCM-Lesart

Stabile Tonform kann im aktuellen Aufbau als passiver Feldanker wirken.

Das bedeutet nicht, dass Hoeren immer beruhigt. Die bisherigen Befunde zeigen:

- chaotisches Hoeren kann Rand/Kippnaehe erzeugen,
- pulsierendes Hoeren kann Uebergangsraum erzeugen,
- stabile Tonform kann visuelle Brueche abfedern,
- Stille kann Schlussrekopplung beguenstigen.

Damit wird Hoeren als zeitliche Feldachse sichtbar:

```text
Hoeren wirkt nicht nur als Energiehoehe,
sondern als Rhythmus, Sequenz und Rekopplungsmoeglichkeit.
```

## Schlussfolgerung

Die neue Gegenprobe stuetzt die These aus 1204:

```text
Nicht visuelle Unruhe allein erzeugt Randnaehe.
Entscheidend ist die Kopplungsqualitaet der Sinnesachsen.
```

MINI_DIO zeigt hier eine passive Anpassung:

```text
Ein wiederholter visueller Bruch wird bei stabiler Tonform weniger stoerend gelesen.
```

Das ist fuer das MCM-System wichtig, weil es eine organische Wahrnehmungsfunktion andeutet: Das Feld kann wiederkehrende Weltspannung ueber eine stabilere Sinnesachse einordnen, statt jeden Bruch neu als Randereignis zu behandeln.

## Wie es weitergeht

Als naechstes sollte die Gegenrichtung getestet werden: unstabile/chaotische Tonform bei klarer visueller Rekopplung. So laesst sich pruefen, ob visuelle Ordnung Hoerchaos ebenfalls abfedern kann oder ob Hoeren die staerkere Randachse bleibt.
