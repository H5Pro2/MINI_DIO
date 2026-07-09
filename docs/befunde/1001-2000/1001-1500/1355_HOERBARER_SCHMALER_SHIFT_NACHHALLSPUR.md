# 1355 - Hoerbarer schmaler Shift: Nachhallspur

## Zweck

Diese Diagnose prueft, ob die in `1352`/`1354` auffaelligen Shift-Preview-Symbole zeitlich weitertragen.
Dazu werden Vorfenster, Trefferfenster und Folgefenster aus denselben Episodenspuren gelesen.

## Befund

- Fenster gesamt: `17`
- Preview traegt aus Vorfenster in Trefferfenster: `11`
- Preview traegt aus Trefferfenster in Folgefenster: `15`
- Symbolfamilie traegt aus Vorfenster in Trefferfenster: `8`
- Symbolfamilie traegt aus Trefferfenster in Folgefenster: `6`
- Durchschnittliches Rekopplungsdelta Folge minus Treffer: `-0.039116`
- Durchschnittliches Straindelta Folge minus Treffer: `-0.011221`
- Rollenverteilung: [('zentrumskontakt_mit_hoeranstieg', 5), ('randnaher_kontaktdruck', 5), ('brueckenuebergang_zum_lauten_kontakt', 4), ('zentrumskontakt_wird_aktiviert', 2), ('lauter_kontakt_bleibt_offen', 1)]
- Preview im Trefferfenster: [('dio_mcm_episode_14coypf', 4), ('dio_mcm_episode_0e7qvj1', 3), ('dio_mcm_episode_0lfde2c', 3), ('dio_mcm_episode_0b7nep9', 2), ('dio_mcm_episode_0geqqo3', 1), ('-', 1), ('dio_mcm_episode_183drjy', 1), ('dio_mcm_episode_1hdpu9s', 1)]
- Preview im Folgefenster: [('dio_mcm_episode_14coypf', 4), ('dio_mcm_episode_0e7qvj1', 3), ('dio_mcm_episode_0lfde2c', 3), ('dio_mcm_episode_0b7nep9', 2), ('-', 2), ('dio_mcm_episode_0geqqo3', 1), ('dio_mcm_episode_183drjy', 1), ('dio_mcm_episode_1hdpu9s', 1)]

## Interpretation

Ein Teil der Shift-Preview-Symbole bleibt nach dem Trefferfenster erhalten. Das spricht fuer eine kurze Nachhall- oder Uebergangsspur.

Wichtig: Auch wenn das Top-Symbol wechselt, kann die Feldfunktion weitertragen. Deshalb sind Rekopplung, Strain und Rollenfolge wichtiger als reine Namensgleichheit.

## Wie es weitergeht

Als naechstes sollte die Nachhallspur rollenbezogen gelesen werden: Brueckenfenster, Randdruck und Zentrumskontakt getrennt vergleichen, statt alle Shiftfenster zusammenzufassen.
