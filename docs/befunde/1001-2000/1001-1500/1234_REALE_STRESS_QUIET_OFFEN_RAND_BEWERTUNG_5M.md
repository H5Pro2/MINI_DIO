# Reale Stress/Quiet Offen/Rand Bewertung 5m

Stand: 2026-07-01

## Grundfrage

Bleibt die in synthetischen Sinnesachsen sichtbare Offen/Rand-Mechanik auch in realen Stress-/Quiet-Welten erkennbar?

Nach aktueller Sichtung: ja, aber real nicht als reine Einzelachse. In realen Weltspuren koppeln sichtbare Formbewegung und Hoer-/Energiebelastung zusammen.

## Pruefaufbau

Ausgewertet wurden die aktuellen 5m-Rezeptorlaeufe:

- `SOL_QUIET_CURRENT`
- `SOL_STRESS_CURRENT`
- `BTC_QUIET_CURRENT`
- `BTC_STRESS_CURRENT`

Die Chartfenster liegen in:

- `docs/befunde/1001-2000/1001-1500/1233_REALE_STRESS_QUIET_OFFEN_RAND_CHARTFENSTER_5M.md`

Die zugrunde liegenden Rollenwerte stammen aus:

- `docs/befunde/1001-2000/1001-1500/1225_AKTUELLE_REZEPTORSCHICHT_STRESS_QUIET_FELDPHASEN_SEGMENTE.csv`
- `docs/befunde/1001-2000/1001-1500/1225_AKTUELLE_REZEPTORSCHICHT_STRESS_QUIET_FELDPHASEN_TRANSITIONS.csv`

## Rollenqualitaet

Die reale 5m-Pruefung zeigt dieselbe Feldrollenordnung:

```text
Rand/Kipp:
  hohe Rohaufnahme
  hohe Lautheit
  niedrigere Rekopplung
  hoeherer Strain

Zentrum:
  geringe Rohaufnahme
  geringe Lautheit
  hohe Rekopplung
  niedriger Strain
```

Beispielwerte:

```text
BTC_QUIET_CURRENT Rand/Kipp:
  avgRaw 0.4078
  avgLoud 0.7147
  avgRec 0.5827
  avgStrain 0.2834

BTC_QUIET_CURRENT Zentrum:
  avgRaw 0.0904
  avgLoud 0.1487
  avgRec 0.7214
  avgStrain 0.1381
```

## Unterschied zu den synthetischen Welten

In den synthetischen Welten konnte die Kanalwirkung getrennt gelesen werden:

```text
Chaotisches Hoeren -> Rand/Kipp deutlich sichtbar.
Chaotisches Sehen bei stabilem Hoeren -> kaum Rand/Kipp.
```

In realen Weltspuren ist die Lage gekoppelter:

```text
sichtbare Bewegungsform
+ Lautheit/Energie
+ Rekopplungsabfall
+ Strain-Anstieg
= Rand/Kipp-Rolle
```

Das bedeutet: Realer Rand/Kipp ist nicht nur Hoeren und nicht nur Sehen. Er ist multisensorische Feldnaehe.

## Befund aus den Chartfenstern

Die staerksten `Offen -> Rand/Kipp` Fenster liegen oft an echten Bewegungs-/Impulskerzen oder abrupten Bewegungsfortsetzungen.

Die staerksten `Rand/Kipp -> Offen` Fenster liegen haeufig an Bruchstellen, an denen nach hoher Belastung wieder Rekopplung moeglich wird.

Damit wird die Feldphasenlesung plausibler:

```text
Offenheit = Bewegungsraum.
Rand/Kipp = kurzzeitige Spannungsnaehe.
Rueckkehr nach Offenheit = Entlastungs-/Rekopplungsversuch.
```

## Schlussfolgerung

Die synthetische Pruefung war wichtig, weil sie zeigte, dass Hoeren als Feldreizachse stark randbildend wirken kann.

Die reale Pruefung zeigt den naechsten Schritt: In echten Weltspuren wirkt Rand/Kipp multisensorisch. MINI_DIO liest hier nicht nur eine isolierte Achse, sondern eine gekoppelte Feldlage aus Form, Energie, Rezeptoraufnahme und Rekopplung.
