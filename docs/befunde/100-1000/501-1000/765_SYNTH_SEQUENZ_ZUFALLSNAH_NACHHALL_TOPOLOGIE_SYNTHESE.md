# SYNTH Sequenz zufallsnah - Nachhall/Topologie-Synthese

Stand: 2026-06-22

## Zweck

Diese Notiz verdichtet die Gegenprobe `SYNTH_ZUFALLSNAH`.

Geprueft wurde dieselbe synthetische Grundwelt `bruch_rand`, aber mit stark veraenderter Phasenfolge:

```text
zweiter_kippimpuls
ruhe_nachhall
oeffnung
rekopplung
randflackern
ruhig_vorlast
gegenpol
bruch_impuls
zweite_rekopplung
```

Damit ist die Pruefung haerter als eine einfache Vertauschung zweier Phasen.
Sie fragt:

```text
Bleibt die MCM-Topologie stabil,
wenn die Weltbausteine in einer zufallsnahen Reihenfolge auftreten?
```

## Datenbasis

- Weltdatei: `data/kontrolliert_synthetic_mcm_sequenz_bruch_rand_zufallsnah_5m.csv`
- Kerzen: `5800`
- Episoden: `5794`
- Trades: `0 -> 0`
- Unique Syntaxsymbole: `167 -> 167`
- Top-Syntax-Ueberlappung: `1.0`
- Top-Familien-Ueberlappung: `1.0`

## Globaler Befund

Die zufallsnahe Sequenz bleibt global stark zentriert:

```text
Zentrum:        0.9517
Offen:          0.0473
Rand/Kipp:      0.0010
Rekopplungsnaehe: 0.2492
```

Damit zerlegt die stark veraenderte Reihenfolge die globale MCM-Topologie nicht.

Die Topologie bleibt:

```text
stark_zentriert_wenig_rand
```

## Rezeptorischer Befund

Die Welt bleibt in der Gesamtaufnahme ruhig genug:

```text
Lautheit:       0.0542
Schaerfe:       0.8031
Rohfeld:        0.0374
Adaptfeld:      0.0333
Reduktion:      0.0041
Adaptionsratio: 0.8909
```

Im Hochlastfenster wird die Welt deutlich offener:

```text
High-Offen:     0.4552
High-Rand/Kipp: 0.0155
High-Lautheit:  0.2138
High-Rohfeld:   0.1272
```

Das ist wichtig:

```text
Die Rezeptorschicht loescht Hochlast nicht.
Sie begrenzt sie so, dass sie als lokale Feldinformation erhalten bleibt.
```

## Lokaler Phasenbefund

Die meisten Phasen werden trotz zufallsnaher Reihenfolge zentrumsnah integriert:

- `ruhe_nachhall`: Zentrum `0.9857`
- `oeffnung`: Zentrum `0.9871`
- `rekopplung`: Zentrum `0.9986`
- `ruhig_vorlast`: Zentrum `0.9943`
- `gegenpol`: Zentrum `0.9600`
- `bruch_impuls`: Zentrum `0.9829`
- `zweite_rekopplung`: Zentrum `0.9873`

Die deutliche Ausnahme bleibt:

```text
randflackern
```

`randflackern` wird lokal offen gelesen:

```text
Zentrum:        0.2643
Offen:          0.5129
Rand/Kipp:      0.0043
Rekopplungsnaehe: 0.2186
```

Damit bleibt die Randphase als lokale Bedeutungsqualitaet sichtbar, auch wenn die globale Topologie stabil bleibt.

## Lesart

Die zufallsnahe Gegenprobe stuetzt drei bisherige Befunde:

1. Die globale MCM-Topologie ist robust.
2. Lokale Bedeutung bleibt phasen- und sequenzsensitiv.
3. Rezeptoradaptation stabilisiert, ohne lokale Reizqualitaet zu vernichten.

Der wichtigste Punkt:

```text
MINI_DIO normalisiert die Welt nicht zu einem neutralen Mittelwert.
Es haelt lokale Unterschiede im Feld lesbar,
waehrend die globale Innenordnung stabil bleibt.
```

## Bedeutung fuer Feldzeit und Nachhall

Diese Pruefung spricht weiter dafuer:

```text
Nachhall ist Kontext, nicht Kontrolle.
Feldzeit ist Integrationsqualitaet, nicht starre Zeitachse.
```

Die vorherige Reihenfolge faerbt lokale Rollen.
Aber eine starke aktuelle Weltphase wie `randflackern` bleibt eigenstaendig feldwirksam.

Das Feld zeigt also keine einfache Kettenreaktion:

```text
Vorzustand -> bestimmt Gegenwart
```

Sondern eher:

```text
Vorzustand + aktuelle Weltwirkung -> lokale Feldrolle
```

## Forschungsgrenze

Dieser Befund beweist keine universelle MCM-Topologie.

Er zeigt aber:

- dieselben Weltbausteine koennen anders sequenziert werden,
- die globale Rollenordnung bleibt trotzdem stabil,
- die lokale Rand-/Offenheitsqualitaet bleibt sichtbar,
- die Rezeptorschicht wirkt als geordnete Aufnahmegrenze,
- die Top-Syntax/Familien reproduzieren sich im Laufvergleich exakt.

## Vorlaeufige Schlussfolgerung

Die zufallsnahe Sequenz ist ein starker Gegenbefund gegen die Annahme, dass MINI_DIO nur eine feste Reihenfolge auswendig liest.

Der passendere Befund lautet:

```text
MINI_DIO liest eine robuste Feldtopologie,
waehrend lokale Rollen durch aktuelle Weltphase,
Vorzustand und Nachhall gefaerbt werden.
```

## Wie es weitergeht

Als naechstes sollte eine reale Sequenzbruch-Gegenprobe folgen. Ziel: pruefen, ob dieselbe Robustheit auch in echten Weltabschnitten mit natuerlichem Bruch, nicht nur in synthetisch gesetzten Phasen, sichtbar bleibt.
