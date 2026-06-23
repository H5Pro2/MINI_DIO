# Weltrelative Topologie-Matrix

Stand: 2026-06-22 23:06:17

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
| REAL_SEQ_BREAK_SOL2025 | 1994 | stark_zentriert_wenig_rand | 0.8144 | 0.1745 | 0.0110 | 0.2503 | 0.6958 | 0.5118 | 0.1545 | 0.8437 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| REAL_SEQ_BREAK_SOL2025 | zentrum_stabil | 0.8144 | 0.7058 | 0.5246 | 0.1438 | 0.8597 | 0.3067 | 0.1139 | dio_mcm_episode_0e7qvj1 | dio_104t |
| REAL_SEQ_BREAK_SOL2025 | offene_variante | 0.1745 | 0.6572 | 0.4620 | 0.1950 | 0.7813 | 0.0029 | 0.8391 | dio_mcm_episode_0e7qvj1 | dio_0m9z |
| REAL_SEQ_BREAK_SOL2025 | spannungsrand_kippnaehe | 0.0110 | 0.5662 | 0.3493 | 0.3031 | 0.6510 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1hew |

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
