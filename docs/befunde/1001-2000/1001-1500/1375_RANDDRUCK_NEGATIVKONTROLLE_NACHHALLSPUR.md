# 1375 - Randdruck: Negativkontrolle Nachhallspur

## Zweck

Diese Diagnose prueft, ob die Randdruck-Kontrollfenster aus `1374` zeitlich weitertragen.
Dazu werden Vorfenster, Trefferfenster und Folgefenster aus denselben Episodenspuren gelesen.

## Befund

- Fenster gesamt: `6`
- Preview traegt aus Vorfenster in Trefferfenster: `4`
- Preview traegt aus Trefferfenster in Folgefenster: `6`
- Symbolfamilie traegt aus Vorfenster in Trefferfenster: `1`
- Symbolfamilie traegt aus Trefferfenster in Folgefenster: `1`
- Durchschnittliches Rekopplungsdelta Folge minus Treffer: `0.000508`
- Durchschnittliches Straindelta Folge minus Treffer: `0.000624`
- Rollenverteilung: [('lauter_kontakt_bleibt_offen', 4), ('brueckenuebergang_zum_lauten_kontakt', 2)]
- Preview im Trefferfenster: [('dio_mcm_episode_0b7nep9', 4), ('dio_mcm_episode_0e7qvj1', 2)]
- Preview im Folgefenster: [('dio_mcm_episode_0b7nep9', 4), ('dio_mcm_episode_0e7qvj1', 2)]

## Interpretation

Ein Teil der Shift-Preview-Symbole bleibt nach dem Trefferfenster erhalten. Das spricht fuer eine kurze Nachhall- oder Uebergangsspur.

Wichtig: Auch wenn das Top-Symbol wechselt, kann die Feldfunktion weitertragen. Deshalb sind Rekopplung, Strain und Rollenfolge wichtiger als reine Namensgleichheit.

## Wie es weitergeht

Als naechstes wird die Nachhallspur rollenbezogen gelesen: Brueckenuebergang und offener lauter Kontakt getrennt vergleichen.
