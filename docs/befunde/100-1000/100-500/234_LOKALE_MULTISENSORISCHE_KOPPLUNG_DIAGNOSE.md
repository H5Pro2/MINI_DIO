# Lokale multisensorische Kopplung - Diagnose

Stand: 2026-06-19 07:18:05

## Zweck

Diese Diagnose liest kurze Abschnitte innerhalb einer Welt.
Sie prueft, ob Hoeren, Sehen und Fuehlen lokal gemeinsam kippen oder rekoppeln.

Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.

Hierarchie der Pruefung:

1. Grundfrage: Gibt es gemeinsame Sinnesinnenlagen innerhalb einer Welt?
2. Unterpruefung: Wo steigen Hoerlast, Sehlast und Felddruck lokal gemeinsam?
3. Folgeschritt: Pruefen, ob lokale Kippnaehe nur kurz aufflammt oder wiederkehrende Innenfeldinseln bildet.

## Rollen nach Welt

| Welt | lokal offen | lokal rekoppelnd | Sinnesreiben | Kippnaehe |
|---|---:|---:|---:|---:|
| SOL_2024_1H | 58 | 18 | 0 | 20 |
| SOL_2024_30M | 47 | 29 | 0 | 20 |
| SOL_2024_5M | 47 | 29 | 0 | 20 |
| SOL_2025_1H | 50 | 26 | 0 | 20 |
| SOL_2025_30M | 47 | 29 | 0 | 20 |
| SOL_2025_5M | 47 | 29 | 2 | 18 |
| STRESS_2023_TEST4 | 1 | 0 | 0 | 1 |
| STRESS_2024_REAL | 1 | 0 | 0 | 1 |
| STRESS_2025_STRESS | 1 | 0 | 0 | 1 |

## Staerkste lokale Kippnaehe

| Welt | Lauf | Ticks | Rolle | Hoerlast | Sehlast | Felddruck | Entlastung | Konflikt | Kippnaehe | Rekopplung |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| SOL_2025_1H | 1 | 401-480 | lokale_multisensorische_kippnaehe | 0.2860 | 0.5880 | 0.2701 | 0.6519 | 0.3715 | 0.3664 | 0.565454 |
| SOL_2025_1H | 2 | 401-480 | lokale_multisensorische_kippnaehe | 0.2861 | 0.5880 | 0.2700 | 0.6518 | 0.3714 | 0.3664 | 0.565049 |
| SOL_2024_1H | 1 | 1761-1840 | lokale_multisensorische_kippnaehe | 0.2676 | 0.5634 | 0.2603 | 0.6586 | 0.3846 | 0.3547 | 0.572289 |
| SOL_2024_1H | 2 | 1761-1840 | lokale_multisensorische_kippnaehe | 0.2677 | 0.5634 | 0.2603 | 0.6584 | 0.3845 | 0.3547 | 0.571854 |
| SOL_2025_30M | 1 | 881-960 | lokale_multisensorische_kippnaehe | 0.2529 | 0.5640 | 0.2646 | 0.6540 | 0.3853 | 0.3530 | 0.568098 |
| SOL_2025_30M | 2 | 881-960 | lokale_multisensorische_kippnaehe | 0.2530 | 0.5640 | 0.2646 | 0.6538 | 0.3852 | 0.3530 | 0.567743 |
| SOL_2025_1H | 1 | 1321-1400 | lokale_multisensorische_kippnaehe | 0.2270 | 0.5722 | 0.2603 | 0.6545 | 0.4204 | 0.3528 | 0.570605 |
| SOL_2025_1H | 2 | 1321-1400 | lokale_multisensorische_kippnaehe | 0.2271 | 0.5722 | 0.2602 | 0.6543 | 0.4203 | 0.3528 | 0.570205 |
| SOL_2024_1H | 1 | 1841-1920 | lokale_multisensorische_kippnaehe | 0.2464 | 0.5612 | 0.2619 | 0.6539 | 0.3997 | 0.3521 | 0.569142 |
| SOL_2024_1H | 2 | 1841-1920 | lokale_multisensorische_kippnaehe | 0.2465 | 0.5612 | 0.2619 | 0.6538 | 0.3996 | 0.3521 | 0.568744 |
| SOL_2025_30M | 1 | 841-920 | lokale_multisensorische_kippnaehe | 0.2537 | 0.5636 | 0.2626 | 0.6577 | 0.3799 | 0.3515 | 0.571578 |
| SOL_2025_30M | 2 | 841-920 | lokale_multisensorische_kippnaehe | 0.2538 | 0.5636 | 0.2625 | 0.6576 | 0.3798 | 0.3515 | 0.571235 |

## Staerkste lokale Rekopplung / Entlastung

| Welt | Lauf | Ticks | Rolle | Entlastung | Fit | Rekopplung | Feldlast | Nachhall |
|---|---:|---|---|---:|---:|---:|---:|---:|
| SOL_2025_5M | 1 | 1521-1600 | lokal_rekoppelnd | 0.7214 | 0.9793 | 0.647802 | 0.1626 | 0.0050 |
| SOL_2025_5M | 2 | 1521-1600 | lokal_rekoppelnd | 0.7213 | 0.9792 | 0.647412 | 0.1624 | 0.0050 |
| SOL_2025_5M | 1 | 561-640 | lokal_rekoppelnd | 0.7204 | 0.9917 | 0.643751 | 0.1713 | 0.0007 |
| SOL_2025_5M | 2 | 561-640 | lokal_rekoppelnd | 0.7202 | 0.9916 | 0.643365 | 0.1711 | 0.0007 |
| SOL_2025_5M | 1 | 1801-1880 | lokal_rekoppelnd | 0.7192 | 0.9812 | 0.646882 | 0.1637 | 0.0027 |
| SOL_2025_5M | 2 | 1801-1880 | lokal_rekoppelnd | 0.7191 | 0.9811 | 0.646479 | 0.1635 | 0.0027 |
| SOL_2025_5M | 1 | 1481-1560 | lokal_rekoppelnd | 0.7181 | 0.9762 | 0.642570 | 0.1738 | 0.0028 |
| SOL_2025_5M | 2 | 1481-1560 | lokal_rekoppelnd | 0.7180 | 0.9760 | 0.642203 | 0.1736 | 0.0028 |
| SOL_2025_5M | 1 | 761-840 | lokal_rekoppelnd | 0.7176 | 0.9908 | 0.642487 | 0.1686 | 0.0010 |
| SOL_2025_5M | 2 | 761-840 | lokal_rekoppelnd | 0.7175 | 0.9906 | 0.642090 | 0.1684 | 0.0010 |
| SOL_2025_5M | 1 | 1001-1080 | lokal_rekoppelnd | 0.7169 | 0.9893 | 0.643044 | 0.1676 | 0.0024 |
| SOL_2025_5M | 1 | 1281-1360 | lokal_rekoppelnd | 0.7168 | 0.9819 | 0.643669 | 0.1673 | 0.0023 |

## Vorlaeufige Lesart

Die Rollen werden relativ innerhalb der jeweiligen Welt gelesen.
Eine lokale Kippnaehe ist also kein absoluter Grenzwert, sondern ein Abschnitt, der gegen seine eigene Welt deutlich hervortritt.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Darin wird bewertet, ob lokale Kippnaehe nur Oberflaechenvarianz ist oder eine wiederkehrende multisensorische Innenfeldinsel bildet.
