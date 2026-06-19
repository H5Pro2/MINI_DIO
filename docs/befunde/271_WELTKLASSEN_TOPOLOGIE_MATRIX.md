# Weltrelative Topologie-Matrix

Stand: 2026-06-19 11:29:18

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
| SIDEWAYS_2026_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8024 | 0.1505 | 0.0471 | 0.2487 | 0.6472 | 0.3991 | 0.1834 | 0.8654 |
| STRESS_2023_NEG_1K | 994 | zentrum_mit_rand_und_uebergang | 0.8410 | 0.1167 | 0.0423 | 0.2455 | 0.6463 | 0.3947 | 0.1835 | 0.8661 |
| EXPANSION_2023_POS_1K | 994 | zentrum_mit_rand_und_uebergang | 0.8139 | 0.1519 | 0.0342 | 0.2435 | 0.6457 | 0.3941 | 0.1859 | 0.8667 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SIDEWAYS_2026_2K | zentrum_stabil | 0.8024 | 0.6540 | 0.4012 | 0.1653 | 0.8752 | 0.3113 | 0.0731 | dio_mcm_episode_183drjy | dio_1p73 |
| SIDEWAYS_2026_2K | offene_variante | 0.1505 | 0.6256 | 0.3915 | 0.2381 | 0.8344 | 0.0033 | 0.9600 | dio_mcm_episode_0y50lf3 | dio_0q15 |
| SIDEWAYS_2026_2K | spannungsrand_kippnaehe | 0.0471 | 0.6005 | 0.3878 | 0.3164 | 0.7986 | 0.0000 | 1.0000 | dio_mcm_episode_0y50lf3 | dio_00gl |
| STRESS_2023_NEG_1K | zentrum_stabil | 0.8410 | 0.6517 | 0.3956 | 0.1686 | 0.8738 | 0.2978 | 0.1100 | dio_mcm_episode_1t5bcxp | dio_1sle |
| STRESS_2023_NEG_1K | offene_variante | 0.1167 | 0.6242 | 0.3858 | 0.2401 | 0.8368 | 0.0000 | 0.9914 | dio_mcm_episode_1t5bcxp | dio_0i1q |
| STRESS_2023_NEG_1K | spannungsrand_kippnaehe | 0.0423 | 0.6009 | 0.4007 | 0.3237 | 0.7937 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1e08 |
| EXPANSION_2023_POS_1K | zentrum_stabil | 0.8139 | 0.6511 | 0.3952 | 0.1700 | 0.8737 | 0.2991 | 0.0841 | dio_mcm_episode_1t5bcxp | dio_1h66 |
| EXPANSION_2023_POS_1K | offene_variante | 0.1519 | 0.6266 | 0.3903 | 0.2414 | 0.8407 | 0.0464 | 0.9735 | dio_mcm_episode_1t5bcxp | dio_0ui5 |
| EXPANSION_2023_POS_1K | spannungsrand_kippnaehe | 0.0342 | 0.6045 | 0.3845 | 0.3176 | 0.8154 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1npy |

## Lesart

Zentrumsnahe Welten: 3
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

## Wie es weitergeht

Als naechstes sollte dieselbe Matrix auf lange ruhige Welten, Stresswelten und Expansionswelten gelegt werden.
Ziel ist zu pruefen, ob `zentrum_mit_rand_und_uebergang` stabil bleibt, ob Randspannung bei Stress sichtbar zunimmt oder ob neue Mischklassen entstehen.
