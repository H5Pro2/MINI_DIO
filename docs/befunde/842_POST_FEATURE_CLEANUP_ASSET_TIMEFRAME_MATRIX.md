# Weltrelative Topologie-Matrix

Stand: 2026-06-26 10:12:33

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
| POST_CLEAN_ASSET_TF_BTC_2025_5M | 9994 | stark_zentriert_wenig_rand | 0.8138 | 0.1802 | 0.0060 | 0.2498 | 0.7054 | 0.5374 | 0.1518 | 0.8429 |
| POST_CLEAN_ASSET_TF_BTC_2025_1H_FULL | 8754 | stark_zentriert_wenig_rand | 0.8072 | 0.1848 | 0.0080 | 0.2496 | 0.7063 | 0.5383 | 0.1518 | 0.8434 |
| POST_CLEAN_ASSET_TF_PAXG_2025_5M | 9994 | stark_zentriert_wenig_rand | 0.8512 | 0.1454 | 0.0034 | 0.2455 | 0.7151 | 0.5432 | 0.1476 | 0.8536 |
| POST_CLEAN_ASSET_TF_PAXG_2025_1H | 8754 | stark_zentriert_wenig_rand | 0.8093 | 0.1862 | 0.0045 | 0.2485 | 0.7057 | 0.5361 | 0.1517 | 0.8433 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| POST_CLEAN_ASSET_TF_BTC_2025_5M | zentrum_stabil | 0.8138 | 0.7148 | 0.5489 | 0.1420 | 0.8591 | 0.3073 | 0.1145 | dio_mcm_episode_0e7qvj1 | dio_104t |
| POST_CLEAN_ASSET_TF_BTC_2025_5M | offene_variante | 0.1802 | 0.6675 | 0.4913 | 0.1907 | 0.7762 | 0.0006 | 0.8373 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| POST_CLEAN_ASSET_TF_BTC_2025_5M | spannungsrand_kippnaehe | 0.0060 | 0.5691 | 0.3553 | 0.3035 | 0.6533 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1c6r |
| POST_CLEAN_ASSET_TF_BTC_2025_1H_FULL | zentrum_stabil | 0.8072 | 0.7166 | 0.5511 | 0.1412 | 0.8604 | 0.3095 | 0.1044 | dio_mcm_episode_0e7qvj1 | dio_104t |
| POST_CLEAN_ASSET_TF_BTC_2025_1H_FULL | offene_variante | 0.1848 | 0.6671 | 0.4900 | 0.1915 | 0.7768 | 0.0012 | 0.8535 | dio_mcm_episode_0e7qvj1 | dio_0m9z |
| POST_CLEAN_ASSET_TF_BTC_2025_1H_FULL | spannungsrand_kippnaehe | 0.0080 | 0.5709 | 0.3576 | 0.3005 | 0.6585 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0ku7 |
| POST_CLEAN_ASSET_TF_PAXG_2025_5M | zentrum_stabil | 0.8512 | 0.7234 | 0.5536 | 0.1395 | 0.8666 | 0.2936 | 0.1369 | dio_mcm_episode_1xx3u1e | dio_14wj |
| POST_CLEAN_ASSET_TF_PAXG_2025_5M | offene_variante | 0.1454 | 0.6696 | 0.4866 | 0.1915 | 0.7814 | 0.0007 | 0.8947 | dio_mcm_episode_1xx3u1e | dio_0m9z |
| POST_CLEAN_ASSET_TF_PAXG_2025_5M | spannungsrand_kippnaehe | 0.0034 | 0.5792 | 0.3567 | 0.2955 | 0.6793 | 0.0000 | 1.0000 | dio_mcm_episode_0ybr5e3 | dio_0xvx |
| POST_CLEAN_ASSET_TF_PAXG_2025_1H | zentrum_stabil | 0.8093 | 0.7150 | 0.5476 | 0.1420 | 0.8591 | 0.3081 | 0.1122 | dio_mcm_episode_0b7nep9 | dio_104t |
| POST_CLEAN_ASSET_TF_PAXG_2025_1H | offene_variante | 0.1862 | 0.6682 | 0.4907 | 0.1901 | 0.7786 | 0.0043 | 0.8313 | dio_mcm_episode_0b7nep9 | dio_00ja |
| POST_CLEAN_ASSET_TF_PAXG_2025_1H | spannungsrand_kippnaehe | 0.0045 | 0.5688 | 0.3521 | 0.3020 | 0.6606 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |

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

Als naechstes sollte die Asset-/Zeitrahmen-Pruefung um weitere Weltarten erweitert werden.
Ziel ist zu klaeren, ob die starke Zentrierung bei BTC/PAXG ein Zeichen robuster Rezeptoradaptation ist oder ob andere Assets wie DOGE/XRP/KAS wieder mehr offene Variante und Randspannung ausbilden.
