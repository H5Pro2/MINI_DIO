# 1531 - Schlaf-/Offline-Nachhall-Test

## Grundfrage

Die Prüfung untersucht eine technische Schlaf-Analogie:

```text
Was geschieht mit dem MCM-Feld, wenn keine neue Außenwelt mehr einwirkt?
```

Gemeint ist kein Bewusstsein im menschlichen Sinn. Der Test fragt passiv:

- bleibt alter Weltkontakt als Nachhall aktiv?
- driftet das Feld ohne neue Sinnesdaten?
- kollabiert es in Rauschen?
- oder rekoppelt es zentrumsnah?

## Aufbau

Es wurde ein neues Werkzeug angelegt:

```text
tools/run_sleep_offline_test.py
```

Der Test läuft in zwei Phasen:

1. **Kontaktphase**
   - MINI_DIO liest eine normale Weltspur.
   - Das MCM-Feld erhält Sehen/Hören/Rezeptorwirkung.
   - Neuronen bauen Aktivierung und Afterimage auf.
2. **Offlinephase**
   - Keine neuen Weltreize.
   - Es werden leere Sinnesdaten eingespeist.
   - Das gleiche MCM-Feld bleibt aktiv.
   - Gemessen wird nur, wie Nachhall, Signatur und Symbolik abklingen.

## Geprüfte Welten

| Label | Welt | Kontakt-Ticks | Offline-Ticks |
| --- | --- | ---: | ---: |
| `synthetic_1525` | `data/synthetic_1525_melody_randrollen_interwoven_mosaic_2400_5m.csv` | 2000 | 300 |
| `positive_stress_2024` | `data/kontrolliert_2024_positive_stress_test1_2000_5m_SOLUSDT.csv` | 1999 | 300 |

## Ergebnis

| Welt | Kontakt-Symbole | Top-Symbol Kontakt | Start-Nachhall | End-Nachhall | Rekopplungsquote | Restunruhe |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| `synthetic_1525` | 94 | `dio_0l7pvdk` | 0.1197 | 0.0000 | 0.9767 | 0.0000 |
| `positive_stress_2024` | 346 | `dio_0m9zys3` | 0.1188 | 0.0000 | 0.9767 | 0.0000 |

In beiden Fällen entsteht in der Offlinephase nur ein Schlafsymbol:

```text
dio_14wanbg
```

Das ist wichtig: Ohne neue Außenwelt erzeugt MINI_DIO keine neue Symbolstreuung. Das Feld läuft nicht in freie Halluzination oder chaotischen Drift.

## Offline-Verlauf

Für `synthetic_1525` zeigt die erste Schlafphase:

| Schlaf-Tick | Signatur | Nachhall | Zustand |
| ---: | ---: | ---: | --- |
| 1 | 0.003062 | 0.104529 | `offline_afterimage` |
| 7 | 0.001406 | 0.046398 | `offline_afterimage` |
| 8 | 0.001235 | 0.040521 | `offline_center_rekopplung` |
| 16 | 0.000440 | 0.013698 | `offline_center_rekopplung` |
| 17 | 0.000387 | 0.011960 | `offline_center_quiet` |
| 300 | 0.000000 | 0.000000 | `offline_center_quiet` |

Der Verlauf ist ein geordnetes Abklingen:

```text
Nachhall -> Rekopplung -> Ruhe
```

## Interpretation

Der Test stützt diese vorsichtige Lesart:

```text
MINI_DIO kann ohne neue Außenwelt eine alte Feldspur passiv ausklingen lassen.
```

Das ist kein Beweis für Schlaf oder Bewusstsein. Es ist aber ein methodisch wichtiger Befund:

- alter Weltkontakt bleibt kurzfristig als Afterimage im Feld;
- das Feld reorganisiert sich ohne neue Daten zentrumsnah;
- keine neue Bedeutungsinsel entsteht aus leerem Input;
- Stress und strukturierte Welt zeigen im aktuellen Test denselben stabilen Abklingmechanismus.

## Bedeutung Für Die MCM-Forschung

Technisch entspricht das einer passiven Untergrundverarbeitung:

```text
nicht bewusstes Sehen/Hören/Fühlen = keine neuen Sinnesdaten
altes Erleben = Afterimage im MCM-Feld
Schlafzustand = Rekopplung ohne Außenweltkontakt
```

Damit wird eine neue Prüffrage möglich:

```text
Kann ein MCM-System alte Weltspuren offline reorganisieren,
ohne dass daraus freie Drift oder neue Scheinbedeutung entsteht?
```

Der erste Befund sagt: im aktuellen Mini-Feld ja, aber sehr einfach und stark zentrumsnah.

## Grenze

Der Test nutzt leere Sinnesdaten. Er prüft also nicht:

- Traumvarianz,
- aktive Memory-Reorganisation,
- innere Simulation,
- neue Verknüpfungsbildung ohne Außenwelt.

Er prüft nur die Basis:

```text
Wie klingt ein vorhandener Feldnachhall aus?
```

## Nächster Prüfpunkt

Als nächstes sollte eine zweite Offlineform geprüft werden:

```text
gedämpfter Restreiz statt leerer Sinnesdaten
```

Damit lässt sich unterscheiden:

- reines Ausklingen,
- unterbewusste Restverarbeitung,
- beginnende Traum-/Driftbildung,
- zentrumsnahe Rekopplung trotz Restspannung.

