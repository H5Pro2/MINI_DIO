# Weltrelative Topologie-Matrix

Stand: 2026-06-19 21:48:36

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
| QUIET_2024_5M_100 | 94 | zentrum_mit_rand_und_uebergang | 0.8085 | 0.1596 | 0.0319 | 0.2553 | 0.6409 | 0.3944 | 0.1952 | 0.8653 |
| STRESS_2024_5M_100 | 94 | zentrum_mit_rand_und_uebergang | 0.8404 | 0.1064 | 0.0532 | 0.2553 | 0.6419 | 0.3956 | 0.1935 | 0.8652 |
| POS_EXP_2023_5M_1K | 994 | zentrum_mit_rand_und_uebergang | 0.8249 | 0.1489 | 0.0262 | 0.2465 | 0.6437 | 0.3968 | 0.1928 | 0.8668 |
| EXT_EXP_2023_5M_1K | 994 | zentrum_mit_rand_und_uebergang | 0.8109 | 0.1489 | 0.0402 | 0.2505 | 0.6456 | 0.3999 | 0.1899 | 0.8685 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| QUIET_2024_5M_100 | zentrum_stabil | 0.8085 | 0.6478 | 0.3994 | 0.1822 | 0.8791 | 0.3158 | 0.0789 | dio_mcm_episode_1t5bcxp | dio_1ltv |
| QUIET_2024_5M_100 | offene_variante | 0.1596 | 0.6207 | 0.3814 | 0.2359 | 0.8288 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1gly |
| QUIET_2024_5M_100 | spannungsrand_kippnaehe | 0.0319 | 0.5693 | 0.3335 | 0.3216 | 0.6967 | 0.0000 | 1.0000 | dio_mcm_episode_04q6913 | dio_1lx6 |
| STRESS_2024_5M_100 | zentrum_stabil | 0.8404 | 0.6494 | 0.3987 | 0.1783 | 0.8836 | 0.3038 | 0.1139 | dio_mcm_episode_1t5bcxp | dio_1h1r |
| STRESS_2024_5M_100 | offene_variante | 0.1064 | 0.6188 | 0.3933 | 0.2452 | 0.8009 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0oi5 |
| STRESS_2024_5M_100 | spannungsrand_kippnaehe | 0.0532 | 0.5689 | 0.3507 | 0.3311 | 0.7039 | 0.0000 | 1.0000 | dio_mcm_episode_0y0oxs9 | dio_0c76 |
| POS_EXP_2023_5M_1K | zentrum_stabil | 0.8249 | 0.6499 | 0.4011 | 0.1808 | 0.8793 | 0.3037 | 0.0915 | dio_mcm_episode_1t5bcxp | dio_0xw3 |
| POS_EXP_2023_5M_1K | offene_variante | 0.1489 | 0.6190 | 0.3791 | 0.2389 | 0.8186 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0tva |
| POS_EXP_2023_5M_1K | spannungsrand_kippnaehe | 0.0262 | 0.5866 | 0.3619 | 0.3084 | 0.7461 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_180s |
| EXT_EXP_2023_5M_1K | zentrum_stabil | 0.8109 | 0.6533 | 0.4049 | 0.1751 | 0.8840 | 0.3089 | 0.0782 | dio_mcm_episode_1t5bcxp | dio_1f3b |
| EXT_EXP_2023_5M_1K | offene_variante | 0.1489 | 0.6201 | 0.3840 | 0.2374 | 0.8177 | 0.0000 | 0.9865 | dio_mcm_episode_1t5bcxp | dio_1tyo |
| EXT_EXP_2023_5M_1K | spannungsrand_kippnaehe | 0.0402 | 0.5837 | 0.3582 | 0.3112 | 0.7429 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_13aw |

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

Diese Pruefung mischt zwei lokale 100-Kerzen-Segmente mit zwei 1000-Kerzen-Expansionswelten.
Die lokalen Segmente sind deshalb als Kurzfenster zu lesen, nicht als gleich lange Vollwelten.

Trotzdem bleibt der Befund klar:

- Alle vier Bedingungswelten bleiben in `zentrum_mit_rand_und_uebergang`.
- Es entsteht keine neue dominante Mischklasse.
- Stress erhoeht lokal Rand/Kippnaehe (`0.0532`) gegenueber dem ruhigen Kurzfenster (`0.0319`).
- Positive Expansion bleibt mit `0.0262` Rand/Kippnaehe sehr zentrumsnah.
- Extreme Expansion hebt Rand/Kippnaehe auf `0.0402`, bleibt aber ebenfalls nicht randlastig.

Damit wirkt Stress bisher eher als lokale Randaktivierung.
Expansion erzwingt im aktuellen Test keine neue Topologieform, sondern verschiebt nur die Rollengewichtung innerhalb derselben Feldordnung.

## Wie es weitergeht

Als naechstes sollten gleich lange ruhige und gleich lange Stresswelten erzeugt oder ausgewaehlt werden.
Dann laesst sich sauberer pruefen, ob die erhoehte Rand/Kippnaehe im Stressfenster ein stabiler Bedingungseffekt ist oder nur Segmentvarianz.
