# PAXG 2025 Langfenster-Zusammenfassung

## Grundlage

Verglichen wurden drei längere PAXG-2025-Lesungen:

| Welt | Episoden | Hinweis |
|---|---:|---|
| PAXG_2025_5M_10K | 9994 | vorhandener 5m-10k-Lauf |
| PAXG_2025_15M_3333 | 3327 | aus 5m-10k aggregierte 15m-Welt |
| PAXG_2025_1H_10K | 8754 | vorhandener 1h-10k-Lauf |

## Topologie

| Welt | Zustand | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2025_5M_10K | stark_zentriert_wenig_rand | 0.8725 | 0.1202 | 0.0073 | 0.7144 | 0.5410 | 0.1517 | 0.8561 |
| PAXG_2025_15M_3333 | stark_zentriert_wenig_rand | 0.9922 | 0.0078 | 0.0000 | 0.7025 | 0.5305 | 0.1652 | 0.8449 |
| PAXG_2025_1H_10K | stark_zentriert_wenig_rand | 0.8098 | 0.1857 | 0.0045 | 0.7061 | 0.5357 | 0.1519 | 0.8437 |

## Randdruck-Lupe

| Welt | Randdruck | Offen | Rekopplung | Dämpfung | Strain | Intake | Visual Gap | Hearing Gap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2025_5M_10K | 0.4372 | 0.1167 | 0.3783 | 0.0678 | 0.1517 | 0.1132 | 0.1649 | 0.0744 |
| PAXG_2025_15M_3333 | 0.4013 | 0.1614 | 0.3180 | 0.1193 | 0.1652 | 0.1042 | 0.1759 | 0.0982 |
| PAXG_2025_1H_10K | 0.4194 | 0.1477 | 0.3308 | 0.1021 | 0.1519 | 0.1052 | 0.1763 | 0.1007 |

## Lesart

Das längere PAXG-2025-Fenster zeigt mehr Tiefe als die 2000er-Ausschnitte:

- 5m und 1h tragen deutlich mehr offene Variante als die kurzen Holdout-Fenster.
- 5m bleibt am stärksten rekoppelnd und am wenigsten gedämpft.
- 15m wirkt im langen Vergleich am stärksten zentriert und am stärksten geglättet.
- Kleine Rand-/Kippanteile erscheinen in 5m und 1h, werden aber nicht dominant.

Damit ist die Dämpfungszunahme aus SHIFT1 keine einfache Gesamttendenz. Sie wirkt eher wie eine lokale Phase innerhalb einer weiterhin rekopplungsstarken PAXG-Welt.

## Schlussfolgerung

PAXG 2025 bestätigt im Langfenster:

```text
stabile zentrumsnahe Topologie
mehr offene Variante bei längerer Feldzeit
weiterhin starke Rekopplung
lokale Dämpfungsphasen ohne Topologiebruch
```

Der wichtigste neue Punkt ist die Feldzeit-Tiefe: längere Fenster machen offene Varianten sichtbarer, ohne dass das Feld kollabiert oder in Randdominanz kippt.
