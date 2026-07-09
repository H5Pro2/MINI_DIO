# Weltrelative Topologie-Matrix

Stand: 2026-06-22 12:34:11

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
| SIDEWAYS_2024_5M_10K | 9994 | gemischte_rollenordnung | 0.7776 | 0.2174 | 0.0050 | 0.2502 | 0.7041 | 0.5369 | 0.1533 | 0.8395 |
| NEGATIVE_STRESS_2024_5M_10K | 9994 | stark_zentriert_wenig_rand | 0.8029 | 0.1907 | 0.0064 | 0.2495 | 0.7052 | 0.5375 | 0.1524 | 0.8421 |
| POSITIVE_EXPANSION_2023_5M_10K | 9994 | gemischte_rollenordnung | 0.7915 | 0.2003 | 0.0082 | 0.2489 | 0.7049 | 0.5367 | 0.1527 | 0.8415 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SIDEWAYS_2024_5M_10K | zentrum_stabil | 0.7776 | 0.7143 | 0.5490 | 0.1423 | 0.8577 | 0.3216 | 0.0954 | dio_mcm_episode_0b7nep9 | dio_104t |
| SIDEWAYS_2024_5M_10K | offene_variante | 0.2174 | 0.6706 | 0.4975 | 0.1892 | 0.7785 | 0.0009 | 0.7860 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SIDEWAYS_2024_5M_10K | spannungsrand_kippnaehe | 0.0050 | 0.5718 | 0.3588 | 0.2981 | 0.6588 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_15yz |
| NEGATIVE_STRESS_2024_5M_10K | zentrum_stabil | 0.8029 | 0.7152 | 0.5499 | 0.1419 | 0.8591 | 0.3113 | 0.1016 | dio_mcm_episode_0b7nep9 | dio_104t |
| NEGATIVE_STRESS_2024_5M_10K | offene_variante | 0.1907 | 0.6673 | 0.4913 | 0.1916 | 0.7769 | 0.0005 | 0.8499 | dio_mcm_episode_0b7nep9 | dio_0m9z |
| NEGATIVE_STRESS_2024_5M_10K | spannungsrand_kippnaehe | 0.0064 | 0.5706 | 0.3560 | 0.2987 | 0.6590 | 0.0000 | 1.0000 | dio_mcm_episode_0b7nep9 | dio_0ku7 |
| POSITIVE_EXPANSION_2023_5M_10K | zentrum_stabil | 0.7915 | 0.7151 | 0.5489 | 0.1418 | 0.8594 | 0.3153 | 0.0982 | dio_mcm_episode_0e7qvj1 | dio_104t |
| POSITIVE_EXPANSION_2023_5M_10K | offene_variante | 0.2003 | 0.6700 | 0.4958 | 0.1900 | 0.7781 | 0.0025 | 0.8192 | dio_mcm_episode_0b7nep9 | dio_0m9z |
| POSITIVE_EXPANSION_2023_5M_10K | spannungsrand_kippnaehe | 0.0082 | 0.5720 | 0.3625 | 0.2995 | 0.6596 | 0.0000 | 1.0000 | dio_mcm_episode_0b7nep9 | dio_17qo |

## Lesart

Zentrumsnahe Welten: 1
Gemischte Rollenordnung: 2
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
