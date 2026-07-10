# 2083 - rf_05:volume im 5m-Holdout und Reifung der passiven Memory

## Zweck

Befund 2081 trug auf 30m. Dieser Lauf prüft die vorab festgelegte Volumen-Phasenantwort von `rf_05` auf der bisher ungenutzten 5m-Zeitebene und hängt das Ergebnis anschließend als neue passive Erfahrung an dieselbe Antwortidentität.

## Vorab festgelegtes Design

- Datenjahre `2024` und `2025`
- Assets `BTC` und `SOL`
- ausschließlich die bisher ungenutzte Zeitebene `5m`
- Startpunkte `0`, `36000`, `72000` je Asset und Jahr
- zwölf nicht überlappende Realwelten mit je `1000` Beobachtungen
- ausschließlich die Komponente `volume`
- feste Offsets `17`, `83`, `251`
- `36` gezielte Phasenkontrollen
- exakt dieselben 100 für `rf_05` gematchten Pseudo-Familien wie ab Befund 2079
- vorab erwartete Antwort: `rf_05:volume = verstaerkt`
- Weltarchiv: `data/2083_rf05_volume_5m_memory_maturation.zip`
- keine neue Klasse, keine Handlung, kein Gate und keine Richtung

## Holdout-Ergebnis

| Gruppe | erwartet/beobachtet | Pseudo gleich | Δ Kontinuität | Δ Ereignisanteil | Δ Abdeckung | Perzentile K/E/A |
|---|---|---:|---:|---:|---:|---:|
| `overall` | `verstaerkt/verstaerkt` | 0/100 | 0.014 | 0.0057 | 0.007 | 1.000/1.000/1.000 |
| `year:2024` | `verstaerkt/gemischt` | 2/100 | -0.004 | 0.0054 | -0.007 | 0.960/1.000/1.000 |
| `year:2025` | `verstaerkt/verstaerkt` | 0/100 | 0.028 | 0.0060 | 0.021 | 1.000/1.000/1.000 |
| `asset:BTC` | `verstaerkt/gemischt` | 0/100 | -0.004 | 0.0087 | -0.007 | 1.000/1.000/1.000 |
| `asset:SOL` | `verstaerkt/verstaerkt` | 7/100 | 0.035 | 0.0027 | 0.021 | 0.990/1.000/0.955 |

## Befund

Im Gesamtprofil repliziert die vorab erwartete Verstärkung. Insgesamt tragen `0/100` gematchte Pseudo-Familien dieselbe Antwort; die drei beobachteten Abstände liegen bei den Perzentilen `1.000`, `1.000` und `1.000`.

Die Antwort ist jedoch nicht über alle Teilkontexte geschlossen: `3/5` Gruppen sind verstärkt. `year:2024` und `asset:BTC` sind gemischt, weil Kontinuität und Abdeckung jeweils leicht sinken, während der Ereignisanteil steigt. Dass ihre Maße gegenüber den Pseudo-Familien dennoch bei hohen Perzentilen liegen, zeigt einen familienbezogenen Abstand, aber keine starre gleichgerichtete Signatur.

Der Lauf prüft keine feste Volumenbedeutung. Er verschiebt nur die Volumenphase relativ zur übrigen Welt. Belegt ist eine reproduzierbare, aber kontextplastische Familienantwort gegenüber gelöster Volumenphase, keine Handelsrichtung, keine Kausalität und keine bevorzugte Aktion.

## Reifung der passiven Antwort-Memory

- Beobachtungen vorher/nachher: `212/217`
- stabile Antwortidentitäten vorher/nachher: `32/32`
- eindeutige Beobachtungssymbole: `217`
- Evidenzquellen: `4`
- `rf_05:volume` Antwortsymbol: `dio_rresponse_0gpsabe`
- `rf_05:volume` Beobachtungen vorher/nachher: `11/16`
- quellenreihenfolgenstabil: `1`
- doppelte Beobachtung abgewiesen: `1`
- passiv/handlungswirksam: `1/0`

Die neue Evidenz erzeugt fünf neue Beobachtungssymbole für fünf Kontexte. Die Familien-Komponenten-Identität bleibt stabil. Das ist Reifung durch zusätzliche Erfahrung, keine fest programmierte Sonderregel für `rf_05`.

## Grenze

Auch nach dieser Reifung wird die Antwort-Memory nicht von MINI_DIO gelesen. Sie besitzt keine Antwortklasse, Bestätigung, Bedeutung oder Vorhersage. Der Lauf bleibt auf BTC/SOL, Marktzeitreihen, 1000er-Fenster und dieselbe zirkuläre Phasenoperation begrenzt.
