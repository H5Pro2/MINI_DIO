# 303 - Rezeptorische MCM-Trennung

## Grundfrage

Was darf in das MCM-Feld wirken?

Die Außenwelt darf nicht ungefiltert als Rohdatenlage in das MCM-Feld fallen. Ein organisches System fühlt nicht die ganze Welt direkt, sondern nimmt sie über Rezeptoren auf. Diese Rezeptoren übersetzen Kontakt zur Außenwelt in eine innere Feldwirkung.

## Umsetzung

Die Sinnesaufnahme wurde in `mini_dio/mini_world.py` sauberer getrennt:

- `sehen`: Formfluss, Formstabilität, Formänderung.
- `hoeren`: Energieton, Energieverschiebung.
- `rezeptoren`: Kontaktlage zwischen äußerer Sinnesaufnahme und innerer Berührung.
- `fuehlen`: MCM-Feldwirkung, abgeleitet aus Rezeptorkontakt, nicht direkt aus Rohwelt.

Damit gilt:

```text
Außenwelt -> Sehen / Hören -> Rezeptoren -> Fühlen -> MCM-Feld
```

Nicht:

```text
Außenwelt -> MCM-Feld
```

## Rezeptorische Kontaktwerte

Die neue Rezeptorschicht beschreibt:

- `visual_contact`: wie stark die sichtbare Form berührt.
- `auditory_contact`: wie stark die energetische Hörspur berührt.
- `contact_pressure`: zusammengefasster Kontakt-/Druckwert.
- `contact_alignment`: Passung zwischen visueller und akustischer Berührung.
- `contact_asymmetry`: gerichtete Kontaktprägung.

Diese Werte sind passiv. Sie sind keine Gates, keine Entry-Signale, keine motorische Steuerung.

## Bedeutung für das MCM-Feld

Das MCM-Feld erhält jetzt nicht mehr direkt Formdaten oder Energiedaten, sondern die innere Wirkung des Rezeptorkontakts:

- `mcm_coherence` entsteht aus Kontaktpassung, Formstabilität und Druckentlastung.
- `mcm_tension` entspricht dem übersetzten Kontaktdruck.
- `mcm_asymmetry` entspricht der gerichteten Kontaktprägung.

Damit wird die MCM-Mechanik organischer: Mini-DIO sieht und hört eine Welt, aber fühlt nur das, was rezeptorisch als innere Berührung ankommt.

## Smoke-Befund

Smoke-Lauf:

- Welt: `SOL_2024_5M_RECEPTOR_SMOKE`
- Datei: `kontrolliert_sol_2024_5m_test1_2000_SOLUSDT.csv`
- Modus: `world_relative`
- Episoden: `1994`
- Trades: `0`

Messwerte aus `episodes.csv`:

- `rezeptor_visual_contact`: Mittelwert `0.299285`
- `rezeptor_auditory_contact`: Mittelwert `0.213473`
- `rezeptor_contact_pressure`: Mittelwert `0.215533`
- `rezeptor_contact_alignment`: Mittelwert `0.861686`
- `fuehlen_mcm_coherence`: Mittelwert `0.566338`
- `fuehlen_mcm_tension`: Mittelwert `0.215533`

Der Lauf bestätigt technisch:

- Die Rezeptorschicht wird geschrieben.
- Die MCM-Fühlwerte werden aus Rezeptorkontakt abgeleitet.
- Die Änderung bleibt passiv und erzeugt keine Handlungskopplung.

## Forschungsstand

Das ist keine neue Handelslogik. Es ist eine Korrektur der Wahrnehmungsontologie:

Mini-DIO erlebt nicht Rohdaten. Mini-DIO erlebt rezeptorisch übersetzte Außenweltwirkung.

Diese Trennung ist wichtig, weil sonst Sehen, Hören und Fühlen vermischt werden und das MCM-Feld zu viele externe Daten direkt tragen muss.

## Wie es weitergeht

Als nächstes sollte die Rezeptortrennung über mehrere bereits geprüfte Welten laufen: SOL, BTC und KAS auf 5m und 1h. Ziel ist zu prüfen, ob die Topologie stabil bleibt und ob `contact_pressure` / `contact_alignment` die bisherigen Öffnungs- und Rekopplungsmuster sauberer erklären.
