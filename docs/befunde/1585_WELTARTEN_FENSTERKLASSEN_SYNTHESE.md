# Weltarten-Fensterklassen

Stand: 2026-07-06

## Grundfrage

Bleiben Einzelrekopplung, Uebergang und Mehrrollennaehe ueber unterschiedliche Weltarten als lokale Feldphasen sichtbar?

## Unterpruefung

Vier Weltarten wurden mit derselben Fensterlogik passiv gelesen:

- ruhige Seitwaertswelt: `RUHIG_SIDEWAYS_2026`
- negative Stresswelt: `STRESS_NEGATIV_2024`
- positive Expansionswelt: `EXPANSION_POSITIV_2023`
- synthetische Rand-/Kipp-Kontrollwelt: `SYNTH_RAND_KIPP`

Pro Welt wurden 9 Fenster mit je 1000 Zeilen und frischem Memory gelesen.

Die Pruefung erzeugt keine Handlung. Sie liest nur Feldrollen, Rekopplung, Carry und Strain.

## Ergebnis

Aus 36 Fenstern entstanden:

- `28` Einzelrekopplungen,
- `8` Uebergaenge mit Randkontakt,
- `0` breite Mehrrollen-Kandidaten.

Bemerkenswert ist die Gleichverteilung:

```text
Jede der vier Weltarten erzeugte 7 Einzelrekopplungen und 2 Uebergangsfenster.
```

Das spricht dafuer, dass Einzelrekopplung und Uebergang nicht nur an eine bestimmte Asset- oder Weltart gebunden sind. Sie erscheinen als lokale Feldphasen innerhalb unterschiedlicher Weltqualitaeten.

## Unterschiede Zwischen Den Weltarten

Die synthetische Rand-/Kipp-Welt hebt sich qualitativ ab:

- hoehere Rekopplung,
- hoehere Carry-Werte,
- niedrigere Strain-Werte,
- eigene dominante Feldrollennamen.

Die realen Welten zeigen dagegen staerker dieselben bekannten Rollenfamilien:

- `dio_mcm_episode_1k2bqha`
- `dio_mcm_episode_0e7qvj1`
- `dio_mcm_episode_1joiyc3`

Damit wirkt die synthetische Welt nicht einfach wie eine Kopie der realen Weltfenster. Sie bildet dieselbe grobe Feldklassik, aber mit anderer Feldfaerbung.

## Vorsicht

Die identische Verteilung `7/2` pro Welt ist interessant, aber noch kein Beweis fuer eine feste MCM-Regel.

Moegliche Lesarten:

- echte lokale Feldphasenstruktur,
- Effekt der 1000er-Fensterbreite,
- Effekt der aktuellen Klassifikationslogik,
- Kombination aus Weltstruktur und Diagnosefenster.

Deshalb ist der Befund stark genug fuer eine Folgediagnose, aber noch nicht stark genug fuer eine feste Aussage wie "jede Welt bildet immer 7/2".

## Bedeutung Fuer MINI_DIO

Die Pruefung stuetzt die aktuelle Arbeitsrichtung:

```text
Feldklassen sind lokale Feldphasen.
Sie sind nicht einfach Assetnamen und nicht reine Rohdatenetiketten.
```

MINI_DIO liest damit in dieser Stufe:

- dominante Einzelrekopplung,
- lokale Uebergangsnaehe,
- Randkontakt als kurzer Strain-Anteil,
- Weltfaerbung ueber Rekopplung, Carry, Strain und Rollennamen.

## Quellen

- [1584 Feldklassen-Fenstersuche Weltarten](1584_FELDKLASSEN_FENSTERSUCHE_WELTARTEN.md)
- [1584 CSV](1584_FELDKLASSEN_FENSTERSUCHE_WELTARTEN.csv)

## Wie es weitergeht

Als naechstes sollte die Fensterbreite variiert werden: 500er, 1000er und 2000er Fenster. Damit wird geprueft, ob die `7/2`-Struktur feldseitig stabil bleibt oder durch die aktuelle Fensterlaenge entsteht.
