# Real/Synthetisch Rollenprofil Bewertung

Stand: 2026-07-01

## Grundfrage

Liegen reale Rand/Kipp-Rollen naeher an reiner Hoerlast, an Formbruch oder an gekoppelter Feldlast?

Nach aktueller Vergleichsmatrix: reale Rand/Kipp-Rollen liegen naeher an gekoppelter Feldlast. Synthetische Rand/Kipp-Rollen koennen dagegen sauber als Hoerlast bei weiter lesbarer Form auftreten.

## Grundlage

Verglichen wurden:

- reale 5m Stress-/Quiet-Segmente aus `1225`
- synthetische Sinnesachsen-Segmente aus `1229`

Die Vergleichsmatrix liegt in:

- `docs/befunde/1001-2000/1001-1500/1235_REAL_SYNTH_ROLLENPROFIL_VERGLEICH.md`
- `docs/befunde/1001-2000/1001-1500/1235_REAL_SYNTH_ROLLENPROFIL_VERGLEICH.csv`

## Hauptbefund

Die Signaturen trennen sich:

```text
SYNTH_VISUAL_STABLE_HEARING_CHAOTIC Rand/Kipp:
  Signatur: hoerlast_bei_lesbarer_form
  Lautheit: 0.8361
  visuelle Schaerfe: 0.7397

SYNTH_DESYNC_AXES Rand/Kipp:
  Signatur: hoerlast_bei_lesbarer_form
  Lautheit: 0.8219
  visuelle Schaerfe: 0.7405

REAL_5M Rand/Kipp:
  Signatur: gekoppelte_feldlast
  Lautheit hoch
  Rohfeld hoch
  visuelle Schaerfe niedriger
  Rekopplung niedriger
  Strain hoeher
```

Damit ist die real/synthetische Unterscheidung fachlich sauberer:

```text
Synthetik kann Einzelachsen isolieren.
Reale Weltspuren koppeln Sinnesachsen.
```

## Bedeutung fuer das MCM-Feld

Rand/Kipp ist keine einfache Klasse wie "viel Bewegung".

In MINI_DIO liest sich Rand/Kipp aktuell als Feldrolle, die aus mehreren Rezeptorqualitaeten entstehen kann:

- reine Hoer-/Energiebelastung bei noch lesbarer Form,
- gekoppelte Weltlast aus Formbewegung, Lautheit, Rekopplungsabfall und Strain,
- seltene kurze Randnaehe aus synthetischer Rand/Kipp-Konstruktion.

Das ist wichtig, weil die Topologie dadurch nicht mechanisch eindimensional wird. Dieselbe Feldrolle kann unterschiedliche Ursachen tragen, solange ihre Feldwirkung aehnlich ist.

## Schlussfolgerung

Die Rezeptorschicht leistet hier zwei Dinge:

1. Sie verhindert, dass Rohweltspannung direkt das MCM-Feld ueberlaedt.
2. Sie laesst trotzdem unterschiedliche Feldursachen unterscheidbar.

Das spricht fuer eine organischere Lesart:

```text
Das Feld speichert nicht einfach Daten.
Es bildet Rollen aus Feldwirkung.
Die Ursache bleibt ueber Sinnesachsen und Rezeptorprofil ruecklesbar.
```

## Grenze

Die verwendeten Signaturen sind diagnostische Einordnung, keine Runtime-Regel.

Sie helfen, Befunde lesbar zu machen. MINI_DIO entscheidet daraus nichts und handelt daraus nicht.
