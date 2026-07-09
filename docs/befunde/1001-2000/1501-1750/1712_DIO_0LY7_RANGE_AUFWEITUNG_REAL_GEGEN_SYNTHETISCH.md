# 1712 - dio_0ly7 Range-Aufweitung real gegen synthetisch

Stand: 2026-07-07 22:16:27

## Zweck

Diese Diagnose prueft, ob Range-Aufweitung allein die Umkehr von `dio_0ly7` erklaert.
Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.

## Hierarchie

1. Grundfrage: Kippt `dio_0ly7` wegen Range-Aufweitung?
2. Unterpruefung: Reale Range-Aufweitung gegen synthetische Range-Aufweitung vergleichen.
3. Folgeschritt: Falls Range allein nicht reicht, Kombinationsursache lesen.

## Vergleich

| Quelle | Welt | Vorkommen | Delta Hoeren | Delta Spannung | Delta Range | Lesung |
|---|---|---:|---:|---:|---:|---|
| real_2023 | SOL_2023_NEG_STRESS_10K | 34 | -0.043620 | -0.042947 | -0.031533 | entlastung_ohne_range_aufweitung |
| real_2023 | SOL_2023_POS_EXPANSION_10K | 43 | -0.043135 | -0.042417 | -0.020025 | entlastung_ohne_range_aufweitung |
| real_2023 | SOL_2023_MOD_NEG_10K | 22 | -0.053593 | -0.050657 | -0.027096 | entlastung_ohne_range_aufweitung |
| real_2023 | SOL_2023_EXT_EXPANSION_10K | 30 | -0.042470 | -0.040997 | -0.036567 | entlastung_ohne_range_aufweitung |
| real_2024 | BTC_2024_5M_10K | 45 | -0.057640 | -0.053699 | -0.015499 | entlastung_ohne_range_aufweitung |
| real_2024 | DOGE_2024_5M_10K | 46 | -0.047111 | -0.045211 | -0.016187 | entlastung_ohne_range_aufweitung |
| real_2024 | XRP_2024_5M_10K | 44 | -0.050795 | -0.048094 | -0.021973 | entlastung_ohne_range_aufweitung |
| real_2024 | PAXG_2024_5M_10K | 42 | -0.044448 | -0.047162 | 0.002834 | range_aufweitung_aber_entlastung |
| real_2025 | BTC_2025_5M_10K | 49 | -0.062321 | -0.057225 | -0.013308 | entlastung_ohne_range_aufweitung |
| real_2025 | DOGE_2025_5M_10K | 47 | -0.051200 | -0.048679 | -0.018922 | entlastung_ohne_range_aufweitung |
| real_2025 | XRP_2025_5M_10K | 48 | -0.054435 | -0.051835 | -0.032750 | entlastung_ohne_range_aufweitung |
| real_2025 | PAXG_2025_5M_10K | 36 | -0.032069 | -0.036574 | 0.002718 | range_aufweitung_aber_entlastung |
| synthetic_core | SYN_RAND_DOMINANZ_A | 58 | 0.012586 | 0.008914 | 0.164518 | lastanstieg_mit_range_aufweitung |
| synthetic_core | SYN_BRUCH_RAND_A | 76 | 0.017137 | 0.013788 | 0.046207 | lastanstieg_mit_range_aufweitung |
| synthetic_core | SYN_REKOPPLUNG_VOR_RAND | 59 | 0.018434 | 0.014969 | 0.043547 | lastanstieg_mit_range_aufweitung |
| synthetic_core | SYN_STARK_PERMUTIERT | 73 | 0.016203 | 0.013390 | 0.039690 | lastanstieg_mit_range_aufweitung |
| synthetic_extra | SYN_RAND_DOMINANZ_B | 58 | 0.012586 | 0.008914 | 0.164518 | lastanstieg_mit_range_aufweitung |
| synthetic_extra | SYN_BRUCH_RAND_B | 76 | 0.017137 | 0.013788 | 0.046207 | lastanstieg_mit_range_aufweitung |
| synthetic_extra | SYN_SEQ_ORIGINAL | 75 | 0.017047 | 0.013703 | 0.047530 | lastanstieg_mit_range_aufweitung |
| synthetic_extra | SYN_SEQ_PERMUTIERT | 76 | 0.016553 | 0.013182 | 0.044203 | lastanstieg_mit_range_aufweitung |
| synthetic_extra | SYN_SEQ_ZUFALLSNAH | 66 | 0.014014 | 0.011086 | 0.037506 | lastanstieg_mit_range_aufweitung |
| synthetic_extra | SYN_REKOPPLUNG_LANG_VOR_RAND | 66 | 0.018230 | 0.014781 | 0.043485 | lastanstieg_mit_range_aufweitung |

## Kurzbefund

- Reale Welten mit Range-Aufweitung: 2
- Synthetische Welten mit Range-Aufweitung: 10

Lesung:

```text
Range-Aufweitung allein reicht nicht aus.
In realen PAXG-Welten bleibt dio_0ly7 trotz leichter Range-Aufweitung entlastend.
In synthetischen Welten koppelt Range-Aufweitung mit Hoer- und Spannungsanstieg.
Der Bruch ist deshalb eine Kombinationswirkung, nicht nur ein Range-Effekt.
```

## Grenze

```text
Das ist eine passive Felddiagnose.
Keine Handlungsregel.
Keine Aussage ueber Absicht.
```
