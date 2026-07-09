# Synthetische Harmonie-Zeitdehnung Topologie-Synthese

Stand: 2026-06-22

## Zweck

Diese Synthese prueft die Zeitdehnungsfrage an einer zweiten synthetischen Grundform.

Nach `bruch_rand` wurde hier `harmonic` verwendet:

- weniger Bruch,
- weniger Randspannung,
- mehr ruhige Expansion,
- mehr Rueckkehr in stabile Feldlage.

Die Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Bleibt der Zeitdehnungseffekt auch bei anderer Grundform sichtbar?
2. Unterpruefung: Wird die gedehnte Variante zentrumsnaeher aufgenommen?
3. Unterpruefung: Gibt es lokale Phasenverschiebungen wie bei `randflackern`?
4. Folgeschritt: Unterschied zwischen allgemeiner Feldzeit-Integration und musterspezifischer Oeffnung klaeren.

## Forschungslaeufe

| Lauf | Welt | Kerzen | Episoden | Unique Syntax | Rekopplung | Carry | Sinneskopplung |
|---|---|---:|---:|---:|---:|---:|---:|
| 722 | Harmonie kompakt | 2700 | 2694 | 47 | 0.7535 | 0.6098 | 0.9152 |
| 723 | Harmonie gedehnt | 10800 | 10794 | 44 | 0.7581 | 0.6198 | 0.9173 |

Befund:

- Beide Varianten reproduzieren Top-Syntax und Top-Familien mit `1.0` Ueberlappung.
- Die gedehnte Variante hat leicht hoehere Rekopplung, Carry und Sinneskopplung.
- Die Anzahl eindeutiger Syntaxsymbole sinkt leicht von `47` auf `44`, obwohl die Welt laenger ist.

Das spricht nicht fuer wahlloses Mehrspeichern, sondern fuer staerkere Verdichtung bei laengerer Integrationszeit.

## Globale Topologie

| Welt | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| HARMONIE_ZEIT_KOMPAKT | 2694 | 0.9978 | 0.0019 | 0.0004 | 0.7535 | 0.6098 | 0.9152 |
| HARMONIE_ZEIT_GEDEHNT | 10794 | 0.9995 | 0.0004 | 0.0001 | 0.7581 | 0.6198 | 0.9173 |

Befund:

- Beide Welten sind extrem zentrumsnah.
- Die gedehnte Welt wird noch zentrumsnaeher.
- Offenheit und Rand/Kippnaehe nehmen unter Dehnung weiter ab.

## Rezeptorachsen

| Welt | Zentrum | Offen | Rand/Kipp | Lautheit | Rohfeld | Adaptfeld | Ratio | High-Offen | High-Rand/Kipp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| HARMONIE_ZEIT_KOMPAKT | 0.9640 | 0.0171 | 0.0011 | 0.0321 | 0.0254 | 0.0231 | 0.9092 | 0.1185 | 0.0111 |
| HARMONIE_ZEIT_GEDEHNT | 0.9921 | 0.0040 | 0.0002 | 0.0206 | 0.0197 | 0.0180 | 0.9143 | 0.0296 | 0.0019 |

Befund:

- Kompakte Harmonie hat die staerkeren Hochlastfenster.
- Gedehnte Harmonie reduziert offene Hochlast deutlich.
- Die adaptierte Feldaufnahme bleibt unter Rohaufnahme.

## Lokale Phasenlesung

Bei `harmonic` gibt es kein starkes `randflackern`.
Die wichtigste offene Phase ist `kippnaehe`, aber auch sie bleibt stark zentriert.

| Phase | Kompakt Zentrum | Kompakt Offen | Kompakt Rekopplung | Gedehnt Zentrum | Gedehnt Offen | Gedehnt Rekopplung |
|---|---:|---:|---:|---:|---:|---:|
| ruhig | 0.9822 | 0.0067 | 0.0089 | 0.9961 | 0.0011 | 0.0022 |
| expansion | 0.9533 | 0.0200 | 0.0244 | 0.9906 | 0.0056 | 0.0039 |
| unruhe | 0.9533 | 0.0267 | 0.0200 | 0.9911 | 0.0050 | 0.0039 |
| kippnaehe | 0.9200 | 0.0356 | 0.0444 | 0.9783 | 0.0094 | 0.0122 |
| rekopplung | 0.9822 | 0.0111 | 0.0044 | 0.9978 | 0.0017 | 0.0000 |
| ruhe_rueckkehr | 0.9932 | 0.0023 | 0.0045 | 0.9989 | 0.0011 | 0.0000 |

Befund:

- In jeder Phase steigt die Zentrumsnaehe durch Dehnung.
- Offene Variante nimmt in jeder Phase ab.
- Die lokale Rekopplungsnaehe nimmt ebenfalls ab, weil die Phase nicht mehr als Uebergang gelesen werden muss, sondern direkt zentrumsnah integriert wird.

## Vergleich zu `bruch_rand`

Der vorherige `bruch_rand`-Test zeigte:

- globale Topologie bleibt stabil,
- `randflackern` bleibt lokal offen,
- Dehnung verschiebt `randflackern` von offener Dominanz zu mehr Zentrum/Rekopplung.

Der neue `harmonic`-Test zeigt:

- globale Topologie bleibt ebenfalls stabil,
- die Welt ist bereits stark zentriert,
- Dehnung macht sie noch zentrumsnaeher,
- es entsteht keine neue starke offene Phase.

Damit ist die Unterscheidung klarer:

```text
Zeitdehnung wirkt allgemein integrierend.
Starke lokale Oeffnung entsteht aber nur, wenn die Weltform selbst Rand-/Bruchqualitaet traegt.
```

## MCM-Lesart

Die zweite Grundform stuetzt die Feldzeit-Hypothese vorsichtig:

- Zeitdehnung veraendert nicht einfach die Menge der Daten.
- Zeitdehnung veraendert die Integrationsqualitaet der Feldwirkung.
- Bei ruhiger/harmonischer Welt wird daraus mehr Zentrum.
- Bei Rand-/Bruchwelt bleibt lokale Oeffnung sichtbar, wird aber teilweise rekoppelt.

Das spricht fuer:

```text
Feldzeit = integrierte Wirkung ueber Innenfeldtiefe
```

Nicht:

```text
Feldzeit = nur Kerzenanzahl oder externe Tick-Laenge
```

## Grenze

Der Befund ist kontrolliert und synthetisch.

Er zeigt keine universelle MCM-Zeitphysik, aber eine reproduzierbare MINI_DIO-Beobachtung:

- gleiche Formbasis,
- andere zeitliche Streckung,
- stabile Topologie,
- veraenderte lokale Integration.

## Wie es weitergeht

Als naechstes sollte `rand_dominanz` kompakt/gedehnt geprueft werden. Das ist der Haertefall: Wenn Zeitdehnung dort nicht nur Zentrum erhoeht, sondern Randlast anders organisiert, koennen wir Feldzeit als robuste Integrationsachse besser abgrenzen.
