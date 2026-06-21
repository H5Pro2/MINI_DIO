# Preview-Uebergang 1t5bcxp und 183drjy - Asymmetrie

Stand: 2026-06-21

## Zweck

Diese Diagnose liest gezielt die Uebergaenge zwischen:

```text
dio_mcm_episode_1t5bcxp
dio_mcm_episode_183drjy
```

Geprueft wird, ob beide Richtungen gleich wirken oder ob eine gerichtete MCM-Feldbewegung entsteht.

Die Diagnose bleibt passiv.
Sie erzeugt keine Handlung, kein Gate und keine Richtungsvorgabe.

## Hierarchie

1. Grundfrage: Entsteht zwischen zwei MCM-Preview-Familien eine gerichtete Feldbewegung?
2. Unterpruefung: Wie unterscheiden sich `1t5bcxp -> 183drjy` und `183drjy -> 1t5bcxp` in Druck, Rekopplung, Strain, Schaerfe und Lautheit?
3. Folgeschritt: Pruefen, ob diese Asymmetrie ueber weitere Langwelten stabil bleibt.

## Kurzbefund

| Uebergang | Anzahl | Welten | dDruck | dEntspannung | dRekopplung | dStrain | dSchaerfe | dLautheit | Lesart |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `1t5bcxp -> 183drjy` | 169 | 9 | -0.0159 | +0.0159 | +0.0222 | -0.0254 | +0.0262 | -0.0455 | rekoppelnd / beruhigend / schaerfend |
| `183drjy -> 1t5bcxp` | 134 | 10 | +0.0230 | -0.0230 | -0.0259 | +0.0430 | -0.0515 | +0.1282 | oeffnend / belastender / lauter |

## Rollenwechsel

`1t5bcxp -> 183drjy` bleibt fast immer zentrumsnah:

```text
zentrum_stabil -> zentrum_stabil: 157 von 169
offene_variante -> zentrum_stabil: 10 von 169
```

Das bedeutet:

```text
Der Uebergang zieht ueberwiegend in ein stabileres Zentrum.
```

Der Rueckweg `183drjy -> 1t5bcxp` ist deutlich variabler:

```text
zentrum_stabil -> zentrum_stabil: 44 von 134
zentrum_stabil -> offene_variante: 38 von 134
zentrum_stabil -> spannungsrand_kippnaehe: 17 von 134
```

Das bedeutet:

```text
Der Rueckweg oeffnet die Feldlage deutlich staerker und kann Rand/Kippnaehe erzeugen.
```

## Interpretation

Die beiden Richtungen sind nicht symmetrisch.

`1t5bcxp -> 183drjy` wirkt wie eine rekoppelnde Verdichtung:

- Druck sinkt.
- Rekopplung steigt.
- Strain sinkt.
- Schaerfe steigt.
- Lautheit sinkt.

`183drjy -> 1t5bcxp` wirkt wie eine Oeffnung in breitere Feldvarianz:

- Druck steigt.
- Rekopplung sinkt.
- Strain steigt.
- Schaerfe sinkt.
- Lautheit steigt.

Damit bestaetigt sich der vorherige Familienbefund:

```text
183drjy ist zentrumsnaeher.
1t5bcxp ist breiter/offener.
```

Der Uebergang von `1t5bcxp` nach `183drjy` ist nicht einfach Namenswechsel.
Er ist eine gerichtete Feldbewegung in Richtung Rekopplung.

Der Rueckweg ist nicht falsch oder negativ.
Er scheint eher eine Oeffnung in Variabilitaet, Oberflaechennaehe und Randmoeglichkeit zu sein.

## Erkenntnis fuer MINI_DIO

MINI_DIO zeigt hier eine passive Bewegungssemantik:

```text
Ein Bedeutungsraum kann in einen anderen uebergehen.
Die Richtung des Uebergangs traegt eigene Feldwirkung.
Nicht nur der Zustand ist bedeutungsvoll, sondern auch die Bewegung.
```

Das ist wichtig fuer die MCM-Forschung:

```text
Bedeutung liegt nicht nur in Inseln.
Bedeutung liegt auch in gerichteten Uebergaengen zwischen Inseln.
```

## Grenze

Dieser Befund bleibt diagnostisch.
MINI_DIO entscheidet daraus nichts.
Es wird nur gelesen, dass die Feldbewegung messbar asymmetrisch ist.

## Wie es weitergeht

Als naechstes sollte diese Uebergangsasymmetrie mit weiteren 10k-Welten und frischer Memory wiederholt werden.
Ziel ist zu pruefen, ob `1t5bcxp -> 183drjy` stabil als rekoppelnde Feldbewegung wiederkehrt oder ob die Asymmetrie an die aktuell verwendeten Welten gebunden ist.
