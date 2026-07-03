# 1390 - Bedeutungsnetz ueber Folgewelten

## Zweck

Diese Diagnose prueft das in `1389` gebildete Bedeutungsnetz gegen neue passive Folgewelten.

Geprueft wird:

```text
Tauchen starke Knoten wieder auf, teilen sie sich, oder entstehen neue Nachbarschaften?
```

Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.

## Befund

- alte Bedeutungsnetz-Knoten: `18`
- starke alte Knoten: `4`
- neue Fenster: `216`
- Folgezustaende: `neue_nachbarschaft_zu_altem_knoten:121, neue_bedeutungsinsel:46, bekannter_knoten_taucht_wieder_auf:43, starker_knoten_taucht_wieder_auf:6`
- exakt wiedergefundene alte Knoten: `2`
- alte Knoten mit Nachbarschaft: `11`

## Nach Welten

- `SYNTH_PURE_HEARING`: neue_nachbarschaft_zu_altem_knoten:43 | neue_bedeutungsinsel:29 | bekannter_knoten_taucht_wieder_auf:12
- `SYNTH_VISUAL_BREAKS_STABLE_PULSE`: neue_nachbarschaft_zu_altem_knoten:31 | bekannter_knoten_taucht_wieder_auf:22 | neue_bedeutungsinsel:7 | starker_knoten_taucht_wieder_auf:6
- `SYNTH_VISUAL_RECOUPLING_CHAOTIC_TONE`: neue_nachbarschaft_zu_altem_knoten:47 | neue_bedeutungsinsel:10 | bekannter_knoten_taucht_wieder_auf:9

## Wiedergefundene alte Knoten

- `dio_meaning_node_d1e40f2c`: `43`
- `dio_meaning_node_b7394769`: `6`

## Moegliche Teilung / Erweiterung

- `dio_meaning_node_5495a55c`: `6` neue Nachbarschaftssignaturen
- `dio_meaning_node_ddfb5575`: `3` neue Nachbarschaftssignaturen
- `dio_meaning_node_d5b684fe`: `2` neue Nachbarschaftssignaturen
- `dio_meaning_node_b7394769`: `2` neue Nachbarschaftssignaturen
- `dio_meaning_node_0fabb2f9`: `2` neue Nachbarschaftssignaturen
- `dio_meaning_node_65a8719c`: `2` neue Nachbarschaftssignaturen

## Dominante neue Signaturen

- `laut+starker_tonwechsel|stabile_form|mittlere_range+mittlerer_wechsel+mittlere_persistenz|starke_aufnahme+hohe_feldspannung`: `43`
- `mittlerer_ton+ruhiger_ton|stabile_form|mittlere_range+mittlerer_wechsel+mittlere_persistenz|gedaempfte_aufnahme+geringe_feldspannung`: `22`
- `leise+ruhiger_ton|stabile_form|mittlere_range+mittlerer_wechsel+mittlere_persistenz|gedaempfte_aufnahme+geringe_feldspannung`: `20`
- `leise+bewegter_ton|stabile_form|mittlere_range+mittlerer_wechsel+mittlere_persistenz|mittlere_aufnahme+mittlere_feldspannung`: `18`
- `mittlerer_ton+bewegter_ton|stabile_form|mittlere_range+mittlerer_wechsel+mittlere_persistenz|mittlere_aufnahme+mittlere_feldspannung`: `12`
- `leise+ruhiger_ton|stabile_form|mittlere_range+mittlerer_wechsel+mittlere_persistenz|mittlere_aufnahme+mittlere_feldspannung`: `10`
- `leise+starker_tonwechsel|stabile_form|mittlere_range+mittlerer_wechsel+mittlere_persistenz|starke_aufnahme+hohe_feldspannung`: `8`
- `mittlerer_ton+ruhiger_ton|stabile_form|mittlere_range+viel_wechsel+geringe_persistenz|gedaempfte_aufnahme+geringe_feldspannung`: `7`

## Lesung

Die Folgewelten bestaetigen nicht einfach eine feste Symboltabelle.
Sie zeigen, ob eine vorhandene Bedeutungsnaehe als Knoten wiederkehrt oder ob sie in neue Nachbarschaften ausweicht.

Exakte Wiederkehr spricht fuer stabile Feldnaehe.
Nachbarschaft ohne Exakttreffer spricht fuer Erweiterung oder Teilung.
Neue Inseln sprechen fuer neue Weltspannung, die noch nicht in der alten Karte enthalten war.

## Grenze

Die Folgewelt-Signatur nutzt eine relative Fensterklassifikation aus `episodes.csv`.
Sie ist eine passive Vergleichsschicht, kein neues Lexikon und keine Handlungslogik.

## Wie es weitergeht

Als naechstes sollten die Nachbarschaftsknoten isoliert werden. Entscheidend ist, ob sie bei weiteren Welten stabil neben demselben alten Knoten bleiben oder in eigenstaendige Knotenfamilien auseinanderdriften.
