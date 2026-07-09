# 2075 - rf_05 unter komponentenisolierten Kontrollen

## Zweck

Befund 2074 zeigte eine klare Kontrollasymmetrie: `rf_05` lag über vollständigem Shape-Shuffle, aber unter Random Sign. Dieser Versuch trennt Körperrichtung, Körpergröße, Dochte und Volumen, um die tragende relationale Komponente enger einzugrenzen.

## Methode

- identische zwölf 2024-Holdoutfenster aus 2074
- Referenzen aus 2074: Realwelt, vollständiges Shape-Shuffle und Random Sign
- vier neue Komponenten-Kontrollen pro Realfenster
- `48` neue Kontrollläufe mit jeweils frischer episodischer Memory
- unveränderte acht Mitglieder von `rf_05`
- Wahrnehmungsmodus: `world_relative`
- Archiv der neuen Komponenten-Kontrollen: `data/2075_rf05_component_controls.zip`
- keine neue Klasse, keine Handlung, kein Gate und keine Richtung

Kontrollformen:

- `sign_shuffle`: permutiert nur die Körpervorzeichen und erhält deren Gesamtverteilung
- `magnitude_shuffle`: permutiert nur die absoluten Körpergrößen und erhält die Richtungsfolge
- `wick_shuffle`: permutiert nur die Paare aus oberem und unterem Docht
- `volume_shuffle`: permutiert nur die Volumenfolge
- `shuffle`: permutiert vollständige lokale Kerzenformen samt Volumen
- `random_sign`: setzt Körpervorzeichen zufällig und erhält die zeitliche Größen-, Docht- und Volumenfolge

## Gesamtprofil

| Weltform | Kontinuität | Ereignisanteil | Abdeckung | Drift | Achsen über Real |
|---|---:|---:|---:|---:|---|
| `real` | 0.758 | 0.0220 | 0.823 | 0.112 | - |
| `shuffle` | 0.697 | 0.0186 | 0.760 | 0.078 | - |
| `random_sign` | 0.782 | 0.0227 | 0.844 | 0.091 | Kontinuität;Ereignisanteil;Abdeckung |
| `sign_shuffle` | 0.748 | 0.0197 | 0.802 | 0.098 | - |
| `magnitude_shuffle` | 0.830 | 0.0227 | 0.875 | 0.236 | Kontinuität;Ereignisanteil;Abdeckung |
| `wick_shuffle` | 0.733 | 0.0258 | 0.802 | 0.093 | Ereignisanteil |
| `volume_shuffle` | 0.779 | 0.0288 | 0.885 | 0.121 | Kontinuität;Ereignisanteil;Abdeckung |

## Paarvergleich

| Kontrolle | Ereignis Real höher | Abdeckung Real höher | gemeinsam Real höher |
|---|---:|---:|---:|
| `shuffle` | 9/12 | 6/12 | 6/12 |
| `random_sign` | 5/12 | 2/12 | 2/12 |
| `sign_shuffle` | 7/12 | 6/12 | 5/12 |
| `magnitude_shuffle` | 5/12 | 2/12 | 2/12 |
| `wick_shuffle` | 3/12 | 5/12 | 1/12 |
| `volume_shuffle` | 1/12 | 3/12 | 0/12 |

## Asset- Und Zeitebenenprofil

Die Teilgruppen bleiben sekundär. Angegeben ist jeweils Real minus Kontrolle bei Kontinuität.

| Gruppe | shape shuffle | random sign | sign shuffle | magnitude shuffle | wick shuffle | volume shuffle |
|---|---:|---:|---:|---:|---:|---:|
| `asset:BTC` | -0.002 | -0.050 | -0.053 | -0.011 | 0.001 | -0.087 |
| `asset:SOL` | 0.122 | 0.001 | 0.073 | -0.124 | 0.047 | 0.044 |
| `timeframe:1h` | 0.051 | 0.009 | 0.015 | -0.088 | 0.052 | -0.052 |
| `timeframe:15m` | 0.074 | -0.058 | 0.005 | -0.049 | -0.003 | 0.009 |

## Befund

Die höchste Kontrollkontinuität trägt `magnitude_shuffle` mit `0.830` gegenüber Real `0.758`.

Den höchsten Familienereignisanteil trägt `volume_shuffle` mit `0.0288`; die höchste Mitgliederabdeckung trägt `volume_shuffle` mit `0.885`. Auf allen drei Primärachsen über Real liegen: `random_sign;magnitude_shuffle;volume_shuffle`.

Die reale Vorzeichenreihenfolge besitzt gegenüber `sign_shuffle` einen kleinen gemeinsamen Vorsprung. Dieser Befund reicht jedoch nicht für eine Richtungsbindung, weil `random_sign` Real gleichzeitig bei Kontinuität, Ereignisanteil und Abdeckung übertrifft. Die Wirkung der Vorzeichenänderung ist damit nicht monoton und hängt von der konkreten Kontrollform ab.

Auch die reale Größen- und Volumenfolge ist nicht notwendig für starke Familienlesung: `magnitude_shuffle` und `volume_shuffle` verstärken `rf_05` auf allen drei Primärachsen. `wick_shuffle` erhöht den Ereignisanteil, senkt aber Kontinuität und Abdeckung. Erst vollständiges Shape-Shuffle senkt alle drei Achsen gemeinsam.

Das Gesamtmuster spricht gegen eine einzelne tragende OHLCV-Komponente. `rf_05` reagiert eher auf die gekoppelte Organisation mehrerer zeitlicher Komponenten und kann durch isolierte Entkopplung sogar verstärkt werden. Daraus folgt derzeit keine begründete organische Erweiterung der Feldmechanik.

Eine einzelne permutierte Komponente wird nicht automatisch als Ursache gelesen. Aussagekräftig ist das Muster über Kontinuität, Ereignisanteil, Abdeckung und die zwölf direkten Paarfenster. Kontrollen, die Real auf mehreren Achsen erreichen oder übertreffen, markieren Komponenten, deren reale Reihenfolge für `rf_05` nicht hinreichend spezifisch ist.

Wenn eine isolierte Permutation deutlich unter Real fällt, bleibt die ursprüngliche Reihenfolge dieser Komponente ein Kandidat für die Tragung. Das ist eine diagnostische Eingrenzung und keine neue Feldregel.

## Grenze

Die Komponenten sind innerhalb rekonstruierter OHLCV-Welten nicht vollständig unabhängig. Eine veränderte Körpergröße beeinflusst den fortlaufenden Preisweg; Dochte und Körper bleiben geometrisch gekoppelt. Der Versuch lokalisiert Empfindlichkeiten, beweist aber keine einzelne kausale Quelle und keine feste Bedeutung von `rf_05`.
