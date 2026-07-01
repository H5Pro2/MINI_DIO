# Weltrelative Topologie-Matrix

Stand: 2026-07-01 10:16:41

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
| SYNTH_VIS_BREAK_STABLE_PULSE | 6594 | stark_zentriert_wenig_rand | 0.9848 | 0.0149 | 0.0003 | 0.2501 | 0.7336 | 0.5772 | 0.1398 | 0.8917 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SYNTH_VIS_BREAK_STABLE_PULSE | zentrum_stabil | 0.9848 | 0.7344 | 0.5781 | 0.1390 | 0.8930 | 0.2539 | 0.2385 | dio_mcm_episode_077r0df | dio_1fll |
| SYNTH_VIS_BREAK_STABLE_PULSE | offene_variante | 0.0149 | 0.6839 | 0.5200 | 0.1913 | 0.8118 | 0.0000 | 1.0000 | dio_mcm_episode_077r0df | dio_17db |
| SYNTH_VIS_BREAK_STABLE_PULSE | spannungsrand_kippnaehe | 0.0003 | 0.5737 | 0.3200 | 0.3164 | 0.6679 | 0.0000 | 1.0000 | dio_mcm_episode_0sxikqi | dio_0kcg |

## Lesart

Zentrumsnahe Welten: 1
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
