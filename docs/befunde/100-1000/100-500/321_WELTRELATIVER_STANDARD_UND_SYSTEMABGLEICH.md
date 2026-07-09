# Weltrelativer Standard Und Systemabgleich

Stand: 2026-06-19

## Zweck

Diese Notiz haelt den Uebergang von hypothetischen Eingangsmoeglichkeiten zur aktuellen Systemmechanik fest.

Geprueft wurde:

1. Ob die feste Sinnesuebersetzung noch Reizuebersteuerung erzeugt.
2. Ob der weltrelative Adapter die Aufnahme ueber verschiedene Welten tragbarer macht.
3. Ob diese Verbesserung im echten MINI_DIO-Lauf auch die innere Feldordnung verbessert.

## Befund Der Aufnahme

Die feste Uebersetzung zeigt in der aktuellen Diagnose weiter auffaellige Achsen:

- `uebersteuert`: 11 Achsen
- `nahe_saettigung`: 7 Achsen
- `tragbar`: 30 Achsen

Der weltrelative Adapter bringt im Vergleich alle geprueften Achsen in den Bereich `tragbar`:

- Verbesserte Achsen: 18
- Verschlechterte Achsen: 0
- Weiter auffaellige Achsen: 0

Das spricht dafuer, dass ein Teil frueherer Feldspannung nicht aus der Welt selbst kam, sondern aus der Art, wie Welt in Sinneswerte uebersetzt wurde.

## Laufvergleich

Verglichen wurde dieselbe Welt:

`data/kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv`

### Feste Uebersetzung

- Unique Syntaxsymbole: 1904
- geschriebene Feld-Episoden: 365
- `field_carried`: 1740
- `field_strained`: 254
- MCM-Rekopplung: 0.6140
- MCM-Tragqualitaet: 0.3557
- MCM-Spannung: 0.2361
- Sinnes-MCM-Kopplung: 0.8204
- Neuro-Last: 0.2207
- Neuro-Support: 0.2717

### Weltrelative Uebersetzung

- Unique Syntaxsymbole: 1811
- geschriebene Feld-Episoden: 15
- `field_carried`: 1986
- `field_strained`: 8
- MCM-Rekopplung: 0.6438
- MCM-Tragqualitaet: 0.3992
- MCM-Spannung: 0.1933
- Sinnes-MCM-Kopplung: 0.8655
- Neuro-Last: 0.1930
- Neuro-Support: 0.3060

## Schlussfolgerung

Der weltrelative Adapter ist nicht nur eine kosmetische Normalisierung.

Er verbessert im Test:

- weniger Uebersteuerung in der Aufnahme,
- weniger fragmentierte Episodenbildung,
- weniger `field_strained`,
- hoehere Rekopplung,
- bessere Sinnes-MCM-Kopplung,
- geringere Neuro-Last,
- hoeheren Neuro-Support.

Damit wird `world_relative` als passiver Standardmodus gesetzt.

Die alte feste Uebersetzung bleibt per CLI explizit pruefbar:

```text
--sense-mode fixed
```

## Grenze

Das ist keine Handlung, kein Gate und keine Strategie.

Der Adapter entscheidet nichts. Er sorgt nur dafuer, dass unterschiedliche Welten MINI_DIO nicht durch Rohskala, Lautstaerke oder Zeitebene falsch ueberreizen.

## Wie Es Weitergeht

Als naechstes wird geprueft, ob der neue Standard ueber mehrere Weltklassen dieselbe Topologiequalitaet erhaelt: Zentrum, offene Bruecke, Randspannung, Rekopplung und lokale Kontaktinseln.
