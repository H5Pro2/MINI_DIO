# 1835 - MCM-Reifungsbahn Gegenprüfung 2024 mit 10k-Nullwelten

Stand: 2026-07-08 23:22:15

## Grundfrage

Wiederholt sich die passive Reifungsbahn in vorhandenen 2024-Assetwelten, oder war `feldzeit_reif` nur ein 2025-10k-Effekt?

## Grundlage

Gelesen wurden vorhandene MINI_DIO-Läufe, ohne neue Handlung, Gate-Logik oder Strategie:

- BTC 2024 5m 10k
- DOGE 2024 5m 10k
- PAXG 2024 5m 10k
- XRP 2024 5m 10k
- zwei 10k-Nullwelten aus BTC 2024 5m

Die Nullwelten wurden längengleich erzeugt. `shuffle_order` entkoppelt die Reihenfolge der Kerzenformen, `random_sign` entkoppelt das Richtungszeichen bei erhaltener Grundform.

## Reifeprofile

| Welt | Gruppe | Kerzen | Symbole | Familien | Bedeutung | Rollenvarianz | Adaptive Rekopplung | Feldzeitdruck | Nullwelt-Abstand | Reifedruck | Zustand |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| BTC_2024_5M_10K | realwelt_2024 | 10000.0000 | 689.0000 | 685.0000 | 1.0000 | 0.5936 | 0.7041 | 0.5650 | 1.0000 | 0.7843 | feldzeit_reif |
| DOGE_2024_5M_10K | realwelt_2024 | 10000.0000 | 685.0000 | 679.0000 | 0.9927 | 0.6106 | 0.7041 | 0.5640 | 0.9591 | 0.7789 | feldzeit_reif |
| PAXG_2024_5M_10K | realwelt_2024 | 10000.0000 | 528.0000 | 527.0000 | 0.7678 | 0.4697 | 0.7139 | 0.5776 | 0.2577 | 0.6057 | breit_getragen |
| XRP_2024_5M_10K | realwelt_2024 | 10000.0000 | 685.0000 | 680.0000 | 0.9934 | 0.6111 | 0.7046 | 0.5641 | 0.9645 | 0.7802 | feldzeit_reif |
| NULL_RANDOM_SIGN_2024_5M_10K | nullwelt_10k | 10000.0000 | 663.0000 | 657.0000 | 0.9607 | 0.4790 | 0.7466 | 0.7672 | 0.0989 | 0.6472 | breit_getragen |
| NULL_SHUFFLE_2024_5M_10K | nullwelt_10k | 10000.0000 | 587.0000 | 583.0000 | 0.8515 | 0.5347 | 0.7431 | 0.7747 | 0.0000 | 0.6220 | breit_getragen |

## Lesung

- Zustandsverteilung: `{'feldzeit_reif': 3, 'breit_getragen': 3}`
- Mittlerer Reifedruck 2024-Realwelt: `0.7373`
- Mittlerer Reifedruck Nullwelt: `0.6346`

Die vorhandenen 2024-Assetwelten werden mehrheitlich als `feldzeit_reif` gelesen. Die 10k-Nullwelten fallen nicht leer aus und werden durch ihre Länge ebenfalls `breit_getragen`. Der Unterschied liegt daher nicht in einem einfachen Stabil-gegen-Instabil-Schema, sondern in der stärkeren Feldzeitreife und im höheren Nullwelt-Abstand der meisten Realwelten. Nullwelt kann Nachhall, Stabilität und Rekopplung tragen; das verschärft die Methode, weil Reife nicht mehr über eine einzelne Klasse behauptet werden darf.

PAXG 2024 fällt schmaler aus als BTC/DOGE/XRP und liegt in dieser Lesung ebenfalls bei `breit_getragen`. Das passt zur bisherigen Beobachtung, dass PAXG lokal anders färbt, ohne die Grundtopologie zu brechen. Gleichzeitig zeigt es: `feldzeit_reif` ist kein automatischer Asset-Stempel, sondern entsteht nur bei ausreichender Breite, Abstand und Feldzeitbindung.

## Grenze

Die Nullwelten sind aus BTC 2024 abgeleitet. Für eine noch härtere Aussage sollten zusätzliche Nullwelten aus DOGE, PAXG und XRP erzeugt werden.
