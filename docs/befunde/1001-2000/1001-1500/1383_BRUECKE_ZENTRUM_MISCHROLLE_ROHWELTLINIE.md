# 1383 - Bruecke/Zentrum-Mischrolle: Rohweltlinie

## Zweck

Diese Diagnose isoliert die staerkste Kopplung aus `1382`:

```text
mischrolle_brueckennaehe_zentrumsnaehe + gemischte_rohwelt
```

Geprueft wird, ob diese Linie eine echte wiederkehrende Feldform sein koennte oder nur eine breite interne Metriknaehe.

Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.

## Befund

- Fenster: `48`
- Preview-Folgecarry: `42/48`
- Welten: [('BTC_2024_5M', 2), ('DOGE_2024_5M', 16), ('PAXG_2024_5M', 14), ('XRP_2024_5M', 16)]
- Effekte: [('stabil', 48)]

## Durchschnittliche Rohweltmerkmale

- Drift: `-0.048866`
- absolute Drift: `0.492130`
- durchschnittliche absolute Bewegung: `0.067113`
- durchschnittliche Range: `0.136134`
- maximale Range: `0.448348`
- Richtungswechsel: `0.369135`
- Persistenz: `0.630865`

## Innenfeldmerkmale

- mittleres Sensorikdelta: `0.008912`
- mittleres Rekopplungsdelta: `0.005589`
- mittleres Folge-Strain-Delta: `0.004004`
- mittleres Folge-Rekopplungsdelta: `-0.003478`

## Dominante Symbole

- Preview: [('dio_mcm_episode_0e7qvj1', 11), ('dio_mcm_episode_0ykar6i', 10), ('dio_mcm_episode_0ybr5e3', 8), ('dio_mcm_episode_14coypf', 5), ('dio_mcm_episode_0b7nep9', 4), ('dio_mcm_episode_1xx3u1e', 3), ('dio_mcm_episode_0geqqo3', 3), ('dio_mcm_episode_1jwnjz4', 2)]
- Familien: [('dio_104t', 20), ('dio_14wj', 10), ('dio_0l7p', 6), ('dio_0m9z', 6), ('dio_155c', 3), ('dio_1u5i', 1), ('dio_00ja', 1), ('dio_1fll', 1)]

## Lesung

Diese Linie liegt nicht in lauter oder eindeutig druckvoller Rohwelt, sondern in gemischter Rohwelt.
Gleichzeitig zeigt sie hohe Rekopplung, tragende Carry-Naehe und niedrigen Strain.

Das spricht dafuer, dass die Mischrolle nicht einfach aus Aussenlaerm entsteht.
Sie wirkt eher wie ein Feldzustand, in dem Uebergang und Zentrumsnaehe gleichzeitig getragen werden.

## Grenze

Der Befund ist ein Indiz.
Die Rohweltform `gemischte_rohwelt` ist breit. Sie muss spaeter feiner visuell/tonal zerlegt werden.
