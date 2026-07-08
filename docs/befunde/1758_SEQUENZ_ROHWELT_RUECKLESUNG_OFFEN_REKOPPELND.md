# Sequenz-Rohwelt-Rücklesung: verteilt offen vs. verteilt rekoppelnd

Stand: 2026-07-08

## Grundfrage

Nach der Vier-Asset-Sequenzmatrix war die nächste Frage:

```text
Was unterscheidet `verteilt_offen` von `verteilt_rekoppelnd` konkret?
```

Es ging nicht um eine neue Welt, sondern um Rücklesung:

```text
Welche Rohweltmerkmale, Rekopplung, Rollenbreite und Nachhall begleiten die Achsenklassen?
```

## Unterprüfung

Ausgewertet wurden die lokalen Real-Sleep-Real-Sequenzen von:

```text
XRP 2025 5m
DOGE 2025 5m
BTC 2025 5m
PAXG 2025 5m
```

Werkzeug:

```text
tools/report_sequence_rawworld_contrast.py
```

Reports:

```text
reports/vier_asset_sequence_rawworld_contrast.md
reports/vier_asset_sequence_rawworld_contrast.csv
reports/vier_asset_sequence_rawworld_contrast_groups.csv
```

## Klassenmittel

| Klasse | n | Rollen | Kombis | Rekopplung | Adaptiv | Nachhall | Basis-Energie | Folge-Energie | Delta Energie | Basis Range | Folge Range |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| kompakt_nachhallend | 1 | 1.00 | 0.00 | 0.6897 | 0.7319 | 0.3191 | 3.8650 | 4.1122 | 0.2472 | 0.003885 | 0.003708 |
| mittlere_uebergangsphase | 5 | 4.00 | 6.00 | 0.6903 | 0.7298 | 0.3023 | 3.6197 | 5.6034 | 1.9838 | 0.003386 | 0.005020 |
| verteilt_offen | 7 | 5.86 | 14.00 | 0.6907 | 0.7273 | 0.3086 | 4.0028 | 3.0147 | -0.9882 | 0.003597 | 0.002744 |
| verteilt_rekoppelnd | 3 | 8.00 | 20.00 | 0.7042 | 0.7362 | 0.3753 | 0.9887 | 1.4035 | 0.4147 | 0.000783 | 0.001135 |

## Befund

`verteilt_offen` und `verteilt_rekoppelnd` sind beide breit, aber nicht gleich.

`verteilt_offen` zeigt hier:

- hohe Rollenbreite,
- viele Kombinationen,
- relativ normale Rekopplung,
- niedrigeren Nachhall als `verteilt_rekoppelnd`,
- höhere Basis-Weltenergie,
- fallende Folgeenergie.

Lesung:

```text
Breite Rollenöffnung nach stärkerem Weltreiz,
aber noch nicht stark rückgebunden.
```

`verteilt_rekoppelnd` zeigt hier:

- höchste Rollen- und Kombinationsbreite,
- deutlich höhere Rekopplung,
- deutlich höheren Nachhall,
- niedrigere Rohweltenergie,
- geringere Range,
- leichte Energiezunahme statt starker Entladung.

Lesung:

```text
Breite Rollenbildung, die vom Feld besser gehalten und rückgebunden wird.
```

## Deutung

Der Unterschied liegt nicht nur in der Anzahl der Rollen.

```text
verteilt_offen       = breite Öffnung bei stärkerer Weltenergie und schwächerer Rückbindung
verteilt_rekoppelnd  = breite Rollenbildung bei ruhigerer Rohwelt und stärkerer Feldbindung
```

Damit wird eine wichtige mechanische Trennung sichtbar:

```text
Rollenbreite ist nicht automatisch Drift.
Rollenbreite kann offen sein.
Rollenbreite kann rekoppelnd getragen sein.
```

Das passt zur bisherigen Topologie-Lesung: Die Topologie bleibt als Rollenraum stabil, aber die lokale Feldphase entscheidet, ob Breite offen driftet oder getragen rekoppelt.

## Grenze

Die Rohwelt-Energie ist eine passive Lesegroesse aus OHLCV. Sie ist keine Regel, kein Gate und keine Handlungslogik.

Die Befunde sind außerdem klassenmittelwertbasiert. Einzelwelten können davon abweichen.

## Folgeschritt

Als nächstes sollte geprüft werden, ob diese Trennung auch in anderen Jahren oder synthetischen Welten sichtbar bleibt:

```text
verteilt_offen      gegen verteilt_rekoppelnd
hohe Weltenergie    gegen ruhige rekoppelnde Weltlage
Nachhall niedrig    gegen Nachhall hoch
```
