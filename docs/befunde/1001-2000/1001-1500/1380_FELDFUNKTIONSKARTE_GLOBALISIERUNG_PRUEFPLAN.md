# 1380 - Feldfunktionskarte: Globalisierung Pruefplan

## Grundfrage

```text
Sind Bruecke, Zentrumskontakt und Randdruck allgemeine passive Feldrollen,
oder sind sie nur in der Mikrophase `hoerbarer_schmaler_shift` stabil?
```

Diese Frage ist der naechste hierarchische Schritt nach `1378` und `1379`.

## Stand

Aus `1378`:

- Bruecke, Zentrumskontakt und Randdruck sind in kontrollierten Gegenproben unterscheidbar.
- Reizstaerke allein reicht nicht.
- Entscheidend ist die Kopplung aus Lagefolge, Sinnesaktivierung und MCM-Nachhall.

Aus `1379`:

- Bruecke tritt ueber BTC, DOGE, SOL und XRP auf.
- Zentrumskontakt tritt ueber DOGE, SOL und XRP auf.
- Randdruck tritt stark BTC-lastig auf, aber auch in SOL und PAXG.

Damit ist die Feldfunktionskarte nicht auf eine einzelne Welt beschraenkt. Sie ist aber noch an den Kandidatenraum `hoerbarer_schmaler_shift` gebunden.

## Methodische Grenze

Die Rollen duerfen nicht einfach auf alle Episoden hart uebertragen werden.

Grund:

```text
Eine Feldfunktion ist nicht nur ein Zahlenbereich.
Sie entsteht aus Lagefolge, Sinnesaktivierung und Nachhall.
```

Wenn wir in beliebigen Episodensets nur Schwellen auf Rekopplung, Strain oder Sinneskopplung legen, bauen wir wieder eine mechanische Pseudorolle.

## Sauberer naechster Test

Der globale Test muss zweistufig sein:

### 1. Kandidatenfrei lesen

Aus grossen Episodensets werden zuerst passive Feldphasen gelesen:

- stabile Rekopplung,
- steigende Sinneskopplung,
- sinkender oder steigender Strain,
- Preview-Nachhall,
- Symbolfamilien-Nachhall,
- Feldzustandswechsel.

Diese Phase benennt noch keine Bruecke, kein Zentrum und keinen Randdruck.

### 2. Rollennaehe pruefen

Erst danach wird geprueft, ob die gelesenen Feldphasen einer bekannten Feldfunktion nahekommen:

- Uebergangsnaehe zu Bruecke,
- aktivierte Zentrumsnaehe,
- fortgesetzter Druckkontakt,
- oder neue Mischrolle.

## Erwartete Ergebnisse

Moegliche Befunde:

### Stabil

```text
Die bekannten Rollen erscheinen auch ausserhalb des Kandidatenraums.
```

Dann waeren Bruecke, Zentrumskontakt und Randdruck staerkere Kandidaten fuer allgemeine MCM-Feldrollen.

### Drift

```text
Eine Rolle bleibt erkennbar, verschiebt aber ihre Nachbarschaft oder Symbolfamilien.
```

Dann waere sie weltspannungsabhaengig, aber nicht beliebig.

### Mischrolle

```text
Neue Feldphasen liegen zwischen bekannten Rollen.
```

Dann waere die Dreierkarte unvollstaendig und muesste erweitert werden.

### Zerfall

```text
Die Rollen verschwinden ausserhalb des Kandidatenraums.
```

Dann waere die Karte mikrophasen-spezifisch und duerfte nicht als globale Feldordnung gelesen werden.

## Naechste technische Umsetzung

Ein neues Diagnosewerkzeug sollte:

1. mehrere vorhandene `episodes.csv` lesen,
2. rollenneutral lokale Feldphasen bilden,
3. Nachhall ueber Folgefenster messen,
4. erst danach Naehe zu `Bruecke`, `Zentrumskontakt`, `Randdruck` oder `neue_mischrolle` markieren,
5. alle Ergebnisse als passive Diagnose ausgeben.
