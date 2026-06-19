# Befund: Reproduzierbarkeit langer Weltklassen

Stand: 2026-06-19

## Zweck

Diese Datei haelt den Reproduzierbarkeitstest der langen `world_relative`-Topologie fest.

Geprueft wurde:

```text
Gleiche Welt + frisches Memory -> bildet MINI_DIO dieselbe passive Rollenordnung erneut?
```

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Testaufbau

Die drei 10k-Welten aus Befund `273` wurden erneut mit frischem Memory gestartet:

| Welt | Kerzen | Modus |
|---|---:|---|
| STABLE_2026_10K_REPRO | 10000 | world_relative |
| STRESS_2023_NEG_10K_REPRO | 10000 | world_relative |
| EXPANSION_2023_POS_10K_REPRO | 10000 | world_relative |

Die neue Matrix liegt in:

```text
docs/befunde/275_REPRO_LANGE_WELTKLASSEN_TOPOLOGIE_MATRIX.md
```

## Reproduktionsbefund

Der direkte Delta-Vergleich gegen die vorherige 10k-Matrix ergab:

```text
delta_share                 = 0.00000000
delta_avg_rekopplung        = 0.00000000
delta_avg_carry             = 0.00000000
delta_avg_strain            = 0.00000000
delta_avg_sensory           = 0.00000000
delta_rekopplung_top_share  = 0.00000000
delta_strain_top_share      = 0.00000000
```

Das gilt fuer alle drei Welten und alle drei Rollen:

- zentrum_stabil,
- offene_variante,
- spannungsrand_kippnaehe.

## Interpretation

Fuer gleiche Datenwelt und frisches Memory ist die passive Topologie aktuell exakt reproduzierbar.

Das bedeutet:

```text
Die Rollenordnung ist im aktuellen Aufbau keine zufaellige Memory-Laune.
Sie entsteht deterministisch aus Welt, Sinnesaufnahme und MCM-Feldreaktion.
```

Wichtig: Das ist kein Beweis fuer eine universelle MCM-Topologie.
Es ist aber ein starker Befund fuer interne Reproduzierbarkeit unter kontrollierten Bedingungen.

## Bedeutung fuer MINI_DIO

MINI_DIO speichert in diesem Test nicht wahllos neue Information.
Bei gleicher Welt entstehen dieselben Rollenanteile erneut.

Damit wird die These staerker:

```text
MINI_DIO bildet eine weltbezogene Innenfeldordnung,
die wiederholbar aus der gegebenen Welt hervorgeht.
```

Das passt zur bisherigen MCM-Arbeitshypothese:

- Welt wirkt als Energie-/Sinnesstruktur,
- das MCM-Feld bildet daraus Innenfeldrollen,
- wiederkehrende Rollen koennen als Bedeutungsraeume gelesen werden.

## Technische Grenze

Die 10k-Laeufe sind trotz Optimierung noch teuer:

| Welt | Laufzeit |
|---|---:|
| STABLE_2026_10K_REPRO | ca. 144.9 s |
| STRESS_2023_NEG_10K_REPRO | ca. 136.8 s |
| EXPANSION_2023_POS_10K_REPRO | ca. 135.6 s |

Fuer groessere Tests sollte weiter profiliert werden, bevor Jahreswelten oder mehrere Wiederholungen breit gestartet werden.

## Forschungsgrenze

Der Befund sagt:

```text
gleiche Welt -> gleiche passive Rollenmatrix
```

Er sagt noch nicht:

```text
andere Welt -> gleiche Topologie immer
```

Das bleibt eine eigene Pruefung.

## Wie es weitergeht

Als naechstes sollte nicht sofort noch breiter getestet werden.
Sinnvoller ist der naechste hierarchische Schritt:

1. eine deutlich andere Welt nehmen,
2. dieselbe Matrix bilden,
3. pruefen, ob die Rollenordnung erhalten bleibt oder ob echte neue Topologieklassen entstehen.

Damit trennen wir Reproduzierbarkeit von Anpassungsfaehigkeit.
