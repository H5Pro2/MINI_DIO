# 1832 - Asset 10k Nullwelt Differenzreport

Stand: 2026-07-08 22:28:06

## Grundfrage

Unterscheiden sich reale Weltspuren und Nullwelten bei gleicher Rueckfuehrungsdaempfung nur in der Topologieklasse, oder in tieferen Merkmalen wie Bedeutungsbreite, adaptiver Rekopplung, Nachhall und Rollenvarianz?

## Grundlage

- Summenquelle: `docs/befunde/1831_DAEMPFUNG_ASSET10K_NULLWELTEN.csv`
- Episodenquelle: `debug/1831_damping_asset10k_null`
- Gruppen: `realwelt` = BTC, DOGE, PAXG und XRP 2025 5m 10k, `nullwelt` = Shuffle/Random

## Gruppenmittel

| Faktor | Gruppe | Welten | Symbole | Familien | Rekopplung | Adaptive Rekopplung | Nachhall | Rollen-Entropie | Milieu-Entropie | Strain |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.3000 | nullwelt | 2.0000 | 222.5000 | 221.5000 | 0.2123 | 0.6821 | 0.5109 | 0.0660 | 1.4547 | 0.1587 |
| 0.3000 | realwelt | 4.0000 | 648.0000 | 644.5000 | 0.2129 | 0.7454 | 0.6656 | 0.1690 | 1.5432 | 0.1689 |
| 0.5000 | nullwelt | 2.0000 | 222.5000 | 221.5000 | 0.3538 | 0.6459 | 0.5109 | 0.0053 | 0.8273 | 0.1587 |
| 0.5000 | realwelt | 4.0000 | 648.0000 | 644.5000 | 0.3549 | 0.7430 | 0.6656 | 0.0943 | 1.3356 | 0.1689 |
| 1.0000 | nullwelt | 2.0000 | 222.5000 | 221.5000 | 0.7076 | 0.7126 | 0.5109 | 0.0000 | 0.5949 | 0.1587 |
| 1.0000 | realwelt | 4.0000 | 648.0000 | 644.5000 | 0.7098 | 0.7450 | 0.6656 | 0.0683 | 1.3707 | 0.1689 |

## Differenz Realwelt minus Nullwelt

| Faktor | Delta Symbole | Delta Familien | Delta adaptive Rekopplung | Delta Nachhall | Delta Rollen-Entropie | Delta Milieu-Entropie | Delta Strain |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.3000 | 425.5000 | 423.0000 | 0.0632 | 0.1547 | 0.1030 | 0.0885 | 0.0102 |
| 0.5000 | 425.5000 | 423.0000 | 0.0971 | 0.1547 | 0.0890 | 0.5082 | 0.0102 |
| 1.0000 | 425.5000 | 423.0000 | 0.0324 | 0.1547 | 0.0683 | 0.7758 | 0.0102 |

## Lesung

Die dominante Feldklasse allein trennt reale Welt und Nullwelt nicht sauber, weil beide Gruppen unter Rueckfuehrungsdaempfung stabil bleiben koennen.

Die Trennung liegt tiefer:

- reale Welten tragen deutlich mehr Symbole und Episodenfamilien,
- reale Assetwelten halten die adaptive Rekopplung hoeher,
- reale Assetwelten tragen mehr Nachhall als Nullwelten,
- reale Assetwelten zeigen mehr Rollen- und Milieuvarianz,
- Nullwelten bleiben schmaler und adaptiv variabler,
- Strain bleibt als Einzelwert nicht ausreichend trennscharf.

Damit wird die Feldordnung nicht als einfacher Stabil/Kollaps-Schalter sichtbar, sondern als Bedeutungsbreite plus Rueckfuehrungsqualitaet plus Rollenvarianz. Gegenueber dem kurzen erweiterten Kontrolltest ist hier wichtig: In langen Assetfenstern ist auch der Nachhall auf der Realweltseite hoeher. Das spricht dafuer, dass Nachhall nur zusammen mit Feldzeit und Bedeutungsbreite sinnvoll gelesen werden darf.

## Grenze

Der Report vergleicht vier 10k-Assetwelten gegen zwei synthetische Nullwelten. Fuer eine belastbarere Aussage muessen weitere Jahre, Zeitachsen und Nullweltvarianten gelesen werden.

## Wie es weitergeht

Als naechstes sollte dieselbe Asset-10k-Logik auf 2024 wiederholt werden. Entscheidend ist, ob Bedeutungsbreite, adaptive Rekopplung und Nachhall auch jahruebergreifend Realwelt und Nullwelt trennen.
