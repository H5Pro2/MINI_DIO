# Passive Feldklassen-Diagnose

Stand: 2026-06-18 23:14:19

## Zweck

Diese Diagnose ordnet mehrere passive MINI_DIO-Welten nach ihrer Innenfeldwirkung.
Sie ersetzt keine Einzelanalyse. Sie prüft, ob aus den bisherigen Mehrweltläufen größere Feldklassen sichtbar werden.

Hierarchie der Prüfung:

1. Grundfrage: Bildet MINI_DIO über verschiedene Welten hinweg wiedererkennbare Innenfeldklassen?
2. Unterprüfung: Welche Rohwelt-Merkmale und Feldwerte begleiten diese Klassen?
3. Folgeschritt: Prüfen, ob die Klassen bei neuen Welten stabil bleiben oder driften.

## Feldklassen

### Stress-Gegenpol

- Welten: `6`
- mittlere Rekopplung: `0.599877`
- mittlere Tragqualität: `0.341485`
- mittlere Spannungs-/Kippwirkung: `775.3`

#### sol_2024_15m_2k

- Datenwelt: `data\kontrolliert_sol_2024_15m_test1_2000_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4468`)
- Rekopplung: `0.606542`
- Tragqualität: `0.343678`
- Sinnes-MCM-Kopplung: `0.805802`
- Episodenmemory: `309`
- field_carried: `1728` (`0.8666`)
- field_strained: `266` (`0.1334`)
- Unique Syntax: `1921`
- gespannte + kippende Wirkung: `583`
- Rohwelt avg_abs_return: `0.004505`
- Rohwelt max_abs_return: `0.089635`
- Rohwelt avg_range: `0.009292`
- Rohwelt drift: `-0.096717`
- Richtungswechsel: `1023`

#### sol_2024_30m_2k

- Datenwelt: `data\kontrolliert_sol_2024_30m_test1_2000_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.3892`)
- Rekopplung: `0.600205`
- Tragqualität: `0.341420`
- Sinnes-MCM-Kopplung: `0.795430`
- Episodenmemory: `441`
- field_carried: `1629` (`0.817`)
- field_strained: `365` (`0.183`)
- Unique Syntax: `1919`
- gespannte + kippende Wirkung: `755`
- Rohwelt avg_abs_return: `0.005375`
- Rohwelt max_abs_return: `0.055329`
- Rohwelt avg_range: `0.011323`
- Rohwelt drift: `0.066131`
- Richtungswechsel: `1051`

#### sol_2024_1h_2k

- Datenwelt: `data\kontrolliert_sol_2024_1h_test1_2000_SOLUSDT.csv`
- dominante Feldwirkung: `gespannt` (`0.3134`)
- Rekopplung: `0.587027`
- Tragqualität: `0.333433`
- Sinnes-MCM-Kopplung: `0.774350`
- Episodenmemory: `643`
- field_carried: `1364` (`0.6841`)
- field_strained: `630` (`0.3159`)
- Unique Syntax: `1854`
- gespannte + kippende Wirkung: `1100`
- Rohwelt avg_abs_return: `0.008273`
- Rohwelt max_abs_return: `0.090465`
- Rohwelt avg_range: `0.017364`
- Rohwelt drift: `0.70204`
- Richtungswechsel: `1046`

#### sol_2025_15m_2k

- Datenwelt: `data\kontrolliert_sol_2025_15m_test1_2000_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4323`)
- Rekopplung: `0.615512`
- Tragqualität: `0.351537`
- Sinnes-MCM-Kopplung: `0.817708`
- Episodenmemory: `247`
- field_carried: `1776` (`0.8907`)
- field_strained: `218` (`0.1093`)
- Unique Syntax: `1895`
- gespannte + kippende Wirkung: `420`
- Rohwelt avg_abs_return: `0.003975`
- Rohwelt max_abs_return: `0.045446`
- Rohwelt avg_range: `0.007683`
- Rohwelt drift: `0.330166`
- Richtungswechsel: `989`

#### sol_2025_30m_2k

