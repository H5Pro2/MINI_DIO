# Befund 288 - Reproduktion der KASUSDT-Zeitebenenstaffelung

## Fragestellung

Geprüft wurde, ob die KASUSDT-Zeitebenenstaffelung aus Befund `285` bei frischer Memory reproduzierbar bleibt.

Verglichen wurden:

- `285_KAS_ZEITEBENEN_TOPOLOGIE_MATRIX.csv`
- `287_REPRO_KAS_ZEITEBENEN_TOPOLOGIE_MATRIX.csv`

## Ergebnis

Die Reproduktion ist exakt.

Alle verglichenen Rollenwerte haben Delta `0.0000000000000000`:

- Zentrum/Stabil
- offene Variante
- Spannungsrand/Kippnähe

Das gilt für:

- KAS 5m
- KAS 15m
- KAS 30m
- KAS 1h

## Interpretation

Die KAS-Zeitebenenwirkung ist in dieser Versuchsanordnung nicht zufällig aus einer einzelnen Memory-Oberfläche entstanden.

MINI_DIO bildet bei identischer Welt und frischer Memory dieselbe grobe Innenfeldordnung erneut aus:

- 5m bleibt zentrumsnah mit Übergang
- 15m bleibt nahezu identisch zu 5m
- 30m bleibt die offenste KAS-Zeitebene
- 1h bleibt wieder nahe am zentrumsnahen Bereich

Damit ist die Zeitebenenstaffelung reproduziert.

## Fachliche Grenze

Das ist ein reproduzierbarer Befund innerhalb dieser Daten- und Codefassung.

Es ist noch kein allgemeiner Nachweis, dass jede Kleinpreis-Welt dieselbe Ordnung bildet. Dafür müssen weitere Assets, andere Jahre und andere Sequenzfenster geprüft werden.

## Bedeutung für MINI_DIO

Die Weltaufnahme ist hier stabil genug, um die nächste Stufe zu rechtfertigen:

KAS kann als Kleinpreis-Testwelt in den regulären Vergleich gegen SOL und BTC aufgenommen werden.

Wichtig ist dabei: Die Topologie bleibt nicht starr gleich, sondern zeigt eine kleine, aber reproduzierbare Zeitebenenverschiebung. Genau diese Verschiebung ist relevant, weil sie auf eine feldbezogene Antwort auf Weltspannung hinweist.

## Wie es weitergeht

Als nächstes sollte KAS/SOL/BTC über dieselben Zeitebenen verglichen werden. Ziel: prüfen, ob 30m allgemein eine offenere Zwischenebene bildet oder ob das ein KAS-spezifischer Effekt ist.
