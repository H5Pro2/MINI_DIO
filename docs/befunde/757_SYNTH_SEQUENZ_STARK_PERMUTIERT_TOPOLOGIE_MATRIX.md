# Weltrelative Topologie-Matrix

Stand: 2026-06-22 21:33:37

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
| SEQUENZ_ORIGINAL | 6094 | stark_zentriert_wenig_rand | 0.9539 | 0.0456 | 0.0005 | 0.2491 | 0.7461 | 0.5985 | 0.1248 | 0.9043 |
| STARK_PERMUTIERT | 6094 | stark_zentriert_wenig_rand | 0.9539 | 0.0455 | 0.0007 | 0.2494 | 0.7459 | 0.5983 | 0.1248 | 0.9041 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SEQUENZ_ORIGINAL | zentrum_stabil | 0.9539 | 0.7496 | 0.6033 | 0.1223 | 0.9098 | 0.2622 | 0.2138 | dio_mcm_episode_0wjn8vm | dio_1fll |
| SEQUENZ_ORIGINAL | offene_variante | 0.0456 | 0.6763 | 0.4995 | 0.1769 | 0.7916 | 0.0000 | 1.0000 | dio_mcm_episode_0wjn8vm | dio_0lwq |
| SEQUENZ_ORIGINAL | spannungsrand_kippnaehe | 0.0005 | 0.5743 | 0.3194 | 0.3192 | 0.6607 | 0.0000 | 1.0000 | dio_mcm_episode_0sxikqi | dio_0kcg |
| STARK_PERMUTIERT | zentrum_stabil | 0.9539 | 0.7494 | 0.6032 | 0.1222 | 0.9097 | 0.2623 | 0.2138 | dio_mcm_episode_0qvodoj | dio_1fll |
| STARK_PERMUTIERT | offene_variante | 0.0455 | 0.6759 | 0.4998 | 0.1774 | 0.7907 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_0lwq |
| STARK_PERMUTIERT | spannungsrand_kippnaehe | 0.0007 | 0.5829 | 0.3220 | 0.3116 | 0.6759 | 0.0000 | 1.0000 | dio_mcm_episode_0qvodoj | dio_0qvy |

## Lesart

Zentrumsnahe Welten: 2
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
