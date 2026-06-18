# Passive Feldklassen-Diagnose

Stand: 2026-06-18 21:15:18

## Zweck

Diese Diagnose ordnet mehrere passive MINI_DIO-Welten nach ihrer Innenfeldwirkung.
Sie ersetzt keine Einzelanalyse. Sie prüft, ob aus den bisherigen Mehrweltläufen größere Feldklassen sichtbar werden.

Hierarchie der Prüfung:

1. Grundfrage: Bildet MINI_DIO über verschiedene Welten hinweg wiedererkennbare Innenfeldklassen?
2. Unterprüfung: Welche Rohwelt-Merkmale und Feldwerte begleiten diese Klassen?
3. Folgeschritt: Prüfen, ob die Klassen bei neuen Welten stabil bleiben oder driften.

## Feldklassen

### Stress-Gegenpol

- Welten: `2`
- mittlere Rekopplung: `0.615676`
- mittlere Tragqualität: `0.349892`
- mittlere Spannungs-/Kippwirkung: `184.0`

#### welt_2023_stress_01

- Datenwelt: `data\kontrolliert_2023_real_test4_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4386`)
- Rekopplung: `0.614985`
- Tragqualität: `0.346134`
- Sinnes-MCM-Kopplung: `0.820632`
- Episodenmemory: `107`
- Unique Syntax: `972`
- gespannte + kippende Wirkung: `191`
- Rohwelt avg_abs_return: `0.003552`
- Rohwelt max_abs_return: `0.102743`
- Rohwelt avg_range: `0.007442`
- Rohwelt drift: `0.42866`
- Richtungswechsel: `449`

#### welt_2024_bridge3_01

- Datenwelt: `data\kontrolliert_2024_bridge_test3_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4728`)
- Rekopplung: `0.616367`
- Tragqualität: `0.353651`
- Sinnes-MCM-Kopplung: `0.821115`
- Episodenmemory: `117`
- Unique Syntax: `979`
- gespannte + kippende Wirkung: `177`
- Rohwelt avg_abs_return: `0.003269`
- Rohwelt max_abs_return: `0.068453`
- Rohwelt avg_range: `0.006902`
- Rohwelt drift: `0.117163`
- Richtungswechsel: `487`

### angespannte Übergangsgruppe

- Welten: `3`
- mittlere Rekopplung: `0.622780`
- mittlere Tragqualität: `0.354723`
- mittlere Spannungs-/Kippwirkung: `128.7`

#### welt_2023_01

- Datenwelt: `data\kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.4688`)
- Rekopplung: `0.623022`
- Tragqualität: `0.353039`
- Sinnes-MCM-Kopplung: `0.829622`
- Episodenmemory: `87`
- Unique Syntax: `947`
- gespannte + kippende Wirkung: `129`
- Rohwelt avg_abs_return: `0.002748`
- Rohwelt max_abs_return: `0.197605`
- Rohwelt avg_range: `0.00553`
- Rohwelt drift: `0.372`
- Richtungswechsel: `375`

#### welt_2024_01

- Datenwelt: `data\kontrolliert_2024_real_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4557`)
- Rekopplung: `0.622297`
- Tragqualität: `0.358091`
- Sinnes-MCM-Kopplung: `0.829287`
- Episodenmemory: `81`
- Unique Syntax: `967`
- gespannte + kippende Wirkung: `128`
- Rohwelt avg_abs_return: `0.002995`
- Rohwelt max_abs_return: `0.133873`
- Rohwelt avg_range: `0.005801`
- Rohwelt drift: `-0.044961`
- Richtungswechsel: `474`

#### expansion_2023_extreme_test1

- Datenwelt: `data\kontrolliert_2023_extreme_expansion_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.4688`)
- Rekopplung: `0.623022`
- Tragqualität: `0.353039`
- Sinnes-MCM-Kopplung: `0.829622`
- Episodenmemory: `87`
- Unique Syntax: `947`
- gespannte + kippende Wirkung: `129`
- Rohwelt avg_abs_return: `0.002748`
- Rohwelt max_abs_return: `0.197605`
- Rohwelt avg_range: `0.00553`
- Rohwelt drift: `0.372`
- Richtungswechsel: `375`

