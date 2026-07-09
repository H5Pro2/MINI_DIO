# Synthetische Sinnesachsen Offen/Rand Bewertung

Stand: 2026-07-01

## Grundfrage

Entsteht `spannungsrand_kippnaehe` in den synthetischen Sinnesachsenwelten durch sichtbare Formzerstoerung oder durch Achsenlast im Feld?

Nach aktueller Sichtung: In den geprueften Beispielen eher durch Achsenlast, besonders Hoer-/Energiespannung.

## Gepruefte Fenster

Die Chartfenster liegen in:

- `docs/befunde/1001-2000/1001-1500/1231_SYNTHETISCHE_SINNESACHSEN_OFFEN_RAND_CHARTFENSTER.md`

Sie zeigen die staerksten direkten Uebergaenge:

- `offene_variante -> spannungsrand_kippnaehe`
- `spannungsrand_kippnaehe -> offene_variante`

## Befund

Die auffaelligsten Fenster zeigen keine klare visuelle Trendlogik.

Stattdessen liegt der Rollensprung an Stellen, an denen die sichtbare Form relativ geordnet bleiben kann, waehrend die Spannungsbreite stark zunimmt. Das passt zu den Segmentwerten:

```text
SYNTH_VISUAL_STABLE_HEARING_CHAOTIC:
  Rand/Kipp avgLoud 0.8361
  Rand/Kipp avgStrain 0.2844

SYNTH_VISUAL_CHAOTIC_HEARING_STABLE:
  Rand/Kipp nicht vorhanden
```

Damit ist die wahrscheinlichere Lesart:

```text
Rand/Kipp wird hier nicht durch visuelles Chaos getragen,
sondern durch Hoer-/Energiebelastung bei weiter lesbarer Form.
```

## Bedeutung fuer MINI_DIO

Das stuetzt die aktuelle Trennung:

- Sehen liest Form und Struktur.
- Hoeren liest Energie, Lautheit und Spannung.
- Rezeptorkontakt bestimmt, wie stark diese Achsen ins Feld gelangen.
- Das MCM-Feld bildet daraus Rollen.

Wichtig: Diese Rollen sind keine Strategie. Sie sind passive Feldantworten auf Sinnesachsen.

## Grenze

Die synthetischen Welten sind konstruiert. Sie zeigen Kanalwirkung unter kontrollierter Belastung, aber noch keine allgemeine Aussage ueber alle realen Welten.

Der aktuelle Befund ist deshalb stark fuer die Mechanik der Sinnestrennung, aber nicht als vollstaendige Weltrobustheit zu lesen.
