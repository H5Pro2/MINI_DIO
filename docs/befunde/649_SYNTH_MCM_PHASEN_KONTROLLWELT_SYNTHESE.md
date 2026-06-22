# Synthetische MCM-Phasenwelt - Kontrollbefund

Stand: 2026-06-22

## Zweck

Diese Synthese prüft eine nicht-marktbasierte Kontrollwelt.

Die Welt wurde künstlich als OHLCV-Sequenz erzeugt, aber nicht aus einem realen Asset geladen. Sie enthält kontrollierte Phasen:

```text
ruhig -> expansion -> unruhe -> kippnaehe -> rekopplung -> ruhe_rueckkehr
```

Die Auswertung bleibt passiv. Es wird keine Handlung, kein Gate und keine Strategie erzeugt.

## Hierarchie

1. Grundfrage: Bildet MINI_DIO auch ohne reale Marktstruktur eine MCM-Rollenordnung?
2. Unterprüfung: Bleibt die Rollenordnung bei gleicher Phasenwelt und anderem Preismaßstab reproduzierbar?
3. Unterprüfung: Entsteht Varianz oder bleibt die synthetische Welt zu harmonisch?
4. Folgeschritt: Eine zweite synthetische Welt mit stärkerer Bruch-, Rand- und Rekopplungsstruktur erzeugen.

## Daten

Zwei Kontrollwelten wurden erzeugt:

- `data/kontrolliert_synthetic_mcm_phasen_a_5m.csv`
- `data/kontrolliert_synthetic_mcm_phasen_b_5m.csv`

Beide haben dieselbe Phasenlogik und 5400 Zeilen. Der Startpreis wurde unterschiedlich gesetzt, um zu prüfen, ob die Lesung am Preismaßstab hängt.

## Laufbefund

| Welt | Rekopplung | Carry | Sinnes-MCM-Kopplung | Unique Syntax | Stabil | Tragend unruhig | Kippend |
|---|---:|---:|---:|---:|---:|---:|---:|
| SYNTH_A | 0.7568 | 0.6170 | 0.9168 | 42 | 5389 | 4 | 1 |
| SYNTH_B | 0.7568 | 0.6170 | 0.9168 | 42 | 5389 | 4 | 1 |

Die beiden Welten sind in den Kernwerten identisch. Auch die Top-Syntax- und Top-Familien-Überlappung liegt bei `1.0`.

## Topologie

| Welt | Zentrum | Offen | Rand/Kipp | Topologiezustand |
|---|---:|---:|---:|---|
| SYNTH_A | 0.9991 | 0.0007 | 0.0002 | `stark_zentriert_wenig_rand` |
| SYNTH_B | 0.9991 | 0.0007 | 0.0002 | `stark_zentriert_wenig_rand` |

Die synthetische Welt erzeugt damit keine Topologieauflösung. Sie erzeugt eine extrem zentrumsnahe Innenfeldordnung.

## Feldbewegung

Die Feldbewegungs-Memory findet nur 14 dominante Bewegungsräume.

Davon ist der größte Teil:

```text
recurrently_reconnecting
```

Nur wenige Bewegungen erscheinen als:

```text
recurrently_opening_strain
world_specific
```

Die Bewegung bleibt also überwiegend rekoppelnd und entlastend.

## Arbeitsbefund

Die synthetische Kontrollwelt ist ein positiver Kontrollfall:

```text
Wenn die Außenwelt künstlich harmonisch und phasenstabil ist,
liest MINI_DIO sie nicht als rauschende Assetwelt,
sondern als stark zentrumsnahe MCM-Feldordnung.
```

Das spricht dafür, dass MINI_DIO nicht einfach immer dieselbe Assettopologie produziert. Die Weltqualität färbt das Innenfeld deutlich:

- reale Assetwelten erzeugen mehr offene Variante, Übergang und Randnähe,
- die synthetische Phasenwelt erzeugt fast reine Zentrum-Stabilität.

## Grenze

Diese Kontrollwelt ist bewusst zu glatt.

Sie prüft Reproduzierbarkeit und Maßstabsrobustheit, aber noch nicht die Fähigkeit, aus künstlicher Bruch-/Randstruktur eine differenzierte MCM-Topologie zu bilden.

Der Befund ist deshalb nicht:

```text
MINI_DIO kann jede synthetische Welt tief lesen.
```

Sondern:

```text
MINI_DIO erkennt eine harmonische synthetische Phasenwelt als fast vollständig zentrumsnah.
```

## Wie es weitergeht

Als nächstes sollte eine zweite synthetische Kontrollwelt gebaut werden, die gezielt stärkere Brüche enthält: echte Randphase, instabile Öffnung, laute Frequenzspitzen und anschließende Rekopplung. Dann kann geprüft werden, ob MINI_DIO nicht nur Harmonie stabilisiert, sondern künstlich erzeugte Kippnähe und Rückbindung getrennt lesen kann.
