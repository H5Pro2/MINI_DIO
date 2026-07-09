# 1043 - PAXG gegen BTC, SOL und KAS: Gleichgruppenvergleich

## Zweck

Diese Pruefung vergleicht PAXG gegen BTC, SOL und KAS in moeglichst gleichlangen Gruppen.

Geprueft wurde nicht, ob PAXG eine voellig andere Topologie bildet, sondern ob PAXG innerhalb derselben MCM-Grundordnung eine andere Feldqualitaet traegt.

## Datengrundlage

Erzeugte Messdateien:

- `1043_PAXG_GEGEN_BTC_SOL_KAS_GLEICHGRUPPEN_MATRIX.csv`
- `1043_PAXG_GEGEN_BTC_SOL_KAS_GLEICHGRUPPEN_AGGREGAT.csv`

Vergleichsgruppen:

- `10K_5M_HARD`: BTC und PAXG, jeweils 2024 und 2025, 10.000 Kerzen, 5m.
- `2K_5M_BROAD`: BTC, SOL, KAS und PAXG, jeweils 2.000 Kerzen, 5m.
- `1H_LONG`: BTC 2025 und PAXG 2024/2025, lange 1h-Welten.

## Befund 1: PAXG ist im 5m-Hard-Vergleich ruhiger

Im 10K-5m-Vergleich liegt PAXG gegen BTC stabiler und ruhiger:

| Gruppe | Asset | Rekopplung | Strain | Stabil | Unruhe | Kippnaehe |
|---|---:|---:|---:|---:|---:|---:|
| 10K_5M_HARD | BTC | 0.704295 | 0.156696 | 0.835501 | 0.154042 | 0.010457 |
| 10K_5M_HARD | PAXG | 0.714143 | 0.152119 | 0.876076 | 0.117171 | 0.006754 |

Lesung:

PAXG koppelt im 5m-Hard-Vergleich staerker zurueck, traegt weniger Strain, bleibt stabiler und erzeugt weniger Randspannung.

Das spricht nicht fuer eine andere Grundtopologie, sondern fuer eine ruhigere Feldfaerbung.

## Befund 2: PAXG ist auch im 2K-Breitvergleich am ruhigsten

Im 2K-5m-Vergleich gegen BTC, SOL und KAS ist PAXG ebenfalls die ruhigste Gruppe:

| Gruppe | Asset | Rekopplung | Strain | Stabil | Unruhe | Kippnaehe |
|---|---:|---:|---:|---:|---:|---:|
| 2K_5M_BROAD | SOL | 0.693318 | 0.157341 | 0.754263 | 0.237212 | 0.008526 |
| 2K_5M_BROAD | KAS | 0.693981 | 0.156209 | 0.778335 | 0.212638 | 0.009027 |
| 2K_5M_BROAD | BTC | 0.695686 | 0.154998 | 0.793882 | 0.197091 | 0.009027 |
| 2K_5M_BROAD | PAXG | 0.703694 | 0.152020 | 0.831494 | 0.161484 | 0.007021 |

Lesung:

PAXG ist in dieser Gruppe nicht nur anders, sondern feldqualitativ am staerksten rekoppelnd und am wenigsten unruhig.

SOL und KAS wirken dagegen feldaktiver, unruhiger und weniger stabil.

## Befund 3: Auf 1h naehern sich BTC und PAXG an

Im langen 1h-Vergleich sind BTC und PAXG deutlich naeher beieinander:

| Gruppe | Asset | Rekopplung | Strain | Stabil | Unruhe | Kippnaehe |
|---|---:|---:|---:|---:|---:|---:|
| 1H_LONG | BTC | 0.706716 | 0.152034 | 0.807174 | 0.184830 | 0.007996 |
| 1H_LONG | PAXG | 0.705512 | 0.152730 | 0.801005 | 0.193636 | 0.005360 |

Lesung:

Der PAXG-Kontrast ist auf 5m deutlich staerker als auf 1h.

Auf 1h bleibt PAXG nicht fremd, sondern bewegt sich nahe an BTC. Die Kippnaehe bleibt bei PAXG niedriger, aber Rekopplung, Strain und Stabilitaet sind nicht mehr klar besser.

Das spricht dafuer, dass die PAXG-Besonderheit zeitebenenabhaengig gelesen werden muss.

## Befund 4: Die Grundfamilie bleibt gleich, die zweite Traegerfamilie unterscheidet sich

In allen Gruppen erscheint `dio_104t` als Top-Familie.

Das ist wichtig:

```text
PAXG bildet keine komplett fremde Topologie.
PAXG nutzt dieselbe Grundfamilie wie BTC, SOL und KAS.
Der Unterschied liegt in der zweiten Traegerfamilie und in der Feldqualitaet.
```

Besonders auffaellig:

- BTC 5m: `dio_104t` gefolgt von `dio_155c`.
- SOL/KAS 5m: `dio_104t` gefolgt von `dio_0m9z`.
- PAXG 5m: `dio_104t` gefolgt von `dio_14wj`.
- BTC/PAXG 1h: beide naehern sich an `dio_104t` und `dio_155c`.

Lesung:

`dio_104t` wirkt wie eine assetuebergreifende Grundfamilie.

`dio_14wj` wirkt im PAXG-5m-Feld wie ein ruhiger zweiter Traeger, der bei BTC, SOL und KAS in dieser Form nicht dominant wird.

## Schlussfolgerung

Die bisherige Erwartung, dass PAXG als Gold-nahe Welt komplett gegensaetzlich zu BTC, SOL oder KAS liegen muesste, bestaetigt sich so nicht.

Praeziser ist:

```text
PAXG ist keine andere MCM-Topologie.
PAXG ist eine ruhigere Rekopplungs-Ausbildung innerhalb derselben Topologie.
```

Damit bestaetigt sich die bisherige MCM-Lesung:

```text
Topologie = stabile Grundordnung
Weltqualitaet = Faerbung der Bedeutungsachsen
```

PAXG zeigt vor allem auf 5m:

- hoehere Rekopplung,
- weniger Strain,
- mehr Stabilitaet,
- weniger Unruhe,
- weniger Kippnaehe,
- eigene zweite Traegerfamilie `dio_14wj`.

Auf 1h verschiebt sich PAXG naeher an BTC. Das bedeutet: Die Weltqualitaet ist nicht nur assetabhaengig, sondern auch zeitebenenabhaengig.

## Bedeutung fuer MINI_DIO

MINI_DIO liest nicht einfach Preisgroesse oder Assetnamen.

Das Feld bildet eine wiederkehrende Grundordnung und faerbt diese je nach Weltspannung, Zeitfenster und sensorischer Aufnahme anders aus.

Das ist fuer die weitere Forschung zentral:

```text
Gleiche Topologie kann unterschiedliche Weltqualitaet tragen.
Unterschiedliche Weltqualitaet muss nicht zwingend neue Topologie bedeuten.
```

Damit wird die naechste Forschungsfrage klarer:

Welche zweiten Traegerfamilien entstehen in welchen Welten, und wann werden sie zu stabilen Bedeutungsraeumen?

## Wie es weitergeht

Als naechstes sollte `dio_14wj` als PAXG-5m-Traegerfamilie isoliert werden. Ziel ist zu pruefen, ob diese Familie eine eigene ruhige Rekopplungsrolle traegt oder nur eine Oberflaechenvariante von `dio_104t` ist.
