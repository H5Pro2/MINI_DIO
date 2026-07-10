# 2076 - rf_05 unter Komponenten-Phasenkontrollen

## Zweck

Befund 2075 zeigte, dass zufällige Einzelkomponenten-Permutationen `rf_05` teils abschwächen, teils aber deutlich verstärken. Dieser Versuch prüft enger, ob die Familie an der relativen zeitlichen Kopplung der OHLCV-Komponenten hängt.

## Vorab Festgelegtes Design

- identische zwölf 2024-Holdoutfenster aus 2074 und 2075
- Komponenten: Körpervorzeichen, absolute Körpergröße, Dochtpaar und Volumen
- feste zirkuläre Offsets: `17`, `83` und `251` Beobachtungen
- jede Kontrolle erhält Reihenfolge, Verteilung und Autokorrelation der verschobenen Komponente vollständig
- nur die relative zeitliche Ausrichtung zum übrigen Feld wird verändert
- `144` neue Kontrollläufe und `12` Realreferenzläufe mit jeweils frischer episodischer Memory
- unveränderte acht Mitglieder von `rf_05`
- Wahrnehmungsmodus: `world_relative`
- Archiv der neuen Phasenkontrollen: `data/2076_rf05_component_phase_controls.zip`
- keine neue Klasse, keine Handlung, kein Gate und keine Richtung

Eine notwendige reale Komponentenkopplung wäre nur dann gestützt, wenn mehrere vorab festgelegte Offsets dieselbe Komponente gegenüber Real gemeinsam bei Kontinuität, Ereignisanteil und Abdeckung schwächen. Einzelne Offseteffekte gelten als Phasensensitivität, nicht als Ursache.

## Gesamtprofil Nach Offset

Realreferenz: Kontinuität `0.758`, Ereignisanteil `0.0220`, Abdeckung `0.823`.

| Komponente | Offset | Kontinuität | Ereignisanteil | Abdeckung | Drift | Achsen über Real | gemeinsam Real höher |
|---|---:|---:|---:|---:|---:|---|---:|
| `sign` | 17 | 0.709 | 0.0214 | 0.781 | 0.142 | - | 3/12 |
| `sign` | 83 | 0.702 | 0.0205 | 0.781 | 0.122 | - | 2/12 |
| `sign` | 251 | 0.781 | 0.0193 | 0.833 | 0.080 | Kontinuität;Abdeckung | 3/12 |
| `magnitude` | 17 | 0.830 | 0.0225 | 0.885 | 0.196 | Kontinuität;Ereignisanteil;Abdeckung | 2/12 |
| `magnitude` | 83 | 0.778 | 0.0216 | 0.833 | 0.146 | Kontinuität;Abdeckung | 3/12 |
| `magnitude` | 251 | 0.793 | 0.0230 | 0.875 | 0.148 | Kontinuität;Ereignisanteil;Abdeckung | 1/12 |
| `wick` | 17 | 0.754 | 0.0248 | 0.812 | 0.085 | Ereignisanteil | 1/12 |
| `wick` | 83 | 0.825 | 0.0284 | 0.875 | 0.050 | Kontinuität;Ereignisanteil;Abdeckung | 0/12 |
| `wick` | 251 | 0.780 | 0.0255 | 0.844 | 0.081 | Kontinuität;Ereignisanteil;Abdeckung | 2/12 |
| `volume` | 17 | 0.800 | 0.0267 | 0.854 | 0.128 | Kontinuität;Ereignisanteil;Abdeckung | 1/12 |
| `volume` | 83 | 0.793 | 0.0267 | 0.875 | 0.089 | Kontinuität;Ereignisanteil;Abdeckung | 0/12 |
| `volume` | 251 | 0.779 | 0.0269 | 0.875 | 0.145 | Kontinuität;Ereignisanteil;Abdeckung | 0/12 |

## Komponentenprofil Über Alle Offsets

Die Komponentenwerte bündeln jeweils `36` Kontrollwelten. Die Paarzahlen enthalten drei direkte Offsets je Realfenster.

| Komponente | Kontinuität | Ereignisanteil | Abdeckung | Drift | Achsen über Real | gemeinsam Real höher |
|---|---:|---:|---:|---:|---|---:|
| `sign` | 0.731 | 0.0204 | 0.799 | 0.105 | - | 8/36 |
| `magnitude` | 0.800 | 0.0224 | 0.865 | 0.159 | Kontinuität;Ereignisanteil;Abdeckung | 6/36 |
| `wick` | 0.787 | 0.0262 | 0.844 | 0.061 | Kontinuität;Ereignisanteil;Abdeckung | 3/36 |
| `volume` | 0.791 | 0.0268 | 0.868 | 0.107 | Kontinuität;Ereignisanteil;Abdeckung | 1/36 |

## Asset- Und Zeitebenenprofil

Angegeben ist Real minus gebündelte Phasenkontrolle bei Kontinuität. Die Teilgruppen bleiben sekundär.

| Gruppe | sign | magnitude | wick | volume |
|---|---:|---:|---:|---:|
| `asset:BTC` | -0.003 | -0.068 | -0.040 | -0.089 |
| `asset:SOL` | 0.057 | -0.018 | -0.019 | 0.025 |
| `timeframe:1h` | 0.055 | 0.002 | -0.000 | -0.035 |
| `timeframe:15m` | -0.001 | -0.086 | -0.058 | -0.030 |

## Befund

Über alle drei Offsets auf allen drei Primärachsen durchgehend unter Real liegen: `-`.

Einzelne Phasenkontrollen, die Real gleichzeitig auf allen drei Primärachsen übertreffen: `magnitude:17;magnitude:251;wick:83;wick:251;volume:17;volume:83;volume:251`.

Im über alle Offsets gebündelten Profil liegt nur `sign` auf allen drei Primärachsen unter Real. Bei der Vorzeichenphase ist der Abstand jedoch nicht breit fensterstabil: Real trägt einen höheren Ereignisanteil in `22/36`, eine höhere Abdeckung in `12/36` und beides gemeinsam nur in `8/36` Paaren. Zudem hebt Offset `251` Kontinuität und Abdeckung wieder über Real.

Die Größen-, Docht- und Volumenphase ist kein notwendiger Träger der realen Familienlesung. Ihre gebündelten Kontrollen liegen jeweils auf allen drei Primärachsen über Real; alle drei Volumen-Offsets tun dies auch einzeln. Damit widerspricht der Lauf einer allgemeinen notwendigen Kopplung aller OHLCV-Komponenten.

Die relative Vorzeichenphase bleibt als begrenzter Empfindlichkeitskandidat offen, aber nicht als belastbare Feldbindung: Der Mittelwertabstand, die geringe gemeinsame Paarbreite und der gegenläufige längste Offset tragen nicht kohärent genug. Das Muster belegt Phasensensitivität, keine Ursache und keine feste Bedeutung von `rf_05`.

Die Messung verändert keine Feldmechanik. Aus diesem Befund folgt keine begründete organische Erweiterung, weil die Wirkung weder über Komponenten noch über Offsets und direkte Fensterpaare kohärent trägt.

## Grenze

Die zirkuläre Verschiebung erzeugt am Umlaufpunkt eine künstliche Nachbarschaft und rekonstruiert anschließend einen neuen Preisweg. Sie bewahrt die Eigenfolge einer Komponente exakt, beweist aber weder Kausalität noch feste Semantik. Die Prüfung bleibt auf Marktzeitreihen und `1000` Beobachtungen je Welt begrenzt.
