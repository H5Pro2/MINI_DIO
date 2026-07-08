# 1834 - MCM-Reifungsbahn Gegenprüfung 2024

Stand: 2026-07-08 23:11:32

## Grundfrage

Wiederholt sich die passive Reifungsbahn in vorhandenen 2024-Assetwelten, oder war `feldzeit_reif` nur ein 2025-10k-Effekt?

## Grundlage

Gelesen wurden vorhandene MINI_DIO-Läufe, ohne neue Handlung, Gate-Logik oder Strategie:

- DOGE 2024 5m 10k
- PAXG 2024 5m 10k
- XRP 2024 5m 10k
- zwei Nullwelten aus der 1831-Kontrollfläche

BTC 2024 5m 10k wurde in diesem Schritt nicht aufgenommen, weil kein gleichartig benannter 10k-Lauf im aktuellen Debugbestand vorliegt. Das ist eine Datenlücke, kein Negativbefund.

## Reifeprofile

| Welt | Gruppe | Kerzen | Symbole | Familien | Bedeutung | Rollenvarianz | Adaptive Rekopplung | Feldzeitdruck | Nullwelt-Abstand | Reifedruck | Zustand |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| DOGE_2024_5M_10K | realwelt_2024 | 10000.0000 | 685.0000 | 679.0000 | 0.9993 | 0.7395 | 0.7041 | 0.5640 | 0.9989 | 0.8081 | feldzeit_reif |
| PAXG_2024_5M_10K | realwelt_2024 | 10000.0000 | 528.0000 | 527.0000 | 0.7729 | 0.5688 | 0.7139 | 0.5776 | 0.6725 | 0.6922 | feldzeit_reif |
| XRP_2024_5M_10K | realwelt_2024 | 10000.0000 | 685.0000 | 680.0000 | 1.0000 | 0.7401 | 0.7046 | 0.5641 | 1.0000 | 0.8087 | feldzeit_reif |
| NULL_RANDOM_2400 | nullwelt | 2400.0000 | 221.0000 | 221.0000 | 0.3238 | 0.2975 | 0.7174 | 0.6979 | 0.0012 | 0.4809 | nullweltnah |
| NULL_SHUFFLE_2400 | nullwelt | 2400.0000 | 224.0000 | 222.0000 | 0.3267 | 0.2975 | 0.7078 | 0.6878 | 0.0005 | 0.4758 | nullweltnah |

## Lesung

- Zustandsverteilung: `{'feldzeit_reif': 3, 'nullweltnah': 2}`
- Mittlerer Reifedruck 2024-Realwelt: `0.7697`
- Mittlerer Reifedruck Nullwelt: `0.4784`

Die vorhandenen 2024-Assetwelten werden ebenfalls als `feldzeit_reif` gelesen. Die Nullwelten bleiben in dieser Gegenprüfung `nullweltnah`. Damit wiederholt sich die Trennung aus 1833 in strengerer Form: Nullwelt kann Nachhall und Rekopplung tragen, bleibt aber ohne vergleichbare Bedeutungsbreite und ohne starken Abstand zur Kontrollfläche.

PAXG 2024 fällt schmaler aus als DOGE/XRP, bleibt aber über Rekopplung und Feldzeitdruck noch innerhalb der reifen Lesung. Das passt zur bisherigen Beobachtung, dass PAXG lokal anders färbt, ohne die Grundtopologie zu brechen.

## Grenze

Die Prüfung nutzt vorhandene 2024-Läufe und keine neu erzeugte vollständige 2024-Dämpfungsreihe. Für eine härtere Aussage sollte dieselbe Logik mit BTC 2024 10k, 2024-Nullwelten gleicher Länge und größeren Fenstern wiederholt werden.

## Wie es weitergeht

Als nächstes sollte ein sauberer 2024-10k-Satz mit BTC, DOGE, PAXG, XRP und längengleichen Nullwelten erzeugt werden. Danach kann geprüft werden, ob `feldzeit_reif` über Assets, Jahre und Nullweltformen stabil unterscheidet.
