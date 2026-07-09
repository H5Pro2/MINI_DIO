# Synthetische stark permutierte Sequenz Nachhall-Synthese

Stand: 2026-06-22

## Zweck

Diese Synthese prueft die staerkste bisherige Sequenzgegenprobe.

Die `bruch_rand`-Phasen wurden nicht nur lokal vertauscht, sondern deutlich neu geordnet:

```text
randflackern -> zweite_rekopplung -> bruch_impuls -> ruhe_nachhall
-> oeffnung -> zweiter_kippimpuls -> rekopplung -> ruhig_vorlast -> gegenpol
```

Die Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Wird die Nachhallstruktur bei starker Permutation zerlegt?
2. Unterpruefung: Bleibt die globale Topologie stabil?
3. Unterpruefung: Veraendern sich lokale Phasenrollen durch fehlenden Vorlauf?
4. Folgeschritt: Zwischen robuster Topologie und lokaler Sequenzsensitivitaet unterscheiden.

## Forschungsbefund

| Welt | Kerzen | Episoden | Unique Syntax | Rekopplung | Carry | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|
| Original | 6100 | 6094 | 172 | 0.7461 | 0.5985 | 0.9043 |
| Stark permutiert | 6100 | 6094 | 173 | 0.7459 | 0.5983 | 0.9042 |

Befund:

- Top-Syntax-Ueberlappung bleibt `1.0`.
- Top-Familien-Ueberlappung bleibt `1.0`.
- Globale Rekopplung, Carry und Sinneskopplung bleiben fast gleich.
- Unique Syntax steigt nur minimal.

Die starke Permutation zerlegt die globale Ordnung nicht.

## Globale Topologie

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry |
|---|---:|---:|---:|---:|---:|
| Original | 0.9539 | 0.0456 | 0.0005 | 0.7461 | 0.5985 |
| Stark permutiert | 0.9539 | 0.0455 | 0.0007 | 0.7459 | 0.5983 |

Befund:

- Zentrum bleibt exakt auf demselben Niveau.
- Offenheit bleibt praktisch gleich.
- Rand/Kippnaehe steigt minimal.

Das ist ein starker Hinweis auf robuste MCM-Topologie:

```text
Die Rollenordnung uebersteht starke Sequenzveraenderung.
```

## Rezeptorachsen

| Welt | Zentrum | Offen | Rand/Kipp | High-Offen | High-Rand/Kipp |
|---|---:|---:|---:|---:|---:|
| Original | 0.8904 | 0.0711 | 0.0011 | 0.4508 | 0.0115 |
| Stark permutiert | 0.8869 | 0.0727 | 0.0015 | 0.4672 | 0.0148 |

Befund:

- Stark permutiert ist leicht offener.
- Hochlastfenster werden offener und randnaeher gelesen.
- Die Abweichung bleibt klein, aber konsistent.

## Lokaler Phasenbefund

Die wichtigste Veraenderung liegt am Beginn:

```text
randflackern steht ohne ruhigen Vorlauf am Anfang.
```

| Phase | Zentrum | Offen | Rekopplungsnaehe | Rand/Kipp | Rekopplung | Carry |
|---|---:|---:|---:|---:|---:|---:|
| Original randflackern | 0.2700 | 0.5186 | 0.2100 | 0.0014 | 0.6954 | 0.5151 |
| Stark permutiert randflackern | 0.1600 | 0.5729 | 0.2643 | 0.0029 | 0.6916 | 0.5057 |

Befund:

- `randflackern` wird ohne vorherige ruhige/oeffnende Sequenz deutlich offener.
- Zentrum sinkt stark.
- Rekopplungsnaehe steigt.
- Rand/Kippnaehe steigt leicht.

Das spricht fuer Sequenzsensitivitaet:

```text
Die gleiche Randphase wird anders gelesen,
wenn sie ohne vorbereitenden Vorlauf auftritt.
```

## Lokale Stabilisierung nach Randstart

Nach dem stark offenen Randstart werden spaetere Phasen schnell wieder zentrumsnah:

- `zweite_rekopplung`: Zentrum `0.9550`
- `bruch_impuls`: Zentrum `0.9500`
- `ruhe_nachhall`: Zentrum `0.9929`
- `oeffnung`: Zentrum `0.9943`
- `rekopplung`: Zentrum `0.9943`

Das ist wichtig:

```text
Die Sequenz startet lokal offener,
aber das Feld reorganisiert danach schnell zur Zentrumslage.
```

## MCM-Lesart

Die starke Permutation zeigt zwei Ebenen:

### Robuste Topologie

Die uebergeordnete MCM-Rollenordnung bleibt stabil.

```text
Zentrum
Offen
Rand/Kipp
Rekopplung
```

### Lokale Sequenzwirkung

Die konkrete Phase wird anders gelesen, wenn ihr Vorlauf anders ist.

```text
Rand am Anfang = offener, weniger zentriert
Rand nach Vorlauf = besser eingebettet
```

## Feldzeit-Folgerung

Feldzeit erscheint hier als Ordnungs- und Kontextspur:

```text
Nicht nur Dauer.
Nicht nur Reihenfolge.
Sondern: vorherige Feldorganisation beeinflusst,
wie eine aktuelle Weltphase aufgenommen wird.
```

Gleichzeitig bleibt die Topologie stabil:

```text
Feldzeit veraendert lokale Rollen,
aber zerlegt nicht automatisch die innere Gesamtordnung.
```

## Bedeutung fuer MINI_DIO

MINI_DIO zeigt in dieser Gegenprobe:

1. robuste globale Innenfeldordnung,
2. lokale Sequenzsensitivitaet,
3. schnelle Reorganisation nach stark offenem Start,
4. stabile Syntaxfamilien trotz anderer Reihenfolge.

Das ist fuer die weitere Forschung relevant:

```text
MINI_DIO speichert nicht einfach die Reihenfolge auswendig.
Es liest Weltphasen in einer stabilen Feldtopologie,
aber die lokale Bedeutung haengt vom zeitlichen Kontext ab.
```

## Grenze

Diese Pruefung ist weiterhin synthetisch.

Gesichert im aktuellen Test:

- starke Permutation zerlegt die globale Topologie nicht,
- `randflackern` wird ohne Vorlauf deutlich offener,
- nachfolgende Phasen reorganisieren schnell Richtung Zentrum.

Noch offen:

- vollstaendig zufaellige Reihenfolgen mit mehreren Wiederholungen,
- reale Sequenzbrueche,
- Messung, wie lange lokale Oeffnung nachwirkt.

## Schlussfolgerung

Die Nachhall-/Feldzeit-Mechanik wird dadurch klarer:

```text
Topologie ist robust.
Lokale Bedeutung ist sequenzsensitiv.
Nachhall wirkt als Kontextspur.
Das Feld kann nach offener Stoerung wieder organisieren.
```

## Wie es weitergeht

Als naechstes sollte die aktuelle Sequenzforschung nicht weiter fragmentiert werden. Sinnvoll ist ein zusammenfassender Forschungsstand: Feldzeit, Nachhall, Topologie und Rezeptoradaptation als ein gemeinsames MINI_DIO-Modell.
