# Befund: lange Weltklassen, Topologie und Laufzeit

Stand: 2026-06-19

## Zweck

Diese Datei haelt zwei Punkte fest:

1. die Laufzeitursache bei langen `world_relative`-Laeufen,
2. den Befund der langen 10k-Weltklassen zur passiven Topologie.

Die Auswertung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Laufzeitbefund

Vor der Korrektur war der Hauptengpass nicht das Schreiben von CSV/JSON und nicht die Topologie-Auswertung.

Das Profil zeigte:

```text
SemanticMemory.action_diagnostics()
SemanticMemory._associative_signal()
SemanticMemory._vector_distance()
```

Diese drei Stellen dominierten den Lauf. MINI_DIO hat pro Tick und Aktion viele Familien im Gedächtnis gegen die aktuelle Sinneslage verglichen, obwohl in passiven Laeufen oft noch kein wirksames Handlungssignal vorhanden war.

Die Korrektur bleibt fachlich klein:

- wenn fuer eine Aktion kein wirksames assoziatives Handlungssignal existiert, wird die teure Distanzsuche uebersprungen,
- die Vektordistanz nutzt die bereits normalisierten Syntaxvektoren direkter.

Gemessener Effekt:

| Lauf | vorher | nachher |
|---|---:|---:|
| 1k Stress | ca. 12.1 s | ca. 2.6 s |
| 2k Sideways | ca. 45.0 s | ca. 8.4 s |

Damit wurde nicht die MCM-Feldmechanik veraendert, sondern eine unnoetig teure Gedächtnissuche entschaerft.

## Lange Weltklassen

Danach wurden drei 10k-Welten unter `world_relative` ausgefuehrt:

| Welt | Kerzen | Episoden | Symbolanzahl |
|---|---:|---:|---:|
| STABLE_2026_10K | 10000 | 9994 | 6854 |
| STRESS_2023_NEG_10K | 10000 | 9994 | 6856 |
| EXPANSION_2023_POS_10K | 10000 | 9994 | 7088 |

Alle drei Welten ergaben denselben passiven Topologiezustand:

```text
zentrum_mit_rand_und_uebergang
```

## Matrixbefund

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| STABLE_2026_10K | 0.8286 | 0.1279 | 0.0435 | 0.6549 | 0.4125 | 0.1763 | 0.8670 |
| STRESS_2023_NEG_10K | 0.8318 | 0.1278 | 0.0404 | 0.6543 | 0.4098 | 0.1760 | 0.8655 |
| EXPANSION_2023_POS_10K | 0.8216 | 0.1390 | 0.0394 | 0.6534 | 0.4097 | 0.1781 | 0.8656 |

## Lesart

Der lange Lauf bestaetigt den bisherigen Kurzbefund:

```text
Die passive Rollenordnung bleibt ueber verschiedene Weltklassen sichtbar.
```

Die Weltklassen veraendern die Anteile, aber sie brechen die Ordnung nicht auf.

Bemerkenswert:

- Stress wird in dieser Aufnahme nicht als Kollaps gelesen.
- Expansion erhoeht leicht die offene Variante.
- Stable und Stress liegen sehr nah beieinander.
- Die Sinnes-MCM-Kopplung bleibt in allen drei langen Welten eng beisammen.

## Bedeutung fuer die MCM-Forschung

Dieser Befund stuetzt die Arbeitshypothese:

```text
MINI_DIO bildet eine passive Innenfeldordnung,
die nicht direkt von festen Symbolnamen abhaengt.
```

Die Topologie wird ueber Rollenqualitaeten gelesen:

- stabile Innenfeldwirkung,
- offene tragende Variante,
- Rand-/Kippnaehe,
- Rekopplung,
- Sinneskopplung.

Das ist keine Aussage, dass eine universelle MCM-Topologie bewiesen ist.
Es ist aber ein staerkerer Befund als ein einzelnes Kurzfenster, weil die Rollenordnung ueber 10k-Welten erhalten bleibt.

## Grenze

Offen bleibt:

- Wiederholung mit frischem Memory ueber mehrere Durchlaeufe,
- andere Assets,
- andere Zeitebenen,
- feste Aufnahme gegen `world_relative`,
- extremere Bruchwelten,
- laengere Jahreswelten.

## Wie es weitergeht

Als naechstes sollte die lange Matrix nicht weiter breit erweitert werden.
Sinnvoller ist eine gezielte Gegenpruefung:

1. dieselben drei 10k-Welten erneut mit frischem Memory laufen lassen,
2. pruefen, ob Zentrum/Offen/Rand-Anteile reproduzierbar nah bleiben,
3. danach erst auf andere Assets oder Jahreswelten gehen.

Das verhindert, dass die Forschung wieder in reine Fragmentanalyse zerfaellt.
