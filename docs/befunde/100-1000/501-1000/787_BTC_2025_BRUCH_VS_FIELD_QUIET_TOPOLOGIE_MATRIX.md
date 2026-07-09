# Weltrelative Topologie-Matrix

Stand: 2026-06-23 09:06:26

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
| BTC_BRUCH | 1994 | stark_zentriert_wenig_rand | 0.8059 | 0.1846 | 0.0095 | 0.2503 | 0.6949 | 0.5126 | 0.1542 | 0.8420 |
| BTC_FELDRUHE | 1994 | stark_zentriert_wenig_rand | 0.8300 | 0.1655 | 0.0045 | 0.2503 | 0.6969 | 0.5132 | 0.1514 | 0.8472 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTC_BRUCH | zentrum_stabil | 0.8059 | 0.7051 | 0.5253 | 0.1432 | 0.8593 | 0.3099 | 0.1151 | dio_mcm_episode_1joiyc3 | dio_104t |
| BTC_BRUCH | offene_variante | 0.1846 | 0.6565 | 0.4651 | 0.1949 | 0.7757 | 0.0027 | 0.8016 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| BTC_BRUCH | spannungsrand_kippnaehe | 0.0095 | 0.5709 | 0.3551 | 0.2958 | 0.6596 | 0.0000 | 1.0000 | dio_mcm_episode_1joiyc3 | dio_05cl |
| BTC_FELDRUHE | zentrum_stabil | 0.8300 | 0.7056 | 0.5242 | 0.1422 | 0.8611 | 0.3015 | 0.1353 | dio_mcm_episode_0e7qvj1 | dio_104t |
| BTC_FELDRUHE | offene_variante | 0.1655 | 0.6569 | 0.4624 | 0.1939 | 0.7826 | 0.0000 | 0.8061 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| BTC_FELDRUHE | spannungsrand_kippnaehe | 0.0045 | 0.5711 | 0.3486 | 0.2989 | 0.6754 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_0ku7 |

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
