# Befund 2000 - Frische Weltbindung: Realwelt gegen Nullwelt

Stand: 2026-07-09

## Frage

Nach der Einführung der passiven Weltbindungsqualität wurde geprüft:

```text
Kann MINI_DIO Feldfunktionen bilden,
aber zugleich ihre Herkunft sauber unterscheiden?
```

Dafür wurden zwei frische Memories verwendet.

## Läufe

Realwelt:

```text
data/kontrolliert_btc_2024_5m_10k_BTCUSDT.csv
memory/1999_world_binding_fresh_real_probe.json
debug/1999_world_binding_fresh_real_btc
```

Nullwelt:

```text
data/synthetic_1835_btc2024_null_5m_shuffle_order_10000.csv
memory/1999_world_binding_fresh_null_probe.json
debug/1999_world_binding_fresh_null_btc
```

## Ergebnis

| Probe | gelesene Anker | Weltbindungsqualität |
|---|---:|---|
| frische Realwelt | 79 | `realworld_bound`: 79 |
| frische Nullwelt | 76 | `field_internal_null_order`: 76 |

Feldfunktionsklassen Realwelt:

```text
open_surface: 24
milieu_island: 43
active_recoupling: 12
```

Feldfunktionsklassen Nullwelt:

```text
open_surface: 24
milieu_island: 40
active_recoupling: 12
```

## Lesung

Die Feldfunktionsklassen entstehen in beiden Prüfungen ähnlich.
Das bestätigt den vorherigen Befund:

```text
Das MCM-Feld kann interne Rollenordnung auch ohne echte Weltbindung bilden.
```

Der neue Punkt ist die Trennung:

```text
Realweltrollen werden als realworld_bound gelesen.
Nullweltrollen werden als field_internal_null_order gelesen.
```

Damit kann MINI_DIO jetzt unterscheiden:

- eine Rolle ist feldintern geordnet,
- eine Rolle ist realweltlich gebunden.

Das ist genau die fehlende Zusatzschicht zur Feldfunktions-Memory.

## Bedeutung

Die MCM-Feldfunktion allein ist nicht genug.
Sie zeigt, dass ein Muster im Feld eine Rolle bildet.

Die Weltbindungsqualität zeigt zusätzlich:

```text
Woher wird diese Rolle getragen?
```

Damit wird die Forschung sauberer, weil eine starke innere Ordnung nicht automatisch als Realwelt-Bedeutung interpretiert wird.

## Nächster Schritt

Als nächstes sollte die Weltbindungsqualität in Mehrwelt-Memories weiter geprüft werden:

- bleibt `realworld_bound` bei realen Folgewelten stabil,
- kippt `field_internal_null_order` bei realem Weltkontakt,
- entstehen Zwischenformen als `mixed_binding`,
- und welche Rollen sind nur feldintern stark, aber nicht realweltlich getragen.
