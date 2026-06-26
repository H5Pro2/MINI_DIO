# 815 - Block-K Randfamilie Folgewelt/Reifung: dio_1un4

## Fragestellung

Bleibt `dio_1un4` eine Randspannung, reift sie ueber laengere Feldzeit nach, driftet sie oder bildet sie Nachbarschaften?

## Gruppensynthese

| Gruppe | Anteil | Klasse | Innenzustand | Strain | Trust | Nachhall | Rekopplung | Carry | Hoeren-Stim. | Einbettung |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| kurz_2k | 0.0021 | tragend_unruhig | inner_effect_carried_unrest | 0.2306 | 0.4696 | 0.0125 | 0.6283 | 0.4291 | 0.4890 | 0.5489 |
| asset_mixed_2k | 0.0025 | tragend_unruhig | inner_effect_carried_unrest | 0.2307 | 0.4566 | 0.0170 | 0.6284 | 0.4298 | 0.4880 | 0.5390 |
| lang_10k | 0.0021 | tragend_unruhig | inner_effect_carried_unrest | 0.2230 | 0.6533 | 0.0475 | 0.6466 | 0.4712 | 0.4871 | 0.6535 |

## 10k-Verlauf

| Segment | Anteil | Klasse | Strain | Trust | Nachhall | Einbettung |
|---|---:|---|---:|---:|---:|---:|
| q1 | 0.0019 | tragend_unruhig | 0.1690 | 0.4017 | 0.0170 | 0.5426 |
| q2 | 0.0019 | tragend_unruhig | 0.2234 | 0.6335 | 0.0367 | 0.5628 |
| q3 | 0.0025 | tragend_unruhig | 0.2217 | 0.7063 | 0.0654 | 0.6401 |
| q4 | 0.0019 | tragend_unruhig | 0.2222 | 0.7188 | 0.0537 | 0.5906 |

## Nachbarschaften

| Gruppe | Welt | Vorher | Nachher | Vorher-Klasse | Nachher-Klasse |
|---|---|---|---|---|---|
| asset_mixed_2k | kontrolliert_btc_2024_5m_test1_2000_btcusdt | dio_1oye:1, dio_1ewh:1, dio_14wj:1 | dio_0u2x:1, dio_1oc2:1, dio_0jho:1 | stabil:4 | stabil:2, tragend_unruhig:2 |
| asset_mixed_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | dio_09bn:1, dio_06jk:1, dio_0l7p:1 | dio_05yg:1, dio_0m9z:1, dio_0byp:1 | stabil:4 | tragend_unruhig:3, stabil:1 |
| asset_mixed_2k | kontrolliert_paxg_2024_5m_test1_2000_paxgusdt | dio_15rn:1, dio_0h9h:1 | dio_0cky:1, dio_0ahb:1 | stabil:2 | tragend_unruhig:2 |
| asset_mixed_2k | kontrolliert_sol_2024_5m_test1_2000_solusdt | dio_0l7p:2, dio_1ap6:1, dio_0h9h:1 | dio_04uf:3, dio_09hj:1, dio_1q85:1 | stabil:9, tragend_unruhig:1 | stabil:7, tragend_unruhig:3 |
| kurz_2k | kontrolliert_2026_sideways_test1_2000_5m_solusdt | dio_1gp2:1, dio_0l7p:1, dio_0m9z:1 | dio_00ja:1, dio_18kx:1, dio_0pxr:1 | stabil:3 | stabil:2, tragend_unruhig:1 |
| kurz_2k | kontrolliert_btc_2025_1h_test1_2000_btcusdt | dio_14wj:2, dio_1d3j:1, dio_1tyd:1 | dio_04uf:1, dio_0i80:1, dio_11it:1 | stabil:4, kippend:1 | stabil:3, tragend_unruhig:2 |
| kurz_2k | kontrolliert_kas_2024_5m_test1_2000_kasusdt | dio_09bn:1, dio_06jk:1, dio_0l7p:1 | dio_05yg:1, dio_0m9z:1, dio_0byp:1 | stabil:4 | tragend_unruhig:3, stabil:1 |
| kurz_2k | kontrolliert_sol_2025_5m_test1_2000_solusdt | dio_0m9z:1, dio_14wj:1, dio_0n0i:1 | dio_0klp:2, dio_18po:1, dio_0h9h:1 | stabil:4, tragend_unruhig:1 | stabil:3, tragend_unruhig:2 |
| lang_10k | kontrolliert_2023_negative_stress_10k_5m_solusdt | dio_0l7p:4, dio_104t:3, dio_0m9z:3 | dio_17ct:3, dio_1mwv:2, dio_0u2x:2 | stabil:18, tragend_unruhig:3 | stabil:18, tragend_unruhig:3 |
| lang_10k | kontrolliert_2023_positive_expansion_10k_5m_solusdt | dio_14wj:2, dio_0m9z:2, dio_0obq:2 | dio_05mh:3, dio_155c:2, dio_04uf:2 | stabil:13, tragend_unruhig:3 | stabil:11, tragend_unruhig:5 |
| lang_10k | kontrolliert_2026_sideways_10k_5m_solusdt | dio_104t:7, dio_0dd2:3, dio_155c:2 | dio_17ct:3, dio_1o4z:2, dio_05yg:2 | stabil:27, tragend_unruhig:1 | stabil:19, tragend_unruhig:8, kippend:1 |
| lang_10k | kontrolliert_btc_2025_5m_10k_btcusdt | dio_14wj:2, dio_0l7p:2, dio_1oye:1 | dio_0pz6:2, dio_04uf:2, dio_0obq:2 | stabil:15, tragend_unruhig:2 | stabil:12, tragend_unruhig:5 |

## Befund

`dio_1un4` bleibt in allen Gruppen eine Rand-/Unruhefamilie, aber sie ist kein reines Rauschen.

- in kurzen und asset-gemischten 2k-Welten ist Trust niedrig und Nachhall fast nicht ausgebildet,
- in 10k steigt Trust und Feldzeit-Einbettung deutlich,
- im 10k-Verlauf beginnt q1 noch schwach getragen; q2 bis q4 zeigen deutlich hoeheren Trust,
- Strain bleibt ab q2 trotzdem hoch; die Familie kippt also nicht einfach in eine stabile Mitte,
- q3 wirkt am staerksten eingebettet, q4 bleibt vertrauensnaeher, aber nicht voll stabilisiert,
- die Nachbarschaften sind ueberwiegend stabil; die Randfamilie ist also eher Bruecken-/Kontaktzone als isoliertes Rauschen.

Damit ist die wahrscheinlichste Lesung: `dio_1un4` ist eine randnahe Spannungsbedeutung, die durch laengere Feldzeit teilweise nachreifen kann, aber ihre Randqualitaet nicht verliert.

## Grenze

Der Befund beschreibt passive Innenfeldreifung. Er ist keine Handlungsauswertung und keine Richtungslogik.

## Wie es weitergeht

Als naechstes sollte `dio_1un4` gegen seine haeufigsten Nachbarfamilien gelesen werden. Dann wird sichtbar, ob daraus eine Bruecke, eine Unterfamilie oder ein isolierter Randpunkt entsteht.
