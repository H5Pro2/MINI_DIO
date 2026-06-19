# Lokale multisensorische Syntax - Befund

Stand: 2026-06-19

## Kurzbefund

Lokale multisensorische Fenster tragen bereits wiederkehrende Symbolfamilien.

Aber:

Die MCM-Feld-Episodensymbole sind in dieser Diagnose noch nicht tragend ausgebildet.
Sie stehen in den ausgewerteten Fenstern fast vollstaendig auf `-`.

Damit ist der Befund zweigeteilt:

1. MINI_DIO bildet lokale Syntaxnaehe ueber `symbol_family`.
2. Die tiefere Feld-Episodenspur ist fuer diese lokalen Fenster noch nicht ausreichend verdichtet.

## Was sichtbar ist

Bei `lokal_rekoppelnd` erscheinen mehrere Familien wiederholt:

- `dio_054b`
- `dio_0ti6`
- `dio_1ttr`
- `dio_0rkf`
- `dio_1ril`

Bei `lokale_multisensorische_kippnaehe` erscheint besonders:

- `dio_0wc3`
- `dio_00cf`

Das ist relevant:

Kippnaehe und Rekopplung verwenden nicht exakt dieselbe Oberflaechensyntax.
Es gibt erste rollenbezogene Familienhaeufungen.

## Was noch nicht sichtbar ist

Die `mcm_field_episode_symbol`-Spalte traegt lokal noch keine stabile eigene Feldsyntax.

In der Diagnose dominiert:

```text
Feldsymbol: -
```

Das bedeutet:

MINI_DIO benennt lokale multisensorische Fenster aktuell eher ueber seine laufende Oberflaechen-/Familien-Syntax als ueber eine gereifte Feld-Episodensprache.

Das ist kein Fehler.
Es ist ein Entwicklungsstand.

## Fachliche Schlussfolgerung

Eine lokale multisensorische Bedeutungsinsel ist noch nicht voll bestaetigt.

Was wir aktuell sagen koennen:

```text
Lokale Sinnesinnenlagen erzeugen wiederkehrende Symbolfamilien.
Sie sind aber noch nicht als eigene MCM-Feld-Episoden verdichtet.
```

Damit liegt MINI_DIO zwischen zwei Stufen:

1. lokale Wahrnehmungsfamilie,
2. gereifte Feld-Episodenbedeutung.

Die erste Stufe ist sichtbar.
Die zweite Stufe muss noch geprueft oder verbessert werden.

## Bedeutung fuer MINI_DIO

Das ist ein wichtiger Hinweis fuer die weitere Forschung:

Wenn MINI_DIO langfristig echte lokale Bedeutungsinseln bilden soll, reicht Oberflaechensyntax nicht.

Die Kopplung muss tiefer werden:

- lokale Kippnaehe,
- lokale Rekopplung,
- dominierende Symbolfamilie,
- MCM-Wirkung,
- Wiederkehr ueber Lauf 1 und Lauf 2,
- spaetere Feld-Episodenspur.

Erst wenn diese Ebenen zusammenfinden, entsteht eine robuste lokale Innenfeldinsel.

## Kritische Einordnung

Die Symbolfamilienanteile pro Fenster sind niedrig.
Das liegt daran, dass ein Fenster viele kurze Symbole enthalten kann.

Deshalb ist nicht der Einzelanteil innerhalb eines Fensters entscheidend, sondern:

- ob Familien rollenbezogen wiederkehren,
- ob dieselben Tickbereiche in Lauf 1 und Lauf 2 aehnlich bleiben,
- ob sich daraus spaeter eine Feld-Episodenspur bildet.

## Wie es weitergeht

Als naechstes sollte die Feld-Episodenspur gezielt untersucht werden:

1. Pruefen, warum `mcm_field_episode_symbol` lokal noch meist `-` bleibt.
2. Klaeren, ob die Feld-Episodenspur nur bei anderen Laufarten entsteht oder aktuell zu spaet/zu grob geschrieben wird.
3. Danach entscheiden, ob MINI_DIO eine passive lokale Feld-Episodenverdichtung braucht.

Wichtig:

Das bleibt passiv.
Es geht nicht um Handlung, sondern um die Frage, ob lokale Wahrnehmungsinseln in eine tiefere MCM-Feldsprache uebergehen koennen.
