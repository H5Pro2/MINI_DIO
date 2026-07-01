# Befund 1203 - Chaotische Form Stabiles Hoeren Phasen-Ruecklesung

## Grundfrage

Welche synthetische Weltphase erzeugt in MINI_DIO welche passive MCM-Feldrolle?

Die Phasen sind nur Ruecklese-Hilfen aus dem Datensatz. Sie sind keine Runtime-Regel und keine Handlungsvorgabe.

## Datengrundlage

- Quelle: `debug\1197_visual_chaotic_hearing_stable\dio_mini_lauf_2\episodes.csv`
- Rollenlogik: dieselbe passive Topologie-Lesart wie in den letzten Weltrelativ-Matrizen.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Sinneskopplung | Hoer-Gap | Lautheit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhige_form_leiser_ton | 700 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7610 | 0.6191 | 0.1192 | 0.9217 | 0.0032 | 0.0115 |
| klare_form_leiser_ton_1 | 1300 | 0.9992 | 0.0008 | 0.0000 | 0.0000 | 0.7592 | 0.6206 | 0.1181 | 0.9188 | 0.0042 | 0.0119 |
| bruch_ohne_lautheit_1 | 1300 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7557 | 0.6173 | 0.1174 | 0.9148 | 0.0068 | 0.0140 |
| klare_form_leiser_ton_2 | 1000 | 0.9990 | 0.0010 | 0.0000 | 0.0000 | 0.7602 | 0.6232 | 0.1184 | 0.9186 | 0.0043 | 0.0121 |
| bruch_ohne_lautheit_2 | 1200 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7577 | 0.6226 | 0.1178 | 0.9148 | 0.0068 | 0.0142 |
| stille_rekopplung | 894 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7622 | 0.6226 | 0.1194 | 0.9214 | 0.0031 | 0.0114 |

## Dominante Innenfeld-Signatur

| Phase | Effektklasse | Awareness | Symbolfamilie | Preview-Symbol |
|---|---|---|---|---|
| ruhige_form_leiser_ton | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_1v8o9kh` |
| klare_form_leiser_ton_1 | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_1v8o9kh` |
| bruch_ohne_lautheit_1 | `stabil` | `inner_effect_stable` | `dio_13o0` | `dio_mcm_episode_0qvodoj` |
| klare_form_leiser_ton_2 | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0qvodoj` |
| bruch_ohne_lautheit_2 | `stabil` | `inner_effect_stable` | `dio_13o0` | `dio_mcm_episode_0qvodoj` |
| stille_rekopplung | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0qvodoj` |

## Befund

- Staerkste offene Variante: `klare_form_leiser_ton_2` mit `0.0010`.
- Staerkste Rand-/Kippnaehe: `ruhige_form_leiser_ton` mit `0.0000`.
- Staerkste Zentrierung: `ruhige_form_leiser_ton` mit `1.0000`.

Lesart:

- Die reine Hoerachse erzeugt keine gleichmaessige Ueberlastung.
- Die Feldrolle haengt von der zeitlichen Hoerform ab: Steigung, Abfall, Puls, Stille oder Impuls.
- Rekopplung wird daran sichtbar, ob nach einer Hoerphase Zentrum, Carry und Sinneskopplung wieder steigen.

Wie es weitergeht: Diese Phasenruecklesung sollte gegen die Desync-Teilwelten gelegt werden, damit sichtbar wird, ob Rand/Kippnaehe aus Hoerimpuls allein oder aus Sinneswiderspruch entsteht.
