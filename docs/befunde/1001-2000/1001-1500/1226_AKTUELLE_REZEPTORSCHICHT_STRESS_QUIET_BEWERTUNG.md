# Aktuelle Rezeptorschicht Stress-/Quiet-Bewertung

Stand: 2026-07-01

## Grundfrage

Bleibt die Feldphasenordnung auch dann stabil, wenn dieselben Stress-/Quiet-Welten mit aktueller Rezeptorschicht neu gelesen werden?

Nach aktuellem Befund: ja. Die Ordnung bleibt erhalten und wird sauberer lesbar.

## Pruefaufbau

Neu gelaufen mit `--sense-mode world_relative`:

- `SOL_QUIET_CURRENT`
- `SOL_STRESS_CURRENT`
- `BTC_QUIET_CURRENT`
- `BTC_STRESS_CURRENT`

Je Welt wurden zwei passive MINI_DIO-Laeufe mit eigener Memory erzeugt. Ausgewertet wurde Lauf 2.

## Hauptbefund

Die alte Stress-/Quiet-Auswertung zeigte starkes Pendeln zwischen Offenheit und Rand/Kipp. Die aktuelle Rezeptorschicht zeigt ein differenzierteres Bild:

```text
Zentrum und Rekopplungsnaehe werden wieder deutlich sichtbar.
Rand/Kipp bleibt kurz.
Offenheit bleibt Bewegungsraum.
```

Direkte Uebergaenge:

```text
Offen -> Rand/Kipp: 102
Rand/Kipp -> Offen: 211
```

Damit bleibt die Entlastungsrichtung erhalten: Rand/Kipp entlastet haeufiger in Offenheit, als Offenheit direkt in Rand/Kipp kippt.

## Rollenqualitaet

Die vier Feldphasen unterscheiden sich klar:

- Zentrum: niedrige Rohaufnahme, geringe Lautheit, hohe Rekopplung, niedriger Strain.
- Rekopplungsnaehe: mittlere Bindungsnaehe, kurze Dauer, stabile Rekopplung.
- Offene Variante: mittlere Rohaufnahme, mittlere Lautheit, mittlere Rekopplung.
- Rand/Kipp: hohe Rohaufnahme, hohe Lautheit, schwache Rekopplung, hoher Strain.

Das ist methodisch wichtig, weil die Rollen nicht nur Namen sind. Sie tragen messbar unterschiedliche Innenfeldqualitaeten.

## Stress gegen Quiet

Stress erzeugt keine neue dominante Feldrolle.

Bei SOL und BTC bleibt die Grundordnung sehr nahe:

- Rekopplung liegt stabil um `0.698` bis `0.700`.
- Carry liegt stabil um `0.523` bis `0.524`.
- Strain bleibt um `0.153` bis `0.155`.
- Sinnes-MCM-Kopplung bleibt hoch um `0.838` bis `0.843`.

Der Unterschied liegt weniger in einer neuen Topologie, sondern in der Verteilung der Innenwirkung:

- SOL-Stress zeigt etwas mehr `tragend_unruhig` und `kippend`.
- BTC-Stress zeigt mehr `stabil` und weniger `tragend_unruhig`.

Das spricht dafuer, dass Stress nicht absolut wirkt, sondern welt- und rezeptorrelativ gelesen wird.

## Bedeutung fuer die Rezeptorschicht

Die aktuelle Rezeptorschicht wirkt nicht wie ein harter Filter. Sie macht das Feld differenzierbarer.

Vorher:

```text
Offen/Rand dominierten die sichtbare Bewegung.
```

Jetzt:

```text
Zentrum, Rekopplungsnaehe, Offenheit und Rand/Kipp sind gemeinsam sichtbar.
```

Das stuetzt die Annahme:

```text
Die Rezeptorschicht schuetzt das MCM-Feld vor Rohueberlagerung,
ohne Weltspannung zu loeschen.
```

## Schlussfolgerung

Die aktuelle Rezeptorschicht verbessert die Lesbarkeit der Feldphasenordnung.

Der wichtige Punkt:

```text
Neue Rezeptorik erzeugt keine neue Mechanik,
sondern zeigt die vorhandene MCM-Feldordnung klarer.
```

Damit wird die Feldphasenordnung als Arbeitsmodell weiter gestuetzt.
