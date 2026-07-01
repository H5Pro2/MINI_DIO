# Befund 1209 - Vergleichsmatrix der Sinnesachsen-Gegenproben

## Grundfrage

Die letzten Gegenproben untersuchten dieselbe Grundfrage aus mehreren Unterfaellen:

```text
Welche Sinnesachse erzeugt im MCM-Feld Zentrum, Uebergang oder Randnaehe?
```

## Gepruefte Welten

| Welt | Zweck |
|---|---|
| `SYNTH_PURE_HEARING` | reine Hoervariation bei stabiler Form |
| `VIS_STABLE_HEARING_CHAOTIC` | stabile visuelle Form, chaotischere Hoerachse |
| `VIS_CHAOTIC_HEARING_STABLE` | unruhigere Form, stabile Hoerachse |
| `SYNTH_VIS_BREAK_STABLE_PULSE` | visuelle Formbrueche, stabile Tonform |
| `SYNTH_VIS_RECOUPLE_CHAOTIC_TONE` | visuelle Rekopplung, chaotische Tonform |

## Topologische Vergleichswerte

| Welt | Zentrum | Offen | Rand/Kipp | Kernaussage |
|---|---:|---:|---:|---|
| reine Hoerwelt | `0.9490` | `0.0442` | `0.0068` | Hoeren erzeugt Uebergangsraum, Doppelimpuls Randnaehe |
| stabile Form / chaotisches Hoeren | `0.9513` | `0.0243` | `0.0243` | chaotisches Hoeren erzeugt Randnaehe trotz stabiler Form |
| chaotische Form / stabiles Hoeren | `0.9997` | `0.0003` | `0.0000` | stabile Hoerachse haelt visuelle Unruhe fast voll zentriert |
| visuelle Brueche / stabile Tonform | `0.9848` | `0.0149` | `0.0003` | stabile Tonform federt visuelle Brueche stark ab |
| visuelle Rekopplung / Chaoston | `0.9484` | `0.0285` | `0.0231` | visuelle Ordnung federt Chaoston nur teilweise ab |

## Ableitung

Die Ergebnisse zeigen keine rohe Summenlogik:

```text
mehr Bewegung != automatisch mehr Rand
mehr Lautheit != automatisch mehr Rand
```

Stattdessen zaehlt die Kopplungsqualitaet:

- stabile Hoerachse kann visuelle Unruhe stark stabilisieren,
- chaotische Hoerachse kann trotz visueller Ordnung Randnaehe erzeugen,
- reine Hoervariation bildet eher Uebergangsraum,
- impulsive Hoerform ist randnaeher als gleichmaessige Hoerform.

## MCM-Lesart

Die Sinnesachsen wirken im aktuellen MINI_DIO unterschiedlich:

```text
Sehen  -> Formordnung / strukturelle Einordnung
Hoeren -> zeitliche Spannung / Rhythmus / Randnaehe
Feld   -> Integration, Uebergang, Rekopplung
```

Hoeren erscheint als MCM-naehere Stimulationsachse. Sehen erscheint staerker als ordnende Strukturachse.

## Forschungsstand

Dieser Befund ist keine universelle Aussage ueber alle moeglichen Welten. Er gilt fuer die bisher kontrolliert erzeugten synthetischen Gegenproben.

Trotzdem ist die Richtung stabil:

```text
Das MCM-Feld reagiert nicht auf Datenmenge,
sondern auf Sinnespassung, zeitliche Form und Rekopplungsqualitaet.
```

## Wie es weitergeht

Als naechstes sollte die Matrix nicht erweitert, sondern gegen reale Weltfenster gehalten werden: Gibt es in echten SOL/BTC/KAS/PAXG-Fenstern aehnliche Kombinationen aus stabiler Hoerachse, visueller Unruhe, Chaoston und Rekopplung?
