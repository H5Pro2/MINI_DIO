# Weltrelative Topologie-Matrix

Stand: 2026-06-22 10:36:22

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
| SYNTH_RAND_A | 6994 | stark_zentriert_wenig_rand | 0.9375 | 0.0603 | 0.0021 | 0.2501 | 0.7405 | 0.5898 | 0.1311 | 0.8979 |
| SYNTH_RAND_B | 6994 | stark_zentriert_wenig_rand | 0.9375 | 0.0603 | 0.0021 | 0.2501 | 0.7405 | 0.5898 | 0.1311 | 0.8979 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SYNTH_RAND_A | zentrum_stabil | 0.9375 | 0.7460 | 0.5973 | 0.1262 | 0.9065 | 0.2667 | 0.2001 | dio_mcm_episode_08lp0ua | dio_1fll |
| SYNTH_RAND_A | offene_variante | 0.0603 | 0.6619 | 0.4819 | 0.2020 | 0.7719 | 0.0000 | 1.0000 | dio_mcm_episode_0mji3u6 | dio_1v2w |
| SYNTH_RAND_A | spannungsrand_kippnaehe | 0.0021 | 0.5930 | 0.3770 | 0.2997 | 0.6951 | 0.0000 | 1.0000 | dio_mcm_episode_0mji3u6 | dio_0zmn |
| SYNTH_RAND_B | zentrum_stabil | 0.9375 | 0.7460 | 0.5973 | 0.1262 | 0.9065 | 0.2667 | 0.2001 | dio_mcm_episode_08lp0ua | dio_1fll |
| SYNTH_RAND_B | offene_variante | 0.0603 | 0.6619 | 0.4819 | 0.2020 | 0.7719 | 0.0000 | 1.0000 | dio_mcm_episode_0mji3u6 | dio_1v2w |
| SYNTH_RAND_B | spannungsrand_kippnaehe | 0.0021 | 0.5930 | 0.3770 | 0.2997 | 0.6951 | 0.0000 | 1.0000 | dio_mcm_episode_0mji3u6 | dio_0zmn |

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
