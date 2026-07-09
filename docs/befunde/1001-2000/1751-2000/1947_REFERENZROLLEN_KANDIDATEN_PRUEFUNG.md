# 1947 - Kandidatenprüfung für weitere passive Referenzrollen

## Grundfrage

Nach `dio_0tay/frueh` stellt sich die Frage, ob weitere Rollen stark genug sind, um später als passive Referenzrolle geführt zu werden.

Wichtig: Diese Prüfung erzeugt noch keine neue Referenzrolle. Sie sucht nur Kandidaten.

## Prüflogik

Eine Rolle wurde nur dann als Kandidat aufgenommen, wenn sie:

- mindestens 20 nicht-fehlende Rücklesungen hat,
- über mindestens 4 Assets vorkommt,
- mindestens 75 Prozent stabile Rücklesung trägt,
- weiterhin Weltvarianz zulässt.

Damit wird verhindert, dass die passive Memory zu einer bloßen Symboltabelle wird.

## Ergebnis

Gefunden wurden 5 family/phase-Zeilen:

| Familie | Phase | Lesung | nicht-fehlende Rücklesungen | stabile Rücklesung |
| --- | --- | --- | ---: | ---: |
| `dio_0tay` | `frueh` | bereits Referenzrolle | 65 | 0.846154 |
| `dio_14wj` | `frueh` | Kandidat: starker zonaler Träger | 86 | 0.790698 |
| `dio_1492` | `frueh` | Kandidat: durchgehende Nullnähe-Achse | 39 | 0.974359 |
| `dio_1492` | `spaet` | Kandidat: durchgehende Nullnähe-Achse | 42 | 0.809524 |
| `dio_1492` | `mitte` | Kandidat: durchgehende Nullnähe-Achse | 41 | 0.780488 |

## Einordnung der Kandidaten

### dio_14wj/frueh

`dio_14wj/frueh` ist breiter als `dio_0tay/frueh` in der Anzahl nicht-fehlender Rücklesungen, aber weniger rein.

Vorbefunde lesen diese Rolle als:

- `hoeren_leiser`
- `starker_zonaler_traeger`
- in B-Fokus links und mittig stabil, rechts nicht mehr durchgehend

Das spricht für eine zonale Brückenrolle, nicht für eine globale Referenzrolle.

Mögliche passive Lesung:

`fruehe_nullnahe_zonenbruecke`

Status:

`prüfen, noch nicht übernehmen`

### dio_1492

`dio_1492` erscheint in `frueh`, `mitte` und `spaet`.

Vorbefunde lesen diese Familie als:

- `kohaerenz_hoeher`
- phasenlokal eigenständig
- häufig `phase_nullnah`

Das wirkt weniger wie ein einzelner Punkt und eher wie eine phasenübergreifende Nullnähe-Achse.

Mögliche passive Lesung:

`phasenuebergreifende_nullnahe_kohaerenzachse`

Status:

`prüfen, aber nur als Achse, nicht als einzelne harte Rolle`

## Schlussfolgerung

`dio_0tay/frueh` bleibt die sauberste bereits übernommene Referenzrolle.

`dio_14wj/frueh` und `dio_1492` sind echte Kandidaten, aber sie sollten noch nicht direkt in die passive Referenzrollen-Memory übernommen werden.

Der Grund:

- `dio_14wj/frueh` ist zonal stark, aber nicht durchgehend.
- `dio_1492` ist stark, aber eher eine Achse über mehrere Phasen als eine einzelne Rolle.

Damit bestätigt sich die Richtung: Referenzrollen müssen selten bleiben. Sonst wird aus organischer Rücklesung wieder eine mechanische Symboltabelle.
