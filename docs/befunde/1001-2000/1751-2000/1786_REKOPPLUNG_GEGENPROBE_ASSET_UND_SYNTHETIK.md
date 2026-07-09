# 1786 - Rekopplung: Gegenprobe über Assets und synthetische Kontrolle

## Grundfrage

Nach 1785 war sichtbar, dass BTC und PAXG beide eine rekoppelnde Feldfunktion zeigen, aber in unterschiedlicher Ausprägung. Die nächste Frage war, ob `verteilt_rekoppelnd` einfach durch Rollenbreite, Datenrauschen oder synthetische Wiederholung entsteht.

## Prüfung

Zusammengeführt wurden vorhandene passive Reports:

- BTC/PAXG-Rekopplungssignatur aus 1785
- BTC/DOGE/XRP 2025 Late-5m
- BTC/DOGE/XRP 2025 1h
- synthetische Randrollen- und Nullkontrolle

Die Prüfung bleibt passiv. Es wird keine Handlung, keine Richtung und keine feste Regel daraus abgeleitet.

## Ergebnis

| Bereich | Befund |
|---|---|
| PAXG | stärkste breite Rekopplung |
| BTC | lokale, zeitmaßabhängige Rekopplung |
| DOGE | Rollenatmung, aber keine stabile Rekopplung |
| XRP | hohe Rollenbreite, aber offen verteilt |
| synthetische Kontrolle | kompakt nachhallend, keine rekoppelnde Breite |

Wichtig: XRP erreicht in den Late-5m-Fenstern hohe Rollen- und Kombinationsbreite, bleibt aber `verteilt_offen`. Die synthetische Kontrolle bleibt trotz strukturierter Sequenzen kompakt nachhallend.

## Interpretation

`verteilt_rekoppelnd` wirkt dadurch selektiv:

```text
Rollenbreite allein
  -> reicht nicht

synthetische Wiederholung
  -> reicht nicht

hoher Nachhall allein
  -> reicht nicht

Breite + Rückbindung + passende Weltspannung
  -> kann rekoppelnde Feldfunktion bilden
```

Damit wird die bisherige Pareidolie-Gegenprüfung stärker: Die rekoppelnde Klasse taucht nicht überall dort auf, wo viele Rollen, viele Kombinationen oder synthetische Muster vorhanden sind. Sie erscheint in den bisherigen Daten nur dort, wo mehrere Feldqualitäten gemeinsam tragen.

## Bedeutung für die MCM-Forschung

Der Befund spricht dafür, dass MINI_DIO nicht nur "mehr Struktur" misst, sondern zwischen unterschiedlichen Feldfunktionen unterscheidet:

- offene Breite
- kompakte Nachhallbindung
- lokale Zeitmaßrekopplung
- breite Rekopplung

Das ist relevant, weil ein MCM-Feld dadurch nicht als starre Symboltabelle gelesen werden muss, sondern als dynamisches Bedeutungsfeld mit verschiedenen Bindungsformen.

## Grenze

Das ist kein Beweis für eine allgemeine Gesetzmäßigkeit. Die Aussage ist enger: In den bisher geprüften Welten tritt rekoppelnde Breite selektiv auf und bleibt gegen DOGE/XRP-Offenheit sowie synthetische Kompaktheit unterscheidbar.

## Artefakte

- `reports/rekopplung_gegenprobe_asset_synthese_matrix.csv`
- `reports/rekopplung_gegenprobe_asset_synthese_matrix.md`

## Wie es weitergeht

Als nächstes sollte gezielt ein weiteres Asset oder eine neu gebaute synthetische Welt geprüft werden, die nicht nur kompakt nachhallt, sondern kontrolliert Breite plus Nachhall erzeugt. Ziel ist zu sehen, ob Rekopplung künstlich provoziert werden kann oder ob reale Weltspannung dafür nötig bleibt.
