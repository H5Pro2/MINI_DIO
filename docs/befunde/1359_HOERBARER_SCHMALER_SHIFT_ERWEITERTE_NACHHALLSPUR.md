# 1359 - Hoerbarer schmaler Shift: Erweiterte Nachhallspur

## Zweck

Diese Diagnose prueft, ob die in `1352`/`1354` auffaelligen Shift-Preview-Symbole zeitlich weitertragen.
Dazu werden Vorfenster, Trefferfenster und Folgefenster aus denselben Episodenspuren gelesen.

## Befund

- Fenster gesamt: `36`
- Preview traegt aus Vorfenster in Trefferfenster: `24`
- Preview traegt aus Trefferfenster in Folgefenster: `28`
- Symbolfamilie traegt aus Vorfenster in Trefferfenster: `18`
- Symbolfamilie traegt aus Trefferfenster in Folgefenster: `14`
- Durchschnittliches Rekopplungsdelta Folge minus Treffer: `-0.057703`
- Durchschnittliches Straindelta Folge minus Treffer: `-0.014062`
- Rollenverteilung: [('brueckenuebergang_zum_lauten_kontakt', 10), ('randnaher_kontaktdruck', 8), ('zentrumskontakt_mit_hoeranstieg', 7), ('lauter_kontakt_bleibt_offen', 4), ('rueckbindung_in_normale_weltspannung', 4), ('zentrumskontakt_wird_aktiviert', 2), ('offener_uebergang_zum_lauten_kontakt', 1)]
- Preview im Trefferfenster: [('dio_mcm_episode_0b7nep9', 7), ('dio_mcm_episode_14coypf', 6), ('dio_mcm_episode_0lfde2c', 6), ('dio_mcm_episode_0e7qvj1', 5), ('dio_mcm_episode_0ykar6i', 3), ('dio_mcm_episode_1rxdw4p', 3), ('dio_mcm_episode_1hdpu9s', 2), ('dio_mcm_episode_0geqqo3', 1)]
- Preview im Folgefenster: [('dio_mcm_episode_0b7nep9', 10), ('dio_mcm_episode_0e7qvj1', 6), ('dio_mcm_episode_14coypf', 6), ('dio_mcm_episode_0lfde2c', 4), ('-', 4), ('dio_mcm_episode_1hdpu9s', 2), ('dio_mcm_episode_1rxdw4p', 2), ('dio_mcm_episode_0geqqo3', 1)]

## Interpretation

Ein Teil der Shift-Preview-Symbole bleibt nach dem Trefferfenster erhalten. Das spricht fuer eine kurze Nachhall- oder Uebergangsspur.

Wichtig: Auch wenn das Top-Symbol wechselt, kann die Feldfunktion weitertragen. Deshalb sind Rekopplung, Strain und Rollenfolge wichtiger als reine Namensgleichheit.

## Wie es weitergeht

Als naechstes sollte die Nachhallspur rollenbezogen gelesen werden: Brueckenfenster, Randdruck und Zentrumskontakt getrennt vergleichen, statt alle Shiftfenster zusammenzufassen.
