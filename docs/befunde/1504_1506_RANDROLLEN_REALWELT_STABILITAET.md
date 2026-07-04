# 1504-1506 - Randrollen in realen Weltfenstern

## Fragestellung

Nach der ersten realen Kontrolle 1503 war offen:

Ist `dio_0l7p` real stabil wiederkehrend oder nur in einem einzelnen SOL-2025-Fenster sichtbar?

Zusatzfrage:

Tauchen `dio_1wdi` oder `dio_14wj` in realen Welten ebenfalls auf?

## Aufbau

Verglichen wurden vier reale Weltfenster:

| Welt | Datei | Typ |
| --- | --- | --- |
| 1503 | `data/kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv` | SOL-Basisfenster |
| 1504 | `data/kontrolliert_real_quiet_sol_2025_5m_2000.csv` | ruhige SOL-Welt |
| 1505 | `data/kontrolliert_long_sol_2025_5m_stress_4000.csv` | stressigere/laengere SOL-Welt |
| 1506 | `data/kontrolliert_btc_2025_5m_test1_2000_BTCUSDT.csv` | anderes Asset, BTC |

Alle Laeufe waren passiv, mit frischem Memory und `world_relative`-Sinnesaufnahme.

## Ergebnis

| Welt | Typ | Top-Familie | `dio_1wdi` | `dio_0l7p` | `dio_14wj` | Nachhall | stabile Feldwirkung | carried_unrest |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1503 | SOL Basis | `dio_104t` | 0 | 144 | 0 | 0.122426 | 1503 | 477 |
| 1504 | SOL ruhig | `dio_104t` | 0 | 140 | 72 | 0.131243 | 1536 | 437 |
| 1505 | SOL stress | `dio_104t` | 0 | 282 | 170 | 0.162519 | 3150 | 812 |
| 1506 | BTC | `dio_104t` | 0 | 126 | 72 | 0.135689 | 1589 | 388 |

## Deutung

`dio_0l7p` kehrt in allen realen Kontrollwelten wieder.

Wichtig: Es ist nicht dominant. Die reale Welt bildet eigene Hauptfamilien, vor allem `dio_104t` und je nach Welt auch `dio_155c`.

Trotzdem bleibt `dio_0l7p` sichtbar:

- SOL Basis: 144
- SOL ruhig: 140
- SOL stress: 282
- BTC 2025: 126

Das spricht fuer reale Anschlussfaehigkeit der fokussierten Randnaehe.

`dio_14wj` tritt in drei von vier realen Pruefungen auf:

- SOL ruhig: 72
- SOL stress: 170
- BTC 2025: 72

Damit ist `dio_14wj` nicht nur synthetisch sichtbar, sondern kann auch in realer Weltspur als Mitrolle auftreten.

`dio_1wdi` tritt in keiner dieser realen Welten auf. Diese Rolle bleibt bisher an die kontrollierte synthetische Nachhall-/Randbruchstruktur gebunden.

## Schlussfolgerung

Die reale Pruefung staerkt die Randrollenkarte, aber differenziert sie:

1. `dio_0l7p` ist die robusteste real anschlussfaehige Randrolle.
2. `dio_14wj` ist ebenfalls real anschlussfaehig, aber eher als Mitrolle.
3. `dio_1wdi` bleibt bisher synthetisch-spezifisch.

Das ist kein Nachweis einer vollstaendigen Universal-Topologie. Es ist aber ein belastbarer Hinweis, dass synthetisch gefundene Feldrollen in realen Weltspuren wieder auftauchen koennen.

## MCM-Deutung

Die reale Welt liest sich nicht als Kopie der synthetischen Melodie.

Sie erzeugt eigene dominante Feldfamilien. Gleichzeitig koennen bekannte Randrollen mitlaufen. Das passt zur MCM-Lesung:

- Bedeutung ist feldnah und kontextabhaengig.
- Eine Rolle muss nicht dominant sein, um real vorhanden zu sein.
- Wiederkehr kann als Nebenrolle auftreten.
- Reale Weltspur ist breiter und bildet eine eigene Bedeutungslandschaft.

## Wie es weitergeht

Als naechstes sollte geprueft werden, welche Rohweltmerkmale `dio_0l7p` in realen Welten aktivieren: Randlage, geringe Beobachtungslast, Fokusnaehe, lokale Umkehr oder eine bestimmte Sinneskopplung.
