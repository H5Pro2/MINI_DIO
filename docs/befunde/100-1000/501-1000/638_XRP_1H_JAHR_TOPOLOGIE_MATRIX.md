# Weltrelative Topologie-Matrix

Stand: 2026-06-22 01:12:10

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
| XRP2024_1H | 8778 | stark_zentriert_wenig_rand | 0.8380 | 0.1486 | 0.0134 | 0.2495 | 0.7047 | 0.5360 | 0.1566 | 0.8460 |
| XRP2025_1H | 8754 | stark_zentriert_wenig_rand | 0.8208 | 0.1642 | 0.0151 | 0.2495 | 0.7034 | 0.5347 | 0.1576 | 0.8434 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| XRP2024_1H | zentrum_stabil | 0.8380 | 0.7150 | 0.5495 | 0.1459 | 0.8612 | 0.2984 | 0.1270 | dio_mcm_episode_0e7qvj1 | dio_104t |
| XRP2024_1H | offene_variante | 0.1486 | 0.6587 | 0.4759 | 0.2030 | 0.7747 | 0.0000 | 0.8765 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| XRP2024_1H | spannungsrand_kippnaehe | 0.0134 | 0.5740 | 0.3573 | 0.3123 | 0.6880 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_18f1 |
| XRP2025_1H | zentrum_stabil | 0.8208 | 0.7138 | 0.5479 | 0.1465 | 0.8593 | 0.3044 | 0.1182 | dio_mcm_episode_0e7qvj1 | dio_104t |
| XRP2025_1H | offene_variante | 0.1642 | 0.6635 | 0.4848 | 0.1994 | 0.7780 | 0.0014 | 0.8406 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| XRP2025_1H | spannungsrand_kippnaehe | 0.0151 | 0.5737 | 0.3554 | 0.3099 | 0.6891 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |

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
