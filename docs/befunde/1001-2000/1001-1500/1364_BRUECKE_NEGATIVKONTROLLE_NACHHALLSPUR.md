# 1364 - Brueckenfunktion: Negativkontrolle Nachhallspur

## Zweck

Diese Diagnose prueft, ob die in `1352`/`1354` auffaelligen Shift-Preview-Symbole zeitlich weitertragen.
Dazu werden Vorfenster, Trefferfenster und Folgefenster aus denselben Episodenspuren gelesen.

## Befund

- Fenster gesamt: `20`
- Preview traegt aus Vorfenster in Trefferfenster: `15`
- Preview traegt aus Trefferfenster in Folgefenster: `14`
- Symbolfamilie traegt aus Vorfenster in Trefferfenster: `13`
- Symbolfamilie traegt aus Trefferfenster in Folgefenster: `14`
- Durchschnittliches Rekopplungsdelta Folge minus Treffer: `-0.000942`
- Durchschnittliches Straindelta Folge minus Treffer: `0.000788`
- Rollenverteilung: [('rueckbindung_in_normale_weltspannung', 17), ('unklare_mikrophase', 3)]
- Preview im Trefferfenster: [('dio_mcm_episode_0e7qvj1', 11), ('dio_mcm_episode_1rxdw4p', 3), ('dio_mcm_episode_1hdpu9s', 3), ('dio_mcm_episode_1jwnjz4', 2), ('dio_mcm_episode_1joiyc3', 1)]
- Preview im Folgefenster: [('dio_mcm_episode_0e7qvj1', 12), ('dio_mcm_episode_1hdpu9s', 3), ('dio_mcm_episode_1rxdw4p', 2), ('dio_mcm_episode_0gqol8d', 1), ('dio_mcm_episode_1joiyc3', 1), ('dio_mcm_episode_1jwnjz4', 1)]

## Interpretation

Ein Teil der Shift-Preview-Symbole bleibt nach dem Trefferfenster erhalten. Das spricht fuer eine kurze Nachhall- oder Uebergangsspur.

Wichtig: Auch wenn das Top-Symbol wechselt, kann die Feldfunktion weitertragen. Deshalb sind Rekopplung, Strain und Rollenfolge wichtiger als reine Namensgleichheit.

## Wie es weitergeht

Als naechstes sollte die Nachhallspur rollenbezogen gelesen werden: Brueckenfenster, Randdruck und Zentrumskontakt getrennt vergleichen, statt alle Shiftfenster zusammenzufassen.
