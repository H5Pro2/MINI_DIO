# SYNTH_RAND_KIPP Endrand-Schwelle

## Fragestellung

Die vorherigen Gegenprüfungen zeigten:

- Der mittlere Binnenraum kann bereits 5 Rollen und 10 Rollen-Kombinationen bilden.
- Das volle 2000er-Fenster rekoppelt dieselbe Rollenbreite aber selektiv.
- Der Endrand erzeugt allein keine breite Rollenbildung.

Damit lautet die konkrete Unterprüfung:

Ab welcher Endrand-Erweiterung kippt ein vollständig rekoppelbares 5-Rollen-Feld in selektive Offline-Rekopplung?

## Prüffenster

Ausgangspunkt war das bekannte `SYNTH_RAND_KIPP start0`-Fenster. Geprüft wurden Ausschnitte ab `start250`, damit der Anfangsrand entfernt bleibt und die späte Randphase schrittweise zunimmt.

| Fenster | Weltbereich | Rollen | Kombinationen | Offline-Rekopplung |
| --- | --- | ---: | ---: | --- |
| 1500 | 250-1750 | 5 | 10 | vollständig |
| 1600 | 250-1850 | 5 | 10 | vollständig |
| 1650 | 250-1900 | 5 | 10 | vollständig |
| 1700 | 250-1950 | 5 | 10 | selektiv |
| 1750 | 250-2000 | 5 | 10 | selektiv |

## Messwerte

| Label | Rollen reaktiviert | Kombinationen voll | Kombinationen teilweise | Nachhall | Rekopplung | Carry | Strain |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `start250_size1600` | 5/5 | 10/10 | 0/10 | 0.6451 | 0.7347 | 0.5799 | 0.1345 |
| `start250_size1650` | 5/5 | 10/10 | 0/10 | 0.6320 | 0.7336 | 0.5784 | 0.1354 |
| `start250_size1700` | 4/5 | 6/10 | 4/10 | 0.6251 | 0.7327 | 0.5776 | 0.1364 |

## Befund

Die Kippschwelle liegt in dieser Prüfreihe zwischen `1650` und `1700` Zeilen.

Das ist fachlich wichtig, weil die Rollenbreite selbst unverändert bleibt: alle drei Schwellenfenster bilden 5 Rollen und 10 Kombinationen. Die Veränderung liegt also nicht in der Anzahl der Rollen, sondern in der Art, wie das Feld die Rollen nach der Offline-Phase wieder an die Welt koppelt.

## Interpretation

Der Endrand wirkt hier nicht als eigenständiger Rollenerzeuger. Er wirkt als Selektivitätsmodulator auf ein bereits vorhandenes breites Rollenfeld.

Das stützt die bisherige Trennung:

- Binnenraum: bildet Rollenbreite und Kombinationen.
- Endrand: verändert die spätere Offline-Rekopplung.
- Selektivität: entsteht nicht automatisch durch viele Rollen, sondern durch ein konkretes Feldmilieu aus Randnähe, Nachhall, Co-Touch-Qualität und gespannter Rollenverteilung.

## Status

Status: passiver Befund, keine Handlungslogik.

Dieser Befund ist eine belastbarere Eingrenzung der zuvor beobachteten selektiven Offline-Feld-Reorganisation. Er zeigt eine schmale Übergangszone, in der ein vollständig rekoppelbares Feld in selektive Rekopplung kippt.

## Wie es weitergeht

Als nächstes sollte geprüft werden, welche konkrete Weltform in `1650-1700` die Selektivität auslöst: Tonlage, Randnähe, visuelle Kippform, Nachhalländerung oder Rollen-Co-Touch.
