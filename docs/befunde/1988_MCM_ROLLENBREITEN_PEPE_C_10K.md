# 1988 - PEPE-C Dritter Gegenlauf zur Milieuinsel 0hiolzy

## Grundfrage

Nach PEPE-A und PEPE-B blieb offen, ob `dio_mcm_episode_0hiolzy` in einem weiteren PEPE-Fenster wieder Anschluss findet oder ob die Rolle an eine sehr konkrete PEPE-A-Feldphase gebunden bleibt.

## Pruefung

- Welt: `FOLLOW_EQ10K_PEPE_C_2024_5M`
- Daten: `data/kontrolliert_pepe_2024_5m_10k_c_PEPEUSDT.csv`
- Memory-Basis: Zustand nach PEPE-B
- Sinnesmodus: `world_relative`
- Debuglauf: `debug/1988_equal10k_pepe_c_2024_5m/dio_mini_lauf_49`

## Rollenbreite

Vor PEPE-C:

- `breite_grundrolle`: 33
- `uebergangsrolle`: 1
- `milieurolle`: 6
- `nebenrolle`: 200

Nach PEPE-C:

- `breite_grundrolle`: 34
- `uebergangsrolle`: 1
- `milieurolle`: 6
- `nebenrolle`: 219

PEPE-C verbreitert das Feld weiter. Es entsteht aber keine neue Milieurolle.

## Befund zu 0hiolzy

`dio_mcm_episode_0hiolzy` bleibt unveraendert als Milieurolle gespeichert:

- `before_role`: `milieurolle`
- `after_role`: `milieurolle`
- `count_delta`: 0
- `world_delta`: 0
- `top_world`: `FOLLOW_EQ10K_PEPE_2024_5M`

Direkte Treffer im PEPE-C-Debug:

- `0hiolzy`: 0

Damit bestaetigt PEPE-C den PEPE-B-Befund: `0hiolzy` ist keine generische PEPE-Rolle. Die Rolle bleibt eine situative Milieuinsel aus PEPE-A.

## Neue PEPE-C-nahe Bewegung

Statt `0hiolzy` wurde eine andere Grundrolle sichtbar gestaerkt:

- `dio_mcm_episode_1yxc2ug`
- `count_delta`: +304
- `world_delta`: +1
- `top_world`: kippt auf `FOLLOW_EQ10K_PEPE_C_2024_5M`
- direkte PEPE-C-Treffer: 304
- dominante Zeitlage: `temporal_far_return`
- Feldwirkung: ueberwiegend `field_carried`

Ausserdem:

- `dio_mcm_episode_010cqn6`: +85, Top-Welt kippt auf PEPE-C, bleibt Nebenrolle
- `dio_mcm_episode_1y7uo9c`: `nebenrolle` -> `breite_grundrolle`

## Interpretation

PEPE-C bestaetigt drei Punkte:

1. Die Grundtopologie bleibt stabil.
2. `0hiolzy` bleibt als gespeicherte Milieuinsel erhalten, wird aber nicht neu gespeist.
3. PEPE-C erzeugt eigene Rekopplung an andere Rollen, besonders `1yxc2ug`.

Das spricht fuer eine phasenabhaengige Bedeutungsbildung: Aehnliche Asset-Welten erzeugen nicht automatisch dieselbe Milieuinsel. Das Feld liest nicht nur "PEPE", sondern konkrete Weltlage, Nachhall, Wiederkehr, Sinneskopplung und Rekopplung.

## Schlussfolgerung

Die Milieuinsel `0hiolzy` ist derzeit als PEPE-A-spezifische Feldphase zu lesen. PEPE-B und PEPE-C tragen stattdessen andere Rollen weiter. Das ist ein wichtiger Hinweis gegen starre Symbolbildung und fuer dynamische Bedeutungsnaehe im MCM-Feld.

## Wie es weitergeht

Als naechstes sollte `1yxc2ug` im PEPE-C-Fenster isoliert rueckgelesen werden. Entscheidend ist, ob es die Rolle von `0hiolzy` ersetzt, eine andere PEPE-Phase beschreibt oder eine breitere Grundrollen-Rekopplung darstellt.
