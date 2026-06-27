# MCM-Rand Und Driftkern Synthese

## Zweck

Diese Notiz fasst die korrigierte Randpruefung nach Erzeugung einer passenden Nachbarschaftsmatrix zusammen.

Ausgangspunkt:

- `882_MCM_RANDPFADE_GEGENKERN_LUPE.md` zeigte eine Datenabdeckungsgrenze.
- `884_MCM_RANDTOKEN_NACHBARSCHAFTSLUPE.md` erzeugte die passende Nachbarschaft fuer Rand-, Oberflaechen- und Drift-Tokens.
- `885_MCM_RANDPFADE_GEGENKERN_LUPE_MIT_ABDECKUNG.md` liest daraus die Gegenkernfrage erneut.

## Zentrale Ergebnisse

Die aktuelle Rand-/Driftpruefung zeigt:

```text
48 untersuchte Tokens
4045 Nachbarschaftskontakte
1 starker Driftkern-Kandidat
1 lokale junge Selbstinsel
2 randstabile Tokens ohne Selbstkern
1 randnah rekoppelnder Token
```

## Wichtigster Einzelbefund

`dio_mcm_episode_0ykar6i` ist kein normaler kurzlebiger Drift.

```text
Pfadklasse: offener_driftpfad
Bewegung: Oeffnung oder Drift
Kontakte: 3556
Welten: 4
Selbstbindung: ca. 0.982
Klassifikation: starker_driftkern_kandidat
```

Das bedeutet:

```text
Drift kann im MCM-Feld selbst eine starke Verdichtung bilden.
Diese Verdichtung ist aber nicht automatisch ein Rand-Gegenkern.
```

## Junge Selbstinsel

`dio_mcm_episode_1eju9g0` bildet eine lokale junge Selbstinsel:

```text
Pfadklasse: junge_oberflaeche
Kontakte: 327
Welten: 1
Selbstbindung: ca. 0.933
```

Das ist lokal stark, aber noch nicht weltuebergreifend genug fuer eine stabile Bedeutungsinsel.

## Randpfade

Die zwei stabilen Randpfade:

```text
0mm85pw
0mw7rev
```

haben Kontakte und mehrere Welten, aber keine Selbstbindung.
Sie wirken daher aktuell nicht wie eigene Randkerne, sondern eher wie randnahe Durchgangs- oder Kontaktzonen.

## Fachliche Interpretation

Die MCM-Topologie wirkt damit differenzierter:

```text
Zentrum bildet stabile Kerne.
Bruecken bilden geordnete Uebergangskerne.
Drift kann starke Selbstverdichtung bilden.
Rand bleibt bisher eher Spannungsnaehe ohne klaren Eigenkern.
Junge Oberflaechen koennen lokal selbstbindend sein, aber noch unreif.
```

Das ist wichtig:

Rand ist nicht einfach Chaos.
Drift ist nicht einfach Zerfall.
Oberflaeche ist nicht automatisch Bedeutung.

Die Feldorganisation trennt diese Zustaende bereits passiv.

## Bedeutung Fuer MINI_DIO

Fuer MINI_DIO bedeutet das:

- Die innere MCM-Matrix besitzt mehr Rollen als nur Zentrum und Rand.
- Starke Drift kann als eigene Verdichtungsform auftreten.
- Randnaehe muss nicht aktiv reguliert werden, solange sie nicht kernbildend wird.
- Junge Selbstinseln sollten beobachtet werden, nicht sofort als stabile Bedeutung gelten.

## Wie es weitergeht

Als naechstes sollte `0ykar6i` isoliert gelesen werden.
Ziel: pruefen, ob dieser Driftkern eine stabile Eigenphase traegt oder ob er nur durch eine einzelne laute Weltsequenz so stark erscheint.
