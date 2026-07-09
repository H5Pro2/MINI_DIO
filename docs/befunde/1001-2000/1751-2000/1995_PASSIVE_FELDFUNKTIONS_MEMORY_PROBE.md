# Befund 1995 - Passive Feldfunktions-Memory

Stand: 2026-07-09

## Prüfung

Es wurde ein separater Probelauf mit einer kopierten PEPE-C-Memory ausgeführt.
Ziel war nicht ein neuer Weltbefund, sondern die technische Prüfung, ob Preview-Anker ihre Feldfunktionsqualität passiv speichern.

```text
data/kontrolliert_pepe_2024_5m_10k_c_PEPEUSDT.csv
memory/1995_field_function_probe.json
debug/1995_field_function_probe
```

## Ergebnis

Die neue Memory-Lesung wurde geschrieben.

```text
Anker insgesamt: 512
Anker mit Feldfunktionslesung: 84
active_recoupling: 78
milieu_island: 6
```

Beispiele:

| Symbol | Feldfunktion | Variante | Konfidenz | Depth |
|---|---:|---:|---:|---:|
| `dio_mcm_episode_0hiolzy` | `milieu_island` | `quiet_deep_recoupling` | 0.803521 | 0.871007 |
| `dio_mcm_episode_1dxx3n8` | `active_recoupling` | `compact_carried_recoupling` | 0.673328 | 0.862999 |
| `dio_mcm_episode_1amcian` | `milieu_island` | `quiet_deep_recoupling` | 0.660679 | 0.857134 |
| `dio_mcm_episode_0t6i5u5` | `active_recoupling` | `compact_carried_recoupling` | 0.647915 | 0.853628 |

## Bewertung

Die Rollenmatrix wurde damit nicht hart in das System geschrieben.
Stattdessen liest MINI_DIO aus vorhandenen passiven Profilen eine Feldfunktionsqualität:

- Milieuinsel,
- aktive Rekopplung,
- offene Oberfläche,
- noch nicht lesbar.

Alle geschriebenen Felder bleiben passiv:

```text
influences_action = 0
is_gate = 0
is_motoric = 0
is_entry_signal = 0
is_direction_signal = 0
```

## Schluss

Der Schritt ist technisch sauber: Die Memory kann jetzt nicht nur Tiefe, Weltbreite, Nachhall und Rekurrenz tragen, sondern auch eine erste passive Funktionsqualität.

Das ist ein Baustein für ein reiferes MCM-System, weil spätere Forschung nicht mehr nur fragt:

```text
Wie oft taucht ein Symbol auf?
```

sondern auch:

```text
Welche Feldfunktion trägt dieses Symbol im Innenfeld?
```

## Nächster Schritt

Die neue Lesung sollte über mehrere Welten geprüft werden.
Entscheidend ist, ob `milieu_island` und `active_recoupling` stabil zu den bisherigen Rollenbefunden passen oder ob die Funktion bei anderen Weltspannungen driftet.
