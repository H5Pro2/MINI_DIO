# Weltrelative Topologie-Matrix

Stand: 2026-06-26 10:46:06

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
| POST_CLEAN_DIVERSE_DOGE_2025_5M | 9994 | stark_zentriert_wenig_rand | 0.8012 | 0.1921 | 0.0067 | 0.2499 | 0.7048 | 0.5372 | 0.1526 | 0.8418 |
| POST_CLEAN_DIVERSE_XRP_2025_5M | 9994 | stark_zentriert_wenig_rand | 0.8111 | 0.1831 | 0.0058 | 0.2499 | 0.7056 | 0.5385 | 0.1523 | 0.8427 |
| POST_CLEAN_DIVERSE_KAS_2024_5M | 1994 | gemischte_rollenordnung | 0.7783 | 0.2131 | 0.0085 | 0.2503 | 0.6932 | 0.5107 | 0.1557 | 0.8396 |
| POST_CLEAN_DIVERSE_SYNTH_RAND_A | 6994 | stark_zentriert_wenig_rand | 0.9312 | 0.0681 | 0.0007 | 0.2504 | 0.7410 | 0.5906 | 0.1297 | 0.8971 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| POST_CLEAN_DIVERSE_DOGE_2025_5M | zentrum_stabil | 0.8012 | 0.7147 | 0.5495 | 0.1423 | 0.8587 | 0.3120 | 0.1037 | dio_mcm_episode_0e7qvj1 | dio_104t |
| POST_CLEAN_DIVERSE_DOGE_2025_5M | offene_variante | 0.1921 | 0.6681 | 0.4923 | 0.1904 | 0.7777 | 0.0005 | 0.8344 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| POST_CLEAN_DIVERSE_DOGE_2025_5M | spannungsrand_kippnaehe | 0.0067 | 0.5696 | 0.3560 | 0.3029 | 0.6591 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0ku7 |
| POST_CLEAN_DIVERSE_XRP_2025_5M | zentrum_stabil | 0.8111 | 0.7153 | 0.5505 | 0.1422 | 0.8592 | 0.3083 | 0.1098 | dio_mcm_episode_0e7qvj1 | dio_104t |
| POST_CLEAN_DIVERSE_XRP_2025_5M | offene_variante | 0.1831 | 0.6668 | 0.4908 | 0.1919 | 0.7752 | 0.0000 | 0.8475 | dio_mcm_episode_0e7qvj1 | dio_0m9z |
| POST_CLEAN_DIVERSE_XRP_2025_5M | spannungsrand_kippnaehe | 0.0058 | 0.5720 | 0.3581 | 0.3018 | 0.6643 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_17qo |
| POST_CLEAN_DIVERSE_KAS_2024_5M | zentrum_stabil | 0.7783 | 0.7036 | 0.5231 | 0.1441 | 0.8578 | 0.3215 | 0.0979 | dio_mcm_episode_1joiyc3 | dio_104t |
| POST_CLEAN_DIVERSE_KAS_2024_5M | offene_variante | 0.2131 | 0.6600 | 0.4715 | 0.1923 | 0.7801 | 0.0000 | 0.7765 | dio_mcm_episode_1joiyc3 | dio_00ja |
| POST_CLEAN_DIVERSE_KAS_2024_5M | spannungsrand_kippnaehe | 0.0085 | 0.5719 | 0.3551 | 0.2960 | 0.6686 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_16i6 |
| POST_CLEAN_DIVERSE_SYNTH_RAND_A | zentrum_stabil | 0.9312 | 0.7468 | 0.5987 | 0.1248 | 0.9066 | 0.2688 | 0.1947 | dio_mcm_episode_08lp0ua | dio_1fll |
| POST_CLEAN_DIVERSE_SYNTH_RAND_A | offene_variante | 0.0681 | 0.6632 | 0.4828 | 0.1946 | 0.7693 | 0.0000 | 1.0000 | dio_mcm_episode_14l8khu | dio_1v2w |
| POST_CLEAN_DIVERSE_SYNTH_RAND_A | spannungsrand_kippnaehe | 0.0007 | 0.5885 | 0.3400 | 0.2996 | 0.6825 | 0.0000 | 1.0000 | dio_mcm_episode_0r9ht2p | dio_11v0 |

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

Als naechstes sollte die synthetische Randwelt separat gegen ihre Rohweltmerkmale geprueft werden.
Ziel ist zu klaeren, warum eine als Randdominanz gedachte Welt nach rezeptorischer Aufnahme stark zentriert erscheint: echte Feldstabilisierung, zu starke Adaptation oder eine synthetische Weltform, die im MCM-Feld nicht als Randspannung ankommt.
