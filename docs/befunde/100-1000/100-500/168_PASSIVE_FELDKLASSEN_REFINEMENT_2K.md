# Passive Feldklassen-Diagnose

Stand: 2026-06-18 22:09:21

## Zweck

Diese Diagnose ordnet mehrere passive MINI_DIO-Welten nach ihrer Innenfeldwirkung.
Sie ersetzt keine Einzelanalyse. Sie prüft, ob aus den bisherigen Mehrweltläufen größere Feldklassen sichtbar werden.

Hierarchie der Prüfung:

1. Grundfrage: Bildet MINI_DIO über verschiedene Welten hinweg wiedererkennbare Innenfeldklassen?
2. Unterprüfung: Welche Rohwelt-Merkmale und Feldwerte begleiten diese Klassen?
3. Folgeschritt: Prüfen, ob die Klassen bei neuen Welten stabil bleiben oder driften.

## Feldklassen

### Stress-Gegenpol

- Welten: `1`
- mittlere Rekopplung: `0.615214`
- mittlere Tragqualität: `0.351964`
- mittlere Spannungs-/Kippwirkung: `192.0`

#### sideways_2026_1k

- Datenwelt: `data\kontrolliert_2026_sideways_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4618`)
- Rekopplung: `0.615214`
- Tragqualität: `0.351964`
- Sinnes-MCM-Kopplung: `0.818717`
- Episodenmemory: `117`
- field_carried: `908` (`0.9135`)
- field_strained: `86` (`0.0865`)
- Unique Syntax: `973`
- gespannte + kippende Wirkung: `192`
- Rohwelt avg_abs_return: `0.003525`
- Rohwelt max_abs_return: `0.0611`
- Rohwelt avg_range: `0.006917`
- Rohwelt drift: `-0.043664`
- Richtungswechsel: `472`

### angespannte Übergangsgruppe

- Welten: `1`
- mittlere Rekopplung: `0.622030`
- mittlere Tragqualität: `0.355412`
- mittlere Spannungs-/Kippwirkung: `271.0`

#### sideways_2026_2k

- Datenwelt: `data\kontrolliert_2026_sideways_test1_2000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4283`)
- Rekopplung: `0.622030`
- Tragqualität: `0.355412`
- Sinnes-MCM-Kopplung: `0.826561`
- Episodenmemory: `175`
- field_carried: `1874` (`0.9398`)
- field_strained: `120` (`0.0602`)
- Unique Syntax: `1890`
- gespannte + kippende Wirkung: `271`
- Rohwelt avg_abs_return: `0.002681`
- Rohwelt max_abs_return: `0.0611`
- Rohwelt avg_range: `0.005312`
- Rohwelt drift: `-0.125398`
- Richtungswechsel: `968`

### ruhige Nähegruppe

- Welten: `2`
- mittlere Rekopplung: `0.630362`
- mittlere Tragqualität: `0.361262`
- mittlere Spannungs-/Kippwirkung: `103.5`

#### negative_moderate_1k

- Datenwelt: `data\kontrolliert_2023_moderate_negative_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5563`)
- Rekopplung: `0.631065`
- Tragqualität: `0.362044`
- Sinnes-MCM-Kopplung: `0.836444`
- Episodenmemory: `45`
- field_carried: `968` (`0.9738`)
- field_strained: `26` (`0.0262`)
- Unique Syntax: `932`
- gespannte + kippende Wirkung: `65`
- Rohwelt avg_abs_return: `0.001601`
- Rohwelt max_abs_return: `0.017682`
- Rohwelt avg_range: `0.003094`
- Rohwelt drift: `0.02433`
- Richtungswechsel: `422`

#### negative_moderate_2k

- Datenwelt: `data\kontrolliert_2023_moderate_negative_test1_2000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5351`)
- Rekopplung: `0.629660`
- Tragqualität: `0.360479`
- Sinnes-MCM-Kopplung: `0.834450`
- Episodenmemory: `105`
- field_carried: `1927` (`0.9664`)
- field_strained: `67` (`0.0336`)
- Unique Syntax: `1824`
- gespannte + kippende Wirkung: `142`
- Rohwelt avg_abs_return: `0.001797`
- Rohwelt max_abs_return: `0.047315`
- Rohwelt avg_range: `0.00357`
- Rohwelt drift: `-0.118763`
- Richtungswechsel: `850`

## Befund

Die bisherigen Welten zeigen keine einheitliche Wortbildung, aber wiedererkennbare Feldklassen.
Das ist wichtig: Die Syntax bleibt weltbezogen, während die Innenfeldwirkung über mehrere Welten hinweg ähnliche Klassen bilden kann.

Die ruhige Nähegruppe wird aktuell vor allem von 2025-Welten getragen. Sie zeigt hohe Rekopplung, hohe Tragqualität, starke stabile Dominanz und wenig gespannte/kippende Wirkung.

Der Stress-Gegenpol zeigt das Gegenteil: geringere Rekopplung, geringere Tragqualität, mehr Kipp- und Spannungswirkung und mehr Episodenmemory. Das wirkt wie stärkere innere Verarbeitungslast.

Wichtig bleibt: Diese Klassen sind passive Beobachtungsklassen. Sie sind keine Gates, keine Handlungsregeln und keine Strategie.

## Wie es weitergeht

Als nächstes sollte eine neue Welt nicht nur einzeln bewertet werden, sondern direkt gegen diese Feldklassen gehalten werden. Entscheidend ist, ob MINI_DIO eine neue Welt in eine bestehende Feldklasse einordnet oder ob eine neue Klasse entsteht.
