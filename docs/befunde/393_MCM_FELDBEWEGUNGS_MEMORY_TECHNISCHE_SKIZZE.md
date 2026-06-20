# MCM-Feldbewegungs-Memory technische Skizze

Stand: 2026-06-20

## Zweck

`MCMFieldMovementMemory` ist eine passive Speicherschicht fuer wiederkehrende MCM-Feldbewegungen.

Sie speichert nicht Regulation.
Sie speichert nicht Wahrnehmungssteuerung.
Sie speichert nicht Handlung.

Sie speichert:

```text
Welche MCM-Feldbewegung kommt wieder?
Welche Feldwirkung traegt sie?
Driftet sie?
Fragmentiert sie?
Rekoppelt sie?
Bleibt sie jung oder wird sie wiederkehrend?
```

## Hierarchie

1. Grundfrage: Wie merkt sich MINI_DIO wiederkehrende Feldwirkung, ohne daraus Regeln zu bauen?
2. Unterpruefung: Welche Bewegungen, Tragarten und Driftspuren muessen passiv gespeichert werden?
3. Folgeschritt: Getrennt davon wird die rezeptorisch-regulatorische Wahrnehmungsschicht beschrieben.

## Grundprinzip

```text
Weltkontakt
-> Sinnesaufnahme
-> rezeptorisch-regulatorische Wahrnehmungsschicht
-> MCM-Feldwirkung
-> MCM-Feldbewegung
-> MCMFieldMovementMemory
```

Die Memory-Schicht beginnt erst nach der MCM-Feldwirkung.
Sie darf nicht mit der Wahrnehmungssteuerung verwechselt werden.

## Eingaben

`MCMFieldMovementMemory` erhaelt verdichtete Feldbewegungsbefunde:

| Eingabe | Bedeutung |
|---|---|
| `movement_key` | gerichtete Feldbewegung, z.B. `from -> to` |
| `top_passive_quality` | Tragart/Feldwirkung, z.B. `eng_getragen`, `fragmentiert` |
| `quality_profile` | Profil der beobachteten Tragarten |
| `top_signature` | dominante Feldpositionsfolge |
| `drift_label` | Wiederkehr-/Driftbeschreibung |
| `events` | Ereignisanzahl als Befundwert |
| `worlds` | Anzahl einbezogener Welten |
| `timeframe` | Weltaufloesung |
| `asset` | Asset-/Weltfamilie |
| `source` | Quellreport |

Nicht speichern:

```text
Fokus / Abstand
lauter / leiser
scharf / unscharf
Druck / Entspannung
Entry
Exit
PnL
Gate
Strategie
```

## Warum die vier Achsen nicht hier liegen

Die Achsen:

```text
Fokus / Abstand
lauter / leiser
scharf / unscharf
Druck / Entspannung
```

beschreiben, wie Informationen in das Feld gelangen, wie nah sie gelesen werden, wie laut sie wirken, wie klar sie sind und ob der Rezeptorkontakt Druck oder Entspannung erzeugt.

Sie gehoeren deshalb in die rezeptorisch-regulatorische Wahrnehmungsschicht.

`MCMFieldMovementMemory` speichert erst die gewachsene Feldspur danach.

## Speicherform

Minimal:

```json
{
  "movement_key": "dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy",
  "seen_count": 0,
  "total_events": 0,
  "dominant_tragart": "eng_getragen",
  "field_memory_quality": "recurrently_carried",
  "maturity_note": "young_trace",
  "dominant_field_position": "rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage",
  "dominant_drift_label": "wiederkehrend_variabel"
}
```

## Feldmemory-Qualitaeten

| Qualitaet | Bedeutung |
|---|---|
| `young` | Einzelspur oder noch zu wenig Wiederkehr |
| `recurrently_carried` | wiederkehrend getragen |
| `recurrently_fragmented` | wiederkehrend fragmentiert |
| `open_drifting` | offen driftend, noch nicht kollabiert |
| `mixed_unstable` | gemischt, noch nicht klar |
| `world_specific` | bisher nur weltbezogen belastbar |
| `asset_sensitive` | assetabhaengig |
| `timeframe_sensitive` | aufloesungsabhaengig |

Diese Qualitaeten sind Befundsprache, keine Regeln.

## Aktueller Code

```text
mini_dio/mcm_field_movement_memory.py
tools/report_mcm_field_movement_memory.py
```

Kernklassen:

```text
FieldMovementObservation
MCMFieldMovementRecord
MCMFieldMovementMemory
```

## Explizite Grenze

`MCMFieldMovementMemory` darf nicht:

- Wahrnehmung steuern,
- Informationen lauter/leiser stellen,
- Fokus oder Abstand setzen,
- Druck oder Entspannung erzeugen,
- Handlung beeinflussen,
- Gates bilden,
- Entries oder Exits erzeugen.

## Aktueller Befund

Die bisherige Mehrwelt-Verdichtung liest:

```text
1t5bcxp -> 183drjy
```

als wiederkehrend getragen.

Der Rueckweg:

```text
183drjy -> 1t5bcxp
```

wird wiederkehrend fragmentierter gelesen.

Eine unabhaengige Late-Shift-Welt erzeugt dagegen:

```text
02xikfk -> 1t5bcxp
```

als junge Einzelspur.

Das ist fachlich wichtig: Wiederkehr wird verdichtet, Einzelkontakt bleibt jung.

## Wie es weitergeht

Als naechstes wird die rezeptorisch-regulatorische Wahrnehmungsschicht separat festgehalten. Sie beschreibt, wie unterschiedliche Asset- und Weltklassen ueber Fokus/Abstand, lauter/leiser, scharf/unscharf und Druck/Entspannung in das MCM-Feld gelangen.
