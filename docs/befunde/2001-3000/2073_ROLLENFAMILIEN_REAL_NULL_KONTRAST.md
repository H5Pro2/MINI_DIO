# 2073 - Rollenfamilien im Real-/Nullwelt-Kontrast

## Zweck

Dieser Versuch prüft alle acht in 2066 gebildeten Rollenfamilien gegen zeitstrukturzerstörte Kontrollwelten auf unveränderter Symbolbasis.

Die Frage ist nicht, ob Nullwelten überhaupt Ordnung bilden. Frühere Befunde zeigen, dass sie das können. Geprüft wird enger, ob die in realen Folgewelten beobachtete Familienanschlussfähigkeit gegenüber zwei assetnahen Kontrollformen einen kontinuierlichen Vorsprung trägt.

## Methode

- reale Referenz: die 15 Folgefenster aus 2070 und 2072
- Kontrollen: je Realfenster eine Shuffle-Order- und eine Random-Sign-Welt
- Kontrollläufe: `30` mit jeweils `1000` Beobachtungen
- Assets: `BTC;DOGE;PAXG;SOL;XRP`
- pro Kontrollwelt eine frische episodische Memory
- Wahrnehmungsmodus: `world_relative`
- Kontrollweltarchiv: `data/2073_role_family_null_controls.zip`
- Debugdaten und entpackte Kontrollwelten bleiben lokal
- keine neue Familienklasse, keine Handlung, kein Gate und keine Richtung

Shuffle erhält die lokalen Kerzenformen, zerstört aber ihre Reihenfolge. Random Sign erhält die Größenordnung der Körper und Dochte, verändert jedoch die Richtung der Körper. Beide Kontrollen bleiben damit asset- und längennah, ohne die reale zeitliche Folge zu bewahren.

## Kontinuierlicher Familienvergleich

Positive Differenzen bedeuten einen Realweltvorsprung. Negative Differenzen bedeuten, dass die gemittelte oder stärkste Kontrolle mindestens gleich hoch liegt. Es wird kein Schwellenwert zur festen Klassifikation verwendet.

| Familie | Kontinuität real/shuffle/random | Real minus stärkste Kontrolle | Ereignisanteil real/shuffle/random | Abdeckung real/shuffle/random | Drift real/shuffle/random |
|---|---:|---:|---:|---:|---:|
| `rf_05` | 0.740/0.725/0.713 | 0.015 | 0.0227/0.0184/0.0203 | 0.800/0.783/0.758 | 0.119/0.140/0.087 |
| `rf_06` | 0.557/0.585/0.531 | -0.028 | 0.0034/0.0049/0.0031 | 0.342/0.425/0.283 | 0.304/0.373/0.242 |
| `rf_07` | 0.978/0.993/0.984 | -0.015 | 0.0259/0.0197/0.0197 | 1.000/1.000/1.000 | 0.003/0.076/0.030 |
| `rf_08` | 0.818/0.703/0.794 | 0.024 | 0.0032/0.0022/0.0032 | 0.800/0.667/0.767 | 0.155/0.131/0.109 |
| `rf_10` | 0.534/0.659/0.477 | -0.125 | 0.0015/0.0022/0.0013 | 0.467/0.600/0.433 | 0.125/0.050/0.286 |
| `rf_13` | 0.590/0.657/0.661 | -0.071 | 0.0025/0.0031/0.0027 | 0.533/0.578/0.556 | 0.055/0.256/0.229 |
| `rf_17` | 0.353/0.830/0.395 | -0.477 | 0.0008/0.0034/0.0007 | 0.267/0.800/0.300 | 0.043/0.059/0.041 |
| `rf_21` | 0.885/0.932/0.840 | -0.048 | 0.0072/0.0080/0.0066 | 0.900/0.933/0.867 | 0.415/0.303/0.512 |

## Paarvergleich Der 15 Ausgangsfenster

