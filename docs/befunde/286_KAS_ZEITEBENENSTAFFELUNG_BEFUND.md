# Befund 286 - KASUSDT-Zeitebenenstaffelung

## Fragestellung

Geprüft wurde, ob MINI_DIO bei einer Kleinpreis-Welt wie KASUSDT seine Innenfeldordnung über mehrere Zeitebenen stabil hält oder ob eine bestimmte Zeitebene eine andere Topologie erzwingt.

Getestete Welten:

- KASUSDT 5m, 2000 Zeilen
- KASUSDT 15m, 2000 Zeilen
- KASUSDT 30m, 2000 Zeilen
- KASUSDT 1h, 2000 Zeilen

Alle Läufe wurden mit `sense-mode=world_relative` ausgeführt.

## Ergebnis

Alle vier Zeitebenen bleiben in derselben groben Feldklasse:

`zentrum_mit_rand_und_uebergang`

Die gemessenen Werte:

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| KAS_2024_5M_2K | 0.8004 | 0.1575 | 0.0421 | 0.6451 | 0.3963 | 0.1869 | 0.8645 |
| KAS_2024_15M_2K | 0.8004 | 0.1545 | 0.0451 | 0.6455 | 0.3964 | 0.1863 | 0.8641 |
| KAS_2024_30M_2K | 0.7894 | 0.1680 | 0.0426 | 0.6451 | 0.3959 | 0.1866 | 0.8640 |
| KAS_2024_1H_2K | 0.7984 | 0.1560 | 0.0456 | 0.6445 | 0.3940 | 0.1865 | 0.8639 |

## Interpretation

Die Zeitebene verändert die Gewichtung, aber nicht die Grundtopologie.

Die 30m-Welt ist in dieser Messung am offensten:

- niedrigster Zentrum-Anteil: `0.7894`
- höchster Offen-Anteil: `0.1680`

Das wirkt wie eine lokale Zeitskalenantwort, nicht wie ein vollständiger Topologiebruch.

Wichtig ist: Rekopplung, Carry, Strain und Sinneskopplung bleiben über alle KAS-Zeitebenen sehr eng beieinander. Das spricht dafür, dass MINI_DIO die Kleinpreis-Welt nicht roh preisabhängig liest, sondern über eine relativ stabile Innenfeldkopplung verarbeitet.

## Fachliche Grenze

Das ist noch kein allgemeiner Nachweis einer universellen Zeitfeld-Topologie.

Der Befund gilt zunächst für:

- KASUSDT Futures-UM Daten
- Jahr 2024
- 2000 Zeilen je Zeitebene
- eine Messreihe mit frischer Memory je Lauf

Für eine stabilere Aussage braucht es Reproduktion und danach den Vergleich gegen SOL/BTC in denselben Zeitebenen.

## Bedeutung für MINI_DIO

MINI_DIO zeigt hier eine robuste Weltaufnahme über unterschiedliche zeitliche Auflösungen.

Das unterstützt die aktuelle Richtung:

- keine rohe Preisgrößenabhängigkeit
- keine harte 5m-Spezialisierung
- keine sofortige Topologiezerstörung durch andere Zeitebenen
- stattdessen eine feldbezogene Anpassung der Innenordnung

Die Zeitebene wirkt damit nicht als externe Regel, sondern als veränderte Weltspannung, auf die das MCM-Feld unterschiedlich, aber geordnet reagiert.

## Wie es weitergeht

Als nächstes sollte die KAS-15m/30m/1h-Staffelung reproduziert werden. Wenn die Deltas stabil bleiben, folgt der direkte Zeitebenenvergleich KAS/SOL/BTC.
