# REAL SOL 2025 - Bruch vs Ruhe Feldzeit-Vergleich

Stand: 2026-06-23

## Zweck

Diese Notiz vergleicht zwei echte SOL-2025-5m-Fenster aus derselben Quelle:

1. reales Bruch-/Stressfenster,
2. rohweltlich ruhigeres Gegenfenster.

Ziel ist die Frage:

```text
Unterscheidet MINI_DIO ruhige und belastete Weltabschnitte nur nach Rohlautstaerke,
oder entsteht eine eigene Innenfeldlesung aus Rezeptoraufnahme, Topologie, Feldzeit und Nachhall?
```

## Weltvergleich Rohdaten

| Welt | Start | Ende | Drift | Max Drawdown | Max Abs Return | Avg Abs Return |
|---|---:|---:|---:|---:|---:|---:|
| Bruch | 80250 | 82250 | -0.1704 | 0.2716 | 0.1056 | 0.002284 |
| Ruhe | 52250 | 54250 | 0.0062 | 0.0694 | 0.0087 | 0.001152 |

Rohweltlich ist der Unterschied klar:

```text
Bruch = deutlich belasteter.
Ruhe  = deutlich ruhiger.
```

## Forschungskette

| Welt | Unique Syntax | Episodenmemory | Rekopplung | Carry | Sinnes-MCM-Kopplung |
|---|---:|---:|---:|---:|---:|
| Bruch | 362 | 7 | 0.6958 | 0.5118 | 0.8437 |
| Ruhe | 337 | 3 | 0.6940 | 0.5101 | 0.8396 |

Beide Welten reproduzieren intern exakt:

```text
Top-Syntax-Ueberlappung = 1.0
Top-Familien-Ueberlappung = 1.0
```

Der Bruchabschnitt bildet mehr Syntaxvielfalt und mehr geschriebene Episodenmemory.
Das ruhige Fenster schreibt weniger Memory, ist aber nicht automatisch rekoppelnder.

## MCM-Wirkungsklassen

| Welt | Stabil | Tragend unruhig | Kippend | Gespannt |
|---|---:|---:|---:|---:|
| Bruch | 1624 | 348 | 19 | 3 |
| Ruhe | 1536 | 437 | 20 | 1 |

Der Bruch ist nicht einfach global chaotischer.
Das ruhige Fenster zeigt sogar mehr `tragend_unruhig`.

Das ist ein wichtiger Befund:

```text
Rohweltliche Ruhe ist nicht identisch mit Innenfeldruhe.
```

## Rezeptorachsen

| Welt | Zentrum | Offen | Rand/Kipp | Lautheit | Rohfeld | Adaptfeld | High-Offen | High-Rand/Kipp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bruch | 0.4032 | 0.4122 | 0.0211 | 0.2077 | 0.1240 | 0.1058 | 0.8000 | 0.1950 |
| Ruhe | 0.3661 | 0.4338 | 0.0231 | 0.2143 | 0.1278 | 0.1087 | 0.7750 | 0.2200 |

Die Rezeptorachsen lesen das ruhige Fenster nicht als trivial ruhiger.
Es traegt sogar leicht mehr Offenheit und Rand/Kippnaehe.

Moegliche Lesart:

```text
Die quiet-Extraktion findet rohweltlich geringe Bewegung,
aber das Feld liest weiterhin lokale Uebergangs- und Kontaktspannung.
```

## Rollen-Topologie

| Welt | Topologiezustand | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe |
|---|---|---:|---:|---:|---:|
| Bruch | stark_zentriert_wenig_rand | 0.8144 | 0.1745 | 0.0110 | 0.2503 |
| Ruhe | gemischte_rollenordnung | 0.7703 | 0.2192 | 0.0105 | 0.2503 |

Die Topologie bleibt in beiden Welten lesbar.

Aber:

- Bruch ist zentrumsnaeher als erwartet.
- Ruhe ist offener/gemischter als erwartet.

Das spricht gegen eine zu einfache Gleichung:

```text
ruhige Welt = ruhiges Feld
stressige Welt = instabiles Feld
```

MINI_DIO liest komplexer:

```text
Weltstruktur + Rezeptoraufnahme + Feldnachhall + lokale Uebergangsqualitaet
```

## Kurzsegment-Lesung

| Welt | Lesung | Stable Ratio | Restless Ratio | Strained Ratio | Temporal Transition |
|---|---|---:|---:|---:|---:|
| Bruch | gemischt | 0.8144 | 0.1745 | 0.0110 | 0.4233 |
| Ruhe | gemischt | 0.7703 | 0.2192 | 0.0105 | 0.3872 |

Beide werden als `gemischt` gelesen.

Der Unterschied liegt nicht in einer harten Klasse, sondern in der Feldfaerbung:

- Bruch: mehr temporaler Uebergang, mehr Memory, mehr Syntaxvielfalt.
- Ruhe: weniger Memory, aber mehr offene/tragend unruhige Feldfaerbung.

## Arbeitsbefund

Der Vergleich zeigt:

```text
MINI_DIO unterscheidet Weltabschnitte nicht nur ueber Rohstress.
Das Innenfeld bildet eine eigene Lesung aus Aufnahme, Topologie, Feldzeit und Nachhall.
```

Das ist fachlich relevant, weil es die MCM-Annahme stuetzt:

```text
Das Feld ist keine lineare Kopie der Aussenwelt.
Es ist eine geordnete Innenreaktion auf Weltkontakt.
```

## Grenze

Die Begriffe `Bruch` und `Ruhe` stammen aus der Rohwelt-Extraktion.

Sie sind keine fertigen MCM-Bedeutungen.

Fuer MINI_DIO gilt:

```text
Rohweltlabel beschreiben den Aussenabschnitt.
MCM-Feldwirkung beschreibt die Innenreaktion.
```

Beide muessen getrennt bleiben.

## Vorlaeufige Schlussfolgerung

Der direkte SOL-2025-Vergleich macht den Befund praeziser:

```text
Die Topologie bleibt auch innerhalb derselben Quelle stabil lesbar.
Die Innenfeldfaerbung folgt aber nicht simpel der Rohweltlautstaerke.
```

Das spricht fuer eine echte Rezeptor-/Innenfeldvermittlung:

```text
Aussenwelt wirkt nicht direkt als Feld.
Aussenwelt wird aufgenommen, begrenzt, nachhallend eingebettet
und als MCM-Feldwirkung organisiert.
```

## Wie es weitergeht

Als naechstes sollte die Quiet-Extraktion methodisch verbessert werden. Sie sollte nicht nur geringe Volatilitaet suchen, sondern auch geringe offene/randnahe Innenfeldwirkung nach dem Lauf gegenpruefen. Danach kann eine zweite ruhige Gegenwelt aus SOL 2025 oder BTC 2025 getestet werden.
