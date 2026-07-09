# Befund 1207 - Visuelle Rekopplung Chaoston Phasen-Ruecklesung

## Grundfrage

Welche synthetische Weltphase erzeugt in MINI_DIO welche passive MCM-Feldrolle?

Die Phasen sind nur Ruecklese-Hilfen aus dem Datensatz. Sie sind keine Runtime-Regel und keine Handlungsvorgabe.

## Datengrundlage

- Quelle: `debug\1207_visual_recoupling_chaotic_tone\dio_mini_lauf_2\episodes.csv`
- Rollenlogik: dieselbe passive Topologie-Lesart wie in den letzten Weltrelativ-Matrizen.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Sinneskopplung | Hoer-Gap | Lautheit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhige_form_leiser_ton | 800 | 0.9988 | 0.0000 | 0.0013 | 0.0000 | 0.7618 | 0.6192 | 0.1190 | 0.9217 | 0.0039 | 0.0068 |
| klare_rekopplung_chaostone | 1200 | 0.9992 | 0.0008 | 0.0000 | 0.0000 | 0.7460 | 0.5895 | 0.1235 | 0.9101 | 0.0493 | 0.1013 |
| visuelle_rekopplung_lautimpuls | 1400 | 0.8700 | 0.0650 | 0.0650 | 0.0000 | 0.7399 | 0.5737 | 0.1536 | 0.8818 | 0.1076 | 0.2054 |
| klare_form_chaotischer_nachhall | 900 | 0.9589 | 0.0400 | 0.0011 | 0.0000 | 0.7235 | 0.5546 | 0.1506 | 0.8775 | 0.1318 | 0.2634 |
| zweite_rekopplung_chaostone | 1400 | 0.9150 | 0.0429 | 0.0421 | 0.0000 | 0.7498 | 0.5949 | 0.1402 | 0.8969 | 0.0683 | 0.1296 |
| stille_schlussrekopplung | 894 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7632 | 0.6228 | 0.1188 | 0.9220 | 0.0032 | 0.0058 |

## Dominante Innenfeld-Signatur

| Phase | Effektklasse | Awareness | Symbolfamilie | Preview-Symbol |
|---|---|---|---|---|
| ruhige_form_leiser_ton | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_1v8o9kh` |
| klare_rekopplung_chaostone | `stabil` | `inner_effect_stable` | `dio_06er` | `dio_mcm_episode_0wjn8vm` |
| visuelle_rekopplung_lautimpuls | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0nyb3ro` |
| klare_form_chaotischer_nachhall | `stabil` | `inner_effect_stable` | `dio_06er` | `dio_mcm_episode_0nyb3ro` |
| zweite_rekopplung_chaostone | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0v5p8er` |
| stille_schlussrekopplung | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0qvodoj` |

## Befund

- Staerkste offene Variante: `visuelle_rekopplung_lautimpuls` mit `0.0650`.
- Staerkste Rand-/Kippnaehe: `visuelle_rekopplung_lautimpuls` mit `0.0650`.
- Staerkste Zentrierung: `stille_schlussrekopplung` mit `1.0000`.

Lesart:

- Die reine Hoerachse erzeugt keine gleichmaessige Ueberlastung.
- Die Feldrolle haengt von der zeitlichen Hoerform ab: Steigung, Abfall, Puls, Stille oder Impuls.
- Rekopplung wird daran sichtbar, ob nach einer Hoerphase Zentrum, Carry und Sinneskopplung wieder steigen.

Wie es weitergeht: Diese Phasenruecklesung sollte gegen die Desync-Teilwelten gelegt werden, damit sichtbar wird, ob Rand/Kippnaehe aus Hoerimpuls allein oder aus Sinneswiderspruch entsteht.
