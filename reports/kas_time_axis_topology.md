# Weltrelative Topologie-Matrix

Stand: 2026-07-08 11:53:17

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
| KAS_2024_5M | 1994 | stark_zentriert_wenig_rand | 0.9895 | 0.0105 | 0.0000 | 0.2503 | 0.6951 | 0.5193 | 0.1663 | 0.8399 |
| KAS_2024_15M | 1994 | stark_zentriert_wenig_rand | 0.9915 | 0.0085 | 0.0000 | 0.2503 | 0.6949 | 0.5189 | 0.1667 | 0.8401 |
| KAS_2024_30M | 1994 | stark_zentriert_wenig_rand | 0.9895 | 0.0105 | 0.0000 | 0.2503 | 0.6943 | 0.5175 | 0.1669 | 0.8391 |
| KAS_2024_1H | 1994 | stark_zentriert_wenig_rand | 0.9855 | 0.0145 | 0.0000 | 0.2503 | 0.6945 | 0.5190 | 0.1675 | 0.8377 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| KAS_2024_5M | zentrum_stabil | 0.9895 | 0.6963 | 0.5210 | 0.1651 | 0.8418 | 0.2529 | 0.2423 | dio_mcm_episode_1qlxgj7 | dio_104t |
| KAS_2024_5M | offene_variante | 0.0105 | 0.5772 | 0.3642 | 0.2865 | 0.6640 | 0.0000 | 1.0000 | dio_mcm_episode_0wyzu1s | dio_16i6 |
| KAS_2024_15M | zentrum_stabil | 0.9915 | 0.6960 | 0.5202 | 0.1656 | 0.8418 | 0.2524 | 0.2438 | dio_mcm_episode_1qlxgj7 | dio_104t |
| KAS_2024_15M | offene_variante | 0.0085 | 0.5720 | 0.3618 | 0.2947 | 0.6461 | 0.0000 | 1.0000 | dio_mcm_episode_0stzut8 | dio_17qo |
| KAS_2024_30M | zentrum_stabil | 0.9895 | 0.6955 | 0.5191 | 0.1657 | 0.8409 | 0.2529 | 0.2423 | dio_mcm_episode_1qlxgj7 | dio_104t |
| KAS_2024_30M | offene_variante | 0.0105 | 0.5818 | 0.3677 | 0.2821 | 0.6746 | 0.0000 | 1.0000 | dio_mcm_episode_16bqw8k | dio_19v1 |
| KAS_2024_1H | zentrum_stabil | 0.9855 | 0.6962 | 0.5213 | 0.1656 | 0.8403 | 0.2539 | 0.2392 | dio_mcm_episode_1qlxgj7 | dio_104t |
| KAS_2024_1H | offene_variante | 0.0145 | 0.5757 | 0.3623 | 0.2910 | 0.6634 | 0.0000 | 1.0000 | dio_mcm_episode_0r7nk4p | dio_0vfj |

## Lesart

Zentrumsnahe Welten: 4
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
