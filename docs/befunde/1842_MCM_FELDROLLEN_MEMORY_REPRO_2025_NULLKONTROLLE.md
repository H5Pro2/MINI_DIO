# 1842 - MCM-Feldrollen-Memory: 2025-Nullkontrolle

## Grundfrage

Bleibt die passive Reifungsrollen-Lesung in echten 2025-Welten staerker als in assetnahen Random/Shuffle-Nullwelten?

## Methode

- Realwelten: BTC, SOL, DOGE, PAXG und XRP 2025.
- Nullwelten: je Asset eine Random-Sign- und eine Shuffle-Order-Welt gleicher Laenge.
- Bewertet wird nicht der Name einer Familie allein, sondern Reifungsprofil: Phase, Nachhall, Feldzeit, Strain und Quellennaehe.

## Gruppenvergleich

| Gruppe | Welten | Kernfamilien Ø | Oberfläche Ø | Quellennähe Ø | Kernnähe Ø | Nachhall-Delta Ø | Feldzeit-Delta Ø | Zustände |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `real` | 5 | 11.40 | 24.60 | 0.722 | 0.242 | 0.1670 | 0.0831 | `reifungsrolle_teilweise_reproduziert:4; reifungsrolle_reproduziert:1` |
| `null_random` | 5 | 11.00 | 25.00 | 0.682 | 0.234 | 0.1627 | 0.0810 | `reifungsrolle_teilweise_reproduziert:5` |
| `null_shuffle` | 5 | 10.00 | 26.00 | 0.661 | 0.188 | 0.1572 | 0.0787 | `reifungsrolle_teilweise_reproduziert:5` |

## Einzelwelten

| Welt | Art | Kern | Oberfläche | Quellennähe | Kernnähe | Nachhall-Delta | Feldzeit-Delta | Lesung |
|---|---|---:|---:|---:|---:|---:|---:|---|
| BTC random_2025_17k | `null_random` | 13 | 23 | 0.647 | 0.200 | 0.1636 | 0.0825 | `reifungsrolle_teilweise_reproduziert` |
| BTC real_2025_17k | `real` | 12 | 24 | 0.750 | 0.400 | 0.1625 | 0.0821 | `reifungsrolle_teilweise_reproduziert` |
| BTC shuffle_2025_17k | `null_shuffle` | 10 | 26 | 0.680 | 0.222 | 0.1613 | 0.0802 | `reifungsrolle_teilweise_reproduziert` |
| DOGE random_2025_16992 | `null_random` | 10 | 26 | 0.714 | 0.320 | 0.1574 | 0.0790 | `reifungsrolle_teilweise_reproduziert` |
| DOGE real_2025_16992 | `real` | 9 | 27 | 0.714 | 0.185 | 0.1584 | 0.0794 | `reifungsrolle_teilweise_reproduziert` |
| DOGE shuffle_2025_16992 | `null_shuffle` | 11 | 25 | 0.647 | 0.214 | 0.1601 | 0.0800 | `reifungsrolle_teilweise_reproduziert` |
| PAXG random_2025_16992 | `null_random` | 8 | 28 | 0.585 | 0.107 | 0.1528 | 0.0757 | `reifungsrolle_teilweise_reproduziert` |
| PAXG real_2025_16992 | `real` | 13 | 23 | 0.647 | 0.161 | 0.1667 | 0.0821 | `reifungsrolle_teilweise_reproduziert` |
| PAXG shuffle_2025_16992 | `null_shuffle` | 7 | 29 | 0.615 | 0.111 | 0.1541 | 0.0775 | `reifungsrolle_teilweise_reproduziert` |
| SOL random_2025_17k | `null_random` | 14 | 22 | 0.714 | 0.276 | 0.1801 | 0.0885 | `reifungsrolle_teilweise_reproduziert` |
| SOL real_2025_17k | `real` | 13 | 23 | 0.750 | 0.241 | 0.1847 | 0.0911 | `reifungsrolle_reproduziert` |
| SOL shuffle_2025_17k | `null_shuffle` | 11 | 25 | 0.647 | 0.133 | 0.1561 | 0.0785 | `reifungsrolle_teilweise_reproduziert` |
| XRP random_2025_16992 | `null_random` | 10 | 26 | 0.750 | 0.269 | 0.1595 | 0.0794 | `reifungsrolle_teilweise_reproduziert` |
| XRP real_2025_16992 | `real` | 10 | 26 | 0.750 | 0.222 | 0.1628 | 0.0809 | `reifungsrolle_teilweise_reproduziert` |
| XRP shuffle_2025_16992 | `null_shuffle` | 11 | 25 | 0.714 | 0.259 | 0.1544 | 0.0774 | `reifungsrolle_teilweise_reproduziert` |

## Befund

- Realwelten liegen in Quellennähe um `0.040` über der stärksten Nullgruppe.
- Realwelten liegen in Kernnähe um `0.008` über der stärksten Nullgruppe.
- Die Nullwelten bilden ebenfalls stabile Oberflächen und einzelne Kernlesungen.
- Der Unterschied liegt nicht in Ja/Nein, sondern in stärkerer Anschluss- und Kernnähe der realen Weltzeit.

Damit ist der Befund kein einfacher Beweis gegen Rauschen, aber ein stärkerer Hinweis:
MINI_DIO liest in realer Weltzeit mehr zusammenhängende Reifungsnähe als in assetnaher synthetischer Umordnung.

## Wie es weitergeht

Als nächstes sollte die Reifungsrollen-Memory nicht erweitert, sondern strenger geprüft werden:
ein zweiter 2025-Ausschnitt mit anderem Startpunkt zeigt, ob dieselbe Differenz auch außerhalb des Jahresanfangs sichtbar bleibt.
