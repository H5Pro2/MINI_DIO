# 1750 - XRP/DOGE 2025 Teilfenster-Mehrrollenprüfung

Stand: 2026-07-08

## Zweck

Nach der XRP-2025-Rohwelt-Lupe sollte geprüft werden, ob die `mittlere_uebergangsphase` aus wenigen lokalen XRP-Segmenten entsteht oder über das gesamte Fenster verteilt getragen wird.

Geprüft wurden:

- XRP 2025 Startfenster,
- XRP 2025 Folgefenster,
- DOGE 2025 Startfenster,
- DOGE 2025 Folgefenster.

Jede Welt wurde in 1000er-Teilfenster zerlegt.

## Ergebnis

Die Teilfensterprüfung zeigt:

| Klasse | Anzahl |
|---|---:|
| `mehrrollen_kandidat` | 19 |
| `zweikern_ohne_randkontakt` | 1 |

Damit ist die erste einfache Hypothese zu grob:

```text
XRP 2025 hat einzelne Übergangssegmente,
DOGE 2025 dagegen nicht.
```

So liest sich der Befund nicht. Auch DOGE 2025 bildet in 1000er-Teilfenstern häufig mehrere stabile Feldrollen.

## Wichtige methodische Trennung

Die 1000er-Teilfensterprüfung liest:

```text
Wie viele stabile Feldrollen entstehen lokal in einem Real-Lauf?
```

Der 5000er-Achsenreport liest zusätzlich:

```text
Welche Rollen und Kombinationen werden über Real-Sleep-Real reaktiviert?
```

Deshalb widersprechen sich die Befunde nicht:

- lokal können DOGE und XRP beide mehrere Feldrollen bilden,
- im längeren 5000er-Kontext bleibt DOGE aber kompakter gebunden,
- XRP bildet über Sleep-/Folgewelt mehr Cross-State-Kombinationen.

## Lesart

Die `mittlere_uebergangsphase` entsteht wahrscheinlich nicht aus einem einzelnen lokalen Segment.

Sie wirkt eher wie eine Kombination aus:

- lokal vorhandener Mehrrollenfähigkeit,
- Nachhall über längere Weltstrecke,
- Reaktivierung im Folgefenster,
- Cross-State-Kombinationen in der Offline-/Folgewelt-Kette.

Kurz:

```text
Übergangsphase = nicht nur lokale Rollenbreite,
sondern Rollenbreite plus reaktivierte Kombinationsqualität.
```

## Auffällige Fenster

Stärkere Mehrrollenfenster:

- `XRP_2025_FOLLOW 0-1000`: 21 Rollen, 7 dauerhafte Rollen, 2 lange Rollen.
- `DOGE_2025_FOLLOW 4000-5000`: 20 Rollen, 7 dauerhafte Rollen, 3 lange Rollen.
- `XRP_2025_A 4000-5000`: 18 Rollen, 6 dauerhafte Rollen, 2 lange Rollen.
- `DOGE_2025_FOLLOW 0-1000`: 19 Rollen, 6 dauerhafte Rollen, 2 lange Rollen.

Das zeigt: Mehrrollenfähigkeit ist nicht XRP-exklusiv. Die stärkere XRP-Übergangsphase muss daher in der späteren Kopplung und Reaktivierung gelesen werden, nicht nur in lokalen Rohsegmenten.

## Zugehöriger Report

- [xrp_doge_2025_teilfenster_mehrrollen_scan.md](../../../../reports/xrp_doge_2025_teilfenster_mehrrollen_scan.md)

## Wie es weitergeht

Als nächstes sollte der stärkste XRP-Teilfensterkandidat als eigene Real-Sleep-Real-Kette gegen einen starken DOGE-Teilfensterkandidaten geprüft werden. Entscheidend ist, ob XRP lokal mehr Cross-State-Reaktivierung bildet oder ob die frühere Übergangsphase erst aus dem 5000er-Gesamtkontext entsteht.
