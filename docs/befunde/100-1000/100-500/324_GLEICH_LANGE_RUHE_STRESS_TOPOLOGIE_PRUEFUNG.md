# Weltrelative Topologie-Matrix

Stand: 2026-06-19 22:04:39

## Zweck

Diese Diagnose prueft, ob MINI_DIO unter `world_relative` weiterhin eine passive Topologie ausbildet.
Die Topologie wird nicht ueber feste `dio_*`-Namen gelesen.
Gelesen werden Rollenqualitaeten aus Innenfeldwirkung, Rekopplung, Carry, Strain und Sinnes-MCM-Kopplung.

Die Diagnose erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Hierarchie

1. Grundfrage: Bleibt eine Rollen-Topologie sichtbar, wenn die Sinnesaufnahme weltrelativ wird?
2. Unterpruefung: Welche Rollenanteile tragen Zentrum, Rand/Kippnaehe, offene Variante und Rekopplungsnaehe?
3. Folgeschritt: Vergleich gegen ruhigere, laengere und staerker gespannte Welten.

## Kurzbefund

| Welt | Episoden | Topologiezustand | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SIDEWAYS_2024_5M_1K | 994 | zentrum_mit_rand_und_uebergang | 0.8169 | 0.1579 | 0.0252 | 0.2485 | 0.6422 | 0.3960 | 0.1939 | 0.8653 |
| SIDEWAYS_2026_5M_1K | 994 | zentrum_mit_rand_und_uebergang | 0.8229 | 0.1499 | 0.0272 | 0.2505 | 0.6433 | 0.3984 | 0.1922 | 0.8661 |
| NEG_STRESS_2023_5M_1K | 994 | zentrum_mit_rand_und_uebergang | 0.8431 | 0.1268 | 0.0302 | 0.2505 | 0.6441 | 0.3972 | 0.1910 | 0.8674 |
| NEG_STRESS_2024_5M_1K | 994 | zentrum_mit_rand_und_uebergang | 0.7958 | 0.1751 | 0.0292 | 0.2495 | 0.6414 | 0.3959 | 0.1950 | 0.8624 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SIDEWAYS_2024_5M_1K | zentrum_stabil | 0.8169 | 0.6484 | 0.3999 | 0.1818 | 0.8788 | 0.3067 | 0.0825 | dio_mcm_episode_1t5bcxp | dio_1lco |
| SIDEWAYS_2024_5M_1K | offene_variante | 0.1579 | 0.6203 | 0.3818 | 0.2376 | 0.8198 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0nqi |
| SIDEWAYS_2024_5M_1K | spannungsrand_kippnaehe | 0.0252 | 0.5774 | 0.3568 | 0.3142 | 0.7112 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0cpy |
| SIDEWAYS_2026_5M_1K | zentrum_stabil | 0.8229 | 0.6502 | 0.4031 | 0.1794 | 0.8808 | 0.3044 | 0.0905 | dio_mcm_episode_1t5bcxp | dio_1f1f |
| SIDEWAYS_2026_5M_1K | offene_variante | 0.1499 | 0.6174 | 0.3799 | 0.2407 | 0.8126 | 0.0000 | 0.9933 | dio_mcm_episode_0y50lf3 | dio_0exb |
| SIDEWAYS_2026_5M_1K | spannungsrand_kippnaehe | 0.0272 | 0.5796 | 0.3585 | 0.3139 | 0.7186 | 0.0000 | 1.0000 | dio_mcm_episode_0y50lf3 | dio_15bw |
| NEG_STRESS_2023_5M_1K | zentrum_stabil | 0.8431 | 0.6503 | 0.4008 | 0.1793 | 0.8805 | 0.2971 | 0.1122 | dio_mcm_episode_1t5bcxp | dio_03wz |
| NEG_STRESS_2023_5M_1K | offene_variante | 0.1268 | 0.6193 | 0.3815 | 0.2391 | 0.8192 | 0.0000 | 0.9921 | dio_mcm_episode_1t5bcxp | dio_11vn |
| NEG_STRESS_2023_5M_1K | spannungsrand_kippnaehe | 0.0302 | 0.5776 | 0.3623 | 0.3155 | 0.7033 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1sl6 |
| NEG_STRESS_2024_5M_1K | zentrum_stabil | 0.7958 | 0.6486 | 0.4004 | 0.1814 | 0.8787 | 0.3110 | 0.0619 | dio_mcm_episode_1t5bcxp | dio_1v9p |
| NEG_STRESS_2024_5M_1K | offene_variante | 0.1751 | 0.6191 | 0.3819 | 0.2376 | 0.8141 | 0.0172 | 0.9828 | dio_mcm_episode_1t5bcxp | dio_1ijy |
| NEG_STRESS_2024_5M_1K | spannungsrand_kippnaehe | 0.0292 | 0.5784 | 0.3578 | 0.3100 | 0.7082 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1thl |

## Lesart

Zentrumsnahe Welten: 4
Gemischte Rollenordnung: 0
Randlastige Welten: 0

Die aktuelle Matrix spricht fuer eine Rollen-Topologie, nicht fuer eine starre geometrische Form.

```text
Zentrum      = stabile Innenfeldwirkung
Rand/Kipp    = lokale Spannung und Bruchnaehe
Offen        = tragende, aber noch nicht fest gereifte Variante
Rekopplung   = Qualitaet, die Zentrum und Uebergang stabilisiert
```

Wichtig: Die numerischen Einteilungen sind Diagnosehilfen.
Sie sind keine Regeln fuer MINI_DIO und keine universellen MCM-Grenzen.

## Zusatzbefund

Diese Pruefung verwendet vier gleich lange 1000-Kerzen-Welten:

- zwei seitwaerts/ruhigere Welten,
- zwei negative Stresswelten.

Der vorherige Kurzsegment-Befund, dass Stress lokal Rand/Kippnaehe erhoeht, wird hier nicht als stabiler
Längeneffekt bestaetigt.

Gleich lange Welten zeigen:

- Alle vier Welten bleiben in `zentrum_mit_rand_und_uebergang`.
- Es entsteht keine neue dominante Mischklasse.
- Rand/Kippnaehe bleibt eng beieinander: `0.0252` bis `0.0302`.
- `NEG_STRESS_2023` ist sogar zentrumsnaeher (`0.8431`) als beide Sideways-Welten.
- `NEG_STRESS_2024` senkt Zentrum (`0.7958`) und erhoeht offene Variante (`0.1751`), ohne randlastig zu werden.

Daraus folgt: Stress wirkt im bisherigen Material nicht automatisch als Randzunahme.
Die MCM-Topologie bleibt stabil, aber Stress kann je nach Weltqualitaet anders gelesen werden:
entweder zentrumsnah rekoppelt oder offener/variantenreicher.

## Wie es weitergeht

Als naechstes sollte nicht mehr nur die Topologieklasse verglichen werden.
Wir muessen innerhalb der stabilen Topologie die Weltqualitaet lesen:
welche Stresswelt rekoppelt zentrumsnah, welche wird offener, und welche Roh-/Sinnesmerkmale tragen diese Differenz.
