# 1717 - Synthetische Zweierkopplungs-Bruchklassen der Oeffnungs-Vorform

Stand: 2026-07-07 23:29:14

## Zweck

Diese Diagnose klassifiziert, welche synthetischen Zweierkopplungen die reale Oeffnungs-Vorform tragen oder brechen.
Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.

## Hierarchie

1. Grundfrage: Welche Zweierkopplung bricht die Oeffnungs-Vorform?
2. Unterpruefung: Range+Hoeren, Range+Spannung und Hoeren+Spannung getrennt lesen.
3. Folgeschritt: Gegen Einzelachsen und volle Dreierlast verdichten.

## Klassifikation

| Welt | Familie | Vorkommen | Delta Hoeren | Delta Spannung | Delta Range | Klasse |
|---|---|---:|---:|---:|---:|---|
| SYN_PAIR_RANGE_HEARING | dio_0ly7 | 58 | 0.007884 | 0.007187 | 0.011778 | bruch_mit_range_aufweitung |
| SYN_PAIR_RANGE_TENSION | dio_0ly7 | 27 | 0.002677 | 0.003837 | 0.005169 | bruch_mit_range_aufweitung |
| SYN_PAIR_HEARING_TENSION | dio_0ly7 | 10 | -0.016061 | -0.011666 | 0.002629 | oeffnung_getragen |

## Lesung

`dio_0ly7` zeigt gemischte Reaktion: einige Welten tragen die Entlastung, andere brechen sie. Damit ist die Form achsensensitiv und muss je Stoerklasse getrennt gelesen werden.

## Grenze

```text
Bruchklasse = passive Felddiagnose
keine Handlungsregel
keine Aussage ueber Absicht
```

## Quelle

- `docs/befunde/1001-2000/1501-1750/1716_DIO_0LY7_ZWEIERKOPPLUNG.csv`

## Wie es weitergeht

Als naechstes sollte die Zweierkopplung direkt gegen Einzelachsen und volle Dreierlast verdichtet werden: welche Kopplungsqualitaet bricht `dio_0ly7` wirklich?
