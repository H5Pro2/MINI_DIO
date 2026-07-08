# 1787 - Synthetische Rekopplungs-Provokation

## Grundfrage

Nach 1786 war offen, ob rekoppelnde Breite künstlich erzeugt werden kann, wenn eine synthetische Welt gezielt Breite und Nachhall anbietet.

Die Prüfung sollte klären:

```text
Kann man `verteilt_rekoppelnd` durch synthetische Breite plus Nachhall provozieren?
Oder bleibt das Feld trotz starker Rückbindung kompakt?
```

## Prüfung

Gebaut wurden zwei synthetische Weltformen:

1. `synthetic_1787_breadth_afterimage_*`
   - mehrere weiche Inseln
   - starke Nachhallhülle
   - Follow-Welt mit Anschlussnähe
   - Shuffle-Kontrolle mit fragmentierter Reihenfolge

2. `synthetic_1788_role_mosaic_afterimage_*`
   - ruhiger Aufbau
   - Expansion
   - breiter Spannungsraum
   - Kompression
   - Bruch/Gegenlauf
   - Rekopplungsversuch

Beide wurden passiv über den Mehrwelt-Achsenreport geprüft.

## Ergebnis

| Welt | Verbindung | Rollen | Kombinationen | Rekopplung | Nachhall | Klasse |
|---|---|---:|---:|---:|---:|---|
| 1787 | Base -> Follow | 2 | 1 | 0.7516 | 0.8079 | `kompakt_nachhallend` |
| 1787 | Base -> Shuffle | 2 | 1 | 0.7516 | 0.8079 | `kompakt_nachhallend` |
| 1788 | Base -> Follow | 2 | 1 | 0.7511 | 0.8003 | `kompakt_nachhallend` |
| 1788 | Base -> Shuffle | 2 | 1 | 0.7511 | 0.8003 | `kompakt_nachhallend` |

Auch mit offeneren Reportparametern blieb 1787 kompakt.

## Interpretation

Der Befund ist negativ, aber fachlich wichtig:

```text
starker Nachhall
+ hohe Rekopplung
+ synthetisch kontrollierte Wiederkehr
!= verteilte Rekopplung
```

Die synthetischen Welten erzeugen eine sehr starke kompakte Nachhallbindung, aber keine verteilte rekoppelnde Rollenbreite. Damit wird 1786 gestützt: `verteilt_rekoppelnd` ist nicht einfach durch Nachhall oder künstlich geordnete Wiederholung provozierbar.

Die Folge ist methodisch wichtig:

- hohe Rekopplung kann kompakt sein
- hoher Nachhall kann kompakt sein
- synthetische Wiederkehr kann kompakt sein
- verteilte Rekopplung braucht offenbar mehr als künstliche Musterbreite

## Bedeutung für MINI_DIO

MINI_DIO unterscheidet hier zwischen:

```text
kompakt nachhallender Bindung
  -> stark, stabil, aber eng

verteilt rekoppelnder Bindung
  -> breiter Rollenraum mit tragender Rückführung
```

Das ist eine wichtige Trennung. Sie verhindert, dass jede hohe Rekopplung automatisch als `verteilt_rekoppelnd` gelesen wird.

## Grenze

Das ist kein Beweis, dass synthetische Rekopplung unmöglich ist. Es zeigt nur: Die hier gebauten synthetischen Welten erzeugen keine verteilte Rekopplung, obwohl sie Nachhall, Rückbindung und kontrollierte Wiederkehr stark anbieten.

## Artefakte

- `tools/build_synthetic_breadth_afterimage_worlds.py`
- `tools/build_synthetic_role_mosaic_afterimage_worlds.py`
- `data/synthetic_1787_breadth_afterimage_base_3000_5m.csv`
- `data/synthetic_1787_breadth_afterimage_follow_3000_5m.csv`
- `data/synthetic_1787_breadth_afterimage_shuffle_3000_5m.csv`
- `data/synthetic_1788_role_mosaic_afterimage_base_3600_5m.csv`
- `data/synthetic_1788_role_mosaic_afterimage_follow_3600_5m.csv`
- `data/synthetic_1788_role_mosaic_afterimage_shuffle_3600_5m.csv`
- `reports/synthetic_1787_breadth_afterimage_axis_probe.md`
- `reports/synthetic_1787_breadth_afterimage_axis_probe_wideparam.md`
- `reports/synthetic_1788_role_mosaic_afterimage_axis_probe.md`

## Wie es weitergeht

Als nächstes sollte nicht weiter blind synthetisch verstärkt werden. Sinnvoller ist eine Rücklesung realer `verteilt_rekoppelnd`-Fenster: Welche Weltmerkmale haben PAXG und BTC gemeinsam, die den synthetischen Welten fehlen?
