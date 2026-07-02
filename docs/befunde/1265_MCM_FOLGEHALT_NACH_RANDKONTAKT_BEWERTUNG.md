# Bewertung: MCM Folgehalt nach Randkontakt

Stand: 2026-07-02

## Kernaussage

Die MCM-Topologie wirkt nicht nur ueber Positionen, sondern ueber gehaltene Folgen.

Ein Zentrumskontakt nach Rand/Kipp ist nur dann stabil lesbar, wenn die Folge nicht sofort wieder in Rand/Kipp zurueckfaellt.

## Messbild

- untersuchte Randkontakte: `2962`
- direkter Rueckfall in Rand/Kipp nach Folgephase: `1056`
- kein direkter Rueckfall im naechsten Segment sichtbar: `1906`
- Folgearten: `{'offene_variante_entlastend_gehalten': 1447, 'offenheit_kurz_getragen_dann_rueckfall': 874, 'zentrum_stabil_entlastend_gehalten': 249, 'rekopplungsnaehe_entlastend_gehalten': 206, 'zentrum_kurz_getragen_dann_rueckfall': 181, 'offene_variante_gemischt_gehalten': 4, 'rekopplung_kurz_getragen_dann_rueckfall': 1}`

## Interpretation

Das Feld bildet keine starre Karte. Es zeigt eine dynamische Topologie:

- Rand/Kipp kann eine kurze Lastspitze sein.
- Zentrum kann nur ein Durchgang sein.
- Rekopplung kann tragen oder direkt wieder brechen.
- Offenheit kann Entlastung sein oder nur Zwischenraum vor neuer Spannung.

Das ist fuer MINI_DIO wichtig, weil Bedeutung nicht aus einem Einzelpunkt entsteht, sondern aus Feldfolge plus Folgehalt.

## Naechste Pruefung

Folgehalt mit Rohweltspannung koppeln: Nicht nur `was folgt im Feld`, sondern `welche Aussenweltform stand davor`.
