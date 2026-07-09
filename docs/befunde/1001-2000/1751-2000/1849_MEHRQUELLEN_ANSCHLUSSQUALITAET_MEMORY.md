# 1849 - Mehrquellen-Anschlussqualität in der Feldrollen-Memory

## Grundfrage

Bleibt die passive Anschlussqualität stabil genug, um nicht nur aus `1846`,
sondern aus mehreren Fensterprüfungen gelesen zu werden?

## Umsetzung

`tools/update_mcm_field_role_memory.py` liest die Anschlussqualität jetzt aus mehreren Quellen:

- `1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv`
- `1848_ANSCHLUSSQUALITAET_NEUE_FENSTER.csv`

Die Anschlussqualität bleibt Teil der passiven Feldrollen-Memory.
Sie erzeugt keine Handlung, kein Gate, keine Richtung und keine Steuerung.

## Prüflauf

```text
updated memory\dio_mini_semantic_memory.json
top_roles=48
states={'feldrolle_anschlussfaehig': 107, 'feldrolle_reift_verdichtend': 37}
attachment_quality={'offen_gemischt': 8, 'kernnah': 5, 'kernnah_ohne_feldzeit': 3, 'nullnah': 2, 'nachhallnah_ohne_kern': 1, 'anschlussnah': 1}
```

## Befund

Die Anschlussqualitäten bleiben über zwei getrennte Prüfreihen sichtbar.
Sie verteilen sich nicht zufällig auf nur eine Einzelklasse.

Aktueller passiver Bedeutungsraum:

- `offen_gemischt`: häufigste offene Zwischenlage
- `kernnah`: klare oder graduelle Kernnähe
- `kernnah_ohne_feldzeit`: Kernnähe, aber noch ohne Feldzeitvorsprung
- `nullnah`: Fenster, in denen Nullwelten stärker anschließen
- `nachhallnah_ohne_kern`: Nachhallvorsprung ohne Kernnähe
- `anschlussnah`: Realwelt-Anschluss ohne klare Kernklassifikation

Damit gewinnt die Feldrollen-Memory Tiefe.
Sie speichert nicht mehr nur Familienbewegung über Phasen,
sondern zusätzlich die Art des Anschlusses gegen Realwelt/Nullwelt-Zwischenlagen.

## Einordnung

Das ist eine organische Erweiterung, weil sie aus wiederholten Befunden entsteht.
Die Schicht beschreibt, wie Feldrollen getragen werden.
Sie bestimmt nicht, was MINI_DIO tun soll.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob `attachment_quality` die Rollenbeschreibung messbar schärft:
gleiche Familien einmal nur mit alter Feldrollen-Memory lesen und einmal mit Anschlussqualität vergleichen.
