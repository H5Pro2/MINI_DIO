# 1828 - Differenzreport: reale Weltordnung gegen Nullwelt

Stand: 2026-07-08 22:14:43

## Grundfrage

Unterscheiden sich reale Weltspuren und Nullwelten bei gleicher Rueckfuehrungsdaempfung nur in der Topologieklasse, oder in tieferen Merkmalen wie Bedeutungsbreite, adaptiver Rekopplung, Nachhall und Rollenvarianz?

## Grundlage

- Summenquelle: `docs/befunde/1001-2000/1751-2000/1827_RUECKFUEHRUNG_DAEMPFUNG_STRESS_NULL.csv`
- Episodenquelle: `debug/1827_rekopplung_damping_stress_null`
- Gruppen: `realwelt` = Stress/Expansion, `nullwelt` = Shuffle/Random

## Gruppenmittel

| Faktor | Gruppe | Welten | Symbole | Familien | Rekopplung | Adaptive Rekopplung | Nachhall | Rollen-Entropie | Milieu-Entropie | Strain |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.3000 | nullwelt | 2.0000 | 222.5000 | 221.5000 | 0.2123 | 0.6821 | 0.5109 | 0.0660 | 1.4547 | 0.1587 |
| 0.3000 | realwelt | 2.0000 | 654.5000 | 651.0000 | 0.2122 | 0.7425 | 0.6617 | 0.1869 | 1.5532 | 0.1708 |
| 0.5000 | nullwelt | 2.0000 | 222.5000 | 221.5000 | 0.3538 | 0.6459 | 0.5109 | 0.0053 | 0.8273 | 0.1587 |
| 0.5000 | realwelt | 2.0000 | 654.5000 | 651.0000 | 0.3537 | 0.7411 | 0.6617 | 0.1138 | 1.4115 | 0.1708 |
| 1.0000 | nullwelt | 2.0000 | 222.5000 | 221.5000 | 0.7076 | 0.7126 | 0.5109 | 0.0000 | 0.5949 | 0.1587 |
| 1.0000 | realwelt | 2.0000 | 654.5000 | 651.0000 | 0.7073 | 0.7425 | 0.6617 | 0.0814 | 1.3854 | 0.1708 |

## Differenz Realwelt minus Nullwelt

| Faktor | Delta Symbole | Delta Familien | Delta adaptive Rekopplung | Delta Nachhall | Delta Rollen-Entropie | Delta Milieu-Entropie | Delta Strain |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.3000 | 432.0000 | 429.5000 | 0.0604 | 0.1507 | 0.1209 | 0.0985 | 0.0121 |
| 0.5000 | 432.0000 | 429.5000 | 0.0952 | 0.1507 | 0.1085 | 0.5842 | 0.0121 |
| 1.0000 | 432.0000 | 429.5000 | 0.0299 | 0.1507 | 0.0814 | 0.7905 | 0.0121 |

## Lesung

Die dominante Feldklasse allein trennt reale Welt und Nullwelt nicht sauber, weil beide Gruppen unter Rueckfuehrungsdaempfung stabil bleiben koennen.

Die Trennung liegt tiefer:

- reale Welten tragen deutlich mehr Symbole und Episodenfamilien,
- reale Welten halten die adaptive Rekopplung stabiler,
- Nullwelten bleiben schmaler und zeigen eine variablere adaptive Rueckfuehrung,
- Strain bleibt als Einzelwert nicht ausreichend trennscharf.

Damit wird die Feldordnung nicht als einfacher Stabil/Kollaps-Schalter sichtbar, sondern als Bedeutungsbreite plus Rueckfuehrungsqualitaet. Das ist methodisch wichtig, weil es die Pareidolie-Gegenfrage schaerfer macht: Nicht jede stabile Klasse ist automatisch gleiche Bedeutung.

## Grenze

Der Report vergleicht nur die 1827-Welten. Fuer eine belastbarere Aussage muessen weitere reale und synthetische Welten mit derselben Differenzlogik gelesen werden.
