# Weltrelative Topologie-Matrix

Stand: 2026-06-21 21:21:02

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
| MOD_POS_10K | 9994 | stark_zentriert_wenig_rand | 0.8036 | 0.1849 | 0.0115 | 0.2497 | 0.7027 | 0.5348 | 0.1577 | 0.8415 |
| POS_RECOVERY_10K | 9994 | stark_zentriert_wenig_rand | 0.8171 | 0.1730 | 0.0099 | 0.2498 | 0.7033 | 0.5352 | 0.1573 | 0.8431 |
| STRESS_10K | 9994 | stark_zentriert_wenig_rand | 0.8212 | 0.1686 | 0.0102 | 0.2495 | 0.7031 | 0.5348 | 0.1574 | 0.8432 |
| LATE_NEG_10K | 9994 | stark_zentriert_wenig_rand | 0.8265 | 0.1631 | 0.0104 | 0.2492 | 0.7045 | 0.5367 | 0.1561 | 0.8445 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| MOD_POS_10K | zentrum_stabil | 0.8036 | 0.7124 | 0.5466 | 0.1467 | 0.8578 | 0.3109 | 0.1142 | dio_mcm_episode_0e7qvj1 | dio_104t |
| MOD_POS_10K | offene_variante | 0.1849 | 0.6681 | 0.4945 | 0.1961 | 0.7794 | 0.0011 | 0.7944 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| MOD_POS_10K | spannungsrand_kippnaehe | 0.0115 | 0.5778 | 0.3609 | 0.3050 | 0.6970 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_05cl |
| POS_RECOVERY_10K | zentrum_stabil | 0.8171 | 0.7126 | 0.5466 | 0.1470 | 0.8585 | 0.3057 | 0.1231 | dio_mcm_episode_0e7qvj1 | dio_104t |
| POS_RECOVERY_10K | offene_variante | 0.1730 | 0.6667 | 0.4915 | 0.1972 | 0.7787 | 0.0017 | 0.8068 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| POS_RECOVERY_10K | spannungsrand_kippnaehe | 0.0099 | 0.5758 | 0.3576 | 0.3081 | 0.6959 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_04u3 |
| STRESS_10K | zentrum_stabil | 0.8212 | 0.7126 | 0.5468 | 0.1470 | 0.8584 | 0.3045 | 0.1222 | dio_mcm_episode_0e7qvj1 | dio_104t |
| STRESS_10K | offene_variante | 0.1686 | 0.6646 | 0.4877 | 0.1987 | 0.7787 | 0.0000 | 0.8273 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| STRESS_10K | spannungsrand_kippnaehe | 0.0102 | 0.5710 | 0.3523 | 0.3103 | 0.6847 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_05cl |
| LATE_NEG_10K | zentrum_stabil | 0.8265 | 0.7138 | 0.5483 | 0.1460 | 0.8593 | 0.3025 | 0.1237 | dio_mcm_episode_0e7qvj1 | dio_104t |
| LATE_NEG_10K | offene_variante | 0.1631 | 0.6658 | 0.4893 | 0.1978 | 0.7787 | 0.0000 | 0.8423 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| LATE_NEG_10K | spannungsrand_kippnaehe | 0.0104 | 0.5781 | 0.3599 | 0.3053 | 0.6982 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |

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