Jede Zahl nennt die Anzahl der Realfenster, die ihre direkt abgeleitete Kontrolle auf derselben Achse übertrifft. `gemeinsam` verlangt im selben Fenster zugleich höhere Mitgliederabdeckung und höheren Familienereignisanteil.

| Familie | Ereignisanteil real > shuffle/random | Abdeckung real > shuffle/random | gemeinsam real > shuffle/random |
|---|---:|---:|---:|
| `rf_05` | 8/15 / 10/15 | 6/15 / 7/15 | 5/15 / 6/15 |
| `rf_06` | 3/15 / 7/15 | 4/15 / 7/15 | 2/15 / 7/15 |
| `rf_07` | 11/15 / 12/15 | 0/15 / 0/15 | 0/15 / 0/15 |
| `rf_08` | 8/15 / 8/15 | 6/15 / 4/15 | 5/15 / 4/15 |
| `rf_10` | 2/15 / 8/15 | 2/15 / 4/15 | 1/15 / 4/15 |
| `rf_13` | 4/15 / 7/15 | 4/15 / 5/15 | 2/15 / 5/15 |
| `rf_17` | 0/15 / 4/15 | 0/15 / 2/15 | 0/15 / 2/15 |
| `rf_21` | 5/15 / 8/15 | 2/15 / 3/15 | 2/15 / 2/15 |

## Gesamtprofil

- mittlere Familienkontinuität real/shuffle/random: `0.682` / `0.760` / `0.674`
- mittlerer Familienereignisanteil real/shuffle/random: `0.0084` / `0.0077` / `0.0072`
- Realwelt übertrifft die jeweils stärkere Kontrolle bei Kontinuität: `2/8` Familien
- Realwelt liegt über dem Kontrollmittel bei Ereignisanteil: `3/8` Familien
- Realwelt liegt über dem Kontrollmittel bei Mitgliederabdeckung: `2/8` Familien

## Befund

- Kontinuität über beiden Kontrollen: `rf_05;rf_08`
- Familienereignisanteil über beiden Kontrollen: `rf_05;rf_07`
- Mitgliederabdeckung über beiden Kontrollen: `rf_05;rf_08`
- gemeinsamer Vorsprung auf allen drei Achsen: `rf_05`
- stärkster Kontrollvorsprung bei Kontinuität: `rf_17` mit Real minus stärkste Kontrolle `-0.477`

Die reale Zeitfolge erzeugt damit keinen breiten Kontinuitätsvorsprung der acht Familien. Shuffle liegt im Gesamtmittel höher, Random Sign etwa auf Realniveau. Die Anschlussfähigkeit aus 2070 und 2072 ist daher zunächst als feldinterne Wiederkehr zu lesen, nicht als ausreichender Nachweis realweltspezifischer Bedeutung.

Nur Familien, die mehrere Achsen und die direkten Paarfenster gemeinsam tragen, bleiben stärkere Kandidaten für eine spätere Weltbindungsprüfung. Auch bei ihnen ist die Nullweltnähe Teil des Befunds und darf nicht ausgeblendet werden.

## Lesung

Der Vergleich liest keine Familie als wahr oder falsch. Entscheidend ist das gemeinsame Profil: Eine Familie ist als realweltlich getragener Bedeutungsraum erst stärker begründet, wenn ihre Präsenz, Mitgliederabdeckung, Ereignistragung und innere Verteilung gegenüber beiden Kontrollen gemeinsam Abstand gewinnen.

Wo Kontrollen gleichauf oder stärker liegen, bleibt die Familie eine feldinterne Ordnungsform ohne ausreichenden Nachweis spezifischer Weltbindung. Das ist kein Fehler des Feldes, aber eine Grenze der Bedeutungsbehauptung.

## Grenze

Der Versuch verwendet dieselben 15 kurzen Folgefenster wie 2070 und 2072. Er prüft Zeitordnung und Richtungsstruktur, aber noch keine völlig fremden Assets, längeren Horizonte oder sensormodal anderen Welten. Die Differenzen sind Forschungsmaße, keine Handlungswerte und keine feste Semantik der einzelnen `dio_*`-Zeichen.
