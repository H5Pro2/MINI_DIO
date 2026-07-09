# Weltrelative Topologie-Matrix

Stand: 2026-06-23 00:10:12

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
| REAL_QUIET_SOL2025 | 1994 | gemischte_rollenordnung | 0.7703 | 0.2192 | 0.0105 | 0.2503 | 0.6940 | 0.5101 | 0.1565 | 0.8396 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| REAL_QUIET_SOL2025 | zentrum_stabil | 0.7703 | 0.7052 | 0.5237 | 0.1440 | 0.8590 | 0.3249 | 0.0918 | dio_mcm_episode_0e7qvj1 | dio_104t |
| REAL_QUIET_SOL2025 | offene_variante | 0.2192 | 0.6605 | 0.4700 | 0.1933 | 0.7791 | 0.0000 | 0.7712 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| REAL_QUIET_SOL2025 | spannungsrand_kippnaehe | 0.0105 | 0.5719 | 0.3513 | 0.3006 | 0.6807 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |

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
