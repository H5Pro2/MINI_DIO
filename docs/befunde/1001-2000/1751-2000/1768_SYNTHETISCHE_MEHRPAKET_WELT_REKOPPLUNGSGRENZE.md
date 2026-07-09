# Synthetische Mehrpaket-Welt: Rekopplungsgrenze trotz wiederholter Kontrastpakete

Stand: 2026-07-08

## Grundfrage

Nach Befund 1767 war sichtbar:

```text
Ein einzelner wirksamer Kontrast kann lokal eine mittlere Übergangsphase öffnen.
Breitere Fenster glätten diese Öffnung aber wieder.
```

Die nächste Frage war:

```text
Verbinden sich mehrere getrennte Kontrastpakete über Feldzeit
zu breiterer rekoppelnder Rollenbildung?
```

## Umsetzung

Der synthetische Welt-Builder wurde um das Preset `rekopplungsbreite_pakete` erweitert.

Dieses Preset enthält drei getrennte Öffnungs-/Varianz-/Rekopplungs-Pakete:

- Paket A mit Öffnung, Varianz und Rekopplung,
- Abstand/Ruhe,
- Paket B mit anderer Richtung und Rekopplung,
- unruhiger Nachhall,
- Paket C mit erneuter Öffnung und Rekopplung,
- ruhige Rückbindung.

Geändert wurde nur die kontrollierte Außenwelt. Die MCM-Feldlogik und die passive Diagnose blieben unverändert.

## Ergebnis

Die lokalen 1000er-Anschlüsse zeigten über drei Varianten:

```text
24 von 24 Fenstern: kompakt_nachhallend
0 mittlere Übergangsphasen
0 verteilt offene Phasen
0 verteilt rekoppelnde Phasen
```

Die breiteren 2000er-Anschlüsse zeigten ebenfalls:

```text
9 von 9 Fenstern: kompakt_nachhallend
```

Damit verbinden sich mehrere formale Kontrastpakete nicht automatisch zu rekoppelnder Rollenbreite.

## Rohwelt-Rücklesung

Die lokalen Fenster lagen im Mittel bei:

- Rollen: `1`,
- Kombinationen: `0`,
- Cross-State: `0`,
- Rekopplung: etwa `0.749`,
- Nachhall: etwa `0.724`,
- leicht steigender Folgeenergie,
- leicht steigender Range,
- fallender Drift.

Die breiteren Fenster lagen ähnlich:

- Rollen: `1`,
- Kombinationen: `0`,
- Rekopplung: etwa `0.751`,
- Nachhall: etwa `0.763`,
- leicht steigender Folgeenergie,
- fallender Drift.

Kurz:

```text
Die Pakete erzeugen hohe Bindung und Nachhall,
aber keine Rollenöffnung.
```

## Deutung

Der Befund ist ein negativer, aber wichtiger Grenzbefund.

Mehrere getrennte Pakete erzeugen keine verteilte Rekopplung, wenn sie für das Feld zu regelmäßig und zu gut rückbindend wirken.

Damit unterscheidet sich diese Welt klar von der lokalen Übergangszone aus 1767:

```text
1767: lokaler Kontrast öffnet kurz mittlere Übergangsbreite.
1768: wiederholte Paketordnung glättet in kompakte Nachhallbindung.
```

Das spricht dafür, dass rekoppelnde Rollenbreite nicht aus Wiederholung allein entsteht. Es braucht offenbar eine Weltlage, die gleichzeitig:

- Rollen öffnet,
- Nachhall hält,
- Rückbindung ermöglicht,
- aber nicht sofort in eine einzige kompakte Rolle zurückführt.

## Bedeutung für MINI_DIO

MINI_DIO liest diese Mehrpaket-Welt nicht als zunehmend komplexe Rollenmatrix, sondern als geordnete Bindungsfolge.

Das ist methodisch wertvoll, weil es gegen eine einfache Annahme spricht:

```text
Mehr synthetische Pakete = mehr Bedeutungsbreite.
```

Stattdessen zeigt sich:

```text
Wiederholte Ordnung kann Rollenbreite auch verhindern,
wenn sie das Feld zu sauber rekoppelt.
```

## Grenze

Diese Prüfung zeigt nicht, dass synthetische rekoppelnde Breite unmöglich ist.

Sie zeigt nur:

```text
Die bisherige Mehrpaket-Konstruktion erzeugt Bindung,
aber keine verteilte Rollenöffnung.
```
