# Sleep-Zwischenrollen Stabilitaet R2 Synthese

Stand: 2026-07-05

## Zweck

Diese Pruefung wiederholt die weiche Real-Sleep-Real-Kette mit neuen Labels.

Ziel:

```text
Bleiben die passiven Zwischenrollen-Kandidaten stabil,
oder entstehen andere Kandidaten?
```

## Ergebnis

Die zweite Kette erzeugte dieselbe Kandidatenstruktur wie die erste:

```text
7 quiet_intermediate_candidate
3 origin_bound_combination
```

Der lokale passive Speicher zeigt:

```text
candidate_count: 7
history: 2
seen_count: 2 fuer alle 7 Kandidaten
```

## Lesung

Die Zwischenrollen-Kandidaten sind in dieser Wiederholung stabil.

Das bedeutet:

```text
Die weichen Sleep-Kombinationen bilden nicht nur einmalige lokale Streuung.
Dieselben sieben Kandidaten tauchen bei gleicher Pruefkette erneut auf.
```

Wichtig bleibt:

```text
Das ist ein passiver Stabilitaetsbefund.
Es ist keine Handlung, kein Gate, keine Richtung und noch keine autonome Semantik.
```

## Bedeutung

Die MCM-Feldstruktur zeigt hier eine kleine, aber klare topologische Erweiterung:

```text
Einzelrollen bleiben nicht isoliert.
Bestimmte Rollenpaare werden im Sleep-Milieu wiederholt gemeinsam anschlussfaehig.
Ein Teil dieser Paare findet in verwandter ruhiger Welt teilweise Anschluss.
```

Damit ist die naechste Stufe begruendet:

```text
Zwischenrollen koennen ueber mehrere Ketten beobachtet werden.
```

## Grenze

Der Speicher liegt lokal unter:

```text
memory/sleep_intermediate_candidates/passive_sleep_intermediate_candidates.json
```

Dieser Ordner ist absichtlich nicht versioniert. Das Repository enthaelt Code und Befunde, aber nicht den lokalen laufenden Forschungszustand.
