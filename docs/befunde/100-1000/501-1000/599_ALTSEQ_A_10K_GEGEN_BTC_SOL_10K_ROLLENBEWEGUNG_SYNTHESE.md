# Altseq-A-10k gegen BTC/SOL-10k: Rollenbewegungs-Synthese

Stand: 2026-06-21

## Zweck

Diese Synthese vergleicht eine bewusst andere Sequenzklasse (`Altseq-A-10k`) mit der bisherigen BTC/SOL-10k-Rollenbewegung.

Die Auswertung bleibt passiv.
Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Bleibt die MCM-Rollenordnung erhalten, wenn die Weltsequenz anders gebaut ist?
2. Unterpruefung: Bleibt `0e7qvj1` als zentrumsnaher Anker sichtbar?
3. Unterpruefung: Bleibt die gerichtete Asymmetrie `Hinweg rekoppelnd / Rueckweg oeffnend` sichtbar?
4. Folgeschritt: Pruefen, ob eine echte dritte Assetklasse dieselbe Rollenbewegung traegt.

## Datenbasis

Altseq-A-10k:

- `kontrolliert_2023_altseq_a_10k_5m_SOLUSDT.csv`
- `kontrolliert_2024_altseq_a_10k_5m_SOLUSDT.csv`
- `kontrolliert_2025_altseq_a_10k_5m_SOLUSDT.csv`

Vergleichsbasis:

- SOL-10k 2024/2025
- BTC-5m-10k 2024/2025

## Topologie Altseq-A-10k

| Welt | Zentrum | Offen | Rand/Kipp | dominanter Preview-Anker |
|---|---:|---:|---:|---|
| ALTSEQ2023_A_10K | 0.8311 | 0.1557 | 0.0132 | `0e7qvj1` |
| ALTSEQ2024_A_10K | 0.8249 | 0.1667 | 0.0084 | `0e7qvj1` |
| ALTSEQ2025_A_10K | 0.8155 | 0.1757 | 0.0088 | `0e7qvj1` |

Alle drei Altseq-Welten bleiben zentrumsnah.
`0e7qvj1` dominiert weiterhin Zentrum, offene Variante und Rand/Kippnaehe.

## Rollenbewegung Altseq-A-10k

Altseq-A-10k zeigt 160 Bewegungsachsen.

Dominante Rollenwechsel:

| Rollenwechsel | Anzahl |
|---|---:|
| `zentrum_stabil->zentrum_stabil` | 85 |
| `zentrum_stabil->offene_variante` | 24 |
| `offene_variante->zentrum_stabil` | 16 |
| `zentrum_stabil->spannungsrand_kippnaehe` | 13 |
| `offene_variante->offene_variante` | 13 |

Bewegungswirkungen:

| Wirkung | Anzahl |
|---|---:|
| `rekoppelnd_entlastend` | 64 |
| `oeffnend_belastend` | 59 |
| `bewegung_offen` | 23 |
| `spannungsnah` | 14 |

## Gemeinsame Kernachsen

| Bewegung | BTC/SOL-10k | Altseq-A-10k | Lesart |
|---|---:|---:|---|
| `0e7qvj1 -> 1hdpu9s` | 125 Ereignisse, rekoppelnd/entlastend | 49 Ereignisse, rekoppelnd/entlastend | stabile Hinbewegung |
| `1hdpu9s -> 0e7qvj1` | 118 Ereignisse, oeffnend/belastend | 44 Ereignisse, oeffnend/belastend | stabile Rueck-/Oeffnungsbewegung |
| `0e7qvj1 -> 1jwnjz4` | 58 Ereignisse, rekoppelnd/entlastend | 34 Ereignisse, rekoppelnd/entlastend | sekundäre stabile Nachbarschaft |
| `1jwnjz4 -> 0e7qvj1` | 58 Ereignisse, oeffnend/belastend | 29 Ereignisse, oeffnend/belastend | sekundäre Rueck-/Oeffnungsbewegung |

## Arbeitsbefund

Altseq-A-10k bricht die bisherige Topologie nicht.

Der Befund wird dadurch staerker, weil Altseq nicht nur dieselben Einzelzeichen wiederholt, sondern dieselbe gerichtete Rollenlogik zeigt:

```text
vom zentrumsnahen Anker in stabile Nachbarschaft
  eher rekoppelnd / entlastend

Rueckweg oder Oeffnung zum Anker / in offene Variante
  eher oeffnend / belastend
```

Damit wirkt die MCM-Topologie aktuell wie ein Rollenraum mit gerichteten Bewegungen.
Die konkrete Syntaxnachbarschaft kann sich je Welt faerben, aber die Rollenbewegung bleibt wiedererkennbar.

## Was das fuer MINI_DIO bedeutet

Der wichtigste Fortschritt ist nicht nur Reproduktion gleicher Namen.
Der wichtigere Befund ist:

```text
MINI_DIO bildet wiederkehrende Feldbewegungen,
die ueber verschiedene Weltsequenzen eine aehnliche Rolle behalten.
```

Das stuetzt die These einer passiven MCM-Innenordnung:

- Zentrum ist nicht nur ein Punkt, sondern ein Bewegungsanker.
- Offene Variante ist nicht Fehler, sondern Nebenraum / Oeffnungszustand.
- Rand/Kippnaehe bleibt klein, aber lesbar.
- Rekopplung und Belastung sind gerichtete Bewegungsqualitaeten.

## Grenze

Altseq ist eine andere Sequenzklasse, aber weiterhin aus SOL-Daten abgeleitet.
Damit prueft dieser Lauf Sequenzvariation, aber noch keine vollstaendige Assetvariation.

Eine echte Haertepruefung braucht weiterhin:

- laengere KAS-Welt,
- oder eine andere nicht-SOL/BTC-Welt,
- oder eine nicht-marktbasierte synthetische Welt mit kontrollierter Energie-/Rhythmusstruktur.

## Wie es weitergeht

Als naechstes sollte entweder eine laengere KAS-Welt erzeugt werden oder eine nicht-marktbasierte Kontrollwelt gebaut werden. Ziel ist zu pruefen, ob die Rollenbewegung `Zentrum -> stabile Nachbarschaft -> offene Rueckbewegung` auch ausserhalb der bisherigen Marktsequenzen erhalten bleibt.
