# PAXG1000 Sleep-Zwischenrollen Abgleich

Stand: 2026-07-05

## Zweck

Diese Pruefung nutzt PAXG als dritte Ausgangswelt fuer denselben passiven Zwischenrollen-Speicher.

Geprueft wurde:

- PAXG 2024 5m als Ursprung,
- gleiche PAXG-2024-5m-Welt als Ruecklesung,
- PAXG 2025 5m als Folgewelt,
- PAXG 2024 1h als andere Zeitebene,
- KAS 2024 5m als andere Asset-Gegenwelt.

Die Pruefung bleibt passiv:

- keine Handlung,
- keine Richtung,
- kein Gate,
- keine Motorik.

## Ergebnis

PAXG bildet in diesem 1000-Zeilen-Fenster keine Sleep-Kombinationen.

```text
touched_role_count: 1
combination_trace_count: 0
```

Die aktive Offline-Rolle ist:

```text
dio_mcm_episode_1joiyc3
```

Diese Rolle wird in der gleichen PAXG-Welt voll rueckgelesen. Auch PAXG 1h und KAS 5m beruehren sie wieder. PAXG 2025 5m laesst sie dagegen unveraendert.

## Speicherbefund

Der bestehende Zwischenrollen-Speicher wurde nicht erweitert.

```text
vorher: 9 Kandidaten
nachher: 9 Kandidaten
```

Damit unterscheidet sich PAXG klar von BTC:

```text
BTC1000: 3 Kombinationen, 2 neue Kandidaten, 1 bekannter Kandidat gestaerkt
PAXG1000: 0 Kombinationen, keine neuen Kandidaten
```

## Lesung

PAXG wirkt in diesem Fenster nicht als kombinatorische Zwischenrollen-Welt, sondern als engere Einzel-Rekopplungswelt.

Das ist fachlich wichtig, weil es gegen eine triviale Speicheraufblaehung spricht:

```text
Nicht jede neue Welt erzeugt neue Zwischenrollen.
```

Der Speicher waechst also nicht automatisch. Er wird nur erweitert, wenn die Offline-Feldlage mehrere gemeinsam ruecklesbare Rollen bildet.

## Grenze

Dieser Befund beweist nicht, dass PAXG grundsaetzlich keine Zwischenrollen erzeugen kann.

Er zeigt nur:

```text
In diesem PAXG-1000-Fenster entsteht keine Offline-Kombinationsbasis.
```

Laengere oder anders gewaehlte PAXG-Welten koennen anders wirken.
