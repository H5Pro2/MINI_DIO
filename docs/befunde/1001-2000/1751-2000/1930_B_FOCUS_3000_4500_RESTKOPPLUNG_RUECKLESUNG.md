# 1930 - B-Fokus 3000_4500: Restkopplung-Rücklesung

## Grundfrage

Warum bildet das B-Fokusfenster `3000_4500` bei SOL und BTC mehr Restkopplung als DOGE, obwohl alle drei noch als `kern_ausgeblendet` gelesen werden?

## Hierarchie der Prüfung

1. Allgemeine Grundfrage: Welche Weltform lässt einen Hartkern nicht voll tragen, aber noch teilweise ankoppeln?
2. Konkrete Unterprüfung: Welche Familien bleiben im Fenster `3000_4500` bei SOL, BTC und DOGE sichtbar?
3. Folgeschritt: Prüfen, ob diese Restkopplung an die Weltform selbst gebunden ist oder nur an einzelne Familien.

## Familienrücklesung

| Asset | sichtbar nicht ausgeblendet | Lesung |
|---|---:|---|
| SOL | 5 von 27 Kernpaaren | 3 getragen, 1 geöffnet, 1 driftend |
| BTC | 5 von 27 Kernpaaren | 3 getragen, 1 geöffnet, 1 driftend |
| DOGE | 1 von 34 Kernpaaren | 1 geöffnet |

Gemeinsam bei SOL und BTC getragen:

- `dio_0tay` früh bleibt `phase_nullnah`.
- `dio_14wj` früh bleibt `phase_nullnah`.
- `dio_06er` früh driftet bei beiden aus der Nullnähe heraus.

Unterschiede:

- SOL trägt zusätzlich `dio_1kpz` früh und öffnet `dio_1kpz` mitte.
- BTC trägt zusätzlich `dio_14wj` spät und öffnet `dio_0nlj` mitte.
- DOGE zeigt nur `dio_0nlj` mitte als offene Restkopplung.

## Weltmerkmale

Die drei B-Fokusfenster unterscheiden sich nicht nur in der Länge, sondern in der Art der Weltspannung:

| Fenster | Zeilen | Drift | mittlere absolute Bewegung | mittlere Range | Richtungswechsel | Lesung |
|---|---:|---:|---:|---:|---:|---|
| `2400_3900` | 1500 | 5.131498 | 0.001289 | 0.006039 | 0.016689 | starke Überexpansion |
| `3000_4500` | 1500 | 1.335919 | 0.000703 | 0.004060 | 0.015354 | balancierte gerichtete Expansion |
| `3200_5200` | 2000 | 2.040129 | 0.000848 | 0.005300 | 0.037538 | länger, wechselhafter |

Damit ist `3000_4500` nicht das stärkste Fenster. Es ist das am saubersten gerichtete Fenster: weniger rau, weniger breit, wenig Richtungswechsel, aber noch genug Expansion.

## Befund

Die Restkopplung scheint hier nicht aus maximaler Energie zu entstehen, sondern aus passender Weltform:

```text
zu laut / zu breit  -> Hartkern wird eher ausgeblendet
zu wechselhaft      -> Hartkern verliert Bindung
gerichtet + ruhig   -> Restkopplung bleibt möglich
```

Das erklärt, warum SOL und BTC im selben Fenster eine ähnliche Restkopplung zeigen. DOGE bleibt schwächer, weil seine Hartkernfamilien in diesem Fenster nur einen offenen Kontakt finden, aber keine direkte Nullnähe-Reproduktion.

## Bedeutung für MINI_DIO

Diese Prüfung stützt die These, dass Weltpassung nicht nur aus Stärke entsteht. Entscheidend ist die Form der Weltspannung:

- gerichtete Bewegung,
- geringe Rauheit,
- begrenzte Richtungswechsel,
- ausreichende, aber nicht übersteuernde Expansion.

Das ist wichtig für die MCM-Mechanik, weil es gegen eine simple Lautstärke-Logik spricht. Das Feld reagiert nicht nur auf viel oder wenig Reiz, sondern auf eine passende Kombination aus Weltspannung, Formruhe und zeitlicher Richtung.

## Methodische Grenze

Das ist weiterhin eine passive Rücklesung. Es wird keine Handlung und keine Strategie daraus abgeleitet. Der Befund sagt nur: Unter dieser Weltform bleibt bei SOL und BTC mehr Kernnähe lesbar als bei DOGE.

## Wie es weitergeht

Als nächstes sollte `3000_4500` gegen ein leicht verschobenes Nachbarfenster geprüft werden. Ziel: klären, ob die Restkopplung wirklich an dieser balancierten Weltform hängt oder ob sie über einen breiteren Bereich stabil bleibt.
