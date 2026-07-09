# Vorwahrnehmung: stabile Wiederkehr, Drift und Umorganisation

Diese Auswertung liest die Holdout-Rückprüfung aus 2041 passiv weiter. Ziel ist nicht Handlung, sondern eine Landkarte: Welche Vorwahrnehmungsrollen kehren stabil wieder, welche verschieben ihre Feldqualität, und welche organisieren sich unter neuer Weltspannung um?

## Kurzbefund

- Ausgewertete Zeilen: 14
- Ausgewertete Ereignisse: 315
- Durchschnittliche Feld-Rücklesung: 0.640
- Durchschnittliche Sinnes-Rücklesung: 0.688
- Durchschnittliche Rohbewegungs-Rücklesung: 0.198
- Stabile/teilstabile Zeilen: 10
- Driftende oder umorganisierte Zeilen: 4

Die Rohbewegung bleibt deutlich schwächer rücklesbar als Feld- und Sinnesnähe. Das spricht gegen eine reine Kopie der Oberfläche und für eine passive Feldnähe-Landkarte.

## Klassen

| landkarte_class | rows | events | avg_field_recall | avg_sensory_recall | avg_motion_recall | avg_carry | avg_strain | avg_rekopplung |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stabil_wiederkehrend | 7 | 132 | 0.943 | 0.929 | 0.159 | 0.374 | 0.271 | 0.586 |
| teilstabil_wiederkehrend | 3 | 132 | 0.566 | 0.323 | 0.222 | 0.383 | 0.258 | 0.596 |
| umorganisierte_rekopplung | 2 | 15 | 0.000 | 1.000 | 0.278 | 0.421 | 0.272 | 0.602 |
| verschobene_rekopplungsqualitaet | 2 | 36 | 0.333 | 0.083 | 0.222 | 0.403 | 0.233 | 0.610 |

## Gruppenlesung

| target_group | source_chain | rows | events | avg_field_recall | avg_sensory_recall | avg_motion_recall | landkarte_classes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| oberflaeche_rekoppelt | long_btc_sol | 2 | 30 | 0.667 | 0.250 | 0.333 | verschobene_rekopplungsqualitaet:1;stabil_wiederkehrend:1 |
| oberflaeche_rekoppelt | multiasset | 2 | 45 | 0.444 | 0.139 | 0.167 | teilstabil_wiederkehrend:1;verschobene_rekopplungsqualitaet:1 |
| oberflaeche_rekoppelt_spaet | long_btc_sol | 2 | 18 | 1.000 | 1.000 | 0.083 | stabil_wiederkehrend:2 |
| oberflaeche_rekoppelt_spaet | multiasset | 2 | 27 | 1.000 | 1.000 | 0.083 | stabil_wiederkehrend:2 |
| rekopplung_oeffnet | long_btc_sol | 3 | 78 | 0.457 | 0.810 | 0.327 | stabil_wiederkehrend:1;teilstabil_wiederkehrend:1;umorganisierte_rekopplung:1 |
| rekopplung_oeffnet | multiasset | 3 | 117 | 0.457 | 0.810 | 0.154 | stabil_wiederkehrend:1;teilstabil_wiederkehrend:1;umorganisierte_rekopplung:1 |

## Fachliche Lesung

- `oberflaeche_rekoppelt_spaet` bleibt über DOGE und PAXG besonders stabil. Die Oberfläche ist anders, aber die offene Rekopplungsrolle bleibt lesbar.
- `rekopplung_oeffnet` bleibt bei BTC und DOGE spannungsnah wiederkehrend, kippt bei PAXG aber in `offene_rekopplung`. Das ist keine einfache Loeschung, sondern eine Umorganisation der Feldrolle.
- `oberflaeche_rekoppelt` zeigt zwischen BTC, DOGE und Multiasset eine Verschiebung der Rekopplungsqualität. Das Feld erkennt Nähe, aber die Tragqualität ist nicht identisch.
- Die niedrige Rohbewegungs-Rücklesung zeigt: Die Vorwahrnehmung hängt nicht primär an identischen Kursbewegungen, sondern an wiederkehrender Feld- und Sinnesnähe.

## Grenze

Diese Landkarte ist passiv. Sie erzeugt keine Handlung, keine Richtung, keinen Entry und kein Gate. Sie beschreibt nur, ob eine frühere Feldnähe in einer neuen Welt stabil, verschoben oder umorganisiert wieder auftaucht.
