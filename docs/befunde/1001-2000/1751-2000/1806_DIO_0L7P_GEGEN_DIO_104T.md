# 1806 - `dio_0l7p` gegen `dio_104t`

## Grundfrage

Diese Prüfung legt zwei Feldfolgen-Signaturen direkt nebeneinander.

Ziel ist eine passive Trennung: Brückenträger, Anschlussknoten oder nur gleiche Oberfläche?

## Quellen

- `reports/dio_0l7p_bridge_tick_window_signature.csv`
- `reports/dio_104t_bridge_tick_window_signature.csv`

## Vergleich

| Muster | Phase | Feld links | Feld rechts | Spannung Δ | Rekopplung Δ | Strain Δ | Lesung |
|---|---|---|---|---:|---:|---:|---|
| `kippnaehe` | `ereignis` | `offen` | `offen` | 0.034399 | -0.00443 | 0.007431 | `rechts_traegt_mehr_offene_last` |
| `kippnaehe` | `nachlauf` | `offen` | `offen` | 0.016627 | -0.00203 | 0.003051 | `rechts_traegt_mehr_offene_last` |
| `kippnaehe` | `vorlauf` | `offen` | `offen` | 0.006347 | -0.006781 | 0.008368 | `rechts_traegt_mehr_offene_last` |
| `tragende_verarbeitung` | `ereignis` | `rekoppelt` | `rekoppelt` | 0.025242 | -0.006317 | 0.004212 | `links_rekoppelt_spitzer` |
| `tragende_verarbeitung` | `nachlauf` | `offen` | `rekoppelt` | -0.0294 | 0.021292 | -0.01427 | `rechts_haelt_rekopplung_laenger` |
| `tragende_verarbeitung` | `vorlauf` | `offen` | `offen` | 0.003038 | 0.00471 | -0.001195 | `nahe_feldlage` |

## Befund

`dio_0l7p` und `dio_104t` teilen die gleiche Grundbewegung: offene Vorphase, tragendes Ereignis und getrennte Kippnähe.

Der Unterschied liegt in der Feldfolge. `dio_0l7p` rekoppelt im Ereignis spitzer und fällt danach wieder offener in Nachprüfung. `dio_104t` hält Rekopplung im Nachlauf stärker und bleibt stärker an Hören mit Wechsel gebunden.

Damit wirkt die Trennung vorläufig so:

- `dio_0l7p`: stärkerer Brückenträger.
- `dio_104t`: stärkerer Anschluss-/Kohärenzknoten.

Das ist kein Beweis für feste Bedeutungen. Die Bedeutung entsteht weiter aus Familie, Weltfenster, Feldfolge und Nachbarschaft.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob diese Rollen in weiteren Kernfamilien ebenfalls paarweise auftreten: Brückenträger, Anschlussknoten, Randknoten und breite Sammelfamilien.
