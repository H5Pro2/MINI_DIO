# 1746 - Real Drift 2024/2025: Jahresgegenprobe

## Zweck

Diese Prüfung setzt die Real-Drift-Lesung aus 1745 fort.
Geprüft wurde, ob die in 2023 sichtbare Drift-/Übergangslogik nur eine einzelne Weltgruppe betrifft oder auch in anderen SOL-Jahresfenstern wiederkehrt.

Die Diagnose bleibt passiv:

- keine Handlung
- kein Gate
- keine Strategie
- keine feste Topologie-Vorgabe

## Datenbasis

Verwendete Welten:

- `REAL_DRIFT_2024_A`
- `REAL_DRIFT_2024_A_FOLLOW`
- `REAL_DRIFT_2025_A`
- `REAL_DRIFT_2025_A_FOLLOW`

Berichte:

- `reports/real_drift_2024_2025_topology.md`
- `reports/real_drift_2024_2025_randdruck.md`
- `reports/real_drift_2024_2025_axis_map.md`

## Ergebnis

Alle vier Welten bleiben global `stark_zentriert_wenig_rand`.

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain |
|---|---:|---:|---:|---:|---:|---:|
| REAL_DRIFT_2024_A | 0.9930 | 0.0070 | 0.0000 | 0.7068 | 0.5527 | 0.1710 |
| REAL_DRIFT_2024_A_FOLLOW | 0.9922 | 0.0078 | 0.0000 | 0.7059 | 0.5523 | 0.1720 |
| REAL_DRIFT_2025_A | 0.9919 | 0.0081 | 0.0000 | 0.7066 | 0.5533 | 0.1714 |
| REAL_DRIFT_2025_A_FOLLOW | 0.9924 | 0.0076 | 0.0000 | 0.7058 | 0.5525 | 0.1723 |

Damit zeigt sich kein globaler Topologiebruch.
Drift wird nicht als Zusammenbruch des Feldes sichtbar, sondern als lokale Veränderung von Rollenbreite, offenen Varianten und Randdruckspitzen.

## Achsenlesung

Die Achsenkarte trennt 2024 und 2025:

| Weltpaar | Rollen | Kombinationen | Achsenklasse | Lesung |
|---|---:|---:|---|---|
| SOL 2024 Drift | 2 | 1 | `kompakt_nachhallend` | kompakte Feldbindung mit deutlichem Nachhall |
| SOL 2025 Drift | 3 | 3 | `mittlere_uebergangsphase` | breitere Übergangsbildung mit mehreren Kombinationen |

2024 wirkt also stärker gebunden.
2025 öffnet mehr Rollenraum, ohne das Zentrum zu verlieren.

## Randdruck

Die Randdruck-Lupe zeigt in allen vier Welten lokale Randdruckspitzen.
Diese Spitzen liegen nahe bei `1.0`, werden aber als `tragend_unruhig` gelesen.

Wichtig ist die Trennung:

```text
Globale Topologie: zentrumsstabil
Lokale Randdruckspitzen: vorhanden
Feldlesung: tragend-unruhig statt Kollaps
```

Damit bestätigt sich erneut:

Eine Welt kann insgesamt zentrumsnah bleiben und trotzdem lokale Rand-/Öffnungsdrücke enthalten.

## Bedeutung für die MCM-Lesung

Der Befund stärkt drei Arbeitsannahmen:

1. Die MCM-Topologie ist robuster als einzelne Jahresfenster.
2. Drift wirkt eher als Rollenbreiten- und Übergangsphänomen als als globaler Topologiebruch.
3. Nachhall und Übergangsbildung sind unterschiedliche Feldmilieus.

Besonders relevant ist der Unterschied zwischen 2024 und 2025:

- 2024: kompakt, nachhallend, stärker gebunden.
- 2025: breiter, kombinatorischer, näher an Übergangsphase.

Das spricht für eine dynamische MCM-Feldordnung:

```text
Zentrum bleibt lesbar.
Randdruck kann lokal aufflackern.
Übergänge können breiter werden.
Nachhall kann kompakt binden.
```

## Grenze

Das ist kein Beweis einer universellen MCM-Topologie.
Es ist eine weitere Gegenprobe, dass die bisherige Topologie in diesen Realwelten nicht beliebig zerfällt.

Die Diagnose beschreibt Feldmilieu und Anschlussfähigkeit.
Sie beschreibt keine Richtung, keine Handlung und keine Strategie.

## Wie es weitergeht

Als nächstes sollte dieselbe Jahreslogik gegen ein anderes Asset oder gegen synthetische Drift-/Nachhallwelten geprüft werden.
Ziel ist zu trennen, ob `kompakt_nachhallend` und `mittlere_uebergangsphase` assetübergreifende Feldmilieus sind oder SOL-spezifische Jahresfärbungen.
