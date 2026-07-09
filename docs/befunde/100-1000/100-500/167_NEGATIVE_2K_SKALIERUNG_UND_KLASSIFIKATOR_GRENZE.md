# Negative 2k-Skalierung Und Klassifikator-Grenze

Stand: 2026-06-18

## Zweck

Diese Datei dokumentiert die 2k-Skalierung der moderat negativen Welt.

Geprueft wurde:

```text
data\kontrolliert_2023_moderate_negative_test1_1000_5m_SOLUSDT.csv
data\kontrolliert_2023_moderate_negative_test1_2000_5m_SOLUSDT.csv
```

Die Grundfrage war:

```text
Bleibt negative Bewegung bei laengerer Weltzeit getragen,
oder kippt sie in einen Stress-Gegenpol?
```

## Ergebnis

Die Rohwerte zeigen weiterhin eine getragene Feldlage.

Der automatische Feldklassenreport ordnet `negative_moderate_2k` aber als:

```text
Stress-Gegenpol
```

ein.

Das ist ein methodisch wichtiger Punkt:

```text
Die automatische Klassifikation ist hier zu grob.
```

## Messwerte

| Welt | Kerzen | Reportklasse | Rekopplung | Tragqualitaet | Strain/Kippung | Memory | Dominante Wirkung |
|---|---:|---|---:|---:|---:|---:|---|
| negative_moderate_1k | 1000 | ruhige Naehegruppe | 0.631065 | 0.362044 | 65 | 45 | stabil |
| negative_moderate_2k | 2000 | Stress-Gegenpol | 0.629660 | 0.360479 | 142 | 105 | stabil |

## Interpretation

Die 2k-Welt ist nicht kollabiert.

Sie zeigt:

```text
field_carried: 1927
field_strained: 67
stabil: 1067
tragend_unruhig: 766
```

Damit ist sie im Innenfeld deutlich getragen.

Die Reportklasse `Stress-Gegenpol` entsteht, weil die bisherige Diagnose starke Memory- und Spannungszunahme hart als Gegenpol wertet.

Das ist fuer die Forschung nuetzlich:

```text
Mehr Memory ist nicht automatisch Stress.
Mehr Memory kann auch laengere Weltzeit und Bedeutungsverdichtung anzeigen.
```

## Methodischer Befund

Der Klassifikator muss kuenftig trennen zwischen:

```text
belastendem Memorydruck
und
tragender Bedeutungsverdichtung
```

Bei `negative_moderate_2k` sieht es eher nach tragender Verdichtung aus:

```text
Rekopplung bleibt hoch.
Tragqualitaet bleibt hoch.
Stabil bleibt dominant.
Field-carried bleibt sehr stark.
```

Das spricht gegen einen echten Stress-Gegenpol.

## Forschungswert

Dieser Lauf zeigt eine Grenze der aktuellen Auswertung.

MINI_DIO selbst wirkt nicht zwingend falsch.

Die Leseschicht muss feiner werden:

```text
Nicht jede Zunahme von Memory ist Stress.
Nicht jede Zunahme von Kippnaehe ist Kollaps.
Die Relation aus Stabilitaet, Rekopplung, Tragqualitaet und Memory entscheidet.
```

## Wie Es Weitergeht

Als naechstes sollte der Feldklassenreport verfeinert werden.

Hierarchie:

1. Grundfrage: Wann ist Memorydruck belastend, wann ist er Bedeutungsverdichtung?
2. Unterpruefung: `field_carried`, dominante Wirkung und Rekopplung muessen in die Klassifikation staerker eingehen.
3. Folgeschritt: Danach die 2k-Welten erneut klassifizieren, ohne neue Laeufe zu starten.
