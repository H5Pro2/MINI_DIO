# 1834 - MCM-Reifungsbahn Gegenprüfung 2024

Stand: 2026-07-08 23:14:08

## Grundfrage

Wiederholt sich die passive Reifungsbahn in vorhandenen 2024-Assetwelten, oder war `feldzeit_reif` nur ein 2025-10k-Effekt?

## Grundlage

Gelesen wurden vorhandene MINI_DIO-Läufe, ohne neue Handlung, Gate-Logik oder Strategie:

- BTC 2024 5m 10k
- DOGE 2024 5m 10k
- PAXG 2024 5m 10k
- XRP 2024 5m 10k
- zwei Nullwelten aus der 1831-Kontrollfläche

Die Nullwelten sind in diesem Schritt noch 2400 Kerzen lang und dienen als vorhandene Kontrollfläche. Das ist methodisch schwächer als gleichlange Nullwelten, aber ausreichend für eine erste 2024-Gegenprüfung.

## Reifeprofile

| Welt | Gruppe | Kerzen | Symbole | Familien | Bedeutung | Rollenvarianz | Adaptive Rekopplung | Feldzeitdruck | Nullwelt-Abstand | Reifedruck | Zustand |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| BTC_2024_5M_10K | realwelt_2024 | 10000.0000 | 689.0000 | 685.0000 | 1.0000 | 0.7189 | 0.7041 | 0.5650 | 1.0000 | 0.8052 | feldzeit_reif |
| DOGE_2024_5M_10K | realwelt_2024 | 10000.0000 | 685.0000 | 679.0000 | 0.9927 | 0.7395 | 0.7041 | 0.5640 | 0.9921 | 0.8059 | feldzeit_reif |
| PAXG_2024_5M_10K | realwelt_2024 | 10000.0000 | 528.0000 | 527.0000 | 0.7678 | 0.5688 | 0.7139 | 0.5776 | 0.6679 | 0.6906 | feldzeit_reif |
| XRP_2024_5M_10K | realwelt_2024 | 10000.0000 | 685.0000 | 680.0000 | 0.9934 | 0.7401 | 0.7046 | 0.5641 | 0.9931 | 0.8065 | feldzeit_reif |
| NULL_RANDOM_2400 | nullwelt | 2400.0000 | 221.0000 | 221.0000 | 0.3217 | 0.2975 | 0.7174 | 0.6979 | 0.0012 | 0.4806 | nullweltnah |
| NULL_SHUFFLE_2400 | nullwelt | 2400.0000 | 224.0000 | 222.0000 | 0.3246 | 0.2975 | 0.7078 | 0.6878 | 0.0005 | 0.4755 | nullweltnah |

## Lesung

- Zustandsverteilung: `{'feldzeit_reif': 4, 'nullweltnah': 2}`
- Mittlerer Reifedruck 2024-Realwelt: `0.7770`
- Mittlerer Reifedruck Nullwelt: `0.4780`

Die vorhandenen 2024-Assetwelten werden ebenfalls als `feldzeit_reif` gelesen. Die Nullwelten bleiben in dieser Gegenprüfung `nullweltnah`. Damit wiederholt sich die Trennung aus 1833 in strengerer Form: Nullwelt kann Nachhall und Rekopplung tragen, bleibt aber ohne vergleichbare Bedeutungsbreite und ohne starken Abstand zur Kontrollfläche.

PAXG 2024 fällt schmaler aus als DOGE/XRP, bleibt aber über Rekopplung und Feldzeitdruck noch innerhalb der reifen Lesung. Das passt zur bisherigen Beobachtung, dass PAXG lokal anders färbt, ohne die Grundtopologie zu brechen.

## Grenze

Die Prüfung nutzt vorhandene 2024-Läufe und keine neu erzeugte vollständige 2024-Dämpfungsreihe. Für eine härtere Aussage sollte dieselbe Logik mit 2024-Nullwelten gleicher Länge und größeren Fenstern wiederholt werden.

## Wie es weitergeht

Als nächstes sollten längengleiche 2024-Nullwelten erzeugt werden. Danach kann geprüft werden, ob `feldzeit_reif` über Assets, Jahre und Nullweltformen stabil unterscheidet.
