# 1837 - MCM-Reifungsbahn mit assetnahen 17k-Nullwelten

Stand: 2026-07-08 23:43:18

## Grundfrage

Verstärkt ein längeres gemeinsames Weltfenster die Trennung zwischen Realwelt und assetnaher Nullwelt?

## Grundlage

Gelesen wurden vorhandene MINI_DIO-Läufe, ohne neue Handlung, Gate-Logik oder Strategie:

- BTC, DOGE, PAXG und XRP wurden als 17k-Realwelten gegen je zwei assetnahe 17k-Nullwelten gelesen. DOGE, PAXG und XRP wurden dafür aus den vorhandenen 2024-01/2024-02-Rohmonaten normalisiert.
- je Realwelt zwei assetnahe Nullwelten: `shuffle_order` und `random_sign`

Die Nullwelten wurden längengleich erzeugt. `shuffle_order` entkoppelt die Reihenfolge der Kerzenformen, `random_sign` entkoppelt das Richtungszeichen bei erhaltener Grundform. Der Nullwelt-Abstand wird assetnah berechnet: BTC gegen BTC-Null, DOGE gegen DOGE-Null, PAXG gegen PAXG-Null, XRP gegen XRP-Null.

## Reifeprofile

| Welt | Gruppe | Kerzen | Symbole | Familien | Bedeutung | Rollenvarianz | Adaptive Rekopplung | Feldzeitdruck | Nullwelt-Abstand | Reifedruck | Zustand |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| BTC_2024_5M_17K | realwelt_2024 | 17000.0000 | 780.0000 | 776.0000 | 0.9442 | 0.5334 | 0.7440 | 0.8030 | 0.6262 | 0.7465 | feldzeit_reif |
| DOGE_2024_5M_17K | realwelt_2024 | 17000.0000 | 826.0000 | 822.0000 | 1.0000 | 0.4942 | 0.7446 | 0.8022 | 1.0000 | 0.8116 | feldzeit_reif |
| PAXG_2024_5M_17K | realwelt_2024 | 17000.0000 | 606.0000 | 601.0000 | 0.7324 | 0.4272 | 0.7533 | 0.8217 | 0.5334 | 0.6832 | feldzeit_reif |
| XRP_2024_5M_17K | realwelt_2024 | 17000.0000 | 812.0000 | 807.0000 | 0.9824 | 0.5204 | 0.7440 | 0.8032 | 0.9898 | 0.8113 | feldzeit_reif |
| BTC_NULL_RANDOM_SIGN_2024_5M_17K | nullwelt_17k | 17000.0000 | 784.0000 | 778.0000 | 0.9478 | 0.4802 | 0.7476 | 0.8040 | 0.1687 | 0.6629 | breit_getragen |
| BTC_NULL_SHUFFLE_2024_5M_17K | nullwelt_17k | 17000.0000 | 680.0000 | 674.0000 | 0.8216 | 0.4930 | 0.7440 | 0.8108 | 0.0000 | 0.6160 | breit_getragen |
| DOGE_NULL_RANDOM_SIGN_2024_5M_17K | nullwelt_17k | 17000.0000 | 821.0000 | 818.0000 | 0.9945 | 0.4900 | 0.7489 | 0.8030 | 0.2365 | 0.6839 | breit_getragen |
| DOGE_NULL_SHUFFLE_2024_5M_17K | nullwelt_17k | 17000.0000 | 674.0000 | 671.0000 | 0.8161 | 0.5034 | 0.7458 | 0.8126 | 0.0002 | 0.6178 | breit_getragen |
| PAXG_NULL_RANDOM_SIGN_2024_5M_17K | nullwelt_17k | 17000.0000 | 590.0000 | 585.0000 | 0.7130 | 0.4257 | 0.7519 | 0.8209 | 0.0797 | 0.6040 | breit_getragen |
| PAXG_NULL_SHUFFLE_2024_5M_17K | nullwelt_17k | 17000.0000 | 540.0000 | 536.0000 | 0.6529 | 0.4398 | 0.7511 | 0.8250 | 0.0000 | 0.5836 | breit_getragen |
| XRP_NULL_RANDOM_SIGN_2024_5M_17K | nullwelt_17k | 17000.0000 | 773.0000 | 769.0000 | 0.9357 | 0.5149 | 0.7476 | 0.8055 | 0.1254 | 0.6597 | breit_getragen |
| XRP_NULL_SHUFFLE_2024_5M_17K | nullwelt_17k | 17000.0000 | 695.0000 | 692.0000 | 0.8416 | 0.5256 | 0.7455 | 0.8108 | 0.0000 | 0.6252 | breit_getragen |

## Lesung

- Zustandsverteilung: `{'feldzeit_reif': 4, 'breit_getragen': 8}`
- Mittlerer Reifedruck 2024-Realwelt: `0.7631`
- Mittlerer Reifedruck Nullwelt: `0.6316`

Die assetnahen Nullwelten fallen nicht leer aus. Sie können stabile, breite und gut rekoppelte Innenfeldlagen bilden. Damit ist klar: Stabilität allein reicht nicht als Reifebeleg. Die strengere Lesung entsteht aus der Kombination von Bedeutungsbreite, Rollenvarianz, Feldzeitdruck und assetnahem Nullwelt-Abstand.

BTC, DOGE und XRP bleiben in der Realwelt weiterhin stärker feldzeitlich gereift als ihre direkten Nullformen. PAXG bleibt der Sonderfall: Es liest sich ruhiger und schmaler, nicht als Bruch der Topologie, sondern als andere Weltspannung. Das bestätigt die bisherige Lesung, dass MINI_DIO nicht jedes Asset gleich behandelt.

## Grenze

Die Nullwelten sind Kontrollwelten, aber keine vollständige Widerlegung von Weltstruktur. Sie erhalten lokale Kerzenform, Länge und Verteilung. Deshalb prüfen sie vor allem, ob Reihenfolge, Richtung und asseteigene Spannung eine zusätzliche Feldordnung erzeugen.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob die 17k-Reifeprofile dieselben Topfamilien und Feldrollen tragen wie die 10k-Profile oder ob mit wachsender Länge neue Rand- und Brückenrollen entstehen.
