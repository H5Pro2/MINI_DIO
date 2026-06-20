# Preview-Uebergangspaare Klassifikation

Stand: 2026-06-19 23:57:18

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
| rekopplungsbogen | 7 | 31 | 22 | dio_mcm_episode_0magw2b->dio_mcm_episode_14wxqua | -0.0195 | 0.0818 | 0.0163 |
| grundinsel_wechsel | 6 | 161 | 33 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | -0.0039 | 0.0128 | 0.0047 |
| gemischte_feldbewegung | 6 | 42 | 23 | dio_mcm_episode_1so7ez5->dio_mcm_episode_02xikfk | 0.0120 | -0.0491 | -0.0062 |
| schaerfungsuebergang | 3 | 23 | 11 | dio_mcm_episode_0inn73s->dio_mcm_episode_04e9yp5 | -0.0072 | 0.0828 | -0.0044 |
| druck_rueckfuehrung | 2 | 39 | 7 | dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 0.0598 | 0.0406 | -0.0300 |
| offener_uebergang | 1 | 11 | 5 | dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | 0.0070 | 0.1278 | -0.0167 |

## Paarmatrix

| Paar | Klasse | Anzahl | Welten | Rollenwechsel | dDruck | dSchaerfe | dRekopplung |
|---|---|---:|---:|---|---:|---:|---:|
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | grundinsel_wechsel | 33 | 4 | zentrum_stabil->zentrum_stabil (33/33) | -0.0165 | 0.0563 | 0.0150 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | druck_rueckfuehrung | 32 | 3 | zentrum_stabil->offene_variante (11/32) | 0.0640 | 0.0021 | -0.0337 |
| dio_mcm_episode_1y00xwb->dio_mcm_episode_0vkdfwc | grundinsel_wechsel | 29 | 6 | zentrum_stabil->zentrum_stabil (24/29) | -0.0020 | -0.0102 | 0.0020 |
| dio_mcm_episode_14wxqua->dio_mcm_episode_1y00xwb | grundinsel_wechsel | 27 | 6 | zentrum_stabil->zentrum_stabil (21/27) | -0.0160 | 0.0153 | 0.0033 |
| dio_mcm_episode_0vkdfwc->dio_mcm_episode_1t5bcxp | grundinsel_wechsel | 26 | 6 | zentrum_stabil->zentrum_stabil (20/26) | 0.0111 | 0.0020 | -0.0042 |
| dio_mcm_episode_04e9yp5->dio_mcm_episode_14wxqua | grundinsel_wechsel | 24 | 6 | zentrum_stabil->zentrum_stabil (19/24) | 0.0091 | 0.0124 | -0.0041 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | grundinsel_wechsel | 22 | 5 | zentrum_stabil->zentrum_stabil (16/22) | -0.0091 | 0.0012 | 0.0161 |
| dio_mcm_episode_1so7ez5->dio_mcm_episode_02xikfk | gemischte_feldbewegung | 11 | 4 | zentrum_stabil->zentrum_stabil (6/11) | 0.0067 | -0.0948 | -0.0042 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_02xikfk | offener_uebergang | 11 | 5 | offene_variante->offene_variante (6/11) | 0.0070 | 0.1278 | -0.0167 |
| dio_mcm_episode_0inn73s->dio_mcm_episode_04e9yp5 | schaerfungsuebergang | 11 | 5 | zentrum_stabil->zentrum_stabil (6/11) | -0.0236 | 0.0921 | 0.0039 |
| dio_mcm_episode_0magw2b->dio_mcm_episode_1yv9fvu | gemischte_feldbewegung | 8 | 5 | zentrum_stabil->zentrum_stabil (3/8) | 0.0089 | -0.1013 | -0.0069 |
| dio_mcm_episode_03xfov3->dio_mcm_episode_183drjy | gemischte_feldbewegung | 8 | 3 | zentrum_stabil->zentrum_stabil (7/8) | 0.0368 | -0.1151 | -0.0237 |
| dio_mcm_episode_14wxqua->dio_mcm_episode_0magw2b | schaerfungsuebergang | 7 | 3 | zentrum_stabil->zentrum_stabil (3/7) | -0.0082 | 0.0837 | -0.0098 |
| dio_mcm_episode_0magw2b->dio_mcm_episode_14wxqua | rekopplungsbogen | 7 | 5 | zentrum_stabil->zentrum_stabil (5/7) | -0.0189 | 0.0124 | 0.0194 |
| dio_mcm_episode_1yv9fvu->dio_mcm_episode_1so7ez5 | gemischte_feldbewegung | 7 | 5 | zentrum_stabil->zentrum_stabil (5/7) | 0.0097 | 0.0373 | -0.0051 |
| dio_mcm_episode_17i4j9o->dio_mcm_episode_0y50lf3 | druck_rueckfuehrung | 7 | 4 | zentrum_stabil->zentrum_stabil (3/7) | 0.0556 | 0.0791 | -0.0263 |
| dio_mcm_episode_0y50lf3->dio_mcm_episode_17i4j9o | rekopplungsbogen | 5 | 3 | zentrum_stabil->zentrum_stabil (5/5) | -0.0052 | 0.1814 | 0.0164 |
| dio_mcm_episode_1yv9fvu->dio_mcm_episode_1y00xwb | rekopplungsbogen | 5 | 3 | zentrum_stabil->zentrum_stabil (5/5) | -0.0145 | 0.2080 | 0.0150 |
| dio_mcm_episode_0vkdfwc->dio_mcm_episode_03xfov3 | schaerfungsuebergang | 5 | 3 | zentrum_stabil->zentrum_stabil (5/5) | 0.0102 | 0.0727 | -0.0074 |
| dio_mcm_episode_009px6q->dio_mcm_episode_0y50lf3 | rekopplungsbogen | 4 | 4 | zentrum_stabil->zentrum_stabil (4/4) | -0.0158 | 0.0160 | 0.0112 |
| dio_mcm_episode_0x7d4av->dio_mcm_episode_0m0hadc | gemischte_feldbewegung | 4 | 3 | zentrum_stabil->zentrum_stabil (3/4) | 0.0009 | 0.0515 | -0.0040 |
| dio_mcm_episode_0m0hadc->dio_mcm_episode_0magw2b | rekopplungsbogen | 4 | 3 | zentrum_stabil->zentrum_stabil (2/4) | -0.0178 | 0.1823 | 0.0097 |
| dio_mcm_episode_0wxdilw->dio_mcm_episode_04e9yp5 | gemischte_feldbewegung | 4 | 3 | zentrum_stabil->zentrum_stabil (3/4) | 0.0092 | -0.0723 | 0.0067 |
| dio_mcm_episode_0magw2b->dio_mcm_episode_1y00xwb | rekopplungsbogen | 3 | 2 | offene_variante->zentrum_stabil (2/3) | -0.0300 | 0.0692 | 0.0320 |
| dio_mcm_episode_037i64j->dio_mcm_episode_02xikfk | rekopplungsbogen | 3 | 2 | zentrum_stabil->offene_variante (1/3) | -0.0344 | -0.0965 | 0.0104 |

