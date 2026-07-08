# 1731 - Asset-Milieu-Matrix 15m BTC/SOL

## Frage

Nach 5m und 1h wurde geprueft, ob 15m eine eigene Milieuschicht erzeugt oder zwischen beiden Zeitmassen vermittelt.

```text
Bildet 15m eine neue MCM-Rollenordnung,
oder bleibt die bekannte Topologie erhalten?
```

## Datenbasis

Gelesen wurden BTC und SOL:

- BTC 2024 Start/Folge,
- BTC 2025 Start/Folge,
- SOL 2024 Start/Folge,
- SOL 2025 Start/Folge.

Alle Fenster enthalten 5000 Zeilen.

Vollberichte:

```text
reports/asset_milieu_15m_matrix.md
reports/asset_milieu_15m_randdruck_recheck.md
reports/asset_milieu_15m_topology_recheck.md
```

## Mittelwerte

| Asset | Randdruck | Offen | Rekopplung | Daempfung | Lesart |
|---|---:|---:|---:|---:|---|
| BTC | 0.4104 | 0.1530 | 0.3113 | 0.1254 | minimal druck-/rekopplungsnaeher |
| SOL | 0.4082 | 0.1550 | 0.3098 | 0.1271 | minimal offener/daempfender |

## Befund

Alle acht 15m-Welten werden gelesen als:

```text
stark_zentriert_wenig_rand
```

Damit ist 15m bisher kein Topologiebruch.
Die Unterschiede zwischen BTC und SOL sind kleiner als die globale Stabilitaet der Rollenordnung.

## Interpretation

15m wirkt als stabiler Zwischenraum:

```text
5m  = mehr lokale Milieuqualitaet
15m = stabiler Zwischenraum
1h  = staerker geglaettet
```

Diese Lesung ist vorlaeufig, weil 15m aktuell nur fuer BTC und SOL geprueft wurde.

## Bedeutung fuer MINI_DIO

MINI_DIO bildet auch bei mittlerer Zeitauflosung keine neue starre Klasse.
Die Feldordnung bleibt zentrumsnah und passt damit zur bisherigen MCM-Topologie:

```text
Zentrum bleibt tragend.
Offene Variante bleibt klein.
Rand/Kipp bleibt lokal, aber nicht dominant.
```

## Methodische Grenze

Dieser Befund ist keine vollstaendige Asset-Matrix.
PAXG, XRP und DOGE muessen fuer 15m nachgezogen werden, wenn dieselbe Assetbreite wie bei 5m und 1h erreicht werden soll.

## Wie es weitergeht

Als naechstes sollten entweder 15m-Daten fuer PAXG/XRP/DOGE ergaenzt werden oder der Vergleich auf BTC/SOL als Zeitmass-Achse verdichtet werden.
