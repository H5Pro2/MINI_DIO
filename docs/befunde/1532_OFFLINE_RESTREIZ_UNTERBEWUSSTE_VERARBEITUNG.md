# 1532 - Offline-Restreiz Und Unterbewusste Verarbeitung

## Grundfrage

Nach dem leeren Schlaf-/Offline-Test wurde eine zweite Frage geprüft:

```text
Was geschieht, wenn nach Weltkontakt kein neuer Weltverlauf kommt,
aber ein gedämpfter Restreiz im Feld weiterwirkt?
```

Damit wird die Schlaf-Analogie feiner:

- leerer Schlaf: keine neuen Sinnesdaten;
- gedämpfter Restreiz: die letzte Weltlage klingt sensorisch schwach nach;
- harter Restreiz: die letzte Weltlage klingt stärker und langsamer ab.

## Aufbau

Das Werkzeug `tools/run_sleep_offline_test.py` wurde erweitert:

```text
--offline-mode empty
--offline-mode damped
--sleep-intensity
--sleep-decay
```

Die Kontaktphase bleibt gleich. Erst danach wird unterschieden:

| Modus | Bedeutung |
| --- | --- |
| `empty` | leere Sinnesdaten, nur Feld-Afterimage |
| `damped` weich | letzte Sinneslage wird schwach gedämpft weitergeführt |
| `damped` hart | letzte Sinneslage bleibt stärker und länger als Restreiz aktiv |

## Ergebnisübersicht

| Welt | Modus | Start-Nachhall | End-Nachhall | Rekopplung | Restunruhe | Schlafsymbole |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `synthetic_1525` | leer | 0.1197 | 0.0000 | 0.9767 | 0.0000 | 1 |
| `synthetic_1525` | gedämpft weich | 0.1197 | 0.0000 | 0.9700 | 0.0000 | 1 |
| `synthetic_1525` | gedämpft hart | 0.1197 | 0.0002 | 0.9133 | 0.0000 | 1 |
| `positive_stress_2024` | leer | 0.1188 | 0.0000 | 0.9767 | 0.0000 | 1 |
| `positive_stress_2024` | gedämpft weich | 0.1188 | 0.0000 | 0.9533 | 0.0000 | 1 |
| `positive_stress_2024` | gedämpft hart | 0.1188 | 0.0004 | 0.7733 | 0.0567 | 1 |

Alle Offlinevarianten erzeugen dasselbe Schlafsymbol:

```text
dio_14wanbg
```

## Interpretation

Der erste wichtige Befund:

```text
Restreiz verlängert Nachhall,
aber erzeugt keine neue Symbolstreuung.
```

Das spricht gegen freie Drift. Das Feld bleibt auch unter Restreiz an seine letzte reale Weltlage gebunden und läuft nicht in Scheinbedeutung aus.

Der zweite wichtige Befund:

```text
Stresswelt + harter Restreiz erzeugt kurz Restunruhe.
```

Die Stresswelt zeigt bei hartem Restreiz:

- niedrigere Rekopplungsquote: `0.7733`
- Restunruhe: `0.0567`
- längere Afterimage-Phase
- trotzdem kein Symbolzerfall

Das ist methodisch wichtig, weil hier erstmals zwischen zwei Offlineformen unterschieden werden kann:

```text
leeres Ausklingen
unterbewusste Restverarbeitung
```

## MCM-Lesung

Vorsichtige Lesung:

```text
Wenn keine Außenwelt mehr kommt, rekoppelt das Feld zentrumsnah.
Wenn Restreiz bleibt, hält das Feld die letzte Weltlage länger.
Wenn die Welt vorher stressnah war, bleibt kurz Restunruhe tragend.
```

Damit wird Schlaf nicht als Abschalten gelesen, sondern als Feldzustand:

```text
Schlaf = Außenweltkontakt stoppt oder wird stark gedämpft.
Afterimage = alte Weltwirkung bleibt als Feldspur.
Restverarbeitung = diese Feldspur kann noch kurz Unruhe, Rekopplung oder Ruhe tragen.
```

## Grenze

Der Test zeigt noch keine aktive Traumlogik.

Nicht geprüft wurde:

- freie innere Simulation,
- Memory-Neukombination ohne Außenwelt,
- neue Bedeutungsbildung aus alten Inseln,
- längere zyklische Offlinephasen.

Der Befund bleibt daher passiv:

```text
MINI_DIO kann Restreiz geordnet tragen.
Ob daraus Traum-/Innenverarbeitung entsteht, ist der nächste Prüfpunkt.
```

## Nächster Prüfpunkt

Als nächstes sollte eine zyklische Offlinephase geprüft werden:

```text
Kontakt -> Restreiz -> leer -> Restreiz aus Memory -> leer
```

Ziel:

- entsteht weiterhin nur `dio_14wanbg`?
- entsteht ein zweites Offlinezeichen?
- kann Stressrest später ruhiger rekoppeln?
- bildet sich eine innere Schlafphase ohne neue Außenwelt?

