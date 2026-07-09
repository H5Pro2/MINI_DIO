# Weltuebergreifende Informationsaufnahme: Diagnose

Stand: 2026-06-19 21:19:49

## Zweck

Diese Diagnose prueft, ob MINI_DIO Welten ueber Sehen, Hoeren und MCM-Feldwirkung vergleichbar aufnimmt.
Sie liest nicht die MCM-Topologie selbst, sondern den Schritt davor: Rohwelt zu Sinneswerten.

Wichtig: Das ist keine Handlung, kein Gate und keine Runtime-Regel.

## Hierarchie

1. Allgemeine Grundfrage: Ist die Informationsaufnahme ueber Welten einheitlich genug?
2. Konkrete Unterpruefung: Welche Sinnesachsen uebersteuern, flachen ab oder bleiben tragbar?
3. Folgeschritt: Wenn die Aufnahme nicht einheitlich ist, braucht MINI_DIO einen weltrelativen Wahrnehmungsadapter.

## Weltuebersicht

| Welt | Zustand | Kerzen | Return p95 | Range p95 | Volume p95 |
|---|---|---:|---:|---:|---:|
| SOL_2023_5M_REAL1 | reiz_uebersteuert | 1000 | 0.0083 | 0.0138 | 129946.43 |
| SOL_2024_5M_REAL1 | reiz_uebersteuert | 1000 | 0.0074 | 0.0125 | 74919.88 |
| SOL_2024_1H_2K | reiz_uebersteuert | 2000 | 0.0242 | 0.0399 | 709571.33 |
| BTC_2024_5M_2K | reiz_uebersteuert | 2000 | 0.0033 | 0.0049 | 420.75 |
| BTC_2024_1H_2K | reiz_uebersteuert | 2000 | 0.0132 | 0.0211 | 5246.11 |
| SOL_2023_NEG_STRESS | reiz_uebersteuert | 1000 | 0.0044 | 0.0069 | 51456.18 |

## Sinnesachsen

