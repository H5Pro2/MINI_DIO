# KAS Randnaehe Gegen Normale Oeffnung

## Zweck

Diese Diagnose trennt innerhalb der KAS-Referenzwelt echte Rand/Kipp-Naehe von normaler offener Wahrnehmung.
Sie ist passiv und erzeugt keine Runtime-Regel.

## Klassenvergleich

| Klasse | Segmente | Familien | Top-Familie | Zentrum | Offen | Rand | Rohfeld avg | Lautheit avg | Unschaerfe avg | MCM-Spannung | Strain | Rekopplung | Drift abs | Range max | Wechsel |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| reale_randphase | 5 | 5 | dio_03iu (1) | 0.1004 | 0.4818 | 0.3451 | 0.2128 | 0.3553 | 0.4545 | 0.1724 | 0.2119 | 0.6395 | 0.0294 | 0.1077 | 0.3575 |
| reale_oeffnungsphase | 60 | 46 | dio_00ly (4) | 0.1278 | 0.7323 | 0.0287 | 0.1506 | 0.2551 | 0.3699 | 0.1270 | 0.1690 | 0.6752 | 0.0105 | 0.0132 | 0.4798 |
| gemischter_uebergang | 102 | 46 | dio_0m9z (11) | 0.4018 | 0.4025 | 0.0236 | 0.1415 | 0.2401 | 0.3474 | 0.1198 | 0.1586 | 0.6934 | 0.0084 | 0.0106 | 0.4826 |
| rekopplung_umfeld | 4 | 3 | dio_104t (2) | 0.7778 | 0.1944 | 0.0000 | 0.1198 | 0.1992 | 0.3438 | 0.1026 | 0.1474 | 0.7103 | 0.0037 | 0.0057 | 0.5714 |

## Mechanischer Kontrast

Gegenueber normaler Oeffnung zeigt echte KAS-Randnaehe:

- Rand/Kipp-Anteil: `+0.3163`
- Offen-Anteil: `-0.2505`
- Zentrum-Anteil: `-0.0274`
- Rohfeldaufnahme: `+0.0622`
- Lautheit: `+0.1001`
- visuelle Unschaerfe: `+0.0846`
- MCM-Spannung: `+0.0454`
- Strain: `+0.0429`
- Rekopplung: `-0.0358`
- absolute Drift: `+0.0189`
- maximale Range: `+0.0945`
- Richtungswechsel: `-0.1223`

## Befund

Normale Oeffnung ist in KAS haeufig. Echte Randnaehe ist selten, aber deutlich.
Der Unterschied liegt nicht in einem einzelnen Wert, sondern in einer Kopplung aus Feldoeffnung, erhoehter Rohfeldaufnahme, hoher Lautheit, geringerer Schaerfe und realer Weltbewegung.

Fuer die Mechanik bedeutet das: MINI_DIO sollte Oeffnung nicht automatisch als Gefahr lesen. Erst wenn Oeffnung mit Rand/Kipp-Naehe, Rohfeldlast und Rekopplungsverlust zusammenfaellt, entsteht eine belastete Feldlage.

## Konsequenz Fuer MINI_DIO

- Rezeptorische Wahrnehmung bleibt vor dem Feld.
- Das MCM-Feld bewertet keine Einzelachse isoliert.
- Randnaehe ist ein Feldzustand aus Zusammenwirkung, kein harter Sensorwert.
- Fuer ein spaeteres DIO-Handlungssystem ist diese Trennung zentral: offene Wahrnehmung darf beobachtbar bleiben, ohne sofort als Blockade oder Aktion gelesen zu werden.

## Wie es weitergeht

Als naechstes sollte diese KAS-Kontrastsignatur gegen PAXG geprueft werden. Ziel: verstehen, warum PAXG trotz Hochlast weniger echte Randnaehe ausbildet.
