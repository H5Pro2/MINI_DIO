# Auditive Regulation - Diagnose

Stand: 2026-06-19 05:39:13

## Zweck

Diese Diagnose liest die Marktenergie als passive Hoerachse.
Sie prueft, ob MINI_DIO zwischen Hinhoeren, Rauschenfiltern, Reizabklingen, genauerem Anhoeren, Alarm, Hintergrund und Beruhigung unterscheiden kann.

Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.

Hierarchie der Pruefung:

1. Grundfrage: Wie reguliert ein MCM-Feld auditive Weltenergie, ohne sie direkt ins Handeln zu uebersetzen?
2. Unterpruefung: Tonstaerke, Tonwechsel, Fokus, Alarm, Hintergrund, Beruhigung und Nachton je Welt lesen.
3. Folgeschritt: Pruefen, welche Hoerzustande harmonische Rekopplung beguenstigen oder Feldlast begleiten.

## Einzelwerte

| Welt | Gruppe | Rolle | dominanter Hoerzustand | Ton avg | Ton p95 | Fokus | Alarm | Beruhigung | Hintergrund | Nachton | Rekopplung | Feldlast | Memorylast |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SOL_2024_5M | referenz | reiz_aktiv_rekoppelnd | rauschen_filtern | 0.004263 | 0.009152 | 0.4572 | 0.2178 | 0.2352 | 0.4543 | 0.1209 | 0.622776 | 0.0527 | 0.0747 |
| SOL_2025_5M | referenz | reiz_aktiv_rekoppelnd | rauschen_filtern | 0.002208 | 0.004948 | 0.4570 | 0.2177 | 0.2360 | 0.4548 | 0.1221 | 0.636504 | 0.0140 | 0.0276 |
| STRESS_2023_TEST4 | stress | last_memory_bindend | hintergrund_hoeren | 0.010587 | 0.024652 | 0.2607 | 0.1224 | 0.2210 | 0.5863 | 0.0440 | 0.596927 | 0.2660 | 0.2447 |
| STRESS_2024_REAL | stress | uebergang_bindend | rauschen_filtern | 0.010384 | 0.024700 | 0.4535 | 0.2493 | 0.2075 | 0.4503 | 0.1352 | 0.601652 | 0.2340 | 0.2447 |
| STRESS_2025_STRESS | stress | last_memory_bindend | rauschen_filtern | 0.009948 | 0.031973 | 0.3897 | 0.1889 | 0.2399 | 0.5019 | 0.0790 | 0.594327 | 0.2872 | 0.2234 |
| SOL_2024_1H | vergleich | last_memory_bindend | rauschen_filtern | 0.011785 | 0.028318 | 0.4440 | 0.2067 | 0.2438 | 0.4656 | 0.1136 | 0.587027 | 0.3159 | 0.3225 |
| SOL_2024_30M | vergleich | uebergang_bindend | rauschen_filtern | 0.007875 | 0.017576 | 0.4447 | 0.2056 | 0.2534 | 0.4678 | 0.1144 | 0.600205 | 0.1830 | 0.2212 |
| SOL_2025_1H | vergleich | last_memory_bindend | rauschen_filtern | 0.011138 | 0.027357 | 0.4426 | 0.2081 | 0.2447 | 0.4669 | 0.1154 | 0.589067 | 0.2944 | 0.2964 |
| SOL_2025_30M | vergleich | uebergang_bindend | rauschen_filtern | 0.008132 | 0.021160 | 0.4397 | 0.2013 | 0.2462 | 0.4689 | 0.1089 | 0.600912 | 0.2016 | 0.2177 |

## Hoerzustandsanteile

| Welt | Hinhoeren | genauer | Alarm | Hintergrund | Beruhigung | Rauschen filtern | Reiz abklingen |
|---|---:|---:|---:|---:|---:|---:|---:|
| SOL_2024_5M | 0.1371 | 0.1486 | 0.0905 | 0.2121 | 0.0565 | 0.3342 | 0.0210 |
| SOL_2025_5M | 0.1431 | 0.1466 | 0.0895 | 0.2251 | 0.0570 | 0.3207 | 0.0180 |
| STRESS_2023_TEST4 | 0.0505 | 0.0707 | 0.0404 | 0.5152 | 0.0404 | 0.2828 | 0.0000 |
| STRESS_2024_REAL | 0.1111 | 0.1212 | 0.1414 | 0.2424 | 0.0202 | 0.3030 | 0.0606 |
| STRESS_2025_STRESS | 0.0808 | 0.0808 | 0.0808 | 0.2929 | 0.0202 | 0.3939 | 0.0505 |
| SOL_2024_1H | 0.1481 | 0.1286 | 0.0835 | 0.2226 | 0.0610 | 0.3337 | 0.0225 |
| SOL_2024_30M | 0.1306 | 0.1386 | 0.0785 | 0.2351 | 0.0630 | 0.3367 | 0.0175 |
| SOL_2025_1H | 0.1381 | 0.1391 | 0.0790 | 0.2641 | 0.0450 | 0.3072 | 0.0275 |
| SOL_2025_30M | 0.1451 | 0.1296 | 0.0745 | 0.2156 | 0.0605 | 0.3552 | 0.0195 |

## Lesart

- `hinhoeren`: Ton wirkt relevant genug, um Aufmerksamkeit zu bekommen.
- `genauer_anhoeren`: Tonwechsel oder Fokusspur braucht feinere Betrachtung.
- `alarm_hoeren`: starke relative Tonveraenderung oder Lautheitsdruck.
- `hintergrund_hoeren`: Ton bleibt als Weltgrund vorhanden, ohne Dominanz.
- `beruhigung_hoeren`: gleichmaessiger Ton wirkt potenziell rekoppelnd.
- `rauschen_filtern`: Tonanteil wird als nicht strukturtragend gedaempft.
- `reiz_abklingen_lassen`: gehoerter Reiz darf auslaufen, ohne weiter Feldlast zu werden.

## Vorlaeufiger Befund

Auditive Regulation sollte als eigene Sinnesregulation gelesen werden.
Tonenergie darf das MCM-Feld stimulieren, aber nicht jede Tonspur darf gleich stark Bedeutung erzeugen.

Eine organische Hoerachse kann erklaeren, warum eine Welt aktiv bleibt, ohne sofort zu binden:
MINI_DIO kann hinhoeren, genauer hinhoeren, Hintergrund halten, Rauschen filtern oder Reizwirkung abklingen lassen.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Dort wird geprueft, welche Hoerzustande bei SOL 5m gegen SOL 30m/1h und Stresssegmente dominieren.
