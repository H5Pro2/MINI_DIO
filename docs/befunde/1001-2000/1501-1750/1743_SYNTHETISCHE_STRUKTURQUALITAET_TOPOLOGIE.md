# 1743 Synthetische Strukturqualität und Topologie

Stand: 2026-07-08

## Grundfrage

Bleibt die bisher robuste MCM-Topologie auch dann erhalten, wenn nicht nur andere Assets, sondern gezielt andere Strukturqualitäten geprüft werden?

## Unterprüfung

Geprüft wurden drei kontrollierte Gegenwelten mit frischer Memory:

- synthetische ruhige Drift,
- synthetischer Bruch-/Randkontakt,
- kontrollierte Expansion 2023.

Zum Vergleich wurden zusätzlich die letzten 5m-Langfenster von BTC, DOGE und PAXG mitgelesen.

Die Prüfung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Befund

Alle geprüften Welten bleiben global in der Topologieklasse `stark_zentriert_wenig_rand`.

Die Topologie bricht also nicht, obwohl die Strukturqualität deutlich wechselt. Der Unterschied liegt in der lokalen Feldfärbung:

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| Synth Ruhe/Drift | 1.0000 | 0.0000 | 0.0000 | 0.7570 | 0.6156 | 0.1182 | 0.9189 |
| Synth Bruch/Rand | 0.9994 | 0.0006 | 0.0000 | 0.7507 | 0.6069 | 0.1251 | 0.9090 |
| Kontroll Expansion 2023 | 0.9859 | 0.0141 | 0.0000 | 0.7079 | 0.5537 | 0.1704 | 0.8407 |
| BTC 2025 5m 10k | 0.9902 | 0.0098 | 0.0000 | 0.7075 | 0.5529 | 0.1698 | 0.8424 |
| DOGE 2025 5m 10k | 0.9911 | 0.0089 | 0.0000 | 0.7069 | 0.5526 | 0.1706 | 0.8413 |
| PAXG 2025 5m 10k | 0.8725 | 0.1202 | 0.0073 | 0.7144 | 0.5410 | 0.1517 | 0.8561 |

## Lesart

Die synthetische Ruhe bildet fast eine reine Zentrumslage. Bruch/Rand erzeugt nur eine minimale offene Nebenvariante, bleibt aber stark rekoppelt. Expansion erzeugt deutlich mehr offene Variante, höheren Strain und geringere Sinneskopplung.

Damit entsteht eine präzisere Trennung:

```text
Topologie        = robuste Grundordnung des Feldes.
Strukturqualität = lokale Färbung durch Ruhe, Bruch, Rand oder Expansion.
```

Wichtig ist der Unterschied zwischen globaler und lokaler Lesung:

```text
Global bleibt das Feld zentrumsnah.
Lokal entstehen Randdruckspitzen, offene Varianten und Rekopplungsunterschiede.
```

Die Randdruck-Lupe bestätigt das:

| Welt | Randdruck | Offen | Rekopplung | Dämpfung |
|---|---:|---:|---:|---:|
| Synth Ruhe/Drift | 0.3994 | 0.1509 | 0.2706 | 0.1791 |
| Synth Bruch/Rand | 0.4567 | 0.0997 | 0.3914 | 0.0522 |
| Kontroll Expansion 2023 | 0.4260 | 0.1328 | 0.3387 | 0.1026 |
| BTC 2025 5m 10k | 0.4273 | 0.1350 | 0.3344 | 0.1034 |
| DOGE 2025 5m 10k | 0.4286 | 0.1346 | 0.3343 | 0.1026 |
| PAXG 2025 5m 10k | 0.4372 | 0.1167 | 0.3783 | 0.0678 |

Bruch/Rand zeigt den höchsten lokalen Randdruck, aber zugleich starke Rekopplung. PAXG bleibt im Vergleich offen und rekopplungsnah. Ruhe zeigt die sauberste Zentrumslage.

## Folgeschluss

Die bisherige Topologie wirkt nicht wie ein bloßer Artefakt einer bestimmten Assetwelt. Sie bleibt auch unter kontrollierten Strukturqualitäten erhalten.

Der Mehrwert der neuen Prüfung liegt darin, dass die Unterschiede nicht mehr nur als Assetunterschiede gelesen werden müssen. MINI_DIO zeigt auch auf kontrollierten Weltformen eine stabile Grundordnung mit lokaler Färbung:

```text
Ruhe      -> Zentrum bindet fast vollständig.
Bruch     -> Randdruck entsteht lokal, rekoppelt aber stark.
Expansion -> Offenheit und Strain wachsen sichtbar.
PAXG      -> offene, phasenreichere Feldfärbung.
BTC/DOGE  -> kompaktere zentrumsstabile Feldfärbung.
```

Das stützt die aktuelle MCM-Arbeitshypothese: Das Feld besitzt eine robuste Grundorganisation, während Weltmilieu und Strukturqualität die lokale Ausprägung verändern.

## Verweise

- [synthetische_strukturqualitaet_topology.md](../../../../reports/synthetische_strukturqualitaet_topology.md)
- [synthetische_strukturqualitaet_randdruck.md](../../../../reports/synthetische_strukturqualitaet_randdruck.md)
- [1742_DOGE_BTC_PAXG_LANGFENSTER_MATRIX.md](1742_DOGE_BTC_PAXG_LANGFENSTER_MATRIX.md)
