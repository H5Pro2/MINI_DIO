# Weltrelative Topologie-Matrix

Stand: 2026-06-22 22:03:01

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
| SYNTH_ZUFALLSNAH | 5794 | stark_zentriert_wenig_rand | 0.9517 | 0.0473 | 0.0010 | 0.2492 | 0.7457 | 0.5972 | 0.1251 | 0.9039 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SYNTH_ZUFALLSNAH | zentrum_stabil | 0.9517 | 0.7492 | 0.6024 | 0.1223 | 0.9097 | 0.2628 | 0.2122 | dio_mcm_episode_0wjn8vm | dio_1fll |
| SYNTH_ZUFALLSNAH | offene_variante | 0.0473 | 0.6771 | 0.4985 | 0.1762 | 0.7935 | 0.0000 | 1.0000 | dio_mcm_episode_1wj5tkj | dio_0lwq |
| SYNTH_ZUFALLSNAH | spannungsrand_kippnaehe | 0.0010 | 0.5858 | 0.3361 | 0.2989 | 0.7014 | 0.0000 | 1.0000 | dio_mcm_episode_0d9qets | dio_00wk |

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
