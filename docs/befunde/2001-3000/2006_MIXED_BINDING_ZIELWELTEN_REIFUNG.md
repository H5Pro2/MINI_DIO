# Befund 2006 - Mixed Binding durch Zielwelten

Stand: 2026-07-09

## Frage

Befund 2004 zeigte zwei mögliche Ursprungsbedingungen für `mixed_binding`:

```text
1. ruhige rekoppelnde Nähe
2. sichtbare Übergangsnähe
```

Diese Prüfung fragt:

```text
Reift mixed_binding, wenn eine passende Zielwelt dieselbe Feldbedingung erneut erzeugt?
```

## Vorgehen

Als Ausgang wurde die Memory aus Befund 1999 kopiert:

```text
memory/1999_world_binding_probe.json
```

Die Testmemory liegt in:

```text
memory/2005_mixed_binding_targeted_probe.json
```

Geprüfte Zielwelten:

```text
MB_TARGET_RUHIG_PAXG_REAL2024
MB_TARGET_RUHIG_BTC_QUIET2025
MB_TARGET_UEBERGANG_DOGE2024
MB_TARGET_UEBERGANG_BTC_FOLLOW6000_7000
```

Die Detailauswertung liegt in:

```text
docs/befunde/2001-3000/2005_MIXED_BINDING_ZIELWELTEN_PROBE.csv
docs/befunde/2001-3000/2005_MIXED_BINDING_ZIELWELTEN_PROBE.md
```

## Ergebnis der fünf Kandidaten

| Symbol | Vorher | Nachher | Berührung | Lesung |
|---|---|---|---:|---|
| `dio_mcm_episode_05w9z7v` | `mixed_binding` | `realworld_bound` | +3 | reift durch ruhige PAXG-Nähe |
| `dio_mcm_episode_08g2xgt` | `mixed_binding` | `mixed_binding` | +1 | bleibt gemischt |
| `dio_mcm_episode_0zkoaz0` | `mixed_binding` | `mixed_binding` | 0 | nicht erneut getroffen |
| `dio_mcm_episode_15jz0fg` | `mixed_binding` | `realworld_bound` | +3 | reift durch ruhige PAXG-Nähe |
| `dio_mcm_episode_1i07qau` | `mixed_binding` | `realworld_bound` | +1 | reift durch ruhige PAXG-Nähe |

## Kernbefund

Die gezielte ruhige PAXG-Zielwelt hat drei der fünf Kandidaten erneut getroffen und nach `realworld_bound` verschoben.

Vorher:

```text
Realweltanteil etwa 0.4 bis 0.5
Nullweltanteil etwa 0.5 bis 0.6
```

Nachher bei den gereiften Kandidaten:

```text
Realweltanteil etwa 0.667
Nullweltanteil etwa 0.333
```

Das ist keine automatische Reifung durch beliebige neue Welt. Die vorherige allgemeine Folgeweltprüfung hatte die Kandidaten nicht bewegt.

Die Reifung trat erst auf, als die Zielwelt zur rückgelesenen Feldbedingung passte:

```text
ruhige rekoppelnde Nähe
```

## Bedeutung für MINI_DIO

Dieser Befund stärkt die Annahme, dass `mixed_binding` kein bloßer Fehlerzustand ist.

`mixed_binding` kann eine Grenzrolle sein:

```text
feldintern tragfähig,
aber noch nicht eindeutig weltgebunden.
```

Wenn eine passende Weltbedingung wiederkehrt, kann diese Rolle realweltlich nachreifen.

Das ist wichtig für Feldintelligenz, weil MINI_DIO hier nicht einfach zählt, sondern kontextabhängig bindet:

```text
nicht jede neue Welt reift eine Rolle,
sondern nur passende Weltähnlichkeit berührt die vorhandene Feldform.
```

## Grenze

Die Prüfung ist weiterhin passiv. Sie erzeugt keine Handlung und keine Strategie.

Außerdem ist der Befund noch klein: fünf Kandidaten, davon drei gereift. Das ist ein starker Hinweis, aber noch kein allgemeines Gesetz.

## Wie es weitergeht

Als nächstes sollten wir diese Zielwelt-Reifung gegen eine Gegenprobe absichern:

```text
1. ruhige PAXG-Nähe erneut oder versetzt prüfen
2. eine ruhige Nicht-PAXG-Welt prüfen
3. eine sichtbare Übergangswelt gezielter suchen, weil die bisherigen Übergangswelten die zwei Übergangskandidaten nicht getroffen haben
```

Ziel ist zu klären, ob die Reifung an PAXG gebunden ist oder an die Feldbedingung `ruhige rekoppelnde Nähe`.
