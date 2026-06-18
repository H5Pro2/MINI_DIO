# Projektstatus

Stand: 2026-06-18

MINI_DIO wurde aus dem grossen `MCM_Trading_Brain`-Projekt als eigenstaendiges Forschungsprojekt angelegt.

## Entkopplungsstand

Fachlich:

- Mini-DIO besitzt eigenen Kern.
- Mini-DIO nutzt eigene MCM-Neuronen, eigene Weltlesung, eigene Semantik und eigene passive Reports.
- Keine direkte Runtime-Abhaengigkeit auf `bot.py`, `MCM_Brain_Modell.py`, `core/` oder `trading/`.

Technisch:

- Kernpaket liegt unter `mini_dio/`.
- Forschungsskripte liegen unter `reports/`.
- Befunde liegen unter `docs/befunde/`.
- Lokale Daten, Memory und Debug-Ausgaben sind getrennt.

## Offene Aufraeumarbeiten

- Historische Reports weiter kuratieren.
- Einheitliche CLI-Kommandos fuer die aktuelle Forschungskette bauen.
- Kleine Testdaten dauerhaft eincheckbar halten.
- Grosse Daten und Debug-Ausgaben nicht in Git aufnehmen.
- Tests fuer Kernfunktionen ergaenzen.

## Arbeitsregel

MINI_DIO bleibt auf Forschungsebene.

Passive Reports duerfen keine Handlung, kein Gate und kein Entry-Signal erzeugen.

