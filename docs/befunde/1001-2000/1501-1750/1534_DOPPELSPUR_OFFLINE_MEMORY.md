# 1534 - Doppelspur-Offlinephase

## Grundfrage

Nach der zyklischen Offlinephase wurde geprüft:

```text
Kann MINI_DIO zwei vorherige Feldspuren offline getrennt halten?
```

Die Prüfung nutzt zwei Kontaktwelten nacheinander:

```text
Kontaktwelt A -> Kontaktwelt B -> Offlinezyklus
```

Im Offlinezyklus wirkt:

- `restreiz` aus der letzten Kontaktwelt B;
- `memory_restreiz` aus der vorherigen Kontaktwelt A;
- dazwischen jeweils Leerphasen.

## Aufbau

`tools/run_sleep_offline_test.py` wurde um eine zweite Kontaktwelt erweitert:

```text
--second-data
--second-contact-ticks
```

Geprüft wurden zwei Reihenfolgen:

| Label | Kontakt A | Kontakt B |
| --- | --- | --- |
| `structured_then_stress` | synthetische Strukturwelt | positive Stresswelt 2024 |
| `stress_then_structured` | positive Stresswelt 2024 | synthetische Strukturwelt |

## Ergebnis

| Lauf | A-Symbole | A-Top | B-Symbole | B-Top | Offline-Symbole | Rekopplung | Restunruhe |
| --- | ---: | --- | ---: | --- | ---: | ---: | ---: |
| `structured_then_stress` | 88 | `dio_0l7pvdk` | 203 | `dio_104t4us` | 1 | 0.9563 | 0.0000 |
| `stress_then_structured` | 274 | `dio_104t4us` | 78 | `dio_1wdik71` | 1 | 0.9438 | 0.0063 |

In beiden Fällen ist das Offline-Symbol:

```text
dio_14wanbg
```

## Interpretation

Die Kontaktphase unterscheidet A und B klar:

- Strukturwelt und Stresswelt erzeugen unterschiedliche Symbolbreiten;
- Reihenfolge verändert die Kontakt-Toprollen;
- Stress zuerst hinterlässt mehr Anfangsnachhall.

Die Offlinephase trennt die beiden Spuren aber noch nicht als eigene Offlinezeichen. Stattdessen entsteht wieder eine gemeinsame Rekopplungsrolle.

Vorläufiger Befund:

```text
MINI_DIO kann zwei Weltkontakte im Feld nacheinander tragen,
aber die aktuelle Offline-Schicht verdichtet sie noch auf eine gemeinsame Rekopplung.
```

Das ist methodisch wichtig. Es zeigt eine Grenze:

```text
Offline-Rekopplung ist stabiler als Offline-Differenzierung.
```

## MCM-Lesung

Die Doppelspurprüfung spricht für:

- stabile Zentrumstendenz nach Weltkontakt;
- starke Bindung an `dio_14wanbg` als Offline-Rekopplungsrolle;
- leichte Restunruhe, wenn Stress vor Struktur kam;
- noch keine getrennte Offline-Memory-Semantik.

Damit ist die aktuelle technische Schlafschicht eher:

```text
Feldberuhigung / Rekopplung
```

und noch nicht:

```text
Traumhafte Kombination getrennter alter Bedeutungsinseln
```

## Grenze

Der Test sagt nicht, dass getrennte Offline-Spuren unmöglich sind. Er zeigt nur:

```text
Mit der aktuellen einfachen Restreiz-Abbildung reicht die Offlinephase noch nicht,
um zwei alte Weltkontakte als getrennte innere Spuren zu halten.
```

Für echte Offline-Differenzierung müsste die alte Spur nicht nur als letzter Sinneszustand, sondern als verdichtete MCM-Episode zurückgeführt werden.

## Nächster Prüfpunkt

Als nächstes sollte geprüft werden:

```text
Offline-Restreiz nicht aus letzter Sinneslage,
sondern aus gespeicherter MCM-Episodenrolle.
```

Ziel:

- bleibt `dio_14wanbg` dominant?
- entsteht eine zweite Offline-Rolle?
- können A- und B-Spur getrennt aktiviert werden?
- oder ist das Feld im Schlaf primär zentrumsrückführend?

