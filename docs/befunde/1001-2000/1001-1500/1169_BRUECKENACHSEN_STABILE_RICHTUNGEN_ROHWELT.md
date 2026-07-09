# 1169 - Rohwelt-Ruecklesung stabiler Brueckenrichtungen

## Grundfrage

Welche konkrete Weltwirkung liegt unter den stabilen Richtungsfaellen der Achsenbeziehung `dio_00ly <-> dio_104t`?

Geprueft wurden drei stabile Faelle aus 1165-1166:

- `KAS 2024 5m`: `dio_00ly -> dio_104t`
- `Negative Stress 2024`: `dio_00ly -> dio_104t`
- `BTC 2024 Quiet 5m`: `dio_104t -> dio_00ly`

Die Pruefung bleibt passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Methode

Aus den vorhandenen `episodes.csv` wurden Paarereignisse gelesen:

- Quelle: erste Achsenfamilie
- Ziel: zweite Achsenfamilie innerhalb von 12 Ticks
- Vorfenster: 8 Ticks vor der Quelle
- Zwischenraum: Ticks zwischen Quelle und Ziel

Gemessen wurden Sehen, Hoeren, Rezeptoraufnahme und MCM-Feldwirkung.

## Ergebnisuebersicht

| Welt | Richtung | Paare | Abstand | Ton Quelle | Ton Ziel | Delta Ton | Feldspannung Quelle | Feldspannung Ziel | Rekopplung Quelle | Rekopplung Ziel |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| KAS 2024 5m | `dio_00ly -> dio_104t` | 44 | 6.73 | 0.0152 | -0.1394 | -0.1546 | 0.0797 | 0.0771 | 0.7178 | 0.7198 |
| Negative Stress 2024 | `dio_00ly -> dio_104t` | 18 | 4.44 | 0.0009 | -0.0966 | -0.0975 | 0.0703 | 0.0775 | 0.7074 | 0.7073 |
| BTC 2024 Quiet 5m | `dio_104t -> dio_00ly` | 80 | 6.03 | -0.0671 | 0.0877 | 0.1548 | 0.0779 | 0.0768 | 0.7208 | 0.7221 |

Alle drei Faelle liegen im groben Feldzustand `stabil`.

Das ist wichtig: Die Richtungsunterschiede entstehen nicht aus offenem Feldkollaps, sondern innerhalb eines tragenden Feldbereichs.

## Zentrale Beobachtung

Die deutlichste Differenz liegt im Hoeren beziehungsweise in der Energie-/Tonspur:

- `dio_00ly -> dio_104t` zeigt in KAS und Negative Stress eine tonale Abwaertsbewegung.
- `dio_104t -> dio_00ly` zeigt in BTC Quiet eine tonale Aufwaertsbewegung.

Die Feldspannung bleibt dagegen relativ nah beieinander.

Damit wirkt die Achsenrichtung nicht wie ein einfacher Stresswechsel. Sie wirkt eher wie eine Brueckenmodulation innerhalb stabiler Feldlage:

- gleiche Grundstabilitaet,
- andere Tonbewegung,
- andere Richtung der Bedeutungsnaehe.

## MCM-Lesung

`dio_00ly` und `dio_104t` bilden einen gemeinsamen Brueckenraum.

Die Richtung dieses Brueckenraums scheint sensibel auf die tonale Weltbewegung zu reagieren:

- fallende Tonbewegung: eher `dio_00ly -> dio_104t`
- steigende Tonbewegung: eher `dio_104t -> dio_00ly`

Das ist noch kein Beweis fuer Kausalitaet. Es ist aber ein belastbarer Hinweis, dass Hoeren/Energie nicht nur Hintergrundrauschen ist, sondern die Richtung der Feldnaehe mitpraegt.

## Warum das fuer MINI_DIO wichtig ist

Die Untersuchung zeigt drei Dinge:

1. Die Brueckenachsen bleiben auch in stabiler Feldlage aktiv.
2. Die Richtung der Achsennaehe ist nicht willkuerlich, sondern folgt messbaren Weltunterschieden.
3. Tonale Bewegung kann ein Feldbereich-Unterscheider sein, ohne direkt Handlung auszulösen.

Damit wird MINI_DIOs aktuelle Trennung gestuetzt:

- Sehen liest Form und Struktur.
- Hoeren liest Energiebewegung.
- Rezeptoren begrenzen und uebersetzen Aufnahme.
- Das MCM-Feld bildet daraus Brueckennaehe, Spannung, Rekopplung und Bedeutung.

## Grenze

Diese Ruecklesung arbeitet mit aggregierten Paarereignissen. Sie sagt noch nicht, ob jedes Einzelereignis genau so gelesen werden muss.

Der naechste harte Test ist eine Segmentlesung:

- einzelne KAS-Paare visualisieren,
- einzelne Negative-Stress-Paare visualisieren,
- einzelne BTC-Quiet-Paare visualisieren,
- pruefen, ob die Tonbewegung im lokalen Verlauf wirklich die gleiche Richtung traegt.

## Kurzfazit

Die stabile Achsenrichtung ist nicht nur eine Symbolstatistik.

Sie hat eine messbare Rohweltspur: Besonders die Energie-/Tonbewegung unterscheidet die Richtung, waehrend das MCM-Feld stabil bleibt.

Das spricht fuer eine feldinterne Brueckenmodulation, nicht fuer chaotische Randspannung.

