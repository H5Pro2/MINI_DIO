# 1699 - Milieu-Relationswechsel und Rohweltphasen

Stand: 2026-07-07 18:32:10

## Zweck

Diese Diagnose liest starke adaptive Milieu-Relationswechsel gegen konkrete Rohweltphasen zurueck.
Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.

## Hierarchie

1. Grundfrage: Welche Weltphasen liegen unter starken Milieu-Wechseln?
2. Unterpruefung: Familien mit `offen_und_gereift -> nur_gereift` und `nur_offen -> offen_und_gereift` vergleichen.
3. Folgeschritt: Wiederkehrende Rohweltprofile als moegliche Milieu-Trigger pruefen.

## Uebersicht

| Transition | Anzahl | Welten |
|---|---:|---|
| nur_gereift->offen_und_gereift | 138 | BTC_2024_5M, DOGE_2024_5M, PAXG_2024_5M, XRP_2024_5M |
| nur_offen->offen_und_gereift | 21 | BTC_2024_5M, DOGE_2024_5M, XRP_2024_5M |
| offen_und_gereift->nur_gereift | 211 | BTC_2024_5M, DOGE_2024_5M, PAXG_2024_5M, XRP_2024_5M |
| offen_und_gereift->nur_offen | 29 | BTC_2024_5M, DOGE_2024_5M, PAXG_2024_5M, XRP_2024_5M |

## Staerkste Wechsel

