# Synthetische Sequenz lange Rekopplung vor Rand Nachhall-Synthese

Stand: 2026-06-22

## Zweck

Diese Synthese prueft die praezisierte Nachhallfrage:

```text
Kann eine laengere rekoppelnde Vorphase die folgende Randphase abfedern?
```

Gegenueber dem vorherigen Test wurde `rekopplung` vor `randflackern` nicht nur verschoben, sondern verlaengert:

```text
rekopplung = 2100 Episoden
randflackern = 700 Episoden
```

Die Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Braucht Rekopplung zeitliche Tiefe, um auf Randfolgen zu wirken?
2. Unterpruefung: Verbessert lange Rekopplung globale Topologie und Carry?
3. Unterpruefung: Wird die nachfolgende Randphase lokal abgefedert?
4. Folgeschritt: Unterschied zwischen globaler Feldstabilisierung und lokaler Randwirkung festhalten.

## Forschungsbefund

| Welt | Kerzen | Episoden | Unique Syntax | Rekopplung | Carry | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|
| Original | 6100 | 6094 | 172 | 0.7461 | 0.5985 | 0.9043 |
| Kurze Rekopplung vor Rand | 6100 | 6094 | 174 | 0.7460 | 0.5982 | 0.9043 |
| Lange Rekopplung vor Rand | 7500 | 7494 | 175 | 0.7485 | 0.6030 | 0.9063 |

Befund:

- Lange Rekopplung erhoeht globale Rekopplung.
- Lange Rekopplung erhoeht globale Tragqualitaet.
- Lange Rekopplung erhoeht Sinneskopplung leicht.
- Die Top-Syntax bleibt stabil reproduzierbar.

Global wirkt lange Rekopplung also stabilisierend.

## Globale Topologie

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry |
|---|---:|---:|---:|---:|---:|
| Original | 0.9539 | 0.0456 | 0.0005 | 0.7461 | 0.5985 |
| Lange Rekopplung vor Rand | 0.9590 | 0.0403 | 0.0007 | 0.7485 | 0.6030 |

Befund:

- Zentrum steigt.
- Offenheit sinkt.
- Rand/Kippnaehe steigt minimal, bleibt aber sehr klein.

Globale Lesart:

```text
Laengere Rekopplung verbessert die Gesamtintegration.
```

## Rezeptorachsen

| Welt | Zentrum | Offen | Rand/Kipp | High-Offen | High-Rand/Kipp |
|---|---:|---:|---:|---:|---:|
| Original | 0.8904 | 0.0711 | 0.0011 | 0.4508 | 0.0115 |
| Lange Rekopplung vor Rand | 0.9082 | 0.0606 | 0.0013 | 0.4307 | 0.0133 |

Befund:

- Zentrum steigt auch in der Rezeptorachsenlesung.
- Offenheit sinkt.
- Hochlast-Offenheit sinkt.
- Hochlast-Rand/Kipp steigt minimal.

Auch hier wirkt die lange Rekopplung eher global tragend.

## Lokaler Phasenbefund

Entscheidend bleibt `randflackern`.

| Variante | Zentrum | Offen | Rekopplungsnaehe | Rand/Kipp | Rekopplung | Carry |
|---|---:|---:|---:|---:|---:|---:|
| Original randflackern | 0.2700 | 0.5186 | 0.2100 | 0.0014 | 0.6954 | 0.5151 |
| Kurze Rekopplung vor Rand | 0.2329 | 0.5486 | 0.2143 | 0.0043 | 0.6946 | 0.5133 |
| Lange Rekopplung vor Rand | 0.2557 | 0.5371 | 0.2029 | 0.0043 | 0.6931 | 0.5137 |

Befund:

- Lange Rekopplung ist besser als kurze Rekopplung direkt vor Rand.
- Aber lange Rekopplung ist lokal nicht besser als das Original.
- `randflackern` bleibt offen dominant.
- Rand/Kippnaehe bleibt gegenueber Original erhoeht.

Damit gilt:

```text
Laengere Rekopplung stabilisiert das Gesamtfeld,
aber sie neutralisiert die lokale Randqualitaet nicht.
```

## MCM-Lesart

Der Befund trennt zwei Ebenen:

### Globale Feldlage

Lange Rekopplung kann das Gesamtfeld tragfaehiger machen.

```text
mehr Zentrum
mehr Carry
mehr Sinneskopplung
```

### Lokale Randlage

Die folgende Randphase bleibt eine Randphase.

```text
aktuelle Randqualitaet bleibt wirksam
auch wenn vorher Rekopplung aufgebaut wurde
```

Das ist fachlich wichtig:

```text
Nachhall beeinflusst Wahrnehmung,
aber ersetzt nicht den aktuellen Weltkontakt.
```

## Feldzeit-Folgerung

Feldzeit ist hier nicht einfach Schutz.

Praeziser:

```text
Feldzeit traegt Integrationsgeschichte.
Diese Geschichte kann das Gesamtfeld stabilisieren.
Aber die aktuelle Weltphase bleibt als eigene Wirkung lesbar.
```

Damit wird die Feldzeit-Mechanik robuster:

- Dauer kann Integration erhoehen.
- Sequenz kann lokale Rollen veraendern.
- Vorzustand kann Kontext geben.
- Gegenwart bleibt eigenstaendig.

## Bedeutung fuer MINI_DIO

MINI_DIO sollte spaeter nicht lernen:

```text
Ich war vorher stabil, also ist der naechste Rand harmlos.
```

Sauberer ist:

```text
Ich war vorher stabil.
Jetzt kommt Randwirkung.
Ich lese beides: Vorzustand und aktuelle Wirkung.
```

Das verhindert eine falsche Ueberberuhigung.

## Grenze

Diese Pruefung ist synthetisch.

Gesichert im aktuellen Test:

- lange Rekopplung verbessert globale Feldintegration,
- lokale Randphase bleibt offen,
- Abfederung ist begrenzt und nicht automatisch.

Noch offen:

- ob eine noch laengere Rekopplung anders wirkt,
- ob mehrere Rekopplungsphasen vor Rand eine andere Wirkung zeigen,
- ob reale Weltfolgen dieselbe Trennung zeigen.

## Schlussfolgerung

Die Nachhall-Hypothese wird dadurch praeziser:

```text
Nachhall ist Kontext,
nicht Kontrolle.
```

Und fuer Feldzeit:

```text
Feldzeit speichert Integrationsgeschichte,
aber die Gegenwart bleibt feldwirksam.
```

## Wie es weitergeht

Als naechstes sollte keine weitere einfache Rekopplungslaenge getestet werden. Sinnvoller ist jetzt eine Gesamtkarte der Sequenzbefunde: Original, Rand-vor-Bruch, kurze Rekopplung-vor-Rand und lange Rekopplung-vor-Rand. Ziel: eine klare Mechanik von Nachhall, Gegenwart und Feldzeit dokumentieren.
