# 1986 - PEPE-B Gegenpruefung der Milieuinsel 0hiolzy

## Grundfrage

Die PEPE-A-Welt hatte mit `dio_mcm_episode_0hiolzy` eine neue Milieuinsel gebildet. Die Gegenpruefung sollte klaeren, ob diese Insel eine allgemeine PEPE-Rolle ist oder ob sie an eine bestimmte Feldphase gebunden bleibt.

## Pruefung

- Welt: `FOLLOW_EQ10K_PEPE_B_2024_5M`
- Daten: `data/kontrolliert_pepe_2024_5m_10k_b_PEPEUSDT.csv`
- Memory-Basis: Zustand nach PEPE-A
- Sinnesmodus: `world_relative`
- Reportdateien:
  - `docs/befunde/1001-2000/1751-2000/1986_MCM_ROLLENBREITEN_PEPE_B_10K_METRIK.csv`
  - `docs/befunde/1001-2000/1751-2000/1986_MCM_ROLLENBREITEN_PEPE_B_10K_DELTA.csv`

## Rollenbreite

Vor PEPE-B:

- `breite_grundrolle`: 32
- `uebergangsrolle`: 1
- `milieurolle`: 6
- `nebenrolle`: 181

Nach PEPE-B:

- `breite_grundrolle`: 33
- `uebergangsrolle`: 1
- `milieurolle`: 6
- `nebenrolle`: 200

PEPE-B verbreitert damit das Feld weiter, erzeugt aber keine neue starke Milieuinsel.

## Befund zu 0hiolzy

`dio_mcm_episode_0hiolzy` bleibt im Speicher als Milieurolle erhalten:

- `count`: 800
- `world_count`: 5
- `depth_score`: 0.87146
- `top_world`: `FOLLOW_EQ10K_PEPE_2024_5M`
- `top_world_share`: 0.96125

Im zweiten PEPE-Fenster selbst wurde diese Rolle jedoch nicht erneut aktiviert:

- `count_delta`: 0
- `world_delta`: 0
- direkte Debug-Treffer in `1986_equal10k_pepe_b_2024_5m`: 0

Das bedeutet: `0hiolzy` ist kein pauschales PEPE-Symbol. Es wirkt als situative Milieuinsel, die stark an die konkrete Weltphase aus PEPE-A gebunden ist.

## Staerkste Rekopplungen

Die staerksten Zunahmen lagen wieder bei vorhandenen Grundrollen:

- `dio_mcm_episode_12tgchq`: +4468
- `dio_mcm_episode_1qlxgj7`: +1729
- `dio_mcm_episode_0iwh9d2`: +1453
- `dio_mcm_episode_0icnf2v`: +612
- `dio_mcm_episode_1yxc2ug`: +198

Eine Nebenrolle reifte in PEPE-B zur breiten Grundrolle:

- `dio_mcm_episode_0whyn34`: `nebenrolle` -> `breite_grundrolle`

## Interpretation

PEPE-B bestaetigt die robuste Grundordnung, aber nicht die automatische Wiederkehr der PEPE-A-Milieuinsel. Das ist fachlich wichtig:

- stabile Feldrollen koennen ueber viele Welten weiter wachsen,
- einzelne Milieuinseln koennen stark, aber phasengebunden sein,
- Bedeutung entsteht nicht als Asset-Etikett, sondern aus konkreter Feldlage, Nachhall, Sinneskopplung und Weltphase.

## Schlussfolgerung

Die Topologie bleibt stabil, aber ihre Milieurollen sind nicht starr. PEPE-A hat eine starke situative Insel gebildet; PEPE-B koppelt stattdessen vor allem an vorhandene Grundrollen und bildet zusaetzliche Nebenrollen. Damit zeigt das Feld nicht nur Reproduktion, sondern auch phasenabhaengige Selektivitaet.

## Wie es weitergeht

Als naechstes sollte die PEPE-A-Zone genauer rueckgelesen werden: Welche Weltspannung, Tonlage, visuelle Form oder Nachhallphase hat `0hiolzy` getragen? Danach kann ein drittes PEPE-Fenster pruefen, ob diese Bedingungen wieder auftauchen.
