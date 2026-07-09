# 1414 - Rhythmus Holdout Inseln

## Zweck

Diese Diagnose prueft die neuen Rhythmus-Holdout-Lagen aus `1395`.

Grundfrage:

Sind die neuen Rhythmuslagen beginnende Bedeutungsinseln oder nur kurzlebige Oberflaechenvarianz?

## Befund

- ausgewertete Rhythmuswelten: `4`
- Inselzustaende: `wiederkehrende_feldinsel:6, oberflaechenvarianz:2, schwache_inselwiederkehr:1`

## Weltuebersicht

- `HOLDOUT_RHYTHM_BLOCK`: schwache_inselwiederkehr:1, oberflaechenvarianz:1
- `HOLDOUT_RHYTHM_IRREGULAR`: wiederkehrende_feldinsel:2, oberflaechenvarianz:1
- `HOLDOUT_RHYTHM_REGULAR`: wiederkehrende_feldinsel:2
- `HOLDOUT_RHYTHM_WAVE`: wiederkehrende_feldinsel:2

## Wiederkehrende oder schwache Inseln

- `HOLDOUT_RHYTHM_BLOCK` -> `schwache_inselwiederkehr`, Fenster `2/10`, Familie `dio_1le1`, Carry `0.575074`, Strain `0.122053`, Rekopplung `0.733038`
- `HOLDOUT_RHYTHM_IRREGULAR` -> `wiederkehrende_feldinsel`, Fenster `6/10`, Familie `dio_1vsy`, Carry `0.554017`, Strain `0.139702`, Rekopplung `0.716849`
- `HOLDOUT_RHYTHM_IRREGULAR` -> `wiederkehrende_feldinsel`, Fenster `3/10`, Familie `dio_0ein`, Carry `0.552421`, Strain `0.140625`, Rekopplung `0.716111`
- `HOLDOUT_RHYTHM_REGULAR` -> `wiederkehrende_feldinsel`, Fenster `6/10`, Familie `dio_0ein`, Carry `0.563621`, Strain `0.150740`, Rekopplung `0.717062`
- `HOLDOUT_RHYTHM_REGULAR` -> `wiederkehrende_feldinsel`, Fenster `4/10`, Familie `dio_0ein`, Carry `0.544582`, Strain `0.150074`, Rekopplung `0.709410`
- `HOLDOUT_RHYTHM_WAVE` -> `wiederkehrende_feldinsel`, Fenster `5/10`, Familie `dio_13o0`, Carry `0.581898`, Strain `0.119308`, Rekopplung `0.739485`
- `HOLDOUT_RHYTHM_WAVE` -> `wiederkehrende_feldinsel`, Fenster `4/10`, Familie `dio_0n0i`, Carry `0.564142`, Strain `0.118579`, Rekopplung `0.732524`

## Lesung

Neue Holdout-Lage bedeutet hier nicht automatisch neue Bedeutung.
Entscheidend ist, ob dieselbe Signatur wiederkehrt, ueber mehrere Fenster getragen wird und dabei Carry, Rekopplung und Strain stabil bleiben.

Die Rhythmuspruefung trennt damit zwei Faelle:

- kurzlebige Oberflaechenvarianz: neue Lage taucht nur einzeln auf
- beginnende Feldinsel: neue Lage wiederholt sich mit tragfaehiger Feldkopplung
