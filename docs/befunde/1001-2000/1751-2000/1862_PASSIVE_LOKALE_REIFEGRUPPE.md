# 1862 - Passive Lokale Reifegruppe

## Grundfrage

Kann aus phasenlokal reproduzierten Familien eine passive Reifegruppe entstehen, ohne daraus Handlung, Gate oder Richtung zu machen?

## Umsetzung

Die Feldrollen-Memory wurde um `local_phase_maturity_group` erweitert.

Quelle:

- `docs/befunde/1001-2000/1751-2000/1861_PHASENLOKALE_FAMILIEN_REPRO_FOLGEFENSTER.csv`

Gespeichert werden nur Familien-Phasen-Paare, die:

- in der Baseline `phasenlokal_eigenstaendig` waren,
- in neuen Folgefenstern dieselbe lokale Phasenqualität reproduziert haben.

## Kurzbefund

- phasenlokal eigenständige Baseline-Paare: `446`
- stabil reproduzierte lokale Qualitäten: `254`

Repro-Profil der eigenständigen Baseline-Paare:

```text
lokale_qualitaet_reproduziert:254
lokale_qualitaet_wird_offen:81
lokale_qualitaet_wird_nullnah:42
lokale_qualitaet_wird_nachhallnah:40
lokale_qualitaet_wird_kernnah:13
lokale_qualitaet_driftet:11
fehlt_im_folgefenster:5
```

## Einordnung

Diese Gruppe ist kein Entscheidungssystem.

Sie ist eine passive Reifeschicht:

- Familie,
- Asset,
- Phase,
- lokale Anschlussqualität,
- Rekopplungs-Edge,
- Nachhall-Edge,
- Temporal-Edge.

Damit bekommt MINI_DIO einen sauberen Kern für Feldrollen-Reifung:
Nicht `ich kenne diesen Namen`, sondern `diese Familie trägt in dieser Phase wiederholt eine ähnliche lokale Qualität`.

Das ist methodisch wichtiger als eine reine Symboltabelle.
Es trennt:

- Namenswiederkehr,
- Fensterwirkung,
- lokale Phasenqualität,
- echte Kontextdrift.

## Grenze

Die Reifegruppe bleibt passiv:

- `read_by_mini_dio = 0`
- `influences_action = 0`
- `is_gate = 0`
- `is_motoric = 0`
- `is_entry_signal = 0`
- `is_direction_signal = 0`

## Wie es weitergeht

Als nächstes sollte diese passive Reifegruppe gegen weitere Weltfenster geprüft werden.
Entscheidend ist, ob die 254 stabilen lokalen Qualitäten erneut stabil bleiben, sich teilen oder in neue Feldrollen übergehen.
