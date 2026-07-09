# Fensterabhaengige Feldklassen

Stand: 2026-07-05

## Grundfrage

Ist eine Feldklasse an ein Asset gebunden, oder entsteht sie aus der lokalen Weltphase innerhalb eines Ausschnitts?

## Unterpruefung

DOGE, XRP und BTC 2024 5m wurden in 30 passive 1000er-Fenster geschnitten. Jedes Fenster wurde mit frischem Memory und `world_relative` gelesen.

Die Pruefung erzeugt keine Handlung. Sie liest nur, ob das MCM-Feld Einzelrekopplung, Uebergang oder breitere Mehrrollennaehe ausbildet.

## Ergebnis

Aus 30 Fenstern entstanden:

- `13` Fenster mit Einzelrekopplung,
- `13` Fenster mit Uebergang und Randkontakt,
- `4` Fenster als Mehrrollen-Kandidat.

Der zentrale Befund:

```text
Die Feldklasse ist nicht asset-fest.
Sie ist lokal fensterabhaengig.
```

DOGE und XRP waren im Startfenster `0` Einzelrekopplung. In spaeteren Fenstern wurden beide zu Uebergangs- oder Mehrrollen-Kandidaten. BTC zeigte ebenfalls sowohl Einzelrekopplung als auch Uebergang und Mehrrollennaehe.

Damit liest MINI_DIO nicht einfach "DOGE ist so" oder "XRP ist so", sondern reagiert auf die lokale Weltphase.

## Reproduktion

Der staerkste XRP-Mehrrollen-Kandidat `start1000_size1000` wurde als Real-Sleep-Real-Kette erneut geprueft.

Real A und Real B blieben stabil:

- Episoden: `994 -> 994`
- Unique Syntax: `250 -> 250`
- Feldepisoden: `5 -> 5`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

Die Sleep-Phase beruehrte alle 5 Rollen und alle 10 Rollenkombinationen. Im Real-B-Follow-up wurden alle 5 Rollen und alle 10 Kombinationen wieder voll reaktiviert.

Das zeigt:

```text
Die Mehrrollennaehe war reproduzierbar.
Die Sleep-Spur markierte bestehende Rollen.
Sie erfand keine neue Weltbedeutung.
```

## Bedeutung Fuer MINI_DIO

Dieser Befund staerkt die Lesung eines dynamischen MCM-Feldes:

- Einzelrekopplung kann eine lokale ruhige oder dominante Feldphase sein.
- Uebergang entsteht, wenn mehrere Rollen sichtbar werden und Randkontakt dazukommt.
- Mehrrollennaehe entsteht, wenn mehrere tragende Rollen gleichzeitig stabil genug werden.
- Dieselbe Weltfamilie kann je nach Ausschnitt unterschiedliche Feldklassen hervorbringen.

Damit wird die MCM-Topologie nicht als starres Asset-Etikett gelesen, sondern als feldzeitliche Organisation einer konkreten Weltphase.

## Quellen

- [1581 Mehrrollen-Fenstersuche DOGE/XRP/BTC](1581_MEHRROLLEN_FENSTERSUCHE_DOGE_XRP_BTC.md)
- [1582 XRP1000 Mehrrollen-Reproduktion](1582_XRP1000_SCAN_START1000_MEHRROLLEN_REPRO.md)
