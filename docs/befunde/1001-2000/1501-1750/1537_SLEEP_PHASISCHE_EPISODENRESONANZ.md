# 1537 - Phasische Episodenresonanz Im Sleep Environment

## Zweck

Diese Pruefung erweitert `1535` und `1536`.

Die Frage lautet:

```text
Kann das Sleep-Environment alte Episodenrollen phasisch unterschiedlich aktivieren,
ohne daraus eine feste Sequenz zu machen?
```

## Mechanische Aenderung

`mini_dio/sleep_field_environment.py` wurde erweitert:

- Episodenrollen besitzen jetzt eine rollenspezifische, deterministische Resonanzphase.
- Aktivierung erfolgt ueber Feldnaehe, Rollenqualitaet und relativen Aktivierungsboden.
- Es wird keine Reihenfolge vorgegeben.
- Es wird keine neue Aussenwelt eingespeist.
- Es wird keine Handlung erzeugt.

Damit entsteht:

```text
Rollenmilieu
  -> phasische Aktivierung
  -> wechselnde Rollensets
  -> weiterhin passives Innenfeld
```

## Gepruefte Laeufe

| Lauf | Quelle | aktive Rollensets | Durchschnitt aktive Rollen | Sleep-Symbol |
| --- | --- | ---: | ---: | --- |
| SOL 2024 Sleep Phase | SOL 2024 5m | 4 | 2.790625 | `dio_019bn1b` |
| Stress 2023 Sleep Phase | Stress 2023 5m | 25 | 3.559375 | `dio_019bn1b` |

## Follow-up

| Lauf | Sleep-Symbol real wiedergefunden | alte Rollen wiedergefunden | Rollenqualitaet |
| --- | ---: | ---: | --- |
| SOL 2024 Sleep Phase | 0 | 2 von 3 Folgepruefungen | `rekopplung_tragend` |
| Stress 2023 Sleep Phase | 0 | 1 von 3 Folgepruefungen | `rekopplung_tragend` |

## Befund

Das Sleep-Symbol bleibt:

```text
dio_019bn1b
```

Es taucht weiterhin nicht als normales reales Weltsymbol in den geprueften Memories auf.

Neu ist aber:

```text
Die darunterliegenden Episodenrollen sind nicht mehr glatt dauerhaft gleich aktiv.
Sie bilden phasische Rollensets.
```

Besonders Stress 2023 zeigt mit 25 aktiven Rollensets deutlich mehr innere Differenzierung als SOL 2024 mit 4 Rollensets.

## Einordnung

Der aktuelle Befund spricht fuer:

```text
keine neue Offline-Semantik
aber phasische Verarbeitung alter Episodenrollen
und Festigung rekopplungstragender Muster
```

Das ist fachlich die richtige Zwischenstufe:

```text
nicht: Schlaf erzeugt neue Weltbedeutung
sondern: Schlafmilieu kann alte Feldrollen differenziert wieder beruehren
```

## Grenze

Noch nicht gezeigt:

- neue Offline-Symbolbindung,
- spaeteres Wiederauftauchen eines neuen Sleep-Symbols in realer Lage,
- eigenstaendige semantische Insel aus reiner Offline-Verarbeitung.

Gezeigt ist:

- stabile Offline-Aktivitaet,
- phasische Rollenaktivierung,
- rekopplungstragende Wiederberuehrung alter Rollen.

## Naechste Frage

Die naechste Pruefung sollte nicht noch mehr Aktivitaet erzwingen.

Sinnvoller ist:

```text
Wie unterscheiden sich Rollen, die im Schlaf oft aktiv werden,
von Rollen, die im realen Kontakt stark tragen?
```

Damit kann geprueft werden, ob MCM-Schlafregulation eher:

- alte Muster festigt,
- offene Muster entlastet,
- Randspannung beruhigt,
- oder seltene Rollen in neue Naehe bringt.

