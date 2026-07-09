# 117 - Passive Drift-/Uebergangs-Phasendynamik

Datum: 2026-06-18

## Grundfrage

Sind Drift und Uebergang nur Rollen innerhalb der Matrix,
oder bilden sie eigene zeitliche Entwicklungsphasen?

## Unterpruefung

Geprueft wurden Vorher-/Nachher-Fenster um:

- `selbstnahe_drift`
- `uebergangszone`

Radius: `3` Ticks vor und nach dem Ereignis.

Zusaetzlich wurden zusammenhaengende Segmente derselben Rolle gelesen.

Skript:

`DIO_MINI/report_passive_drift_transition_phase_dynamics.py`

Ausgabe:

`debug/dio_mini_passive_drift_transition_phase_dynamics_20260618/phase_offset_profile.csv`

`debug/dio_mini_passive_drift_transition_phase_dynamics_20260618/phase_transition_pairs.csv`

`debug/dio_mini_passive_drift_transition_phase_dynamics_20260618/phase_segments.csv`

`debug/dio_mini_passive_drift_transition_phase_dynamics_20260618/phase_segment_summary.csv`

`debug/dio_mini_passive_drift_transition_phase_dynamics_20260618/phase_dynamics_summary.json`

## Ergebnis

Zielereignisse:

- `selbstnahe_drift`: `51441`
- `uebergangszone`: `39135`

Segmentbefund:

- `selbstnahe_drift`
  - Segmente: `35485`
  - mittlere Laenge: `1.449655`
  - maximale Laenge: `11`
  - dominanter Zustand davor: `zentrum`
  - dominanter Zustand danach: `zentrum`
- `uebergangszone`
  - Segmente: `35315`
  - mittlere Laenge: `1.108169`
  - maximale Laenge: `6`
  - dominanter Zustand davor: `zentrum`
  - dominanter Zustand danach: `zentrum`

## Offset-Lesung Drift

Bei `selbstnahe_drift`:

- Offset `-3`: dominant `zentrum`
- Offset `-2`: dominant `zentrum`
- Offset `-1`: dominant `selbstnahe_drift`
- Offset `0`: `selbstnahe_drift`
- Offset `1`: dominant `selbstnahe_drift`
- Offset `2`: dominant `zentrum`
- Offset `3`: dominant `zentrum`

Innenfeld:

- Carry faellt am Driftpunkt auf `0.352898`.
- Strain faellt am Driftpunkt auf `0.163116`.
- Rekopplung faellt am Driftpunkt auf `0.656976`.
- Danach steigen Carry und Rekopplung wieder Richtung Zentrum.

Passiv gelesen:

Drift ist kein harter Kollaps.
Drift ist eine kurze selbstnahe Abweichung,
bei der das Zentrum kurz verlassen wird,
aber die Ordnung danach wieder zurueckfindet.

## Offset-Lesung Uebergang

Bei `uebergangszone`:

- Offset `-3`: dominant `zentrum`
- Offset `-2`: dominant `zentrum`
- Offset `-1`: dominant `zentrum`
- Offset `0`: `uebergangszone`
- Offset `1`: dominant `zentrum`
- Offset `2`: dominant `zentrum`
- Offset `3`: dominant `zentrum`

Innenfeld:

- Carry am Uebergang: `0.371446`
- Strain am Uebergang: `0.209286`
- Rekopplung am Uebergang: `0.654051`
- Direkt nach dem Uebergang:
  - Carry steigt auf `0.402588`
  - Strain faellt auf `0.171633`
  - Rekopplung steigt auf `0.679798`

Passiv gelesen:

Uebergang ist eine sehr kurze Druck-/Rekopplungsphase.
Am Uebergang steigt die Spannung,
danach organisiert sich das Feld wieder Richtung Zentrum.

## MCM-Schluss

Drift und Uebergang sind nicht nur statische Rollen.

Sie tragen zeitliche Qualitaet:

- Drift ist eine kurze selbstnahe Abweichungsphase.
- Uebergang ist eine kurze Rekopplungsphase.

Beide Phasen liegen dominant zwischen Zentrum-Zustaenden.

Damit zeigt Mini-DIO eine passive Raum-Zeit-Ordnung:
Ein Zustand ist nicht nur Ort im Feld,
sondern besitzt Vorlauf,
Kippmoment
und Ruecklauf.

## Grenze des Befunds

Die Analyse bleibt passiv.

Sie erzeugt keine Handlung,
kein Gate
und kein Entry-Signal.

Sie zeigt zeitliche Naehe und Phasenstruktur,
aber keine harte Kausalitaet.

## Bedeutung fuer Mini-DIO

Mini-DIO liest nicht nur:

`welcher Zustand ist da?`

sondern zunehmend:

`woher kommt dieser Zustand und wohin entspannt er sich?`

Das ist relevant fuer eine organische MCM-Regulation,
weil Regulation nicht nur auf Momentwerte reagieren darf,
sondern die Bewegung eines Innenfeldes verstehen muss.

## Wie es weitergeht

Grundfrage:

Sind diese Phasen nur um Drift und Uebergang sichtbar,
oder besitzt auch das Zentrum eine eigene Vorlauf-/Ruecklaufstruktur?

Unterpruefung:

Zentrum nicht als statische Mitte behandeln,
sondern Fenster um starke Zentrumspunkte lesen.

Folgeschritt:

Passive Zentrum-Phasendynamik pruefen:
Was stabilisiert Zentrum,
was verlaesst Zentrum,
und was kehrt zu Zentrum zurueck?