- Datenwelt: `data\kontrolliert_sol_2025_30m_test1_2000_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.3977`)
- Rekopplung: `0.600912`
- Tragqualität: `0.343351`
- Sinnes-MCM-Kopplung: `0.796364`
- Episodenmemory: `434`
- field_carried: `1592` (`0.7984`)
- field_strained: `402` (`0.2016`)
- Unique Syntax: `1920`
- gespannte + kippende Wirkung: `744`
- Rohwelt avg_abs_return: `0.005871`
- Rohwelt max_abs_return: `0.050243`
- Rohwelt avg_range: `0.011423`
- Rohwelt drift: `0.045879`
- Richtungswechsel: `1021`

#### sol_2025_1h_2k

- Datenwelt: `data\kontrolliert_sol_2025_1h_test1_2000_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.3159`)
- Rekopplung: `0.589067`
- Tragqualität: `0.335489`
- Sinnes-MCM-Kopplung: `0.776872`
- Episodenmemory: `591`
- field_carried: `1407` (`0.7056`)
- field_strained: `587` (`0.2944`)
- Unique Syntax: `1860`
- gespannte + kippende Wirkung: `1050`
- Rohwelt avg_abs_return: `0.008056`
- Rohwelt max_abs_return: `0.118642`
- Rohwelt avg_range: `0.016035`
- Rohwelt drift: `-0.275683`
- Richtungswechsel: `1050`

### angespannte Übergangsgruppe

- Welten: `1`
- mittlere Rekopplung: `0.622776`
- mittlere Tragqualität: `0.358038`
- mittlere Spannungs-/Kippwirkung: `239.0`

#### sol_2024_5m_2k

- Datenwelt: `data\kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4604`)
- Rekopplung: `0.622776`
- Tragqualität: `0.358038`
- Sinnes-MCM-Kopplung: `0.829033`
- Episodenmemory: `149`
- field_carried: `1889` (`0.9473`)
- field_strained: `105` (`0.0527`)
- Unique Syntax: `1887`
- gespannte + kippende Wirkung: `239`
- Rohwelt avg_abs_return: `0.002809`
- Rohwelt max_abs_return: `0.133873`
- Rohwelt avg_range: `0.005589`
- Rohwelt drift: `-0.125012`
- Richtungswechsel: `955`

### ruhige Nähegruppe

- Welten: `1`
- mittlere Rekopplung: `0.636504`
- mittlere Tragqualität: `0.365647`
- mittlere Spannungs-/Kippwirkung: `63.0`

#### sol_2025_5m_2k

- Datenwelt: `data\kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5742`)
- Rekopplung: `0.636504`
- Tragqualität: `0.365647`
- Sinnes-MCM-Kopplung: `0.838491`
- Episodenmemory: `55`
- field_carried: `1966` (`0.986`)
- field_strained: `28` (`0.014`)
- Unique Syntax: `1680`
- gespannte + kippende Wirkung: `63`
- Rohwelt avg_abs_return: `0.001263`
- Rohwelt max_abs_return: `0.010683`
- Rohwelt avg_range: `0.002423`
- Rohwelt drift: `0.07211`
- Richtungswechsel: `990`

## Befund

Die bisherigen Welten zeigen keine einheitliche Wortbildung, aber wiedererkennbare Feldklassen.
Das ist wichtig: Die Syntax bleibt weltbezogen, während die Innenfeldwirkung über mehrere Welten hinweg ähnliche Klassen bilden kann.

Die ruhige Nähegruppe wird aktuell vor allem von 2025-Welten getragen. Sie zeigt hohe Rekopplung, hohe Tragqualität, starke stabile Dominanz und wenig gespannte/kippende Wirkung.

Der Stress-Gegenpol zeigt das Gegenteil: geringere Rekopplung, geringere Tragqualität, mehr Kipp- und Spannungswirkung und mehr Episodenmemory. Das wirkt wie stärkere innere Verarbeitungslast.

Wichtig bleibt: Diese Klassen sind passive Beobachtungsklassen. Sie sind keine Gates, keine Handlungsregeln und keine Strategie.

## Wie es weitergeht

Als nächstes sollte eine neue Welt nicht nur einzeln bewertet werden, sondern direkt gegen diese Feldklassen gehalten werden. Entscheidend ist, ob MINI_DIO eine neue Welt in eine bestehende Feldklasse einordnet oder ob eine neue Klasse entsteht.
