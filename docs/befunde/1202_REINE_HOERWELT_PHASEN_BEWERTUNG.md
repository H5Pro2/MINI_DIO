# Befund 1202 - Bewertung der reinen Hoerwelt-Phasen

## Grundfrage

Nach Befund 1200 war klar, dass reine Hoervariation nicht einfach zu Kollaps fuehrt, sondern vor allem Uebergangsraum bildet.

Die konkrete Anschlussfrage war:

```text
Welche Hoerphase erzeugt welche Feldrolle?
```

## Datengrundlage

- Phasenreport: `docs/befunde/1201_REINE_HOERWELT_PHASEN_RUECKLESUNG.md`
- CSV: `docs/befunde/1201_REINE_HOERWELT_PHASEN_RUECKLESUNG.csv`
- Lauf: `debug/1199_pure_hearing/dio_mini_lauf_2/`
- Welt: `data/synthetic_mcm_pure_hearing_5m.csv`

## Kernergebnis

Die reine Hoerwelt trennt drei unterschiedliche Feldreaktionen:

| Hoerphase | Feldwirkung |
|---|---|
| ruhiger/leiser Ton | volle Zentrierung |
| steigender Ton | volle Zentrierung |
| fallender Ton | fast volle Zentrierung, minimale Randnaehe |
| pulsierender Ton | deutlicher Uebergangsraum |
| stiller Ton | fast volle Zentrierung |
| Doppelimpuls | Rand-/Kippnaehe und offene Variante |
| Schlussrekopplung | volle Zentrierung |

## Zahlenbefund

- `hoeren_pulsierend_form_stabil`
  - `offene_variante`: `0.1969`
  - `spannungsrand_kippnaehe`: `0.0000`
  - Rekopplung: `0.7142`
  - Carry: `0.5357`
  - Strain: `0.1674`

- `hoeren_doppelimpuls_form_stabil`
  - `offene_variante`: `0.0467`
  - `spannungsrand_kippnaehe`: `0.0458`
  - Rekopplung: `0.7483`
  - Carry: `0.5891`
  - Strain: `0.1433`

- `schluss_rekopplung`
  - `zentrum_stabil`: `1.0000`
  - Rekopplung: `0.7634`
  - Carry: `0.6228`
  - Strain: `0.1187`

## Interpretation

Die Hoerachse wirkt nicht nur ueber Lautheit. Entscheidend ist die zeitliche Struktur des Tons:

- Gleichmaessig steigende oder fallende Energie bleibt fuer das Feld tragbar.
- Pulsierende Energie oeffnet Uebergangsraum, ohne das Feld stark an den Rand zu treiben.
- Doppelimpuls erzeugt die klarste Rand-/Kippnaehe.
- Nach der Impulsphase kann das Feld wieder zentrumsnah rekoppeln.

Damit ist Hoeren im aktuellen MINI_DIO nicht nur ein Datenkanal, sondern eine zeitliche Stimulationsachse.

## MCM-Lesart

Die reine Hoerwelt stuetzt die Trennung:

```text
Hoeren = Energie / Ton / zeitliche Spannung
MCM-Feld = Integration, Uebergang, Randnaehe und Rueckfuehrung
```

Die wichtigste Beobachtung ist:

```text
Nicht die Hoerenergie allein entscheidet, sondern ihre Form ueber Zeit.
```

Das passt zur bisherigen Feldzeit-Lesart: Zeit erscheint im Feld nicht nur als Reihenfolge, sondern als gewirkte Energieform.

## Schlussfolgerung

MINI_DIO unterscheidet in der reinen Hoerwelt bereits:

- ruhige tonale Zentrierung,
- pulsierende Uebergangsbildung,
- impulsive Randnaehe,
- anschliessende Rekopplung.

Das ist fuer die weitere MCM-Forschung wichtig, weil es zeigt, dass die Hoerachse eine eigene Feldrolle tragen kann, ohne mit Sehen oder direktem Kontakt vermischt werden zu muessen.

## Wie es weitergeht

Als naechstes sollte diese Phasenruecklesung gegen die Desync-Teilwelten gelegt werden: Entsteht Rand/Kippnaehe dort aus Hoerimpuls allein oder erst aus Sinneswiderspruch zwischen stabiler Form und chaotischer Hoerachse?
