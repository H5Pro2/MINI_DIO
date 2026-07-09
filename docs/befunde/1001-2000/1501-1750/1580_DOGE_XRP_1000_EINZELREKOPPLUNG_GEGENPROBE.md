# DOGE/XRP 1000: Einzelrekopplung als Gegenprobe

Stand: 2026-07-05 23:31

## Grundfrage

Gibt es neben BTC ein weiteres Nicht-SOL-Fenster, das zwischen Einzelrekopplung und breitem Mehrrollenfeld liegt?

## Unterprüfung

Geprüft wurden zwei neue 1000-Zeilen-Fenster aus vorhandenen 10k-Welten:

- `data/kontrolliert_doge2024_sleep_origin_1000_5m.csv`
- `data/kontrolliert_xrp2024_sleep_origin_1000_5m.csv`

Beide wurden als Real-Sleep-Real-Kette mit frischem Memory, `world_relative`-Sinnesaufnahme und weicher Sleep-Reorganisation ausgeführt.

## Ergebnis DOGE

- Real-A-Feldrollen: `1`
- lange tragende Rollen: `1`
- Strain-Rollen: `0`
- Sleep-Kombinationen: `0`
- reaktivierte Rollen: `1 / 1`
- Feldrolle: `dio_mcm_episode_1joiyc3`

Lesung:

DOGE bildet in diesem 1000er-Fenster keine Übergangsklasse. Trotz eigener Asset-Färbung bleibt das Innenfeld auf eine dominante Feldrolle gebunden.

## Ergebnis XRP

- Real-A-Feldrollen: `1`
- lange tragende Rollen: `1`
- Strain-Rollen: `0`
- Sleep-Kombinationen: `0`
- reaktivierte Rollen: `1 / 1`
- Feldrolle: `dio_mcm_episode_1joiyc3`

Lesung:

XRP verhält sich in diesem 1000er-Fenster ebenfalls wie Einzelrekopplung. Es entsteht keine mehrrollige Feldnähe und keine Offline-Kombination.

## Vergleich zur bisherigen Abstufung

```text
PAXG/KAS/DOGE/XRP 1000
  -> Einzelrekopplung
  -> eine dominante Feldrolle
  -> keine Sleep-Kombination

BTC 1000
  -> Übergangsfeld
  -> zwei tragende Rollen + kurzer Strain-Kontakt
  -> drei Sleep-Kombinationen

SOL 2024 2000
  -> breites Mehrrollenfeld
  -> drei lange tragende Rollen + zwei kurze Strain-Kontakte
  -> zehn Sleep-Kombinationen
```

## Bedeutung

Die Gegenprobe verschiebt die Frage:

Nicht jedes andere Asset liefert automatisch eine Zwischenklasse. DOGE und XRP bleiben in den geprüften Startfenstern trotz anderer Weltfärbung feldgebunden. Damit wird BTC als Übergangsfeld interessanter, weil BTC nicht nur ein beliebiges Nicht-SOL-Verhalten zeigt, sondern eine spezifische Zwischenform zwischen Einzelrekopplung und breitem Mehrrollenfeld.

## Grenze

Der Befund gilt nur für die geprüften 1000er-Startfenster. Andere DOGE/XRP-Fenster können anders ausfallen. Um das zu klären, braucht es eine Fenstersuche innerhalb der längeren 10k-Welten.

## Wie es weitergeht

Als nächstes sollte eine passive Fenstersuche über DOGE/XRP/BTC 10k laufen. Ziel: nicht ein Asset bewerten, sondern Fenster finden, in denen Einzelrekopplung in Übergang kippt.
