# Weltrelative Topologie-Matrix

Stand: 2026-07-01 05:23:33

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
| VIS_STABLE_HEARING_CHAOTIC | 7394 | gemischte_rollenordnung | 0.9513 | 0.0243 | 0.0243 | 0.2184 | 0.7539 | 0.6057 | 0.1296 | 0.9087 |
| VIS_CHAOTIC_HEARING_STABLE | 6394 | stark_zentriert_wenig_rand | 0.9997 | 0.0003 | 0.0000 | 0.1905 | 0.7590 | 0.6208 | 0.1182 | 0.9179 |
| SYNTH_DESYNC_AXES | 8494 | stark_zentriert_wenig_rand | 0.9803 | 0.0105 | 0.0092 | 0.2352 | 0.7527 | 0.6061 | 0.1260 | 0.9108 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| VIS_STABLE_HEARING_CHAOTIC | zentrum_stabil | 0.9513 | 0.7603 | 0.6133 | 0.1224 | 0.9199 | 0.2630 | 0.2117 | dio_mcm_episode_0qvodoj | dio_1fll |
| VIS_STABLE_HEARING_CHAOTIC | offene_variante | 0.0243 | 0.6472 | 0.4728 | 0.2481 | 0.7274 | 0.0000 | 1.0000 | dio_mcm_episode_0v5p8er | dio_0ntz |
| VIS_STABLE_HEARING_CHAOTIC | spannungsrand_kippnaehe | 0.0243 | 0.6112 | 0.4414 | 0.2923 | 0.6558 | 0.0000 | 1.0000 | dio_mcm_episode_0v5p8er | dio_1rrr |
| VIS_CHAOTIC_HEARING_STABLE | zentrum_stabil | 0.9997 | 0.7590 | 0.6209 | 0.1182 | 0.9179 | 0.2506 | 0.2498 | dio_mcm_episode_0qvodoj | dio_1fll |
| VIS_CHAOTIC_HEARING_STABLE | offene_variante | 0.0003 | 0.6493 | 0.4266 | 0.1883 | 0.8138 | 0.0000 | 1.0000 | dio_mcm_episode_1v8o9kh | dio_0pxr |
| SYNTH_DESYNC_AXES | zentrum_stabil | 0.9803 | 0.7553 | 0.6093 | 0.1231 | 0.9152 | 0.2551 | 0.2350 | dio_mcm_episode_0v5p8er | dio_1fll |
| SYNTH_DESYNC_AXES | offene_variante | 0.0105 | 0.6470 | 0.4707 | 0.2458 | 0.7332 | 0.0000 | 1.0000 | dio_mcm_episode_0v5p8er | dio_03yj |
| SYNTH_DESYNC_AXES | spannungsrand_kippnaehe | 0.0092 | 0.6006 | 0.4204 | 0.3016 | 0.6475 | 0.0000 | 1.0000 | dio_mcm_episode_0v5p8er | dio_0kcg |

## Lesart

Zentrumsnahe Welten: 2
Gemischte Rollenordnung: 1
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
