# 006 - Adaptive passive Rekopplung

## Begriff

Adaptive passive Rekopplung bezeichnet eine zweite, erfahrungsgewichtete Lesung der MCM-Rueckfuehrung.

Die bisherige `mcm_rekopplung_quality` bleibt als stabile Referenz erhalten. Daneben wird `mcm_adaptive_rekopplung_quality` geschrieben.

## Warum zwei Werte

Die statische Rekopplung beantwortet:

```text
Wie rekoppelt diese Lage nach der Grundformel?
```

Die adaptive Rekopplung beantwortet:

```text
Wie rekoppelt diese Lage, wenn fruehere passive Episoden mitsprechen?
```

Damit wird die Rueckfuehrung nicht mehr nur durch feste Gewichte gelesen. Wiederkehrende Erfahrung kann verschieben, ob Tragen, Alignment, Strain-Entlastung oder Sinneskopplung staerker in die aktuelle Feldlesung eingehen.

## Funktion

Die adaptive Rekopplung ist passiv.

Sie ist:

- keine Handlung,
- kein Gate,
- keine Richtungsvorgabe,
- keine Strategie,
- kein Ersatz fuer die statische Referenz.

Sie dient nur dazu, erfahrungsnahe Feldrueckfuehrung sichtbar zu machen.

## Mechanik

Pro Lage werden vier Anteile gelesen:

- `mcm_carry_quality`: tragende Feldnaehe,
- `reflection_alignment`: innere Ausrichtung,
- `1 - mcm_strain_quality`: Entlastung von Feldspannung,
- `sensory_coupling`: Sinnes-MCM-Kopplung.

Ohne Erfahrung nutzt MINI_DIO die statische Gewichtung:

```text
carry 0.42
alignment 0.24
strain_relief 0.20
sensory 0.14
```

Mit Erfahrung werden Episoden aus `episode_memory` gelesen. Wenn eine passende Symbolfamilie vorhanden ist, wird zuerst diese Familie genutzt. Sonst wird die gesamte Episodenerfahrung verwendet.

Aus dieser Erfahrung entstehen dynamische Gewichte:

```text
carry_weight
alignment_weight
strain_relief_weight
sensory_weight
```

Diese Gewichte werden normalisiert und als Debugfelder ausgegeben.

## Zustandslesung

Die adaptive Schicht schreibt:

- `adaptive_untrained`: keine passende Erfahrung vorhanden,
- `adaptive_jung`: Erfahrung vorhanden, aber noch jung,
- `adaptive_rekopplung_angehoben`: adaptive Lesung liegt klar ueber der statischen Referenz,
- `adaptive_rekopplung_gedaempft`: adaptive Lesung liegt klar unter der statischen Referenz,
- `adaptive_rekopplung_nahe_statisch`: adaptive und statische Lesung liegen nahe beieinander.

## Erster Smoke-Befund

Ein erster Smoke-Lauf mit BTC 2024 5m, 1000 Zeilen und frischer Memory zeigte:

```text
avg_mcm_rekopplung_quality          0.683874
avg_mcm_adaptive_rekopplung_quality 0.728393
max_mcm_adaptive_rekopplung_quality 0.793495
avg_mcm_adaptive_rekopplung_experience 0.613291
```

Die adaptive Schicht wurde im Lauf sichtbar:

```text
adaptive_untrained 5
adaptive_jung 300
adaptive_rekopplung_angehoben 689
```

Das ist noch kein abschliessender Befund. Es zeigt aber, dass die adaptive Rekopplung technisch greift und nicht nur als leerer Platzhalter geschrieben wird.

## Forschungsgrenze

Aus dieser Mechanik folgt noch nicht:

```text
Das Feld entscheidet besser.
Das Feld handelt.
Das Feld beweist adaptive Intelligenz.
```

Sauberer ist:

```text
MINI_DIO kann passive Rueckfuehrung erfahrungsgewichtet sichtbar machen.
```

## Wie es weitergeht

Als naechstes wird geprueft, ob adaptive Rekopplung ueber mehrere Welten stabil, weltabhaengig oder driftend wirkt. Entscheidend ist, ob sie nur allgemein anhebt oder ob sie je nach Symbolfamilie und Weltmilieu unterschiedlich gewichtet.
