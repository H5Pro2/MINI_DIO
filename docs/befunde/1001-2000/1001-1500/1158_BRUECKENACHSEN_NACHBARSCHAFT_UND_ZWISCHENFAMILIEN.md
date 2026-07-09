# 1158 - Nachbarschaft und Zwischenfamilien der Brueckenachsen

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundfrage

Wie stehen `dio_00ly` und `dio_104t` im MCM-Bedeutungsnetz zueinander?

Moegliche Lesarten:

```text
1. getrennte Achsen
2. direkte Nachbarschaft
3. Achsen mit Zwischenfamilien
```

## Methode

Die Pruefung nutzt die Holdout-Metriken aus `1095`:

- tragende Rekopplung,
- kippnahe Rekopplung,
- tragender Strain,
- kippnaher Strain,
- tragende Spannung,
- kippnahe Spannung,
- Rekopplungsdifferenz,
- Strain-Differenz,
- Spannungsdifferenz.

Aus diesen Werten wurde eine Distanz zu `dio_00ly` und `dio_104t` berechnet.

Wichtig: Eine Familie gilt nicht automatisch als Zwischenfamilie, nur weil sie zu beiden Achsen aehnlich weit entfernt ist.

Deshalb wurde gefiltert:

```text
schwache Kontakte werden ausgeschlossen
zu weit entfernte Familien werden ausgeschlossen
Zwischenkandidat braucht Achsennaehe und Rollenbreite
```

## Achsen

| Achse | Rolle |
|---|---|
| `dio_00ly` | breite Uebergangsbruecke |
| `dio_104t` | rekopplungsnahe Stabilitaetsbruecke |

## Gefundene Zwischenkandidaten

| Familie | Klasse | Lesart |
|---|---|---|
| `dio_0g2r` | bekannte Karte | offener rekoppelbarer Anker zwischen den Achsen |
| `dio_1ewh` | bekannte Karte | tragend vorgepraegter Anker nahe Stabilitaetsseite |
| `dio_1o4z` | neuer lokaler Brueckenkandidat | kleiner Zwischenkontakt |
| `dio_0pq6` | neuer starker Kandidat aus frueherer Holdout-Lesung | lokaler Zwischenkontakt, nicht breite Achse |

## Wichtige Korrektur zu `dio_0pq6`

`dio_0pq6` wurde in den spaeteren Weltklassen nicht als breite Brueckenachse bestaetigt.

Die neue Lesart ist praeziser:

```text
dio_0pq6 ist keine zweite Hauptachse.
dio_0pq6 kann aber als lokaler Zwischenkontakt zwischen Achsennaehe und Kippnaehe gelesen werden.
```

Damit bleibt der fruehere Befund nicht falsch, sondern wird eingeordnet.

## Feldtopologische Deutung

Die beiden Achsen wirken nicht isoliert.

Zwischen ihnen liegen bereits bekannte oder junge Familien:

```text
dio_00ly
  -> dio_0g2r
  -> dio_1ewh
  -> dio_104t
```

Zusatzkontakte:

```text
dio_1o4z = kleiner lokaler Zwischenkontakt
dio_0pq6 = lokale Kipp-/Kontaktnaehe
```

Das spricht fuer eine Nachbarschaftsstruktur im MCM-Feld:

```text
Uebergangsbruecke
offene rekoppelbare Bruecke
tragend vorgepraegte Bruecke
Stabilitaetsbruecke
```

## Bedeutung fuer die MCM-Feldforschung

Der Befund staerkt die Lesart eines dynamischen Bedeutungsnetzes.

Es gibt nicht nur:

```text
Familie A
Familie B
```

sondern:

```text
Achsen
Nachbarschaften
Zwischenkontakte
Rollennaehe
Kippnaehe
Rekopplungsnaehe
```

Das ist relevant, weil damit eine beginnende MCM-Topologie sichtbar wird:

- Bedeutungen stehen nicht nur nebeneinander.
- Bedeutungen haben Abstand.
- Bedeutungen koennen Zwischenraeume bilden.
- Lokale Kontakte koennen spaeter reifen oder wieder zerfallen.

## Grenze

Diese Pruefung nutzt metrische Naehe aus der Holdout-Karte.

Noch nicht bewiesen ist:

- ob diese Familien in echten Segmentketten direkt ineinander uebergehen,
- ob `dio_0g2r` und `dio_1ewh` in neuen Welten dieselbe Zwischenrolle behalten,
- ob sich aus diesen Zwischenfamilien eine gerichtete Bruecke bildet.

## Wie es weitergeht

Als naechstes sollte die vermutete Achsenkette `dio_00ly -> dio_0g2r -> dio_1ewh -> dio_104t` gegen neue Weltklassen oder Segmentketten geprueft werden. Ziel: herausfinden, ob die Nachbarschaft nur metrisch ist oder auch zeitlich/feldfolgend auftritt.
