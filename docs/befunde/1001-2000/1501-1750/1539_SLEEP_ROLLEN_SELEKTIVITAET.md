# 1539 - Sleep Rollen Selektivitaet

## Zweck

Diese Pruefung beantwortet die Gegenfrage aus `1538`:

```text
Welche realen Rollen werden im Schlaf nicht aktiv?
```

Damit wird geprueft, ob das Sleep-Environment einfach alle vorhandenen Rollen aktiviert oder ob es selektiv arbeitet.

## Neues Werkzeug

Neu hinzugefuegt wurde:

- `tools/report_sleep_role_selection_gap.py`

Das Werkzeug vergleicht:

- reale `mcm_field_episode_memory`-Rollen einer Quelle,
- Sleep-Aktivitaet derselben Quelle,
- Rollenqualitaet der aktivierten und nicht aktivierten Rollen.

Es schreibt keine Runtime-Memory und erzeugt keine neue Aussenwelt.

## Ergebnisse

| Quelle | reale Rollen | Sleep-aktiv | nicht Sleep-aktiv | aktive Qualitaet | inaktive Qualitaet |
| --- | ---: | ---: | ---: | --- | --- |
| SOL 2024 5m | 5 | 3 | 2 | 3 x `rekopplung_tragend` | 2 x `offen_ungeklart` |
| Stress 2023 5m | 7 | 6 | 1 | 6 x `rekopplung_tragend` | 1 x `offen_ungeklart` |

## Befund

In beiden Quellen gilt:

```text
Alle rekopplungstragenden Rollen wurden im Sleep-Lauf aktiv.
Offene/ungeklaerte Rollen blieben inaktiv.
```

Das bedeutet:

```text
Sleep-Aktivitaet ist nicht Vollaktivierung aller Memory-Rollen.
Sleep-Aktivitaet ist selektiv auf rekopplungstragende Rollen gerichtet.
```

## Einordnung

Der aktuelle Befund stuetzt die Lesart:

```text
MCM-Schlafregulation festigt bevorzugt bereits rekopplungstragende Rollen.
```

Nicht gezeigt ist:

```text
Bearbeitung offener oder ungeklaerter Rollen
Entlastung belasteter Randnaehe
Entstehung neuer Offline-Semantik
```

## Methodischer Wert

Dieser Befund ist wichtig, weil er eine einfache Gegenhypothese abschwaecht:

```text
Wenn Sleep nur alles aktiviert,
ist keine Selektion sichtbar.
```

Die Daten zeigen bisher:

```text
Sleep aktiviert nicht alles.
Sleep aktiviert im geprueften Stand die rekopplungstragenden Rollen.
```

## Naechste Prueffrage

Die naechste Frage lautet:

```text
Kann das Sleep-Milieu auch offene Rollen beruehren,
wenn die Aktivierungsnaehe anders gelesen wird,
ohne sie kuenstlich zu erzwingen?
```

Das waere der naechste Schritt, um zwischen reiner Festigung und moeglicher Verarbeitung offener Muster zu unterscheiden.

