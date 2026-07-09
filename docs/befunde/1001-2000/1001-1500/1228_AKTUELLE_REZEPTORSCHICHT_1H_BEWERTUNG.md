# Aktuelle Rezeptorschicht 1h-Bewertung

Stand: 2026-07-01

## Grundfrage

Bleibt die Feldphasenordnung erhalten, wenn MINI_DIO dieselben Stress-/Quiet-Welten nicht als 5m-, sondern als 1h-Welt liest?

Nach aktuellem Befund: ja. Die Feldphasenordnung bleibt erhalten und wirkt auf 1h sogar ruhiger zentrumsnah.

## Pruefaufbau

Neu gelaufen mit `--sense-mode world_relative`:

- `SOL_QUIET_1H`
- `SOL_STRESS_1H`
- `BTC_QUIET_1H`
- `BTC_STRESS_1H`

Je Welt wurden zwei passive MINI_DIO-Laeufe mit eigener Memory erzeugt. Ausgewertet wurde Lauf 2.

## Hauptbefund

Direkte Uebergaenge:

```text
Offen -> Rand/Kipp: 105
Rand/Kipp -> Offen: 264
```

Damit bestaetigt sich die schon bei 5m sichtbare Entlastungsrichtung. Rand/Kipp geht deutlich haeufiger in Offenheit zurueck, als Offenheit direkt in Rand/Kipp kippt.

## Rollenqualitaet

Die vier Feldphasen bleiben auch bei 1h getrennt lesbar:

- Zentrum: geringe Rohaufnahme, geringe Lautheit, hohe Rekopplung, niedriger Strain.
- Rekopplungsnaehe: kurze Bindungsnaehe mit stabiler Rekopplung.
- Offene Variante: Bewegungsraum mit mittlerer Rohaufnahme und mittlerer Lautheit.
- Rand/Kipp: hohe Rohaufnahme, hohe Lautheit, schwache Rekopplung und hoher Strain.

Die 1h-Welten zeigen damit keine neue Feldmechanik. Sie zeigen dieselbe Topologie in groberer Zeitaufloesung.

## Stress gegen Quiet

Stress erzeugt auch auf 1h keine neue dominante Rolle.

SOL und BTC bleiben nah an derselben Feldordnung. BTC 1h zeigt etwas staerkere Zentrumsnaehe:

```text
BTC_QUIET_1H:  zentrum_stabil Dauer 2124
BTC_STRESS_1H: zentrum_stabil Dauer 2073
SOL_QUIET_1H:  zentrum_stabil Dauer 1993
SOL_STRESS_1H: zentrum_stabil Dauer 1940
```

Das spricht dafuer, dass die Rezeptorschicht die Weltspannung nicht platt normalisiert. Sie laesst Asset- und Zeitstruktur weiter sichtbar, ohne das MCM-Feld mit Rohspannung zu ueberladen.

## Schlussfolgerung

Die aktuelle Rezeptorschicht ist nicht nur 5m-kompatibel.

Sie erhaelt die Feldphasenordnung auch in 1h-Welten:

```text
Zentrum bleibt Zentrum.
Rekopplung bleibt Bindungsnaehe.
Offenheit bleibt Bewegungsraum.
Rand/Kipp bleibt kurze Spannungsnaehe.
```

Das staerkt die Annahme, dass MINI_DIO hier keine reine Zeitframe-Artefaktik liest, sondern eine robuste MCM-Feldphasenordnung.

## Wie es weitergeht

Als naechstes sollten wir eine dritte Zeit-/Weltklasse pruefen: entweder sehr kurze 5m-Ausschnitte mit hoeherem Rauschen oder laengere 1h-Folgewelten. Ziel ist zu klaeren, ob Rand/Kipp unter veraenderter Weltlaenge kurz bleibt oder ob sich eine neue Brueckenrolle bildet.
