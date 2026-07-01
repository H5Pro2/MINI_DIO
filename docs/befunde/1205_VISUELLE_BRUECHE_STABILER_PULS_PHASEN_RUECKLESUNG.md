# Befund 1205 - Visuelle Brueche bei stabilem Puls Phasen-Ruecklesung

## Grundfrage

Welche synthetische Weltphase erzeugt in MINI_DIO welche passive MCM-Feldrolle?

Die Phasen sind nur Ruecklese-Hilfen aus dem Datensatz. Sie sind keine Runtime-Regel und keine Handlungsvorgabe.

## Datengrundlage

- Quelle: `debug\1205_visual_breaks_stable_pulse\dio_mini_lauf_2\episodes.csv`
- Rollenlogik: dieselbe passive Topologie-Lesart wie in den letzten Weltrelativ-Matrizen.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Sinneskopplung | Hoer-Gap | Lautheit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhige_form_leiser_ton | 800 | 0.9988 | 0.0000 | 0.0013 | 0.0000 | 0.7615 | 0.6188 | 0.1197 | 0.9219 | 0.0036 | 0.0121 |
| stabiler_puls_klare_form | 1200 | 0.9983 | 0.0017 | 0.0000 | 0.0000 | 0.7223 | 0.5574 | 0.1483 | 0.8810 | 0.1201 | 0.2416 |
| formbruch_stabiler_puls | 1400 | 0.9321 | 0.0679 | 0.0000 | 0.0000 | 0.7204 | 0.5556 | 0.1457 | 0.8803 | 0.1115 | 0.2235 |
| rekopplung_stabiler_puls | 900 | 0.9989 | 0.0011 | 0.0000 | 0.0000 | 0.7309 | 0.5753 | 0.1469 | 0.8847 | 0.1175 | 0.2375 |
| zweiter_formbruch_stabiler_puls | 1400 | 0.9993 | 0.0000 | 0.0007 | 0.0000 | 0.7239 | 0.5646 | 0.1467 | 0.8803 | 0.1124 | 0.2252 |
| stille_schlussrekopplung | 894 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7626 | 0.6219 | 0.1195 | 0.9220 | 0.0036 | 0.0120 |

## Dominante Innenfeld-Signatur

| Phase | Effektklasse | Awareness | Symbolfamilie | Preview-Symbol |
|---|---|---|---|---|
| ruhige_form_leiser_ton | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_1v8o9kh` |
| stabiler_puls_klare_form | `stabil` | `inner_effect_stable` | `dio_0z9t` | `dio_mcm_episode_1hs3jsa` |
| formbruch_stabiler_puls | `stabil` | `inner_effect_stable` | `dio_1mwv` | `dio_mcm_episode_0v5p8er` |
| rekopplung_stabiler_puls | `stabil` | `inner_effect_stable` | `dio_1xme` | `dio_mcm_episode_077r0df` |
| zweiter_formbruch_stabiler_puls | `stabil` | `inner_effect_stable` | `dio_06qi` | `dio_mcm_episode_077r0df` |
| stille_schlussrekopplung | `stabil` | `inner_effect_stable` | `dio_1fll` | `dio_mcm_episode_077r0df` |

## Befund

- Staerkste offene Variante: `formbruch_stabiler_puls` mit `0.0679`.
- Staerkste Rand-/Kippnaehe: `ruhige_form_leiser_ton` mit `0.0013`.
- Staerkste Zentrierung: `stille_schlussrekopplung` mit `1.0000`.

Lesart:

- Die reine Hoerachse erzeugt keine gleichmaessige Ueberlastung.
- Die Feldrolle haengt von der zeitlichen Hoerform ab: Steigung, Abfall, Puls, Stille oder Impuls.
- Rekopplung wird daran sichtbar, ob nach einer Hoerphase Zentrum, Carry und Sinneskopplung wieder steigen.

Wie es weitergeht: Diese Phasenruecklesung sollte gegen die Desync-Teilwelten gelegt werden, damit sichtbar wird, ob Rand/Kippnaehe aus Hoerimpuls allein oder aus Sinneswiderspruch entsteht.
