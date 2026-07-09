# 1529 - Memory-Wiederverwendung und Feldzeit-Test

## Grundfrage

Die vorherigen Null- und Stresskontrollen zeigten, dass MINI_DIO strukturierte Welten, Nullwelten und Stresswelten unterschiedlich beantwortet. Offen blieb die nächste methodische Frage:

```text
Wird bei wiederholtem Weltkontakt vorhandene Bedeutung wiederverwendet,
oder entstehen trotz Memory wieder neue Symbolinseln?
```

Diese Prüfung ist wichtig, weil sie zwischen bloßer Reaktion und beginnender Bedeutungswiederverwendung unterscheidet. Ein starkes Ergebnis wäre nicht, dass das System mehr neue Namen erzeugt, sondern dass bekannte Rollen stabil wieder aktiviert werden.

## Aufbau

Es wurden drei Läufe mit isolierter Debug-Memory ausgeführt:

1. **A - frische Memory auf 1525**
   - strukturierte Mosaikwelt
   - Memory vorher gelöscht
2. **B - gleiche Welt ohne Reset**
   - identische Mosaikwelt
   - gleiche Memory wie A
3. **C - verwandte Holdout-Welt**
   - andere, aber verwandte Mosaikwelt
   - gleiche Memory wie A und B

Alle Läufe blieben passiv. Es wurden keine Handlungen, Gates oder Richtungsvorgaben geprüft.

## Ergebnis

| Lauf | Welt | Symbole | stabil | Unruhe | Nachhall | Feldzeit-Vertrauen | Bedeutungsanzeige | Kernrollen |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| A | 1525 frisch | 97 | 0.8759 | 0.1236 | 0.4053 | 0.7784 | 0 / 2394 | `dio_0l7p`, `dio_1wdi`, `dio_14wj`, `dio_1fll` |
| B | 1525 wiederholt | 97 | 0.8759 | 0.1236 | 0.4053 | 0.7784 | 2098 / 296 | gleiche Rollen, verdoppelte Memory-Zähler |
| C | 1502 Holdout | 85 | 0.8719 | 0.1281 | 0.3666 | 0.7318 | 1041 / 153 | gleiche Kernrollen, leicht geringerer Nachhall |

Die vollständige Tabelle liegt in [1529_MEMORY_WIEDERVERWENDUNG_FELDZEIT_TEST.csv](1529_MEMORY_WIEDERVERWENDUNG_FELDZEIT_TEST.csv).

## Interpretation

### A nach B

Der zweite Lauf erzeugt keine neue Symbolstreuung. Die Symbolzahl bleibt bei `97`, die Top-Symbole bleiben gleich, und die Feldwerte bleiben nahezu identisch.

Der Unterschied liegt in der Memory-Wiederverwendung:

- A: `meaning_display_found = 0`
- B: `meaning_display_found = 2098`

Das bedeutet: Beim zweiten Kontakt liest MINI_DIO große Teile der Innenfeldlage als bereits benennbar. Es wird nicht einfach wieder neu erfunden, sondern vorhandene Bedeutungsqualität wird erneut aktiviert.

### B nach C

Die Holdout-Welt ist kürzer und anders geordnet. Trotzdem bleiben die Kernrollen erhalten:

- `dio_0l7p`
- `dio_1wdi`
- `dio_14wj`
- `dio_1fll`

Die Symbolzahl sinkt auf `85`, der Nachhall sinkt von `0.4053` auf `0.3666`, und das Feldzeit-Vertrauen sinkt von `0.7784` auf `0.7318`. Das ist fachlich plausibel: Die Welt ist verwandt, aber nicht identisch. MINI_DIO übernimmt also nicht blind, sondern koppelt an bekannte Rollen mit veränderter Feldtiefe.

## Befund

Der Test stützt die Annahme:

```text
MINI_DIO speichert nicht wahllos neue Information,
sondern kann bekannte Bedeutungsrollen erneut aktivieren.
```

Noch nicht bewiesen ist Lernen im starken Sinn. Gezeigt ist aber eine reproduzierbare Memory-Wiederverwendung:

- gleiche Welt -> gleiche Rollen und gleiche Feldkarte,
- wiederholte Welt -> Bedeutungsanzeige wird aktiv,
- verwandte Welt -> bekannte Rollen werden übertragen, aber Feldzeit und Nachhall verändern sich.

Damit wird die Anti-Pareidolie-Prüfung erweitert. Wenn nur Rauschen vorläge, wäre bei B eher erneute Symbolstreuung zu erwarten. Stattdessen bleibt die Ordnung eng und wird als bekannt markiert.

## Grenze

Dieser Befund beweist noch keine allgemeine MCM-Lernfähigkeit. Er zeigt aber, dass die aktuelle MINI_DIO-Memory nicht nur Rohdaten zählt, sondern wiederkehrende Feldrollen in einer Weise trägt, die bei erneutem und verwandtem Weltkontakt lesbar bleibt.
