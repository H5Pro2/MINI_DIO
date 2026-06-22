# Synthetische Welten nach adaptierter Feldkopplung - Synthese

## Fragestellung

Bleibt die synthetische Topologie-Differenzierung erhalten, wenn MCM-Feldspannung nicht mehr Rohfeldaufnahme, sondern adaptierte Feldaufnahme liest?

## Ergebnis

Ja. Die Differenzierung bleibt erhalten, aber Rand/Kipp wird sauberer begrenzt.

## Vergleich der auffaelligen Phasen

| Welt | Phase | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Rohfeld |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Harmonie | `kippnaehe` | 0.9556 | 0.0178 | 0.0011 | 0.0256 | 0.7511 | 0.6072 | 0.1188 | 0.0279 |
| Bruch/Rand | `randflackern` | 0.2729 | 0.5157 | 0.0014 | 0.2100 | 0.6957 | 0.5155 | 0.1511 | 0.0938 |
| Randdominanz | `laute_randphase` | 0.0650 | 0.7613 | 0.0288 | 0.1450 | 0.6729 | 0.4874 | 0.1792 | 0.1644 |

## Befund

Die Ordnung bleibt abgestuft:

```text
Harmonie
  -> fast reine Zentrumnaehe

Bruch/Rand
  -> lokale Oeffnung, wenig Rand/Kipp

Randdominanz
  -> starke lokale Oeffnung, sichtbare Rand/Kipp-Naehe, danach Rekopplung
```

Die wichtigste Veraenderung gegenueber der Rohkopplung:

```text
Rand/Kipp wird weniger direkt von Rohlast getrieben.
```

Das Feld liest die Belastung weiterhin, aber nicht mehr als ungefilterte Rohspannung.

## Mechanische Bedeutung

Die Korrektur verbessert die fachliche Trennung:

- Rohfeldaufnahme beschreibt, was die Welt an Last anbietet.
- Adaptierte Feldaufnahme beschreibt, was die Rezeptorschicht ins Feld laesst.
- MCM-Spannung liest die adaptierte Feldaufnahme.
- Topologie liest damit Innenfeldwirkung, nicht Rohdatenlast.

## Schluss

Die Topologie ist durch die Korrektur nicht verschwunden.

Sie wirkt eher sauberer:

```text
Das Feld bleibt empfindlich fuer Weltspannung,
aber Randlast wird nicht mehr direkt aus Rohlast erzeugt.
```

Damit ist die adaptierte Feldkopplung aktuell der bessere MCM-konforme Mechanikstand.

Wie es weitergeht: Als naechstes sollte die alte Formulierung in bestehenden Berichten nicht ueberschrieben, aber als historisch markiert werden: Befunde vor `683_ADAPTIERTE_FELDKOPPLUNG_UMSETZUNG.md` koennen Roh- und Feldspannung noch staerker vermischen.
