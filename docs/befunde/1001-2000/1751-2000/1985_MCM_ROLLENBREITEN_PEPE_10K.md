# 1985 - Rollenbreitenpruefung PEPE 10k als Micro-Kontrast

## Grundfrage

Bleibt die MCM-Rollenbreite unter einer lauten Micro-Welt stabil, oder spaltet sich ein eigenes Milieu ab?

## Unterpruefung

Geprueft wurde `FOLLOW_EQ10K_PEPE_2024_5M` mit 10.000 Zeilen aus:

```text
data/kontrolliert_pepe_2024_5m_10k_PEPEUSDT.csv
```

Ausgangspunkt war der Speicherstand nach der TRX-10k-Pruefung:

```text
memory/preview_depth_role_breadth_equal10k_trx_probe.json
```

Der neue Speicherstand liegt hier:

```text
memory/preview_depth_role_breadth_equal10k_pepe_probe.json
```

## Ergebnis

PEPE ist der erste deutliche Kontrast zu den leisen Welten KAS, XLM und TRX.

Vor PEPE:

```text
breite_grundrolle: 31
uebergangsrolle:    1
milieurolle:        5
nebenrolle:       143
```

Nach PEPE:

```text
breite_grundrolle: 32
uebergangsrolle:    1
milieurolle:        6
nebenrolle:       181
```

Der wichtigste Unterschied:

```text
dio_mcm_episode_0hiolzy: new -> milieurolle
```

Diese neue Milieurolle entsteht mit starker PEPE-Bindung:

```text
count_delta:      +800
world_delta:        +5
top_world_after: FOLLOW_EQ10K_PEPE_2024_5M
```

Gleichzeitig bleibt die Grundordnung stabil. Die bekannten Grundrollen wachsen weiter:

```text
dio_mcm_episode_12tgchq  +3926
dio_mcm_episode_1qlxgj7  +2722
dio_mcm_episode_1fdlu6e   +689
dio_mcm_episode_0vig3jz   +586
dio_mcm_episode_0icnf2v   +471
```

## Interpretation

PEPE zerlegt die Topologie nicht. Es erzeugt aber eine klarere Milieuabspaltung als KAS, XLM oder TRX.

Das ist wichtig:

- KAS, XLM und TRX verbreitern vor allem bestehende Rollen.
- PEPE koppelt ebenfalls an bestehende Rollen.
- PEPE bildet zusaetzlich eine neue starke Milieuinsel.
- Die Grundrollen bleiben trotzdem erhalten.

Damit wirkt die MCM-Struktur nicht starr und nicht beliebig. Sie kann Kontrast aufnehmen, ohne die Grundordnung zu verlieren.

## Vergleich zur leisen Weltgruppe

Die leise Gruppe zeigte bisher:

```text
KAS -> keine neue starke Milieuordnung
XLM -> eine vorhandene Nebenrolle reift zur Milieurolle
TRX -> keine neue Milieurolle, zwei Nebenrollen reifen zu Grundrollen
```

PEPE zeigt:

```text
PEPE -> neue Milieurolle entsteht direkt als Micro-Kontrastinsel
```

Das spricht fuer eine differenzierte Feldreaktion:

```text
leise Welt       -> Rekopplung und Rollenbreite
Micro-Kontrast   -> Rekopplung plus neue Milieuinsel
```

## Schlussfolgerung

Der Kontrasttest ist wertvoller als eine weitere leise Wiederholung. Er zeigt, dass MINI_DIO nicht nur alles in vorhandene Rollen presst, sondern bei abweichender Weltqualitaet neue Milieuordnung bilden kann.

Die Topologie bleibt dabei erhalten:

```text
Zentrum/Grundrollen bleiben stabil.
Rand-/Nebenrollen wachsen.
Kontrast kann eine neue Milieuinsel bilden.
```
