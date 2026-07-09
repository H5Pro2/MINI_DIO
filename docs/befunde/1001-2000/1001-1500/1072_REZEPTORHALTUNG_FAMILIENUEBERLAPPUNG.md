# 1072 - Rezeptorhaltung Familienueberlappung

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Bleiben `tragende_verarbeitung` und `kippnaehe` in Mini-DIOs Symbolfamilien getrennt, oder gibt es Familien, die beide Rollen ueberbruecken?

## Weltgruppen

| Weltgruppe | Tragend Episoden | Kipp Episoden | Geteilte Familien | Familien gesamt | Jaccard | Tragend Rekopplung | Kipp Rekopplung | Tragend Strain | Kipp Strain |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| feld_5m | 10928 | 9975 | 28 | 681 | 0.0411 | 0.7351 | 0.6585 | 0.1205 | 0.1996 |
| real_segment | 1103 | 1099 | 7 | 304 | 0.0230 | 0.7251 | 0.6438 | 0.1219 | 0.2075 |
| regime | 9138 | 8626 | 19 | 680 | 0.0279 | 0.7327 | 0.6584 | 0.1212 | 0.1999 |
| synthetisch | 28820 | 16648 | 4 | 281 | 0.0142 | 0.7619 | 0.7116 | 0.1177 | 0.1486 |
| zeit_1h | 9710 | 9458 | 25 | 707 | 0.0354 | 0.7322 | 0.6546 | 0.1218 | 0.2025 |

## Staerkste Brueckenfamilien

| Weltgruppe | Familie | Tragend Anteil | Kipp Anteil | Brueckenwert | Tragend Count | Kipp Count |
|---|---|---:|---:|---:|---:|---:|
| synthetisch | dio_1fll | 0.9722 | 0.0483 | 0.0483 | 28019 | 804 |
| synthetisch | dio_0g3b | 0.0269 | 0.0102 | 0.0102 | 774 | 169 |
| real_segment | dio_0g2r | 0.0036 | 0.0036 | 0.0036 | 4 | 4 |
| feld_5m | dio_17ct | 0.0018 | 0.0023 | 0.0018 | 20 | 23 |
| real_segment | dio_1ewh | 0.0073 | 0.0018 | 0.0018 | 8 | 2 |
| real_segment | dio_0z3k | 0.0018 | 0.0018 | 0.0018 | 2 | 2 |
| real_segment | dio_155c | 0.0018 | 0.0018 | 0.0018 | 2 | 2 |
| real_segment | dio_17ct | 0.0018 | 0.0036 | 0.0018 | 2 | 4 |
| real_segment | dio_1gp2 | 0.0018 | 0.0055 | 0.0018 | 2 | 6 |
| zeit_1h | dio_1ewh | 0.0065 | 0.0017 | 0.0017 | 63 | 16 |
| regime | dio_17ct | 0.0020 | 0.0015 | 0.0015 | 18 | 13 |
| zeit_1h | dio_1gp2 | 0.0019 | 0.0015 | 0.0015 | 18 | 14 |

## Befund

Die Haltungen sind nicht vollstaendig getrennt. Es gibt geteilte Symbolfamilien, aber ihre Brueckenstaerke unterscheidet sich je nach Weltgruppe deutlich.

Das spricht fuer eine innere Semantik, die nicht nur zwei feste Klassen bildet. Einzelne Familien koennen als Uebergangstraeger wirken: dieselbe Familie kann in tragender Verarbeitung und in Kippnaehe erscheinen, aber mit anderer Feldqualitaet.

## Schluss

Mini-DIO zeigt hier keine simple Wenn-Dann-Trennung. Die Symbolfamilien bilden eher ein Feldnetz: getrennte Bereiche plus Brueckenfamilien.

## Wie es weitergeht

Als naechstes sollte eine starke Brueckenfamilie isoliert und gegen Rohweltfenster gelesen werden: Welche Weltabschnitte lassen dieselbe Familie tragend oder kippnah erscheinen?
