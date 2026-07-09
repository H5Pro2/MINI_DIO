# 1370 - Zentrumskontakt: Negativkontrolle Nachhallspur

## Zweck

Diese Diagnose prueft, ob die in `1367` gewaehlten Zentrumskontakt-Kontrollfenster zeitlich weitertragen.
Dazu werden Vorfenster, Trefferfenster und Folgefenster aus denselben Episodenspuren gelesen.

## Befund

- Fenster gesamt: `19`
- Preview traegt aus Vorfenster in Trefferfenster: `16`
- Preview traegt aus Trefferfenster in Folgefenster: `13`
- Symbolfamilie traegt aus Vorfenster in Trefferfenster: `16`
- Symbolfamilie traegt aus Trefferfenster in Folgefenster: `15`
- Durchschnittliches Rekopplungsdelta Folge minus Treffer: `-0.000878`
- Durchschnittliches Straindelta Folge minus Treffer: `0.000266`
- Rollenverteilung: [('brueckenuebergang_zum_lauten_kontakt', 7), ('rueckbindung_in_normale_weltspannung', 7), ('offener_uebergang_zum_lauten_kontakt', 4), ('lauter_kontakt_bleibt_offen', 1)]
- Preview im Trefferfenster: [('dio_mcm_episode_0e7qvj1', 7), ('dio_mcm_episode_1hdpu9s', 7), ('dio_mcm_episode_0ykar6i', 2), ('dio_mcm_episode_0b7nep9', 1), ('dio_mcm_episode_14l8khu', 1), ('dio_mcm_episode_1jwnjz4', 1)]
- Preview im Folgefenster: [('dio_mcm_episode_1hdpu9s', 8), ('dio_mcm_episode_0e7qvj1', 6), ('dio_mcm_episode_0b7nep9', 3), ('dio_mcm_episode_0lfde2c', 2)]

## Interpretation

Ein Teil der Shift-Preview-Symbole bleibt nach dem Trefferfenster erhalten. Das spricht fuer eine kurze Nachhall- oder Uebergangsspur.

Wichtig: Auch wenn das Top-Symbol wechselt, kann die Feldfunktion weitertragen. Deshalb sind Rekopplung, Strain und Rollenfolge wichtiger als reine Namensgleichheit.
