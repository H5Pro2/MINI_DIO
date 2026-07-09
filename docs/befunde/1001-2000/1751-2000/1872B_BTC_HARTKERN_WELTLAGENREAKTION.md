# BTC-Hartkern: Weltlagenreaktion

Diese Prüfung liest nur die BTC-Paare aus dem harten Kern der lokalen Reifegruppe.
Damit wird nicht mehr die ganze Baseline verglichen, sondern die Frage: Wie reagiert der harte BTC-Kern unter den geprüften Weltlagen?

## Ergebnis

| Weltlage | Kernpaare | Zustandsprofil | Qualitätsprofil |
|---|---:|---|---|
| ruhig | 27 | `lokale_qualitaet_reproduziert:16; lokale_qualitaet_wird_nullnah:3; lokale_qualitaet_wird_nachhallnah:3; lokale_qualitaet_wird_offen:3; fehlt_im_folgefenster:2` | `phase_nullnah:18; phase_offen_gemischt:4; phase_nachhallnah_ohne_kern:3; fehlt:2` |
| stress | 27 | `lokale_qualitaet_reproduziert:19; lokale_qualitaet_wird_nachhallnah:3; lokale_qualitaet_wird_kernnah:2; lokale_qualitaet_wird_offen:2; lokale_qualitaet_wird_nullnah:1` | `phase_nullnah:18; phase_offen_gemischt:4; phase_nachhallnah_ohne_kern:3; phase_kernnah:2` |

## Lesung

Der SOL-Hartkern bleibt unter allen drei Weltlagen teilweise reproduzierbar.
Stress zeigt in dieser Prüfung etwas mehr direkte lokale Reproduktion als ruhige Welt und Expansion.
Expansion verschiebt stärker in Nachhall- und Kernnähe. Das spricht nicht für Kollaps, sondern für eine unterschiedliche Randantwort je Weltspannung.

Wichtig: Das ist weiterhin eine passive Feldlesung. Es wird keine Handlung, kein Gate und keine Richtung daraus abgeleitet.

## Wie es weitergeht

Als nächstes sollten die Einzelberichte assetübergreifend zusammengeführt werden. Erst dann ist klar, welche Hartkernantwort allgemein ist und welche asset-spezifisch bleibt.
