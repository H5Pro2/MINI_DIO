# 1697 - Lupenprofile der Drittperioden-Treffer

Stand: 2026-07-07 18:02:35

## Zweck

Diese Diagnose gruppiert die Rohwelt-Lupe aus 1696 in relative Arbeitsprofile.
Die Gruppen entstehen aus dem jeweiligen Datensatz selbst und sind keine festen Regeln.

## Hierarchie

1. Grundfrage: Welche Typen von Vorfenster-zu-Folgephase-Bewegung liegen unter den Treffern?
2. Unterpruefung: Range, Hoeren-Gap und Feldspannung relativ zueinander gruppieren.
3. Folgeschritt: Die Profile gegen weitere Assetfenster testen.

## Profilzaehlung

| Profil | Anzahl |
|---|---:|
| hoerprofil_entlastet | 5 |
| hoerprofil_springt_hoch | 1 |
| milieu_umlagert_nahe | 5 |
| rangegetriebene_umgebung | 9 |

## Beispiele

### hoerprofil_entlastet

| Familie | Wechsel | Welt | Range-Delta | Hoeren-Delta | Spannungs-Delta |
|---|---|---|---:|---:|---:|
| dio_13o0 | offen_und_gereift->nur_gereift | ALTSEQ_2023 | 0.0077 | 0.0767 | 0.0674 |
| dio_1fll | nur_gereift->offen_und_gereift | MOD_NEG_2023 | 0.0299 | 0.0804 | 0.0756 |
| dio_1j1f | nur_gereift->offen_und_gereift | NEG_STRESS_2023 | 0.0626 | 0.1321 | 0.0725 |
| dio_1wdi | offen_und_gereift->nur_gereift | EXPANSION_2023 | 0.0262 | 0.0801 | 0.0629 |
| dio_1yt8 | offen_und_gereift->nur_gereift | NEG_STRESS_2023 | 0.0509 | 0.0718 | 0.0529 |

### hoerprofil_springt_hoch

| Familie | Wechsel | Welt | Range-Delta | Hoeren-Delta | Spannungs-Delta |
|---|---|---|---:|---:|---:|
| dio_0ioc | nur_gereift->offen_und_gereift | NEG_STRESS_2023 | 0.0181 | 0.0900 | 0.0738 |

### milieu_umlagert_nahe

| Familie | Wechsel | Welt | Range-Delta | Hoeren-Delta | Spannungs-Delta |
|---|---|---|---:|---:|---:|
| dio_01hu | nur_gereift->offen_und_gereift | MOD_NEG_2023 | 0.0314 | 0.0186 | 0.0248 |
| dio_01hu | nur_gereift->offen_und_gereift | ALTSEQ_2023 | 0.0360 | 0.0349 | 0.0357 |
| dio_0dd2 | nur_gereift->offen_und_gereift | NEG_STRESS_2023 | 0.0575 | 0.0089 | 0.0167 |
| dio_0ly7 | nur_gereift->offen_und_gereift | ALTSEQ_2023 | 0.0321 | 0.0443 | 0.0426 |
| dio_10dv | nur_gereift->offen_und_gereift | MOD_NEG_2023 | 0.0716 | 0.0253 | 0.0206 |

### rangegetriebene_umgebung

| Familie | Wechsel | Welt | Range-Delta | Hoeren-Delta | Spannungs-Delta |
|---|---|---|---:|---:|---:|
| dio_092h | offen_und_gereift->nur_gereift | NEG_STRESS_2023 | 0.2020 | 0.1748 | 0.1483 |
| dio_0f4r | offen_und_gereift->nur_gereift | ALTSEQ_2023 | 0.1235 | 0.0341 | 0.0184 |
| dio_10dv | nur_gereift->offen_und_gereift | ALTSEQ_2023 | 0.1001 | 0.0004 | 0.0011 |
| dio_14d9 | offen_und_gereift->nur_gereift | ALTSEQ_2023 | 0.1079 | 0.0316 | 0.0196 |
| dio_1cmd | nur_gereift->offen_und_gereift | ALTSEQ_2023 | 0.1555 | 0.1473 | 0.1175 |
| dio_1qyl | offen_und_gereift->nur_gereift | NEG_STRESS_2023 | 0.0815 | 0.0644 | 0.0453 |
| dio_1r55 | nur_gereift->offen_und_gereift | ALTSEQ_2023 | 0.0783 | 0.0401 | 0.0303 |
| dio_1r55 | nur_gereift->offen_und_gereift | MOD_NEG_2023 | 0.0732 | 0.0302 | 0.0226 |

## Lesung

`milieu_umlagert_nahe` ist der interessanteste passive Kandidat: Familie und Wechselrichtung wiederholen sich, waehrend Vorfenster und Folgephase in Hoeren und Spannung nahe bleiben.

Hoer-, Spannungs- und Rangeprofile zeigen dagegen eher, dass eine erkennbare Weltveraenderung am Wechsel beteiligt ist.

Das trennt zwei Arbeitsfragen:

```text
Milieu-Umlagerung: aehnliche Welt-/Feldlage, andere Milieuschicht.
Weltgetriebener Wechsel: veraenderte Range, Hoeren oder Feldspannung faerbt die Familie um.
```
