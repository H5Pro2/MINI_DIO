# Passive Feldklassen-Diagnose

Stand: 2026-06-18 21:49:48

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
- Unique Syntax: `972`
- gespannte + kippende Wirkung: `191`
- Rohwelt avg_abs_return: `0.003552`
- Rohwelt max_abs_return: `0.102743`
- Rohwelt avg_range: `0.007442`
- Rohwelt drift: `0.42866`
- Richtungswechsel: `449`

#### sideways_2026

- Datenwelt: `data\kontrolliert_2026_sideways_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4618`)
- Rekopplung: `0.615214`
- Tragqualität: `0.351964`
- Sinnes-MCM-Kopplung: `0.818717`
- Episodenmemory: `117`
- Unique Syntax: `973`
- gespannte + kippende Wirkung: `192`
- Rohwelt avg_abs_return: `0.003525`
- Rohwelt max_abs_return: `0.0611`
- Rohwelt avg_range: `0.006917`
- Rohwelt drift: `-0.043664`
- Richtungswechsel: `472`

### angespannte Übergangsgruppe

- Welten: `2`
- mittlere Rekopplung: `0.623022`
- mittlere Tragqualität: `0.353039`
- mittlere Spannungs-/Kippwirkung: `129.0`

#### basis_2023

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

#### expansion_extreme

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

- Welten: `2`
- mittlere Rekopplung: `0.631987`
- mittlere Tragqualität: `0.357422`
- mittlere Spannungs-/Kippwirkung: `53.0`

#### expansion_positive

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

#### negative_stress

- Datenwelt: `data\kontrolliert_2023_negative_stress_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5533`)
- Rekopplung: `0.630398`
- Tragqualität: `0.356899`
- Sinnes-MCM-Kopplung: `0.835699`
- Episodenmemory: `59`
- Unique Syntax: `927`
- gespannte + kippende Wirkung: `66`
- Rohwelt avg_abs_return: `0.001579`
- Rohwelt max_abs_return: `0.015099`
- Rohwelt avg_range: `0.003167`
- Rohwelt drift: `-0.029304`
- Richtungswechsel: `395`

### ruhige Nähegruppe

- Welten: `2`
- mittlere Rekopplung: `0.630810`
- mittlere Tragqualität: `0.360662`
- mittlere Spannungs-/Kippwirkung: `58.5`

#### sideways_2024

- Datenwelt: `data\kontrolliert_2024_moderate_sideways_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5181`)
- Rekopplung: `0.630554`
- Tragqualität: `0.359280`
- Sinnes-MCM-Kopplung: `0.834716`
- Episodenmemory: `43`
- Unique Syntax: `922`
- gespannte + kippende Wirkung: `52`
- Rohwelt avg_abs_return: `0.001553`
- Rohwelt max_abs_return: `0.016155`
- Rohwelt avg_range: `0.002946`
- Rohwelt drift: `-0.021215`
- Richtungswechsel: `476`

#### negative_moderate

- Datenwelt: `data\kontrolliert_2023_moderate_negative_test1_1000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5563`)
- Rekopplung: `0.631065`
- Tragqualität: `0.362044`
- Sinnes-MCM-Kopplung: `0.836444`
- Episodenmemory: `45`
- Unique Syntax: `932`
- gespannte + kippende Wirkung: `65`
- Rohwelt avg_abs_return: `0.001601`
- Rohwelt max_abs_return: `0.017682`
- Rohwelt avg_range: `0.003094`
- Rohwelt drift: `0.02433`
- Richtungswechsel: `422`

## Befund

Die bisherigen Welten zeigen keine einheitliche Wortbildung, aber wiedererkennbare Feldklassen.
Das ist wichtig: Die Syntax bleibt weltbezogen, während die Innenfeldwirkung über mehrere Welten hinweg ähnliche Klassen bilden kann.

Die ruhige Nähegruppe wird aktuell vor allem von 2025-Welten getragen. Sie zeigt hohe Rekopplung, hohe Tragqualität, starke stabile Dominanz und wenig gespannte/kippende Wirkung.

Der Stress-Gegenpol zeigt das Gegenteil: geringere Rekopplung, geringere Tragqualität, mehr Kipp- und Spannungswirkung und mehr Episodenmemory. Das wirkt wie stärkere innere Verarbeitungslast.

Wichtig bleibt: Diese Klassen sind passive Beobachtungsklassen. Sie sind keine Gates, keine Handlungsregeln und keine Strategie.

## Wie es weitergeht

Als nächstes sollte eine neue Welt nicht nur einzeln bewertet werden, sondern direkt gegen diese Feldklassen gehalten werden. Entscheidend ist, ob MINI_DIO eine neue Welt in eine bestehende Feldklasse einordnet oder ob eine neue Klasse entsteht.
