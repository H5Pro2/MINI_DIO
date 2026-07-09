# 1929 - B-Fokusfenster: korrigierter Hartkern-Brillen-Vergleich

## Grundfrage

Ist die Restkopplung der B-Fokusfenster nur bei DOGE sichtbar, oder entsteht sie auch, wenn dieselben synthetischen Weltformen mit SOL- und BTC-Weltlabel neu durch MINI_DIO laufen?

## Methodische Korrektur

Die erste Gegenlesung in [1922_SYN_B_FOCUS_HARTKERNBRILLEN_VERGLEICH.md](1922_SYN_B_FOCUS_HARTKERNBRILLEN_VERGLEICH.md) war methodisch zu grob.
Dort wurden SOL und BTC gegen DOGE-gelabelte Folgefenster gelesen.
Dadurch konnten SOL- und BTC-Kernpaare kaum auftauchen.

Die korrigierte Prüfung läuft anders:

```text
gleiche synthetische Weltform
aber eigener MINI_DIO-Lauf mit SOL-Label
aber eigener MINI_DIO-Lauf mit BTC-Label
danach Hartkernvergleich je passender Brille
```

## Ergebnis

| Brille | Fenster | getragen | geöffnet | verschoben | ausgeblendet | Score | Lesung |
|---|---|---:|---:|---:|---:|---:|---|
| DOGE | `2400_3900` | 0 | 2 | 1 | 31 | -0.574 | `kern_ausgeblendet` mit Öffnungsrest |
| DOGE | `3000_4500` | 0 | 1 | 0 | 33 | -0.626 | `kern_ausgeblendet` schwach |
| DOGE | `3200_5200` | 1 | 0 | 1 | 32 | -0.572 | `kern_ausgeblendet` mit Resttragung |
| SOL | `2400_3900` | 1 | 1 | 2 | 23 | -0.485 | `kern_ausgeblendet` mit Restkopplung |
| SOL | `3000_4500` | 3 | 1 | 1 | 22 | -0.400 | `kern_ausgeblendet` mit stärkster Restkopplung |
| SOL | `3200_5200` | 1 | 0 | 0 | 26 | -0.589 | `kern_ausgeblendet` schwach |
| BTC | `2400_3900` | 2 | 1 | 0 | 24 | -0.498 | `kern_ausgeblendet` mit Restkopplung |
| BTC | `3000_4500` | 3 | 1 | 1 | 22 | -0.400 | `kern_ausgeblendet` mit stärkster Restkopplung |
| BTC | `3200_5200` | 1 | 0 | 1 | 25 | -0.552 | `kern_ausgeblendet` mit Restverschiebung |

## Lesung

Die korrigierte Prüfung zeigt:
SOL und BTC sind nicht vollständig blind gegenüber den B-Fokusfenstern.
Auch sie bilden Restkopplung, wenn die Weltform mit passendem Weltlabel neu durch MINI_DIO läuft.

Der stärkste gemeinsame Restkopplungsbereich liegt bei `3000_4500`:

- SOL: 3 getragen, 1 geöffnet, 1 verschoben
- BTC: 3 getragen, 1 geöffnet, 1 verschoben

DOGE reagiert im selben Bereich schwächer.

## Bedeutung

Die relationale Formel bleibt gültig, muss aber präziser gelesen werden:

```text
Weltform + korrekt gelesene Hartkern-Brille -> Passungsprofil
```

Die Weltform trägt nicht jeden Kern gleich.
Aber wenn die Sinnesaufnahme korrekt unter dem jeweiligen Weltlabel erzeugt wird, können mehrere Hartkerne Restkopplung ausbilden.

Das stärkt die Interpretation von Restkopplung als reale Feldantwort und nicht als bloßes Artefakt einer einzelnen Brille.

## Methodischer Gewinn

Diese Korrektur ist wichtig:

- Sie trennt echte Ausblendung von falsch gelabelter Ausblendung.
- Sie zeigt, dass Weltpassung nur mit passender Wahrnehmungskette gelesen werden darf.
- Sie verhindert, dass fehlende Paare als Feldkollaps missverstanden werden.
