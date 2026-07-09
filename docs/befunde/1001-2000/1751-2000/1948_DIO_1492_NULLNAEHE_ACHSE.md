# 1948 - dio_1492 als nullnahe Kohärenzachse

## Grundfrage

`dio_1492` sollte nicht als einzelne Referenzrolle gelesen werden, sondern als mögliche Achse:

`frueh -> mitte -> spaet`

Die Frage lautet:

Bildet `dio_1492` über mehrere Phasen eine stabile nullnahe Kohärenzbahn?

## Vorgehen

Ausgewertet wurden zwei vorhandene Folgefenster-Prüfungen:

- `1861_PHASENLOKALE_FAMILIEN_REPRO_FOLGEFENSTER.csv`
- `1864_LOKALE_REIFEGRUPPE_REPRO_WEITERE_FENSTER.csv`

Für jedes Asset wurde geprüft:

- ist `dio_1492` in `frueh`, `mitte`, `spaet` vorhanden?
- werden alle drei Phasen stabil reproduziert?
- bleibt die dominante Qualität `phase_nullnah`?

## Ergebnis

Es wurden 8 Asset/Followup-Kombinationen gefunden.

Davon:

- 6 vollständige `phase_nullnah`-Achsen
- 2 Teilachsen oder Varianzfälle

| Quelle | Asset | Achsenzustand | stabile Phasen | Qualitäten |
| --- | --- | --- | --- | --- |
| 1861 | BTC | vollständige Nullnähe-Achse | frueh, mitte, spaet | nullnah, nullnah, nullnah |
| 1861 | DOGE | vollständige Nullnähe-Achse | frueh, mitte, spaet | nullnah, nullnah, nullnah |
| 1861 | XRP | vollständige Nullnähe-Achse | frueh, mitte, spaet | nullnah, nullnah, nullnah |
| 1861 | SOL | Teilachse oder Varianz | frueh, spaet | nullnah, offen, nullnah |
| 1864 | BTC | vollständige Nullnähe-Achse | frueh, mitte, spaet | nullnah, nullnah, nullnah |
| 1864 | DOGE | vollständige Nullnähe-Achse | frueh, mitte, spaet | nullnah, nullnah, nullnah |
| 1864 | SOL | vollständige Nullnähe-Achse | frueh, mitte, spaet | nullnah, nullnah, nullnah |
| 1864 | XRP | Teilachse oder Varianz | mitte | kernnah, nullnah, offen |

## Einordnung

`dio_1492` wirkt nicht wie ein einzelner Punkt im Feld.

Die Familie verhält sich eher wie eine phasenübergreifende Achse:

- frühe Lage: nullnahe Anbindung
- mittlere Lage: häufig weiter nullnah, aber anfälliger für Öffnung
- späte Lage: häufig weiter nullnah, aber weltabhängig

Damit ist `dio_1492` fachlich anders als `dio_0tay/frueh`.

`dio_0tay/frueh` ist eine frühe Brückenberuhigung.

`dio_1492` ist eher eine nullnahe Kohärenzbahn über mehrere Feldphasen.

## Wichtig

Das ist keine harte Achse.

SOL und XRP zeigen, dass die Bahn unter bestimmten Weltbedingungen teilweise öffnet oder verschoben wird. Genau deshalb darf `dio_1492` nicht als starre Referenzrolle übernommen werden.

Besser ist:

`dio_1492` als Achsenkandidat führen, aber noch nicht als passive Referenzrolle speichern.

## Schlussfolgerung

Die MCM-Topologie zeigt hier nicht nur einzelne Rollen, sondern mögliche Feldbahnen.

Das ist für Mini-DIO wichtig, weil damit Bedeutung nicht nur als Punkt entsteht, sondern als Bewegung über Phasen:

- eine Rolle kann punktuell sein,
- eine Rolle kann zonal sein,
- eine Rolle kann achsenförmig über Zeit/Feldphase laufen.
