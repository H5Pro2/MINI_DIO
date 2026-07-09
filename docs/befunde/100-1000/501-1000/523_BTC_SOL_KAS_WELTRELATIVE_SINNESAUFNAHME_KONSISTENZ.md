# Weltuebergreifende Informationsaufnahme: Diagnose

Stand: 2026-06-21 14:58:43

## Zweck

Diese Diagnose prueft, ob MINI_DIO Welten ueber Sehen, Hoeren und MCM-Feldwirkung vergleichbar aufnimmt.
Sie liest nicht die MCM-Topologie selbst, sondern den Schritt davor: Rohwelt zu Sinneswerten.
Sinnesmodus: `world_relative`.

Wichtig: Das ist keine Handlung, kein Gate und keine Runtime-Regel.

## Hierarchie

1. Allgemeine Grundfrage: Ist die Informationsaufnahme ueber Welten einheitlich genug?
2. Konkrete Unterpruefung: Welche Sinnesachsen uebersteuern, flachen ab oder bleiben tragbar?
3. Folgeschritt: Wenn die Aufnahme nicht einheitlich ist, braucht MINI_DIO einen weltrelativen Wahrnehmungsadapter.

## Weltuebersicht

| Welt | Zustand | Kerzen | Return p95 | Range p95 | Volume p95 |
|---|---|---:|---:|---:|---:|
| BTC2025_QUIET | reiz_tragbar | 4000 | 0.0016 | 0.0022 | 110.96 |
| BTC2025_STRESS | reiz_tragbar | 4000 | 0.0030 | 0.0045 | 272.68 |
| SOL2024_QUIET | reiz_tragbar | 4000 | 0.0036 | 0.0052 | 24394.60 |
| SOL2024_STRESS | reiz_tragbar | 4000 | 0.0078 | 0.0125 | 69890.81 |
| SOL2025_QUIET | reiz_tragbar | 4000 | 0.0035 | 0.0051 | 26572.83 |
| SOL2025_STRESS | reiz_tragbar | 4000 | 0.0058 | 0.0091 | 47157.64 |
| KAS2024_5M | reiz_tragbar | 2000 | 0.0082 | 0.0124 | 2622793.65 |

## Sinnesachsen