### mittlere Feldlage

- Welten: `1`
- mittlere Rekopplung: `0.633577`
- mittlere Tragqualität: `0.357946`
- mittlere Spannungs-/Kippwirkung: `40.0`

#### expansion_2023_positive_test1

- Datenwelt: `data\kontrolliert_2023_positive_expansion_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5684`)
- Rekopplung: `0.633577`
- Tragqualität: `0.357946`
- Sinnes-MCM-Kopplung: `0.839469`
- Episodenmemory: `41`
- Unique Syntax: `913`
- gespannte + kippende Wirkung: `40`
- Rohwelt avg_abs_return: `0.001357`
- Rohwelt max_abs_return: `0.021124`
- Rohwelt avg_range: `0.002699`
- Rohwelt drift: `0.016285`
- Richtungswechsel: `430`

### ruhige Nähegruppe

- Welten: `3`
- mittlere Rekopplung: `0.632791`
- mittlere Tragqualität: `0.360844`
- mittlere Spannungs-/Kippwirkung: `42.7`

#### welt_2025_core_01

- Datenwelt: `data\kontrolliert_2025_core_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5443`)
- Rekopplung: `0.633885`
- Tragqualität: `0.361269`
- Sinnes-MCM-Kopplung: `0.839992`
- Episodenmemory: `25`
- Unique Syntax: `923`
- gespannte + kippende Wirkung: `29`
- Rohwelt avg_abs_return: `0.001364`
- Rohwelt max_abs_return: `0.010683`
- Rohwelt avg_range: `0.002607`
- Rohwelt drift: `0.136845`
- Richtungswechsel: `495`

#### welt_2025_mid_shift_01

- Datenwelt: `data\kontrolliert_2025_mid_shift_test_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5131`)
- Rekopplung: `0.630490`
- Tragqualität: `0.359369`
- Sinnes-MCM-Kopplung: `0.836657`
- Episodenmemory: `57`
- Unique Syntax: `923`
- gespannte + kippende Wirkung: `62`
- Rohwelt avg_abs_return: `0.001667`
- Rohwelt max_abs_return: `0.011924`
- Rohwelt avg_range: `0.003237`
- Rohwelt drift: `0.036347`
- Richtungswechsel: `496`

#### welt_2025_late_shift_01

- Datenwelt: `data\kontrolliert_2025_late_shift_test_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5473`)
- Rekopplung: `0.633998`
- Tragqualität: `0.361895`
- Sinnes-MCM-Kopplung: `0.842004`
- Episodenmemory: `21`
- Unique Syntax: `923`
- gespannte + kippende Wirkung: `37`
- Rohwelt avg_abs_return: `0.001554`
- Rohwelt max_abs_return: `0.010344`
- Rohwelt avg_range: `0.002992`
- Rohwelt drift: `0.034787`
- Richtungswechsel: `512`

## Befund

Die bisherigen Welten zeigen keine einheitliche Wortbildung, aber wiedererkennbare Feldklassen.
Das ist wichtig: Die Syntax bleibt weltbezogen, während die Innenfeldwirkung über mehrere Welten hinweg ähnliche Klassen bilden kann.

Die ruhige Nähegruppe wird aktuell vor allem von 2025-Welten getragen. Sie zeigt hohe Rekopplung, hohe Tragqualität, starke stabile Dominanz und wenig gespannte/kippende Wirkung.

Der Stress-Gegenpol zeigt das Gegenteil: geringere Rekopplung, geringere Tragqualität, mehr Kipp- und Spannungswirkung und mehr Episodenmemory. Das wirkt wie stärkere innere Verarbeitungslast.

Wichtig bleibt: Diese Klassen sind passive Beobachtungsklassen. Sie sind keine Gates, keine Handlungsregeln und keine Strategie.

## Wie es weitergeht

Als nächstes sollte eine neue Welt nicht nur einzeln bewertet werden, sondern direkt gegen diese Feldklassen gehalten werden. Entscheidend ist, ob MINI_DIO eine neue Welt in eine bestehende Feldklasse einordnet oder ob eine neue Klasse entsteht.
