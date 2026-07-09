# 1530 - Stress-Memory-Wiederverwendung

## Grundfrage

Nach dem Memory-Test auf einer strukturierten Mosaikwelt wurde dieselbe Frage unter Feldlast geprüft:

```text
Bleibt Bedeutungswiederverwendung auch unter Stress stabil,
oder driftet sie in neue Rand- und Nebelzonen?
```

Die Prüfung ist eine Fortsetzung der Anti-Pareidolie-Grenze. Wenn Memory nur oberflächliche Benennung wäre, müsste eine Stress-Holdout-Welt starke Neubenennung oder deutliche Feldkartenauflösung zeigen.

## Aufbau

Es wurden drei Läufe mit isolierter Debug-Memory ausgeführt:

1. **A - Stress frisch**
   - `data/kontrolliert_2024_positive_stress_test1_2000_5m_SOLUSDT.csv`
   - Memory vorher gelöscht
2. **B - gleiche Stresswelt ohne Reset**
   - gleiche Welt
   - gleiche Memory wie A
3. **C - negative Stress-Holdout-Welt**
   - `data/kontrolliert_2024_negative_stress_test1_1000_5m_SOLUSDT.csv`
   - gleiche Memory wie A und B

Alle Läufe blieben passiv. Es wurden keine Handlungen, Gates oder Richtungsvorgaben geprüft.

## Ergebnis

| Lauf | Welt | Symbole | stabil | Unruhe | Kippnähe | Nachhall | Feldzeit-Vertrauen | Feldzeit-Vorsicht | Bedeutungsanzeige | Feldkarten-Ähnlichkeit |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A | positiver Stress frisch | 345 | 0.7638 | 0.2312 | 0.0050 | 0.1448 | 0.5958 | 0.2489 | 0 / 1994 | - |
| B | positiver Stress wiederholt | 345 | 0.7633 | 0.2317 | 0.0050 | 0.1448 | 0.5958 | 0.2489 | 1532 / 462 | 0.9995 |
| C | negativer Stress-Holdout | 266 | 0.7586 | 0.2344 | 0.0070 | 0.1062 | 0.5098 | 0.3030 | 761 / 233 | 0.9965 |

Die Kernrollen verschieben sich innerhalb des Stressraums:

| Lauf | dominante Rollen |
| --- | --- |
| A | `dio_0m9z`, `dio_104t`, `dio_0l7p`, `dio_155c`, `dio_14wj` |
| B | gleiche Rollen, verdoppelte Memory-Zähler |
| C | `dio_155c`, `dio_104t`, `dio_0h9h`, `dio_0m9z`, `dio_0l7p` |

## Interpretation

### A nach B

Der zweite Stresslauf erzeugt keine neue Symbolstreuung:

- `unique_symbols` bleibt `345`
- Nachhall bleibt `0.1448`
- Feldzeit-Vertrauen bleibt `0.5958`
- Feldkarten-Ähnlichkeit liegt bei `0.9995`
- `meaning_display_found` steigt von `0` auf `1532`

Das bedeutet: Auch unter Stress kann MINI_DIO bekannte Bedeutungsrollen wieder aktivieren. Die Memory wirkt nicht als Beruhigung der Welt, sondern als Wiedererkennung der bekannten Feldlage.

### B nach C

Die negative Stress-Holdout-Welt bleibt mit der Stress-Feldkarte verwandt, aber sie trägt schwerer:

- weniger Symbole: `266`
- niedrigerer Nachhall: `0.1062`
- niedrigeres Feldzeit-Vertrauen: `0.5098`
- höhere Feldzeit-Vorsicht: `0.3030`
- Kippnähe steigt leicht auf `0.0070`

Trotzdem bleibt die Feldkarten-Ähnlichkeit hoch (`0.9965`). Das spricht gegen bloße Neubenennung. Die Welt koppelt an den bekannten Stressraum an, verschiebt aber seine Gewichtung.

## Befund

Der Test stützt diese Lesart:

```text
MINI_DIO kann auch unter Feldlast bekannte Bedeutungsräume wiederverwenden.
Stress bleibt dabei Stress.
Memory hebt die Last nicht auf, sondern macht sie wiedererkennbar.
```

Das ist methodisch wichtig: Die Stresswelt wird nicht zur ruhigen Welt umgedeutet. Das Feld erkennt eine verwandte Lastlage und trägt sie mit ähnlicher Karte, aber niedrigerer Feldzeit und höherer Vorsicht.

## Grenze

Der Befund beweist keine bewusste Verarbeitung. Er zeigt eine passive Wiederverwendung von Feldrollen unter Last. Ob daraus später aktive Selbstregulation entstehen kann, muss getrennt geprüft werden.
