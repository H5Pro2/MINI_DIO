# Passive Feldklassen-Diagnose

Stand: 2026-06-18 22:15:53

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
- mittlere Rekopplung: `0.614985`
- mittlere Tragqualität: `0.346134`
- mittlere Spannungs-/Kippwirkung: `191.0`

#### stress_2023_1k

- Datenwelt: `data\kontrolliert_2023_real_test4_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4386`)
- Rekopplung: `0.614985`
- Tragqualität: `0.346134`
- Sinnes-MCM-Kopplung: `0.820632`
- Episodenmemory: `107`
- field_carried: `905` (`0.9105`)
- field_strained: `89` (`0.0895`)
- Unique Syntax: `972`
- gespannte + kippende Wirkung: `191`
- Rohwelt avg_abs_return: `0.003552`
- Rohwelt max_abs_return: `0.102743`
- Rohwelt avg_range: `0.007442`
- Rohwelt drift: `0.42866`
- Richtungswechsel: `449`

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

- Welten: `3`
- mittlere Rekopplung: `0.631487`
- mittlere Tragqualität: `0.360353`
- mittlere Spannungs-/Kippwirkung: `104.0`

#### positive_stress_2k

- Datenwelt: `data\kontrolliert_2024_positive_stress_test1_2000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5236`)
- Rekopplung: `0.631225`
- Tragqualität: `0.362635`
- Sinnes-MCM-Kopplung: `0.836229`
- Episodenmemory: `79`
- field_carried: `1946` (`0.9759`)
- field_strained: `48` (`0.0241`)
- Unique Syntax: `1775`
- gespannte + kippende Wirkung: `130`
- Rohwelt avg_abs_return: `0.001896`
- Rohwelt max_abs_return: `0.022743`
- Rohwelt avg_range: `0.003592`
- Rohwelt drift: `0.174695`
- Richtungswechsel: `977`

#### positive_expansion_1k

- Datenwelt: `data\kontrolliert_2023_positive_expansion_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5684`)
- Rekopplung: `0.633577`
- Tragqualität: `0.357946`
- Sinnes-MCM-Kopplung: `0.839469`
- Episodenmemory: `41`
- field_carried: `972` (`0.9779`)
- field_strained: `22` (`0.0221`)
- Unique Syntax: `913`
- gespannte + kippende Wirkung: `40`
- Rohwelt avg_abs_return: `0.001357`
- Rohwelt max_abs_return: `0.021124`
- Rohwelt avg_range: `0.002699`
- Rohwelt drift: `0.016285`
- Richtungswechsel: `430`

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
