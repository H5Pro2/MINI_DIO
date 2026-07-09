# Preview-Uebergangspaare Klassifikation

Stand: 2026-06-20 09:44:19

## Zweck

Diese Diagnose klassifiziert konkrete MCM-Preview-Uebergangspaare als passive Feldbewegungen.
Sie bleibt passiv: keine Handlung, kein Gate, kein Entry-Signal.

## Hierarchie

1. Grundfrage: Welche Bewegungsarten entstehen zwischen Bedeutungsinseln?
2. Unterpruefung: Paare nach Weltbreite, Druck, Schaerfe, Rekopplung und Rollenwechsel klassifizieren.
3. Folgeschritt: stabile Bewegungsarten ueber weitere Welten validieren.

## Bewegungsarten

- `grundinsel_wechsel`: breiter, ruhiger Wechsel zwischen stabilen Inseln.
- `rekopplungsbogen`: Druck sinkt und Rekopplung steigt.
- `druck_rueckfuehrung`: Druck steigt und Rekopplung sinkt beim Rueckweg.
- `offener_uebergang`: Wechsel mit offener Variante und leichtem Druck.
- `schaerfungsuebergang`: Schaerfe steigt ohne starken Druckanstieg.
- `lokale_einzelkante`: seltene lokale Kante.
- `gemischte_feldbewegung`: noch nicht klar genug getrennte Bewegung.

## Klassenuebersicht

| Klasse | Paare | Events | Welten-Summe | Top-Paar | dDruck | dSchaerfe | dRekopplung |
|---|---:|---:|---:|---|---:|---:|---:|
| lokale_einzelkante | 7 | 7 | 7 | dio_mcm_episode_1xlulkb->dio_mcm_episode_00i7zy5 | 0.0111 | -0.0331 | -0.0133 |
| rekopplungsbogen | 6 | 6 | 6 | dio_mcm_episode_00i7zy5->dio_mcm_episode_05712v1 | -0.0672 | 0.1782 | 0.0316 |
| offener_uebergang | 4 | 4 | 4 | dio_mcm_episode_0inn73s->dio_mcm_episode_0ifxej6 | 0.0118 | -0.0421 | -0.0085 |
| druck_rueckfuehrung | 2 | 2 | 2 | dio_mcm_episode_05712v1->dio_mcm_episode_0cokzhj | 0.1077 | -0.3078 | -0.0670 |
| schaerfungsuebergang | 1 | 1 | 1 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | -0.0337 | 0.1547 | 0.0066 |

## Paarmatrix

| Paar | Klasse | Anzahl | Welten | Rollenwechsel | dDruck | dSchaerfe | dRekopplung |
|---|---|---:|---:|---|---:|---:|---:|
| dio_mcm_episode_1xlulkb->dio_mcm_episode_00i7zy5 | lokale_einzelkante | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | 0.0054 | 0.0000 | -0.0124 |
| dio_mcm_episode_00i7zy5->dio_mcm_episode_05712v1 | rekopplungsbogen | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | -0.0402 | 0.1342 | 0.0238 |
| dio_mcm_episode_05712v1->dio_mcm_episode_0cokzhj | druck_rueckfuehrung | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | 0.0482 | -0.4469 | -0.0356 |
| dio_mcm_episode_0cokzhj->dio_mcm_episode_1al8fjz | lokale_einzelkante | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | 0.0169 | 0.0499 | 0.0028 |
| dio_mcm_episode_1al8fjz->dio_mcm_episode_1y2gc2i | lokale_einzelkante | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | 0.0273 | -0.0482 | -0.0109 |
| dio_mcm_episode_1y2gc2i->dio_mcm_episode_1y26981 | lokale_einzelkante | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | 0.0168 | 0.0310 | -0.0267 |
| dio_mcm_episode_1y26981->dio_mcm_episode_17i4j9o | lokale_einzelkante | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | -0.0164 | -0.0676 | 0.0014 |
| dio_mcm_episode_17i4j9o->dio_mcm_episode_0y50lf3 | lokale_einzelkante | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | 0.0243 | 0.0261 | -0.0133 |
| dio_mcm_episode_0y50lf3->dio_mcm_episode_19w6ffd | druck_rueckfuehrung | 1 | 1 | zentrum_stabil->spannungsrand_kippnaehe (1/1) | 0.1673 | -0.1687 | -0.0984 |
| dio_mcm_episode_19w6ffd->dio_mcm_episode_0inn73s | rekopplungsbogen | 1 | 1 | spannungsrand_kippnaehe->offene_variante (1/1) | -0.1286 | 0.2092 | 0.0862 |
| dio_mcm_episode_0inn73s->dio_mcm_episode_0ifxej6 | offener_uebergang | 1 | 1 | offene_variante->offene_variante (1/1) | 0.0100 | -0.0922 | -0.0163 |
| dio_mcm_episode_0ifxej6->dio_mcm_episode_0x7d4av | rekopplungsbogen | 1 | 1 | offene_variante->zentrum_stabil (1/1) | -0.0542 | 0.2979 | 0.0134 |
| dio_mcm_episode_0x7d4av->dio_mcm_episode_0x44t5z | offener_uebergang | 1 | 1 | offene_variante->spannungsrand_kippnaehe (1/1) | 0.0122 | 0.3478 | -0.0247 |
| dio_mcm_episode_0x44t5z->dio_mcm_episode_1acdaev | rekopplungsbogen | 1 | 1 | spannungsrand_kippnaehe->offene_variante (1/1) | -0.0783 | 0.1217 | 0.0374 |
| dio_mcm_episode_1acdaev->dio_mcm_episode_0vzztud | offener_uebergang | 1 | 1 | offene_variante->offene_variante (1/1) | 0.0001 | 0.3636 | 0.0074 |
| dio_mcm_episode_0vzztud->dio_mcm_episode_0vq085e | offener_uebergang | 1 | 1 | offene_variante->offene_variante (1/1) | 0.0248 | -0.7875 | -0.0003 |
| dio_mcm_episode_0vq085e->dio_mcm_episode_1yv9fvu | rekopplungsbogen | 1 | 1 | offene_variante->zentrum_stabil (1/1) | -0.0903 | 0.2607 | 0.0162 |
| dio_mcm_episode_1yv9fvu->dio_mcm_episode_1so7ez5 | rekopplungsbogen | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | -0.0118 | 0.0457 | 0.0130 |
| dio_mcm_episode_1so7ez5->dio_mcm_episode_02xikfk | lokale_einzelkante | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | 0.0036 | -0.2230 | -0.0339 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | schaerfungsuebergang | 1 | 1 | zentrum_stabil->zentrum_stabil (1/1) | -0.0337 | 0.1547 | 0.0066 |

## Befund

Die Klassifikation ist ein erster Ordnungsversuch, keine endgueltige Ontologie.
Sie zeigt aber, dass die Uebergaenge nicht gleichartig sind.

Der wichtigste bisherige Bewegungsbefund bleibt:

```text
1t5bcxp -> 183drjy = rekoppelnde Richtung
183drjy -> 1t5bcxp = Rueckfuehrung mit mehr Druck/offener Variante
```

Damit entsteht eine passive Feldbewegung zwischen Grundinsel und rekoppelnder Innenzone.

## Wie es weitergeht

Als naechstes wird geprueft, ob diese Bewegungsarten in weiteren Welten stabil bleiben oder neue Klassen benoetigen.
