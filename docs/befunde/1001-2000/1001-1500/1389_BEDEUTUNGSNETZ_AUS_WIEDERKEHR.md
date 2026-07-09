# 1389 - Passives MCM-Bedeutungsnetz aus Wiederkehr

## Zweck

Diese Diagnose baut aus `1387` ein erstes passives Bedeutungsnetz.

Knoten sind wiederkehrende Unterform-/Feldspuren.
Kanten sind Kopplungen zu Familien- oder Preview-Kernen.

Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.

## Befund

- Knoten: `18`
- Kanten: `48`
- semantisch gebundene Kanten: `29`
- reine Oberflaechenkanten: `19`
- Knotenzustaende: `junge_spur:9, rollenuebergreifend_offen:5, tragende_bedeutungsnaehe:4`
- Kantenarten: `semantisch_gekoppelt:25, oberflaechennaehe:19, stark_semantisch_gekoppelt:4`

## Semantisch vs. Oberflaeche

- mittleres Gewicht semantischer Kanten: `0.816355`
- mittleres Gewicht reiner Oberflaechenkanten: `0.416144`
- Folge-Strain semantischer Kanten: `0.000621`
- Folge-Strain reiner Oberflaechenkanten: `0.002076`
- Folge-Rekopplung semantischer Kanten: `-0.001143`
- Folge-Rekopplung reiner Oberflaechenkanten: `-0.003536`

## Staerkste Knoten

- `dio_meaning_node_119d9d87`: `tragende_bedeutungsnaehe`, obs `10`, worlds `3`, weight `0.765123`, bindings `family:5 | family_and_preview:2 | none:2 | preview:1`
- `dio_meaning_node_b7394769`: `tragende_bedeutungsnaehe`, obs `7`, worlds `3`, weight `0.741671`, bindings `preview:4 | family:2 | none:1`
- `dio_meaning_node_476ccc10`: `tragende_bedeutungsnaehe`, obs `5`, worlds `3`, weight `0.672681`, bindings `none:2 | preview:2 | family_and_preview:1`
- `dio_meaning_node_5495a55c`: `tragende_bedeutungsnaehe`, obs `3`, worlds `1`, weight `0.714134`, bindings `family:2 | none:1`
- `dio_meaning_node_541277a5`: `rollenuebergreifend_offen`, obs `4`, worlds `2`, weight `0.524313`, bindings `none:3 | family:1`
- `dio_meaning_node_ddfb5575`: `rollenuebergreifend_offen`, obs `4`, worlds `2`, weight `0.414095`, bindings `none:3 | preview:1`
- `dio_meaning_node_d5b684fe`: `rollenuebergreifend_offen`, obs `2`, worlds `2`, weight `0.577656`, bindings `none:1 | family:1`
- `dio_meaning_node_ea0096d4`: `rollenuebergreifend_offen`, obs `2`, worlds `1`, weight `0.430867`, bindings `none:2`
- `dio_meaning_node_e7db1d51`: `rollenuebergreifend_offen`, obs `2`, worlds `1`, weight `0.414698`, bindings `none:2`
- `dio_meaning_node_1c830c6d`: `junge_spur`, obs `1`, worlds `1`, weight `1.0`, bindings `family_and_preview:1`

## Lesung

Das Bedeutungsnetz speichert keine externe Bedeutung.
Es liest nur, welche Feldspuren wiederholt nahe beieinander liegen und ob diese Naehe semantisch gebunden ist.

Wenn semantische Kanten hoeher gewichtet sind als reine Oberflaechenkanten, wird Feldbewusstsein technisch greifbarer:

```text
Das Feld traegt nicht nur Aehnlichkeit.
Es traegt wiederkehrende innere Naehe.
```

## Grenze

Diese Netzschicht ist eine passive Diagnose.
Sie darf nicht als Motorik, Gate, Handlung oder Strategie gelesen werden.
