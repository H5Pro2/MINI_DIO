# Feldruhige Fensterselektion

## Zweck

Diese Diagnose korrigiert die reine Rohwelt-Quiet-Extraktion.

Rohweltlich ruhig bedeutet nicht automatisch innenfeldruhig. Deshalb werden mehrere rohweltlich ruhige Kandidaten passiv durch MINI_DIO gelesen und danach nach Feldruhe sortiert.

## Quelle

- Quelle: `data\1-12_2025_5m_BTCUSDT.csv`

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
| 1 | BTC2025_FIELD_QUIET_03 | 52750 | 54750 | 0.3876 | 0.4814 | stark_zentriert_wenig_rand | 0.8300 | 0.1655 | 0.0045 | 0.6977 | 0.5124 | 0.1519 | 340 | 3 |
| 2 | BTC2025_FIELD_QUIET_02 | 74000 | 76000 | 0.3783 | 0.4810 | stark_zentriert_wenig_rand | 0.8285 | 0.1665 | 0.0050 | 0.6982 | 0.5141 | 0.1520 | 324 | 1 |
| 3 | BTC2025_FIELD_QUIET_01 | 50250 | 52250 | 0.3742 | 0.4697 | stark_zentriert_wenig_rand | 0.8089 | 0.1830 | 0.0080 | 0.6964 | 0.5113 | 0.1535 | 348 | 1 |
| 4 | BTC2025_FIELD_QUIET_04 | 72250 | 74250 | 0.4103 | 0.4663 | stark_zentriert_wenig_rand | 0.8019 | 0.1946 | 0.0035 | 0.6961 | 0.5116 | 0.1538 | 345 | 1 |
| 5 | BTC2025_FIELD_QUIET_05 | 59000 | 61000 | 0.4104 | 0.4649 | gemischte_rollenordnung | 0.7999 | 0.1936 | 0.0065 | 0.6960 | 0.5106 | 0.1536 | 362 | 1 |

## Befund

- Feldruhigster Kandidat: `BTC2025_FIELD_QUIET_03`
- Rohweltlicher Start/Ende: `52750` / `54750`
- Topologie: `stark_zentriert_wenig_rand`
- Zentrum: `0.8300`
- Offen: `0.1655`
- Rand/Kipp: `0.0045`

Der Befund trennt die Ebenen:

```text
Rohweltliche Ruhe = Eigenschaft des Aussenfensters.
Feldruhe = Eigenschaft der MCM-Innenreaktion.
```

## Wie es weitergeht

Als naechstes sollte der feldruhigste Kandidat direkt gegen das reale Bruchfenster verglichen werden. Ziel: nicht Rohruhe gegen Rohstress, sondern Feldruhe gegen Feldbruch innerhalb derselben Quelle.
