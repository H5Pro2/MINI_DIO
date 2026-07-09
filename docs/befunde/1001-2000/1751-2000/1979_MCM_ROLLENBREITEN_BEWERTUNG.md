# 1979 - MCM-Rollenbreiten-Metrik

## Grundfrage

Kann MINI_DIO passive Bedeutungsrollen nicht nur benennen, sondern nach Feldbreite unterscheiden?

## Unterprüfung

Es wurde ein passives Diagnosewerkzeug ergänzt:

- `tools/report_mcm_role_breadth_metric.py`

Das Tool liest vorhandene Preview-Anker aus der Memory und bewertet sie nach:

- Wiederkehr
- Weltanzahl
- Verteilung über Weltmilieus
- Top-Welt-Dominanz
- Quiet-/Stress-/Shift-Anteilen
- Spezifität gegen Breite

Wichtig: Die Metrik verändert keine Feldmechanik. Sie liest nur vorhandene Memory.

## Ergebnis

Die Rollenbreite trennt die zuletzt untersuchten Rollen sinnvoll:

### Breite Grundrollen

`dio_mcm_episode_0icnf2v`

- Count: `76574`
- Welten: `32`
- Lesart: `breite_grundrolle`
- Breite-Score: `0.905104`

`dio_mcm_episode_1rj8742`

- Count: `15161`
- Welten: `33`
- Lesart: `breite_grundrolle`
- Breite-Score: `0.928350`
- Übergangs-Score: `0.614724`

`1rj8742` bleibt damit zwar stark übergangsfähig, ist aber nicht eng genug, um nur als Übergangsrolle gelesen zu werden.

### Milieurolle

`dio_mcm_episode_1i3ov0z`

- Count: `2073`
- Welten: `11`
- Lesart: `milieurolle`
- Milieu-Score: `0.617828`
- Quiet-Anteil: `0.878919`

Damit bestätigt die Metrik die vorige Deutung: `1i3ov0z` ist keine breite Grundrolle, sondern eine engere BTC-Quiet-Milieubildung.

### Nebenrolle

`dio_mcm_episode_12fuh1y`

- Count: `20`
- Welten: `12`
- Lesart: `nebenrolle`
- Nebenrollen-Score: `0.537635`

Damit bleibt `12fuh1y` eine kleine, noch nicht tragend verdichtete Nebenrolle.

### Übergangsrolle

In der Top-Auswertung erscheint `dio_mcm_episode_0wo0tz1` als Übergangsrolle:

- Count: `4119`
- Welten: `24`
- Übergangs-Score: `0.799`

Das passt zur vorherigen Beobachtung, dass manche Rollen nicht ein einzelnes Milieu repräsentieren, sondern Übergänge zwischen Feldlagen tragen.

## Befund

MINI_DIO kann mit dieser Diagnose in vier passive Rollenbreiten gelesen werden:

1. Grundrolle: breite, weltübergreifende Funktion.
2. Übergangsrolle: Brücke zwischen Milieus oder Feldlagen.
3. Milieurolle: spezifische, stark gebundene Lage.
4. Nebenrolle: kleine oder unreife Bedeutung.

Das ist ein wichtiger Schritt weg von bloßer Symbolzählung. Die gleiche Symbolhäufigkeit reicht nicht aus. Entscheidend ist, wie breit oder spezifisch eine Rolle im Feld getragen wird.

## Bedeutung für MCM-Feldentwicklung

Die MCM-Ordnung bekommt dadurch mehr Tiefe:

- ein Symbol kann häufig sein, aber trotzdem unspezifisch
- ein Symbol kann kleiner sein, aber ein klares Milieu tragen
- Brückenrollen können zwischen Zuständen vermitteln
- Nebenrollen können spätere Reifekandidaten sein

Damit wird MINI_DIO nicht härter programmiert, sondern besser lesbar. Die organische Erweiterung liegt in der Diagnosefähigkeit: Rollenbreite wird sichtbar.

## Grenze

Die Lesart ist eine Forschungsdiagnose. Sie ist keine endgültige Taxonomie und keine Handlungslogik.
