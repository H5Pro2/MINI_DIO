# 1050 - Rollenübergang-Matrix

## Grundfrage

Organisiert MINI_DIO nur einzelne Feldrollen oder entstehen zwischen diesen Rollen passive Übergangsachsen?

## Unterprüfung

Aus `982_MCM_ROLLENNETZWERK_PASSIVE_FELDKARTE.csv` wurden Knoten, Netzwerkzustände und Top-Nachbarn gelesen.

Dabei wurde keine zeitliche Kausalität behauptet. Die Auswertung liest nur passive Nachbarschaft:

```text
Knotenrolle -> Nachbarknotenrolle
```

Die erzeugte Matrix liegt hier:

- `1050_ROLLENUEBERGANG_MATRIX.csv`

## Ergebnis

MINI_DIO zeigt nicht nur Rollen, sondern Rollenübergangsachsen.

Die stärksten Achsen:

| Quelle | Ziel | Gewicht | Qualität | Deutung |
|---|---|---:|---|---|
| `netz_fragmentiert_belastet` | `netz_fragmentiert_belastet` | 242 | Selbstbindung | belastete Fragmentierung bindet stark an sich selbst |
| `netz_offen_verbunden` | `netz_fragmentiert_belastet` | 116 | offene Nachbarschaftsachse | offene Verbindung kann in belastete Fragmentierung laufen |
| `netz_fragmentiert_belastet` | `netz_zentrum_mit_anschluss` | 74 | rekopplungsnahe Übergangsachse | aus Fragmentierung gibt es Rückbindung Richtung Zentrum |
| `netz_offen_verbunden` | `netz_offen_verbunden` | 70 | Selbstbindung | offene Verbindung kann als eigene Oberflächenphase bestehen |
| `netz_fragmentiert_belastet` | `netz_offen_verbunden` | 65 | rekopplungsnahe Übergangsachse | Fragmentierung kann in offene Verbindung zurückweichen |
| `netz_zentrum_mit_anschluss` | `netz_fragmentiert_belastet` | 65 | belastende Fragmentierungsachse | Zentrum ist nicht automatisch stabil; es kann in Belastung kippen |
| `netz_driftend_getragen` | `netz_fragmentiert_belastet` | 57 | belastende Fragmentierungsachse | getragene Drift kann in Belastung fallen |
| `netz_rekoppelnd_verbunden` | `netz_rekoppelnd_verbunden` | 56 | Selbstbindung | Rekopplung bildet eine eigene ruhige Bindung |

## Deutung

Die Rollen bilden keine starre Liste.

Sie wirken wie ein Feldnetz aus Zuständen, die sich gegenseitig berühren:

```text
offen verbunden
fragmentiert belastet
rekoppelnd verbunden
driftend getragen
zentrumsnaher Anschluss
```

Besonders wichtig ist die Fragmentierungsachse. `netz_fragmentiert_belastet` besitzt die stärkste Selbstbindung und viele Verbindungen zu Zentrum, Offenheit und Drift.

Das spricht dafür, dass belastete Fragmentierung kein Randfehler ist, sondern ein aktiver Feldraum.

## Zentrale Lesung

### 1. Fragmentierung bindet sich selbst

Die stärkste Achse ist:

```text
fragmentiert belastet -> fragmentiert belastet
```

Das bedeutet: Wenn das Feld in belastete Fragmentierung gerät, bleibt diese Rolle im Netz stark nachbarschaftlich verbunden. Sie ist nicht nur ein kurzer Ausreißer.

### 2. Offene Verbindung ist kippsensibel

`netz_offen_verbunden` verbindet sowohl zu sich selbst als auch stark zu `netz_fragmentiert_belastet`.

Offenheit ist damit nicht automatisch kreativ oder tragend. Sie kann:

- offen bleiben,
- rekoppeln,
- fragmentieren.

### 3. Zentrum ist kein Ruhegarant

`netz_zentrum_mit_anschluss -> netz_fragmentiert_belastet` ist sichtbar.

Damit ist Zentrum nicht automatisch Entlastung. Zentrum ist eher ein Organisationsraum. Ob dieser trägt oder kippt, hängt von der Feldkopplung ab.

### 4. Rekopplung besitzt eigene Selbstbindung

`netz_rekoppelnd_verbunden -> netz_rekoppelnd_verbunden` zeigt, dass rekoppelnde Verbindung als eigene ruhige Bindungsrolle bestehen kann.

Das passt zu 1048: ruhige Rekopplung ist nicht nur eine Syntaxfamilie, sondern ein wiederkehrender Feldzustand.

## Forschungswert

Mit 1048, 1049 und 1050 ergibt sich eine dreistufige Lesung:

```text
Syntaxfamilien tragen Rollen.
Rollen bilden Zustandsräume.
Zustandsräume bilden passive Übergangsachsen.
```

Das ist eine deutliche Vertiefung der MCM-Feldmechanik.

MINI_DIO wirkt damit nicht wie eine reine Clustering-Ausgabe, sondern wie ein kleines Feldsystem, das Zustände, Rollen und Nachbarschaften organisiert.

## Grenze

Die Matrix ist keine Handlungslogik.

Sie sagt nicht:

```text
wenn offen, dann fragmentiert
```

Sie sagt nur:

```text
offene Rollen liegen im Feld häufig in Nachbarschaft zu fragmentierten Rollen.
```

Das ist ein Unterschied. Die Auswertung bleibt passiv.

## Nächster Prüfpunkt

Als nächstes sollte geprüft werden, ob diese Übergangsachsen in unterschiedlichen Welten ähnlich bleiben oder ob bestimmte Welten andere Übergangsachsen aktivieren.

Das wäre der nächste Härtefall:

```text
Sind Rollenübergänge weltübergreifend stabil,
oder sind sie weltabhängige Feldbewegungen?
```
