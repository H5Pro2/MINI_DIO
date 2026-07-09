# 1419 - Rhythmus Amplitude Kontrast

## Zweck

Diese Pruefung trennt Rhythmusform von Lautstaerke.

Grundfrage:

Bleibt eine Rhythmusinsel erhalten, wenn dieselbe zeitliche Form leiser oder lauter wird?

## Aufbau

Geprueft wurden zwei Rhythmusformen:

- `regular`: harter Tickwechsel
- `wave`: wellenfoermige Bewegung

Beide Formen wurden mit niedriger, Basis- und hoher Amplitude verglichen.

## Befund

| Welt | Form | Pegel | Wechsel | Symbole | stabil | tragend_unruhig | Carry | Rekopplung | Strain | Kopplung | Nachhall |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| REGULAR_BASE | regular | base | 998 | 24 | 712 | 282 | 0.555928 | 0.713970 | 0.150471 | 0.826495 | 0.425093 |
| REGULAR_LOW | regular | low | 999 | 11 | 994 | 0 | 0.579544 | 0.730814 | 0.142139 | 0.853737 | 0.638319 |
| REGULAR_HIGH | regular | high | 999 | 45 | 514 | 480 | 0.527975 | 0.695736 | 0.159427 | 0.803296 | 0.227563 |
| WAVE_BASE | wave | base | 60 | 37 | 994 | 0 | 0.575977 | 0.737141 | 0.119177 | 0.901279 | 0.460114 |
| WAVE_LOW | wave | low | 60 | 19 | 994 | 0 | 0.596476 | 0.748774 | 0.117961 | 0.910305 | 0.638740 |
| WAVE_HIGH | wave | high | 60 | 64 | 975 | 19 | 0.559119 | 0.726057 | 0.126779 | 0.889030 | 0.364384 |

## Lesung

Der harte Tickwechsel ist amplitudensensibel.

Bei niedriger Amplitude wird `regular` vollstaendig stabil getragen. Bei hoher Amplitude kippt derselbe Rhythmus stark in `tragend_unruhig`. Die Form bleibt also erkennbar, aber die Lautstaerke entscheidet, ob sie feldtragend oder spannungsreicher wirkt.

Die Wellenform ist deutlich robuster.

Selbst bei hoher Amplitude bleibt `wave` fast vollstaendig stabil. Die Symbolzahl steigt, aber die Feldwirkung kollabiert nicht. Das spricht dafuer, dass wellenfoermige zeitliche Ordnung vom MCM-Feld besser integriert wird als harter Taktwechsel.

## Schlussfolgerung

Wir reden nicht nur von Rauschen.

Die Daten sprechen fuer eine Unterscheidung zwischen:

- Rhythmusform: zeitliche Ordnung / Melodie
- Amplitude: Lautstaerke / Energiepegel
- Feldwirkung: wie diese Ordnung im MCM-Feld getragen wird

Eine laute Welle bleibt tragfaehiger als ein lauter harter Tickwechsel. Damit bekommt der Begriff Harmonie hier eine technische Bedeutung: nicht Ruhe, sondern integrierbare zeitliche Ordnung.

## Grenze

Der Befund beschreibt passive Feldwirkung.

Er ist kein Handlungssignal, kein Gate und keine Strategie. Er zeigt nur, dass Mini-DIO Rhythmusform und Energiepegel unterschiedlich im Innenfeld verarbeitet.

## Wie es weitergeht

Als naechstes sollte eine echte Melodie-Welt gebaut werden: mehrere Ton-/Rhythmusphasen in Folge, nicht nur eine einzelne Rhythmusform. Dann pruefen wir, ob Mini-DIO nicht nur Rhythmus, sondern gerichtete melodische Ordnung als Bedeutungsfolge verdichtet.
