# Weltrelative Topologie-Matrix

Stand: 2026-06-21 16:32:50

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
| KAS2024_5M | 1994 | stark_zentriert_wenig_rand | 0.8079 | 0.1795 | 0.0125 | 0.2503 | 0.6930 | 0.5087 | 0.1606 | 0.8430 |
| KAS2024_15M | 1994 | stark_zentriert_wenig_rand | 0.8099 | 0.1770 | 0.0130 | 0.2503 | 0.6930 | 0.5086 | 0.1612 | 0.8433 |
| KAS2024_30M | 1994 | stark_zentriert_wenig_rand | 0.8054 | 0.1820 | 0.0125 | 0.2503 | 0.6923 | 0.5074 | 0.1618 | 0.8423 |
| KAS2024_1H | 1994 | gemischte_rollenordnung | 0.7914 | 0.1896 | 0.0191 | 0.2503 | 0.6923 | 0.5084 | 0.1622 | 0.8408 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| KAS2024_5M | zentrum_stabil | 0.8079 | 0.7033 | 0.5219 | 0.1489 | 0.8589 | 0.3097 | 0.1142 | dio_mcm_episode_0e7qvj1 | dio_104t |
| KAS2024_5M | offene_variante | 0.1795 | 0.6548 | 0.4607 | 0.2035 | 0.7813 | 0.0000 | 0.8101 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| KAS2024_5M | spannungsrand_kippnaehe | 0.0125 | 0.5723 | 0.3487 | 0.3070 | 0.6952 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_18i0 |
| KAS2024_15M | zentrum_stabil | 0.8099 | 0.7037 | 0.5227 | 0.1493 | 0.8591 | 0.3090 | 0.1152 | dio_mcm_episode_0e7qvj1 | dio_104t |
| KAS2024_15M | offene_variante | 0.1770 | 0.6526 | 0.4559 | 0.2052 | 0.7824 | 0.0000 | 0.8130 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| KAS2024_15M | spannungsrand_kippnaehe | 0.0130 | 0.5725 | 0.3509 | 0.3074 | 0.6885 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_18f1 |
| KAS2024_30M | zentrum_stabil | 0.8054 | 0.7029 | 0.5208 | 0.1500 | 0.8588 | 0.3107 | 0.1183 | dio_mcm_episode_0e7qvj1 | dio_104t |
| KAS2024_30M | offene_variante | 0.1820 | 0.6533 | 0.4588 | 0.2046 | 0.7782 | 0.0000 | 0.7824 | dio_mcm_episode_0e7qvj1 | dio_0jkk |
| KAS2024_30M | spannungsrand_kippnaehe | 0.0125 | 0.5779 | 0.3550 | 0.3025 | 0.7075 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0zmn |
| KAS2024_1H | zentrum_stabil | 0.7914 | 0.7040 | 0.5233 | 0.1490 | 0.8588 | 0.3162 | 0.1103 | dio_mcm_episode_0e7qvj1 | dio_104t |
| KAS2024_1H | offene_variante | 0.1896 | 0.6551 | 0.4618 | 0.2027 | 0.7797 | 0.0000 | 0.7593 | dio_mcm_episode_0e7qvj1 | dio_0jkk |
| KAS2024_1H | spannungsrand_kippnaehe | 0.0191 | 0.5750 | 0.3529 | 0.3086 | 0.7005 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |

## Lesart

Zentrumsnahe Welten: 3
Gemischte Rollenordnung: 1
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
