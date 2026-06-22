# Weltrelative Topologie-Matrix

Stand: 2026-06-22 00:04:29

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
| PAXG2024_1H_YEAR | 8778 | stark_zentriert_wenig_rand | 0.8195 | 0.1691 | 0.0114 | 0.2479 | 0.7032 | 0.5310 | 0.1576 | 0.8434 |
| PAXG2025_1H_YEAR | 8754 | stark_zentriert_wenig_rand | 0.8336 | 0.1574 | 0.0090 | 0.2489 | 0.7045 | 0.5344 | 0.1559 | 0.8458 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| PAXG2024_1H_YEAR | zentrum_stabil | 0.8195 | 0.7130 | 0.5434 | 0.1471 | 0.8584 | 0.3044 | 0.1229 | dio_mcm_episode_0e7qvj1 | dio_104t |
| PAXG2024_1H_YEAR | offene_variante | 0.1691 | 0.6646 | 0.4834 | 0.1986 | 0.7805 | 0.0034 | 0.8160 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| PAXG2024_1H_YEAR | spannungsrand_kippnaehe | 0.0114 | 0.5751 | 0.3500 | 0.3080 | 0.6943 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1v58 |
| PAXG2025_1H_YEAR | zentrum_stabil | 0.8336 | 0.7136 | 0.5458 | 0.1464 | 0.8598 | 0.2996 | 0.1329 | dio_mcm_episode_0e7qvj1 | dio_104t |
| PAXG2025_1H_YEAR | offene_variante | 0.1574 | 0.6643 | 0.4843 | 0.1980 | 0.7802 | 0.0029 | 0.8273 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| PAXG2025_1H_YEAR | spannungsrand_kippnaehe | 0.0090 | 0.5752 | 0.3530 | 0.3074 | 0.6978 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |

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
