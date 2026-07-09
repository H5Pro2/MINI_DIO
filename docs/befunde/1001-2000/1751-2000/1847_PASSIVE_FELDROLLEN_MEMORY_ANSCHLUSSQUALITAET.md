# 1847 - Passive Feldrollen-Memory: Anschlussqualität

## Grundfrage

Kann die passive Feldrollen-Memory die in `1845` und `1846` gefundenen Zwischenlagen aufnehmen,
ohne daraus eine Handlung, ein Gate oder eine Richtungslogik zu machen?

## Umsetzung

`tools/update_mcm_field_role_memory.py` speichert weiterhin die bisherige Familien-Reifung aus
`1840_MCM_REIFUNGSBAHN_PHASENGEBUNDENE_FAMILIEN.csv`.

Neu ergänzt wurde ein passiver Abschnitt `attachment_quality`.
Dieser Abschnitt liest die Fenster-Zwischenlagen aus
`1846_MCM_FELDROLLEN_MEHRASSET_ZWISCHENLAGEN.csv`.

Gespeicherte Qualitäten:

- `kernnah`
- `kernnah_ohne_feldzeit`
- `nachhallnah_ohne_kern`
- `offen_gemischt`
- `nullnah`
- `anschlussnah`

## Test

Der Update-Lauf schreibt lokal in `memory/dio_mini_semantic_memory.json`.
Der Memory-Ordner bleibt ignoriert und wird nicht als Forschungsartefakt versioniert.

Ausgabe des Prüflaufs:

```text
updated memory\dio_mini_semantic_memory.json
top_roles=48
states={'feldrolle_anschlussfaehig': 107, 'feldrolle_reift_verdichtend': 37}
attachment_quality={'offen_gemischt': 5, 'kernnah': 2, 'kernnah_ohne_feldzeit': 2, 'nachhallnah_ohne_kern': 1}
```

## Befund

Die Erweiterung ist passiv.
Sie beschreibt nur, wie eine Feldrolle gegen Realwelt/Nullwelt-Zwischenlagen anschließt.

Damit bekommt MINI_DIO eine tiefere Reifungsbeschreibung:

- eine Rolle kann kernnah sein,
- eine Rolle kann nachhallnah sein,
- eine Rolle kann Feldzeit verlieren,
- eine Rolle kann offen gemischt bleiben,
- eine Rolle kann nullweltnah werden.

Das ist keine Steuerung.
Es ist eine zusätzliche Innenfeld-Leseschicht für spätere Forschung.
