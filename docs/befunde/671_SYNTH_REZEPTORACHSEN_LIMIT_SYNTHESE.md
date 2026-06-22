# Synthetische Rezeptorachsen-Limit - Synthese

## Fragestellung

Welche Achse begrenzt Randlast am staerksten: Hoeren, Sehen, Feldinput oder Adaptation?

Diese Diagnose bleibt passiv. Sie beschreibt Aufnahmequalitaet vor dem MCM-Feld und ist keine Handlungsschicht.

## Vergleich

| Welt | auffaelligste Phase | Zentrum | Offen | Rand/Kipp | Lautheit | Schaerfe | Rohfeld | Adaptfeld | Reduktion |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Harmonie | `kippnaehe` | 0.9589 | 0.0167 | 0.0011 | 0.0286 | 0.8272 | 0.0278 | 0.0253 | 0.0026 |
| Bruch/Rand | `randflackern` | 0.2871 | 0.4971 | 0.0043 | 0.1454 | 0.6242 | 0.0938 | 0.0808 | 0.0130 |
| Randdominanz | `laute_randphase` | 0.0762 | 0.7113 | 0.0600 | 0.2779 | 0.5375 | 0.1644 | 0.1353 | 0.0291 |

## Befund

Die Randlast steigt nicht durch eine einzelne isolierte Achse. Sie entsteht als Kopplung:

- Hoeren liefert die Reizspitze: Lautheit steigt von Harmonie zu Bruch/Rand zu Randdominanz deutlich.
- Sehen verliert Stabilitaet: die visuelle Schaerfe faellt besonders in `randflackern` und `laute_randphase`.
- Feldinput nimmt zu: Rohfeldaufnahme steigt in denselben Phasen deutlich.
- Adaptation begrenzt: die adaptierte Feldaufnahme bleibt unter der Rohaufnahme; die Reduktion steigt genau dort, wo die Welt lauter und offener wird.

## Schluss

Die wichtigste Begrenzungsachse ist bisher nicht ein einzelner Sinneskanal, sondern die rezeptorische Adaptation vor dem MCM-Feld.

Hoeren und Sehen bestimmen die Reizqualitaet:

- Hoeren macht Weltspannung laut.
- Sehen verliert unter Randlast Schaerfe.
- Feldinput traegt die Aufnahme in Richtung MCM-Feld.

Die Adaptation entscheidet, wie stark diese Aufnahme als Feldwirkung durchgelassen wird.

## Bedeutung fuer MINI_DIO

Das stuetzt die aktuelle Architektur:

```text
Weltkontakt
  -> getrennte Sinnesaufnahme
  -> Rezeptorschicht
  -> adaptierte Feldaufnahme
  -> MCM-Feldwirkung
  -> passive Innenfeldrolle
```

Damit wirkt die Rezeptorschicht nicht wie ein starrer Limiter. Sie wirkt eher wie eine organische Aufnahmegrenze: Weltspannung bleibt sichtbar, aber sie wird nicht ungeordnet in das MCM-Feld geworfen.

## Offene Grenze

Der Befund gilt bisher fuer die geprueften synthetischen Welten. Er zeigt noch nicht, wie stark die Adaptation bei echten, sehr langen Weltfolgen oder bei anderen Weltarten tragen kann.

Wie es weitergeht: Als naechstes sollte die Achsendiagnose auf echte Assetwelten angewendet werden, damit klar wird, ob dieselbe Begrenzungslogik auch ausserhalb synthetischer Phasen stabil bleibt.
