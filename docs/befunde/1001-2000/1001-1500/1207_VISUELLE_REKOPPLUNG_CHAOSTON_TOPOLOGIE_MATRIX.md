# Weltrelative Topologie-Matrix

Stand: 2026-07-01 10:25:14

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
| SYNTH_VIS_RECOUPLE_CHAOTIC_TONE | 6594 | gemischte_rollenordnung | 0.9484 | 0.0285 | 0.0231 | 0.2496 | 0.7467 | 0.5906 | 0.1359 | 0.8999 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SYNTH_VIS_RECOUPLE_CHAOTIC_TONE | zentrum_stabil | 0.9484 | 0.7524 | 0.5987 | 0.1287 | 0.9100 | 0.2637 | 0.2093 | dio_mcm_episode_0nyb3ro | dio_1fll |
| SYNTH_VIS_RECOUPLE_CHAOTIC_TONE | offene_variante | 0.0285 | 0.6621 | 0.4770 | 0.2266 | 0.7693 | 0.0000 | 1.0000 | dio_mcm_episode_0nyb3ro | dio_1wge |
| SYNTH_VIS_RECOUPLE_CHAOTIC_TONE | spannungsrand_kippnaehe | 0.0231 | 0.6170 | 0.4009 | 0.3200 | 0.6447 | 0.0000 | 1.0000 | dio_mcm_episode_0nyb3ro | dio_03rd |

## Lesart

Zentrumsnahe Welten: 0
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
