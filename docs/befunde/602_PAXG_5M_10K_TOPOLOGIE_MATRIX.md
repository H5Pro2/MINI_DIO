# Weltrelative Topologie-Matrix

Stand: 2026-06-21 23:55:49

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
| PAXG2024_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8797 | 0.1142 | 0.0061 | 0.2473 | 0.7135 | 0.5386 | 0.1523 | 0.8545 |
| PAXG2025_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8724 | 0.1204 | 0.0072 | 0.2471 | 0.7140 | 0.5414 | 0.1515 | 0.8557 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| PAXG2024_5M_10K | zentrum_stabil | 0.8797 | 0.7203 | 0.5474 | 0.1452 | 0.8643 | 0.2839 | 0.1661 | dio_mcm_episode_1eju9g0 | dio_104t |
| PAXG2024_5M_10K | offene_variante | 0.1142 | 0.6681 | 0.4810 | 0.1985 | 0.7863 | 0.0026 | 0.8571 | dio_mcm_episode_1eju9g0 | dio_00ja |
| PAXG2024_5M_10K | spannungsrand_kippnaehe | 0.0061 | 0.5816 | 0.3507 | 0.3027 | 0.7152 | 0.0000 | 1.0000 | dio_mcm_episode_1eju9g0 | dio_0hgv |
| PAXG2025_5M_10K | zentrum_stabil | 0.8724 | 0.7219 | 0.5517 | 0.1434 | 0.8669 | 0.2866 | 0.1546 | dio_mcm_episode_1hdpu9s | dio_104t |
| PAXG2025_5M_10K | offene_variante | 0.1204 | 0.6647 | 0.4786 | 0.2004 | 0.7832 | 0.0000 | 0.8969 | dio_mcm_episode_1hdpu9s | dio_00ja |
| PAXG2025_5M_10K | spannungsrand_kippnaehe | 0.0072 | 0.5811 | 0.3506 | 0.3043 | 0.7084 | 0.0000 | 1.0000 | dio_mcm_episode_1hdpu9s | dio_00hc |

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
