# 1384 - Feldfunktionsrollen im Vergleich

## Zweck

Diese Diagnose vergleicht drei passive Rollenlinien aus `1382`:

- Bruecke-only
- Zentrum-only
- Bruecke/Zentrum-Mischrolle

Ziel ist zu pruefen, ob die Mischrolle eigene Merkmale traegt oder nur eine Zwischenbezeichnung aus Bruecke und Zentrum ist.

Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.

## Kurzbefund

### brueckennaehe

- Fenster: `67`
- Preview-Folgecarry: `0.865672`
- Rohweltformen: `gemischte_rohwelt:34, laute_oder_druckvolle_rohwelt:22, wechselhafte_rohwelt:5, ruhige_enge_rohwelt:5, gerichtete_weltbewegung:1`
- Welten: `XRP_2024_5M:24, DOGE_2024_5M:18, PAXG_2024_5M:17, BTC_2024_5M:4, SOL_2024_5M:4`
- Effekte: `stabil:67`
- Familien: `dio_104t:34, dio_0m9z:7, dio_0l7p:7, dio_155c:5, dio_14wj:5`
- Drift: `0.115505`
- absolute Drift: `0.694759`
- durchschnittliche Bewegung: `0.095244`
- Range: `0.187903`
- Richtungswechsel: `0.408925`
- Persistenz: `0.591075`
- Sensorikdelta: `0.010045`
- Rekopplungsdelta: `0.007956`
- Folge-Strain-Delta: `0.002835`
- Folge-Rekopplungsdelta: `-0.003049`

### zentrumsnaehe

- Fenster: `21`
- Preview-Folgecarry: `0.666667`
- Rohweltformen: `gemischte_rohwelt:16, wechselhafte_rohwelt:3, ruhige_enge_rohwelt:1, laute_oder_druckvolle_rohwelt:1`
- Welten: `DOGE_2024_5M:9, XRP_2024_5M:8, PAXG_2024_5M:3, BTC_2024_5M:1`
- Effekte: `stabil:21`
- Familien: `dio_104t:10, dio_0l7p:5, dio_14wj:2, dio_1u5i:1, dio_0m9z:1`
- Drift: `0.161065`
- absolute Drift: `0.582370`
- durchschnittliche Bewegung: `0.069926`
- Range: `0.139480`
- Richtungswechsel: `0.421124`
- Persistenz: `0.578876`
- Sensorikdelta: `-0.003728`
- Rekopplungsdelta: `-0.002188`
- Folge-Strain-Delta: `0.002124`
- Folge-Rekopplungsdelta: `-0.001655`

### mischrolle_brueckennaehe_zentrumsnaehe

- Fenster: `65`
- Preview-Folgecarry: `0.861538`
- Rohweltformen: `gemischte_rohwelt:48, laute_oder_druckvolle_rohwelt:9, ruhige_enge_rohwelt:6, wechselhafte_rohwelt:2`
- Welten: `PAXG_2024_5M:20, XRP_2024_5M:19, DOGE_2024_5M:19, SOL_2024_5M:4, BTC_2024_5M:3`
- Effekte: `stabil:65`
- Familien: `dio_104t:24, dio_14wj:15, dio_0m9z:9, dio_0l7p:9, dio_155c:4`
- Drift: `-0.078779`
- absolute Drift: `0.575055`
- durchschnittliche Bewegung: `0.076700`
- Range: `0.155132`
- Richtungswechsel: `0.366125`
- Persistenz: `0.633875`
- Sensorikdelta: `0.009603`
- Rekopplungsdelta: `0.006215`
- Folge-Strain-Delta: `0.004552`
- Folge-Rekopplungsdelta: `-0.004600`

## Lesung

Bruecke-only ist die breiteste Rolle und tritt in mehreren Rohweltformen auf.
Zentrum-only ist deutlich seltener und liegt ebenfalls meist in gemischter Rohwelt.
Die Mischrolle ist nicht nur die Summe beider Rollen: sie ist haeufiger als Zentrum-only, stark in gemischter Rohwelt gebunden und zeigt hohe Carry-Naehe.

Damit wirkt sie wie eine eigene passive Feldlinie zwischen Uebergang und Zentrumsnaehe.
Sie sollte vorerst nicht als harte neue Kategorie behandelt werden, sondern als Kandidat fuer eine wiederkehrende Kopplungsfunktion.

## Grenze

Die Rohweltform `gemischte_rohwelt` ist noch zu breit.
Der naechste saubere Schritt ist eine feinere Zerlegung dieser gemischten Rohwelt in visuelle und tonale Unterformen.

## Wie es weitergeht

Als naechstes sollte `gemischte_rohwelt` innerhalb der Mischrolle feiner gelesen werden: welche konkreten Ton-, Range-, Richtungswechsel- und Verdichtungsfolgen tragen diese Kopplung?
