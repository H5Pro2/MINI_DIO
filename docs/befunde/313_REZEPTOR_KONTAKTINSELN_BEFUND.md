# 313 - Lokale Rezeptor-Kontaktinseln

## Grundfrage

Entstehen innerhalb laengerer Welten lokale Kontaktinseln, in denen hoher Kontaktdruck und niedrige Kontaktpassung auftreten, ohne dass das MCM-Feld dauerhaft kollabiert?

## Methodik

Die Inseln wurden weltrelativ bestimmt.

Nicht verwendet wurden absolute Regeln. Pro Welt wurden Diagnosebereiche gebildet:

- hoher `contact_pressure`: oberer weltrelativer Bereich,
- niedriger `contact_alignment`: unterer weltrelativer Bereich,
- Kontaktinsel: beide Bedingungen treten lokal zusammen auf.

Diese Schwellen sind Diagnosehilfen, keine Gates und keine MCM-Regeln.

## Datengrundlage

Ausgewertet wurden:

- `SOL_2023_NEG_STRESS_10K_RECEPTOR`
- `SOL_2024_SIDEWAYS_5K_RECEPTOR`
- `SOL_2025_STRESS_5K_RECEPTOR`
- `SOL_2026_STABLE_5K_RECEPTOR`

Erzeugte Dateien:

- `312_REZEPTOR_KONTAKTINSELN_EVENTS.csv`
- `312_REZEPTOR_KONTAKTINSELN_SUMMARY.csv`

## Befunduebersicht

| Welt | Inseln | Insel-Episoden | Anteil | Durchschnittsdauer | Max. Dauer | Rekoppelt danach | Offen getragen danach | Bleibt kippnah danach |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SOL 2023 Negative Stress 10k | 428 | 528 | 0.0528 | 1.2336 | 7 | 275 | 147 | 6 |
| SOL 2024 Sideways 5k | 215 | 263 | 0.0527 | 1.2233 | 7 | 119 | 91 | 5 |
| SOL 2025 Stress 5k | 211 | 246 | 0.0493 | 1.1659 | 5 | 108 | 100 | 3 |
| SOL 2026 Stable 5k | 233 | 274 | 0.0549 | 1.1760 | 5 | 155 | 76 | 2 |

Gesamt:

- Kontaktinseln: `1087`
- Durchschnittsdauer: `1.206` Ticks
- Maximale Dauer: `7` Ticks

Nachlaufzustand:

- `rekoppelt_nach_kontaktinsel`: `657`
- `offen_getragen_nach_kontaktinsel`: `414`
- `bleibt_kippnah_nach_kontaktinsel`: `16`

Dominante Innenfeldwirkung waehrend der Inseln:

- `tragend_unruhig`: `549`
- `kippend`: `407`
- `gespannt`: `108`
- `stabil`: `23`

## Interpretation

Lokale Kontaktinseln entstehen in allen geprueften Dauerlastwelten.

Sie sind meist kurz. Das ist fachlich relevant:

```text
Der Kontakt wird kurz intensiver oder schlechter passend.
Das Feld oeffnet oder spannt sich lokal.
Danach rekoppelt es in vielen Faellen wieder.
```

Das spricht gegen einen einfachen Kollaps unter Dauerlast. Eher sichtbar ist eine lokale Kontaktverarbeitung:

- Druckspitzen treten auf.
- Alignment faellt lokal.
- Die Insel bleibt meist kurz.
- Danach rekoppelt das Feld haeufig.
- Nur ein kleiner Teil bleibt kippnah.

## Bedeutung fuer die MCM-Lesung

Die Rezeptorschicht zeigt damit eine organische Eigenschaft:

```text
Nicht jede Beruehrung wird dauerhaft Feldlast.
Viele Beruehrungen werden kurz getragen, verarbeitet und wieder rekoppelt.
```

Das passt zur bisherigen MCM-Feldordnung:

- Zentrum bleibt als Rueckkopplungsnaehe erhalten.
- Rand-/Kippnaehe entsteht lokal.
- Offene Varianten tragen Spannung, ohne sofort Kollaps zu bedeuten.
- Rekopplung ist ein aktiver passiver Feldprozess, keine programmierte Handlung.

## Wichtiges Ergebnis

Die lokale Diagnose ist aussagekraeftiger als nur die Gesamtdauer einer Welt.

Laengere Welt bedeutet nicht automatisch mehr Last. Entscheidend ist:

- wie oft lokale Kontaktinseln entstehen,
- wie lange sie halten,
- ob sie danach rekoppeln,
- ob sie offen getragen bleiben,
- oder ob sie kippnah haengen bleiben.

## Grenze

Diese Kontaktinseln sind keine Handlungssignale.

Sie zeigen Wahrnehmungs- und Feldreaktion:

```text
Kontakt -> lokale Spannung -> Feldreaktion -> Rekopplung oder offene Fortsetzung
```

Sie duerfen nicht als Entry-, Gate- oder Strategiemechanik gelesen werden.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob dieselben Kontaktinsel-Familien wiederkehren: tragen bestimmte `symbol_family`- oder `mcm_field_episode_preview_symbol`-Muster wiederholt solche Inseln, und unterscheiden sich rekoppelnde Inseln von kippnahen Inseln semantisch?
