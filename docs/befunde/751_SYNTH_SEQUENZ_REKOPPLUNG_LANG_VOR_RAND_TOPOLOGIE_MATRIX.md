# Weltrelative Topologie-Matrix

Stand: 2026-06-22 20:29:30

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
| REKOPPLUNG_LANG_VOR_RAND | 7494 | stark_zentriert_wenig_rand | 0.9590 | 0.0403 | 0.0007 | 0.2486 | 0.7485 | 0.6030 | 0.1240 | 0.9063 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SEQUENZ_ORIGINAL | zentrum_stabil | 0.9539 | 0.7496 | 0.6033 | 0.1223 | 0.9098 | 0.2622 | 0.2138 | dio_mcm_episode_0wjn8vm | dio_1fll |
| SEQUENZ_ORIGINAL | offene_variante | 0.0456 | 0.6763 | 0.4995 | 0.1769 | 0.7916 | 0.0000 | 1.0000 | dio_mcm_episode_0wjn8vm | dio_0lwq |
| SEQUENZ_ORIGINAL | spannungsrand_kippnaehe | 0.0005 | 0.5743 | 0.3194 | 0.3192 | 0.6607 | 0.0000 | 1.0000 | dio_mcm_episode_0sxikqi | dio_0kcg |
| REKOPPLUNG_LANG_VOR_RAND | zentrum_stabil | 0.9590 | 0.7518 | 0.6076 | 0.1216 | 0.9116 | 0.2607 | 0.2180 | dio_mcm_episode_0qvodoj | dio_1fll |
| REKOPPLUNG_LANG_VOR_RAND | offene_variante | 0.0403 | 0.6732 | 0.4965 | 0.1788 | 0.7857 | 0.0000 | 1.0000 | dio_mcm_episode_0mji3u6 | dio_0lwq |
| REKOPPLUNG_LANG_VOR_RAND | spannungsrand_kippnaehe | 0.0007 | 0.5771 | 0.3269 | 0.3144 | 0.6712 | 0.0000 | 1.0000 | dio_mcm_episode_0sxikqi | dio_1rrr |

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
