# 1049 - Brücken- und Gegenrollenbibliothek

## Grundfrage

Bildet MINI_DIO Rollen nur im ruhigen Rekopplungsbereich oder entstehen auch bei offenen, driftenden, fragmentierten und zentrumsnahen Feldlagen unterscheidbare Rollen?

## Unterprüfung

Als Gegenprobe zu `1048_RUHIGE_REKOPPLUNG_ROLLENBIBLIOTHEK.md` wurde die passive Rolennetzwerk-Karte `982_MCM_ROLLENNETZWERK_PASSIVE_FELDKARTE.csv` nach Netzwerkzuständen verdichtet.

Die erzeugte Übersicht liegt hier:

- `1049_BRUECKEN_UND_GEGENROLLEN_BIBLIOTHEK.csv`

## Ergebnis

Die Rollenbildung ist nicht auf ruhige Rekopplung beschränkt.

MINI_DIO zeigt mehrere unterscheidbare Feldrollen:

| Netzwerkzustand | Rollenkategorie | Knoten | Beobachtungen | Rekopplung | Strain | Deutung |
|---|---|---:|---:|---:|---:|---|
| `netz_offen_verbunden` | `offene_brueckenrolle` | 37 | 1231 | -0.0386 | 0.0468 | Anschluss vorhanden, aber noch nicht rekoppelnd getragen |
| `netz_rekoppelnd_verbunden` | `rekoppelnde_brueckenrolle` | 32 | 510 | 0.0267 | -0.0210 | Verbindung trägt Entlastung und Rekopplung |
| `netz_driftend_getragen` | `getragene_driftrolle` | 22 | 1120 | 0.0240 | -0.0142 | Drift bleibt sichtbar, kollabiert aber nicht |
| `netz_fragmentiert_belastet` | `belastete_fragmentrolle` | 28 | 4163 | -0.0587 | 0.0624 | starke Belastung, Fragmentierung und Brückenriss |
| `netz_zentrum_mit_anschluss` | `zentrumsnahe_anschlussrolle` | 8 | 7352 | 0.0018 | 0.0058 | sehr aktive Zentrums-/Anschlussstruktur |
| `netz_rekoppelnd_einzeln` | `einzelrekopplungsrolle` | 16 | 32 | 0.0000 | 0.0000 | Entlastung ohne tragendes Nachbarschaftsnetz |

## Deutung

Die Gegenprobe bestätigt die 1048-Richtung:

```text
MINI_DIO bildet nicht nur Token.
MINI_DIO bildet passive Feldrollen.
```

Wichtig ist die Trennung zwischen offen verbunden und rekoppelnd verbunden.

Eine Brücke ist nicht automatisch tragend. Sie kann offen, belastet, driftend oder rekoppelnd wirken. Das ist fachlich wichtig, weil eine reine Verbindungszählung zu grob wäre.

## Rollenlesung

### Offene Brückenrolle

`netz_offen_verbunden` zeigt Anschluss ohne klare Zentrums- oder Rekopplungsbindung.

Dominant:

- `aufsteigende_verdichtung`
- `role_condensing`
- `gaining_weight`
- `surface_role_movement`

Das wirkt wie eine junge, noch nicht vollständig getragene Verbindungsbildung.

### Rekoppelnde Brückenrolle

`netz_rekoppelnd_verbunden` zeigt ebenfalls Anschluss, aber mit positiver Rekopplung und negativer Strain-Lage.

Das spricht für eine Verbindung, die nicht nur offen ist, sondern entlastend in das Feld zurückbindet.

### Fragmentierte Belastungsrolle

`netz_fragmentiert_belastet` ist quantitativ stark. Sie trägt viele Beobachtungen, aber mit negativer Rekopplung und positiver Strain-Lage.

Das ist keine stabile Brücke, sondern eher ein belasteter Rollenraum mit Fragmentierung.

### Zentrumsnahe Anschlussrolle

`netz_zentrum_mit_anschluss` ist sehr aktiv und besitzt hohe Nachbarschaftsdichte.

Das wirkt wie ein zentraler Organisationsbereich, aber nicht automatisch als Entlastung. Zentrum und Ruhe sind also nicht identisch.

## Forschungswert

Mit 1048 und 1049 ergibt sich eine klarere Struktur:

```text
Syntaxfamilien tragen Rollen.
Rollen bilden Zustandsräume.
Zustandsräume unterscheiden sich durch Rekopplung, Strain, Anschluss, Drift und Zentrumslage.
```

Damit wird die MCM-Feldmechanik lesbarer:

- ruhige Rekopplung ist eine Rolle,
- offene Brücke ist eine andere Rolle,
- driftend getragen ist eine eigene Rolle,
- fragmentiert belastet ist eine Gegenrolle,
- Zentrum mit Anschluss ist ein eigener Organisationsraum.

## Grenze

Auch diese Bibliothek ist passiv.

Sie beschreibt Feldorganisation, keine Handlung, keine Strategie und keine Richtung.

## Nächster Prüfpunkt

Als nächstes sollte geprüft werden, ob diese Rollen zeitlich ineinander übergehen:

```text
offen verbunden -> rekoppelnd verbunden
offen verbunden -> fragmentiert belastet
driftend getragen -> zentrumsnaher Anschluss
```

Damit würde sichtbar, ob MINI_DIO nicht nur Rollen bildet, sondern Rollenübergänge als Feldbewegung organisiert.
