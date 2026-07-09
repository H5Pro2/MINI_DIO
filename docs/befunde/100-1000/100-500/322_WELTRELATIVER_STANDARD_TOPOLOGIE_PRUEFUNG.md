# Weltrelative Topologie-Matrix

Stand: 2026-06-19 21:37:56

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
| SOL_2024_5M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8255 | 0.1389 | 0.0356 | 0.2503 | 0.6434 | 0.3995 | 0.1931 | 0.8652 |
| SOL_2024_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8114 | 0.1605 | 0.0281 | 0.2503 | 0.6438 | 0.3988 | 0.1915 | 0.8658 |
| BTC_2024_5M_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8335 | 0.1384 | 0.0281 | 0.2503 | 0.6452 | 0.4000 | 0.1890 | 0.8673 |
| BTC_2024_1H_2K | 1994 | zentrum_mit_rand_und_uebergang | 0.8325 | 0.1334 | 0.0341 | 0.2497 | 0.6467 | 0.4016 | 0.1875 | 0.8684 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOL_2024_5M_2K | zentrum_stabil | 0.8255 | 0.6502 | 0.4043 | 0.1805 | 0.8800 | 0.3032 | 0.0936 | dio_mcm_episode_1t5bcxp | dio_0y8z |
| SOL_2024_5M_2K | offene_variante | 0.1389 | 0.6186 | 0.3812 | 0.2384 | 0.8144 | 0.0000 | 0.9892 | dio_mcm_episode_1t5bcxp | dio_1kpm |
| SOL_2024_5M_2K | spannungsrand_kippnaehe | 0.0356 | 0.5807 | 0.3607 | 0.3101 | 0.7204 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_04dy |
| SOL_2024_1H_2K | zentrum_stabil | 0.8114 | 0.6512 | 0.4041 | 0.1779 | 0.8811 | 0.3084 | 0.0773 | dio_mcm_episode_1t5bcxp | dio_0xvr |
| SOL_2024_1H_2K | offene_variante | 0.1605 | 0.6187 | 0.3809 | 0.2378 | 0.8174 | 0.0000 | 0.9938 | dio_mcm_episode_1t5bcxp | dio_0un2 |
| SOL_2024_1H_2K | spannungsrand_kippnaehe | 0.0281 | 0.5738 | 0.3490 | 0.3188 | 0.7017 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_12gk |
| BTC_2024_5M_2K | zentrum_stabil | 0.8335 | 0.6519 | 0.4050 | 0.1763 | 0.8811 | 0.3002 | 0.1023 | dio_mcm_episode_1t5bcxp | dio_1oem |
| BTC_2024_5M_2K | offene_variante | 0.1384 | 0.6181 | 0.3792 | 0.2393 | 0.8154 | 0.0000 | 0.9891 | dio_mcm_episode_1t5bcxp | dio_0nvl |
| BTC_2024_5M_2K | spannungsrand_kippnaehe | 0.0281 | 0.5768 | 0.3547 | 0.3183 | 0.7154 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1q4y |
| BTC_2024_1H_2K | zentrum_stabil | 0.8325 | 0.6541 | 0.4064 | 0.1735 | 0.8838 | 0.3000 | 0.0994 | dio_mcm_episode_1t5bcxp | dio_0zn5 |
| BTC_2024_1H_2K | offene_variante | 0.1334 | 0.6174 | 0.3826 | 0.2426 | 0.8099 | 0.0038 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0hwx |
| BTC_2024_1H_2K | spannungsrand_kippnaehe | 0.0341 | 0.5810 | 0.3596 | 0.3121 | 0.7210 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1ema |

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
