# Wahrnehmungsadapter: Laufvergleich

Stand: 2026-06-19

## Grundfrage

Liegt das Problem bei der MCM-Topologie oder bereits in der Berechnung der Informationsaufnahme?

## Unterpruefung

Geprueft wurden drei Ebenen:

1. aktuelle feste Sinnesuebersetzung,
2. einfache weltrelative Skalierung,
3. weiche weltrelative Sinneskompression.

Die zugehoerigen Diagnosen:

- `262_WELTUEBERGREIFENDE_INFORMATIONSAUFNAHME_DIAGNOSE.md`
- `263_WELTRELATIVER_WAHRNEHMUNGSADAPTER_VERGLEICH.md`
- `264_WEICHER_WELTRELATIVER_WAHRNEHMUNGSADAPTER_VERGLEICH.md`

Zusatzpruefung:

- `fixed`: `debug/intake_compare_fixed_2024_real1_01/`
- `world_relative`: `debug/intake_compare_world_relative_2024_real1_01/`

## Befund 1: aktuelle Aufnahme ist nicht welteinheitlich

Die feste Uebersetzung nutzt in `mini_dio/mini_world.py` unter anderem feste Teiler:

- `form_flow = direction / 0.018`
- `form_change = change / 0.009`

Damit kann eine Welt zufaellig gut passen, waehrend eine andere Welt uebersteuert oder zu flach wirkt.

Die Diagnose `262` zeigt ueber mehrere Welten deutliche Auffaelligkeiten:

- `sehen.form_stability` uebersteuert breit.
- `sehen.form_change` und `hoeren.energy_shift` laufen oft in Grenznaehe.
- 1h-Welten und BTC/SOL-Unterschiede werden teilweise durch Skalierung statt durch echte Feldwirkung verzerrt.

## Befund 2: einfache Weltrelativitaet reicht nicht

Die erste weltrelative Variante setzte Werte relativ zur Weltverteilung, aber mit harter Randnaehe.

Ergebnis aus `263`:

- Verbesserte Achsen: 0
- Verschlechterte Achsen: 13
- Weiter auffaellige Achsen: 22

Grund:

```text
p95 als Skala + harte Begrenzung
=> viele Werte liegen wieder nahe am Rand
=> andere Form der Uebersteuerung
```

Das ist keine organische Wahrnehmung.

## Befund 3: weiche weltrelative Kompression funktioniert deutlich besser

Die zweite Variante nutzt eine weiche sensorische Kompression.

Ergebnis aus `264`:

- Verbesserte Achsen: 22
- Verschlechterte Achsen: 0
- Weiter auffaellige Achsen: 0

Das ist der bisher klarste Hinweis:

```text
Ein relevanter Teil der bisherigen Feldspannung kam aus der Berechnung der Sinnesaufnahme.
```

## Laufvergleich auf 2024-Realwelt

Beide Laeufe blieben passiv:

- `trades=0`
- keine Handlung
- keine Gates

Vergleich Run 2:

| Modus | Syntax | Carry | Strain | Rekopplung | Sensory Coupling | Dominante Innenwirkung |
|---|---:|---:|---:|---:|---:|---|
| `fixed` | 967 | 0.3581 | 0.2100 | 0.6223 | 0.8293 | `inner_effect_carried_unrest` |
| `world_relative` | 943 | 0.3944 | 0.1884 | 0.6434 | 0.8638 | `inner_effect_stable` |

Die weiche Aufnahme:

- reduziert Strain,
- erhoeht Rekopplung,
- erhoeht Sensory Coupling,
- senkt Syntaxstreuung leicht,
- verschiebt die dominante Innenwirkung von `carried_unrest` zu `stable`.

## Kritische Lesart

Das ist gut gegen rohe Reizlast.

Aber:

Wenn der Adapter zu stark beruhigt, kann echte Weltspannung wegkomprimiert werden.

Die richtige Mechanik ist deshalb nicht:

```text
alles glatt normalisieren
```

sondern:

```text
Welt relativ aufnehmen,
starke Reize weich komprimieren,
aber reale Brueche, Rhythmuswechsel und Kippnaehe erhalten.
```

## Schlussfolgerung

Ja, Berechnung und Umsetzung haben grossen Einfluss.

Der naechste Aufbau braucht eine saubere Sinnesarchitektur:

```text
Rohwelt
-> Weltprofil
-> weiche Sinneskompression
-> Sehen / Hoeren / Fuehlen
-> MCM-Feldwirkung
-> Bedeutungsverdichtung
```

Das MCM-Feld sollte nicht Rohdatenlast tragen.
Es sollte bereits vorgeformte, weltrelative Sinnesinformation bekommen.

## Grenze

Der neue Modus `--sense-mode world_relative` ist eingebaut, aber noch nicht als Standard gesetzt.

Er ist aktuell ein Forschungsmodus.

## Wie es weitergeht

Als naechstes muss dieselbe Rollenmatrix mit `world_relative` ueber mehrere Welten laufen.

Grundfrage:

```text
Bleibt die MCM-Rollenordnung unter sauberer Sinnesaufnahme stabiler,
oder wird sie nur kuenstlich beruhigt?
```

Konkrete Unterpruefung:

- `SOL_2023_5M_REAL1`
- `SOL_2024_5M_REAL1`
- `SOL_2024_1H`
- `BTC_2024_5M`
- `BTC_2024_1H`
- `SOL_2023_NEG_STRESS`

Erst wenn die Rollenrelationen unter `world_relative` klarer und nicht flacher werden, sollte der Adapter als Standardmechanik gelten.
