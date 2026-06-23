# BTC 2025 Feldruhe - Methodik-Synthese

Stand: 2026-06-23

## Zweck

Diese Notiz prueft, ob die zweistufige Feldruhe-Methode auch auf BTC 2025 traegt.

Die Methode trennt:

```text
Rohweltliche Ruhe = Eigenschaft des Aussenfensters.
Feldruhe = Eigenschaft der MCM-Innenreaktion.
```

Damit wird vermieden, ein rohweltlich ruhiges Fenster automatisch als innenfeldruhig zu lesen.

## Datengrundlage

- Quelle: `data\1-12_2025_5m_BTCUSDT.csv`
- Kandidaten: 5 nicht stark ueberlappende ruhige Rohweltfenster
- Fensterlaenge: 2000 Zeilen
- Auswertung: passive MINI_DIO-Forschungskette pro Kandidat

## Ergebnis der BTC-2025-Pruefung

Der feldruhigste Kandidat war:

```text
BTC2025_FIELD_QUIET_03
Start: 52750
Ende: 54750
Topologie: stark_zentriert_wenig_rand
Zentrum: 0.8300
Offen:   0.1655
Rand:    0.0045
```

Die Reproduktionsnaehe blieb vollstaendig stabil:

```text
Top-Syntax-Ueberlappung:   1.0
Top-Familien-Ueberlappung: 1.0
```

## Rohruhe gegen Feldruhe

Auch bei BTC gilt:

```text
Der rohweltlich ruhigste Kandidat ist nicht automatisch der feldruhigste Kandidat.
```

Konkret:

```text
Rohquiet-Rang 1:  BTC2025_FIELD_QUIET_01
Feldquiet-Rang 1: BTC2025_FIELD_QUIET_03
```

Das bestaetigt die methodische Korrektur aus SOL 2025.

## Topologische Lesung

Die fuenf Kandidaten blieben ueberwiegend zentrumsnah:

| Rang | Kandidat | Topologie | Zentrum | Offen | Rand/Kipp |
|---:|---|---|---:|---:|---:|
| 1 | BTC2025_FIELD_QUIET_03 | stark_zentriert_wenig_rand | 0.8300 | 0.1655 | 0.0045 |
| 2 | BTC2025_FIELD_QUIET_02 | stark_zentriert_wenig_rand | 0.8285 | 0.1665 | 0.0050 |
| 3 | BTC2025_FIELD_QUIET_01 | stark_zentriert_wenig_rand | 0.8089 | 0.1830 | 0.0080 |
| 4 | BTC2025_FIELD_QUIET_04 | stark_zentriert_wenig_rand | 0.8019 | 0.1946 | 0.0035 |
| 5 | BTC2025_FIELD_QUIET_05 | gemischte_rollenordnung | 0.7999 | 0.1936 | 0.0065 |

Damit bleibt die Grundordnung stabil:

```text
BTC 2025 bildet keine Gegen-Topologie.
BTC 2025 bestaetigt die robuste Zentrum-Peripherie-Lesung.
```

## Fachliche Ableitung

Die BTC-Pruefung stuetzt drei Punkte:

1. Feldruhe ist keine einfache Kopie roher Kursruhe.
2. MINI_DIO liest eine eigene Innenfeldordnung.
3. Die robuste Topologie bleibt auch bei anderem Asset erhalten.

Wichtig:

```text
Das ist ein Befund der passiven Innenfeldlesung.
Es ist keine Handelsregel und kein Runtime-Gate.
```

## Bedeutung fuer MINI_DIO

BTC 2025 zeigt, dass die feldruhige Auswahl assetuebergreifend sinnvoll ist.

Die MCM-Innenreaktion wirkt nicht wie ein einfacher Volatilitaetsmesser. Sie sortiert die Welt nach:

- zentrumsnaher Integration,
- offener Feldwirkung,
- Rand-/Kippnaehe,
- Rekopplung,
- Carry,
- Strain.

Damit wird die naechste Forschungsfrage klarer:

```text
Welche Aussenweltformen erzeugen feldruhige Innenordnung,
und welche erzeugen offene oder randnahe Feldlagen?
```

## Wie es weitergeht

Als naechstes sollte SOL 2025 gegen BTC 2025 direkt verglichen werden. Ziel: pruefen, ob Feldruhe nur innerhalb eines Assets relativ ist oder ob sich assetuebergreifend eine aehnliche MCM-Feldordnung zeigt.
