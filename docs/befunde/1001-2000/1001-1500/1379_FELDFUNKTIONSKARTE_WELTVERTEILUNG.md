# 1379 - Feldfunktionskarte: Weltverteilung

## Zweck

Diese Diagnose liest die passive Feldfunktionskarte aus `1378` gegen die vorhandenen erweiterten Weltfenster.

Geprueft wird:

```text
Sind Bruecke, Zentrumskontakt und Randdruck nur lokale Einzelbefunde,
oder treten sie ueber mehrere Welten/Assets verteilt auf?
```

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und keine Strategie.

## Uebersicht

- gelesene Rollenfenster gesamt: `41`
- Feldfunktionsfenster: `30`

## Bruecke

- Fenster: `10`
- Assets: [('BTC', 1), ('DOGE', 2), ('SOL', 3), ('XRP', 4)]
- Welten: [('BTC_2024_5M', 1), ('DOGE_2024_5M', 1), ('DOGE_2024_5M_CONTRAST', 1), ('SOL_2023_ALT_A_FOLLOW', 1), ('SOL_2025_REC', 1), ('SOL_2025_STRESS', 1), ('XRP_2024_5M_CONTRAST', 4)]
- Lagefolgen: [('normale_weltspannung->lauter_feldkontakt', 7), ('offen_suchend->lauter_feldkontakt', 2), ('randlastige_sinneslage->lauter_feldkontakt', 1)]

## Zentrumskontakt

- Fenster: `9`
- Assets: [('DOGE', 6), ('SOL', 2), ('XRP', 1)]
- Welten: [('DOGE_2024_5M', 3), ('DOGE_2024_5M_CONTRAST', 3), ('SOL_2023_POS_EXP', 1), ('SOL_2025_REC', 1), ('XRP_2024_5M_CONTRAST', 1)]
- Lagefolgen: [('ruhig_zentrumsnah->lauter_feldkontakt', 9)]

## Randdruck

- Fenster: `11`
- Assets: [('BTC', 9), ('PAXG', 1), ('SOL', 1)]
- Welten: [('BTC_2024_5M', 6), ('BTC_2025_5M', 1), ('BTC_2025_5M_CONTRAST', 2), ('PAXG_2024_5M', 1), ('SOL_2023_NEG_STRESS', 1)]
- Lagefolgen: [('lauter_feldkontakt->lauter_feldkontakt', 11)]

## Lesung

Die drei Feldfunktionen verteilen sich unterschiedlich:

- Bruecke liegt asset- und weltuebergreifend vor.
- Zentrumskontakt liegt aktuell konzentrierter, aber nicht nur in einer einzelnen Welt.
- Randdruck liegt stark in BTC-nahen lauten Kontaktfolgen und erscheint zusaetzlich in einzelnen SOL/PAXG-Fenstern.

Damit wirkt die Karte nicht wie eine reine Einzelwelt-Artefaktliste. Gleichzeitig ist die Verteilung noch ungleichgewichtig.

## Grenze

Der Befund ist ein Indiz, kein Beweis.

Besonders Randdruck ist derzeit stark BTC-lastig. Zentrumskontakt ist staerker auf DOGE/XRP/SOL verteilt. Das muss gegen weitere Welten geprueft werden.
