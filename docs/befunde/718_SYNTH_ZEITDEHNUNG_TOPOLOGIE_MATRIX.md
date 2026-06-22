# Weltrelative Topologie-Matrix

Stand: 2026-06-22 13:04:33

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
| ZEIT_KOMPAKT | 2994 | stark_zentriert_wenig_rand | 0.9522 | 0.0468 | 0.0010 | 0.2495 | 0.7404 | 0.5862 | 0.1263 | 0.9010 |
| ZEIT_GEDEHNT | 11994 | stark_zentriert_wenig_rand | 0.9537 | 0.0460 | 0.0003 | 0.2496 | 0.7494 | 0.6055 | 0.1241 | 0.9059 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ZEIT_KOMPAKT | zentrum_stabil | 0.9522 | 0.7442 | 0.5918 | 0.1234 | 0.9067 | 0.2627 | 0.2126 | dio_mcm_episode_0wjn8vm | dio_1fll |
| ZEIT_KOMPAKT | offene_variante | 0.0468 | 0.6666 | 0.4786 | 0.1812 | 0.7894 | 0.0000 | 1.0000 | dio_mcm_episode_0wjn8vm | dio_0lwq |
| ZEIT_KOMPAKT | spannungsrand_kippnaehe | 0.0010 | 0.5812 | 0.3231 | 0.3080 | 0.6788 | 0.0000 | 1.0000 | dio_mcm_episode_0r9ht2p | dio_0kcg |
| ZEIT_GEDEHNT | zentrum_stabil | 0.9537 | 0.7526 | 0.6098 | 0.1216 | 0.9115 | 0.2622 | 0.2137 | dio_mcm_episode_0qvodoj | dio_1fll |
| ZEIT_GEDEHNT | offene_variante | 0.0460 | 0.6832 | 0.5162 | 0.1748 | 0.7922 | 0.0000 | 1.0000 | dio_mcm_episode_08lp0ua | dio_0lwq |
| ZEIT_GEDEHNT | spannungsrand_kippnaehe | 0.0003 | 0.5827 | 0.3250 | 0.3073 | 0.6832 | 0.0000 | 1.0000 | dio_mcm_episode_0sxikqi | dio_1rrr |

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
