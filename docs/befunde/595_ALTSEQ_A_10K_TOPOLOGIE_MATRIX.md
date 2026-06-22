# Weltrelative Topologie-Matrix

Stand: 2026-06-21 23:36:08

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
| ALTSEQ2023_A_10K | 9994 | stark_zentriert_wenig_rand | 0.8311 | 0.1557 | 0.0132 | 0.2486 | 0.7043 | 0.5351 | 0.1569 | 0.8446 |
| ALTSEQ2024_A_10K | 9994 | stark_zentriert_wenig_rand | 0.8249 | 0.1667 | 0.0084 | 0.2499 | 0.7034 | 0.5349 | 0.1572 | 0.8440 |
| ALTSEQ2025_A_10K | 9994 | stark_zentriert_wenig_rand | 0.8155 | 0.1757 | 0.0088 | 0.2496 | 0.7032 | 0.5354 | 0.1574 | 0.8426 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ALTSEQ2023_A_10K | zentrum_stabil | 0.8311 | 0.7139 | 0.5472 | 0.1466 | 0.8596 | 0.3004 | 0.1306 | dio_mcm_episode_0e7qvj1 | dio_104t |
| ALTSEQ2023_A_10K | offene_variante | 0.1557 | 0.6643 | 0.4855 | 0.1985 | 0.7779 | 0.0026 | 0.8239 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| ALTSEQ2023_A_10K | spannungsrand_kippnaehe | 0.0132 | 0.5729 | 0.3548 | 0.3132 | 0.6906 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_1sp4 |
| ALTSEQ2024_A_10K | zentrum_stabil | 0.8249 | 0.7124 | 0.5464 | 0.1474 | 0.8584 | 0.3030 | 0.1281 | dio_mcm_episode_0e7qvj1 | dio_104t |
| ALTSEQ2024_A_10K | offene_variante | 0.1667 | 0.6650 | 0.4876 | 0.1983 | 0.7794 | 0.0006 | 0.8157 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| ALTSEQ2024_A_10K | spannungsrand_kippnaehe | 0.0084 | 0.5758 | 0.3501 | 0.3059 | 0.7035 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_00hc |
| ALTSEQ2025_A_10K | zentrum_stabil | 0.8155 | 0.7127 | 0.5472 | 0.1470 | 0.8578 | 0.3064 | 0.1200 | dio_mcm_episode_0e7qvj1 | dio_104t |
| ALTSEQ2025_A_10K | offene_variante | 0.1757 | 0.6660 | 0.4897 | 0.1977 | 0.7794 | 0.0011 | 0.8161 | dio_mcm_episode_0e7qvj1 | dio_00ja |
| ALTSEQ2025_A_10K | spannungsrand_kippnaehe | 0.0088 | 0.5707 | 0.3486 | 0.3138 | 0.6934 | 0.0000 | 1.0000 | dio_mcm_episode_0e7qvj1 | dio_04u3 |

## Lesart

Zentrumsnahe Welten: 3
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
