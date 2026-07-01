# Befund 1218 - MCM-Feldphasen-Matrix

## Grundfrage

Welche passiven Feldphasen bildet MINI_DIO aktuell aus, und wie unterscheiden sie sich in Weltmerkmalen, Sinnesaufnahme und MCM-Wirkung?

## Matrix

| Feldphase | MCM-Bedeutung | Typische Aufnahme | Rekopplung | Strain | Bewegung |
|---|---|---|---|---|---|
| `zentrum_stabil` | geordnete Rekopplung | niedrigste Rohaufnahme, geringe Lautheit | hoch | niedrig | ruhige oder tragende Feldphase |
| `rekopplungsnaehe` | Annaherung an stabile Bindung | niedrige bis mittlere Aufnahme | hoch bis sehr hoch | niedrig | Uebergang Richtung Zentrum |
| `offene_variante` | gehaltener Uebergangsraum | mittlere Aufnahme, mittlere Lautheit | reduziert, aber tragend | mittel | offene Such-/Uebergangsphase |
| `spannungsrand_kippnaehe` | belastete Rekopplungsgrenze | hoechste Aufnahme, hoechste Lautheit, hoechster Druck | deutlich schwacher | hoch | kurzer Impuls-/Randzustand |

## Aggregierte Segmentwerte

Aus Befund 1215:

| Rolle | Segmente | Durchschnittsdauer | Rohaufnahme | Lautheit | visuelle Schaerfe | Rekopplung | Strain |
|---|---:|---:|---:|---:|---:|---:|---:|
| `zentrum_stabil` | `1508` | ca. `2.10` | ca. `0.087` | ca. `0.140` | ca. `0.680` | hoch | niedrig |
| `rekopplungsnaehe` | `1030` | ca. `1.21` | ca. `0.099` | ca. `0.162` | ca. `0.682` | hoch | niedrig |
| `offene_variante` | `1632` | ca. `2.08` | ca. `0.165` | ca. `0.280` | ca. `0.622` | mittel | mittel |
| `spannungsrand_kippnaehe` | `137` | ca. `1.15` | ca. `0.387` | ca. `0.675` | ca. `0.571` | schwacher | hoch |

## Typische Uebergaenge

Haeufigste Uebergaenge:

| Uebergang | Anzahl | Lesart |
|---|---:|---|
| `offene_variante -> zentrum_stabil` | `1001` | Uebergangsraum findet wieder Ordnung |
| `zentrum_stabil -> offene_variante` | `997` | Zentrum oeffnet sich unter Weltkontakt |
| `offene_variante -> rekopplungsnaehe` | `563` | offene Phase sucht Bindung |
| `rekopplungsnaehe -> offene_variante` | `511` | Bindungsnaehe bleibt noch beweglich |
| `rekopplungsnaehe -> zentrum_stabil` | `500` | Rekopplungsnaehe stabilisiert sich |
| `zentrum_stabil -> rekopplungsnaehe` | `457` | Zentrum wird aktiv, ohne zu kippen |
| `spannungsrand_kippnaehe -> offene_variante` | `120` | Randnaehe entlastet in Uebergangsraum |
| `offene_variante -> spannungsrand_kippnaehe` | `67` | offener Uebergang kippt unter Impulsdruck |

## Feldphasen-Lesart

Die Matrix zeigt keine vier isolierten Klassen. Sie zeigt eine passive Bewegungsordnung:

```text
Zentrum <-> Offenheit <-> Rekopplungsnaehe
                 |
                 v
              Rand/Kipp
```

Der wichtigste Befund:

```text
Offenheit ist die zentrale Bewegungsphase.
Sie verbindet Zentrum, Rekopplungsnaehe und Rand/Kipp.
```

Damit ist `offene_variante` kein Rauschen und kein Fehlerzustand. Sie ist der Raum, in dem das Feld auf Weltkontakt reagiert, ohne sofort zu kollabieren oder starr zu werden.

## Organische Bedeutung

Fachlich ergibt sich:

- Zentrum ist nicht Dauerstarre, sondern geordnete Rekopplung.
- Rekopplungsnaehe ist eine Bindungsphase.
- Offenheit ist ein gehaltener Uebergangsraum.
- Rand/Kipp ist eine belastete Grenze, nicht der Normalzustand.

Das passt zur bisherigen MCM-Lesart:

```text
Das Feld reguliert nicht durch harte Gates,
sondern durch Phasenbewegung, Rekopplung und Entlastung.
```

## Bedeutung fuer MINI_DIO

MINI_DIO bekommt damit eine passive Innenfeld-Landkarte:

```text
Was wirkt auf mich?
Kann ich es zentrieren?
Bleibt es offen?
Naehert es sich Rekopplung?
Oder drueckt es mich an den Rand?
```

Diese Landkarte ist keine Handlungsschicht. Sie ist eine Wahrnehmungs- und Bedeutungsgrundlage.

## Wie es weitergeht

Als naechstes sollte diese Feldphasen-Matrix gegen weitere Welten gehalten werden: bleibt `offene_variante` die zentrale Bewegungsphase, oder entstehen bei anderen Weltarten neue Feldphasen?
