# Weltrelative Topologie-Matrix

Stand: 2026-06-21 22:51:36

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
| BTC2024_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8302 | 0.1599 | 0.0099 | 0.2497 | 0.7037 | 0.5350 | 0.1567 | 0.8440 |
| BTC2025_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8400 | 0.1492 | 0.0108 | 0.2498 | 0.7041 | 0.5353 | 0.1561 | 0.8455 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC2024_5M_10K | zentrum_stabil | 0.8302 | 0.7130 | 0.5471 | 0.1468 | 0.8586 | 0.3011 | 0.1292 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC2024_5M_10K | offene_variante | 0.1599 | 0.6633 | 0.4842 | 0.1989 | 0.7777 | 0.0006 | 0.8310 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| BTC2024_5M_10K | spannungsrand_kippnaehe | 0.0099 | 0.5725 | 0.3483 | 0.3118 | 0.6947 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0qj7 |
| BTC2025_5M_10K | zentrum_stabil | 0.8400 | 0.7132 | 0.5470 | 0.1464 | 0.8596 | 0.2977 | 0.1354 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC2025_5M_10K | offene_variante | 0.1492 | 0.6625 | 0.4828 | 0.1993 | 0.7769 | 0.0000 | 0.8410 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| BTC2025_5M_10K | spannungsrand_kippnaehe | 0.0108 | 0.5717 | 0.3497 | 0.3123 | 0.6912 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_02zp |

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
