# Sinnesgetrennte Achspruefung

Stand: 2026-06-20

## Grundfrage

Reagieren die neuen Wahrnehmungsfaehigkeiten von MINI_DIO getrennt genug, oder entsteht wieder eine globale, gleichfoermige Regulation?

## Gepruefte Welten

Es wurden vier kurze Kontrollwelten mit frischer Memory und `world_relative` gelesen:

- `REAL_SOL_1000`
- `NEG_STRESS_2023_1000`
- `POS_EXPANSION_2023_1000`
- `BRIDGE_2024_1000`

Die Rohdaten liegen in:

```text
docs/befunde/401_SINNESGETRENNTE_ACHSPRUEFUNG.csv
```

## Ergebnis

| Welt | Symbole | Avg Feldinput | Max Feldinput | Avg Anpassungspotenzial | Max Anpassungspotenzial | Sehfokus | Sichtabstand | Hinhoeren | Hoerdaempfung | Fuehlabstand | Rekopplung | Strain |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| REAL_SOL_1000 | 256 | 0.1281 | 0.5461 | 0.1350 | 0.2442 | 0.6424 | 0.3480 | 0.7810 | 0.2190 | 0.1850 | 0.6873 | 0.1628 |
| NEG_STRESS_2023_1000 | 229 | 0.1219 | 0.5161 | 0.1338 | 0.2423 | 0.6413 | 0.3517 | 0.7900 | 0.2100 | 0.1826 | 0.6908 | 0.1605 |
| POS_EXPANSION_2023_1000 | 244 | 0.1228 | 0.5263 | 0.1352 | 0.2567 | 0.6405 | 0.3601 | 0.7874 | 0.2126 | 0.1864 | 0.6888 | 0.1616 |
| BRIDGE_2024_1000 | 258 | 0.1289 | 0.5422 | 0.1359 | 0.2577 | 0.6412 | 0.3531 | 0.7797 | 0.2203 | 0.1872 | 0.6867 | 0.1639 |

## Interpretation

Die technische Trennung funktioniert:

```text
field_intake_pressure = echte Rezeptorwirkung
adaptation_potential = beobachtbare Anpassungsfaehigkeit
adapted_field_intake_pressure = Diagnosewert, keine Feldsteuerung
```

Die Weltmittelwerte liegen aber noch eng beieinander.
Das bedeutet:

```text
Die Achsen sind sauber sichtbar, aber im globalen Mittel noch nicht stark welttrennend.
```

Das ist kein Fehler.
Weltmittelwerte glaetten lokale Unterschiede stark.
Eine Welt kann lokal kippen, rekoppeln oder driften, obwohl der Durchschnitt ruhig aussieht.

## Fachliche Schlussfolgerung

Die aktuelle Schicht darf nicht wieder als globale Daempfung verstanden werden.

Sie ist ein Satz von Organismus-Faehigkeiten:

- genauer sehen,
- Abstand zur Form halten,
- genauer hinhoeren,
- leiser aufnehmen,
- Kontakt zulassen,
- Fuehlabstand bilden.

Welche Kombination tragfaehig ist, muss aus Episoden gelernt werden.

## Naechster Pruefpunkt

Die naechste Pruefung muss lokal sein:

```text
Welche Episoden zeigen mehr Sehen?
Welche Episoden zeigen mehr Hoeren?
Welche Episoden zeigen mehr Abstand?
Welche davon rekoppeln?
Welche bleiben als Strain oder Kippnaehe stehen?
```

Erst diese lokale Kopplung beantwortet, ob MINI_DIO lernt, seine Wahrnehmungsfaehigkeiten differenziert zu nutzen.

## Wie es weitergeht

Als naechstes wird eine lokale Achsenkarte gebaut: Episode fuer Episode wird gelesen, ob Sehen, Hoeren oder Fuehlabstand dominiert und ob die jeweilige Achsenlage getragen, kippnah oder rekoppelnd war.
