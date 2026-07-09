# Weltrelative Topologie-Matrix

Stand: 2026-06-21 17:17:03

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
| QUIET2024_R1 | 94 | zentrum_mit_rand_und_uebergang | 0.8085 | 0.1596 | 0.0319 | 0.2553 | 0.6413 | 0.3941 | 0.1954 | 0.8656 |
| QUIET2024_R2 | 94 | zentrum_mit_rand_und_uebergang | 0.8085 | 0.1596 | 0.0319 | 0.2553 | 0.6409 | 0.3944 | 0.1952 | 0.8653 |
| STRESS2024_R1 | 94 | zentrum_mit_rand_und_uebergang | 0.8404 | 0.1064 | 0.0532 | 0.2553 | 0.6422 | 0.3953 | 0.1937 | 0.8655 |
| STRESS2024_R2 | 94 | zentrum_mit_rand_und_uebergang | 0.8404 | 0.1064 | 0.0532 | 0.2553 | 0.6419 | 0.3956 | 0.1935 | 0.8652 |
| POS_EXP2023_R1 | 994 | zentrum_mit_rand_und_uebergang | 0.8249 | 0.1489 | 0.0262 | 0.2455 | 0.6440 | 0.3964 | 0.1930 | 0.8671 |
| POS_EXP2023_R2 | 994 | zentrum_mit_rand_und_uebergang | 0.8249 | 0.1489 | 0.0262 | 0.2465 | 0.6437 | 0.3968 | 0.1928 | 0.8668 |
| EXT_EXP2023_R1 | 994 | zentrum_mit_rand_und_uebergang | 0.8129 | 0.1469 | 0.0402 | 0.2505 | 0.6460 | 0.3995 | 0.1901 | 0.8688 |
| EXT_EXP2023_R2 | 994 | zentrum_mit_rand_und_uebergang | 0.8109 | 0.1489 | 0.0402 | 0.2505 | 0.6456 | 0.3999 | 0.1899 | 0.8685 |
| NEG_STRESS2023_R1 | 994 | zentrum_mit_rand_und_uebergang | 0.8410 | 0.1288 | 0.0302 | 0.2505 | 0.6445 | 0.3969 | 0.1912 | 0.8677 |
| NEG_STRESS2023_R2 | 994 | zentrum_mit_rand_und_uebergang | 0.8431 | 0.1268 | 0.0302 | 0.2505 | 0.6441 | 0.3972 | 0.1910 | 0.8674 |
| NEG_STRESS2024_R1 | 994 | zentrum_mit_rand_und_uebergang | 0.7958 | 0.1751 | 0.0292 | 0.2495 | 0.6418 | 0.3955 | 0.1952 | 0.8628 |
| NEG_STRESS2024_R2 | 994 | zentrum_mit_rand_und_uebergang | 0.7958 | 0.1751 | 0.0292 | 0.2495 | 0.6414 | 0.3959 | 0.1950 | 0.8624 |
| SIDEWAYS2024_R1 | 994 | zentrum_mit_rand_und_uebergang | 0.8159 | 0.1590 | 0.0252 | 0.2485 | 0.6426 | 0.3956 | 0.1941 | 0.8656 |
| SIDEWAYS2024_R2 | 994 | zentrum_mit_rand_und_uebergang | 0.8169 | 0.1579 | 0.0252 | 0.2485 | 0.6422 | 0.3960 | 0.1939 | 0.8653 |
| SIDEWAYS2026_R1 | 994 | zentrum_mit_rand_und_uebergang | 0.8219 | 0.1509 | 0.0272 | 0.2505 | 0.6437 | 0.3981 | 0.1924 | 0.8665 |
| SIDEWAYS2026_R2 | 994 | zentrum_mit_rand_und_uebergang | 0.8229 | 0.1499 | 0.0272 | 0.2505 | 0.6433 | 0.3984 | 0.1922 | 0.8661 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| QUIET2024_R1 | zentrum_stabil | 0.8085 | 0.6481 | 0.3991 | 0.1824 | 0.8794 | 0.3158 | 0.0789 | dio_mcm_episode_1t5bcxp | dio_1ltv |
| QUIET2024_R1 | offene_variante | 0.1596 | 0.6210 | 0.3811 | 0.2361 | 0.8291 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1gly |
| QUIET2024_R1 | spannungsrand_kippnaehe | 0.0319 | 0.5697 | 0.3332 | 0.3218 | 0.6970 | 0.0000 | 1.0000 | dio_mcm_episode_04q6913 | dio_1lx6 |
| QUIET2024_R2 | zentrum_stabil | 0.8085 | 0.6478 | 0.3994 | 0.1822 | 0.8791 | 0.3158 | 0.0789 | dio_mcm_episode_1t5bcxp | dio_1ltv |
| QUIET2024_R2 | offene_variante | 0.1596 | 0.6207 | 0.3814 | 0.2359 | 0.8288 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1gly |
| QUIET2024_R2 | spannungsrand_kippnaehe | 0.0319 | 0.5693 | 0.3335 | 0.3216 | 0.6967 | 0.0000 | 1.0000 | dio_mcm_episode_04q6913 | dio_1lx6 |
| STRESS2024_R1 | zentrum_stabil | 0.8404 | 0.6497 | 0.3984 | 0.1784 | 0.8839 | 0.3038 | 0.1139 | dio_mcm_episode_1t5bcxp | dio_1h1r |
| STRESS2024_R1 | offene_variante | 0.1064 | 0.6192 | 0.3930 | 0.2453 | 0.8012 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0oi5 |
| STRESS2024_R1 | spannungsrand_kippnaehe | 0.0532 | 0.5693 | 0.3504 | 0.3313 | 0.7042 | 0.0000 | 1.0000 | dio_mcm_episode_0y0oxs9 | dio_0c76 |
| STRESS2024_R2 | zentrum_stabil | 0.8404 | 0.6494 | 0.3987 | 0.1783 | 0.8836 | 0.3038 | 0.1139 | dio_mcm_episode_1t5bcxp | dio_1h1r |
| STRESS2024_R2 | offene_variante | 0.1064 | 0.6188 | 0.3933 | 0.2452 | 0.8009 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0oi5 |
| STRESS2024_R2 | spannungsrand_kippnaehe | 0.0532 | 0.5689 | 0.3507 | 0.3311 | 0.7039 | 0.0000 | 1.0000 | dio_mcm_episode_0y0oxs9 | dio_0c76 |
| POS_EXP2023_R1 | zentrum_stabil | 0.8249 | 0.6503 | 0.4007 | 0.1810 | 0.8796 | 0.3037 | 0.0915 | dio_mcm_episode_1t5bcxp | dio_0xw3 |
| POS_EXP2023_R1 | offene_variante | 0.1489 | 0.6194 | 0.3788 | 0.2391 | 0.8189 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0tva |
| POS_EXP2023_R1 | spannungsrand_kippnaehe | 0.0262 | 0.5870 | 0.3616 | 0.3086 | 0.7465 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_180s |
| POS_EXP2023_R2 | zentrum_stabil | 0.8249 | 0.6499 | 0.4011 | 0.1808 | 0.8793 | 0.3037 | 0.0915 | dio_mcm_episode_1t5bcxp | dio_0xw3 |
| POS_EXP2023_R2 | offene_variante | 0.1489 | 0.6190 | 0.3791 | 0.2389 | 0.8186 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0tva |
| POS_EXP2023_R2 | spannungsrand_kippnaehe | 0.0262 | 0.5866 | 0.3619 | 0.3084 | 0.7461 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_180s |
| EXT_EXP2023_R1 | zentrum_stabil | 0.8129 | 0.6537 | 0.4044 | 0.1754 | 0.8842 | 0.3082 | 0.0804 | dio_mcm_episode_1t5bcxp | dio_1f3b |
| EXT_EXP2023_R1 | offene_variante | 0.1469 | 0.6205 | 0.3841 | 0.2379 | 0.8179 | 0.0000 | 0.9863 | dio_mcm_episode_1t5bcxp | dio_1tyo |
| EXT_EXP2023_R1 | spannungsrand_kippnaehe | 0.0402 | 0.5841 | 0.3579 | 0.3114 | 0.7432 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_13aw |
| EXT_EXP2023_R2 | zentrum_stabil | 0.8109 | 0.6533 | 0.4049 | 0.1751 | 0.8840 | 0.3089 | 0.0782 | dio_mcm_episode_1t5bcxp | dio_1f3b |
| EXT_EXP2023_R2 | offene_variante | 0.1489 | 0.6201 | 0.3840 | 0.2374 | 0.8177 | 0.0000 | 0.9865 | dio_mcm_episode_1t5bcxp | dio_1tyo |
| EXT_EXP2023_R2 | spannungsrand_kippnaehe | 0.0402 | 0.5837 | 0.3582 | 0.3112 | 0.7429 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_13aw |
| NEG_STRESS2023_R1 | zentrum_stabil | 0.8410 | 0.6507 | 0.4005 | 0.1794 | 0.8810 | 0.2978 | 0.1100 | dio_mcm_episode_1t5bcxp | dio_03wz |
| NEG_STRESS2023_R1 | offene_variante | 0.1288 | 0.6198 | 0.3815 | 0.2390 | 0.8197 | 0.0000 | 0.9922 | dio_mcm_episode_1t5bcxp | dio_11vn |
| NEG_STRESS2023_R1 | spannungsrand_kippnaehe | 0.0302 | 0.5779 | 0.3620 | 0.3157 | 0.7036 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1sl6 |
| NEG_STRESS2023_R2 | zentrum_stabil | 0.8431 | 0.6503 | 0.4008 | 0.1793 | 0.8805 | 0.2971 | 0.1122 | dio_mcm_episode_1t5bcxp | dio_03wz |
| NEG_STRESS2023_R2 | offene_variante | 0.1268 | 0.6193 | 0.3815 | 0.2391 | 0.8192 | 0.0000 | 0.9921 | dio_mcm_episode_1t5bcxp | dio_11vn |
| NEG_STRESS2023_R2 | spannungsrand_kippnaehe | 0.0302 | 0.5776 | 0.3623 | 0.3155 | 0.7033 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1sl6 |
| NEG_STRESS2024_R1 | zentrum_stabil | 0.7958 | 0.6490 | 0.4000 | 0.1817 | 0.8790 | 0.3110 | 0.0619 | dio_mcm_episode_1t5bcxp | dio_1v9p |
| NEG_STRESS2024_R1 | offene_variante | 0.1751 | 0.6195 | 0.3816 | 0.2378 | 0.8145 | 0.0172 | 0.9828 | dio_mcm_episode_1t5bcxp | dio_1ijy |
| NEG_STRESS2024_R1 | spannungsrand_kippnaehe | 0.0292 | 0.5788 | 0.3575 | 0.3102 | 0.7085 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1thl |
| NEG_STRESS2024_R2 | zentrum_stabil | 0.7958 | 0.6486 | 0.4004 | 0.1814 | 0.8787 | 0.3110 | 0.0619 | dio_mcm_episode_1t5bcxp | dio_1v9p |
| NEG_STRESS2024_R2 | offene_variante | 0.1751 | 0.6191 | 0.3819 | 0.2376 | 0.8141 | 0.0172 | 0.9828 | dio_mcm_episode_1t5bcxp | dio_1ijy |
| NEG_STRESS2024_R2 | spannungsrand_kippnaehe | 0.0292 | 0.5784 | 0.3578 | 0.3100 | 0.7082 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_1thl |
| SIDEWAYS2024_R1 | zentrum_stabil | 0.8159 | 0.6489 | 0.3996 | 0.1820 | 0.8793 | 0.3070 | 0.0814 | dio_mcm_episode_1t5bcxp | dio_1lco |
| SIDEWAYS2024_R1 | offene_variante | 0.1590 | 0.6207 | 0.3814 | 0.2376 | 0.8202 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0nqi |
| SIDEWAYS2024_R1 | spannungsrand_kippnaehe | 0.0252 | 0.5778 | 0.3565 | 0.3144 | 0.7115 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0cpy |
| SIDEWAYS2024_R2 | zentrum_stabil | 0.8169 | 0.6484 | 0.3999 | 0.1818 | 0.8788 | 0.3067 | 0.0825 | dio_mcm_episode_1t5bcxp | dio_1lco |
| SIDEWAYS2024_R2 | offene_variante | 0.1579 | 0.6203 | 0.3818 | 0.2376 | 0.8198 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0nqi |
| SIDEWAYS2024_R2 | spannungsrand_kippnaehe | 0.0252 | 0.5774 | 0.3568 | 0.3142 | 0.7112 | 0.0000 | 1.0000 | dio_mcm_episode_1t5bcxp | dio_0cpy |
| SIDEWAYS2026_R1 | zentrum_stabil | 0.8219 | 0.6505 | 0.4027 | 0.1795 | 0.8811 | 0.3048 | 0.0881 | dio_mcm_episode_1t5bcxp | dio_1f1f |
| SIDEWAYS2026_R1 | offene_variante | 0.1509 | 0.6179 | 0.3799 | 0.2408 | 0.8135 | 0.0000 | 1.0000 | dio_mcm_episode_0y50lf3 | dio_0exb |
| SIDEWAYS2026_R1 | spannungsrand_kippnaehe | 0.0272 | 0.5800 | 0.3582 | 0.3141 | 0.7190 | 0.0000 | 1.0000 | dio_mcm_episode_0y50lf3 | dio_15bw |
| SIDEWAYS2026_R2 | zentrum_stabil | 0.8229 | 0.6502 | 0.4031 | 0.1794 | 0.8808 | 0.3044 | 0.0905 | dio_mcm_episode_1t5bcxp | dio_1f1f |
| SIDEWAYS2026_R2 | offene_variante | 0.1499 | 0.6174 | 0.3799 | 0.2407 | 0.8126 | 0.0000 | 0.9933 | dio_mcm_episode_0y50lf3 | dio_0exb |
| SIDEWAYS2026_R2 | spannungsrand_kippnaehe | 0.0272 | 0.5796 | 0.3585 | 0.3139 | 0.7186 | 0.0000 | 1.0000 | dio_mcm_episode_0y50lf3 | dio_15bw |

## Lesart

Zentrumsnahe Welten: 16
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