| Welt | Familie | Wechsel | vorher | Folge | Basis Nettoverlauf % | Folge Nettoverlauf % | Basis Range % | Folge Range % | Basis Hoeren-Gap | Folge Hoeren-Gap | Basis Spannung | Folge Spannung |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PAXG_2024_5M | dio_0z9t | offen_und_gereift->nur_gereift | 63 | 36 | -1.1823 | 0.0495 | 0.0566 | 0.0539 | 0.1104 | 0.1112 | 0.1078 | 0.1078 |
| BTC_2024_5M | dio_0dd2 | offen_und_gereift->nur_gereift | 44 | 37 | -0.1781 | 4.1602 | 0.1039 | 0.0681 | 0.0797 | 0.0806 | 0.0766 | 0.0771 |
| BTC_2024_5M | dio_0z9t | offen_und_gereift->nur_gereift | 35 | 24 | 0.8855 | 3.2716 | 0.0973 | 0.0703 | 0.1133 | 0.1086 | 0.1095 | 0.1044 |
| PAXG_2024_5M | dio_1xrt | offen_und_gereift->nur_gereift | 27 | 32 | -0.9369 | 0.4970 | 0.1102 | 0.0637 | 0.0527 | 0.0519 | 0.0764 | 0.0790 |
| DOGE_2024_5M | dio_07uk | offen_und_gereift->nur_gereift | 26 | 25 | -8.7970 | 2.3289 | 0.2863 | 0.2714 | 0.1310 | 0.1334 | 0.1211 | 0.1225 |
| PAXG_2024_5M | dio_1350 | offen_und_gereift->nur_gereift | 24 | 26 | -0.5906 | 0.0495 | 0.0783 | 0.0843 | 0.0411 | 0.0384 | 0.0513 | 0.0493 |
| PAXG_2024_5M | dio_0fl2 | offen_und_gereift->nur_gereift | 17 | 31 | -1.0340 | 0.0990 | 0.0788 | 0.0675 | 0.0762 | 0.0743 | 0.0739 | 0.0717 |
| DOGE_2024_5M | dio_1o0u | offen_und_gereift->nur_gereift | 26 | 21 | -10.8998 | 1.0490 | 0.3277 | 0.2488 | 0.1821 | 0.1898 | 0.1654 | 0.1707 |
| PAXG_2024_5M | dio_17ct | offen_und_gereift->nur_gereift | 19 | 28 | -1.6208 | 0.4469 | 0.0941 | 0.0567 | 0.1187 | 0.1233 | 0.1114 | 0.1152 |
| XRP_2024_5M | dio_06jk | offen_und_gereift->nur_gereift | 27 | 19 | -8.1177 | -10.0935 | 0.1123 | 0.0991 | 0.1291 | 0.1324 | 0.1226 | 0.1260 |
| PAXG_2024_5M | dio_1nmh | offen_und_gereift->nur_gereift | 21 | 24 | -1.0837 | 0.2979 | 0.0071 | 0.0000 | 0.1763 | 0.1720 | 0.1736 | 0.1686 |
| BTC_2024_5M | dio_1tiu | offen_und_gereift->nur_gereift | 27 | 17 | 0.5949 | 2.7387 | 0.0969 | 0.0619 | 0.0782 | 0.0828 | 0.0755 | 0.0784 |
| DOGE_2024_5M | dio_06jk | offen_und_gereift->nur_gereift | 19 | 25 | -10.6116 | 1.6326 | 0.1409 | 0.1083 | 0.1296 | 0.1233 | 0.1235 | 0.1187 |
| XRP_2024_5M | dio_1r55 | offen_und_gereift->nur_gereift | 28 | 16 | -8.0590 | -7.2056 | 0.0759 | 0.0662 | 0.1277 | 0.1244 | 0.1239 | 0.1185 |
| PAXG_2024_5M | dio_05ap | offen_und_gereift->nur_gereift | 22 | 20 | -1.2821 | 1.0924 | 0.0631 | 0.0547 | 0.0422 | 0.0511 | 0.0483 | 0.0547 |
| XRP_2024_5M | dio_0ly7 | offen_und_gereift->nur_gereift | 20 | 20 | -6.3988 | -6.9417 | 0.1332 | 0.1203 | 0.0405 | 0.0388 | 0.0476 | 0.0462 |
| PAXG_2024_5M | dio_13o0 | offen_und_gereift->nur_gereift | 19 | 20 | -0.6394 | 0.5979 | 0.0991 | 0.1018 | 0.0120 | 0.0112 | 0.0285 | 0.0289 |
| XRP_2024_5M | dio_13o0 | offen_und_gereift->nur_gereift | 20 | 17 | -8.5229 | -7.4543 | 0.1931 | 0.1329 | 0.0147 | 0.0150 | 0.0317 | 0.0324 |
| BTC_2024_5M | dio_1fll | offen_und_gereift->nur_gereift | 21 | 15 | 0.7370 | 3.1601 | 0.1188 | 0.0701 | 0.0176 | 0.0148 | 0.0288 | 0.0257 |
| XRP_2024_5M | dio_17dc | offen_und_gereift->nur_gereift | 23 | 12 | -7.4408 | -6.1572 | 0.2852 | 0.1687 | 0.1349 | 0.1394 | 0.1262 | 0.1262 |
| PAXG_2024_5M | dio_17db | offen_und_gereift->nur_gereift | 24 | 11 | -1.2733 | 0.8969 | 0.0700 | 0.1220 | 0.1763 | 0.1738 | 0.1602 | 0.1608 |
| BTC_2024_5M | dio_13o0 | offen_und_gereift->nur_gereift | 17 | 17 | -1.6293 | 1.5088 | 0.1722 | 0.1418 | 0.0117 | 0.0147 | 0.0301 | 0.0316 |
| XRP_2024_5M | dio_05ap | offen_und_gereift->nur_gereift | 21 | 12 | -7.1592 | -8.5668 | 0.1064 | 0.1116 | 0.0405 | 0.0392 | 0.0468 | 0.0465 |
| BTC_2024_5M | dio_17dc | offen_und_gereift->nur_gereift | 23 | 8 | -5.4607 | 3.2494 | 0.2640 | 0.1972 | 0.1319 | 0.1413 | 0.1210 | 0.1272 |
| DOGE_2024_5M | dio_07o8 | offen_und_gereift->nur_gereift | 11 | 19 | -10.6607 | 0.3699 | 0.2917 | 0.1927 | 0.1362 | 0.1264 | 0.1406 | 0.1298 |
| XRP_2024_5M | dio_0v65 | offen_und_gereift->nur_gereift | 11 | 17 | -5.1091 | -5.4817 | 0.3488 | 0.2463 | 0.0065 | 0.0091 | 0.0473 | 0.0450 |
| DOGE_2024_5M | dio_17dc | offen_und_gereift->nur_gereift | 19 | 8 | -11.3061 | 0.6559 | 0.3420 | 0.2240 | 0.1364 | 0.1377 | 0.1252 | 0.1249 |
| PAXG_2024_5M | dio_0om4 | offen_und_gereift->nur_gereift | 16 | 11 | -0.2979 | 0.8915 | 0.1767 | 0.1579 | 0.0589 | 0.0669 | 0.0756 | 0.0812 |
| BTC_2024_5M | dio_0n0i | offen_und_gereift->nur_gereift | 14 | 12 | -0.6728 | 3.6225 | 0.1862 | 0.1460 | 0.0154 | 0.0122 | 0.0342 | 0.0320 |
| PAXG_2024_5M | dio_0nmc | offen_und_gereift->nur_gereift | 5 | 21 | -0.6897 | 0.6474 | 0.0790 | 0.0686 | 0.2011 | 0.2041 | 0.2051 | 0.2065 |
| DOGE_2024_5M | dio_0jqc | offen_und_gereift->nur_gereift | 14 | 11 | -10.7349 | 1.8919 | 0.1727 | 0.1327 | 0.1173 | 0.1126 | 0.1129 | 0.1083 |
| PAXG_2024_5M | dio_087m | offen_und_gereift->nur_gereift | 12 | 13 | -1.0309 | 0.3471 | 0.1607 | 0.1337 | 0.0721 | 0.0728 | 0.0798 | 0.0775 |

## Lesung

`offen_und_gereift -> nur_gereift` bedeutet: Eine Familie bleibt in der Folgewelt vorhanden, verliert aber ihre offene Schicht und wird enger gereift gelesen.

`nur_offen -> offen_und_gereift` bedeutet: Eine zuvor nur offene Familie bekommt in der Folgewelt zusaetzliche gereifte Anteile.

Die Rohweltspalten dienen als Ruecklesung, nicht als Ursachebeweis. Entscheidend ist, ob solche Wechsel wiederholt mit aehnlichen Spannungs-, Range-, Hoer- oder Feldprofilen auftreten.

## Grenze

Dieser Bericht zeigt Kopplungen zwischen Milieu-Wechsel und Weltphase. Er beweist noch keinen Mechanismus und erzeugt keine neue Regel.
