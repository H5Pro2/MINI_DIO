# 1953 - Reproduktion der dio_1492 ?bergangsketten

## Fragestellung

Nach dem Nachweis lokaler ?bergangsketten wurde gepr?ft, ob die st?rksten Ketten ?ber mehrere Weltgruppen wiederkehren oder nur lokal auftreten.

Hierarchie der Pr?fung:

- Grundfrage: Bleibt das lokale Feldnetz von `dio_1492` ?ber Weltgruppen erhalten?
- Unterpr?fung: Welche ?bergangsketten erscheinen fr?h, mittig oder sp?t erneut?
- Folgeschritt: Driftf?lle getrennt von stabilen Ketten untersuchen.

Die Pr?fung bleibt passiv. Es wird keine Handlungslogik, kein Signal und kein Gate abgeleitet.

## Datengrundlage

Quelle: `1952_DIO_1492_UEBERGANGSKETTEN.csv` und alle vorhandenen Verdichtungszonen-Transitionen.

- gepr?fte Ketten: `29`
- starke Ketten mit count >= 50: `8`

## Reproduktionsklassen

- `frueh_bis_mitte`: `11`
- `einzelgruppe`: `11`
- `lokal_reproduziert`: `7`

Starke Ketten:

- `frueh_bis_mitte`: `8`

## Befund

Die st?rksten Ketten sind nicht durchgehend ?ber alle sp?teren Weltgruppen stabil, aber mehrere von ihnen wiederholen sich von fr?hen bis mittleren Gruppen. Das spricht f?r reproduzierbare lokale Feldpfade, nicht f?r reine Einmalereignisse.

Gleichzeitig bricht die Reproduktion in sp?teren Gruppen teilweise ab. Das ist kein Widerspruch zur Achsenlesung: Die Achse kann stabil bleiben, w?hrend ihre ?bergangsketten unter anderer Weltspannung driften oder durch andere Anschlussr?ume ersetzt werden.

## St?rkste gepr?fte Ketten

- `dio_mcm_episode_0e7qvj1` outgoing `dio_mcm_episode_1hdpu9s`: count `176`, Dateien `5`, `frueh_bis_mitte`, `anschluss_zu_zentrum`
- `dio_mcm_episode_0e7qvj1` incoming `dio_mcm_episode_0mji3u6`: count `170`, Dateien `7`, `frueh_bis_mitte`, `anschluss_zu_uebergang`
- `dio_mcm_episode_0e7qvj1` incoming `dio_mcm_episode_1hdpu9s`: count `162`, Dateien `5`, `frueh_bis_mitte`, `anschluss_zu_zentrum`
- `dio_mcm_episode_0e7qvj1` outgoing `dio_mcm_episode_1jwnjz4`: count `113`, Dateien `6`, `frueh_bis_mitte`, `anschluss_zu_rekopplung`
- `dio_mcm_episode_0e7qvj1` incoming `dio_mcm_episode_1jwnjz4`: count `98`, Dateien `6`, `frueh_bis_mitte`, `anschluss_zu_rekopplung`
- `dio_mcm_episode_0e7qvj1` incoming `dio_mcm_episode_0z748ck`: count `87`, Dateien `5`, `frueh_bis_mitte`, `anschluss_zu_rekopplung`
- `dio_mcm_episode_0e7qvj1` outgoing `dio_mcm_episode_0mji3u6`: count `85`, Dateien `7`, `frueh_bis_mitte`, `anschluss_zu_uebergang`
- `dio_mcm_episode_0e7qvj1` outgoing `dio_mcm_episode_18l3thm`: count `60`, Dateien `4`, `frueh_bis_mitte`, `anschluss_zu_zentrum`
- `dio_mcm_episode_0e7qvj1` incoming `dio_mcm_episode_18l3thm`: count `49`, Dateien `4`, `frueh_bis_mitte`, `anschluss_zu_zentrum`
- `dio_mcm_episode_1q3us3f` incoming `dio_mcm_episode_18l3thm`: count `38`, Dateien `4`, `frueh_bis_mitte`, `anschluss_zu_zentrum`
- `dio_mcm_episode_1q3us3f` outgoing `dio_mcm_episode_1hdpu9s`: count `37`, Dateien `3`, `lokal_reproduziert`, `anschluss_zu_zentrum`
- `dio_mcm_episode_1q3us3f` incoming `dio_mcm_episode_1hdpu9s`: count `32`, Dateien `2`, `lokal_reproduziert`, `anschluss_zu_zentrum`

## Interpretation

`dio_1492` besitzt damit ein lokales Feldnetz mit reproduzierbaren Teilpfaden. Dieses Netz ist nicht vollst?ndig statisch. Es verh?lt sich eher wie eine stabile Achse mit kontextabh?ngigen ?bergangskorridoren.

Fachlich bedeutet das:

- Die Achse bleibt als Zentrum/Nulln?he-Struktur lesbar.
- Einige Ketten bleiben ?ber mehrere Weltgruppen erhalten.
- Sp?tere Weltgruppen k?nnen die Ketten ausd?nnen oder umlagern.
- Das Feldnetz zeigt damit Reproduktion und Drift zugleich.

## Grenze

Die Pr?fung zeigt keine bewusste Entscheidung. Sie zeigt passive Wiederkehr, Anschlussf?higkeit und Drift innerhalb des Bedeutungsnetzes.

## N?chster Pr?fpunkt

Als n?chstes sollten die Driftf?lle isoliert werden: Welche starken Ketten verschwinden in sp?ten Weltgruppen, und welche neuen Anschlussr?ume treten dort an ihre Stelle?
