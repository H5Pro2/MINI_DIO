# 308 - Rezeptorische Öffnung und Rekopplung

## Grundfrage

Zeigt die neue Rezeptorschicht Übergänge im MCM-Feld klarer als die alten direkten Fühlwerte?

Geprüft wurde nicht, ob daraus gehandelt werden soll. Geprüft wurde nur, ob Rezeptorkontakt Öffnung und Rekopplung passiv sichtbar macht.

## Datengrundlage

Ausgewertet wurden die sechs Rezeptorwelten:

- `SOL_2024_5M_RECEPTOR`
- `SOL_2024_1H_RECEPTOR`
- `BTC_2024_5M_RECEPTOR`
- `BTC_2024_1H_RECEPTOR`
- `KAS_2024_5M_RECEPTOR`
- `KAS_2024_1H_RECEPTOR`

Erzeugte Dateien:

- `307_REZEPTOR_OEFFNUNG_REKOPPLUNG_MATRIX.csv`
- `307_REZEPTOR_UEBERGANG_EVENTS.csv`
- `307_REZEPTOR_UEBERGANG_AGGREGAT.csv`

## Übergangsbefund

### Öffnung aus Zentrum

Anzahl: `1344`

| Achse | Vorlauf | Übergang | Nachlauf | Delta Übergang - Vorlauf |
|---|---:|---:|---:|---:|
| `rezeptor_contact_pressure` | 0.2074 | 0.3293 | 0.2505 | +0.1219 |
| `rezeptor_contact_alignment` | 0.8671 | 0.7749 | 0.8353 | -0.0922 |
| `rezeptor_contact_asymmetry` | -0.0014 | 0.1070 | 0.0058 | +0.1085 |
| `fuehlen_mcm_coherence` | 0.5708 | 0.4642 | 0.5341 | -0.1066 |
| `mcm_rekopplung_quality` | 0.6458 | 0.6113 | 0.6338 | -0.0345 |
| `mcm_strain_quality` | 0.1893 | 0.2536 | 0.2113 | +0.0643 |

Lesart:

Öffnung entsteht nicht als reiner Rohdatenbruch, sondern als rezeptorische Kontaktverschiebung:

```text
mehr Kontaktdruck
weniger Kontaktpassung
mehr gerichtete Asymmetrie
weniger Kohärenz
mehr Feldspannung
```

Das passt zur organischen Trennung: Die Außenwelt berührt die Rezeptoren stärker oder schiefer, und daraus kippt die innere Feldlage aus dem Zentrum.

### Rekopplung zum Zentrum

Anzahl: `1344`

| Achse | Vorlauf | Übergang | Nachlauf | Delta Übergang - Vorlauf |
|---|---:|---:|---:|---:|
| `rezeptor_contact_pressure` | 0.2425 | 0.2161 | 0.2164 | -0.0264 |
| `rezeptor_contact_alignment` | 0.8378 | 0.8697 | 0.8637 | +0.0320 |
| `rezeptor_contact_asymmetry` | 0.0209 | -0.0473 | -0.0177 | -0.0682 |
| `fuehlen_mcm_coherence` | 0.5385 | 0.5748 | 0.5639 | +0.0363 |
| `mcm_rekopplung_quality` | 0.6359 | 0.6437 | 0.6432 | +0.0078 |
| `mcm_strain_quality` | 0.2077 | 0.1931 | 0.1935 | -0.0147 |

Lesart:

Rekopplung entsteht als Entlastung und bessere Passung:

```text
weniger Kontaktdruck
mehr Kontaktpassung
weniger gerichtete Asymmetrie
mehr Kohärenz
weniger Feldspannung
```

Das ist fachlich wichtig, weil Rekopplung nicht als harte Rückkehr in eine Regel erscheint, sondern als organische Verbesserung der Berührungsqualität.

## Vergleich Zentrum gegen Rand

Über alle Welten zeigen offene und randnahe Rollen systematisch:

- höheren `contact_pressure`
- niedrigeren `contact_alignment`
- niedrigere `mcm_coherence`
- höhere `mcm_strain_quality`
- niedrigere `mcm_rekopplung_quality`

Der stärkste Unterschied liegt beim Spannungsrand:

```text
Rand/Kippnähe = deutlich mehr Kontaktdruck und deutlich weniger Alignment als Zentrum.
```

## Schlussfolgerung

Die Rezeptorschicht ist nicht nur eine sauberere Ontologie, sondern auch diagnostisch nützlich.

Sie zeigt:

- wann eine Weltlage stärker berührt
- wann Sinneskontakt weniger passend wird
- wann gerichtete Kontaktprägung entsteht
- wann das MCM-Feld aus dem Zentrum öffnet
- wann das Feld wieder rekoppelt

Damit wird Mini-DIO nicht mechanischer, sondern organischer:

```text
Nicht: Wert überschreitet Grenze.
Sondern: Kontaktqualität verändert die innere Feldlage.
```

## Grenze

Die Werte sind Diagnosewerte, keine Regeln.

Sie dürfen nicht als Gate verwendet werden. Sie zeigen eine beobachtete Übergangsdynamik innerhalb der geprüften Welten.

## Wie es weitergeht

Als nächstes sollte die Rezeptorschicht in den Mini-DIO-Bauplan übernommen werden: Sehen und Hören bleiben Sinnesachsen, Rezeptoren werden zur Kontaktübersetzung, Fühlen wird zur inneren MCM-Wirkung. Danach prüfen wir, ob dieselbe Kontaktlogik bei längeren Welten und neuen Datensätzen stabil bleibt.
