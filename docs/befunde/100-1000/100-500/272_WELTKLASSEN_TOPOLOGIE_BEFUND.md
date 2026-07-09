# Befund: Weltklassen und passive Topologie

Stand: 2026-06-19

## Zweck

Diese Datei haelt den Befund zur Pruefung von drei unterschiedlichen Weltklassen fest:

- Seitwaerts-/ruhigere Welt,
- negative Stresswelt,
- positive Expansionswelt.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Datengrundlage

Ausgewertet wurden frische `world_relative`-Laeufe:

| Welt | Datenbasis | Episoden |
|---|---|---:|
| SIDEWAYS_2026_2K | kontrolliert_2026_sideways_test1_2000_5m_SOLUSDT.csv | 1994 |
| STRESS_2023_NEG_1K | kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv | 994 |
| EXPANSION_2023_POS_1K | kontrolliert_2023_positive_expansion_test1_1000_5m_SOLUSDT.csv | 994 |

Die laengeren 10k-Laeufe wurden fuer diesen Schritt begonnen, waren aber zu schwer fuer eine schnelle Vergleichspruefung und wurden gestoppt. Fuer den aktuellen Befund wurden daher kuerzere repraesentative Fenster verwendet.

## Kurzbefund

Alle drei Weltklassen bilden denselben passiven Topologiezustand:

```text
zentrum_mit_rand_und_uebergang
```

Die Matrix zeigt:

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Sinneskopplung |
|---|---:|---:|---:|---:|---:|
| SIDEWAYS_2026_2K | 0.8024 | 0.1505 | 0.0471 | 0.6472 | 0.8654 |
| STRESS_2023_NEG_1K | 0.8410 | 0.1167 | 0.0423 | 0.6463 | 0.8661 |
| EXPANSION_2023_POS_1K | 0.8139 | 0.1519 | 0.0342 | 0.6457 | 0.8667 |

## Interpretation

Der aktuelle Befund spricht dafuer, dass die passive Rollenordnung nicht nur in einer einzelnen Welt sichtbar ist.

Wichtig ist aber die genaue Lesart:

```text
Die Weltklasse veraendert die Rollenanteile,
aber sie zerlegt die Topologie im aktuellen Fenster nicht.
```

Seitwaerts und Expansion zeigen mehr offene Variante.
Die Stresswelt zeigt in diesem kurzen Fenster sogar den hoechsten Zentrumsanteil.
Das bedeutet nicht, dass Stress immer beruhigt.
Es bedeutet nur: Unter der aktuellen weltrelativen Aufnahme wurde die negative Stresswelt nicht als randlastiger Kollaps gelesen, sondern als enger zentrierte Rollenordnung mit weniger offener Variante.

## Bedeutung fuer MINI_DIO

MINI_DIO liest unter `world_relative` weiterhin:

- Zentrum,
- offene Uebergangsvariante,
- Rand-/Kippnaehe,
- Rekopplungsqualitaet.

Damit bleibt die MCM-Feldordnung auch bei veraenderter Aussenwelt lesbar.
Der Befund stuetzt die Arbeitshypothese, dass die Topologie aus der Feldreaktion entsteht und nicht nur aus festen Symbolnamen oder harten Rohdatenwerten.

## Grenze

Dieser Befund ist noch kein Beweis fuer eine universelle MCM-Topologie.

Noch offen:

- lange 10k-Welten,
- weitere Stressfenster,
- andere Assets,
- andere Zeitebenen,
- Wiederholung mit frischem Memory,
- Vergleich gegen feste Sinnesaufnahme.

## Wie es weitergeht

Als naechstes sollte die lange Weltpruefung effizienter gemacht werden, bevor 10k-Fenster erneut laufen:

1. Laufzeitprofil fuer 10k-Laeufe messen.
2. pruefen, ob Reportausgabe oder Episodenverdichtung der Engpass ist.
3. danach je eine lange ruhige, Stress- und Expansionswelt sequenziell laufen lassen.
4. die Matrix `271` auf lange Welten erweitern oder als `273` neu schreiben.
