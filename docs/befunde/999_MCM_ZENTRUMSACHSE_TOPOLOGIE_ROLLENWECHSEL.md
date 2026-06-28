# MCM-Zentrumsachse und Topologie-Rollenwechsel

## Zweck

Diese Datei legt zeitlich lokalisierte Zentrumsachsen gegen Topologie-Rollenbewegungen.
Unterschieden wird direkte Achsenpaar-Spur und angrenzende Rollenbewegung der beteiligten Knoten.

## Sicherheitsgrenze

- passive Ruecklesung
- keine Handlung
- kein Gate
- keine Strategie

## Achsenvergleich

| Achse | Zeitlagen | Paar-Events | direkte Topologie | angrenzende Topologie | Knotenrollen | Lesung |
|---|---:|---:|---:|---:|---|---|
| `183drjy<->1t5bcxp` | 4 | 24 | 0 | 4 | `183drjy=nichtbruecke_rekopplungsfeld / 1t5bcxp=nichtbruecke_zentrum_schwach` | `zeitachse_mit_angrenzender_rollenbewegung` |
| `183drjy<->1hjbx8p` | 0 | 0 | 0 | 4 | `183drjy=nichtbruecke_rekopplungsfeld / 1hjbx8p=nichtbruecke_zentrum_schwach` | `breite_naehe_mit_angrenzender_rollenbewegung` |
| `02xikfk<->1t5bcxp` | 5 | 31 | 0 | 0 | `02xikfk=nichtbruecke_zentrum_schwach / 1t5bcxp=nichtbruecke_zentrum_schwach` | `zeitachse_ohne_topologische_paarspur` |

## Detailprofile

### `183drjy<->1t5bcxp`

- Zeitlich lokalisierte Welten: `POS_EXPANSION_2023:1 | EXT_EXPANSION_2023:1 | SIDEWAYS_2024:1 | NEG_STRESS_2023:1`
- Direkte Rollenwechsel: `-`
- Direkte Effekte: `-`
- Angrenzende Rollenwechsel: `zentrum_stabil->zentrum_stabil:2 | zentrum_stabil->offene_variante:1 | offene_variante->offene_variante:1`
- Angrenzende Effekte: `rekoppelnd_entlastend:3 | oeffnend_belastend:1`
- Knoten A: `183drjy` / `nichtbruecke_rekopplungsfeld` / `zentrum_stabil` / Beobachtungen 6107
- Knoten B: `1t5bcxp` / `nichtbruecke_zentrum_schwach` / `zentrum_stabil` / Beobachtungen 2599

### `183drjy<->1hjbx8p`

- Zeitlich lokalisierte Welten: `-`
- Direkte Rollenwechsel: `-`
- Direkte Effekte: `-`
- Angrenzende Rollenwechsel: `zentrum_stabil->zentrum_stabil:2 | zentrum_stabil->offene_variante:1 | offene_variante->offene_variante:1`
- Angrenzende Effekte: `rekoppelnd_entlastend:3 | oeffnend_belastend:1`
- Knoten A: `183drjy` / `nichtbruecke_rekopplungsfeld` / `zentrum_stabil` / Beobachtungen 6107
- Knoten B: `1hjbx8p` / `nichtbruecke_zentrum_schwach` / `zentrum_stabil` / Beobachtungen 402

### `02xikfk<->1t5bcxp`

- Zeitlich lokalisierte Welten: `POS_EXPANSION_2023:1 | EXT_EXPANSION_2023:1 | NEG_STRESS_2024:1 | SIDEWAYS_2024:1 | NEG_STRESS_2023:1`
- Direkte Rollenwechsel: `-`
- Direkte Effekte: `-`
- Angrenzende Rollenwechsel: `-`
- Angrenzende Effekte: `-`
- Knoten A: `02xikfk` / `nichtbruecke_zentrum_schwach` / `zentrum_stabil` / Beobachtungen 70
- Knoten B: `1t5bcxp` / `nichtbruecke_zentrum_schwach` / `zentrum_stabil` / Beobachtungen 2599

## Befund

Wenn eine Achse zeitlich lokalisiert ist, aber kaum direkte Topologie-Paarspur besitzt,
dann ist sie eher als Feldlage mit angrenzender Rollenbewegung zu lesen, nicht als starre Kante.

Arbeitsableitung:

```text
Zentrumsachsen koennen zeitlich auftreten, waehrend die Topologie ihren Ausdruck
ueber Rollenbewegungen der beteiligten Knoten oder ihrer Nachbarschaft zeigt.
```

## Wie es weitergeht

Als naechstes sollte die staerkste Achse lokal segmentiert werden: Welche konkreten Kontaktsegmente erzeugen die Rollennaehe?
