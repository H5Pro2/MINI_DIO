# Feldruhige Fensterselektion

## Zweck

Diese Diagnose korrigiert die reine Rohwelt-Quiet-Extraktion.

Rohweltlich ruhig bedeutet nicht automatisch innenfeldruhig. Deshalb werden mehrere rohweltlich ruhige Kandidaten passiv durch MINI_DIO gelesen und danach nach Feldruhe sortiert.

## Quelle

- Quelle: `data\1-12_2025_5m_SOLUSDT.csv`

## Methode

1. Rohweltlich ruhige Fenster suchen.
2. Ueberlappende Kandidaten reduzieren.
3. Jeden Kandidaten passiv durch MINI_DIO laufen lassen.
4. Topologie aus den Episoden lesen.
5. Relativ nach Feldruhe sortieren.

Die Sortierung ist Diagnose, keine Runtime-Regel.

## Kandidaten

| Rang | Kandidat | Start | Ende | Rohquiet | Feldquiet | Topologie | Zentrum | Offen | Rand | Rekopplung | Carry | Strain | Syntax | Memory |
|---:|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | SOL2025_FIELD_QUIET_02 | 103120 | 105120 | 0.5427 | 0.4663 | stark_zentriert_wenig_rand | 0.8029 | 0.1881 | 0.0090 | 0.6959 | 0.5120 | 0.1549 | 342 | 3 |
| 2 | SOL2025_FIELD_QUIET_04 | 101750 | 103750 | 0.5640 | 0.4589 | gemischte_rollenordnung | 0.7894 | 0.2031 | 0.0075 | 0.6949 | 0.5104 | 0.1554 | 345 | 3 |
| 3 | SOL2025_FIELD_QUIET_01 | 52250 | 54250 | 0.5368 | 0.4485 | gemischte_rollenordnung | 0.7703 | 0.2192 | 0.0105 | 0.6940 | 0.5101 | 0.1565 | 337 | 3 |
| 4 | SOL2025_FIELD_QUIET_05 | 69750 | 71750 | 0.5900 | 0.4461 | gemischte_rollenordnung | 0.7658 | 0.2282 | 0.0060 | 0.6933 | 0.5089 | 0.1570 | 359 | 5 |
| 5 | SOL2025_FIELD_QUIET_03 | 34500 | 36500 | 0.5526 | 0.4333 | gemischte_rollenordnung | 0.7397 | 0.2548 | 0.0055 | 0.6939 | 0.5099 | 0.1559 | 329 | 3 |

## Befund

- Feldruhigster Kandidat: `SOL2025_FIELD_QUIET_02`
- Rohweltlicher Start/Ende: `103120` / `105120`
- Topologie: `stark_zentriert_wenig_rand`
- Zentrum: `0.8029`
- Offen: `0.1881`
- Rand/Kipp: `0.0090`

Der Befund trennt die Ebenen:

```text
Rohweltliche Ruhe = Eigenschaft des Aussenfensters.
Feldruhe = Eigenschaft der MCM-Innenreaktion.
```

## Wie es weitergeht

Als naechstes sollte der feldruhigste Kandidat direkt gegen das reale Bruchfenster verglichen werden. Ziel: nicht Rohruhe gegen Rohstress, sondern Feldruhe gegen Feldbruch innerhalb derselben Quelle.
