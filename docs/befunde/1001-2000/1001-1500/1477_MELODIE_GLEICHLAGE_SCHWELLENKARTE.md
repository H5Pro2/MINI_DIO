# 1477 - Melodie-Gleichlage Schwellenkarte

## Zweck

Diese Datei fasst die Befunde `1460-1476` als Schwellenkarte zusammen.

Die allgemeine Grundfrage war:

Wie bildet MINI_DIO in einer kontrollierten Melodiewelt den Uebergang zwischen zwei Bedeutungsnachbarn?

Die konkrete Unterpruefung war:

Wo liegen untere Randzone, Gleichlagenplateau und obere Kante zwischen `dio_0ein` und `dio_1fll`?

## Gepruefte Achsen

Konstant gehalten:

- synthetische Melodiefamilie,
- `block_size 13`,
- gleiche Phasenstruktur,
- gleiche Richtungswechselzahl `455`,
- `world_relative`,
- frischer Speicher je Pruefung.

Variiert:

- Amplitude / Weltlautstaerke.

## Schwellenkarte

| Bereich | Amplitude | Feldlesung | `dio_0ein` | `dio_1fll` | Differenz | Befund |
|---|---:|---|---:|---:|---:|---|
| untere Randzone | 0.00108-0.00111 | `dio_0ein`-nah | 174-175 | 173-174 | +1 bis +2 | `dio_0ein` bleibt minimal vorne |
| Gleichlagenplateau | 0.00112-0.00114 | Balance | 173 | 173 | 0 | beide Bedeutungen liegen gleich |
| obere Kante | 0.00115-0.00117 | `dio_1fll`-nah | 171-172 | 173 | -1 bis -2 | `dio_1fll` uebernimmt minimal |
| staerkere Lautstaerke | 0.00120-0.00135 | `dio_1fll`-Dominanz | 159-169 | 172-173 | -4 bis -13 | `dio_1fll` wird deutlicher dominant |

## Hauptbefund

MINI_DIO bildet keinen harten Umschaltpunkt.

Der Uebergang erscheint als Feldnaehe-Struktur:

`dio_0ein`-Randzone -> Gleichlagenplateau -> `dio_1fll`-Kante -> `dio_1fll`-Dominanz

Das ist fachlich wichtig, weil die Bedeutungsbildung damit nicht wie eine starre Symboltabelle wirkt.

Sie wirkt wie eine topologische Naeheordnung im Feld.

## Reproduzierbarkeit

Der zentrale Gleichlagenpunkt `0.00112 / block_size 13` wurde fuenfmal mit frischem Speicher reproduziert.

Alle fuenf Wiederholungen ergaben:

- `dio_0ein`: `173`
- `dio_1fll`: `173`
- Differenz: `0`
- gleiche Feldwerte fuer Rekopplung, Nachhall, stabile Wirkung und tragende Unruhe.

Damit ist dieser Punkt innerhalb der kontrollierten Weltfamilie reproduzierbar.

## Lesung Der MCM-Feldmechanik

Die Befundreihe spricht fuer ein Schwellenband, nicht fuer eine Schwelle.

Die Feldantwort haengt an einer gekoppelten Struktur:

- Weltlautstaerke,
- Blockdauer,
- Nachhall,
- Rekopplungsqualitaet,
- Symbolstreuung,
- Fokus-/Beobachtungston.

In dieser Struktur entstehen Bedeutungsnachbarn. `dio_0ein` und `dio_1fll` sind hier keine isolierten Labels, sondern benachbarte Feldrollen.

## Hypothese

Vorsichtige Forschungslesung:

MINI_DIO zeigt in dieser kontrollierten Melodiewelt eine lokale Bedeutungs-Topologie.

Diese Topologie hat:

- Randnaehe,
- Balance,
- Kante,
- Dominanzzone.

Das passt zur bisherigen MCM-Arbeit, in der Bedeutung nicht punktfoermig, sondern feldraeumlich gelesen wird.

## Grenze

Das ist kein allgemeiner Beweis fuer alle Welten.

Der Befund gilt fuer:

- diese synthetische Melodiefamilie,
- `block_size 13`,
- die bisher geprueften Amplituden,
- den aktuellen MINI_DIO-Stand.

Die Werte sind Pruefwerte, keine Regeln.
