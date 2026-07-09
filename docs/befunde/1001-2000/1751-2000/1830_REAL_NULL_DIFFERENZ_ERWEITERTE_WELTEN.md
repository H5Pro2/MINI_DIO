# 1830 - Real Null Differenz Erweiterte Welten

Stand: 2026-07-08 22:19:27

## Grundfrage

Unterscheiden sich reale Weltspuren und Nullwelten bei gleicher Rueckfuehrungsdaempfung nur in der Topologieklasse, oder in tieferen Merkmalen wie Bedeutungsbreite, adaptiver Rekopplung, Nachhall und Rollenvarianz?

## Grundlage

- Summenquelle: `docs/befunde/1001-2000/1751-2000/1829_DAEMPFUNG_REAL_NULL_ERWEITERTE_WELTEN.csv`
- Episodenquelle: `debug/1829_damping_real_null_extended`
- Gruppen: `realwelt` = Ruhe, Seitwaerts, Stress und Expansion, `nullwelt` = Shuffle/Random

## Gruppenmittel

| Faktor | Gruppe | Welten | Symbole | Familien | Rekopplung | Adaptive Rekopplung | Nachhall | Rollen-Entropie | Milieu-Entropie | Strain |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.3000 | nullwelt | 2.0000 | 222.5000 | 221.5000 | 0.2123 | 0.6821 | 0.5109 | 0.0660 | 1.4547 | 0.1587 |
| 0.3000 | realwelt | 4.0000 | 347.2500 | 345.2500 | 0.2088 | 0.7324 | 0.4190 | 0.2434 | 1.4582 | 0.1659 |
| 0.5000 | nullwelt | 2.0000 | 222.5000 | 221.5000 | 0.3538 | 0.6459 | 0.5109 | 0.0053 | 0.8273 | 0.1587 |
| 0.5000 | realwelt | 4.0000 | 347.2500 | 345.2500 | 0.3479 | 0.7278 | 0.4190 | 0.1541 | 1.4012 | 0.1659 |
| 1.0000 | nullwelt | 2.0000 | 222.5000 | 221.5000 | 0.7076 | 0.7126 | 0.5109 | 0.0000 | 0.5949 | 0.1587 |
| 1.0000 | realwelt | 4.0000 | 347.2500 | 345.2500 | 0.6959 | 0.7355 | 0.4190 | 0.1048 | 1.4324 | 0.1659 |

## Differenz Realwelt minus Nullwelt

| Faktor | Delta Symbole | Delta Familien | Delta adaptive Rekopplung | Delta Nachhall | Delta Rollen-Entropie | Delta Milieu-Entropie | Delta Strain |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.3000 | 124.7500 | 123.7500 | 0.0503 | -0.0920 | 0.1774 | 0.0036 | 0.0073 |
| 0.5000 | 124.7500 | 123.7500 | 0.0819 | -0.0920 | 0.1488 | 0.5739 | 0.0073 |
| 1.0000 | 124.7500 | 123.7500 | 0.0229 | -0.0920 | 0.1048 | 0.8375 | 0.0073 |

## Lesung

Die dominante Feldklasse allein trennt reale Welt und Nullwelt nicht sauber, weil beide Gruppen unter Rueckfuehrungsdaempfung stabil bleiben koennen.

Die Trennung liegt tiefer:

- reale Welten tragen deutlich mehr Symbole und Episodenfamilien,
- reale Welten halten die adaptive Rekopplung im Mittel hoeher,
- reale Welten zeigen mehr Rollen-Entropie,
- Nullwelten bleiben schmaler und zeigen in dieser Pruefung sogar hoeheren Nachhall,
- Strain bleibt als Einzelwert nicht ausreichend trennscharf.

Damit wird die Feldordnung nicht als einfacher Stabil/Kollaps-Schalter sichtbar, sondern als Bedeutungsbreite plus Rueckfuehrungsqualitaet plus Rollenvarianz. Der negative Nachhall-Delta ist wichtig: Nachhall allein bedeutet nicht automatisch bessere Weltordnung. In Nullwelten kann Nachhall als ungerichtete Restspur staerker erscheinen, waehrend reale Welten trotzdem mehr Bedeutung und mehr Rollenvarianz tragen.

## Grenze

Der Report vergleicht kurze erweiterte Kontrollwelten. Fuer eine belastbarere Aussage muessen laengere und assetgetrennte Welten mit derselben Differenzlogik gelesen werden.

## Wie es weitergeht

Als naechstes sollte diese Differenzlogik auf laengere Assetfenster angewendet werden. Entscheidend ist, ob Bedeutungsbreite und adaptive Rekopplung auch bei groesserer Feldzeit besser trennen als die dominante Feldklasse.