| Welt | Achse | Zustand | p95 abs | Saettigung | Flachheit |
|---|---|---|---:|---:|---:|
| BTC2025_QUIET | sehen.form_flow | tragbar | 0.5470 | 0.0000 | 0.0790 |
| BTC2025_QUIET | sehen.form_stability | tragbar | 0.6203 | 0.0000 | 0.0343 |
| BTC2025_QUIET | sehen.form_change | tragbar | 0.5212 | 0.0000 | 0.0955 |
| BTC2025_QUIET | hoeren.energy_tone | tragbar | 0.4897 | 0.0000 | 0.0585 |
| BTC2025_QUIET | hoeren.energy_shift | tragbar | 0.5511 | 0.0000 | 0.0678 |
| BTC2025_QUIET | mcm_feldwirkung.mcm_coherence | tragbar | 0.7765 | 0.0000 | 0.0003 |
| BTC2025_QUIET | mcm_feldwirkung.mcm_tension | tragbar | 0.2786 | 0.0000 | 0.0032 |
| BTC2025_QUIET | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.3028 | 0.0000 | 0.1148 |
| BTC2025_STRESS | sehen.form_flow | tragbar | 0.5511 | 0.0022 | 0.0712 |
| BTC2025_STRESS | sehen.form_stability | tragbar | 0.6093 | 0.0003 | 0.0390 |
| BTC2025_STRESS | sehen.form_change | tragbar | 0.5511 | 0.0025 | 0.0755 |
| BTC2025_STRESS | hoeren.energy_tone | tragbar | 0.4861 | 0.0000 | 0.0640 |
| BTC2025_STRESS | hoeren.energy_shift | tragbar | 0.5511 | 0.0000 | 0.0600 |
| BTC2025_STRESS | mcm_feldwirkung.mcm_coherence | tragbar | 0.7812 | 0.0000 | 0.0003 |
| BTC2025_STRESS | mcm_feldwirkung.mcm_tension | tragbar | 0.2706 | 0.0000 | 0.0027 |
| BTC2025_STRESS | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.2965 | 0.0000 | 0.1205 |
| SOL2024_QUIET | sehen.form_flow | tragbar | 0.5511 | 0.0000 | 0.0558 |
| SOL2024_QUIET | sehen.form_stability | tragbar | 0.6197 | 0.0000 | 0.0410 |
| SOL2024_QUIET | sehen.form_change | tragbar | 0.5511 | 0.0000 | 0.0820 |
| SOL2024_QUIET | hoeren.energy_tone | tragbar | 0.4896 | 0.0000 | 0.0673 |
| SOL2024_QUIET | hoeren.energy_shift | tragbar | 0.5511 | 0.0000 | 0.0570 |
| SOL2024_QUIET | mcm_feldwirkung.mcm_coherence | tragbar | 0.7766 | 0.0000 | 0.0003 |
| SOL2024_QUIET | mcm_feldwirkung.mcm_tension | tragbar | 0.2671 | 0.0000 | 0.0037 |
| SOL2024_QUIET | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.3029 | 0.0000 | 0.1192 |
| SOL2024_STRESS | sehen.form_flow | tragbar | 0.5511 | 0.0018 | 0.0653 |
| SOL2024_STRESS | sehen.form_stability | tragbar | 0.6361 | 0.0013 | 0.0423 |
| SOL2024_STRESS | sehen.form_change | tragbar | 0.5511 | 0.0020 | 0.0628 |
| SOL2024_STRESS | hoeren.energy_tone | tragbar | 0.4960 | 0.0000 | 0.0610 |
| SOL2024_STRESS | hoeren.energy_shift | tragbar | 0.5511 | 0.0000 | 0.0628 |
| SOL2024_STRESS | mcm_feldwirkung.mcm_coherence | tragbar | 0.7736 | 0.0000 | 0.0003 |
| SOL2024_STRESS | mcm_feldwirkung.mcm_tension | tragbar | 0.2667 | 0.0000 | 0.0010 |
| SOL2024_STRESS | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.3190 | 0.0000 | 0.1190 |
| SOL2025_QUIET | sehen.form_flow | tragbar | 0.5511 | 0.0000 | 0.0612 |
| SOL2025_QUIET | sehen.form_stability | tragbar | 0.6383 | 0.0000 | 0.0395 |
| SOL2025_QUIET | sehen.form_change | tragbar | 0.5510 | 0.0003 | 0.0573 |
| SOL2025_QUIET | hoeren.energy_tone | tragbar | 0.4793 | 0.0003 | 0.0607 |
| SOL2025_QUIET | hoeren.energy_shift | tragbar | 0.5511 | 0.0000 | 0.0457 |
| SOL2025_QUIET | mcm_feldwirkung.mcm_coherence | tragbar | 0.7725 | 0.0000 | 0.0003 |
| SOL2025_QUIET | mcm_feldwirkung.mcm_tension | tragbar | 0.2644 | 0.0000 | 0.0022 |
| SOL2025_QUIET | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.3083 | 0.0000 | 0.1087 |
| SOL2025_STRESS | sehen.form_flow | tragbar | 0.5511 | 0.0030 | 0.0767 |
| SOL2025_STRESS | sehen.form_stability | tragbar | 0.6285 | 0.0005 | 0.0367 |
| SOL2025_STRESS | sehen.form_change | tragbar | 0.5511 | 0.0030 | 0.0715 |
| SOL2025_STRESS | hoeren.energy_tone | tragbar | 0.4924 | 0.0000 | 0.0570 |
| SOL2025_STRESS | hoeren.energy_shift | tragbar | 0.5510 | 0.0000 | 0.0628 |
| SOL2025_STRESS | mcm_feldwirkung.mcm_coherence | tragbar | 0.7773 | 0.0000 | 0.0003 |
| SOL2025_STRESS | mcm_feldwirkung.mcm_tension | tragbar | 0.2668 | 0.0000 | 0.0010 |
| SOL2025_STRESS | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.2945 | 0.0000 | 0.1315 |
| KAS2024_5M | sehen.form_flow | tragbar | 0.5511 | 0.0035 | 0.0720 |
| KAS2024_5M | sehen.form_stability | tragbar | 0.6260 | 0.0020 | 0.0450 |
| KAS2024_5M | sehen.form_change | tragbar | 0.5510 | 0.0035 | 0.0650 |
| KAS2024_5M | hoeren.energy_tone | tragbar | 0.5057 | 0.0000 | 0.0585 |
| KAS2024_5M | hoeren.energy_shift | tragbar | 0.5511 | 0.0000 | 0.0645 |
| KAS2024_5M | mcm_feldwirkung.mcm_coherence | tragbar | 0.7740 | 0.0000 | 0.0005 |
| KAS2024_5M | mcm_feldwirkung.mcm_tension | tragbar | 0.2720 | 0.0000 | 0.0025 |
| KAS2024_5M | mcm_feldwirkung.mcm_asymmetry | tragbar | 0.3115 | 0.0000 | 0.1100 |

## Befund

Auffaellige Sinnesachsen: -

Wenn Welten vor allem durch feste Teiler oder lokale Rohverhaeltnisse uebersetzt werden, kann das MCM-Feld nicht sicher unterscheiden, ob es echte Feldwirkung oder falsche Reizskalierung erlebt.
Im weltrelativen Modus wird dagegen geprueft, ob die Aufnahme bereits gegen den eigenen Rhythmus der Welt gelesen wird.

## Grenze

Diese Diagnose bewertet nur die Informationsaufnahme.
Sie entscheidet nicht, welche Topologie wahr ist und sie erzeugt keine neue Feldwirkung.

## Wie es weitergeht

Als naechstes sollte bei weiterhin auffaelligen Achsen geprueft werden, ob sie echte Weltqualitaet tragen oder ob der Adapter eine feinere Aufnahme braucht.
