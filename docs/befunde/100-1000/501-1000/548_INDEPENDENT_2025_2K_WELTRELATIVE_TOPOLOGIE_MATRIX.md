# Weltrelative Topologie-Matrix

Stand: 2026-06-21 21:04:39

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
| BTC2025_5M_2K | 1994 | stark_zentriert_wenig_rand | 0.8205 | 0.1660 | 0.0135 | 0.2497 | 0.6921 | 0.5082 | 0.1600 | 0.8430 |
| BTC2025_1H_2K | 1994 | stark_zentriert_wenig_rand | 0.8305 | 0.1525 | 0.0171 | 0.2503 | 0.6960 | 0.5136 | 0.1577 | 0.8465 |
| SOL2025_5M_2K | 1994 | gemischte_rollenordnung | 0.7844 | 0.2046 | 0.0110 | 0.2503 | 0.6908 | 0.5073 | 0.1612 | 0.8400 |
| SOL2025_1H_2K | 1994 | stark_zentriert_wenig_rand | 0.8109 | 0.1710 | 0.0181 | 0.2503 | 0.6932 | 0.5105 | 0.1603 | 0.8434 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC2025_5M_2K | zentrum_stabil | 0.8205 | 0.7022 | 0.5212 | 0.1490 | 0.8582 | 0.3050 | 0.1290 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC2025_5M_2K | offene_variante | 0.1660 | 0.6525 | 0.4574 | 0.2022 | 0.7797 | 0.0000 | 0.7885 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| BTC2025_5M_2K | spannungsrand_kippnaehe | 0.0135 | 0.5705 | 0.3443 | 0.3127 | 0.7025 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1x3j |
| BTC2025_1H_2K | zentrum_stabil | 0.8305 | 0.7069 | 0.5281 | 0.1460 | 0.8619 | 0.3013 | 0.1238 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC2025_1H_2K | offene_variante | 0.1525 | 0.6505 | 0.4532 | 0.2043 | 0.7797 | 0.0000 | 0.8553 | dio_mcm_episode_0e7qvj1 | dio_0jkk |
| BTC2025_1H_2K | spannungsrand_kippnaehe | 0.0171 | 0.5711 | 0.3464 | 0.3099 | 0.6930 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1qya |
| SOL2025_5M_2K | zentrum_stabil | 0.7844 | 0.7015 | 0.5204 | 0.1488 | 0.8573 | 0.3191 | 0.1087 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SOL2025_5M_2K | offene_variante | 0.2046 | 0.6560 | 0.4656 | 0.2011 | 0.7811 | 0.0000 | 0.7525 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SOL2025_5M_2K | spannungsrand_kippnaehe | 0.0110 | 0.5732 | 0.3507 | 0.3078 | 0.7015 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0l74 |
| SOL2025_1H_2K | zentrum_stabil | 0.8109 | 0.7047 | 0.5255 | 0.1477 | 0.8602 | 0.3086 | 0.1138 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SOL2025_1H_2K | offene_variante | 0.1710 | 0.6518 | 0.4567 | 0.2040 | 0.7795 | 0.0000 | 0.8182 | dio_mcm_episode_0e7qvj1 | dio_05yg |
| SOL2025_1H_2K | spannungsrand_kippnaehe | 0.0181 | 0.5712 | 0.3477 | 0.3134 | 0.6940 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_05cl |

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
