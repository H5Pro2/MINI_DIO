# Weltrelative Topologie-Matrix

Stand: 2026-06-21 21:28:51

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
| BTC2024_5M_2K | 1994 | stark_zentriert_wenig_rand | 0.8220 | 0.1650 | 0.0130 | 0.2503 | 0.6939 | 0.5118 | 0.1588 | 0.8437 |
| SOL2024_5M_2K | 1994 | gemischte_rollenordnung | 0.7859 | 0.2001 | 0.0140 | 0.2497 | 0.6916 | 0.5094 | 0.1612 | 0.8398 |
| KAS2024_5M_2K | 1994 | stark_zentriert_wenig_rand | 0.8084 | 0.1795 | 0.0120 | 0.2503 | 0.6922 | 0.5095 | 0.1602 | 0.8423 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC2024_5M_2K | zentrum_stabil | 0.8220 | 0.7042 | 0.5251 | 0.1475 | 0.8590 | 0.3045 | 0.1232 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC2024_5M_2K | offene_variante | 0.1650 | 0.6524 | 0.4586 | 0.2032 | 0.7792 | 0.0000 | 0.8237 | dio_mcm_episode_0e7qvj1 | dio_0jkk |
| BTC2024_5M_2K | spannungsrand_kippnaehe | 0.0130 | 0.5717 | 0.3471 | 0.3105 | 0.6940 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_14e7 |
| SOL2024_5M_2K | zentrum_stabil | 0.7859 | 0.7027 | 0.5231 | 0.1485 | 0.8578 | 0.3184 | 0.1066 | dio_mcm_episode_0e7qvj1 | dio_104t |
| SOL2024_5M_2K | offene_variante | 0.2001 | 0.6564 | 0.4668 | 0.2007 | 0.7794 | 0.0000 | 0.7619 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| SOL2024_5M_2K | spannungsrand_kippnaehe | 0.0140 | 0.5717 | 0.3498 | 0.3075 | 0.6915 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_11nu |
| KAS2024_5M_2K | zentrum_stabil | 0.8084 | 0.7026 | 0.5225 | 0.1484 | 0.8582 | 0.3096 | 0.1148 | dio_mcm_episode_0e7qvj1 | dio_104t |
| KAS2024_5M_2K | offene_variante | 0.1795 | 0.6539 | 0.4613 | 0.2031 | 0.7803 | 0.0000 | 0.8101 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| KAS2024_5M_2K | spannungsrand_kippnaehe | 0.0120 | 0.5713 | 0.3480 | 0.3079 | 0.6949 | 0.0000 | 1.0000 | dio_mcm_episode_1jx2k4i | dio_18i0 |

## Lesart

Zentrumsnahe Welten: 2
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
