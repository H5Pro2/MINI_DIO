# Rollen-Split: calibrated_relative gegen world_relative

Stand: 2026-07-06

## Zweck

Nach dem MCM-Feldepisoden-Rollen-Split wurde geprüft, ob die feinere passive Rollenlesung nur im Modus `calibrated_relative` funktioniert oder auch im bisherigen Milieu-Modus `world_relative`.

Die Frage:

```text
Bleibt die Feldepisoden-Aufteilung stabil,
wenn die Rezeptoraufnahme wieder weltrelativ gelesen wird?
```

## Vergleich

### calibrated_relative

1650:

```text
Effektklassen:
kippend: 42
stabil: 1257
tragend_unruhig: 345

Sleep-Rollen: 9 / 9 reaktiviert
Sleep-Kombinationen: 27 / 27 voll reaktiviert
```

1700:

```text
Effektklassen:
kippend: 45
stabil: 1269
tragend_unruhig: 380

Sleep-Rollen: 8 / 8 reaktiviert
Sleep-Kombinationen: 22 / 22 voll reaktiviert
```

### world_relative

1650:

```text
Effektklassen:
gespannt: 2
stabil: 1377
tragend_unruhig: 265

Sleep-Rollen: 4 / 4 reaktiviert
Sleep-Kombinationen: 6 / 6 voll reaktiviert
```

1700:

```text
Effektklassen:
gespannt: 2
stabil: 1401
tragend_unruhig: 291

Sleep-Rollen: 4 / 4 reaktiviert
Sleep-Kombinationen: 6 / 6 voll reaktiviert
```

## Befund

Die feinere Rollenlesung bleibt auch unter `world_relative` erhalten.
Sie fällt dort aber schmaler aus:

- `calibrated_relative` liest mehr lokale Kippnähe.
- `world_relative` liest dieselbe Welt stärker zentrumsnah.
- `world_relative` reduziert die Kippnähe auf sehr dünne `gespannt`-Kontakte.
- Beide Modi reaktivieren ihre berührten Sleep-Rollen und Kombinationen vollständig.

Damit ist der Rollen-Split nicht an einen einzelnen Sinnesmodus gebunden.
Der Sinnesmodus färbt aber, welche Feldqualität sichtbar wird.

## Einordnung

Das stützt die aktuelle Lesung:

```text
Die MCM-Feldwirkung besitzt lokale Rollenunterschiede.
Die Rezeptoraufnahme entscheidet mit, wie scharf diese Unterschiede sichtbar werden.
```

`calibrated_relative` ist aktuell besser für lokale Kipp-/Übergangszonen.
`world_relative` ist aktuell besser für robuste Milieu- und Zentrumlesung.

Beide sind methodisch wertvoll, aber sie beantworten unterschiedliche Fragen.

## Grenze

Das ist weiterhin passive Diagnostik.

Nicht gezeigt ist:

```text
MINI_DIO handelt anders.
```

Gezeigt ist:

```text
MINI_DIOs MCM-Feldepisoden lassen sich feiner und reproduzierbar lesen.
```

## Nächster Prüfpunkt

Als nächstes sollte diese Rollen-Split-Lesung gegen reale Welten geprüft werden.
Wichtig ist, ob `field_stabil`, `field_tragend_unruhig`, `field_gespannt` oder `field_kippend` auch bei nicht synthetischen Weltfenstern sinnvoll und reproduzierbar erscheinen.
