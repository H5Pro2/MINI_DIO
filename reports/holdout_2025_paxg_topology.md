# Weltrelative Topologie-Matrix

Stand: 2026-07-08 12:47:49

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
| PAXG_2025_5M_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9950 | 0.0050 | 0.0000 | 0.2417 | 0.7165 | 0.5397 | 0.1565 | 0.8628 |
| PAXG_2025_15M_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9900 | 0.0100 | 0.0000 | 0.2467 | 0.6984 | 0.5179 | 0.1639 | 0.8441 |
| PAXG_2025_1H_HOLDOUT | 1994 | stark_zentriert_wenig_rand | 0.9935 | 0.0065 | 0.0000 | 0.2477 | 0.6952 | 0.5162 | 0.1665 | 0.8400 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| PAXG_2025_5M_HOLDOUT | zentrum_stabil | 0.9950 | 0.7172 | 0.5407 | 0.1558 | 0.8636 | 0.2515 | 0.2465 | dio_mcm_episode_0iwh9d2 | dio_14wj |
| PAXG_2025_5M_HOLDOUT | offene_variante | 0.0050 | 0.5803 | 0.3582 | 0.2863 | 0.6874 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_03h4 |
| PAXG_2025_15M_HOLDOUT | zentrum_stabil | 0.9900 | 0.6996 | 0.5196 | 0.1625 | 0.8459 | 0.2528 | 0.2427 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_2025_15M_HOLDOUT | offene_variante | 0.0100 | 0.5759 | 0.3498 | 0.2979 | 0.6685 | 0.0000 | 1.0000 | dio_mcm_episode_0xg0gjh | dio_03h4 |
| PAXG_2025_1H_HOLDOUT | zentrum_stabil | 0.9935 | 0.6960 | 0.5172 | 0.1657 | 0.8411 | 0.2519 | 0.2453 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_2025_1H_HOLDOUT | offene_variante | 0.0065 | 0.5776 | 0.3605 | 0.2875 | 0.6694 | 0.0000 | 1.0000 | dio_mcm_episode_0x60uui | dio_0ac6 |

## Lesart

Zentrumsnahe Welten: 3
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
