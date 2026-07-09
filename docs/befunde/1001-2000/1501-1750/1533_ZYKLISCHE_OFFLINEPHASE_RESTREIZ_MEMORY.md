# 1533 - Zyklische Offlinephase Mit Restreiz Und Memory-Restreiz

## Grundfrage

Nach leerem Offline-Test und gedämpftem Restreiz wurde geprüft:

```text
Kann eine wiederholte Offlinephase alte Feldspuren erneut aktivieren,
ohne neue Außenwelt zu bekommen?
```

Die Prüfung ist weiterhin passiv. Es wird keine Handlung erzeugt und keine neue Welt eingespielt.

## Aufbau

`tools/run_sleep_offline_test.py` wurde um `--offline-mode cyclic` erweitert.

Eine Offlinephase besteht aus vier Abschnitten:

```text
Restreiz -> Leerphase -> Memory-Restreiz -> Leer-Rekopplung
```

Jeder Abschnitt dauerte im Test 20 Ticks, ein ganzer Zyklus 80 Ticks. Insgesamt wurden 320 Offline-Ticks geprüft.

## Geprüfte Welten

| Welt | Kontakt-Ticks | Offline-Ticks | Modus |
| --- | ---: | ---: | --- |
| `synthetic_1525_cyclic` | 2000 | 320 | zyklisch |
| `positive_stress_2024_cyclic` | 1999 | 320 | zyklisch |

## Ergebnisübersicht

| Welt | Schlafsymbole | Top-Schlafsymbol | Rekopplung | Restunruhe | End-Nachhall |
| --- | ---: | --- | ---: | ---: | ---: |
| `synthetic_1525_cyclic` | 1 | `dio_14wanbg` | 0.9656 | 0.0000 | 0.000686 |
| `positive_stress_2024_cyclic` | 1 | `dio_14wanbg` | 0.7938 | 0.0000 | 0.001633 |

Der wichtigste Befund:

```text
Auch zyklische Offlinephasen erzeugen keine neue Symbolstreuung.
```

## Phasenlesung

Bei `positive_stress_2024_cyclic` zeigt der erste Zyklus:

| Phase | Befund |
| --- | --- |
| `restreiz` | bleibt zunächst `offline_afterimage` |
| `leerphase` | fällt in `offline_center_rekopplung` und danach `offline_center_quiet` |
| `memory_restreiz` | hebt den Nachhall erneut an, bleibt aber meist rekoppelnd |
| `leer_rekopplung` | klingt wieder Richtung Ruhe aus |

Die aggregierte Phasenzählung zeigt:

| Welt / Phase / Zustand | Ticks |
| --- | ---: |
| `synthetic_1525`, `leer_rekopplung`, `offline_center_quiet` | 80 |
| `positive_stress_2024`, `memory_restreiz`, `offline_center_rekopplung` | 76 |
| `positive_stress_2024`, `restreiz`, `offline_afterimage` | 65 |
| `positive_stress_2024`, `leer_rekopplung`, `offline_center_quiet` | 60 |

## Interpretation

Die zyklische Offlinephase zeigt keine Traumsyntax im engeren Sinn. Sie zeigt aber mehr als reines Abschalten:

```text
Eine alte Weltspur kann offline erneut angeregt werden.
Diese Anregung bleibt an dieselbe Feldrolle gebunden.
Sie erzeugt Nachhall und Rekopplung, aber keine freie Neubenennung.
```

Das ist eine saubere Zwischenstufe:

```text
leerer Schlaf
  -> geordnetes Ausklingen

gedämpfter Restreiz
  -> verlängerte Nachhallphase

zyklischer Restreiz
  -> wiederholte Reaktivierung derselben Feldspur
```

## MCM-Lesung

Vorsichtige MCM-Lesung:

```text
Das Feld kann eine alte Spur wieder aufnehmen,
ohne eine neue Außenwelt zu brauchen.
```

Das wirkt wie eine sehr einfache unterbewusste Restverarbeitung:

- nicht bewusstes Sehen/Hören/Fühlen im Sinne neuer Sinnesdaten findet nicht statt;
- alte Feldwirkung kann wieder angeregt werden;
- Stressrest bleibt länger aktiv als strukturierter Rest;
- dennoch hält das Feld die Rekopplungsrichtung.

## Grenze

Noch nicht gezeigt ist:

- neue innere Kombination alter Bedeutungsinseln,
- aktive Traumvarianz,
- Memory-Reorganisation über mehrere unabhängige alte Spuren,
- semantische Neubildung ohne Außenwelt.

Der aktuelle Befund ist daher:

```text
MINI_DIO zeigt zyklische Offline-Reaktivierung,
aber noch keine eigenständige Offline-Bedeutungsneubildung.
```

## Nächster Prüfpunkt

Als nächstes sollte eine Doppelspur-Offlinephase geprüft werden:

```text
Kontaktwelt A -> Kontaktwelt B -> Offlinezyklus mit Restspur A/B
```

Ziel:

- bleibt nur `dio_14wanbg`?
- entsteht eine zweite Offline-Rolle?
- werden zwei alte Feldspuren getrennt gehalten?
- oder vermischt das Feld beide Spuren in eine gemeinsame Rekopplung?

