# MCM-Pfadklassifikation

## Zweck

Diese Diagnose erweitert die Verdichtungspfad-Lesart von vier Beispiel-Tokens auf alle gemeinsamen Tokens der Driftmatrix.
Sie ist passiv und klassifiziert Feldbewegungen, nicht Verhalten.

## Pfadklassen

| Pfadklasse | Anzahl |
|---|---:|

## Ausgangsbewegungen

| Bewegung aus Driftlupe | Anzahl |
|---|---:|

## Staerkste Tokens Je Pfadklasse

| Pfadklasse | Token | Bewegung | Basiszone | Folgezone | Beobachtungsdelta | Weltendelta | Grund |
|---|---|---|---|---|---:|---:|---|

## Befund

Offene Driftpfade sind mindestens so stark wie stabile oder rekoppelnde Pfade. Das wuerde auf eine noch stark weltgefaerbte Feldoberflaeche hinweisen.
Randpfade bleiben selten. Das passt zum bisherigen Befund: Randnaehe entsteht lokal, aber sie dominiert die Topologie nicht.

## Bedeutung Fuer MINI_DIO

Die Pfadklassifikation verschiebt die Lesart von Tokenlisten zu Feldbewegungen.
Ein `dio_mcm_episode_*`-Zeichen ist damit nicht nur ein Name, sondern kann eine Insel, ein Pfad, eine Bruecke oder eine Driftbewegung tragen.

## Wie es weitergeht

Als naechstes sollte diese Pfadklassifikation gegen eine weitere frische Weltgruppe reproduziert werden. Ziel: pruefen, ob die Verteilung der Pfadklassen stabil bleibt oder ob neue Weltspannung andere Pfadtypen erzwingt.
