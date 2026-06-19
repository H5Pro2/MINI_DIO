# Befund 302 - Rekopplung nach Öffnung

Stand: 2026-06-19

## Zweck

Dieser Befund prüft, was nach einer offenen Episode passiert.

Grundfrage:

Ist `offene_variante` ein instabiler Zustand, der häufig kippt, oder ein temporärer Innenfeldzustand, der wieder ins Zentrum zurückgeführt wird?

Konkrete Unterprüfung:

Für jede offene Episode wurde der Folgebereich von acht Episoden gelesen:

- Rückkehr in `zentrum_stabil`
- Offenbleiben als `offene_variante`
- Kippen in `spannungsrand_kippnaehe`

## Datengrundlage

Erzeugte Dateien:

- `docs/befunde/300_REKOPPLUNG_NACH_OEFFNUNG_MATRIX.csv`
- `docs/befunde/301_REKOPPLUNG_NACH_OEFFNUNG_EVENTS.csv`

Geprüft wurden alle offenen Episoden aus den 12 Asset-/Zeitebenen-Welten.

## Gesamtergebnis

Gesamt über alle Welten:

- `rekoppelt_zentrum`: 3162 Fälle
- `bleibt_offen`: 261 Fälle
- `kippt_rand`: 61 Fälle

Die offene Variante führt also meistens zurück in eine zentrumsnahe Ordnung.

## Weltvergleich

| Welt | offene Episoden | Zentrum danach | Offen danach | Rand/Kipp danach |
|---|---:|---:|---:|---:|
| KAS_2024_5M_2K | 313 | 0.9169 | 0.0735 | 0.0096 |
| KAS_2024_15M_2K | 306 | 0.8987 | 0.0817 | 0.0196 |
| KAS_2024_30M_2K | 335 | 0.8507 | 0.1194 | 0.0299 |
| KAS_2024_1H_2K | 311 | 0.9293 | 0.0643 | 0.0064 |
| SOL_2024_5M_2K | 286 | 0.9650 | 0.0280 | 0.0070 |
| SOL_2024_15M_2K | 297 | 0.9024 | 0.0909 | 0.0067 |
| SOL_2024_30M_2K | 319 | 0.9216 | 0.0627 | 0.0157 |
| SOL_2024_1H_2K | 301 | 0.9070 | 0.0831 | 0.0100 |
| BTC_2024_5M_2K | 263 | 0.9202 | 0.0570 | 0.0228 |
| BTC_2024_15M_2K | 222 | 0.8784 | 0.0721 | 0.0495 |
| BTC_2024_30M_2K | 255 | 0.8980 | 0.0863 | 0.0157 |
| BTC_2024_1H_2K | 276 | 0.9022 | 0.0725 | 0.0254 |

## Interpretation

Die offene Variante ist in dieser Prüfung kein dominanter Kollapszustand.

Sie wirkt eher wie ein temporärer Innenfeldzustand:

1. Eine Weltspannung öffnet das Feld.
2. Das Feld hält diese Offenheit kurz.
3. In den meisten Fällen erfolgt Rückkopplung in zentrumsnahe Ordnung.

KAS 30m bleibt am häufigsten offen. Das passt zur bisherigen Beobachtung, dass KAS und SOL bei 30m eine stärkere Öffnung zeigen.

BTC 15m kippt relativ am häufigsten in den Rand. Das macht BTC 15m in dieser Prüfung zu einer interessanten Stress-/Randwelt, obwohl BTC insgesamt zentrumsnäher wirkt.

## Bedeutung für die MCM-Forschung

Dieser Befund stützt die Annahme einer passiven Eigenregulation im MCM-Feld.

Die Regulation wurde hier nicht als harte Regel programmiert. Gelesen wurde nur, was nach offenen Episoden geschieht.

Der Befund:

Offenheit bedeutet nicht automatisch Zerfall. In der Mehrzahl der Fälle entsteht eine Rückführung in zentrumsnahe Ordnung.

Das passt zur Arbeitshypothese:

Das MCM-Feld kann Spannung aufnehmen, öffnen und anschließend wieder in eine tragendere Innenlage rekoppeln.

## Grenze des Befunds

Der Folgebereich von acht Episoden ist eine diagnostische Wahl.

Der Befund zeigt eine lokale Rückführungsdynamik in den geprüften Welten. Er sagt noch nicht, ob dieselbe Dynamik bei allen Datenlängen, Assets und Regimes gleich bleibt.

## Wie es weitergeht

Als nächstes prüfen wir die Randfälle: Welche Welt- und Sinnesbedingungen führen dazu, dass eine offene Episode nicht rekoppelt, sondern offen bleibt oder in den Spannungsrand kippt?
