# Real-Sleep-Real Baseline

Stand: 2026-07-05 15:10:32

## Zweck

Diese Kette prueft, was sich zwischen zwei gleichen Real-Welt-Beruehrungen veraendert,
wenn dazwischen eine entkoppelte MCM-Schlafdiagnose liegt.

Wichtig: In der Baseline schreibt die Schlafphase noch keine Memory um.
Sie erzeugt nur Diagnoseartefakte. Dadurch bleibt sichtbar, was Wiederholung mit gleicher Memory leistet,
bevor spaeter echte Schlaf-Reorganisation erlaubt wird.

## Kette

- Welt: `data\kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv`
- Real A Memory: `memory\real_sleep_real\sol2024_5m_2000_baseline\memory_A_real_run.json`
- Sleep Diagnose: `debug\real_sleep_real\sol2024_5m_2000_baseline\sleep`
- Memory nach Sleep: `memory\real_sleep_real\sol2024_5m_2000_baseline\memory_A_after_sleep.json`
- Real B Memory: `memory\real_sleep_real\sol2024_5m_2000_baseline\memory_B_real_run_after_sleep.json`

## Real A -> Real B

- Episoden: `1994.0` -> `1994.0`
- Unique Syntax: `351.0` -> `351.0`
- geschriebene Feldepisoden: `5.0` -> `5.0`
- MCM-Tragqualitaet: `0.509901` -> `0.510684`
- MCM-Rekopplung: `0.693318` -> `0.692524`
- MCM-Sinneskopplung: `0.83793` -> `0.837184`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Sleep Diagnose

- Sleep Ticks: `300`
- Rollen im Sleep-Pool: `5`
- aktive Rollensets: `3`
- Sleep Unique Syntax: `1`
- mittlerer Nachhall: `0.027274`
- passive Sleep-Memory geschrieben: `False`

Sleep-Zustaende:

- `sleep_rekopplung`: `300`

## Bewertung

Diese Baseline ist noch kein Nachweis fuer schlafbedingtes Lernen.
Sie trennt aber die drei Ebenen: erste Weltberuehrung, entkoppelte Feldaktivitaet, zweite Weltberuehrung.
Damit ist der naechste Schritt sauber messbar: Schlaf darf spaeter begrenzt Memory-Reorganisation schreiben,
und die zweite Weltberuehrung kann gegen diese Baseline verglichen werden.

## Wie es weitergeht

Als naechstes wird dieselbe Kette mit aktiver, aber klar begrenzter Sleep-Memory-Reorganisation vorbereitet.
Dann pruefen wir, ob im Schlaf beruehrte Rollen im zweiten Real-Lauf stabiler, klarer oder driftender wieder auftauchen.
