# Bewegungsarten Rohwelt-Segmente

Stand: 2026-06-20 09:44:19

## Zweck

Diese Diagnose legt validierte MCM-Preview-Bewegungen neben ihre lokalen Rohwelt- und Rezeptorsegmente.
Sie bleibt passiv: keine Handlung, kein Gate, keine aktive Regulation.

## Hierarchie

1. Grundfrage: Welche Welt-/Rezeptorlage begleitet eine passive Feldbewegung?
2. Unterpruefung: vor, waehrend und nach stabilen Uebergangspaaren vergleichen.
3. Folgeschritt: daraus passive Ausloesemilieus lesen, nicht Handlungsregeln.

## Phasenmatrix

| Paar | Phase | Samples | Welten | Segment | Rolle | Formstabilitaet | Formbruch | Energiebruch | Druck | Alignment | Strain | Rekopplung |
|---|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | nachher | 2 | 1 | rekoppelnde_lage | zentrum_stabil | -0.1487 | 0.1633 | 0.1688 | 0.1843 | 0.9269 | 0.1805 | 0.6456 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | vorher | 2 | 1 | rekoppelnde_lage | zentrum_stabil | 0.1652 | 0.2589 | 0.2487 | 0.1903 | 0.8669 | 0.1864 | 0.6473 |
| dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | wechsel | 1 | 1 | rekoppelnde_lage | zentrum_stabil | 0.2818 | 0.0658 | 0.0000 | 0.1587 | 0.8600 | 0.1766 | 0.6513 |

## Ereignislupe

| Welt | Paar | Tick | Vorher | Wechsel | Nachher | dDruck | dRekopplung |
|---|---|---:|---|---|---|---:|---:|
| LATE_SHIFT_2023 | dio_mcm_episode_02xikfk->dio_mcm_episode_1t5bcxp | 254 | rekoppelnde_lage | rekoppelnde_lage | rekoppelnde_lage | -0.0060 | -0.0017 |

## Befund

Die Rohwelt-Segmentlupe beschreibt das Milieu einer Feldbewegung.
Sie sagt nicht: Wenn dieses Segment kommt, dann muss diese Bewegung folgen.

Fachlich wichtig ist die Trennung:

```text
Rohwelt/Rezeptorlage = Kontaktmilieu
MCM-Preview-Wechsel = passive Feldbewegung
```

Damit bleibt die Diagnose organisch: Weltkontakt wird gelesen, aber nicht als Regel gesetzt.

## Wie es weitergeht

Als naechstes sollten die besten Milieus auf Wiederkehr und Drift geprueft werden.
Dann wird sichtbar, ob eine Feldbewegung an eine konkrete Weltlage gebunden ist oder mehrere Milieus tragen kann.
