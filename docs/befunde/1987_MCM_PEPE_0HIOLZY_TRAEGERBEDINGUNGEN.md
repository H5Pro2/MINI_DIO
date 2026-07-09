# 1987 - PEPE-A Ruecklesung der Milieuinsel 0hiolzy

## Grundfrage

`dio_mcm_episode_0hiolzy` wurde in PEPE-A als starke neue Milieuinsel sichtbar, kehrte im zweiten PEPE-Fenster aber nicht direkt wieder. Diese Ruecklesung fragt deshalb:

Welche Welt-, Sinnes- und Feldbedingungen haben `0hiolzy` in PEPE-A getragen?

## Datenbasis

- Welt: `FOLLOW_EQ10K_PEPE_2024_5M`
- Debuglauf: `debug/1985_equal10k_pepe_2024_5m/dio_mini_lauf_47/episodes.csv`
- Rohwelt: `data/kontrolliert_pepe_2024_5m_10k_PEPEUSDT.csv`
- Zielrolle: `dio_mcm_episode_0hiolzy`
- Segmenttabelle: `docs/befunde/1987_MCM_PEPE_0HIOLZY_SEGMENTE.csv`

## Grobbefund

`0hiolzy` trat in PEPE-A 769-mal direkt in den Episoden auf. Die Aktivierung war nicht gleichmaessig ueber den ganzen Lauf verteilt, sondern lag in 10 Segmenten. Das groesste Segment dominiert klar:

- Hauptsegment: Tick 9327 bis 9994
- Laenge: 668 Ticks
- Anteil am direkten Auftreten: ca. 86.9 Prozent

Damit ist `0hiolzy` keine frei verteilte Zufallsrolle, sondern eine spaete, zusammenhaengende Feldphase.

## Segmentstruktur

Die laengsten Segmente:

| Start | Ende | Laenge | fuehrende Formfamilie | dominante Zeitlage |
|---:|---:|---:|---|---|
| 9327 | 9994 | 668 | `dio_14wj` | `temporal_far_return` |
| 9083 | 9107 | 25 | `dio_14wj` | `temporal_far_return` |
| 8125 | 8143 | 19 | `dio_14wj` | `temporal_far_return` |
| 9041 | 9056 | 16 | `dio_14wj` | `temporal_far_return` |
| 9306 | 9315 | 10 | `dio_14wj` | `temporal_near_return` |

Die dominante Formfamilie ist nicht exklusiv, aber auffaellig haeufig `dio_14wj`. Das spricht fuer eine wiederkehrende Form-/Feldnaehe, nicht fuer ein einzelnes isoliertes Tick-Ereignis.

## Feldprofil gegenueber dem Rest der PEPE-A-Welt

Gegenueber allen anderen PEPE-A-Ticks zeigt `0hiolzy`:

- mehr Tragqualitaet: `mcm_carry_quality` ca. 0.592 statt 0.559
- weniger Feldspannung: `mcm_strain_quality` ca. 0.152 statt 0.166
- mehr Rekopplung: `mcm_rekopplung_quality` ca. 0.733 statt 0.716
- mehr Sinneskopplung: `mcm_sensory_coupling` ca. 0.858 statt 0.843
- deutlich weniger Hoer-Feld-Luecke: `mcm_hearing_field_gap` ca. 0.034 statt 0.081
- mehr Nachhall: `mini_afterimage` ca. 0.828 statt 0.687
- mehr Wiederkehr: `mini_recurrence_strength` ca. 0.941 statt 0.767
- weniger direkte Kontaktspannung: `rezeptor_contact_pressure` ca. 0.056 statt 0.094
- weniger auditive Lautheit: `perception_auditory_loudness` ca. 0.076 statt 0.169
- etwas schaerferes Sehen: `perception_visual_sharpness` ca. 0.642 statt 0.626

Die Milieuinsel entsteht damit nicht aus maximaler Lautheit oder maximalem Druck. Sie wirkt eher wie eine ruhiger rekoppelnde, nachhallstarke Feldphase mit guter Wiederkehr und geringerer Hoer-Luecke.

## Rohweltprofil

Im Hauptsegment 9327 bis 9994:

- Close: ca. `0.00000093` -> `0.00000091`
- aufsummierte Kerzenrendite: ca. -0.1231
- durchschnittliche Range: ca. 0.01133
- durchschnittliches Volumen: ca. 19.6 Mrd.

Die Rolle liegt also nicht in einem klaren reinen Expansionsschub, sondern in einer spaeten, leicht fallenden, dennoch rekoppelnden Weltphase.

## Interpretation

`0hiolzy` wirkt wie eine situative Milieuinsel:

- spaet im Lauf,
- stark zusammenhaengend,
- nachhall- und wiederkehrstark,
- nicht laut, sondern eher leiser und rekoppelnder,
- visuell ausreichend scharf,
- mit geringerer direkter Kontaktspannung.

Das erklaert, warum PEPE-B die Rolle nicht automatisch wieder aktivierte. Die Rolle scheint nicht an das Asset PEPE gebunden zu sein, sondern an eine konkrete Kombination aus Weltphase, Rekopplung, Nachhall, Wiederkehr und Sinneslage.

## Arbeitshypothese

`0hiolzy` bezeichnet wahrscheinlich keine Marktklasse und keine einfache Preisform. Es ist eher eine phasenabhaengige MCM-Bedeutungsinsel:

> Eine spaete, leiser gekoppelte, nachhallstarke und stabil rekoppelnde Feldphase, die trotz fallender Rohweltbewegung als getragen gelesen wird.

Diese Hypothese muss gegen weitere Fenster geprueft werden.

## Wie es weitergeht

Als naechstes sollte ein drittes PEPE-Fenster oder ein gezielt ausgeschnittenes Nachbarfenster um aehnliche Bedingungen geprueft werden. Entscheidend ist, ob hohe Wiederkehr, hoher Nachhall, geringe Hoer-Luecke und geringe Kontaktspannung erneut `0hiolzy` oder eine verwandte Milieurolle erzeugen.