| Welt | Achse | Zustand | p95 abs | Saettigung | Flachheit |
|---|---|---|---:|---:|---:|
| SOL_2023_5M_REAL1 | sehen.form_flow | tragbar | 0.8607 | 0.0430 | 0.0910 |
| SOL_2023_5M_REAL1 | sehen.form_stability | uebersteuert | 1.0000 | 0.3170 | 0.3370 |
| SOL_2023_5M_REAL1 | sehen.form_change | nahe_saettigung | 1.0000 | 0.0580 | 0.0590 |
| SOL_2023_5M_REAL1 | hoeren.energy_tone | tragbar | 0.5593 | 0.0110 | 0.0750 |
| SOL_2023_5M_REAL1 | hoeren.energy_shift | nahe_saettigung | 1.0000 | 0.0620 | 0.2120 |
| SOL_2023_5M_REAL1 | mcm_feldwirkung.mcm_coherence | tragbar | 0.7092 | 0.0000 | 0.0120 |
| SOL_2023_5M_REAL1 | mcm_feldwirkung.mcm_tension | tragbar | 0.5562 | 0.0000 | 0.0010 |
| SOL_2023_5M_REAL1 | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.4422 | 0.0020 | 0.0790 |
| SOL_2024_5M_REAL1 | sehen.form_flow | tragbar | 0.8371 | 0.0330 | 0.0460 |
| SOL_2024_5M_REAL1 | sehen.form_stability | uebersteuert | 1.0000 | 0.4670 | 0.4840 |
| SOL_2024_5M_REAL1 | sehen.form_change | nahe_saettigung | 0.9910 | 0.0540 | 0.0440 |
| SOL_2024_5M_REAL1 | hoeren.energy_tone | tragbar | 0.4908 | 0.0060 | 0.0790 |
| SOL_2024_5M_REAL1 | hoeren.energy_shift | nahe_saettigung | 1.0000 | 0.0690 | 0.0240 |
| SOL_2024_5M_REAL1 | mcm_feldwirkung.mcm_coherence | tragbar | 0.7904 | 0.0000 | 0.0070 |
| SOL_2024_5M_REAL1 | mcm_feldwirkung.mcm_tension | tragbar | 0.5386 | 0.0000 | 0.0010 |
| SOL_2024_5M_REAL1 | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.4513 | 0.0010 | 0.0770 |
| SOL_2024_1H_2K | sehen.form_flow | uebersteuert | 1.0000 | 0.3190 | 0.0185 |
| SOL_2024_1H_2K | sehen.form_stability | uebersteuert | 1.0000 | 0.5005 | 0.4870 |
| SOL_2024_1H_2K | sehen.form_change | uebersteuert | 1.0000 | 0.4185 | 0.0190 |
| SOL_2024_1H_2K | hoeren.energy_tone | tragbar | 0.5212 | 0.0055 | 0.0575 |
| SOL_2024_1H_2K | hoeren.energy_shift | nahe_saettigung | 1.0000 | 0.0740 | 0.0385 |
| SOL_2024_1H_2K | mcm_feldwirkung.mcm_coherence | tragbar | 0.6147 | 0.0000 | 0.0480 |
| SOL_2024_1H_2K | mcm_feldwirkung.mcm_tension | tragbar | 0.6350 | 0.0000 | 0.0005 |
| SOL_2024_1H_2K | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.7192 | 0.0030 | 0.0400 |
| BTC_2024_5M_2K | sehen.form_flow | tragbar | 0.3514 | 0.0030 | 0.1265 |
| BTC_2024_5M_2K | sehen.form_stability | uebersteuert | 1.0000 | 0.5000 | 0.4975 |
| BTC_2024_5M_2K | sehen.form_change | tragbar | 0.4433 | 0.0070 | 0.1110 |
| BTC_2024_5M_2K | hoeren.energy_tone | tragbar | 0.5519 | 0.0085 | 0.0595 |
| BTC_2024_5M_2K | hoeren.energy_shift | uebersteuert | 1.0000 | 0.1100 | 0.0260 |
| BTC_2024_5M_2K | mcm_feldwirkung.mcm_coherence | tragbar | 0.7656 | 0.0000 | 0.0115 |
| BTC_2024_5M_2K | mcm_feldwirkung.mcm_tension | tragbar | 0.4621 | 0.0000 | 0.0005 |
| BTC_2024_5M_2K | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.3337 | 0.0000 | 0.0910 |
| BTC_2024_1H_2K | sehen.form_flow | uebersteuert | 1.0000 | 0.1090 | 0.0380 |
| BTC_2024_1H_2K | sehen.form_stability | uebersteuert | 1.0000 | 0.5035 | 0.4960 |
| BTC_2024_1H_2K | sehen.form_change | uebersteuert | 1.0000 | 0.1415 | 0.0305 |
| BTC_2024_1H_2K | hoeren.energy_tone | tragbar | 0.5954 | 0.0110 | 0.0550 |
| BTC_2024_1H_2K | hoeren.energy_shift | nahe_saettigung | 1.0000 | 0.0900 | 0.0345 |
| BTC_2024_1H_2K | mcm_feldwirkung.mcm_coherence | tragbar | 0.6833 | 0.0000 | 0.0320 |
| BTC_2024_1H_2K | mcm_feldwirkung.mcm_tension | tragbar | 0.6088 | 0.0000 | 0.0005 |
| BTC_2024_1H_2K | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.5949 | 0.0040 | 0.0795 |
| SOL_2023_NEG_STRESS | sehen.form_flow | tragbar | 0.4819 | 0.0140 | 0.0640 |
| SOL_2023_NEG_STRESS | sehen.form_stability | uebersteuert | 1.0000 | 0.3630 | 0.3330 |
| SOL_2023_NEG_STRESS | sehen.form_change | tragbar | 0.5813 | 0.0090 | 0.0880 |
| SOL_2023_NEG_STRESS | hoeren.energy_tone | tragbar | 0.5873 | 0.0140 | 0.0580 |
| SOL_2023_NEG_STRESS | hoeren.energy_shift | nahe_saettigung | 1.0000 | 0.0610 | 0.1260 |
| SOL_2023_NEG_STRESS | mcm_feldwirkung.mcm_coherence | tragbar | 0.7672 | 0.0000 | 0.0050 |
| SOL_2023_NEG_STRESS | mcm_feldwirkung.mcm_tension | tragbar | 0.4723 | 0.0000 | 0.0010 |
| SOL_2023_NEG_STRESS | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.3351 | 0.0000 | 0.1190 |

## Befund

Auffaellige Sinnesachsen: SOL_2023_5M_REAL1:sehen.form_stability=uebersteuert, SOL_2023_5M_REAL1:sehen.form_change=nahe_saettigung, SOL_2023_5M_REAL1:hoeren.energy_shift=nahe_saettigung, SOL_2024_5M_REAL1:sehen.form_stability=uebersteuert, SOL_2024_5M_REAL1:sehen.form_change=nahe_saettigung, SOL_2024_5M_REAL1:hoeren.energy_shift=nahe_saettigung, SOL_2024_1H_2K:sehen.form_flow=uebersteuert, SOL_2024_1H_2K:sehen.form_stability=uebersteuert, SOL_2024_1H_2K:sehen.form_change=uebersteuert, SOL_2024_1H_2K:hoeren.energy_shift=nahe_saettigung, BTC_2024_5M_2K:sehen.form_stability=uebersteuert, BTC_2024_5M_2K:hoeren.energy_shift=uebersteuert, ... (6 weitere)

Wenn Welten vor allem durch feste Teiler oder lokale Rohverhaeltnisse uebersetzt werden, kann das MCM-Feld nicht sicher unterscheiden, ob es echte Feldwirkung oder falsche Reizskalierung erlebt.
Damit ist ein Teil der bisherigen Weltunterschiede moeglicherweise Wahrnehmungsproblem, nicht Topologieproblem.

## Grenze

Diese Diagnose bewertet nur die Informationsaufnahme.
Sie entscheidet nicht, welche Topologie wahr ist und sie erzeugt keine neue Feldwirkung.

## Wie es weitergeht

Als naechstes sollte ein weltrelativer Wahrnehmungsadapter entworfen werden: jede Welt wird zuerst gegen ihren eigenen Rhythmus, ihre eigene Lautstaerke und ihre eigene Formspannung gelesen, bevor Werte in das MCM-Feld gehen.
