# Befund 1203 - Stabile Form Chaotisches Hoeren Phasen-Ruecklesung

## Grundfrage

Welche synthetische Weltphase erzeugt in MINI_DIO welche passive MCM-Feldrolle?

Die Phasen sind nur Ruecklese-Hilfen aus dem Datensatz. Sie sind keine Runtime-Regel und keine Handlungsvorgabe.

## Datengrundlage

- Quelle: `debug\1197_visual_stable_hearing_chaotic\dio_mini_lauf_2\episodes.csv`
- Rollenlogik: dieselbe passive Topologie-Lesart wie in den letzten Weltrelativ-Matrizen.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Sinneskopplung | Hoer-Gap | Lautheit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhige_form_leiser_ton | 900 | 0.9989 | 0.0000 | 0.0011 | 0.0000 | 0.7614 | 0.6193 | 0.1196 | 0.9216 | 0.0035 | 0.0120 |
| ruhige_form_laute_wicks_1 | 1600 | 0.8812 | 0.0587 | 0.0600 | 0.0000 | 0.7401 | 0.5793 | 0.1444 | 0.8893 | 0.0874 | 0.1726 |
| stille_rekopplung | 900 | 0.9989 | 0.0000 | 0.0011 | 0.0000 | 0.7617 | 0.6208 | 0.1195 | 0.9211 | 0.0043 | 0.0136 |
| lauter_nachhall_ohne_form | 1700 | 0.9988 | 0.0006 | 0.0006 | 0.0000 | 0.7631 | 0.6230 | 0.1196 | 0.9224 | 0.0033 | 0.0117 |
| ruhige_form_laute_wicks_2 | 1400 | 0.8814 | 0.0607 | 0.0579 | 0.0000 | 0.7431 | 0.5856 | 0.1445 | 0.8896 | 0.0873 | 0.1723 |
| schluss_rekopplung | 894 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7627 | 0.6230 | 0.1193 | 0.9220 | 0.0035 | 0.0117 |

## Dominante Innenfeld-Signatur

| Phase | Effektklasse | Awareness | Symbolfamilie | Preview-Symbol |
|---|---|---|---|---|
| ruhige_form_leiser_ton | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_1v8o9kh` |
| ruhige_form_laute_wicks_1 | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0v5p8er` |
| stille_rekopplung | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0v5p8er` |
| lauter_nachhall_ohne_form | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0qvodoj` |
| ruhige_form_laute_wicks_2 | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_077r0df` |
| schluss_rekopplung | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_077r0df` |

## Befund

- Staerkste offene Variante: `ruhige_form_laute_wicks_2` mit `0.0607`.
- Staerkste Rand-/Kippnaehe: `ruhige_form_laute_wicks_1` mit `0.0600`.
- Staerkste Zentrierung: `schluss_rekopplung` mit `1.0000`.

Lesart:

- Die reine Hoerachse erzeugt keine gleichmaessige Ueberlastung.
- Die Feldrolle haengt von der zeitlichen Hoerform ab: Steigung, Abfall, Puls, Stille oder Impuls.
- Rekopplung wird daran sichtbar, ob nach einer Hoerphase Zentrum, Carry und Sinneskopplung wieder steigen.

Wie es weitergeht: Diese Phasenruecklesung sollte gegen die Desync-Teilwelten gelegt werden, damit sichtbar wird, ob Rand/Kippnaehe aus Hoerimpuls allein oder aus Sinneswiderspruch entsteht.
