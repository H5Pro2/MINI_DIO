# Lokale Feld-Episoden-Vorschau - Befund

Stand: 2026-06-19

## Kurzbefund

Die leere lokale `mcm_field_episode_symbol`-Spur hatte eine technische und fachliche Ursache:

`mcm_field_episode_symbol` wurde bisher nur geschrieben, wenn der passive EpisodeTracker eine Episode abschliesst.

Lokale Fenster betrachten aber viele Ticks innerhalb einer noch laufenden Episode.
Darum stand dort haeufig `-`.

## Änderung

MINI_DIO schreibt nun zusaetzlich pro Tick eine passive Vorschau:

```text
mcm_field_episode_preview_symbol
```

Diese Vorschau:

- schliesst keine Episode ab,
- schreibt nichts ins Memory,
- beeinflusst keine Handlung,
- ist kein Gate,
- ist kein Entry-Signal,
- macht nur die aktuell entstehende Feld-Episodensprache lokal lesbar.

## Bedeutung

Damit werden zwei Ebenen getrennt:

1. `mcm_field_episode_symbol`  
   Eine abgeschlossene Feld-Episode wurde wirklich gespeichert.

2. `mcm_field_episode_preview_symbol`  
   Eine Feld-Episode ist gerade im Entstehen und kann lokal gelesen werden.

Das ist fachlich sauberer als die bisherige Diagnose, weil lokale multisensorische Fenster nicht warten muessen, bis eine Episode schliesst.

## Kritische Grenze

Die Vorschau ist noch keine gereifte Bedeutung.

Sie zeigt nur:

```text
So sieht die aktuell entstehende Feld-Episode aus.
```

Erst wenn dieselbe Vorschau wiederkehrt, spaeter abgeschlossen wird und im Memory stabil auftaucht, kann man von gereifter Feld-Episodenverdichtung sprechen.

## Technische Verifikation

Ein kurzer Testlauf hat bestaetigt:

```text
mcm_field_episode_symbol         -> bleibt oft "-" bis zum Episodenabschluss
mcm_field_episode_preview_symbol -> ist pro Tick gefuellt
```

Beispielhafte Top-Vorschauen aus dem Testlauf:

- `dio_mcm_episode_02xikfk`
- `dio_mcm_episode_1eik02d`
- `dio_mcm_episode_037i64j`

Damit ist die lokale Feldsprache nun im Debug sichtbar, ohne die Memory-Schreibung vorzuziehen.

## Wie es weitergeht

Als naechstes braucht es einen neuen Lauf oder eine neue Forschungskette, damit `mcm_field_episode_preview_symbol` in frischen `episodes.csv`-Dateien vorhanden ist.

Danach wird die lokale multisensorische Syntaxdiagnose erneut ausgefuehrt.
Dann kann geprueft werden, ob lokale Kipp- und Rekopplungsfenster eigene Feld-Episoden-Vorschau-Sprache tragen.
