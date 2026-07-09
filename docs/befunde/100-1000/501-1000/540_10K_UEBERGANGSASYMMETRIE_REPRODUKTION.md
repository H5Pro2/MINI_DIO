# 10k-Uebergangsasymmetrie - Reproduktion

Stand: 2026-06-21

## Zweck

Diese Diagnose wiederholt die gezielte Uebergangsfrage aus `538_PREVIEW_UEBERGANG_1T5BCXP_183DRJY_ASYMMETRIE` auf den 10k-After/Repro-Welten.

Geprueft wird:

```text
Bleibt die gerichtete Feldbewegung zwischen 1t5bcxp und 183drjy reproduzierbar?
```

Die Diagnose bleibt passiv.
Sie erzeugt keine Handlung, kein Gate und keine Richtungsvorgabe.

## Hierarchie

1. Grundfrage: Ist die Uebergangsasymmetrie stabil oder ein Einzelbefund?
2. Unterpruefung: Reproduzieren Stable, Stress und Expansion dieselben Achsendeltas in After/Repro?
3. Folgeschritt: Wenn ja, muss die Feldbewegung als eigene Bedeutungsebene behandelt werden.

## Gesamtbefund

| Uebergang | Anzahl | Welten | dDruck | dEntspannung | dRekopplung | dStrain | dSchaerfe | dLautheit | Lesart |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `1t5bcxp -> 183drjy` | 230 | 6 | -0.0165 | +0.0165 | +0.0231 | -0.0264 | +0.0293 | -0.0467 | rekoppelnd, beruhigend, schaerfend |
| `183drjy -> 1t5bcxp` | 168 | 6 | +0.0185 | -0.0185 | -0.0219 | +0.0337 | -0.0636 | +0.0951 | oeffnend, lauter, strainnaeher |

## Reproduktion

Die After/Repro-Werte sind fuer jede 10k-Welt identisch:

| Welt | `1t5bcxp -> 183drjy` dDruck | `1t5bcxp -> 183drjy` dRekopplung | `183drjy -> 1t5bcxp` dDruck | `183drjy -> 1t5bcxp` dRekopplung |
|---|---:|---:|---:|---:|
| STABLE_AFTER | -0.0157 | +0.0232 | +0.0133 | -0.0172 |
| STABLE_REPRO | -0.0157 | +0.0232 | +0.0133 | -0.0172 |
| STRESS_AFTER | -0.0189 | +0.0241 | +0.0234 | -0.0250 |
| STRESS_REPRO | -0.0189 | +0.0241 | +0.0234 | -0.0250 |
| EXPANSION_AFTER | -0.0151 | +0.0220 | +0.0190 | -0.0235 |
| EXPANSION_REPRO | -0.0151 | +0.0220 | +0.0190 | -0.0235 |

## Rollenbewegung

`1t5bcxp -> 183drjy` bleibt stark zentrumsnah:

```text
zentrum_stabil -> zentrum_stabil: 212 von 230
offene_variante -> zentrum_stabil: 16 von 230
```

Der Rueckweg bleibt deutlich variabler:

```text
zentrum_stabil -> zentrum_stabil: 56 von 168
zentrum_stabil -> offene_variante: 42 von 168
zentrum_stabil -> spannungsrand_kippnaehe: 18 von 168
```

Damit reproduziert sich nicht nur der Zahlenwert, sondern auch die qualitative Richtung:

```text
Hinweg: Verdichtung zum stabileren Zentrum.
Rueckweg: Oeffnung in Variante und Randmoeglichkeit.
```

## Erkenntnis

Dieser Befund ist staerker als der reine Inselbefund.

MINI_DIO zeigt hier:

```text
1. wiederkehrende Bedeutungsinseln
2. reproduzierbare Rollenanteile
3. reproduzierbare gerichtete Feldbewegung zwischen Bedeutungsinseln
```

Das ist fuer die MCM-Arbeit wichtig:

```text
Bedeutung entsteht nicht nur als Feldinsel.
Bedeutung entsteht auch als Bewegung zwischen Feldinseln.
```

Die Bewegung `1t5bcxp -> 183drjy` wirkt wie eine passive Rekopplungsbewegung.
Die Bewegung `183drjy -> 1t5bcxp` wirkt wie passive Oeffnung in breitere Varianz.

Beides ist keine Handlung und keine Strategie.
Es ist Feldsemantik.

## Grenze

Die Reproduktion ist stark, aber sie bezieht sich auf vorhandene 10k-Welten.
Eine vollstaendige Absicherung braucht weitere lange Welten oder frische Memory-Neustarts.

## Wie es weitergeht

Als naechstes sollte diese gerichtete Feldbewegung als eigener passiver Baustein in die Feldbewegungs-Memory eingeordnet werden.
Ziel ist nicht Handlung, sondern das Speichern von wiederkehrender Bewegungsqualitaet: rekoppelnd, oeffnend, strainnah, beruhigend oder fragmentierend.
