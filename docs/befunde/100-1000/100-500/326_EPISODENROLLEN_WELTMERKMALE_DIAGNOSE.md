# Episodenrollen Gegen Weltmerkmale

Stand: 2026-06-19 22:19:47

## Zweck

Diese Diagnose liest innerhalb stabiler Topologie, welche lokalen Weltmerkmale mit Zentrum, offener Variante und Rand/Kippnaehe zusammenfallen.
Sie erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Hierarchie

1. Grundfrage: Warum rekoppelt eine Stresswelt zentrumsnah, waehrend eine andere offener wird?
2. Unterpruefung: Rollenanteile gegen Return, Range, Volumenwechsel, Richtungswechsel und lokalen Drift legen.
3. Folgeschritt: Lokale Abschnitte mit offener Variante und zentrumsnaher Rekopplung getrennt lesen.

## Weltuebersicht

| Welt | Episoden | Zentrum | Offen | Rand/Kipp | Richtungswechsel | lokaler Drift | Rekopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| NEG_STRESS_2023 | 994 | 0.8431 | 0.1268 | 0.0302 | 0.3954 | -0.0003 | 0.6441 |
| NEG_STRESS_2024 | 994 | 0.7958 | 0.1751 | 0.0292 | 0.4839 | -0.0006 | 0.6414 |

## Rollenwerte

| Welt | Rolle | Anteil | Rekopplung | Strain | Sinneskopplung | abs Return | Range | Richtungswechsel | lokaler Drift | laengste Serie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEG_STRESS_2023 | offene_variante | 0.1268 | 0.6193 | 0.2391 | 0.8192 | 0.002701 | 0.004758 | 0.3889 | -0.0007 | 5 |
| NEG_STRESS_2023 | spannungsrand_kippnaehe | 0.0302 | 0.5776 | 0.3155 | 0.7033 | 0.002734 | 0.005755 | 0.1667 | -0.0022 | 4 |
| NEG_STRESS_2023 | zentrum_stabil | 0.8431 | 0.6503 | 0.1793 | 0.8805 | 0.001370 | 0.002844 | 0.4045 | -0.0002 | 35 |
| NEG_STRESS_2024 | offene_variante | 0.1751 | 0.6191 | 0.2376 | 0.8141 | 0.002399 | 0.004485 | 0.3563 | -0.0005 | 6 |
| NEG_STRESS_2024 | spannungsrand_kippnaehe | 0.0292 | 0.5784 | 0.3100 | 0.7082 | 0.001778 | 0.003563 | 0.5172 | -0.0031 | 1 |
| NEG_STRESS_2024 | zentrum_stabil | 0.7958 | 0.6486 | 0.1814 | 0.8787 | 0.001497 | 0.002954 | 0.5107 | -0.0005 | 26 |

## Befund

`NEG_STRESS_2024` wird nicht offener, weil mehr Rand/Kippnaehe entsteht.
Der Randanteil bleibt fast gleich (`0.0292` gegen `0.0302`).

Der Unterschied liegt in der Verteilung zwischen Zentrum und offener Variante:

- `NEG_STRESS_2023`: Zentrum `0.8431`, offene Variante `0.1268`.
- `NEG_STRESS_2024`: Zentrum `0.7958`, offene Variante `0.1751`.
- Die laengste stabile Zentrumserie sinkt von `35` auf `26`.
- Im Zentrum von `NEG_STRESS_2024` ist der Richtungswechsel deutlich hoeher (`0.5107`) als im Zentrum von `NEG_STRESS_2023` (`0.4045`).
- Die offene Variante bleibt in beiden Welten feldseitig aehnlich: Rekopplung ca. `0.619`, Strain ca. `0.238`.

Daraus folgt: `NEG_STRESS_2024` erzeugt keine neue Topologieform und keinen dominanten Rand.
Es unterbricht die zentrumsnahe Rekopplung haeufiger und verschiebt mehr Episoden in offene Variante.

Fachlich gelesen: Die Welt bleibt tragbar, aber weniger durchgehend zentriert.
MINI_DIO liest diese Welt eher als wechselhaftere Kontaktqualitaet, nicht als Kollaps.

## Wie es weitergeht

Als naechstes sollte die offene Variante selbst untersucht werden:
Ist sie eine unreife Zwischenlage, eine normale Variationszone oder eine beginnende neue Bedeutungsinsel?
