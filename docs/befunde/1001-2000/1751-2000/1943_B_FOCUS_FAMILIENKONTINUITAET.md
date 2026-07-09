# 1943 - B-Fokus Nachbarfenster: Familienkontinuit?t

## Grundfrage

Besteht die B-Fokus-Restkopplungszone aus denselben Familien, oder aktiviert jede Teilzone andere Rollen?

## Methode

Gelesen wurden die nicht ausgeblendeten Hartkern-Familien aus:

- SOL `2800_4300`, `3000_4500`, `3200_4700`
- BTC `2800_4300`, `3000_4500`, `3200_4700`

Ein Slot bedeutet: eine Familie/Phase bleibt in einem Asset-Fenster nicht ausgeblendet.

## Ergebnis

| Familie | Phase | Slots | Assets | Zustandsprofil | Qualit?tsprofil | Lesung |
|---|---|---:|---|---|---|---|
| `dio_0tay` | `frueh` | 6 | `BTC;SOL` | `lokale_qualitaet_reproduziert:6` | `phase_nullnah:6` | `durchgehender_zonaler_traeger` |
| `dio_06er` | `frueh` | 4 | `BTC;SOL` | `lokale_qualitaet_wird_kernnah:2; lokale_qualitaet_driftet:2` | `phase_kernnah:2; phase_ohne_nullfamilie:2` | `zonaler_uebergangstraeger` |
| `dio_14wj` | `frueh` | 4 | `BTC;SOL` | `lokale_qualitaet_reproduziert:4` | `phase_nullnah:4` | `starker_zonaler_traeger` |
| `dio_0nlj` | `mitte` | 3 | `BTC` | `lokale_qualitaet_wird_offen:2; lokale_qualitaet_reproduziert:1` | `phase_offen_gemischt:2; phase_nullnah:1` | `asset_spezifischer_zonentraeger` |
| `dio_14wj` | `spaet` | 3 | `BTC` | `lokale_qualitaet_reproduziert:3` | `phase_nullnah:3` | `asset_spezifischer_zonentraeger` |
| `dio_1kpz` | `frueh` | 3 | `SOL` | `lokale_qualitaet_reproduziert:2; lokale_qualitaet_driftet:1` | `phase_nullnah:2; phase_ohne_nullfamilie:1` | `asset_spezifischer_zonentraeger` |
| `dio_1kpz` | `mitte` | 2 | `SOL` | `lokale_qualitaet_wird_offen:1; lokale_qualitaet_reproduziert:1` | `phase_offen_gemischt:1; phase_nullnah:1` | `lokale_teilzonenrolle` |
| `dio_0nlj` | `spaet` | 1 | `BTC` | `lokale_qualitaet_wird_offen:1` | `phase_offen_gemischt:1` | `einzelfenster_restrolle` |

## Befund

`dio_0tay/frueh` ist der st?rkste zonale Tr?ger. Diese Familie bleibt in allen sechs Slots sichtbar und reproduziert ?berall `phase_nullnah`.

`dio_14wj/frueh` ist ein starker gemeinsamer Tr?ger, aber nicht ?ber die komplette Zone. Die Familie tr?gt links und in der Mitte bei SOL und BTC, verschwindet aber im rechten Nachbarfenster.

`dio_06er/frueh` ist keine stabile Reproduktion, sondern eine ?bergangsrolle. Links wird sie kernnah, in der Mitte driftet sie ohne Nullfamilie. Das liest sich wie ein Rand-/Br?ckenverhalten innerhalb derselben Zone.

Asset-spezifisch:

- BTC h?lt zus?tzlich `dio_14wj/spaet` ?ber alle drei Fenster stabil nullnah.
- BTC h?lt `dio_0nlj/mitte` ?ber alle drei Fenster, aber offen bis nullnah.
- SOL h?lt `dio_1kpz/frueh` ?ber alle drei Fenster, aber mit Drift links und Nulln?he in Mitte/Rechts.

## Bedeutung f?r MINI_DIO

Die Zone besteht nicht aus beliebigem Rauschen. Es gibt einen durchgehenden gemeinsamen Tr?ger, mehrere Teilzonentr?ger und asset-spezifische Nebentr?ger.

Damit kann MINI_DIO sp?ter Bedeutungsr?ume feiner lesen:

```text
Zonaler Kerntr?ger      -> bleibt ?ber Weltformbereich stabil
Teilzonentr?ger         -> tr?gt nur in bestimmten Abschnitten
?bergangsrolle          -> zeigt Drift, ?ffnung oder Kernn?he
Asset-spezifischer Rand -> geh?rt st?rker zur jeweiligen Brille
```

Das ist weiter passiv. Es wird keine Handlung daraus abgeleitet.

## Wie es weitergeht

Als n?chstes sollte `dio_0tay/frueh` r?ckgelesen werden: Welche Rohwelt- und Feldmerkmale machen diese Familie ?ber SOL und BTC hinweg zum durchgehenden zonalen Tr?ger?
