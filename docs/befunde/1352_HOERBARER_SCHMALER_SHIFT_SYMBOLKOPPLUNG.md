# 1352 - Hoerbarer schmaler Shift: Symbolkopplung

## Zweck

Diese Diagnose koppelt die in 1351 gefundenen kompakten Hoer-/Druckfenster passiv mit vorhandenen `episodes.csv`-Laeufen.
Geprueft wird, ob die Rohweltphase auch in Mini-DIOs eigener Syntax, Episodenspur und MCM-Bedeutung wieder auftaucht.

## Befund

- Fenster gesamt: 17
- Gemappte Fenster: 17
- Mappingstatus: {'mapped': 17}
- Top-Symbolfamilien: [('dio_104t', 8), ('dio_0m9z', 5), ('dio_0l7p', 1), ('dio_1lsu', 1), ('dio_1q7h', 1), ('dio_0ypg', 1)]
- Top-MCM-Preview-Symbole: [('dio_mcm_episode_14coypf', 4), ('dio_mcm_episode_0e7qvj1', 3), ('dio_mcm_episode_0lfde2c', 3), ('dio_mcm_episode_0b7nep9', 2), ('dio_mcm_episode_0geqqo3', 1), ('-', 1), ('dio_mcm_episode_183drjy', 1), ('dio_mcm_episode_1hdpu9s', 1)]
- Top-Bedeutungszustaende: [('meaning_stable_inner_field', 16), ('-', 1)]

## Rollenbezogene Kopplung

### brueckenuebergang_zum_lauten_kontakt

- Fenster: 4
- Symbolfamilien: [('dio_104t', 3), ('dio_0m9z', 1)]
- MCM-Preview-Symbole: [('dio_mcm_episode_0e7qvj1', 3), ('dio_mcm_episode_0b7nep9', 1)]
- Bedeutungszustaende: [('meaning_stable_inner_field', 4)]
- Rekopplung Mittel: 0.707504
- Strain Mittel: 0.155009

### lauter_kontakt_bleibt_offen

- Fenster: 1
- Symbolfamilien: [('dio_1lsu', 1)]
- MCM-Preview-Symbole: [('dio_mcm_episode_0b7nep9', 1)]
- Bedeutungszustaende: [('meaning_stable_inner_field', 1)]
- Rekopplung Mittel: 0.708659
- Strain Mittel: 0.150725

### randnaher_kontaktdruck

- Fenster: 5
- Symbolfamilien: [('dio_104t', 3), ('dio_0ypg', 1), ('dio_0m9z', 1)]
- MCM-Preview-Symbole: [('dio_mcm_episode_0lfde2c', 3), ('dio_mcm_episode_183drjy', 1), ('dio_mcm_episode_1eju9g0', 1)]
- Bedeutungszustaende: [('meaning_stable_inner_field', 4), ('-', 1)]
- Rekopplung Mittel: 0.694182
- Strain Mittel: 0.167970

### zentrumskontakt_mit_hoeranstieg

- Fenster: 5
- Symbolfamilien: [('dio_0m9z', 2), ('dio_104t', 2), ('dio_0l7p', 1)]
- MCM-Preview-Symbole: [('dio_mcm_episode_14coypf', 4), ('dio_mcm_episode_0geqqo3', 1)]
- Bedeutungszustaende: [('meaning_stable_inner_field', 5)]
- Rekopplung Mittel: 0.714447
- Strain Mittel: 0.148325

### zentrumskontakt_wird_aktiviert

- Fenster: 2
- Symbolfamilien: [('dio_1q7h', 1), ('dio_0m9z', 1)]
- MCM-Preview-Symbole: [('-', 1), ('dio_mcm_episode_1hdpu9s', 1)]
- Bedeutungszustaende: [('meaning_stable_inner_field', 2)]
- Rekopplung Mittel: 0.665833
- Strain Mittel: 0.163725

## Interpretation

Die kompakten Hoer-/Druckphasen sind nicht nur Rohweltmessungen.
Sie koppeln in den gemappten Fenstern an wiederkehrende Symbolfamilien, MCM-Preview-Symbole und Bedeutungszustaende.
Damit wird der Befund konkreter: Die Phase ist eine lokale Feldfunktion, die je nach Lage als Brueckenuebergang, Randdruck oder aktivierter Zentrumskontakt gelesen wird.

Wichtig: Diese Diagnose bleibt passiv. Sie erzeugt keine Handlung und keine Richtungsvorgabe.

## Wie es weitergeht

Als naechstes sollte die Symbolkopplung gegen eine Kontrollgruppe ohne Hoeranstieg geprueft werden. Nur so sehen wir, ob diese `dio_*`-Kopplung spezifisch fuer die kompakte Hoer-/Druckphase ist oder allgemein in beliebigen Weltfenstern auftritt.
