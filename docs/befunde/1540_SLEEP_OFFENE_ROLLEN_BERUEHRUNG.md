# 1540 - Sleep Offene Rollen Beruehrung

## Zweck

Diese Pruefung erweitert `1539`.

Die Frage lautet:

```text
Kann das Sleep-Milieu offene/ungeklaerte Rollen beruehren,
ohne sie kuenstlich zu erzwingen?
```

## Technischer Hinweis

Der Sleep-Reporter wurde korrigiert:

```text
active_roles schreibt jetzt alle aktiven Rollen in die CSV,
nicht nur die ersten 5.
```

Das war wichtig, weil die Selektionspruefung sonst bei mehr als 5 aktiven Rollen offene Rollen uebersehen konnte.

## Vorgehen

Es wurde keine neue Aussenwelt eingespeist.

Geaendert wurden nur Sleep-Bedingungen der Diagnose:

- `activation_floor`
- `max_active_roles`

Damit wird nicht festgelegt, welche Rolle aktiv werden soll. Es wird nur die Naehe breiter gelesen.

## Ergebnisse

| Quelle | Aktivierungsbedingung | Sleep-aktive Rollen | offene Rollen aktiv | Befund |
| --- | --- | ---: | ---: | --- |
| SOL 2024 5m | `activation_floor=0.45`, `max_active_roles=5` | 5 von 5 | 2 von 2 | offene Rollen beruehrt |
| Stress 2023 5m | `activation_floor=0.65`, `max_active_roles=7` | 7 von 7 | 1 von 1 | offene Rolle beruehrt |

## SOL 2024

Bei weicherer Aktivierungsnaehe wurden alle Rollen beruehrt:

- 3 x `rekopplung_tragend`
- 2 x `offen_ungeklart`

Die offenen Rollen waren:

- `dio_mcm_episode_0eghs1d`
- `dio_mcm_episode_0qrlave`

## Stress 2023

Bei moderat weicher Aktivierungsnaehe wurden ebenfalls alle Rollen beruehrt:

- 6 x `rekopplung_tragend`
- 1 x `offen_ungeklart`

Die offene Rolle war:

- `dio_mcm_episode_0sjrih9`

## Befund

Offene/ungeklaerte Rollen sind nicht prinzipiell vom Sleep-Milieu ausgeschlossen.

Sie werden aber nicht in der strengeren Standardbedingung aktiv.

Das bedeutet:

```text
strenge Schlafnaehe
  -> bevorzugt rekopplungstragende Rollen

weichere Schlafnaehe
  -> kann offene Rollen mitberuehren
```

## Einordnung

Das ist keine neue Offline-Semantik.

Es zeigt aber:

```text
MCM-Schlafregulation besitzt einen diagnostischen Naehebereich.
Je nachdem wie eng oder weich dieser Bereich gelesen wird,
werden nur tragende Rollen oder auch offene Rollen beruehrt.
```

Damit wird die naechste Forschungsfrage greifbarer:

```text
Fuehrt das Beruehren offener Rollen spaeter zu Musterfestigung,
zu neuer Bindung,
oder bleibt es nur kurzfristige Offline-Aktivitaet?
```

