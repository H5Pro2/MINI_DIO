# Weltrelative Topologie-Matrix

Stand: 2026-06-21 21:13:17

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
| BTC2025_5M_QUIET_4K | 3994 | stark_zentriert_wenig_rand | 0.8415 | 0.1480 | 0.0105 | 0.2501 | 0.7000 | 0.5232 | 0.1558 | 0.8476 |
| BTC2025_5M_STRESS_4K | 3994 | stark_zentriert_wenig_rand | 0.8247 | 0.1612 | 0.0140 | 0.2501 | 0.6982 | 0.5221 | 0.1577 | 0.8443 |
| SOL2025_5M_QUIET_4K | 3994 | gemischte_rollenordnung | 0.7894 | 0.1990 | 0.0115 | 0.2499 | 0.6970 | 0.5214 | 0.1591 | 0.8409 |
| SOL2025_5M_STRESS_4K | 3994 | stark_zentriert_wenig_rand | 0.8215 | 0.1650 | 0.0135 | 0.2499 | 0.6984 | 0.5229 | 0.1579 | 0.8439 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC2025_5M_QUIET_4K | zentrum_stabil | 0.8415 | 0.7086 | 0.5344 | 0.1464 | 0.8608 | 0.2972 | 0.1452 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC2025_5M_QUIET_4K | offene_variante | 0.1480 | 0.6596 | 0.4714 | 0.1983 | 0.7824 | 0.0000 | 0.7936 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| BTC2025_5M_QUIET_4K | spannungsrand_kippnaehe | 0.0105 | 0.5783 | 0.3506 | 0.3060 | 0.7104 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1ghk |
| BTC2025_5M_STRESS_4K | zentrum_stabil | 0.8247 | 0.7083 | 0.5351 | 0.1468 | 0.8599 | 0.3030 | 0.1263 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC2025_5M_STRESS_4K | offene_variante | 0.1612 | 0.6577 | 0.4704 | 0.2005 | 0.7783 | 0.0016 | 0.8183 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| BTC2025_5M_STRESS_4K | spannungsrand_kippnaehe | 0.0140 | 0.5714 | 0.3494 | 0.3096 | 0.6908 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1a0q |
| SOL2025_5M_QUIET_4K | zentrum_stabil | 0.7894 | 0.7076 | 0.5346 | 0.1472 | 0.8581 | 0.3165 | 0.1104 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SOL2025_5M_QUIET_4K | offene_variante | 0.1990 | 0.6621 | 0.4790 | 0.1973 | 0.7809 | 0.0013 | 0.7610 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SOL2025_5M_QUIET_4K | spannungsrand_kippnaehe | 0.0115 | 0.5737 | 0.3517 | 0.3081 | 0.7032 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |
| SOL2025_5M_STRESS_4K | zentrum_stabil | 0.8215 | 0.7084 | 0.5356 | 0.1468 | 0.8594 | 0.3039 | 0.1231 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SOL2025_5M_STRESS_4K | offene_variante | 0.1650 | 0.6593 | 0.4732 | 0.2003 | 0.7798 | 0.0030 | 0.8209 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SOL2025_5M_STRESS_4K | spannungsrand_kippnaehe | 0.0135 | 0.5707 | 0.3527 | 0.3098 | 0.6800 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_18i0 |

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
