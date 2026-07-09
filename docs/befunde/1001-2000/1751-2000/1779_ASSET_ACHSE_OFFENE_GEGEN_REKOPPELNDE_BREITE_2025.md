# 1779 - Asset-Achse: offene gegen rekoppelnde Breite 2025

## Grundfrage

Die vorherigen PAXG-Prüfungen zeigten, dass Rollenbreite nicht automatisch rekoppelnde Breite ist. Die offene Frage war, ob BTC, DOGE oder XRP dieselbe rekoppelnde Qualität zeigen oder ob PAXG in der lokalen Vier-Asset-Sequenz einen besonderen rekoppelnden Pol bildet.

## Prüfung

Ausgewertet wurde die vorhandene Vier-Asset-Sequenzmatrix 2025:

- XRP 2025, vier lokale Anschlussfenster
- DOGE 2025, vier lokale Anschlussfenster
- BTC 2025, vier lokale Anschlussfenster
- PAXG 2025, vier lokale Anschlussfenster

Die Daten wurden nach Asset und Achsenklasse gruppiert. Entscheidend waren Rollenanzahl, Kombinationen, Rekopplung, Nachhall und Richtungswechsel der Folgewelt.

## Ergebnis

PAXG ist in dieser Sequenz der einzige Assetbereich mit `verteilt_rekoppelnd`.

Aggregiert zeigt sich:

| Klasse | Anzahl | Rollen | Kombinationen | Rekopplung | Nachhall | Folge-Richtungswechsel |
|---|---:|---:|---:|---:|---:|---:|
| `verteilt_offen` | 7 | 5.8571 | 14.0000 | 0.690667 | 0.3086 | 0.5087 |
| `verteilt_rekoppelnd` | 3 | 8.0000 | 20.0000 | 0.704207 | 0.3753 | 0.3046 |

BTC und XRP bilden breite Rollenräume, bleiben aber überwiegend `verteilt_offen`. DOGE zeigt Rollenatmung zwischen Übergang, Kompaktheit, Offenheit und erneutem Übergang. PAXG zeigt dagegen mehrfach `verteilt_rekoppelnd`.

## Interpretation

Der Befund trennt offene Breite von rekoppelnder Breite weiter:

- Offene Breite bedeutet: viele Rollen oder Kombinationen entstehen, aber sie bleiben stärker drift- oder richtungswechselnah.
- Rekoppelnde Breite bedeutet: viele Rollen und Kombinationen entstehen, aber das Feld hält sie stärker zusammen.
- PAXG 2025 wirkt in dieser lokalen Matrix als rekoppelnder Pol innerhalb derselben Grundtopologie.

Damit bestätigt sich die Arbeitsform:

```text
Rollenbreite allein
  -> verteilt_offen

Rollenbreite + Nachhall + Rekopplung + ruhigere Anschlussrichtung
  -> verteilt_rekoppelnd
```

## Grenze

Das ist eine passive Diagnose, keine Asset-Regel und keine Handlungsanweisung. Der Befund gilt für die geprüfte lokale 2025-Sequenz. Ob BTC, DOGE oder XRP in anderen Zeitfenstern ebenfalls `verteilt_rekoppelnd` werden können, muss separat geprüft werden.

## Artefakte

- `reports/asset_achsenvergleich_offen_vs_rekoppelnd_2025.csv`
- `reports/asset_achsenvergleich_offen_vs_rekoppelnd_2025.md`
- Grundlage: `reports/vier_asset_sequence_rawworld_contrast.csv`
