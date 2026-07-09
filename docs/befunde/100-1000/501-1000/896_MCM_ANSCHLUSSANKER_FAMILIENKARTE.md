# MCM-Anschlussanker Familienkarte

## Zweck

Diese passive Diagnose ordnet lokale Anschlussanker den beobachteten starken Anschlussanker-Unterrollen zu.
Geprueft wird, ob lokale Anker eher zum verteilenden `0b7nep9`-Typ, zum kernnahen `1jx2k4i`-Typ oder zu einer eigenen Uebergangsrolle tendieren.

## Gesamtbefund

- Lokale/starke Anschlussanker in der Familienkarte: `7`
- Familienprofil: `kernnaher_inselanker_familie:4; verteilungsanker_familie:2; uebergangsanker_familie:1`

## Familienkarte

| Token | Ankerklasse | Familie | Gewicht | Welten | Dauer | Pfadklasse | Bewegung | Hauptnachbar | Begruendung |
|---|---|---|---:|---:|---:|---|---|---|---|
| `1jx2k4i` | starker_anschlussanker | kernnaher_inselanker_familie | 33 | 5 | 133.18 | stabile_insel | stabil | `1joiyc3` | Stabile Insel mit starker Kopplung an Brueckenkern. |
| `1q3us3f` | lokaler_anschlussanker | kernnaher_inselanker_familie | 26 | 3 | 57.27 | stabile_insel | stabil | `18l3thm` | Stabile Insel mit starker Kopplung an Brueckenkern. |
| `0z748ck` | lokaler_anschlussanker | kernnaher_inselanker_familie | 22 | 5 | 59.45 | stabile_insel | stabil | `0e7qvj1` | Stabile Insel mit starker Kopplung an Brueckenkern. |
| `1hdpu9s` | lokaler_anschlussanker | kernnaher_inselanker_familie | 12 | 2 | 20.42 | stabile_insel | stabil | `0e7qvj1` | Stabile Insel mit starker Kopplung an Brueckenkern. |
| `1xx3u1e` | lokaler_anschlussanker | uebergangsanker_familie | 12 | 2 | 15.00 | brueckenpfad | reifung_oder_verdichtung | `0geqqo3` | Brueckenpfad oder Rekopplungszone ohne klare starke Kernfamilie. |
| `0b7nep9` | starker_anschlussanker | verteilungsanker_familie | 35 | 2 | 470.94 | brueckenpfad | stabil | `00nzcuc` | Lange gewichtete Dauer und starke Anschlussbreite deuten auf verteilende Feldphase. |
| `00nzcuc` | lokaler_anschlussanker | verteilungsanker_familie | 14 | 2 | 134.07 | - | - | `0b7nep9` | Direkte gewichtete Kopplung an 0b7nep9. |

## Interpretation

Die Anschlussanker-Ebene teilt sich in mindestens drei lesbare Familien:

- `verteilungsanker_familie`: bindet offene oder lange Feldphasen an und wirkt eher als breiter Anschlussraum.
- `kernnaher_inselanker_familie`: koppelt stabile Inseln direkt an Brueckenkerne.
- `uebergangsanker_familie`: wirkt als Reifungs- oder Rekopplungsstueck zwischen stabiler Insel und Brueckenpfad.

Das spricht dafuer, dass die MCM-Topologie nicht nur Zentrum/Rand kennt, sondern eine differenzierte Anschlusszone zwischen stabiler Bedeutung und offener Feldbewegung ausbildet.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob diese Anschlussanker-Familien in anderen Weltgruppen wieder auftauchen oder ob sie nur aus dieser Brueckenlandschaft entstehen.