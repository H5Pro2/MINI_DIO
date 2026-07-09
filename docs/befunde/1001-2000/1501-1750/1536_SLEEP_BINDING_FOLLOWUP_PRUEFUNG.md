# 1536 - Sleep Binding Follow-up Pruefung

## Zweck

Diese Pruefung erweitert `1535`.

Die Frage lautet nicht:

```text
Muss eine Offline-Bindung spaeter real getragen werden?
```

Sondern:

```text
Taucht ein im entkoppelten Feld entstandenes oder verarbeitetes Muster
spaeter in realer Lage wieder auf?

Oder werden vor allem alte Episodenrollen gefestigt?
```

## Neues Werkzeug

Neu hinzugefuegt wurde:

- `tools/report_sleep_binding_followup.py`

Das Werkzeug liest:

- einen vorhandenen Sleep-Environment-Debug,
- die Quell-Memory,
- eine oder mehrere reale Folge-Memory-Dateien.

Es prueft passiv:

- ob Sleep-Symbole in realen `symbols` wieder auftauchen,
- ob aktive Sleep-Episodenrollen in realem `mcm_field_episode_memory` wieder auftauchen,
- welche Rollenqualitaet diese Treffer tragen.

Es erzeugt keine neue Aussenwelt und schreibt kein Runtime-Memory.

## Gepruefte Sleep-Laeufe

| Sleep-Lauf | Quelle | Sleep-Top-Symbol | aktive Rollen |
| --- | --- | --- | ---: |
| SOL 2024 Sleep | SOL 2024 5m | `dio_019bn1b` | 5 |
| Stress 2023 Sleep | Stress 2023 5m | `dio_019bn1b` | 5 |

## Ergebnisse

| Sleep-Lauf | Folgepruefungen | Sleep-Symbol real wiedergefunden | alte Episodenrollen wiedergefunden | nur Quellrollen |
| --- | ---: | ---: | ---: | ---: |
| SOL 2024 Sleep | 3 | 0 | 2 | 1 |
| Stress 2023 Sleep | 3 | 0 | 1 | 2 |

## Befund

Das Offline-Symbol:

```text
dio_019bn1b
```

tauchte in den geprueften realen Memory-Dateien nicht als normales Weltsymbol wieder auf.

Damit ist es aktuell nicht als neue weltunabhaengige Semantik bestaetigt.

Was aber sichtbar ist:

```text
aktive Sleep-Episodenrollen
  -> koennen in realen Memory-Dateien wieder auftauchen
  -> wirken damit eher als Festigung oder Wiederberuehrung alter Episodenrollen
```

## Einordnung

Der aktuelle Stand spricht eher fuer:

```text
Offline-Rekopplung
alte Episodenrollen bleiben aktivierbar
teilweise Wiederauftauchen alter Rollen in realen Memories
```

Noch nicht sichtbar ist:

```text
neue Offline-Symbolbindung
die spaeter als eigenstaendiges reales Muster wiederkehrt
```

## Wichtig

Das ist kein negativer Befund.

Es trennt sauber:

```text
Offline-Aktivitaet != neue Bedeutung
Rekopplung alter Rollen != neue Semantik
Wiederauftauchen alter Rollen = moegliche Musterfestigung
```

## Naechste Prueffrage

Die naechste technische Frage lautet:

```text
Kann das Sleep-Environment Rollen phasisch differenzieren,
ohne eine feste Sequenz zu erzwingen?
```

Erst wenn daraus neue Offline-Symbole oder neue Rollenbindungen entstehen, kann geprueft werden, ob diese spaeter in realer Lage wieder auftauchen.

