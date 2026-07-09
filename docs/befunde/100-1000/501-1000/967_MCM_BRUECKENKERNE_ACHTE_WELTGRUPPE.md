# MCM-Brueckenkerne Vergleich

## Zweck

Diese Diagnose vergleicht alle internen Brueckenpaare aus dem Brueckennetz.
Ziel ist zu pruefen, ob es einen zentralen Brueckenkern oder mehrere getrennte Brueckenkerne gibt.

## Kernklassen

| Klasse | Anzahl |
|---|---:|

## Brueckenpaare

| Klasse | Token A | Token B | Gewicht | Welten | bidirektional | A->B | B->A | Dauer | Exitphase |
|---|---|---|---:|---:|---:|---:|---:|---:|---|

## Befund

Es gibt keinen einzelnen dominanten zentralen Kern. Das Feld waere eher verteilt oder lokal organisiert.

## Bedeutung

Die Brueckentopologie wirkt hier hierarchisch:

```text
zentraler Brueckenkern
sekundaere Brueckenkerne
lokale Brueckenpfade
schwache Brueckenkanten
```

Damit entsteht keine flache Verbindungsliste, sondern eine strukturierte Uebergangstopologie.

## Wie es weitergeht

Als naechstes sollte die Rolle des zentralen Kerns gegen Randpfade und stabile Inseln gelesen werden: fuehrt der Kern eher in Zentrum, Rand oder offene Feldlagen?
