# 1692 - Wiederkehrende Milieu-Wechsel-Familien

Stand: 2026-07-07 16:44:27

## Zweck

Diese Diagnose verfolgt Familien, die in 2024 und 2025 mit gleicher Milieu-Wechselrichtung wiederkehren.
Sie bleibt passiv: keine Handlung, kein Gate, keine Richtung.

## Hierarchie

1. Grundfrage: Welche wiederkehrenden Familien tragen denselben Milieu-Wechsel ueber Weltjahre?
2. Unterpruefung: Wie aehnlich sind Range, Hoeren-Gap und Feldspannung im Folgezustand?
3. Folgeschritt: Stabile Kandidaten mit weiteren Weltfenstern pruefen.

## Uebersicht

- Wechsel-Familien 2024: `262`
- Wechsel-Familien 2025: `241`
- gemeinsame Familien: `155`
- Familien-Jaccard: `0.4454`
- gleiche Familie plus gleicher Wechsel: `111`

## Wechseltypen

| Wechsel | Familien 2024 | Familien 2025 | gemeinsam | Jaccard |
|---|---:|---:|---:|---:|
| nur_gereift->offen_und_gereift | 92 | 127 | 42 | 0.2373 |
| nur_offen->offen_und_gereift | 23 | 21 | 4 | 0.1000 |
| offen_und_gereift->nur_gereift | 168 | 142 | 61 | 0.2450 |
| offen_und_gereift->nur_offen | 31 | 25 | 4 | 0.0769 |

## Haefigste Wiederkehrfamilien

| Familie | Wechsel | 2024 | 2025 | Folge Range 2024 | Folge Range 2025 | Folge Hoeren 2024 | Folge Hoeren 2025 | Folge Spannung 2024 | Folge Spannung 2025 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_0m49 | nur_gereift->offen_und_gereift | 3 | 3 | 0.1889 | 0.2427 | 0.1877 | 0.1864 | 0.1757 | 0.1757 |
| dio_1qyl | offen_und_gereift->nur_gereift | 3 | 3 | 0.3213 | 0.9661 | 0.0288 | 0.0268 | 0.0542 | 0.0547 |
| dio_1ba6 | offen_und_gereift->nur_gereift | 2 | 3 | 0.5507 | 0.4471 | 0.0081 | 0.0082 | 0.0425 | 0.0359 |
| dio_01kh | offen_und_gereift->nur_gereift | 3 | 1 | 0.3409 | 0.5855 | 0.1202 | 0.1239 | 0.1223 | 0.1252 |
| dio_02x1 | offen_und_gereift->nur_gereift | 3 | 1 | 0.4920 | 0.7432 | 0.1214 | 0.1289 | 0.1292 | 0.1335 |
| dio_033x | offen_und_gereift->nur_gereift | 2 | 2 | 0.9626 | 0.8011 | 0.2851 | 0.2606 | 0.2276 | 0.2019 |
| dio_04q7 | offen_und_gereift->nur_gereift | 2 | 2 | 0.1768 | 0.6381 | 0.0417 | 0.0375 | 0.0546 | 0.0532 |
| dio_0f4r | offen_und_gereift->nur_gereift | 1 | 3 | 0.0664 | 0.3992 | 0.1217 | 0.1267 | 0.1143 | 0.1172 |
| dio_0p8i | offen_und_gereift->nur_gereift | 3 | 1 | 0.5041 | 0.7354 | 0.0277 | 0.0415 | 0.0538 | 0.0620 |
| dio_0u24 | offen_und_gereift->nur_gereift | 2 | 2 | 0.3932 | 0.4897 | 0.0073 | 0.0098 | 0.0409 | 0.0354 |
| dio_10dv | nur_gereift->offen_und_gereift | 2 | 2 | 0.0807 | 0.1653 | 0.1169 | 0.1192 | 0.1133 | 0.1157 |
| dio_1gsb | nur_gereift->offen_und_gereift | 3 | 1 | 0.2898 | 0.6296 | 0.0731 | 0.0726 | 0.0806 | 0.0804 |
| dio_1w94 | offen_und_gereift->nur_gereift | 2 | 2 | 0.2732 | 1.2248 | 0.0575 | 0.0545 | 0.0827 | 0.0817 |
| dio_00pl | offen_und_gereift->nur_gereift | 2 | 1 | 0.1769 | 0.1462 | 0.0214 | 0.0253 | 0.0571 | 0.0569 |
| dio_01hu | nur_gereift->offen_und_gereift | 2 | 1 | 0.0955 | 0.1763 | 0.0740 | 0.0765 | 0.0744 | 0.0760 |
| dio_01q0 | offen_und_gereift->nur_gereift | 2 | 1 | 0.5618 | 0.7131 | 0.0661 | 0.0757 | 0.0757 | 0.0816 |
| dio_02vn | offen_und_gereift->nur_gereift | 2 | 1 | 0.4026 | 1.2631 | 0.0405 | 0.0371 | 0.0854 | 0.0768 |
| dio_047z | offen_und_gereift->nur_gereift | 2 | 1 | 0.3393 | 1.1788 | 0.2537 | 0.2650 | 0.2067 | 0.2069 |
| dio_058t | offen_und_gereift->nur_gereift | 2 | 1 | 0.4608 | 1.9925 | 0.1110 | 0.1199 | 0.1368 | 0.1373 |
| dio_05ap | nur_gereift->offen_und_gereift | 1 | 2 | 0.0782 | 0.1632 | 0.0416 | 0.0444 | 0.0476 | 0.0499 |
| dio_05il | offen_und_gereift->nur_gereift | 2 | 1 | 1.3320 | 1.7449 | 0.0531 | 0.0215 | 0.1049 | 0.0774 |
| dio_07o8 | offen_und_gereift->nur_gereift | 1 | 2 | 0.1760 | 0.3442 | 0.1263 | 0.1329 | 0.1295 | 0.1348 |
| dio_092o | offen_und_gereift->nur_offen | 2 | 1 | 0.3723 | 1.2263 | 0.0446 | 0.0231 | 0.0829 | 0.0731 |
| dio_0d03 | offen_und_gereift->nur_gereift | 2 | 1 | 0.1330 | 0.4044 | 0.0186 | 0.0239 | 0.0569 | 0.0580 |
| dio_0d46 | nur_gereift->offen_und_gereift | 2 | 1 | 0.0703 | 0.3136 | 0.1835 | 0.1817 | 0.1685 | 0.1655 |