## Befund

Die Klassifikation ist ein erster Ordnungsversuch, keine endgueltige Ontologie.
Sie zeigt aber, dass die Uebergaenge nicht gleichartig sind.

Der wichtigste bisherige Bewegungsbefund bleibt:

```text
1t5bcxp -> 183drjy = breiter Grundinsel-Wechsel mit rekoppelnder Tendenz
183drjy -> 1t5bcxp = Rueckfuehrung mit mehr Druck/offener Variante
```

Damit entsteht eine passive Feldbewegung zwischen Grundinsel und rekoppelnder Innenzone.
Die automatische Klasse `grundinsel_wechsel` fuer `1t5bcxp -> 183drjy` ist daher
nicht falsch, aber unvollstaendig: das Paar ist breit genug fuer Grundinsel-Wechsel
und zeigt gleichzeitig Drucksenkung plus Rekopplungsanstieg.

Fachlich sauberer ist die Lesart:

```text
1t5bcxp -> 183drjy = rekoppelnder Grundinsel-Wechsel
183drjy -> 1t5bcxp = druckvollere Rueckfuehrung
```

Weitere Klassen sind als Arbeitsklassen zu lesen. Sie helfen beim Sortieren, aber sie
duerfen nicht als starre MCM-Ontologie behandelt werden.

## Wie es weitergeht

Als naechstes wird geprueft, ob diese Bewegungsarten in weiteren Welten stabil bleiben oder neue Klassen benoetigen.
