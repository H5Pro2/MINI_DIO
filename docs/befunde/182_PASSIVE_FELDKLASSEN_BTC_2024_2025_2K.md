# Passive Feldklassen-Diagnose

Stand: 2026-06-18 22:41:38

## Zweck

Diese Diagnose ordnet mehrere passive MINI_DIO-Welten nach ihrer Innenfeldwirkung.
Sie ersetzt keine Einzelanalyse. Sie prüft, ob aus den bisherigen Mehrweltläufen größere Feldklassen sichtbar werden.

Hierarchie der Prüfung:

1. Grundfrage: Bildet MINI_DIO über verschiedene Welten hinweg wiedererkennbare Innenfeldklassen?
2. Unterprüfung: Welche Rohwelt-Merkmale und Feldwerte begleiten diese Klassen?
3. Folgeschritt: Prüfen, ob die Klassen bei neuen Welten stabil bleiben oder driften.

## Feldklassen

### Stress-Gegenpol

- Welten: `3`
- mittlere Rekopplung: `0.612200`
- mittlere Tragqualität: `0.346052`
- mittlere Spannungs-/Kippwirkung: `410.3`

#### btc_2024_1h_2k

- Datenwelt: `data\kontrolliert_btc_2024_1h_test1_2000_BTCUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4208`)
- Rekopplung: `0.610376`
- Tragqualität: `0.345005`
- Sinnes-MCM-Kopplung: `0.811991`
- Episodenmemory: `329`
- field_carried: `1717` (`0.8611`)
- field_strained: `277` (`0.1389`)
- Unique Syntax: `1911`
- gespannte + kippende Wirkung: `517`
- Rohwelt avg_abs_return: `0.00402`
- Rohwelt max_abs_return: `0.040279`
- Rohwelt avg_range: `0.008416`
- Rohwelt drift: `0.520496`
- Richtungswechsel: `1056`

#### btc_2025_1h_2k

- Datenwelt: `data\kontrolliert_btc_2025_1h_test1_2000_BTCUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4238`)
- Rekopplung: `0.611240`
- Tragqualität: `0.347018`
- Sinnes-MCM-Kopplung: `0.812374`
- Episodenmemory: `347`
- field_carried: `1712` (`0.8586`)
- field_strained: `282` (`0.1414`)
- Unique Syntax: `1908`
- gespannte + kippende Wirkung: `523`
- Rohwelt avg_abs_return: `0.003934`
- Rohwelt max_abs_return: `0.050245`
- Rohwelt avg_range: `0.008045`
- Rohwelt drift: `-0.084367`
- Richtungswechsel: `1054`

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

- Welten: `2`
- mittlere Rekopplung: `0.637478`
- mittlere Tragqualität: `0.367316`
- mittlere Spannungs-/Kippwirkung: `90.0`

#### btc_2024_5m_2k

- Datenwelt: `data\kontrolliert_btc_2024_5m_test1_2000_BTCUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5667`)
- Rekopplung: `0.636577`
- Tragqualität: `0.366108`
- Sinnes-MCM-Kopplung: `0.833261`
- Episodenmemory: `63`
- field_carried: `1952` (`0.9789`)
- field_strained: `42` (`0.0211`)
- Unique Syntax: `1576`
- gespannte + kippende Wirkung: `90`
- Rohwelt avg_abs_return: `0.001154`
- Rohwelt max_abs_return: `0.048341`
- Rohwelt avg_range: `0.002102`
- Rohwelt drift: `0.035835`
- Richtungswechsel: `1048`

#### btc_2025_5m_2k

- Datenwelt: `data\kontrolliert_btc_2025_5m_test1_2000_BTCUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.5712`)
- Rekopplung: `0.638380`
- Tragqualität: `0.368524`
- Sinnes-MCM-Kopplung: `0.827711`
- Episodenmemory: `87`
- field_carried: `1950` (`0.9779`)
- field_strained: `44` (`0.0221`)
- Unique Syntax: `1440`
- gespannte + kippende Wirkung: `90`
- Rohwelt avg_abs_return: `0.000779`
- Rohwelt max_abs_return: `0.009667`
- Rohwelt avg_range: `0.001355`
- Rohwelt drift: `0.037023`
- Richtungswechsel: `1037`

## Befund

Die bisherigen Welten zeigen keine einheitliche Wortbildung, aber wiedererkennbare Feldklassen.
Das ist wichtig: Die Syntax bleibt weltbezogen, während die Innenfeldwirkung über mehrere Welten hinweg ähnliche Klassen bilden kann.

Die ruhige Nähegruppe wird aktuell vor allem von 2025-Welten getragen. Sie zeigt hohe Rekopplung, hohe Tragqualität, starke stabile Dominanz und wenig gespannte/kippende Wirkung.

Der Stress-Gegenpol zeigt das Gegenteil: geringere Rekopplung, geringere Tragqualität, mehr Kipp- und Spannungswirkung und mehr Episodenmemory. Das wirkt wie stärkere innere Verarbeitungslast.

Wichtig bleibt: Diese Klassen sind passive Beobachtungsklassen. Sie sind keine Gates, keine Handlungsregeln und keine Strategie.

## Wie es weitergeht

Als nächstes sollte eine neue Welt nicht nur einzeln bewertet werden, sondern direkt gegen diese Feldklassen gehalten werden. Entscheidend ist, ob MINI_DIO eine neue Welt in eine bestehende Feldklasse einordnet oder ob eine neue Klasse entsteht.
