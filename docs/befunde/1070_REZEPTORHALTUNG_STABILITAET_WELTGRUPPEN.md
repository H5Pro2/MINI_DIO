# 1070 - Rezeptorhaltung Stabilitaet ueber Weltgruppen

Diese Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Frage

Bleiben die in 1067-1069 gefundenen Rezeptorhaltungen ueber verschiedene Weltgruppen erhalten, oder waren sie nur ein Einzelbefund?

## Methode

- Je Lauf werden Tonband und Rollen weltrelativ bestimmt.
- Geprueft werden zwei Muster:
  - `tragende_verarbeitung`: tonal_mid + zentrum_rekoppelnd.
  - `kippnaehe`: tonal_high + rand_kipp.
- Pro Weltgruppe wird gelesen, ob die erwarteten Achsrichtungen wiederkehren.
- Keine globalen Grenzwerte, keine Handlung, keine Runtime-Regel.

## Weltgruppen-Uebersicht

| Weltgruppe | Muster | Profile | Unterstuetzte Erwartungsachsen | Staerkste Achsen |
|---|---|---:|---:|---|
| feld_5m | kippnaehe | 12 | 1.000 | lautheit=0.2423, rezeptor_hoerkontakt=0.2423, rezeptor_stimulation=0.2423, daempfung=0.1913 |
| feld_5m | tragende_verarbeitung | 12 | 1.000 | visuelle_schaerfe=0.1017, visuelle_distanz=-0.1017, hinhoeren=0.0582, daempfung=-0.0582 |
| real_segment | kippnaehe | 4 | 1.000 | lautheit=0.2392, rezeptor_hoerkontakt=0.2392, rezeptor_stimulation=0.2392, daempfung=0.1899 |
| real_segment | tragende_verarbeitung | 4 | 1.000 | visuelle_distanz=-0.0970, visuelle_schaerfe=0.0970, daempfung=-0.0515, hinhoeren=0.0515 |
| regime | kippnaehe | 6 | 1.000 | lautheit=0.2340, rezeptor_hoerkontakt=0.2340, rezeptor_stimulation=0.2340, daempfung=0.1871 |
| regime | tragende_verarbeitung | 6 | 1.000 | visuelle_schaerfe=0.1059, visuelle_distanz=-0.1059, daempfung=-0.0625, hinhoeren=0.0625 |
| synthetisch | kippnaehe | 30 | 1.000 | lautheit=0.1238, rezeptor_hoerkontakt=0.1238, rezeptor_stimulation=0.1238, daempfung=0.1158 |
| synthetisch | tragende_verarbeitung | 30 | 1.000 | visuelle_schaerfe=0.0228, visuelle_distanz=-0.0228, hinhoeren=0.0132, daempfung=-0.0132 |
| zeit_1h | kippnaehe | 12 | 1.000 | lautheit=0.2503, rezeptor_hoerkontakt=0.2503, rezeptor_stimulation=0.2503, daempfung=0.1962 |
| zeit_1h | tragende_verarbeitung | 12 | 1.000 | visuelle_schaerfe=0.0957, visuelle_distanz=-0.0957, daempfung=-0.0599, hinhoeren=0.0599 |

## Staerkste Einzelachsen

| Weltgruppe | Muster | Achse | Richtung | Delta | Support |
|---|---|---|---:|---:|---:|
| zeit_1h | kippnaehe | lautheit | 1 | 0.250289 | 1.000 |
| zeit_1h | kippnaehe | rezeptor_hoerkontakt | 1 | 0.250289 | 1.000 |
| zeit_1h | kippnaehe | rezeptor_stimulation | 1 | 0.250289 | 1.000 |
| feld_5m | kippnaehe | lautheit | 1 | 0.242252 | 1.000 |
| feld_5m | kippnaehe | rezeptor_hoerkontakt | 1 | 0.242252 | 1.000 |
| feld_5m | kippnaehe | rezeptor_stimulation | 1 | 0.242252 | 1.000 |
| real_segment | kippnaehe | lautheit | 1 | 0.239190 | 1.000 |
| real_segment | kippnaehe | rezeptor_hoerkontakt | 1 | 0.239190 | 1.000 |

## Befund

Die beiden Haltungen bleiben als unterschiedliche Rezeptorstile lesbar:

- Tragende Verarbeitung zeigt eher Schaerfe/Hinhoeren und geringere Rohlast.
- Kippnaehe zeigt eher Lautheit/Stimulation/Feldaufnahme und Distanz.

Die Stabilitaet ist nicht als starres Schema zu lesen. Einzelne Weltgruppen verschieben die Staerke der Achsen, aber die Grundtrennung bleibt passiv sichtbar.

## Schluss

Damit wird die Rezeptorhaltung als eigenstaendige Ebene plausibler: Nicht nur die Weltenergie entscheidet, sondern wie der Organismus sieht, hoert und Aufnahme zulaesst.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob Mini-DIO diese Haltungen als wiederkehrende Innenfeld-Bedeutungen verdichtet oder ob sie nur diagnostische Achsen bleiben.
