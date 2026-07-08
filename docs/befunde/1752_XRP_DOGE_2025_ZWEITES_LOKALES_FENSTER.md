# XRP/DOGE 2025: zweites lokales Real-Sleep-Real-Folgefenster

Stand: 2026-07-08

## Grundfrage

Die vorherige lokale Real-Sleep-Real-Gegenprüfung zeigte XRP 2025 im Kandidatenfenster deutlich verteilter als DOGE. Die offene Frage war:

```text
Bleibt die verteilte XRP-Offenheit im nächsten Folgefenster erhalten,
oder war sie nur ein lokaler Einzelbefund?
```

## Unterprüfung

Geprüft wurde das nächste lokale Folgefenster:

```text
XRP:  6000-7000 -> 7000-8000
DOGE: 6000-7000 -> 7000-8000
```

Werkzeug:

```text
tools/report_multiworld_axis_map.py
```

Report:

```text
reports/xrp_doge_2025_lokale_realsleepreal_achsen_2.md
```

CSV:

```text
reports/xrp_doge_2025_lokale_realsleepreal_achsen_2.csv
```

## Ergebnis

| Welt | Achsenklasse | Rollen | Kombinationen | Cross-State | Reaktivierung | Kombinationsquote | Nachhall |
|---|---|---:|---:|---:|---:|---:|---:|
| XRP 2025 lokal 2 | verteilt_offen | 6 | 13 | 7 | 0.3333 | 0.0769 | 0.3206 |
| DOGE 2025 lokal 2 | kompakt_nachhallend | 1 | 0 | 0 | 1.0000 | 0.0000 | 0.3191 |

## Befund

XRP bleibt im zweiten lokalen Folgefenster verteilt und offen. Die Rollenbreite bleibt hoch, und es entstehen weiterhin mehrere Cross-State-Kombinationen. DOGE fällt im gleichen Folgeschritt dagegen auf eine kompakte, nachhallende Ordnung zurück.

Damit wird der vorherige Befund geschärft:

```text
Die XRP-Offenverteilung ist in diesem Bereich nicht nur ein einmaliges lokales Aufblitzen.
Sie trägt mindestens über ein weiteres lokales Folgefenster.
```

DOGE zeigt dagegen:

```text
Lokale Mehrrollenbildung ist möglich,
aber sie rekoppelt im nächsten Schritt wieder kompakter.
```

## Deutung

Die mittlere Übergangsphase entsteht nicht allein durch lokale Rollenanzahl. Entscheidend ist, ob sich Rollen, Kombinationen und Offline-/Folgewelt-Reaktivierung über Anschlussfenster weitertragen.

Für XRP 2025 spricht dieser zweite lokale Test für eine breitere, offenere Innenfeldphase. Für DOGE 2025 spricht er eher für kurzfristige lokale Mehrrollenbildung mit anschließender kompakter Rekopplung.

## Grenze

Das ist keine Aussage über Richtung, Handlung oder Strategie. Die Diagnose beschreibt nur passive Innenfeldordnung:

```text
Weltkontakt -> Real-Sleep-Real-Verarbeitung -> Rollenbreite -> Kombinationsqualität -> Rekopplung
```

## Folgeschritt

Als nächstes sollte geprüft werden, ob XRP auch in `7000-8000 -> 8000-9000` verteilt offen bleibt oder ob dort ebenfalls eine kompaktere Rekopplung einsetzt. Erst danach lässt sich unterscheiden zwischen:

- längerer XRP-Übergangsphase,
- lokaler XRP-Offeninsel,
- oder beginnender Rekopplung nach verteilter Phase.
