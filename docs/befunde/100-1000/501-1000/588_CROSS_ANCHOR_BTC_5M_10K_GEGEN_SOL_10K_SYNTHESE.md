# Cross-Anker-Synthese: BTC-5m-10k gegen SOL-10k

Stand: 2026-06-21

## Zweck

Diese Synthese prueft, ob die in SOL-10k sichtbare Anker- und Bewegungsordnung auch in BTC-10k-Welten erscheint.

Die Auswertung bleibt passiv.
Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Ist `0e7qvj1` nur SOL-nah oder auch in BTC-10k sichtbar?
2. Unterpruefung: Bleibt die Rollenordnung zentrumsnah?
3. Unterpruefung: Bleibt die Bewegungsasymmetrie um `0e7qvj1` erhalten?
4. Folgeschritt: KAS-10k benoetigt zuerst eine laengere KAS-Quelle; aktuell liegen nur KAS-2k-Kontrollwelten vor.

## Gepruefte BTC-Welten

- `kontrolliert_btc_2024_5m_10k_BTCUSDT.csv`
- `kontrolliert_btc_2025_5m_10k_BTCUSDT.csv`

Beide Dateien wurden aus vorhandenen BTC-Jahresdaten als kontrollierte 10k-Welten erzeugt.
Beide Welten reproduzierten Top-Syntax und Top-Familien exakt.

## Topologie

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|
| BTC2024_5M_10K | 0.8302 | 0.1599 | 0.0099 | 0.7037 | 0.5350 | 0.8440 |
| BTC2025_5M_10K | 0.8400 | 0.1492 | 0.0108 | 0.7041 | 0.5353 | 0.8455 |

Beide BTC-10k-Welten bleiben `stark_zentriert_wenig_rand`.

`dio_mcm_episode_0e7qvj1` dominiert auch in BTC:

- Zentrum,
- offene Variante,
- Rand/Kippnaehe.

Damit ist `0e7qvj1` nicht nur SOL-10k-nah.
Er erscheint auch in BTC-10k als zentrumsnaher MCM-Preview-Anker.

## Feldbewegungs-Memory BTC

| Qualitaet | Anzahl |
|---|---:|
| `recurrently_reconnecting` | 45 |
| `recurrently_opening_strain` | 38 |
| `world_specific` | 20 |
| `young` | 57 |

Bewegungswirkung:

| Wirkung | Anzahl |
|---|---:|
| `rekoppelnd_entlastend` | 70 |
| `oeffnend_belastend` | 53 |
| `bewegung_offen` | 22 |
| `spannungsnah` | 15 |

Staerkste BTC-Bewegungen:

- `0mji3u6 -> 0e7qvj1`: 44 Ereignisse, `recurrently_reconnecting`, `rekoppelnd_entlastend`
- `0e7qvj1 -> 1jwnjz4`: 41 Ereignisse, `recurrently_reconnecting`, `rekoppelnd_entlastend`
- `1jwnjz4 -> 0e7qvj1`: 39 Ereignisse, `recurrently_opening_strain`, `oeffnend_belastend`
- `0e7qvj1 -> 1hdpu9s`: 19 Ereignisse, `recurrently_reconnecting`, `rekoppelnd_entlastend`
- `1hdpu9s -> 0e7qvj1`: 14 Ereignisse, `recurrently_opening_strain`, `oeffnend_belastend`

## Vergleich zu SOL-10k

SOL-10k zeigte dominant:

- `0e7qvj1 -> 1hdpu9s`: rekoppelnd/entlastend
- `1hdpu9s -> 0e7qvj1`: oeffnend/belastend

BTC-10k zeigt dieselbe qualitative Asymmetrie, aber mit verschobener Nachbarschaft:

- `0e7qvj1 -> 1jwnjz4`: rekoppelnd/entlastend
- `1jwnjz4 -> 0e7qvj1`: oeffnend/belastend
- `0e7qvj1 -> 1hdpu9s` bleibt ebenfalls rekoppelnd/entlastend, aber weniger dominant.

## Arbeitsbefund

Die bisherige MCM-Lesart wird differenzierter:

`0e7qvj1` wirkt assetuebergreifend als zentrumsnaher Anker.
Die gerichtete Grundasymmetrie bleibt erhalten:

```text
vom Anker weg: rekoppelnd / entlastend
zum Anker zurueck aus Gegenrichtung: oeffnend / belastend
```

Aber die konkrete Nachbarschaft ist assetabhaengig:

- SOL koppelt staerker ueber `1hdpu9s`.
- BTC koppelt staerker ueber `1jwnjz4`, waehrend `1hdpu9s` weiter als sekundaere Achse sichtbar bleibt.

Das spricht gegen eine starre Namenskopie.
Es spricht eher fuer eine stabile MCM-Rollenbewegung mit welt-/assetbezogener Nachbarschaft.

## Grenze

KAS-10k wurde noch nicht geprueft, weil im aktuellen Projekt nur KAS-2k-Kontrollwelten vorhanden sind.
Eine echte KAS-10k-Gegenprobe braucht zuerst eine laengere KAS-Rohwelt.

## Wie es weitergeht

Als naechstes sollte entweder eine laengere KAS-Welt beschafft/erzeugt werden oder die BTC/SOL-10k-Achsen gemeinsam in einer Mehrquellen-Feldbewegungs-Memory verdichtet werden.
Ziel ist zu klaeren, welche Bewegungen allgemeine MCM-Achsen sind und welche nur assetnahe Nachbarschaften darstellen.
