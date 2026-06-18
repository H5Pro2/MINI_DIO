# 116 - Passive Drift-/Uebergangs-Merkmalsnaehe

Datum: 2026-06-18

## Grundfrage

Welche Weltmerkmale lassen Drift oder Uebergangszone staerker auftreten,
ohne dass das Zentrum kollabiert?

## Unterpruefung

Die passiven Matrix-Rollen wurden gegen die multisensorische Signatur gelesen:

- Sehen: `sehen_*`
- Hoeren: `hoeren_*`
- Feldlage: `feld_*`
- Folgezustand: `folge_*`
- MCM-Innenwerte: Carry, Strain, Rekopplung

Geprueft wurde,
welche Merkmale bei `selbstnahe_drift`
und `uebergangszone`
gegenueber dem Gesamtfeld ueber- oder unterrepraesentiert sind.

Skript:

`DIO_MINI/report_passive_drift_transition_feature_proximity.py`

Ausgabe:

`debug/dio_mini_passive_drift_transition_feature_proximity_20260618/matrix_role_feature_enrichment.csv`

`debug/dio_mini_passive_drift_transition_feature_proximity_20260618/matrix_role_profile.csv`

`debug/dio_mini_passive_drift_transition_feature_proximity_20260618/drift_transition_feature_proximity_summary.json`

## Ergebnis

Gelesen wurden `350184` passive Zeilen.

Rollenanteile:

- `zentrum`: `123223` Zeilen, Anteil `0.351881`
- `tragende_bruecke`: `67314` Zeilen, Anteil `0.192225`
- `selbstnahe_drift`: `51441` Zeilen, Anteil `0.146897`
- `uebergangszone`: `39135` Zeilen, Anteil `0.111756`
- `entlastende_bruecke`: `36384` Zeilen, Anteil `0.1039`
- `entlastende_bruecke_mit_offener_varianz`: `32687` Zeilen, Anteil `0.093342`

## Selbstnahe Drift

`selbstnahe_drift` koppelt besonders stark an:

- `feld_coherence_neutral`
  - Rollenanteil `0.880776`
  - Basisanteil `0.304289`
  - Anreicherung `0.576487`
- `sehen_unstable`
  - Rollenanteil `0.976342`
  - Basisanteil `0.438232`
  - Anreicherung `0.538109`
- `folge_carry_bleibt`
  - Rollenanteil `0.775315`
  - Basisanteil `0.396674`
  - Anreicherung `0.378641`
- `folge_rekopplung_bleibt`
  - Rollenanteil `0.851908`
  - Basisanteil `0.626419`
  - Anreicherung `0.225489`
- `sehen_motion_mid`
  - Rollenanteil `0.734784`
  - Basisanteil `0.528054`
  - Anreicherung `0.20673`

Passiv gelesen:

Selbstnahe Drift erscheint,
wenn das Sehen instabil ist,
das Feld aber nicht eindeutig polar kippt.
Carry und Rekopplung bleiben haeufig stehen.

Das wirkt nicht wie Zusammenbruch,
sondern wie ein innerer Driftbereich:
Das Feld sieht Unruhe,
aber die innere Ordnung haelt noch genug,
um nicht in Randkollaps zu gehen.

## Uebergangszone

`uebergangszone` koppelt besonders stark an:

- `folge_strain_faellt`
  - Rollenanteil `0.732362`
  - Basisanteil `0.203747`
  - Anreicherung `0.528615`
- `folge_rekopplung_steigt`
  - Rollenanteil `0.628133`
  - Basisanteil `0.18952`
  - Anreicherung `0.438613`
- `folge_carry_steigt`
  - Rollenanteil `0.636821`
  - Basisanteil `0.300713`
  - Anreicherung `0.336108`
- `hoeren_tone_high`
  - Rollenanteil `0.419446`
  - Basisanteil `0.176536`
  - Anreicherung `0.24291`
- `sehen_neutral`
  - Rollenanteil `0.639198`
  - Basisanteil `0.439143`
  - Anreicherung `0.200054`

Passiv gelesen:

Die Uebergangszone ist nicht einfach Chaos.
Sie erscheint dort,
wo Strain faellt,
Rekopplung steigt,
Carry steigt
und der Markt akustisch/energetisch staerker wird.

Das sieht nach einer passiven Rekopplungsbewegung aus:
Energie ist vorhanden,
aber das Feld organisiert sich eher Richtung Entlastung,
nicht Richtung Zerfall.

## MCM-Schluss

Drift und Uebergang sind unterscheidbare Innenfeldzustaende.

`selbstnahe_drift`:

- instabiles Sehen,
- neutrale Feldkohaerenz,
- mittlere Spannung,
- haltende Carry/Rekopplung.

`uebergangszone`:

- fallender Strain,
- steigende Rekopplung,
- steigender Carry,
- hoehere Tonlage,
- neutraleres Sehen.

Damit wird die MCM-Topologie tiefer:
Die Rollen sind nicht nur Orte,
sondern tragen unterschiedliche Bewegungsqualitaeten.

## Grenze des Befunds

Die Analyse zeigt passive Merkmalsnaehe.

Sie beweist keine harte Kausalitaet
und darf nicht als Regel, Gate oder Handlungssignal verwendet werden.

## Wie es weitergeht

Grundfrage:

Sind Drift und Uebergang nur Rollen innerhalb der Matrix,
oder bilden sie eigene zeitliche Entwicklungsphasen?

Unterpruefung:

Vorher-/Nachher-Fenster um starke Drift-
und Uebergangsbereiche lesen.

Folgeschritt:

Passive Phasendynamik pruefen:
Was kommt vor Drift,
was kommt nach Drift,
was kommt vor Uebergang,
was kommt nach Uebergang?
