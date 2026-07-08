# Weltrelative Topologie-Matrix

Stand: 2026-07-08 13:00:53

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
| PAXG_2025_5M_SHIFT1 | 1994 | stark_zentriert_wenig_rand | 0.9935 | 0.0065 | 0.0000 | 0.2442 | 0.7066 | 0.5278 | 0.1599 | 0.8535 |
| PAXG_2025_15M_SHIFT1 | 1994 | stark_zentriert_wenig_rand | 0.9900 | 0.0100 | 0.0000 | 0.2462 | 0.6957 | 0.5150 | 0.1660 | 0.8407 |
| PAXG_2025_1H_SHIFT1 | 1994 | stark_zentriert_wenig_rand | 0.9930 | 0.0070 | 0.0000 | 0.2477 | 0.6981 | 0.5220 | 0.1639 | 0.8445 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| PAXG_2025_5M_SHIFT1 | zentrum_stabil | 0.9935 | 0.7074 | 0.5290 | 0.1590 | 0.8546 | 0.2519 | 0.2453 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_2025_5M_SHIFT1 | offene_variante | 0.0065 | 0.5821 | 0.3510 | 0.2935 | 0.6819 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_033x |
| PAXG_2025_15M_SHIFT1 | zentrum_stabil | 0.9900 | 0.6968 | 0.5166 | 0.1647 | 0.8424 | 0.2528 | 0.2427 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_2025_15M_SHIFT1 | offene_variante | 0.0100 | 0.5815 | 0.3553 | 0.2895 | 0.6787 | 0.0000 | 1.0000 | dio_mcm_episode_0x60uui | dio_033x |
| PAXG_2025_1H_SHIFT1 | zentrum_stabil | 0.9930 | 0.6990 | 0.5232 | 0.1630 | 0.8457 | 0.2520 | 0.2449 | dio_mcm_episode_1qlxgj7 | dio_104t |
| PAXG_2025_1H_SHIFT1 | offene_variante | 0.0070 | 0.5777 | 0.3623 | 0.2872 | 0.6691 | 0.0000 | 1.0000 | dio_mcm_episode_0x60uui | dio_16i6 |

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
