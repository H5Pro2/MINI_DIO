# Weltrelative Topologie-Matrix

Stand: 2026-06-22 00:27:48

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
| DOGE2024_1H_YEAR | 8778 | stark_zentriert_wenig_rand | 0.8237 | 0.1634 | 0.0130 | 0.2498 | 0.7036 | 0.5348 | 0.1574 | 0.8441 |
| DOGE2025_1H_YEAR | 8754 | stark_zentriert_wenig_rand | 0.8132 | 0.1719 | 0.0149 | 0.2498 | 0.7033 | 0.5346 | 0.1576 | 0.8430 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| DOGE2024_1H_YEAR | zentrum_stabil | 0.8237 | 0.7137 | 0.5478 | 0.1465 | 0.8597 | 0.3036 | 0.1196 | dio_mcm_episode_0e7qvj1 | dio_104t |
| DOGE2024_1H_YEAR | offene_variante | 0.1634 | 0.6627 | 0.4834 | 0.2001 | 0.7773 | 0.0000 | 0.8480 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| DOGE2024_1H_YEAR | spannungsrand_kippnaehe | 0.0130 | 0.5767 | 0.3574 | 0.3063 | 0.6966 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0qj7 |
| DOGE2025_1H_YEAR | zentrum_stabil | 0.8132 | 0.7137 | 0.5476 | 0.1462 | 0.8593 | 0.3073 | 0.1122 | dio_mcm_episode_0e7qvj1 | dio_104t |
| DOGE2025_1H_YEAR | offene_variante | 0.1719 | 0.6650 | 0.4879 | 0.1984 | 0.7797 | 0.0007 | 0.8372 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| DOGE2025_1H_YEAR | spannungsrand_kippnaehe | 0.0149 | 0.5743 | 0.3598 | 0.3102 | 0.6872 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0zmn |

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
