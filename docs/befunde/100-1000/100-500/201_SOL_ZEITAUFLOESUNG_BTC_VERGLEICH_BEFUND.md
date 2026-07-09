# SOL-Zeitaufloesung und BTC-Vergleich

Stand: 2026-06-18

## Zweck

Diese Notiz prueft, ob die bei BTC beobachtete Zeitstaffelung auch bei SOL sichtbar wird.

Hierarchie der Pruefung:

1. Grundfrage: Ist zeitliche Verdichtung eine allgemeine MCM-Feldwirkung?
2. Unterpruefung: Zeigt SOL dieselbe Staffelung wie BTC?
3. Folgeschritt: Klaeren, ob unterschiedliche Welten unterschiedliche Verdichtungsempfindlichkeit besitzen.

## Ergebnis

SOL bestaetigt den Grundmechanismus:

Mit groesserer Zeitaufloesung sinken Rekopplung und Tragqualitaet, waehrend Feldspannung, Kippnaehe und Episodenmemory steigen.

Aber SOL ist deutlich empfindlicher als BTC.

Bei BTC:

- 5m und 15m bleiben in der ruhigen Naehegruppe.
- 30m bildet die Uebergangszone.
- 1h bildet den Stress-Gegenpol.

Bei SOL:

- 2025 5m bleibt ruhig tragend.
- 2024 5m ist bereits Uebergangsgruppe.
- 15m, 30m und 1h fallen in den Stress-Gegenpol.

## SOL-Werte

| Welt | Rekopplung | Tragqualitaet | field_strained | Episodenmemory | dominante Wirkung |
|---|---:|---:|---:|---:|---|
| SOL 2024 5m | `0.622776` | `0.358038` | `105` | `149` | `tragend_unruhig` |
| SOL 2024 15m | `0.606542` | `0.343678` | `266` | `309` | `tragend_unruhig` |
| SOL 2024 30m | `0.600205` | `0.341420` | `365` | `441` | `tragend_unruhig` |
| SOL 2024 1h | `0.587027` | `0.333433` | `630` | `643` | `gespannt` |
| SOL 2025 5m | `0.636504` | `0.365647` | `28` | `55` | `stabil` |
| SOL 2025 15m | `0.615512` | `0.351537` | `218` | `247` | `tragend_unruhig` |
| SOL 2025 30m | `0.600912` | `0.343351` | `402` | `434` | `tragend_unruhig` |
| SOL 2025 1h | `0.589067` | `0.335489` | `587` | `591` | `tragend_unruhig` |

## BTC-Vergleich

BTC zeigt dieselbe Richtung, aber spaeteren Kipppunkt:

| Welt | Feldlage |
|---|---|
| BTC 5m | ruhig tragend |
| BTC 15m | ruhig tragend mit mehr Spannung |
| BTC 30m | Uebergangszone |
| BTC 1h | Stress-Gegenpol |

SOL kippt frueher:

| Welt | Feldlage |
|---|---|
| SOL 5m | je nach Jahr ruhig bis Uebergang |
| SOL 15m | Stress-Gegenpol |
| SOL 30m | Stress-Gegenpol |
| SOL 1h | Stress-Gegenpol |

## Interpretation

Das spricht fuer zwei getrennte Erkenntnisse:

1. Zeitliche Verdichtung wirkt allgemein auf das MCM-Feld.
2. Jede Welt besitzt eine eigene Verdichtungsempfindlichkeit.

SOL scheint in den geprueften Abschnitten schneller in Feldlast zu kippen als BTC.

Das ist nicht einfach "mehr Volatilitaet". Es ist eine andere innere Tragbarkeit der Weltspur.

## Bedeutung fuer MINI_DIO

MINI_DIO liest nicht nur Asset, Preis oder Datenmenge.

Es entsteht eine passive Feldreaktion aus:

- Weltspur,
- Zeitverdichtung,
- Sinneskopplung,
- Rekopplung,
- Tragqualitaet,
- Kippnaehe,
- Episodenmemory.

Damit wird die MCM-Arbeit konkreter:

Eine Welt hat nicht nur Inhalt, sondern auch eine eigene zeitliche Feldmasse.

## Wie es weitergeht

Als naechstes sollte die Verdichtungsempfindlichkeit als eigene Diagnosekarte gebaut werden.

Konkrete Unterpruefung:

- pro Asset und Zeitaufloesung eine `Verdichtungs-Sensitivitaet` berechnen,
- nicht als Regel, sondern als passive Messgroesse:
  - wie schnell sinkt Rekopplung?
  - wie schnell steigt `field_strained`?
  - wie stark waechst Episodenmemory?

Ziel:

MINI_DIO soll verschiedene Welten nicht nur nach Klasse lesen, sondern nach ihrer Empfindlichkeit gegen zeitliche Verdichtung.
