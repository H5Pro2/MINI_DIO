# MCM-Feldbewegungs-Memory Summary

Stand: 2026-06-20

## Zweck

Dieser Report verdichtet vorhandene passive Befunde in eine erste MCM-Feldbewegungs-Memory.
Er ist keine Handlungsschicht, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Welche gerichteten MCM-Feldbewegungen tragen wiederkehrende Feldwirkung?
2. Unterpruefung: Welche Bewegungen wirken wiederkehrend getragen, fragmentiert oder offen driftend?
3. Folgeschritt: Diese passive Erinnerung kann spaeter als Innenfeld-Leseschicht dienen, ohne Handlung zu erzwingen.

## Eingaben

- `docs\befunde\386_JAHRES_ZEITAUFLOESUNGS_MATRIX_GERICHTETE_FELDBEWEGUNG.csv`
- `docs\befunde\391_KAS_ASSET_GEGENPROBE_PASSIVE_REGULATIONSQUALITAET_reproduktion.csv`

Quellenhinweis:

Dieser Report kann mehrere Ableitungen derselben Grundbefunde enthalten.
Er liest deshalb die wiederkehrende Richtung als Verdichtungsbefund, nicht als unabhaengige statistische Beweiszahl.

## Passive Verdichtung

| Bewegung | Beobachtungen | Ereignisse | dominante Tragart | Feldmemory-Qualitaet | Reifungsnotiz | dominante Feldposition | Drift | Quellen |
|---|---:|---:|---|---|---|---|---|---|
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 7 | 480 | fragmentiert | recurrently_fragmented | consistent_top_quality | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | lokal_offen | 386_JAHRES_ZEITAUFLOESUNGS_MATRIX_GERICHTETE_FELDBEWEGUNG.csv:6; 391_KAS_ASSET_GEGENPROBE_PASSIVE_REGULATIONSQUALITAET_reproduktion.csv:1 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 7 | 537 | eng_getragen | recurrently_carried | consistent_top_quality | rekoppelnde_lage->rekoppelnde_lage->rekoppelnde_lage | wiederkehrend_variabel | 386_JAHRES_ZEITAUFLOESUNGS_MATRIX_GERICHTETE_FELDBEWEGUNG.csv:6; 391_KAS_ASSET_GEGENPROBE_PASSIVE_REGULATIONSQUALITAET_reproduktion.csv:1 |

## Befund

Die bisherige Verdichtung bleibt passiv:

- `dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy` wird als wiederkehrend getragen gelesen.
- `dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp` wird als wiederkehrend fragmentiert gelesen.

Wichtig: Diese Qualitaeten sind keine Regeln. Sie beschreiben gewachsene Innenfeldspuren.

## Export

- CSV: `docs\befunde\394_MCM_FELDBEWEGUNGS_MEMORY_SUMMARY.csv`
- JSON: `docs\befunde\394_MCM_FELDBEWEGUNGS_MEMORY_SUMMARY.json`

## Wie es weitergeht

Als naechstes kann diese MCM-Feldbewegungs-Memory gegen weitere Welten laufen, um zu pruefen, ob neue Bewegungen jung bleiben, driften oder wiederkehrend tragen.
