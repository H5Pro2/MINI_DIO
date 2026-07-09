# 819 - Block-K MCM-Uebergangskarte

## Fragestellung

Welche kompakte Rollenkarte entsteht um die Randfamilie `dio_1un4` aus Randfamilie, Ankern, Bruecken, Kontaktzone und stabiler Mitte?

## Rollenuebersicht

| Rolle | Anzahl |
|---|---:|
| beidseitige_bruecke | 5 |
| vorfeldanker | 3 |
| instabile_kontaktzone | 2 |
| randfamilie | 1 |
| offene_kontaktzone | 1 |
| randnahe_unruhe | 1 |

## Karte

| Rolle | Familie | Hits | Vorher | Nachher | Stabil | Unruhe | Strain | Trust | Einbettung | Brueckentyp |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| randfamilie | dio_1un4 | 238 |  |  | 0.0000 | 1.0000 | 0.2250 | 0.6067 | 0.6499 | randspannung |
| vorfeldanker | dio_0l7p | 13 | 13 | 0 | 1.0000 | 0.0000 | 0.1356 | 0.8156 | 0.7823 | stabiler_nachbar |
| vorfeldanker | dio_104t | 13 | 13 | 0 | 0.9854 | 0.0146 | 0.1485 | 0.8391 | 0.7961 | stabiler_nachbar |
| vorfeldanker | dio_14wj | 8 | 8 | 0 | 1.0000 | 0.0000 | 0.1254 | 0.7937 | 0.7708 | stabiler_nachbar |
| beidseitige_bruecke | dio_155c | 14 | 8 | 6 | 0.9809 | 0.0191 | 0.1554 | 0.8172 | 0.7780 | balancierte_bruecke |
| beidseitige_bruecke | dio_17ct | 10 | 1 | 9 | 1.0000 | 0.0000 | 0.1467 | 0.7576 | 0.7419 | balancierte_bruecke |
| beidseitige_bruecke | dio_0h9h | 7 | 5 | 2 | 1.0000 | 0.0000 | 0.1382 | 0.7938 | 0.7656 | balancierte_bruecke |
| beidseitige_bruecke | dio_1mwv | 5 | 1 | 4 | 1.0000 | 0.0000 | 0.1378 | 0.6662 | 0.7001 | balancierte_bruecke |
| beidseitige_bruecke | dio_0obq | 5 | 3 | 2 | 0.9930 | 0.0070 | 0.1554 | 0.7414 | 0.7264 | balancierte_bruecke |
| instabile_kontaktzone | dio_0m9z | 12 | 9 | 3 | 0.7430 | 0.2570 | 0.1639 | 0.8098 | 0.7702 | instabile_kontaktzone |
| instabile_kontaktzone | dio_04uf | 10 | 1 | 9 | 0.4535 | 0.5465 | 0.1655 | 0.7184 | 0.7149 | unbestimmt |
| randnahe_unruhe | dio_05yg | 5 | 0 | 5 | 0.0084 | 0.9916 | 0.1760 | 0.7195 | 0.7113 | randnahe_unruhe |
| offene_kontaktzone | dio_0u2x | 5 | 0 | 5 | 0.5507 | 0.4493 | 0.1753 | 0.5603 | 0.6475 | unbestimmt |

## Befund

Die MCM-Uebergangskarte zeigt keine flache Wolke. Um die Randfamilie entsteht eine gegliederte Rollenordnung:

- eine randnahe Spannungsfamilie als Ausgangspunkt,
- stabile Vorfeldanker, die vor der Randspannung haeufig auftreten,
- beidseitige Bruecken, die Randnaehe beruehren und stabil bleiben,
- instabile Kontaktzonen, die zwischen stabil und unruhig mischen,
- offene Folgezonen und weitere Randunruhe als Anschlussbereiche.

Damit wirkt das Feld topologisch gegliedert: Rand, Kontakt, Bruecke und stabile Umgebung sind passiv unterscheidbar.

## Grenze

Die Karte ist eine passive Innenfeldkarte. Sie ist keine Handlungskarte, keine Strategie und keine Richtungsvorhersage.

## Wie es weitergeht

Als naechstes sollte diese Karte gegen eine zweite Randfamilie geprueft werden. Nur dann sehen wir, ob die Rollenordnung allgemein ist oder spezifisch um `dio_1un4` entsteht.
