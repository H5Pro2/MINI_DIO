# 2074 - rf_05 im unabhängigen Jahres- und Zeitebenen-Holdout

## Zweck

Befund 2073 ließ `rf_05` als einzige Rollenfamilie mit gemeinsamem Gruppenabstand bei Kontinuität, Ereignisanteil und Mitgliederabdeckung zurück. Dieser Holdout prüft, ob der Vorsprung außerhalb der verwendeten 2025er 1h-Fenster bestehen bleibt.

## Vorab Festgelegtes Design

- ausschließlich Datenjahr `2024`
- Assets: `BTC` und `SOL`
- Zeitebenen: `1h` und `15m`
- drei über das Jahr verteilte Fenster je Asset und Zeitebene
- `12` Realfenster mit jeweils `1000` Beobachtungen
- je Realfenster eine Shuffle- und eine Random-Sign-Kontrolle
- insgesamt `36` frische Läufe mit jeweils frischer episodischer Memory
- unveränderte acht Mitglieder von `rf_05` aus Befund 2066
- Wahrnehmungsmodus: `world_relative`
- reproduzierbares Weltarchiv: `data/2074_rf05_crossyear_timeframe_holdout.zip`
- keine neue Klasse, keine Handlung, kein Gate und keine Richtung

Der Primärvergleich wurde vor dem Lauf auf drei Achsen festgelegt: Familienkontinuität, mittlerer Familienereignisanteil und mittlere Mitgliederabdeckung. Der Zeitebenen- und Assetvergleich ist sekundär.

## Gesamtvergleich

| Gruppe | Welten | Kontinuität real/shuffle/random | Real minus stärkste Kontrolle | Ereignisanteil real/shuffle/random | Abdeckung real/shuffle/random | Drift real/shuffle/random |
|---|---:|---:|---:|---:|---:|---:|
| `overall` | 12 | 0.758/0.697/0.782 | -0.024 | 0.0220/0.0186/0.0227 | 0.823/0.760/0.844 | 0.112/0.078/0.091 |
| `asset:BTC` | 6 | 0.691/0.694/0.741 | -0.050 | 0.0191/0.0174/0.0205 | 0.729/0.750/0.792 | 0.093/0.115/0.080 |
| `asset:SOL` | 6 | 0.823/0.701/0.822 | 0.001 | 0.0248/0.0198/0.0250 | 0.917/0.771/0.896 | 0.162/0.130/0.164 |
| `timeframe:1h` | 6 | 0.764/0.714/0.755 | 0.009 | 0.0206/0.0193/0.0213 | 0.833/0.792/0.812 | 0.130/0.050/0.086 |
| `timeframe:15m` | 6 | 0.752/0.678/0.809 | -0.058 | 0.0233/0.0179/0.0241 | 0.812/0.729/0.875 | 0.159/0.160/0.097 |

## Paarvergleich

Die Paarzahlen zeigen, in wie vielen direkt zugeordneten Fenstern Realwelt die jeweilige Kontrolle übertrifft. `gemeinsam` verlangt gleichzeitig höhere Abdeckung und höheren Ereignisanteil.

| Gruppe | Ereignis real > shuffle/random | Abdeckung real > shuffle/random | gemeinsam real > shuffle/random |
|---|---:|---:|---:|
| `overall` | 9/12 / 5/12 | 6/12 / 2/12 | 6/12 / 2/12 |
| `asset:BTC` | 4/6 / 2/6 | 2/6 / 0/6 | 2/6 / 0/6 |
| `asset:SOL` | 5/6 / 3/6 | 4/6 / 2/6 | 4/6 / 2/6 |
| `timeframe:1h` | 4/6 / 2/6 | 3/6 / 1/6 | 3/6 / 1/6 |
| `timeframe:15m` | 5/6 / 3/6 | 3/6 / 1/6 | 3/6 / 1/6 |

## Befund

Im vorab festgelegten Gesamtvergleich liegt Realwelt auf folgenden Primärachsen über beiden Kontrollen: `-`.

Der gemeinsame Vorsprung von `rf_05` aus 2073 wird damit im unabhängigen Holdout nicht reproduziert. Realwelt liegt zwar auf allen drei Primärachsen über Shuffle, bleibt aber auf allen drei unter Random Sign. Im direkten Paarvergleich übertrifft Real die Random-Sign-Kontrolle gleichzeitig bei Abdeckung und Ereignisanteil nur in `2/12` Fenstern.

Die Asymmetrie der Kontrollen ist fachlich wichtig: Shuffle zerstört die Reihenfolge der lokalen Kerzenformen, Random Sign erhält dagegen die zeitliche Folge von Größenordnung, Dochten und Volumen und verändert vor allem die Körperrichtung. Das Profil spricht daher eher für eine Bindung an zeitliche Intensitäts- und Formfolge als für eine bereits belegte Bindung an reale Richtungsfolge. Diese Lesung ist eine Hypothese aus dem Kontrollmuster, kein neuer Mechanismus.

Ein Vorsprung auf nur einer Achse reicht nicht, um `rf_05` als realweltspezifischen Bedeutungsraum zu lesen. Entscheidend ist, ob die relationale Familie zugleich breiter, häufiger und über die Fenster hinweg kontinuierlicher getragen wird.

Die Teilgruppen zeigen, ob ein möglicher Gesamtabstand von einem einzelnen Asset oder einer Zeitebene stammt. Sie werden nicht nachträglich zur Hauptbestätigung umgedeutet.

## Grenze

Der Holdout erweitert Jahr, Asset und Zeitebene, bleibt aber bei Marktzeitreihen und `1000` Beobachtungen je Welt. Er prüft keine Robotiksensorik, keine andere Sinnesmodalität und keine feste Semantik. Alle Werte bleiben passive Forschungsmaße.
