# Reale Uebergangswelt Und Sleep-Reproduktion

Stand: 2026-07-06

## Grundfrage

Ist selektive Sleep-Reaktivierung typisch fuer lange Uebergangsfenster, oder war sie eine Besonderheit der synthetischen Rand-/Kipp-Welt?

## Unterpruefung

Als reale 2000er-Uebergangswelt wurde `RUHIG_SIDEWAYS_2026 start6000` reproduziert:

```text
Real A: data/scan_ruhig-sideways-2026_start6000_size2000.csv
Sleep: passive Offline-Reorganisation
Real B: dieselbe Welt erneut
```

Die Pruefung bleibt passiv. Sie erzeugt keine Handlung, keine Richtung und kein Gate.

## Realwelt-Reproduktion

Real A und Real B blieben stabil:

- Episoden: `1994 -> 1994`
- Unique Syntax: `330 -> 330`
- Feldepisoden: `3 -> 3`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`
- MCM-Tragqualitaet: `0.512023 -> 0.512779`
- MCM-Rekopplung: `0.694806 -> 0.694040`

Damit ist auch diese reale Uebergangswelt reproduzierbar.

## Sleep-Reaktivierung

Die Sleep-Phase beruehrte 3 Rollen:

- `dio_mcm_episode_0e7qvj1`
- `dio_mcm_episode_1k2bqha`
- `dio_mcm_episode_0sjrih9`

Im Real-B-Follow-up:

- `3 / 3` Rollen wurden reaktiviert,
- `3 / 3` Kombinationen wurden voll reaktiviert,
- keine Rolle blieb unveraendert,
- keine Kombination blieb nur teilweise.

Der Sleep-Zustand blieb durchgehend:

```text
sleep_rekopplung
```

## Vergleich Zu SYNTH_RAND_KIPP

Der synthetische 2000er-Mehrrollen-Kandidat zeigte:

- `5` Rollen,
- `10` Kombinationen,
- `4 / 5` Rollen reaktiviert,
- `6 / 10` Kombinationen voll reaktiviert,
- `4 / 10` Kombinationen teilweise reaktiviert.

Die reale 2000er-Uebergangswelt zeigt dagegen:

- `3` Rollen,
- `3` Kombinationen,
- `3 / 3` Rollen reaktiviert,
- `3 / 3` Kombinationen voll reaktiviert.

## Lesung

Selektive Offline-Reorganisation ist damit nicht automatisch typisch fuer jedes lange Uebergangsfenster.

Aktuelle vorsichtige Lesung:

```text
Reale fokussierte Uebergangsfenster koennen voll rekoppeln.
Breitere synthetische Mehrrollennaehe kann selektiv rekoppeln.
```

Das spricht fuer unterschiedliche Offline-Kopplungsqualitaet je Feldmilieu:

- fokussierte Rollenlage: vollere Sleep-Reaktivierung,
- breite Rollenlage mit mehreren Strain-Kontakten: selektivere Sleep-Reaktivierung.

## Bedeutung Fuer MINI_DIO

MINI_DIO bildet nicht nur "Sleep ja/nein" ab.

Die Offline-Feld-Reorganisation unterscheidet bisher:

- fokussierte Rollensets,
- breite Rollensets,
- tragende Rollen,
- strainnahe Rollen,
- voll reaktivierte Kombinationen,
- teilweise reaktivierte Kombinationen.

Damit wird Sleep/Offline nicht als mechanischer Wiederholungsmodus lesbar, sondern als passive Reorganisationsqualitaet.

## Quellen

- [1589 SYNTH_RAND_KIPP 2000 Mehrrollen-Repro](1589_SYNTH_RAND_KIPP_2000_MEHRROLLEN_REPRO.md)
- [1590 SYNTH_RAND_KIPP Mehrrollen-Repro Synthese](1590_SYNTH_RAND_KIPP_MEHRROLLEN_REPRO_SYNTHESE.md)
- [1591 RUHIG_SIDEWAYS 2000 Uebergang-Repro](1591_RUHIG_SIDEWAYS_2000_UEBERGANG_REPRO.md)
