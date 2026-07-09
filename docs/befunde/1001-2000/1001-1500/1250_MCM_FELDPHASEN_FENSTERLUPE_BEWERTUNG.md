# MCM-Feldphasen Fensterlupe Bewertung

Stand: 2026-07-02

## Grundfrage

Was zeigt die Fensterlupe ueber situative Rand-/Kipp-Phasen im MCM-Feld?

## Ergebnis

Die Diagnose `1249_MCM_FELDPHASEN_FENSTERLUPE` fand `2655` konkrete Drei-Phasen-Fenster ueber `10` Zielphasenfamilien.

Die dominante Lesart ist:

```text
Rand/Kipp ist in den meisten Faellen kein dauerhafter Kollaps,
sondern ein kurzer Lastkontakt mit anschliessender Entlastung.
```

## Zentrale Zahlen

- `2077` Fenster: `lastkontakt_entlastet`
- `184` Fenster: `rekopplung_vor_neuer_last`
- `168` Fenster: `rekopplung_bricht_in_last`
- `145` Fenster: `gemischtes_fenster`
- `78` Fenster: `rekopplung_nimmt_zu`
- `3` Fenster: `lastkontakt_bleibt`

Die groesste Phase:

```text
offene_variante -> spannungsrand_kippnaehe -> offene_variante
```

zeigt:

- `1341` Fenster
- mittlere Rekopplung in der Randphase: `0.5910`
- mittlerer Strain in der Randphase: `0.2819`
- Folge-Delta Rekopplung: `+0.0609`
- Folge-Delta Strain: `-0.0942`

Das ist fachlich wichtig: Die Randphase erzeugt Spannung, aber die Folgebewegung entlastet.

## Unterformen

### 1. Lastkontakt mit Entlastung

Das ist die Hauptform.

Lesart:

```text
Das Feld beruehrt Rand/Kipp.
Danach steigt Rekopplung.
Danach faellt Strain.
```

Diese Form wirkt wie ein belastender Kontakt, der wieder in Offenheit, Zentrum oder Rekopplung zurueckfindet.

### 2. Rekopplung vor neuer Last

Beispiel:

```text
spannungsrand_kippnaehe -> zentrum_stabil -> spannungsrand_kippnaehe
```

Diese Form zeigt:

- Rekopplung hoch in der Mitte
- danach Rekopplung faellt
- Strain steigt wieder

Lesart:

```text
Das Feld findet kurz Zentrum,
wird danach aber erneut an den Rand gezogen.
```

Das ist keine Entlastungsphase, sondern eine Rueckfall- oder Wiederbelastungsform.

### 3. Gemischtes Fenster

Diese Form ist noch nicht eindeutig.

Sie kann bedeuten:

- kurze Rekopplung ohne klare Entlastung,
- Zwischenphase,
- oder unzureichend aufgeloeste Segmentierung.

## Bedeutung fuer MINI_DIO

Die MCM-Feldbewegung wirkt nicht wie ein statischer Zustand.

Wichtiger als der Einzelzustand ist die Folge:

```text
Was macht das Feld nach dem Kontakt?
```

Daraus entsteht eine stabilere Lesart:

- Rand/Kipp allein ist nicht automatisch negativ.
- Zentrum allein ist nicht automatisch stabil, wenn danach neue Randlast folgt.
- Offenheit nach Rand/Kipp ist oft entlastend.
- Rekopplung kann entweder Entlastung oder Vorbereitung neuer Last sein.

## Methodische Grenze

Die Fensterlupe liest Feldphasen-Segmente, nicht direkt rohe Kerzenfenster.

Damit ist bestaetigt:

```text
Die MCM-Feldfolge ist strukturiert lesbar.
```

Noch nicht bestaetigt ist:

```text
Welche konkrete Rohweltbewegung jede dieser Feldfolgen ausloest.
```

Dafuer braucht es eine naechste Lupe mit direkter Kopplung:

- Phase,
- Weltfenster,
- Kerzenbereich,
- Ton-/Energieprofil,
- Rezeptorprofil,
- Feldfolge.

## Schluss

Die Rand-/Kipp-Phasen zeigen eine differenzierte Feldlogik.

Sie sind nicht einfach Chaosrand.

Sie koennen sein:

- entlastender Lastkontakt,
- Rueckfall nach kurzer Stabilisierung,
- gemischte Zwischenphase,
- oder junge/driftende Spur.

Das stuetzt die bisherige MCM-Lesung: Die Topologie ist nicht nur Raumordnung, sondern Bewegungsordnung.
