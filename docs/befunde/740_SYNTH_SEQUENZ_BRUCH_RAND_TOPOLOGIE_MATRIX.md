# Weltrelative Topologie-Matrix

Stand: 2026-06-22 18:07:51

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
| SEQUENZ_PERMUTIERT | 6094 | stark_zentriert_wenig_rand | 0.9524 | 0.0471 | 0.0005 | 0.2491 | 0.7462 | 0.5985 | 0.1248 | 0.9043 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SEQUENZ_ORIGINAL | zentrum_stabil | 0.9539 | 0.7496 | 0.6033 | 0.1223 | 0.9098 | 0.2622 | 0.2138 | dio_mcm_episode_0wjn8vm | dio_1fll |
| SEQUENZ_ORIGINAL | offene_variante | 0.0456 | 0.6763 | 0.4995 | 0.1769 | 0.7916 | 0.0000 | 1.0000 | dio_mcm_episode_0wjn8vm | dio_0lwq |
| SEQUENZ_ORIGINAL | spannungsrand_kippnaehe | 0.0005 | 0.5743 | 0.3194 | 0.3192 | 0.6607 | 0.0000 | 1.0000 | dio_mcm_episode_0sxikqi | dio_0kcg |
| SEQUENZ_PERMUTIERT | zentrum_stabil | 0.9524 | 0.7497 | 0.6036 | 0.1221 | 0.9100 | 0.2626 | 0.2126 | dio_mcm_episode_0wjn8vm | dio_1fll |
| SEQUENZ_PERMUTIERT | offene_variante | 0.0471 | 0.6756 | 0.4980 | 0.1764 | 0.7920 | 0.0000 | 1.0000 | dio_mcm_episode_0wjn8vm | dio_0lwq |
| SEQUENZ_PERMUTIERT | spannungsrand_kippnaehe | 0.0005 | 0.5753 | 0.3191 | 0.3177 | 0.6648 | 0.0000 | 1.0000 | dio_mcm_episode_0sxikqi | dio_1rrr |

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
