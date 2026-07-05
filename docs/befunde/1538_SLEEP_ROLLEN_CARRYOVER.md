# 1538 - Sleep Rollen Carryover

## Zweck

Diese Pruefung erweitert `1537`.

Die Frage lautet:

```text
Welche im Schlaf aktiven Rollen tragen auch in realen Memory-Kontexten?
```

Damit wird nicht nach neuer Offline-Semantik gesucht, sondern nach Musterfestigung:

```text
Schlafrolle
  -> reale Memory-Kontexte
  -> rekopplungstragende Wiederkehr?
```

## Neues Werkzeug

Neu hinzugefuegt wurde:

- `tools/report_sleep_role_carryover.py`

Das Werkzeug liest:

- Sleep-Environment-Ticks,
- Quell-Memory,
- mehrere reale Folge-Memories.

Es wertet pro Schlafrolle aus:

- Aktivitaet im Sleep-Lauf,
- durchschnittliche Sleep-Resonanz,
- Qualitaet in der Quell-Memory,
- Treffer in Folge-Memories,
- Rollenqualitaet in Folge-Memories.

Es ist rein passiv.

## Ergebnisse

| Sleep-Lauf | aktive Sleep-Rollen | Carryover-Zustand |
| --- | ---: | --- |
| SOL 2024 Sleep Phase | 3 | 3 x `cross_memory_rekopplung` |
| Stress 2023 Sleep Phase | 6 | 6 x `cross_memory_rekopplung` |

## SOL 2024

| Rolle | Sleep-Ticks | Quelle | Folge-Treffer |
| --- | ---: | --- | ---: |
| `dio_mcm_episode_1k2bqha` | 320 | `rekopplung_tragend` | 2 |
| `dio_mcm_episode_0e7qvj1` | 320 | `rekopplung_tragend` | 2 |
| `dio_mcm_episode_1wra2fc` | 253 | `rekopplung_tragend` | 1 |

## Stress 2023

| Rolle | Sleep-Ticks | Quelle | Folge-Treffer |
| --- | ---: | --- | ---: |
| `dio_mcm_episode_0mk4vj4` | 320 | `rekopplung_tragend` | 1 |
| `dio_mcm_episode_0d1w2c7` | 224 | `rekopplung_tragend` | 1 |
| `dio_mcm_episode_0qx4uth` | 212 | `rekopplung_tragend` | 1 |
| `dio_mcm_episode_1gwfnz5` | 170 | `rekopplung_tragend` | 1 |
| `dio_mcm_episode_1g7u9la` | 154 | `rekopplung_tragend` | 1 |
| `dio_mcm_episode_0b7nep9` | 59 | `rekopplung_tragend` | 1 |

## Befund

Alle phasisch aktiven Sleep-Rollen der beiden geprueften Laeufe sind in den Folgepruefungen als `cross_memory_rekopplung` klassifiziert.

Das bedeutet:

```text
Die Sleep-Aktivitaet haengt nicht beliebig im Feld.
Sie beruehrt Rollen, die auch in realen Memory-Kontexten rekopplungstragend auftreten.
```

## Einordnung

Der Befund spricht aktuell fuer:

```text
Musterfestigung alter rekopplungstragender Rollen
```

Er spricht noch nicht fuer:

```text
neue weltunabhaengige Offline-Semantik
```

Das ist methodisch wichtig:

```text
Schlafaktivitaet
  -> nicht automatisch neue Bedeutung
  -> aber moeglicherweise Festigung tragender Feldrollen
```

## Naechste Prueffrage

Die naechste sinnvolle Frage lautet:

```text
Welche Rollen werden im Schlaf nicht aktiv,
obwohl sie real stark tragen?
```

Das wuerde zeigen, ob MCM-Schlafregulation selektiv arbeitet:

- nur rekopplungstragende Rollen,
- auch offene Muster,
- auch belastete Randnaehe,
- oder nur Rollen mit hoher Quellenpraegung.

