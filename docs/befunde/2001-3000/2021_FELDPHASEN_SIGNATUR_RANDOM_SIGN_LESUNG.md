# 2021 - Lesung des Random-Sign-Feldphasenvergleichs

## Ausgangspunkt

Nach dem Shuffle-Nullvergleich wurde ein stärkerer Nulltest durchgeführt.

Diesmal wurden Random-Sign-Welten verwendet. Dadurch bleibt die äußere Größenordnung teilweise erhalten, aber Richtung und Vorzeichen werden gestört.

Wichtig: Ein erster Lauf wurde wegen fehlerhafter `world-label`-Benennung verworfen. Die gültige Auswertung ist die Kette `2020` mit korrekt als `NULL_RANDSIGN` markierten Welten.

## Ergebnis

Die gültige Random-Sign-Kette enthält:

- `293` Feldphasen-Signaturen
- `169` junge Feldphasen
- `98` positive Rekopplungsphasen
- `26` stabile Crossworld-Feldphasen
- `217` dominant realweltgebundene Signaturen
- `72` dominant feldinterne Nullordnungen
- `4` Mixed-Binding-Signaturen

Gegenüber dem Shuffle-Vergleich nimmt die Zahl feldinterner Nullordnungen zu.

## Kernphasen

Einige starke Feldphasen bleiben stabil, nehmen aber Nullanteile auf:

- `dio_mcm_episode_0icnf2v`
  - real: `12360`
  - null/random-sign: `13842`
  - Zustand: `stable_crossworld_field_phase`
  - dominante Bindung: `realworld_bound`, mit deutlichem Mixed-Anteil

- `dio_mcm_episode_1rj8742`
  - real: `3453`
  - null/random-sign: `2310`
  - Zustand: `stable_crossworld_field_phase`

- `dio_mcm_episode_1qlxgj7`
  - real: `2401`
  - null/random-sign: `1043`
  - Zustand: `stable_crossworld_field_phase`

- `dio_mcm_episode_0wo0tz1`
  - real: `1504`
  - null/random-sign: `1772`
  - Zustand: `stable_crossworld_field_phase`
  - Mixed-Anteil sichtbar

- `dio_mcm_episode_12tgchq`
  - real: `2037`
  - null/random-sign: `725`
  - Zustand: `stable_crossworld_field_phase`

## Interpretation

Random-Sign trennt deutlicher als Shuffle.

Wenn eine Feldphase trotz Random-Sign stabil bleibt, ist sie wahrscheinlich nicht nur an konkrete Kerzenfolge gebunden. Sie kann auch durch Rezeptorverteilung, Energielage, Rekopplung und interne Feldnähe getragen werden.

Gleichzeitig zeigen die neuen `field_internal_null_order`-Signaturen, dass gestörte Welten eigene feldinterne Ordnungen bilden können. Diese sind nicht automatisch realweltlich zu lesen.

Damit entsteht eine wichtige Unterscheidung:

- stabile Realwelt-Feldphase
- stabile Crossworld-Feldphase
- Mixed-Binding-Phase
- feldinterne Nullordnung

## Bedeutung für MINI_DIO

MINI_DIO bekommt dadurch eine präzisere Felddiagnostik.

Es reicht nicht mehr zu sagen: Eine Signatur kommt wieder.

Wichtiger ist:

- In welcher Weltqualität kommt sie wieder?
- Bleibt sie realweltgebunden?
- Wird sie durch Nullwelten mitgetragen?
- Wird sie zur feldinternen Ordnung?
- Wird sie zu einer Mixed-Binding-Phase?

Das ist eine organische Erweiterung der MCM-Feldmemory, weil die Herkunft und Bindungsqualität einer Bedeutung mitgeführt wird.

## Konsequenz

Für die weitere Entwicklung sollte MINI_DIO starke Feldphasen nicht einfach als "gut" oder "stabil" behandeln.

Stabilität braucht Herkunft:

- realweltstabil
- nullstabil
- gemischt stabil
- jung/offen

Damit wird das Feld nicht härter programmiert, sondern genauer lesbar.
