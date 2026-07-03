# 1382 - Feldfunktionskarte: Rohwelt-Ruecklesung

## Zweck

Diese Diagnose liest die in `1381` markierten Feldfunktionsnaehen gegen konkrete Candle-Fenster zurueck.

Geprueft wird:

```text
Koppeln Brueckennaehe, Zentrumsnaehe, Randdrucknaehe und Mischrollen an reale Aussenweltformen,
oder entstehen sie nur aus internen Metriknaehen?
```

Die Diagnose bleibt passiv. Keine Handlung, keine Richtung, keine Strategie.

## Datengrundlage

- gelesene Naehefenster: `169`

## Rollennaehe und Rohweltformen

### `brueckennaehe`

- Fenster: `67`
- Rohweltformen: gemischte_rohwelt:34 | laute_oder_druckvolle_rohwelt:22 | wechselhafte_rohwelt:5 | ruhige_enge_rohwelt:5 | gerichtete_weltbewegung:1
- Welten: XRP_2024_5M:24 | DOGE_2024_5M:18 | PAXG_2024_5M:17 | BTC_2024_5M:4 | SOL_2024_5M:4

### `mischrolle_brueckennaehe_zentrumsnaehe`

- Fenster: `65`
- Rohweltformen: gemischte_rohwelt:48 | laute_oder_druckvolle_rohwelt:9 | ruhige_enge_rohwelt:6 | wechselhafte_rohwelt:2
- Welten: PAXG_2024_5M:20 | XRP_2024_5M:19 | DOGE_2024_5M:19 | SOL_2024_5M:4 | BTC_2024_5M:3

### `zentrumsnaehe`

- Fenster: `21`
- Rohweltformen: gemischte_rohwelt:16 | wechselhafte_rohwelt:3 | ruhige_enge_rohwelt:1 | laute_oder_druckvolle_rohwelt:1
- Welten: DOGE_2024_5M:9 | XRP_2024_5M:8 | PAXG_2024_5M:3 | BTC_2024_5M:1

### `entlastungsnaehe`

- Fenster: `7`
- Rohweltformen: gemischte_rohwelt:4 | ruhige_enge_rohwelt:3
- Welten: PAXG_2024_5M:6 | XRP_2024_5M:1

### `randdrucknaehe`

- Fenster: `5`
- Rohweltformen: gemischte_rohwelt:3 | laute_oder_druckvolle_rohwelt:1 | ruhige_enge_rohwelt:1
- Welten: BTC_2024_5M:1 | SOL_2024_5M:1 | PAXG_2024_5M:1 | XRP_2024_5M:1 | DOGE_2024_5M:1

### `mischrolle_brueckennaehe_entlastungsnaehe`

- Fenster: `4`
- Rohweltformen: gemischte_rohwelt:4
- Welten: PAXG_2024_5M:2 | DOGE_2024_5M:2

## Lesung

Wenn eine Rollennaehe ueberwiegend mit konkreten Rohweltformen koppelt, spricht das fuer reale Aussenweltbindung.
Wenn sie breit ueber alle Rohweltformen verteilt ist, muss sie vorsichtig als interne Feldnaehe gelesen werden.

## Grenze

Die Rohweltform ist eine einfache Ruecklesung aus Candle-Fenstern. Sie ist keine endgueltige visuelle Formanalyse.

## Wie es weitergeht

Als naechstes sollte die staerkste Kopplung aus dieser Ruecklesung isoliert werden. Dann kann geprueft werden, ob sie in weiteren Welten stabil bleibt oder nur in einem Asset/Regime auftritt.
