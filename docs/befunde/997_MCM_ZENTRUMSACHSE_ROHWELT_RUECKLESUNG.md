# MCM-Zentrumsachse: Rohwelt-Ruecklesung

## Zweck

Diese Datei legt eine reziproke Zentrumsachse passiv auf Rohwelt-, Rezeptor- und Uebergangsereignisse zurueck.

## Sicherheitsgrenze

- passive Ruecklesung
- keine Handlung
- kein Gate
- keine Strategie

## Achsen

| Achse | Events | Paar-Events | Quellen | Welten | Effekte | Klassen | Rekopplung | Strain | Lesung |
|---|---:|---:|---|---|---|---|---:|---:|---|
| `183drjy <-> 1t5bcxp` | 1944 | 26 | `317_REZEPTOR_EPISODENFAMILIEN_REPRO_EVENTS.csv:1103 | 312_REZEPTOR_KONTAKTINSELN_EVENTS.csv:756 | 337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv:55 | 542_MCM_FELDBEWEGUNGS_MEMORY_MEHRQUELLEN_UEBERGANGSRAUM.csv:30` | `SOL_2023_NEG_STRESS_10K_RECEPTOR:594 | SOL_2026_STABLE_5K_RECEPTOR:352 | SOL_2024_SIDEWAYS_5K_RECEPTOR:298 | SOL_2025_STRESS_5K_RECEPTOR:268 | BTC_2024_1H_RECEPTOR:76 | SOL_2024_1H_RECEPTOR:70` | `tragend_unruhig:988 | kippend:839 | stabil:32 | oeffnend_belastend:24 | oeffnend_belastend:1:13 | oeffnend_belastend:2:9` | `rekoppelnde_lage:93 | offene_lage:28 | bewegungsbruch:25 | recurrently_opening_strain:24 | druck_lage:15 | recurrently_reconnecting:5` | 0.600436 | 0.270818 | `achse_weltlich_getragen` |
| `183drjy <-> 1hjbx8p` | 711 | 2 | `317_REZEPTOR_EPISODENFAMILIEN_REPRO_EVENTS.csv:358 | 312_REZEPTOR_KONTAKTINSELN_EVENTS.csv:307 | 337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv:24 | 542_MCM_FELDBEWEGUNGS_MEMORY_MEHRQUELLEN_UEBERGANGSRAUM.csv:22` | `SOL_2023_NEG_STRESS_10K_RECEPTOR:332 | SOL_2026_STABLE_5K_RECEPTOR:154 | SOL_2024_SIDEWAYS_5K_RECEPTOR:82 | SOL_2025_STRESS_5K_RECEPTOR:46 | BTC_2024_1H_RECEPTOR:26 | -:22` | `tragend_unruhig:335 | kippend:328 | oeffnend_belastend:17 | oeffnend_belastend:1:11 | oeffnend_belastend:2:5 | rekoppelnd_entlastend:4` | `rekoppelnde_lage:56 | recurrently_opening_strain:17 | bewegungsbruch:8 | druck_lage:5 | recurrently_reconnecting:4 | offene_lage:3` | 0.599929 | 0.269101 | `achse_weltlich_getragen` |
| `02xikfk <-> 1t5bcxp` | 1459 | 33 | `317_REZEPTOR_EPISODENFAMILIEN_REPRO_EVENTS.csv:850 | 312_REZEPTOR_KONTAKTINSELN_EVENTS.csv:536 | 337_BEWEGUNGSARTEN_ROHWELT_SEGMENTE_events.csv:55 | 542_MCM_FELDBEWEGUNGS_MEMORY_MEHRQUELLEN_UEBERGANGSRAUM.csv:18` | `SOL_2023_NEG_STRESS_10K_RECEPTOR:332 | SOL_2025_STRESS_5K_RECEPTOR:284 | SOL_2024_SIDEWAYS_5K_RECEPTOR:246 | SOL_2026_STABLE_5K_RECEPTOR:210 | SOL_2024_5M_RECEPTOR:66 | SOL_2024_1H_RECEPTOR:61` | `tragend_unruhig:789 | kippend:561 | stabil:36 | oeffnend_belastend:9 | rekoppelnd_entlastend:7 | oeffnend_belastend:2:5` | `rekoppelnde_lage:93 | offene_lage:28 | bewegungsbruch:25 | druck_lage:15 | recurrently_opening_strain:9 | recurrently_reconnecting:7` | 0.601301 | 0.268529 | `achse_weltlich_getragen` |

## Befund

Eine Achse ist staerker, wenn sie nicht nur als `dio_net_*`-Paar erscheint,
sondern auch in Rezeptorereignissen, Rohwelt-Uebergaengen oder Feldbewegungs-Memory wieder auftaucht.

Arbeitsableitung:

```text
Die verlegte Mitte kann als weltlich getragene Achse gelesen werden,
wenn ihre beiden Knoten in Ereignissen und Uebergaengen wieder gekoppelt auftreten.
```

## Wie es weitergeht

Als naechstes sollte diese Achse zeitlich lokalisiert werden: in welchen Tickbereichen und Weltphasen tritt sie gehauft auf?