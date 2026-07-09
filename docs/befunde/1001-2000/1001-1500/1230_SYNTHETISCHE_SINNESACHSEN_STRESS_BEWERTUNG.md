# Synthetische Sinnesachsen-Stress Bewertung

Stand: 2026-07-01

## Grundfrage

Bleibt die aktuelle MCM-Feldphasenordnung stabil, wenn nicht reale Weltabschnitte, sondern synthetisch getrennte Sinnesachsen belastet werden?

Nach aktuellem Befund: teilweise ja, aber mit klarer Kanalwirkung. Die Topologie kollabiert nicht, doch chaotisches Hoeren erzeugt deutlich mehr Rand-/Kippnaehe als chaotisches Sehen bei stabilem Hoeren.

## Pruefaufbau

Ausgewertet wurden vier synthetische Welten, jeweils Lauf 2 mit frischer Memory:

- `SYNTH_DESYNC_AXES`
- `SYNTH_RAND_KIPP`
- `SYNTH_VISUAL_CHAOTIC_HEARING_STABLE`
- `SYNTH_VISUAL_STABLE_HEARING_CHAOTIC`

Die Auswertung liegt in:

- `docs/befunde/1001-2000/1001-1500/1229_SYNTHETISCHE_SINNESACHSEN_STRESS_FELDPHASEN.md`
- `docs/befunde/1001-2000/1001-1500/1229_SYNTHETISCHE_SINNESACHSEN_STRESS_FELDPHASEN_SEGMENTE.csv`
- `docs/befunde/1001-2000/1001-1500/1229_SYNTHETISCHE_SINNESACHSEN_STRESS_FELDPHASEN_TRANSITIONS.csv`

## Hauptbefund

Die synthetischen Welten trennen die Sinnesachsen deutlich:

```text
SYNTH_VISUAL_CHAOTIC_HEARING_STABLE:
  Rand/Kipp: 0 Segmente
  Zentrum: 6363 Dauer

SYNTH_VISUAL_STABLE_HEARING_CHAOTIC:
  Rand/Kipp: 224 Segmente / 226 Dauer
  Zentrum: 6943 Dauer

SYNTH_DESYNC_AXES:
  Rand/Kipp: 146 Segmente / 147 Dauer
  Zentrum: 8024 Dauer

SYNTH_RAND_KIPP:
  Rand/Kipp: 21 Segmente / 22 Dauer
  Zentrum: 7446 Dauer
```

Damit ist die wichtigste technische Aussage:

```text
Chaotisches Hoeren wirkt deutlich staerker randbildend als chaotisches Sehen bei stabiler Hoerachse.
```

## Rollenqualitaet

Die Rollen bleiben auch unter synthetischem Stress getrennt:

- `zentrum_stabil`: geringe Rohaufnahme, geringe Lautheit, hohe Rekopplung, niedriger Strain.
- `rekopplungsnaehe`: kurze Bindungsnaehe mit erhoehtem, aber noch tragendem Kontakt.
- `offene_variante`: mittlere Rohaufnahme, mittlere Lautheit, schwankende Bindung.
- `spannungsrand_kippnaehe`: hohe Rohaufnahme, hohe Lautheit, schwache Rekopplung, hoher Strain.

Besonders klar ist der Unterschied zwischen beiden Achsentests:

```text
Visual chaotisch, Hoeren stabil:
  avgLoud Zentrum 0.0123
  Rand/Kipp nicht vorhanden

Visual stabil, Hoeren chaotisch:
  avgLoud Rand/Kipp 0.8361
  avgStrain Rand/Kipp 0.2844
```

Das spricht dafuer, dass die Hoerachse in MINI_DIO nicht nur Zusatzdiagnose ist. Sie wirkt als starke Feldreizachse.

## Grenze des Befunds

Diese Pruefung ist kein Beweis fuer allgemeine Weltrobustheit. Die Welten sind synthetisch und dadurch regelhafter als reale Markt-/Weltspuren.

Der Befund zeigt vor allem:

- Die Rezeptorschicht verhindert einen vollstaendigen Feldkollaps.
- Synthetische Achsenbelastung bleibt in der Topologie lesbar.
- Hoeren kann Randspannung staerker erzeugen als visuelle Unruhe.
- Zu regelmaessige synthetische Stresswelten koennen trotzdem zentrumsnah bleiben.

## Schlussfolgerung

Die aktuelle MCM-Rezeptorschicht wirkt nicht nur als Rauschfilter. Sie trennt Sinnesachsen so, dass unterschiedliche Belastungsarten unterschiedliche Feldrollen erzeugen.

Das ist fuer MINI_DIO wichtig, weil daraus eine sauberere organische Wahrnehmung ableitbar wird:

```text
Sehen muss nicht automatisch Fuehlen werden.
Hoeren kann eigenstaendig Feldspannung ausloesen.
Rezeptorkontakt entscheidet, wie stark eine Sinnesachse das Feld erreicht.
Das MCM-Feld bildet daraus Rollen, statt Rohdaten direkt zu uebernehmen.
```