## Rohwelt-nahe Kandidaten

Diese Tabelle sortiert nach kleiner Differenz in Folge-Range, Folge-Hoeren-Gap und Folge-Feldspannung.

| Familie | Wechsel | Delta Range | Delta Hoeren | Delta Spannung | 2024 | 2025 |
|---|---|---:|---:|---:|---:|---:|
| dio_0f8s | offen_und_gereift->nur_gereift | 0.0055 | 0.0025 | 0.0041 | 1 | 1 |
| dio_0sa1 | offen_und_gereift->nur_gereift | 0.0136 | 0.0020 | 0.0008 | 1 | 1 |
| dio_084i | offen_und_gereift->nur_gereift | 0.0212 | 0.0036 | 0.0026 | 1 | 1 |
| dio_00pl | offen_und_gereift->nur_gereift | 0.0308 | 0.0039 | 0.0001 | 2 | 1 |
| dio_1rrr | offen_und_gereift->nur_gereift | 0.0362 | 0.0025 | 0.0012 | 2 | 1 |
| dio_0z35 | nur_gereift->offen_und_gereift | 0.0419 | 0.0006 | 0.0017 | 1 | 1 |
| dio_0m49 | nur_gereift->offen_und_gereift | 0.0539 | 0.0013 | 0.0001 | 3 | 3 |
| dio_16i6 | offen_und_gereift->nur_offen | 0.0281 | 0.0181 | 0.0164 | 1 | 1 |
| dio_1r55 | nur_gereift->offen_und_gereift | 0.0633 | 0.0013 | 0.0007 | 1 | 2 |
| dio_06jk | nur_gereift->offen_und_gereift | 0.0579 | 0.0100 | 0.0104 | 1 | 1 |
| dio_14l0 | offen_und_gereift->nur_gereift | 0.0593 | 0.0088 | 0.0130 | 2 | 1 |
| dio_01hu | nur_gereift->offen_und_gereift | 0.0808 | 0.0025 | 0.0016 | 2 | 1 |
| dio_10dv | nur_gereift->offen_und_gereift | 0.0846 | 0.0023 | 0.0024 | 2 | 2 |
| dio_0fc4 | offen_und_gereift->nur_gereift | 0.0576 | 0.0175 | 0.0146 | 1 | 2 |
| dio_05ap | nur_gereift->offen_und_gereift | 0.0850 | 0.0029 | 0.0022 | 1 | 2 |
| dio_18im | nur_gereift->offen_und_gereift | 0.0900 | 0.0014 | 0.0019 | 2 | 1 |
| dio_1fll | nur_gereift->offen_und_gereift | 0.0935 | 0.0002 | 0.0007 | 1 | 1 |
| dio_1q2r | nur_gereift->offen_und_gereift | 0.0846 | 0.0130 | 0.0061 | 1 | 1 |
| dio_0u24 | offen_und_gereift->nur_gereift | 0.0964 | 0.0025 | 0.0055 | 2 | 2 |
| dio_13o0 | nur_gereift->offen_und_gereift | 0.0963 | 0.0042 | 0.0044 | 1 | 1 |
| dio_137l | offen_und_gereift->nur_offen | 0.0994 | 0.0080 | 0.0002 | 1 | 1 |
| dio_1ba6 | offen_und_gereift->nur_gereift | 0.1036 | 0.0001 | 0.0066 | 2 | 3 |
| dio_0dd2 | nur_gereift->offen_und_gereift | 0.1146 | 0.0017 | 0.0019 | 1 | 1 |
| dio_1udx | offen_und_gereift->nur_gereift | 0.1071 | 0.0151 | 0.0018 | 1 | 1 |
| dio_1aeg | nur_gereift->offen_und_gereift | 0.1298 | 0.0007 | 0.0002 | 1 | 1 |

## Lesung

Gleiche Familie plus gleicher Wechsel bedeutet nicht, dass die Weltphase identisch ist.
Es zeigt aber, dass dieselbe interne Familienlage in unterschiedlichen Weltjahren erneut in dieselbe Milieu-Bewegung geraten kann.

Die Rohwelt-nahe Kandidaten sind die naechste Pruefflaeche.
Dort ist die Aehnlichkeit von Folge-Range, Hoeren-Gap und Feldspannung am hoechsten.

## Grenze

Dieser Bericht beweist keinen Ausloeser.
Er isoliert Kandidaten fuer weitere Ruecklesung.

## Wie es weitergeht

Als naechstes sollten die rohweltnahen Kandidaten gegen ein weiteres Jahr oder ein anderes Assetfenster verfolgt werden. Wichtig ist, ob dieselbe Familie bei aehnlichem Folgeprofil erneut dieselbe Milieu-Bewegung zeigt.
