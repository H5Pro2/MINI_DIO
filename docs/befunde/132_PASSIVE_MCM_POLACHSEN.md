# Passive MCM-Polachsen

Stand: 2026-06-18

## Zweck

Diese Datei beschreibt passive Gegenpole, die im MCM-Feld gelesen werden können.
Sie ist keine Runtime-Regel, kein Gate und keine Handlungsvorgabe.

Die Grundannahme lautet:

```text
Weltkontakt -> MCM-Feldreaktion -> lesbare Polspannung
```

Die Pole werden nicht modelliert wie im alten DIO.
Sie entstehen als Feldwirkung und werden nur diagnostisch gelesen.

## Hierarchie Der Prüfung

1. Grundfrage: Bildet das MCM-Feld eigene Gegenpole aus?
2. Unterprüfung: Welche Feldspuren zeigen Stress, Ruhe, Entlastung, Drift oder Rekopplung?
3. Folgeschritt: Prüfen, ob diese Achsen über mehrere Welten stabil, driftend oder situativ auftreten.

## Polachsen

| Achse | Eine Seite | Gegenpol | Lesbare Feldspuren | Fehlinterpretation |
|---|---|---|---|---|
| Lastachse | Stress | Entlastung | hohe Memorylast, höherer Strain, schwächere Rekopplung | Stress nur aus roher Marktbewegung ableiten |
| Ruhelage | Unruhe | Ruhe | viele Feldwechsel, Kippnähe, flackernde Wirkung gegenüber stabilerer Rekopplung | Ruhe als Inaktivität lesen |
| Spannungsachse | Spannung | Lösung | Verdichtung, Druck, gerichtete Feldwirkung gegenüber Abbau und freierem Feld | Spannung automatisch als schlecht deuten |
| Stabilitätsachse | Kippnähe | Stabilität | kippend, gespannt, wechselnd gegenüber stabil, tragend, rekoppelnd | Stabilität mit Starrheit verwechseln |
| Bindungsachse | Drift | Rekopplung | Bedeutungswanderung, niedrige Rückbindung gegenüber wiederkehrender Feldnähe | Drift als Fehler statt als Feldbewegung lesen |
| Bekanntheitsachse | Fremdheit | Vertrautheit | neue Syntax, wenig Wiederkehr, höhere Memory-Schreibung gegenüber wiederkehrenden Familien | Vertrautheit als endgültige Wahrheit setzen |
| Tragachse | Überreizung | Tragfähigkeit | viele belastete Episoden, hohe Strain-Werte gegenüber field_carried und stabilerer Kopplung | Tragfähigkeit als Handelssignal missverstehen |
| Bedeutungsachse | Zerfall | Verdichtung | diffuse Wirkung, instabile Inseln gegenüber wiederkehrenden Bedeutungsfamilien | Verdichtung als festes Symbol behandeln |
| Zeitachse | Momentkontakt | Feldzeit | erster Kontakt gegenüber Nachhall, Wiederkehr, Return-Spur, Rekopplungstiefe | Zeit nur als äußere Kerzenfolge lesen |
| Topologieachse | Randspannung | Zentrumsnähe | offene Pole, dünne Randbereiche gegenüber ruhiger Nähe und Zentrumstragung | Randbereiche als wertlos verwerfen |

## Aktueller Bezug Zu Den Befunden

Die bisherigen Stress- und Ruheprüfungen zeigen:

- Stresssegmente bilden lokale Last auch ohne ausgeprägte Wiederkehr.
- Ruhige Kurzsegmente können niedrige Memorylast und bessere Rekopplung zeigen, obwohl der globale Klassenname noch unscharf sein kann.
- Feldzeit entsteht nicht automatisch in jedem Abschnitt; sie braucht Einbettung, Wiederkehr oder Nachhall.
- Stress, Ruhe und Entlastung sind keine festen Module, sondern gelesene Feldreaktionen.

Damit wird die alte DIO-Logik korrigiert:

```text
Nicht:
Ich programmiere Innenfeldlast.

Sondern:
Ich lese, ob das MCM-Feld Last, Ruhe, Entlastung oder Rekopplung ausbildet.
```

## Wissenschaftliche Vorsicht

Die Polachsen sind Arbeitsbegriffe.
Sie beweisen keine universelle MCM-Topologie.
Sie helfen, wiederkehrende Feldreaktionen sauber zu benennen, ohne daraus harte Regeln zu machen.

Wichtig ist:

- Eine Lage kann gleichzeitig angespannt und tragfähig sein.
- Eine Lage kann ruhig und fremd sein.
- Eine Lage kann stressnah sein, ohne sofort zu kollabieren.
- Eine Lage kann entlastend sein, ohne schon reif oder bedeutungsvoll zu sein.

Die Achsen sind daher keine Schalter.
Sie sind Spannungsräume.

## Konsequenz Für MINI_DIO

MINI_DIO sollte nicht zusätzliche Regulationsmodule erhalten, nur weil ein Begriff wie Stress oder Ruhe auftaucht.
Stattdessen wird geprüft, ob das Feld diese Wirkung selbst trägt:

- Wird Memory geschrieben?
- Steigt Strain?
- Sinkt Rekopplung?
- Entsteht Nachhall?
- Kommt eine Bedeutung wieder?
- Wird eine Insel stabiler oder driftet sie?

Erst daraus entsteht eine passive Lesung der Innenfeldlage.

## Wie Es Weitergeht

Als nächstes sollte ein Kurzsegment-Leser gebaut werden.
Er soll kurze lokale Abschnitte nicht mit denselben Maßstäben wie 1000-Zeilen-Welten klassifizieren.

Konkrete nächste Prüfung:

1. lokale Stresssegmente,
2. lokale Ruhesegmente,
3. längere Kontextwelten,
4. Vergleich der Polachsen Last, Ruhe, Rekopplung und Feldzeit.

Ziel ist eine saubere Trennung zwischen lokaler Feldreaktion und kontextueller Feldzeit.
