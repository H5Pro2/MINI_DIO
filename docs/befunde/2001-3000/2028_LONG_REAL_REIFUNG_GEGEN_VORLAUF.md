# 2028 - Lange Realwelt-Kette gegen Vorlauf

## Zweck

Dieser Befund vergleicht die bisherige Real-Follow-Kette mit einer längeren reinen Realwelt-Kette.

Geprüft wurde nicht Handlung, Richtung oder Strategie, sondern:

- ob Feldphasen unter mehr realer Außenwelt stabil bleiben,
- ob ihre Herkunft realweltgetragen bleibt,
- ob bestehende Signaturen reifen,
- ob neue Signaturen neben die alten treten.

## Laufbasis

Neue lange Realwelt-Kette:

```text
memory/2026_field_phase_signature_long_real_chain.json
```

Sie besteht aus sechs realen Fenstern:

```text
BTC 0-17k
BTC 17k-34k
BTC 34k-51k
SOL 0-17k
SOL 17k-34k
SOL 34k-51k
```

Gesamtumfang:

```text
102000 Kerzen
```

## Ergebnis der langen Realwelt-Kette

Die Feldphasen-Signatur-Memory enthält:

```text
464 Signaturen
82 stable_crossworld_field_phase
154 positive_recoupling_field_phase
228 young_field_phase
464 realworld_bound
```

Feldfunktionen:

```text
171 active_recoupling
165 open_surface
128 milieu_island
```

Damit bleibt die Herkunft in dieser Kette vollständig realweltgetragen.

## Reifung über mehr Außenwelt

Die durchschnittliche Feldphasentiefe stieg im Verlauf der sechs Fenster:

```text
0.707641
0.759603
0.791085
0.812562
0.827902
0.835596
```

Die durchschnittliche Drift blieb dagegen eng:

```text
0.050406
0.050719
0.051800
0.051011
0.051051
0.052213
```

Lesung:

```text
Mehr reale Außenwelt erhöht die Feldphasentiefe,
ohne dass die Drift proportional entgleist.
```

Das spricht für Reifung statt bloßer Aufblähung.

## Vergleich zur vorherigen Real-Follow-Kette

Top-120-Vergleich:

```text
alte Real-Follow-Kette: 120 Signaturen
lange Realwelt-Kette: 120 Signaturen
gemeinsam: 55 Signaturen
Jaccard-Nähe: 0.2973
```

Das bedeutet:

```text
Die neue Kette kopiert nicht einfach die alte Oberfläche.
Sie hält aber einen wiedererkennbaren Kern und bildet neue Nachbarschaften.
```

## Beispiele gereifter gemeinsamer Signaturen

```text
dio_mcm_episode_0iwh9d2
positive_recoupling_field_phase -> stable_crossworld_field_phase
Tiefe 0.764748 -> 0.848824
Funktion milieu_island -> milieu_island

dio_mcm_episode_12tgchq
positive_recoupling_field_phase -> stable_crossworld_field_phase
Tiefe 0.824693 -> 0.847418
Funktion milieu_island -> milieu_island

dio_mcm_episode_0bygq81
positive_recoupling_field_phase -> stable_crossworld_field_phase
Tiefe 0.723534 -> 0.846386
Funktion milieu_island -> milieu_island

dio_mcm_episode_1qv5i56
young_field_phase -> stable_crossworld_field_phase
Tiefe 0.613271 -> 0.844299
Funktion milieu_island -> milieu_island
```

## Fachliche Lesung

Dieser Befund ist wichtig, weil er drei Dinge trennt:

```text
Wiederkehr:
Eine Signatur taucht erneut auf.

Reifung:
Eine Signatur gewinnt Tiefe und Crossworld-Stabilität.

Herkunft:
Eine Signatur bleibt realweltgetragen oder kippt in andere Herkunftsqualität.
```

In der langen Realwelt-Kette bleibt die Herkunft sauber realweltgetragen.
Gleichzeitig entstehen neue Signaturen und alte Signaturen reifen unterschiedlich.

Das passt zur bisherigen MINI_DIO-Linie:

```text
Das Feld speichert nicht nur Namen.
Es verdichtet Feldphasenqualität über Weltkontakt.
```

## Grenze

Das ist kein Beweis für Bewusstsein und keine Aussage über Handlung.

Der Befund zeigt:

```text
Unter mehr realem Weltkontakt bildet MINI_DIO stabilere Feldphasen,
ohne dass diese Stabilität durch Nullstörung erklärt werden muss.
```

## Wie es weitergeht

Als nächstes sollte eine lange Realwelt-Kette mit anderem Asset oder anderem Regime geprüft werden. Entscheidend ist, ob dieselben stabilen Kernsignaturen erneut auftauchen oder ob die Topologie neue reale Rollen ausbildet.
