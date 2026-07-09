# Passive Feldklassen-Diagnose

Stand: 2026-06-18 22:56:10

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
- mittlere Rekopplung: `0.610808`
- mittlere Tragqualität: `0.346012`
- mittlere Spannungs-/Kippwirkung: `520.0`

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

### angespannte Übergangsgruppe

- Welten: `2`
- mittlere Rekopplung: `0.624621`
- mittlere Tragqualität: `0.357377`
- mittlere Spannungs-/Kippwirkung: `261.5`

#### btc_2024_30m_2k

- Datenwelt: `data\kontrolliert_btc_2024_30m_test1_2000_BTCUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.4654`)
- Rekopplung: `0.626156`
- Tragqualität: `0.359372`
- Sinnes-MCM-Kopplung: `0.831493`
- Episodenmemory: `179`
- field_carried: `1865` (`0.9353`)
- field_strained: `129` (`0.0647`)
- Unique Syntax: `1808`
- gespannte + kippende Wirkung: `248`
- Rohwelt avg_abs_return: `0.002435`
- Rohwelt max_abs_return: `0.035559`
- Rohwelt avg_range: `0.005`
- Rohwelt drift: `0.135095`
- Richtungswechsel: `1032`

#### btc_2025_30m_2k

- Datenwelt: `data\kontrolliert_btc_2025_30m_test1_2000_BTCUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.4238`)
- Rekopplung: `0.623087`
- Tragqualität: `0.355382`
- Sinnes-MCM-Kopplung: `0.828265`
- Episodenmemory: `167`
- field_carried: `1862` (`0.9338`)
- field_strained: `132` (`0.0662`)
- Unique Syntax: `1855`
- gespannte + kippende Wirkung: `275`
- Rohwelt avg_abs_return: `0.002731`
- Rohwelt max_abs_return: `0.047218`
- Rohwelt avg_range: `0.005388`
- Rohwelt drift: `0.034616`
- Richtungswechsel: `1058`

### ruhige Nähegruppe

- Welten: `4`
- mittlere Rekopplung: `0.634396`
- mittlere Tragqualität: `0.365097`
- mittlere Spannungs-/Kippwirkung: `131.8`

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

#### btc_2024_15m_2k

- Datenwelt: `data\kontrolliert_btc_2024_15m_test1_2000_BTCUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.507`)
- Rekopplung: `0.631196`
- Tragqualität: `0.362364`
- Sinnes-MCM-Kopplung: `0.834866`
- Episodenmemory: `105`
- field_carried: `1911` (`0.9584`)
- field_strained: `83` (`0.0416`)
- Unique Syntax: `1720`
- gespannte + kippende Wirkung: `176`
- Rohwelt avg_abs_return: `0.002042`
- Rohwelt max_abs_return: `0.042378`
- Rohwelt avg_range: `0.004016`
- Rohwelt drift: `-0.01809`
- Richtungswechsel: `1063`

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

#### btc_2025_15m_2k

- Datenwelt: `data\kontrolliert_btc_2025_15m_test1_2000_BTCUSDT.csv`
- dominante Feldwirkung: `stabil` (`0.513`)
- Rekopplung: `0.631429`
- Tragqualität: `0.363392`
- Sinnes-MCM-Kopplung: `0.835053`
- Episodenmemory: `125`
- field_carried: `1915` (`0.9604`)
- field_strained: `79` (`0.0396`)
- Unique Syntax: `1726`
- gespannte + kippende Wirkung: `171`
- Rohwelt avg_abs_return: `0.001887`
- Rohwelt max_abs_return: `0.032544`
- Rohwelt avg_range: `0.003695`
- Rohwelt drift: `0.142811`
- Richtungswechsel: `1009`

## Befund

Die bisherigen Welten zeigen keine einheitliche Wortbildung, aber wiedererkennbare Feldklassen.
Das ist wichtig: Die Syntax bleibt weltbezogen, während die Innenfeldwirkung über mehrere Welten hinweg ähnliche Klassen bilden kann.

Die ruhige Nähegruppe wird aktuell vor allem von 2025-Welten getragen. Sie zeigt hohe Rekopplung, hohe Tragqualität, starke stabile Dominanz und wenig gespannte/kippende Wirkung.

Der Stress-Gegenpol zeigt das Gegenteil: geringere Rekopplung, geringere Tragqualität, mehr Kipp- und Spannungswirkung und mehr Episodenmemory. Das wirkt wie stärkere innere Verarbeitungslast.

Wichtig bleibt: Diese Klassen sind passive Beobachtungsklassen. Sie sind keine Gates, keine Handlungsregeln und keine Strategie.

## Wie es weitergeht

Als nächstes sollte eine neue Welt nicht nur einzeln bewertet werden, sondern direkt gegen diese Feldklassen gehalten werden. Entscheidend ist, ob MINI_DIO eine neue Welt in eine bestehende Feldklasse einordnet oder ob eine neue Klasse entsteht.
