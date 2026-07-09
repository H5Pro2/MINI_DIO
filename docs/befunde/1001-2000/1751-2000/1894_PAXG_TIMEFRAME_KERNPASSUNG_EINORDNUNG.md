# 1894 - PAXG-Timeframe: Einordnung der Kernpassung

## Grundfrage

Ist `kern_verschoben` eine allgemeine PAXG-Eigenschaft oder eine 5m-spezifische Übergangslage?

## Prüfung

Zusätzlich zu den PAXG-5m-Folgefenstern wurden vier PAXG-1h-Fenster geprüft:

- PAXG 2025 1h `4000_5000`
- PAXG 2025 1h `5000_6000`
- PAXG 2024 1h `4000_5000`
- PAXG 2024 1h `5000_6000`

Alle Fenster wurden gegen den harten lokalen Reifekern gelesen.

## Ergebnis

```text
p24_1h_4000_5000 -> kern_ausgeblendet
p24_1h_5000_6000 -> kern_ausgeblendet
p25_1h_4000_5000 -> kern_ausgeblendet
p25_1h_5000_6000 -> kern_ausgeblendet
```

Die passive Weltpassungs-Memory enthält nach der Aktualisierung:

```text
kern_getragen: 13
kern_ausgeblendet: 9
kern_verschoben: 1
```

## Lesung

`kern_verschoben` bleibt bislang eine seltene Zwischenqualität.
Im PAXG-1h-Timeframe wird der bisherige lokale Kern überwiegend ausgeblendet.

Damit ist die 5m-Verschiebung nicht einfach PAXG-typisch.
Sie wirkt eher wie eine spezifische Übergangslage eines bestimmten Weltfensters.

## Bedeutung

PAXG trennt die Weltpassung schärfer als erwartet:

- 5m kann den Kern tragen, verschieben oder ausblenden.
- 1h blendet den bisherigen Kern in den geprüften Fenstern deutlich stärker aus.

Das spricht dafür, dass Weltpassung nicht nur assetabhängig ist.
Sie ist auch timeframe- und fensterabhängig.

## Mechanischer Befund

Die Memory wird dadurch nicht härter.
Sie wird genauer:

```text
Innenkern + Asset + Timeframe + Fensterlage -> Passungsqualität
```

Diese Qualität bleibt passiv.
Sie ist keine Handlung, kein Gate und keine Richtung.
