# Weltrelative Topologie-Matrix

Stand: 2026-06-22 01:05:16

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
| XRP2024_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8280 | 0.1581 | 0.0139 | 0.2495 | 0.7042 | 0.5356 | 0.1564 | 0.8444 |
| XRP2025_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8380 | 0.1517 | 0.0103 | 0.2498 | 0.7044 | 0.5363 | 0.1565 | 0.8453 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| XRP2024_5M_10K | zentrum_stabil | 0.8280 | 0.7142 | 0.5483 | 0.1456 | 0.8600 | 0.3020 | 0.1239 | dio_mcm_episode_0e7qvj1 | dio_104t |
| XRP2024_5M_10K | offene_variante | 0.1581 | 0.6635 | 0.4851 | 0.1994 | 0.7768 | 0.0000 | 0.8449 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| XRP2024_5M_10K | spannungsrand_kippnaehe | 0.0139 | 0.5744 | 0.3600 | 0.3088 | 0.6849 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0n8c |
| XRP2025_5M_10K | zentrum_stabil | 0.8380 | 0.7137 | 0.5484 | 0.1466 | 0.8597 | 0.2984 | 0.1324 | dio_mcm_episode_0e7qvj1 | dio_104t |
| XRP2025_5M_10K | offene_variante | 0.1517 | 0.6616 | 0.4821 | 0.2008 | 0.7756 | 0.0000 | 0.8496 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| XRP2025_5M_10K | spannungsrand_kippnaehe | 0.0103 | 0.5739 | 0.3530 | 0.3103 | 0.6947 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_18f1 |

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
