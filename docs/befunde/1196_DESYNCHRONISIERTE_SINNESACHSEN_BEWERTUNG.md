# Befund 1196 - Desynchronisierte Sinnesachsen als Haertetest

## Grundfrage

Die Rand-/Kipp-Gegenprobe 1194 zeigte, dass mehr Rohspannung allein keine breite Randdominanz erzeugt. Deshalb wurde ein haerterer Test gebaut:

```text
Nicht die Welt wird nur lauter.
Die Sinnesachsen werden widerspruechlich.
```

Die Testwelt kombiniert ruhige Form mit lauter Energie, klare Form mit leiser Energie, bruechige Bewegung mit gedämpfter Lautheit und lauten Nachhall ohne starke Formbewegung.

## Datengrundlage

- Builder: `data_builder/synthetic_desync_world_builder.py`
- Welt: `data/synthetic_mcm_desync_axes_8500_5m.csv`
- Lauf: `debug/1195_desync_axes/dio_mini_lauf_2/`
- Topologie-Matrix: `docs/befunde/1195_DESYNC_AXES_TOPOLOGIE_MATRIX.md`
- CSV-Matrix: `docs/befunde/1195_DESYNC_AXES_TOPOLOGIE_MATRIX.csv`

Der Lauf wurde mit frischem Memory im Modus `world_relative` ausgefuehrt.

## Messwerte

Der Lauf umfasst:

- Kerzen: `8500`
- Episoden: `8494`
- eindeutige Symbole: `69`
- durchschnittliche Rekopplung: `0.7527`
- durchschnittlicher Carry: `0.6061`
- durchschnittlicher Strain: `0.1260`
- durchschnittliche Sinneskopplung: `0.9108`
- durchschnittlicher Nachhall: `0.7728`
- zeitliche Trust-Stuetze: `0.9265`
- zeitliche Caution-Stuetze: `0.0351`

Passive Innenfeldklassen:

- `stabil`: `8327`
- `tragend_unruhig`: `89`
- `kippend`: `76`
- `gespannt`: `2`

Episode-Memory-Zustaende:

- `field_carried`: `8492`
- `field_strained`: `2`

## Topologische Rollen

| Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|
| `zentrum_stabil` | `0.9803` | `0.7553` | `0.6093` | `0.1231` | `0.9152` |
| `offene_variante` | `0.0105` | `0.6470` | `0.4707` | `0.2458` | `0.7332` |
| `spannungsrand_kippnaehe` | `0.0092` | `0.6006` | `0.4204` | `0.3016` | `0.6475` |

## Bewertung

Die desynchronisierte Welt erzeugt weiterhin keine Feldkollaps-Dominanz. Das Zentrum bleibt sogar sehr stark. Gleichzeitig steigt der messbare Anteil von `spannungsrand_kippnaehe` gegenueber der reinen Rand-/Kipp-Gegenprobe deutlich an:

- Rand-/Kipp-Gegenprobe 1194: `spannungsrand_kippnaehe` ca. `0.0007`
- Desync-Gegenprobe 1196: `spannungsrand_kippnaehe` ca. `0.0092`

Das ist fachlich relevant: Nicht reine Lautstaerke belastet das Feld am staerksten, sondern widerspruechliche Sinnesaufnahme.

## Interpretation

MINI_DIO behandelt die Welt nicht als rohe Datenlast. Das Feld reagiert auf Passung zwischen Sinnesachsen:

- wenn Sehen, Hoeren und Feldwirkung zusammenpassen, entsteht hohe Rekopplung;
- wenn Sinnesachsen widerspruechlich werden, steigt Rand-/Kippnaehe;
- dennoch kann das Feld grosse Teile der Desynchronisation integrieren.

Damit wird die receptorische MCM-Mechanik weiter bestaetigt:

```text
Welt -> Sinnesachsen -> Rezeptorik -> MCM-Feldwirkung
```

Die MCM bekommt nicht alles ungefiltert. Sie bekommt eine bereits receptorisch uebersetzte Feldwirkung. Genau dadurch bleibt Topologie moeglich.

## Bedeutung fuer die 0-Punkt-Hypothese

Die 0-Punkt-Hypothese wird nicht widerlegt. Die Daten sprechen eher dafuer, dass Zentrum und Rand nicht durch absolute Reizstaerke entstehen, sondern durch die Qualitaet der Rekopplung:

- Zentrum: hohe Rekopplung, hoher Carry, niedriger Strain, hohe Sinneskopplung.
- Rand/Kippnaehe: niedrigere Rekopplung, niedrigerer Carry, hoeherer Strain, schwächere Sinneskopplung.

Der 0-Punkt wirkt damit weiter als rueckfuehrende Feldnaehe. Rand entsteht dort, wo die Feldwirkung schlechter integriert werden kann.

## Methodischer Schluss

Die naechste Haertepruefung sollte nicht nur lauter oder laenger sein. Sie sollte gezielt die Sinnesachsen variieren:

1. Sehen stabil, Hoeren chaotisch.
2. Sehen chaotisch, Hoeren stabil.
3. Beide chaotisch, aber Feldspannung niedrig.
4. Beide stabil, aber Feldspannung hoch.

So kann getrennt werden, ob Randnaehe eher aus visueller Unschaerfe, akustischer Uebersteuerung, Rezeptorfehlpassung oder echter Feldspannung entsteht.

## Wie es weitergeht

Als naechstes sollte die Desync-Welt in Teilvarianten zerlegt werden. Zuerst nur `Sehen stabil / Hoeren chaotisch`, danach `Sehen chaotisch / Hoeren stabil`. Erst danach kann sauber gesagt werden, welche Sinnesachse die Randnaehe staerker beeinflusst.
