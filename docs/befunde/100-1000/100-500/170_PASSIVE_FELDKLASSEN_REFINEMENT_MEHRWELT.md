# Passive Feldklassen-Diagnose

Stand: 2026-06-18 22:10:13

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
- mittlere Rekopplung: `0.615100`
- mittlere Tragqualität: `0.349049`
- mittlere Spannungs-/Kippwirkung: `191.5`

#### stress_2023

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

- Welten: `5`
- mittlere Rekopplung: `0.623358`
- mittlere Tragqualität: `0.355354`
- mittlere Spannungs-/Kippwirkung: `147.0`

#### basis_2023

- Datenwelt: `data\kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.4688`)
- Rekopplung: `0.623022`
- Tragqualität: `0.353039`
- Sinnes-MCM-Kopplung: `0.829622`
- Episodenmemory: `87`
- field_carried: `934` (`0.9396`)
- field_strained: `60` (`0.0604`)
- Unique Syntax: `947`
- gespannte + kippende Wirkung: `129`
- Rohwelt avg_abs_return: `0.002748`
- Rohwelt max_abs_return: `0.197605`
- Rohwelt avg_range: `0.00553`
- Rohwelt drift: `0.372`
- Richtungswechsel: `375`

#### basis_2024

- Datenwelt: `data\kontrolliert_2024_real_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4557`)
- Rekopplung: `0.622297`
- Tragqualität: `0.358091`
- Sinnes-MCM-Kopplung: `0.829287`
- Episodenmemory: `81`
- field_carried: `932` (`0.9376`)
- field_strained: `62` (`0.0624`)
- Unique Syntax: `967`
- gespannte + kippende Wirkung: `128`
- Rohwelt avg_abs_return: `0.002995`
- Rohwelt max_abs_return: `0.133873`
- Rohwelt avg_range: `0.005801`
- Rohwelt drift: `-0.044961`
- Richtungswechsel: `474`

#### expansion_extreme

- Datenwelt: `data\kontrolliert_2023_extreme_expansion_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.4688`)
- Rekopplung: `0.623022`
- Tragqualität: `0.353039`
- Sinnes-MCM-Kopplung: `0.829622`
- Episodenmemory: `87`
- field_carried: `934` (`0.9396`)
- field_strained: `60` (`0.0604`)
- Unique Syntax: `947`
- gespannte + kippende Wirkung: `129`
- Rohwelt avg_abs_return: `0.002748`
- Rohwelt max_abs_return: `0.197605`
- Rohwelt avg_range: `0.00553`
- Rohwelt drift: `0.372`
- Richtungswechsel: `375`

#### expansion_late

- Datenwelt: `data\kontrolliert_2024_late_positive_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.492`)
- Rekopplung: `0.626417`
- Tragqualität: `0.357191`
- Sinnes-MCM-Kopplung: `0.833999`
- Episodenmemory: `57`
- field_carried: `963` (`0.9688`)
- field_strained: `31` (`0.0312`)
- Unique Syntax: `954`
- gespannte + kippende Wirkung: `78`
- Rohwelt avg_abs_return: `0.002174`
- Rohwelt max_abs_return: `0.016623`
- Rohwelt avg_range: `0.004128`
- Rohwelt drift: `0.08832`
- Richtungswechsel: `490`

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

- Welten: `7`
- mittlere Rekopplung: `0.631373`
- mittlere Tragqualität: `0.359612`
- mittlere Spannungs-/Kippwirkung: `65.1`

#### basis_2025

- Datenwelt: `data\kontrolliert_2025_core_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5443`)
- Rekopplung: `0.633885`
- Tragqualität: `0.361269`
- Sinnes-MCM-Kopplung: `0.839992`
- Episodenmemory: `25`
- field_carried: `982` (`0.9879`)
- field_strained: `12` (`0.0121`)
- Unique Syntax: `923`
- gespannte + kippende Wirkung: `29`
- Rohwelt avg_abs_return: `0.001364`
- Rohwelt max_abs_return: `0.010683`
- Rohwelt avg_range: `0.002607`
- Rohwelt drift: `0.136845`
- Richtungswechsel: `495`

#### expansion_positive

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

#### expansion_recovery

- Datenwelt: `data\kontrolliert_2025_positive_recovery_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5141`)
- Rekopplung: `0.630474`
- Tragqualität: `0.359369`
- Sinnes-MCM-Kopplung: `0.836705`
- Episodenmemory: `57`
- field_carried: `961` (`0.9668`)
- field_strained: `33` (`0.0332`)
- Unique Syntax: `924`
- gespannte + kippende Wirkung: `62`
- Rohwelt avg_abs_return: `0.001666`
- Rohwelt max_abs_return: `0.011924`
- Rohwelt avg_range: `0.003233`
- Rohwelt drift: `0.03098`
- Richtungswechsel: `495`

#### sideways_2024

- Datenwelt: `data\kontrolliert_2024_moderate_sideways_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5181`)
- Rekopplung: `0.630554`
- Tragqualität: `0.359280`
- Sinnes-MCM-Kopplung: `0.834716`
- Episodenmemory: `43`
- field_carried: `969` (`0.9748`)
- field_strained: `25` (`0.0252`)
- Unique Syntax: `922`
- gespannte + kippende Wirkung: `52`
- Rohwelt avg_abs_return: `0.001553`
- Rohwelt max_abs_return: `0.016155`
- Rohwelt avg_range: `0.002946`
- Rohwelt drift: `-0.021215`
- Richtungswechsel: `476`

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

#### negative_stress_1k

- Datenwelt: `data\kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5533`)
- Rekopplung: `0.630398`
- Tragqualität: `0.356899`
- Sinnes-MCM-Kopplung: `0.835699`
- Episodenmemory: `59`
- field_carried: `964` (`0.9698`)
- field_strained: `30` (`0.0302`)
- Unique Syntax: `927`
- gespannte + kippende Wirkung: `66`
- Rohwelt avg_abs_return: `0.001579`
- Rohwelt max_abs_return: `0.015099`
- Rohwelt avg_range: `0.003167`
- Rohwelt drift: `-0.029304`
- Richtungswechsel: `395`

## Befund

Die bisherigen Welten zeigen keine einheitliche Wortbildung, aber wiedererkennbare Feldklassen.
Das ist wichtig: Die Syntax bleibt weltbezogen, während die Innenfeldwirkung über mehrere Welten hinweg ähnliche Klassen bilden kann.

Die ruhige Nähegruppe wird aktuell vor allem von 2025-Welten getragen. Sie zeigt hohe Rekopplung, hohe Tragqualität, starke stabile Dominanz und wenig gespannte/kippende Wirkung.

Der Stress-Gegenpol zeigt das Gegenteil: geringere Rekopplung, geringere Tragqualität, mehr Kipp- und Spannungswirkung und mehr Episodenmemory. Das wirkt wie stärkere innere Verarbeitungslast.

Wichtig bleibt: Diese Klassen sind passive Beobachtungsklassen. Sie sind keine Gates, keine Handlungsregeln und keine Strategie.

## Wie es weitergeht

Als nächstes sollte eine neue Welt nicht nur einzeln bewertet werden, sondern direkt gegen diese Feldklassen gehalten werden. Entscheidend ist, ob MINI_DIO eine neue Welt in eine bestehende Feldklasse einordnet oder ob eine neue Klasse entsteht.
