# MCM-Brueckenkerne Zielrollen Vergleich

## Zweck

Diese Notiz vergleicht den zentralen Brueckenkern mit den beiden sekundaeren Brueckenkernen.
Ziel ist zu pruefen, ob alle Kerne gleich funktionieren oder ob der zentrale Kern eine Sonderrolle im MCM-Feld einnimmt.

## Verglichene Kerne

| Kern | Klasse aus 876 | Besonderheit |
|---|---|---|
| `0e7qvj1` / `18l3thm` | zentraler_brueckenkern | staerkster Rueckbezug, Gewicht 84 |
| `0db07p4` / `1joiyc3` | sekundaerer_brueckenkern | eigenstaendiger stabiler Anschlusskern |
| `0e7qvj1` / `0mji3u6` | sekundaerer_brueckenkern | Seitenarm des zentralen Kerns, weil `0e7qvj1` beteiligt ist |

## Zielrollen

### Zentraler Kern `0e7qvj1` / `18l3thm`

Austritte vom Kern nach Pfadklasse:

| Pfadklasse | Gewicht |
|---|---:|
| stabile_insel | 21 |
| brueckenpfad | 12 |
| rekoppelnder_pfad | 8 |
| unbekannt | 7 |
| junge_oberflaeche | 1 |
| randpfad | 1 |

Staerkste Zielzone:

```text
stabile_bedeutungsinsel: 33
```

### Sekundaerer Kern `0db07p4` / `1joiyc3`

Austritte vom Kern nach Pfadklasse:

| Pfadklasse | Gewicht |
|---|---:|
| stabile_insel | 17 |
| unbekannt | 7 |
| junge_oberflaeche | 1 |
| randpfad | 1 |

Staerkste Zielzone:

```text
stabile_bedeutungsinsel: 17
```

### Sekundaerer Kern `0e7qvj1` / `0mji3u6`

Austritte vom Kern nach Pfadklasse:

| Pfadklasse | Gewicht |
|---|---:|
| brueckenpfad | 46 |
| rekoppelnder_pfad | 8 |
| unbekannt | 7 |
| stabile_insel | 6 |
| junge_oberflaeche | 1 |
| randpfad | 1 |

Staerkste Zielzone:

```text
stabile_bedeutungsinsel: 52
```

## Befund

Alle drei Kerne fuehren kaum direkt in Randpfade.
Rand erscheint also nicht als Hauptziel der Brueckenkerne.

Der zentrale Kern `0e7qvj1` / `18l3thm` zeigt die breiteste Anschlussstruktur:

```text
stabile Insel,
Brueckenpfad,
Rekopplung,
wenig Rand,
wenig junge Oberflaeche.
```

Der sekundaere Kern `0db07p4` / `1joiyc3` wirkt enger:

```text
stabile Insel als Hauptanschluss,
weniger Brueckenweiterleitung.
```

Der sekundaere Kern `0e7qvj1` / `0mji3u6` ist kein unabhaengiger Kern im strengen Sinn.
Er wirkt eher wie ein Seitenarm des zentralen Kerns, weil `0e7qvj1` selbst Teil des zentralen Kerns ist.
Sein starkes Brueckenpfad-Gewicht kommt wesentlich daher, dass er wieder an `18l3thm` gekoppelt ist.

## Interpretation

Die Brueckentopologie wirkt nicht flach und nicht beliebig.
Sie wirkt hierarchisch:

```text
zentraler Kern:
0e7qvj1 / 18l3thm

sekundaerer stabiler Anschlusskern:
0db07p4 / 1joiyc3

Seitenarm des zentralen Kerns:
0e7qvj1 / 0mji3u6
```

Der zentrale Kern vermittelt am staerksten zwischen Bruecke, stabiler Bedeutung und Rekopplung.
Er wirkt nicht wie ein Randkanal und nicht wie chaotische Oeffnung.
Er wirkt eher wie ein geordneter Uebergangs- und Anschlussbereich.

## Bedeutung Fuer Die MCM-Lesart

Die bisherigen Befunde lassen sich damit praezisieren:

```text
MCM-Bruecken sind nicht nur Kanten.
Ein Teil der Bruecken organisiert sich zu Kernen.
Ein Kern kann zentrale und sekundaere Anschlussrollen tragen.
```

Damit bekommt die MCM-Topologie eine weitere Ebene:

```text
Inseln
Randbereiche
Rekopplungszonen
Bruecken
Brueckenkerne
Bruecken-Seitenarme
```

## Wie es weitergeht

Als naechstes sollte diese Kernstruktur gegen stabile Inseln und Randpfade gelegt werden.
Ziel: pruefen, ob der zentrale Brueckenkern wirklich zentrumsnah arbeitet oder ob er nur durch stabile Inseln zentrumsnah erscheint.
