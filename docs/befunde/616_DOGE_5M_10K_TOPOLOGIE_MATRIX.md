# Weltrelative Topologie-Matrix

Stand: 2026-06-22 00:20:34

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
| DOGE2024_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8235 | 0.1656 | 0.0109 | 0.2494 | 0.7036 | 0.5350 | 0.1569 | 0.8439 |
| DOGE2025_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8300 | 0.1591 | 0.0109 | 0.2499 | 0.7036 | 0.5353 | 0.1570 | 0.8444 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| DOGE2024_5M_10K | zentrum_stabil | 0.8235 | 0.7134 | 0.5473 | 0.1465 | 0.8594 | 0.3035 | 0.1230 | dio_mcm_episode_0e7qvj1 | dio_104t |
| DOGE2024_5M_10K | offene_variante | 0.1656 | 0.6638 | 0.4858 | 0.1991 | 0.7772 | 0.0006 | 0.8326 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| DOGE2024_5M_10K | spannungsrand_kippnaehe | 0.0109 | 0.5737 | 0.3552 | 0.3086 | 0.6871 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_05cl |
| DOGE2025_5M_10K | zentrum_stabil | 0.8300 | 0.7130 | 0.5473 | 0.1470 | 0.8591 | 0.3011 | 0.1297 | dio_mcm_episode_0e7qvj1 | dio_104t |
| DOGE2025_5M_10K | offene_variante | 0.1591 | 0.6637 | 0.4852 | 0.1986 | 0.7783 | 0.0006 | 0.8264 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| DOGE2025_5M_10K | spannungsrand_kippnaehe | 0.0109 | 0.5729 | 0.3546 | 0.3121 | 0.6902 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |

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
