# Passive Feldklassen-Diagnose

Stand: 2026-06-18 22:02:33

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
- mittlere Rekopplung: `0.618622`
- mittlere Tragqualität: `0.353688`
- mittlere Spannungs-/Kippwirkung: `231.5`

#### sideways_2026_1k

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

#### sideways_2026_2k

- Datenwelt: `data\kontrolliert_2026_sideways_test1_2000_5m_SOLUSDT.csv`
- dominante Feldwirkung: `tragend_unruhig` (`0.4283`)
- Rekopplung: `0.622030`
- Tragqualität: `0.355412`
- Sinnes-MCM-Kopplung: `0.826561`
- Episodenmemory: `175`
- Unique Syntax: `1890`
- gespannte + kippende Wirkung: `271`
- Rohwelt avg_abs_return: `0.002681`
- Rohwelt max_abs_return: `0.0611`
- Rohwelt avg_range: `0.005312`
- Rohwelt drift: `-0.125398`
- Richtungswechsel: `968`

### mittlere Feldlage

- Welten: `1`
- mittlere Rekopplung: `0.630398`
- mittlere Tragqualität: `0.356899`
- mittlere Spannungs-/Kippwirkung: `66.0`

#### negative_stress_1k

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

- Welten: `1`
- mittlere Rekopplung: `0.631065`
- mittlere Tragqualität: `0.362044`
- mittlere Spannungs-/Kippwirkung: `65.0`

#### negative_moderate_1k

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
