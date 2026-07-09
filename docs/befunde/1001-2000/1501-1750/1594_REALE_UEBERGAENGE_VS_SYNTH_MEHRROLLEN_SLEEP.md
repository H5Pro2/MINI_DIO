# Reale Uebergaenge Gegen Synthetische Mehrrollennaehe

Stand: 2026-07-06

## Grundfrage

Unterscheidet sich Offline-Feld-Reorganisation zwischen fokussierten realen Uebergangsfenstern und breiter synthetischer Mehrrollennaehe?

## Unterpruefung

Verglichen wurden drei Real-Sleep-Real-Reproduktionen:

- `SYNTH_RAND_KIPP start0 size2000`
- `RUHIG_SIDEWAYS_2026 start6000 size2000`
- `EXPANSION_POSITIV_2023 start2000 size2000`

Alle Laeufe nutzten frisches Memory, dieselbe Welt als Real A und Real B sowie dieselbe passive Sleep-Reorganisation.

## Ergebnis Im Vergleich

| Welt | Rollen | Kombinationen | Rollen reaktiviert | Kombinationen voll | Kombinationen teilweise | Sleep-Zustand |
|---|---:|---:|---:|---:|---:|---|
| SYNTH_RAND_KIPP start0 | 5 | 10 | 4 / 5 | 6 / 10 | 4 / 10 | sleep_rekopplung |
| RUHIG_SIDEWAYS_2026 start6000 | 3 | 3 | 3 / 3 | 3 / 3 | 0 / 3 | sleep_rekopplung |
| EXPANSION_POSITIV_2023 start2000 | 3 | 3 | 3 / 3 | 3 / 3 | 0 / 3 | sleep_rekopplung |

Alle drei Welten waren in Real A und Real B reproduzierbar. Die Top-Syntax- und Top-Familien-Ueberlappung lag jeweils bei `1.0`.

## Lesung

Die reale Doppelpruefung bestaetigt:

```text
Fokussierte reale Uebergangsfenster rekoppeln offline vollstaendig.
Breitere synthetische Mehrrollennaehe rekoppelt offline selektiv.
```

Damit ist selektive Sleep-Reaktivierung nicht einfach eine Eigenschaft langer Fenster. Sie scheint eher an Breite, Rollenzahl, Strain-Anteil und Feldmilieu gekoppelt zu sein.

## Bedeutung Fuer MINI_DIO

Die Offline-Feld-Reorganisation trennt aktuell mindestens zwei Qualitaeten:

- **fokussierte Uebergangsrekopplung**
  Wenige Rollen, klare Kombinationen, volle Rueckaktivierung.

- **breite Mehrrollennaehe**
  Mehr Rollen, mehr Kombinationen, teilweise Rueckaktivierung.

Das ist wichtig, weil es die Schlaf-/Offline-Schicht nicht als starres Wiederholen beschreibt. Sie liest bestehende Feldrollen, aber ihre Rueckkopplung bleibt feldmilieuspezifisch.

## Konsequenz Fuer Die Naechste Forschung

Der naechste methodische Schritt ist nicht noch eine beliebige Reproduktion, sondern eine gezielte Rollenbreiten-Pruefung:

```text
Wie viele Rollen und Strain-Kontakte braucht ein Fenster,
bis Offline-Reorganisation von voller Rekopplung in selektive Rekopplung kippt?
```

## Quellen

- [1589 SYNTH_RAND_KIPP 2000 Mehrrollen-Repro](1589_SYNTH_RAND_KIPP_2000_MEHRROLLEN_REPRO.md)
- [1591 RUHIG_SIDEWAYS 2000 Uebergang-Repro](1591_RUHIG_SIDEWAYS_2000_UEBERGANG_REPRO.md)
- [1593 EXPANSION_POSITIV 2000 Uebergang-Repro](1593_EXPANSION_POSITIV_2000_UEBERGANG_REPRO.md)
