# 311 - Rezeptorschicht unter Dauerlast

## Grundfrage

Bleibt die rezeptorische Wahrnehmungsarchitektur auch bei längeren Welten stabil, oder entstehen unter Dauerlast neue Kontakt-Archetypen?

## Prüfaufbau

Geprüft wurden längere kontrollierte Welten:

- `SOL_2023_NEG_STRESS_10K_RECEPTOR`
- `SOL_2024_SIDEWAYS_5K_RECEPTOR`
- `SOL_2025_STRESS_5K_RECEPTOR`
- `SOL_2026_STABLE_5K_RECEPTOR`

Hinweis:

Ein geplanter vollständiger 10k-Block wurde wegen Laufzeit begrenzt. Der vollständige 10k-Lauf `SOL_2023_NEG_STRESS_10K_RECEPTOR` liegt vor. Die drei weiteren Dauerlastwelten wurden als 5k-Ausschnitte aus vorhandenen 10k-Welten erzeugt, damit der Vergleich reproduzierbar und zeitlich tragbar bleibt.

## Topologischer Befund

Alle geprüften Dauerlastwelten bleiben bei:

```text
zentrum_mit_rand_und_uebergang
```

| Welt | Episoden | Zentrum | Offen | Rand/Kipp |
|---|---:|---:|---:|---:|
| SOL 2023 Negative Stress 10k | 9994 | 0.8406 | 0.1302 | 0.0292 |
| SOL 2024 Sideways 5k | 4994 | 0.8324 | 0.1378 | 0.0298 |
| SOL 2025 Stress 5k | 4994 | 0.8240 | 0.1508 | 0.0252 |
| SOL 2026 Stable 5k | 4994 | 0.8396 | 0.1282 | 0.0322 |

Damit zeigt sich aktuell:

```text
Die Rezeptorarchitektur bleibt auch bei längerer Weltsequenz topologisch stabil.
```

## Rezeptorische Dauerlastwerte

| Welt | Contact Pressure Ø | Pressure P95 | High Pressure Anteil | Alignment Ø | Low Alignment Anteil | MCM Coherence Ø | High Strain Anteil |
|---|---:|---:|---:|---:|---:|---:|---:|
| SOL 2023 Negative Stress 10k | 0.2076 | 0.3551 | 0.0757 | 0.8658 | 0.1257 | 0.5661 | 0.0621 |
| SOL 2024 Sideways 5k | 0.2114 | 0.3556 | 0.0791 | 0.8650 | 0.1298 | 0.5653 | 0.0667 |
| SOL 2025 Stress 5k | 0.2145 | 0.3487 | 0.0799 | 0.8594 | 0.1390 | 0.5656 | 0.0623 |
| SOL 2026 Stable 5k | 0.2064 | 0.3566 | 0.0765 | 0.8667 | 0.1366 | 0.5766 | 0.0615 |

## Interpretation

Es entsteht bisher kein klar neuer Kontakt-Archetyp nur durch längere Laufdauer.

Stattdessen sieht man eine stabile Kontaktökonomie:

- durchschnittlicher Kontaktdruck bleibt eng beieinander,
- P95-Druck bleibt über Welten sehr ähnlich,
- Low-Alignment-Anteil steigt leicht in Stress-/Dauerlastwelten,
- MCM-Kohärenz bleibt erstaunlich stabil,
- Zentrum-Rand-Übergangsordnung bleibt erhalten.

Die Rezeptorschicht wirkt damit nicht wie ein künstlicher Verstärker, sondern wie eine Dämpfungs- und Übersetzungsschicht:

```text
Weltspannung wird nicht roh vergrößert.
Sie wird als Kontaktqualität ins Feld übersetzt.
```

## Was das für Mini-DIO bedeutet

Die MCM-Feldordnung scheint unter längerer Sequenz nicht sofort zu kollabieren.

Wichtiger als absolute Dauerlast ist offenbar:

- wie Kontaktpassung driftet,
- wie oft Alignment fällt,
- wie oft Druckspitzen auftreten,
- ob diese Spitzen rekoppeln oder offen bleiben.

Das spricht dafür, dass zukünftige Forschung weniger auf Rohdatenlänge und stärker auf lokale Kontaktübergänge schauen sollte.

## Grenze

Die Schwellen in der Auswertung, etwa `High Pressure` oder `Low Alignment`, sind Diagnosehilfen. Sie sind keine Regeln, keine Gates und keine MCM-Grenzwerte.

Der Befund ist:

```text
In den geprüften Dauerlastwelten bleibt die rezeptorische MCM-Topologie stabil.
Neue Archetypen sind bisher nicht zwingend sichtbar.
```

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob innerhalb dieser Dauerlastwelten lokale Kontaktinseln entstehen: kurze Abschnitte, in denen `contact_pressure` hoch, `contact_alignment` niedrig und Rekopplung trotzdem möglich ist. Das wäre wichtiger als noch längere Gesamtläufe.
