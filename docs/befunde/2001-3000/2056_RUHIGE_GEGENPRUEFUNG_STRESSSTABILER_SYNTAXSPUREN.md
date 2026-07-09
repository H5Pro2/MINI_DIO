# 2056 - Ruhige Gegenprüfung stressstabiler Syntaxspuren

## Zweck

Diese Auswertung nimmt nur die unter Stress weltübergreifend stabilen Spuren aus 2054 und prüft sie gegen ruhige oder seitwärts laufende Welten aus 2055.

Die Prüfung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung, kein Gate und keine motorische Kopplung.

## Grundfrage

Sind die stressstabilen Spuren allgemeine Feldrollen, oder werden sie hauptsächlich durch belastete Außenwelt aktiviert?

## Übersicht

- geprüfte stressstabile Spuren: `4`
- Statusverteilung: `{'allgemeine_feldrolle': 1, 'ruhig_jung_wiedergefunden': 3}`

## Statusklassen

| quiet_status | families | quiet_fields | max_quiet_events |
| --- | --- | --- | --- |
| allgemeine_feldrolle | 1 | tragende_rekopplung:1 | 11 |
| ruhig_jung_wiedergefunden | 3 | tragende_rekopplung:3 | 8 |

## Detail

| symbol_family | quiet_status | stress_field | stress_events | quiet_events | quiet_labels | quiet_field | quiet_reifung | quiet_mcm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dio_17j2 | allgemeine_feldrolle | tragende_rekopplung | 15 | 11 | adapted_sideways:1;btc_quiet:1;sol_quiet:1 | tragende_rekopplung | weltuebergreifend_feldstabil | 0.462/0.150/0.681 |
| dio_0e70 | ruhig_jung_wiedergefunden | offene_rekopplung | 10 | 8 | adapted_sideways:2;btc_quiet:1;sol_quiet:1 | tragende_rekopplung | weltuebergreifend_feldoffen | 0.394/0.220/0.627 |
| dio_18d9 | ruhig_jung_wiedergefunden | tragende_rekopplung | 5 | 6 | adapted_sideways:1 | tragende_rekopplung | junge_syntaxinsel | 0.464/0.181/0.667 |
| dio_0qzh | ruhig_jung_wiedergefunden | tragende_rekopplung | 5 | 2 | adapted_sideways:1 | tragende_rekopplung | junge_syntaxinsel | 0.410/0.196/0.645 |

## Interpretation

- Wenn eine Spur auch in ruhigen Welten feldnah bleibt, ist sie eher eine allgemeine Feldrolle.
- Wenn sie in ruhigen Welten nicht wieder auftaucht, wirkt sie eher stressspezifisch.
- Wenn sie ruhig verschoben wieder auftaucht, spricht das für eine Feldrolle, deren Bedeutung von Weltspannung moduliert wird.

## Bedeutung für MINI_DIO

Die Gegenprüfung verhindert, dass Stressrobustheit automatisch als allgemeine Reife gelesen wird. MINI_DIO kann damit später zwischen Grundrolle, Stressrolle und situativer Aktivierung unterscheiden.
