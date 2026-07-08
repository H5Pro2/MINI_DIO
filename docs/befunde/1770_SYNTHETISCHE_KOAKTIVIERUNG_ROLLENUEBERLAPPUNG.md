# Synthetische Koaktivierung: lokale Rollenüberlappung

Stand: 2026-07-08

## Grundfrage

Nach Befund 1769 war die Trennung sichtbar:

```text
Mehr Syntax erzeugt nicht automatisch mehr topologische Rollenbreite.
```

Die nächste Unterprüfung war deshalb:

```text
Öffnet sich Rollenbreite eher dann,
wenn mehrere Milieus zeitlich nah koaktiv werden
und nicht nur nacheinander als Pakete erscheinen?
```

## Umsetzung

Der synthetische Welt-Builder wurde um das Preset `rekopplungsbreite_koaktiv` erweitert.

Die Welt enthält:

- eine ruhige Startphase,
- einen zentrumsnahen Puls,
- eine offene Überlagerung,
- eine Gegenpol-Überlagerung,
- koaktive Berührung,
- versetzte Rekopplung,
- eine zweite koaktive Berührung,
- späte Bindung,
- ruhige Rückbindung.

Geändert wurde die kontrollierte Außenwelt. Die MCM-Feldlogik blieb unverändert.

## Ergebnis

Die 1000er-Fenster über drei Varianten zeigten:

```text
24 Fenster gesamt
22 kompakt_nachhallend
2 mittlere_uebergangsphase
0 verteilt_offen
0 verteilt_rekoppelnd
```

Die beiden geöffneten Fenster lagen in:

```text
SYN1770_A_1000_2000
SYN1770_B_1000_2000
```

Beide zeigten:

```text
3 Rollen
3 Kombinationen
Cross-State 2
mittlere_uebergangsphase
```

Variante C blieb in denselben Fensterlogiken kompakt.

## Breite Fenster

Die 2000er-Gegenprüfung bestätigte den lokalen Befund:

```text
9 Fenster gesamt
7 kompakt_nachhallend
2 mittlere_uebergangsphase
```

Auch dort öffneten nur A und B im frühen Anschluss:

```text
SYN1770_A_0_2000
SYN1770_B_0_2000
```

Damit ist die Rollenöffnung nicht nur ein einzelner 1000er-Zufall, aber auch keine globale Eigenschaft der ganzen Welt.

## Rohwelt-Rücklesung

Die Klassenmittel zeigen den Unterschied scharf:

`kompakt_nachhallend`:

- Rollen: `1`,
- Kombinationen: `0`,
- Cross-State: `0`,
- Folgewelt-Energie fällt im Mittel,
- Range fällt oder bleibt gedämpft,
- Drift wird nicht als Rollenöffnung gelesen.

`mittlere_uebergangsphase`:

- Rollen: `3`,
- Kombinationen: `3`,
- Cross-State: `2`,
- Folgewelt-Energie steigt deutlich,
- Folgewelt-Range steigt deutlich,
- Drift geht gleichzeitig zurück,
- adaptive Rekopplung steigt gegenüber der Basisrekopplung.

Kurz:

```text
Rollenüberlappung entsteht dort,
wo steigende Folgeenergie und steigende Range
mit fallender Drift und erhöhter adaptiver Rekopplung zusammenfallen.
```

## Deutung

Die Koaktivierungswelt bringt einen Mehrwert gegenüber 1768 und 1769:

- wiederholte Pakete allein öffnen nicht,
- Versatz und mehr Syntax allein öffnen nicht,
- koaktive Nähe kann lokal öffnen.

Die Öffnung bleibt aber begrenzt:

```text
Koaktivierung erzeugt lokale mittlere Übergangsphasen,
aber noch keine verteilte rekoppelnde Rollenbreite.
```

Damit wird die nächste Grenze klarer:

```text
Für verteilte Rekopplung reicht nicht,
dass Rollen kurz gemeinsam auftauchen.
Sie müssen als über mehrere Weltabschnitte tragfähiges Milieu
gleichzeitig breit und rekoppelnd gehalten werden.
```

## Bedeutung für MINI_DIO

MINI_DIO trennt hier drei Ebenen:

- Syntaxmenge,
- lokale Rollenöffnung,
- verteilte rekoppelnde Rollenbreite.

Das ist wichtig, weil das Feld dadurch nicht jede erhöhte Komplexität sofort als tiefere Bedeutung liest.

Die aktuelle Lesung lautet:

```text
Koaktivierung ist ein Kandidat für Rollenöffnung.
Verteilte Rekopplung braucht zusätzlich tragende Milieubindung.
```

## Grenze

Dieser Befund gilt für die geprüften synthetischen Koaktivierungswelten A, B und C.

Er beweist nicht, dass verteilte Rekopplung nur über Koaktivierung entstehen kann. Er zeigt aber, dass Koaktivierung gegenüber reiner Paketfolge und reiner Syntaxvarianz näher an Rollenöffnung liegt.

## Wie es weitergeht

Als nächstes sollte die geöffnete A/B-Zone mit realen rekoppelnden PAXG-Abschnitten verglichen werden. Entscheidend ist, ob dort ähnliche Rohweltbedingungen auftreten oder ob reale verteilte Rekopplung zusätzlich eine andere Milieuqualität trägt.
