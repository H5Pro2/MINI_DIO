# MCM-Feldepisoden Rollen-Split

Stand: 2026-07-06

## Zweck

Die vorherige Diagnose zeigte eine methodische Engstelle:

```text
Die Rezeptoraufnahme sah lokale Unterschiede,
aber die MCM-Feldepisoden verdichteten zu grob auf field_carried.
```

Dadurch wurden Kippnähe, tragende Unruhe und stabile Phasen zwar lokal sichtbar,
aber für Sleep/Offline nicht als getrennte passive Rollen verfügbar.

Diese Prüfung trennt deshalb die passive Feldepisodenrolle feiner:

```text
field_stabil
field_tragend_unruhig
field_kippend
```

Wichtig: Das ist keine Handlung, kein Gate und keine Strategie.
Es ist nur eine feinere passive Lesung der bereits vorhandenen MCM-Feldwirkung.

## Technische Änderung

Die Episodenverdichtung verwendet nicht mehr nur den groben Zustand `field_carried`.
Stattdessen wird die passive MCM-Effektklasse als `field_episode_role` gespeichert.

Zusätzlich bleibt der alte Grundzustand als Referenz erhalten:

```text
base_field_effect_state
passive_mcm_effect_class
field_episode_role
```

Damit kann später unterschieden werden:

```text
Grundzustand: carried
lokale Feldrolle: stabil / tragend_unruhig / kippend
```

## Direkter Test

Testwelt:

```text
scan_synth-rand-kipp-start0_start250_size1700.csv
Sinnesmodus: calibrated_relative
```

Ergebnis der passiven Episodenrollen:

```text
field_stabil: 1269
field_tragend_unruhig: 380
field_kippend: 45
```

Damit ist der frühere Kollaps auf eine einzige Offline-Grundrolle technisch aufgelöst.
Die Welt wird nicht mehr nur als eine tragende Gesamtfläche gelesen,
sondern als stabile, unruhig tragende und kippnahe Feldepisode.

## Real-Sleep-Real 1650

Test:

```text
scan_synth-rand-kipp-start0_start250_size1650.csv
Sinnesmodus: calibrated_relative
```

Real-A-Effektklassen:

```text
kippend: 42
stabil: 1257
tragend_unruhig: 345
```

Sleep/Offline:

```text
reaktivierte Rollen: 9 / 9
voll reaktivierte Kombinationen: 27 / 27
teilweise reaktivierte Kombinationen: 0 / 27
Follow-up: sleep_roles_fully_reactivated
```

## Real-Sleep-Real 1700

Test:

```text
scan_synth-rand-kipp-start0_start250_size1700.csv
Sinnesmodus: calibrated_relative
```

Real-A-Effektklassen:

```text
kippend: 45
stabil: 1269
tragend_unruhig: 380
```

Sleep/Offline:

```text
reaktivierte Rollen: 8 / 8
voll reaktivierte Kombinationen: 22 / 22
teilweise reaktivierte Kombinationen: 0 / 22
Follow-up: sleep_roles_fully_reactivated
```

## Befund

Die Rollen-Split-Prüfung zeigt:

- `field_carried` war zu breit.
- Lokale MCM-Wirkungen waren bereits vorhanden, wurden aber zu grob verdichtet.
- Mit `field_episode_role` werden stabile, tragend-unruhige und kippnahe Phasen passiv getrennt lesbar.
- Sleep/Offline kann diese getrennten Rollen und deren Kombinationen vollständig wieder berühren.
- Die Top-Syntax und Top-Familien bleiben dabei stabil; es entsteht keine neue Weltbedeutung durch Sleep.

## Einordnung

Das spricht für eine feinere MCM-Feldepisoden-Sprache.

Nicht:

```text
Das Feld entscheidet anders.
```

Sondern:

```text
Das Feld trägt schon unterschiedliche lokale Wirkungen.
Die Diagnostik liest diese Wirkungen nun feiner.
```

Damit wird MINI_DIO nicht mechanischer, sondern passiver genauer:
Die innere Feldepisode bekommt mehr semantische Auflösung, ohne in Handlung übersetzt zu werden.

## Nächster Prüfpunkt

Als nächstes sollte die Rollen-Split-Lesung gegen `world_relative` und weitere Welten geprüft werden.
Entscheidend ist, ob `field_stabil`, `field_tragend_unruhig` und `field_kippend` auch außerhalb dieser synthetischen Schwellenwelt wieder sinnvoll auseinanderfallen.
