# PAXG Zeitmaß- und Jahresvergleich der Rekopplungsbreite

Stand: 2026-07-08

## Grundfrage

Nach 1775 war sichtbar:

```text
PAXG 2024 5m zeigt rekoppelnde Rollenbreite als lokale Phase.
```

Die nächste Unterprüfung war:

```text
Wiederholt sich diese Phase in PAXG 2025
und bleibt sie bei 1h-Zeitmaß erhalten?
```

## Prüfung

Verglichen wurden:

- PAXG 2024 5m,
- PAXG 2025 5m,
- PAXG 2024/2025 1h.

Für 1h wurden neue lokale Follow-Slices erzeugt:

```text
data/paxg_2024_1h_follow_candidate_4000_5000.csv
data/paxg_2024_1h_follow_candidate_5000_6000.csv
data/paxg_2024_1h_follow_candidate_6000_7000.csv
data/paxg_2024_1h_follow_candidate_7000_8000.csv
data/paxg_2025_1h_follow_candidate_4000_5000.csv
data/paxg_2025_1h_follow_candidate_5000_6000.csv
data/paxg_2025_1h_follow_candidate_6000_7000.csv
data/paxg_2025_1h_follow_candidate_7000_8000.csv
```

Die Reports liegen in:

```text
reports/btc_paxg_2025_sequence_rawworld_contrast.csv
reports/paxg_1h_lokale_realsleepreal_sequenz.csv
reports/paxg_1h_sequence_rawworld_contrast.csv
reports/paxg_2024_2025_1h_phasenvergleich.csv
```

## Ergebnis

PAXG 2024 5m:

```text
mittlere_uebergangsphase
mittlere_uebergangsphase
verteilt_rekoppelnd
mittlere_uebergangsphase
```

PAXG 2025 5m:

```text
mittlere_uebergangsphase
verteilt_rekoppelnd
verteilt_rekoppelnd
verteilt_rekoppelnd
```

PAXG 1h 2024/2025:

```text
kompakt_nachhallend
verteilt_offen
verteilt_offen
verteilt_offen
verteilt_offen
verteilt_offen
```

## Befund

PAXG 2025 bestätigt die rekoppelnde Rollenbreite stärker als PAXG 2024.

Sie erscheint dort nicht nur als einzelnes Fenster, sondern als längere lokale Folge.

PAXG 1h zeigt dagegen:

```text
Rollenbreite bleibt sichtbar,
aber die Rückbindung wird eher verteilt_offen
als verteilt_rekoppelnd gelesen.
```

## Deutung

Rekoppelnde Rollenbreite ist damit nicht einfach:

```text
PAXG allgemein
```

sondern abhängig von:

- lokaler Anschlussgeschichte,
- Zeitmaß,
- adaptiver Erfahrungskopplung,
- Nachhall,
- Rollen-/Kombinationsbreite.

Das 1h-Zeitmaß glättet die Welt nicht einfach leer.

Es erhält Rollenbreite, verändert aber ihre Qualität:

```text
5m: rekoppelnde Breite möglich
1h: breite Offenheit stärker sichtbar
```

## Bedeutung für MINI_DIO

MINI_DIO zeigt hier eine wichtige Trennung:

```text
Breite ist nicht automatisch Rekopplung.
```

Ein Feld kann viele Rollen halten und trotzdem offener bleiben.

Rekopplung braucht offenbar mehr als Rollenanzahl:

```text
Rollenbreite + Anschlussqualität + passende Erfahrungsrückbindung.
```

## Grenze

Die 1h-Prüfung nutzt lokale 1000er-Slices aus PAXG 2024/2025.

Sie ist eine passive Vergleichsprüfung, keine vollständige Aussage über alle PAXG-1h-Phasen.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob `verteilt_offen` bei 1h durch andere Fenster doch in `verteilt_rekoppelnd` kippt oder ob 1h systematisch mehr offene Breite als rekoppelnde Breite trägt.
