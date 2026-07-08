# 1836 - MCM-Reifungsbahn mit assetnahen 10k-Nullwelten

Stand: 2026-07-08 23:31:08

## Grundfrage

Bleibt die passive Reifungsbahn auch dann unterscheidbar, wenn jede Realwelt gegen eigene, längengleiche Nullwelten geprüft wird?

## Grundlage

Gelesen wurden vorhandene MINI_DIO-Läufe, ohne neue Handlung, Gate-Logik oder Strategie:

- BTC 2024 5m 10k
- DOGE 2024 5m 10k
- PAXG 2024 5m 10k
- XRP 2024 5m 10k
- je zwei assetnahe 10k-Nullwelten: `shuffle_order` und `random_sign`

Die Nullwelten wurden längengleich erzeugt. `shuffle_order` entkoppelt die Reihenfolge der Kerzenformen, `random_sign` entkoppelt das Richtungszeichen bei erhaltener Grundform. Der Nullwelt-Abstand wird assetnah berechnet: BTC gegen BTC-Null, DOGE gegen DOGE-Null, PAXG gegen PAXG-Null, XRP gegen XRP-Null.

## Reifeprofile

| Welt | Gruppe | Kerzen | Symbole | Familien | Bedeutung | Rollenvarianz | Adaptive Rekopplung | Feldzeitdruck | Nullwelt-Abstand | Reifedruck | Zustand |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| BTC_2024_5M_10K | realwelt_2024 | 10000.0000 | 689.0000 | 685.0000 | 1.0000 | 0.5936 | 0.7041 | 0.5650 | 0.9431 | 0.7748 | feldzeit_reif |
| DOGE_2024_5M_10K | realwelt_2024 | 10000.0000 | 685.0000 | 679.0000 | 0.9927 | 0.6106 | 0.7041 | 0.5640 | 1.0000 | 0.7857 | feldzeit_reif |
| PAXG_2024_5M_10K | realwelt_2024 | 10000.0000 | 528.0000 | 527.0000 | 0.7678 | 0.4697 | 0.7139 | 0.5776 | 0.5229 | 0.6499 | feldzeit_reif |
| XRP_2024_5M_10K | realwelt_2024 | 10000.0000 | 685.0000 | 680.0000 | 0.9934 | 0.6111 | 0.7046 | 0.5641 | 0.7449 | 0.7436 | feldzeit_reif |
| BTC_NULL_RANDOM_SIGN_2024_5M_10K | nullwelt_10k | 10000.0000 | 663.0000 | 657.0000 | 0.9607 | 0.4790 | 0.7466 | 0.7672 | 0.0932 | 0.6463 | breit_getragen |
| BTC_NULL_SHUFFLE_2024_5M_10K | nullwelt_10k | 10000.0000 | 587.0000 | 583.0000 | 0.8515 | 0.5347 | 0.7431 | 0.7747 | 0.0000 | 0.6220 | breit_getragen |
| DOGE_NULL_RANDOM_SIGN_2024_5M_10K | nullwelt_10k | 10000.0000 | 652.0000 | 648.0000 | 0.9461 | 0.4523 | 0.7458 | 0.7700 | 0.0915 | 0.6395 | breit_getragen |
| DOGE_NULL_SHUFFLE_2024_5M_10K | nullwelt_10k | 10000.0000 | 577.0000 | 574.0000 | 0.8377 | 0.4984 | 0.7442 | 0.7773 | 0.0007 | 0.6147 | breit_getragen |
| PAXG_NULL_RANDOM_SIGN_2024_5M_10K | nullwelt_10k | 10000.0000 | 525.0000 | 521.0000 | 0.7613 | 0.4460 | 0.7495 | 0.7837 | 0.0547 | 0.6050 | breit_getragen |
| PAXG_NULL_SHUFFLE_2024_5M_10K | nullwelt_10k | 10000.0000 | 480.0000 | 477.0000 | 0.6965 | 0.4477 | 0.7491 | 0.7877 | 0.0000 | 0.5858 | breit_getragen |
| XRP_NULL_RANDOM_SIGN_2024_5M_10K | nullwelt_10k | 10000.0000 | 681.0000 | 678.0000 | 0.9891 | 0.4947 | 0.7464 | 0.7680 | 0.1003 | 0.6550 | breit_getragen |
| XRP_NULL_SHUFFLE_2024_5M_10K | nullwelt_10k | 10000.0000 | 600.0000 | 596.0000 | 0.8705 | 0.4561 | 0.7444 | 0.7750 | 0.0001 | 0.6126 | breit_getragen |

## Lesung

- Zustandsverteilung: `{'feldzeit_reif': 4, 'breit_getragen': 8}`
- Mittlerer Reifedruck 2024-Realwelt: `0.7385`
- Mittlerer Reifedruck Nullwelt: `0.6226`

Die assetnahen Nullwelten fallen nicht leer aus. Sie können stabile, breite und gut rekoppelte Innenfeldlagen bilden. Damit ist klar: Stabilität allein reicht nicht als Reifebeleg. Die strengere Lesung entsteht aus der Kombination von Bedeutungsbreite, Rollenvarianz, Feldzeitdruck und assetnahem Nullwelt-Abstand.

BTC, DOGE und XRP bleiben in der Realwelt weiterhin stärker feldzeitlich gereift als ihre direkten Nullformen. PAXG bleibt der Sonderfall: Es liest sich ruhiger und schmaler, nicht als Bruch der Topologie, sondern als andere Weltspannung. Das bestätigt die bisherige Lesung, dass MINI_DIO nicht jedes Asset gleich behandelt.

## Grenze

Die Nullwelten sind Kontrollwelten, aber keine vollständige Widerlegung von Weltstruktur. Sie erhalten lokale Kerzenform, Länge und Verteilung. Deshalb prüfen sie vor allem, ob Reihenfolge, Richtung und asseteigene Spannung eine zusätzliche Feldordnung erzeugen.

## Wie es weitergeht

Als nächstes sollten größere Fenster gegen dieselbe assetnahe Nullweltlogik laufen. Entscheidend ist, ob Feldzeitreife mit wachsender Weltlänge stabiler wird oder ob Nullwelten bei sehr langen Sequenzen ähnliche Rollenbreite ausbilden.
