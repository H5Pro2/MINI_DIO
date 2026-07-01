# Befund 1201 - Reine Hoerwelt Phasen-Ruecklesung

## Grundfrage

Welche synthetische Weltphase erzeugt in MINI_DIO welche passive MCM-Feldrolle?

Die Phasen sind nur Ruecklese-Hilfen aus dem Datensatz. Sie sind keine Runtime-Regel und keine Handlungsvorgabe.

## Datengrundlage

- Quelle: `debug\1199_pure_hearing\dio_mini_lauf_2\episodes.csv`
- Rollenlogik: dieselbe passive Topologie-Lesart wie in den letzten Weltrelativ-Matrizen.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Sinneskopplung | Hoer-Gap | Lautheit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhige_form_leiser_ton | 900 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7621 | 0.6195 | 0.1188 | 0.9221 | 0.0031 | 0.0060 |
| hoeren_steigend_form_stabil | 1400 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7636 | 0.6226 | 0.1189 | 0.9226 | 0.0027 | 0.0059 |
| hoeren_fallend_form_stabil | 1400 | 0.9993 | 0.0000 | 0.0007 | 0.0000 | 0.7638 | 0.6228 | 0.1192 | 0.9226 | 0.0030 | 0.0065 |
| hoeren_pulsierend_form_stabil | 1600 | 0.8031 | 0.1969 | 0.0000 | 0.0000 | 0.7142 | 0.5357 | 0.1674 | 0.8587 | 0.1704 | 0.3383 |
| hoeren_still_form_stabil | 1000 | 0.9990 | 0.0000 | 0.0010 | 0.0000 | 0.7635 | 0.6222 | 0.1191 | 0.9220 | 0.0037 | 0.0072 |
| hoeren_doppelimpuls_form_stabil | 1200 | 0.9075 | 0.0467 | 0.0458 | 0.0000 | 0.7483 | 0.5891 | 0.1433 | 0.8951 | 0.0767 | 0.1485 |
| schluss_rekopplung | 894 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7634 | 0.6228 | 0.1187 | 0.9225 | 0.0036 | 0.0056 |

## Dominante Innenfeld-Signatur

| Phase | Effektklasse | Awareness | Symbolfamilie | Preview-Symbol |
|---|---|---|---|---|
| ruhige_form_leiser_ton | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_1v8o9kh` |
| hoeren_steigend_form_stabil | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_1v8o9kh` |
| hoeren_fallend_form_stabil | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0qvodoj` |
| hoeren_pulsierend_form_stabil | `stabil` | `inner_effect_stable` | `dio_1nmh` | `dio_mcm_episode_1rneafq` |
| hoeren_still_form_stabil | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0qvodoj` |
| hoeren_doppelimpuls_form_stabil | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_0v5p8er` |
| schluss_rekopplung | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_1engxbn` |

## Befund

- Staerkste offene Variante: `hoeren_pulsierend_form_stabil` mit `0.1969`.
- Staerkste Rand-/Kippnaehe: `hoeren_doppelimpuls_form_stabil` mit `0.0458`.
- Staerkste Zentrierung: `ruhige_form_leiser_ton` mit `1.0000`.

Lesart:

- Die reine Hoerachse erzeugt keine gleichmaessige Ueberlastung.
- Die Feldrolle haengt von der zeitlichen Hoerform ab: Steigung, Abfall, Puls, Stille oder Impuls.
- Rekopplung wird daran sichtbar, ob nach einer Hoerphase Zentrum, Carry und Sinneskopplung wieder steigen.

Wie es weitergeht: Diese Phasenruecklesung sollte gegen die Desync-Teilwelten gelegt werden, damit sichtbar wird, ob Rand/Kippnaehe aus Hoerimpuls allein oder aus Sinneswiderspruch entsteht.
