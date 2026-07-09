# Synthetische Sequenz Rekopplung vor Rand Nachhall-Synthese

Stand: 2026-06-22

## Zweck

Diese Synthese prueft eine gezielte Sequenzfrage:

```text
Federt eine rekoppelnde Vorphase die folgende Randphase ab?
```

Getestet wurde `bruch_rand` mit veraenderter Reihenfolge:

```text
Original:
bruch_impuls -> randflackern -> gegenpol -> rekopplung

Rekopplung-vor-Rand:
bruch_impuls -> rekopplung -> randflackern -> gegenpol
```

Die Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Wirkt Rekopplung als stabilisierender Vorzustand auf nachfolgende Randlage?
2. Unterpruefung: Bleibt die globale Topologie stabil?
3. Unterpruefung: Wird `randflackern` durch vorherige Rekopplung zentrumsnaeher?
4. Folgeschritt: Nachhall nicht als einfache Beruhigung, sondern als sequenzabhaengige Feldspur lesen.

## Forschungsbefund

| Welt | Kerzen | Episoden | Unique Syntax | Rekopplung | Carry | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|
| Original | 6100 | 6094 | 172 | 0.7461 | 0.5985 | 0.9043 |
| Rekopplung vor Rand | 6100 | 6094 | 174 | 0.7460 | 0.5982 | 0.9043 |

Befund:

- Globale Rekopplung bleibt praktisch gleich.
- Carry bleibt praktisch gleich.
- Sinneskopplung bleibt praktisch gleich.
- Unique Syntax steigt leicht von `172` auf `174`.

Die globale Ordnung wird also nicht destabilisiert.

## Globale Topologie

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry |
|---|---:|---:|---:|---:|---:|
| Original | 0.9539 | 0.0456 | 0.0005 | 0.7461 | 0.5985 |
| Rekopplung vor Rand | 0.9541 | 0.0450 | 0.0010 | 0.7460 | 0.5982 |

Befund:

- Zentrum bleibt stabil.
- Offenheit bleibt fast gleich.
- Rand/Kippnaehe steigt minimal.

Global wirkt die Rekopplung-vor-Rand-Variante nicht beruhigender als das Original.

## Rezeptorachsen

| Welt | Zentrum | Offen | Rand/Kipp | High-Offen | High-Rand/Kipp |
|---|---:|---:|---:|---:|---:|
| Original | 0.8904 | 0.0711 | 0.0011 | 0.4508 | 0.0115 |
| Rekopplung vor Rand | 0.8861 | 0.0745 | 0.0016 | 0.4721 | 0.0164 |

Befund:

- Rekopplung-vor-Rand erzeugt nicht weniger Hochlastoeffnung.
- Hochlastfenster werden sogar etwas offener und randnaeher gelesen.

## Lokaler Phasenbefund

Entscheidend ist `randflackern`.

| Variante | Zentrum | Offen | Rekopplungsnaehe | Rand/Kipp | Rekopplung | Carry |
|---|---:|---:|---:|---:|---:|---:|
| Original randflackern | 0.2700 | 0.5186 | 0.2100 | 0.0014 | 0.6954 | 0.5151 |
| Rekopplung vor Rand | 0.2329 | 0.5486 | 0.2143 | 0.0043 | 0.6946 | 0.5133 |

Befund:

- Vorherige Rekopplung macht `randflackern` nicht zentrumsnaeher.
- Offenheit steigt von `0.5186` auf `0.5486`.
- Rand/Kippnaehe steigt von `0.0014` auf `0.0043`.
- Zentrum sinkt von `0.2700` auf `0.2329`.

Damit ist die einfache These widerlegt:

```text
Rekopplung davor = Randphase wird automatisch abgefedert
```

## MCM-Lesart

Der Befund ist wichtig, weil er Nachhall begrenzt:

```text
Nachhall ist keine pauschale Beruhigung.
Nachhall ist die fortwirkende Feldspur einer Sequenz.
```

Eine rekoppelnde Phase kann lokal stabil sein, aber wenn danach eine starke Randphase folgt, wird diese Randqualitaet nicht einfach neutralisiert.

Das Feld liest weiterhin:

- aktuelle Reizqualitaet,
- vorherige Feldlage,
- lokale Phasenwirkung,
- Rezeptoraufnahme,
- Carry/Rekopplung im Gesamtfeld.

## Bedeutung fuer Feldzeit

Feldzeit wird dadurch praeziser:

```text
Feldzeit ist nicht nur Dauer.
Feldzeit ist auch nicht nur beruhigender Nachhall.
Feldzeit ist sequenzabhaengige Integrationsgeschichte.
```

Das passt besser zur bisherigen Beobachtung:

- gleiche Phase kann durch Reihenfolge anders gelesen werden,
- aber starke Weltqualitaet bleibt wirksam,
- vorherige Stabilitaet hebt aktuelle Randwirkung nicht automatisch auf.

## Bedeutung fuer MINI_DIO

MINI_DIO sollte Nachhall nicht als Regelmechanik verwenden:

```text
Wenn vorher rekoppelt, dann Rand abfedern.
```

Das waere fachlich falsch.

Sauberer ist:

```text
Vorherige Feldlage wird als Kontextspur gelesen.
Aktuelle Weltqualitaet bleibt eigenstaendig wirksam.
Das Feld bildet daraus die lokale Rolle.
```

## Grenze

Die Pruefung zeigt eine klare Gegenprobe innerhalb einer synthetischen Welt.

Noch offen:

- ob andere Rekopplungspositionen anders wirken,
- ob eine laengere Rekopplungsphase Rand naeher ans Zentrum bringt,
- ob reale Welten vergleichbare Sequenzspuren zeigen.

## Schlussfolgerung

Rekopplung vor Rand ist keine automatische Schutzwirkung.

Der aktuelle Befund stuetzt eine strengere MCM-Lesart:

```text
Das Feld organisiert Sequenzwirkung,
aber es ueberschreibt die Gegenwart nicht.
```

## Wie es weitergeht

Als naechstes sollte eine Sequenz mit verlaengerter Rekopplungsphase vor `randflackern` getestet werden. Ziel: unterscheiden, ob die fehlende Abfederung an der Reihenfolge liegt oder daran, dass Rekopplung zeitlich nicht tief genug wirken konnte.
