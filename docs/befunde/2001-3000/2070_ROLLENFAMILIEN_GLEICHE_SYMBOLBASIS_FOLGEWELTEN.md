# 2070 - Rollenfamilien in neuen Folgewelten auf gleicher Symbolbasis

## Zweck

Diese Auswertung startet neue reale Folgeweltlaeufe und liest die vollstaendigen Mitglieder von `rf_07`, `rf_21` und `rf_05` direkt aus der passiven Rollenfamilien-Memory 2069 zurueck.

Die Symbolbasis wird nicht neu gruppiert. Geprueft werden exakt die in 2066 gebildeten `dio_*`-Mitglieder.

## Methode

- reale 1h-Folgewelten: `15`
- Assets: `BTC;DOGE;PAXG;SOL;XRP`
- Startpunkte pro Asset: `[5000, 6000, 7000]`
- Beobachtungen pro Welt: `1000` Rohzeilen
- veroeffentlichtes Weltarchiv: `data/2070_role_family_followworlds.zip`
- entpackte Weltdateien und Debug-Ausgaben bleiben lokal und werden nicht gepusht
- pro Welt ein Lauf mit frischer episodischer Memory
- Wahrnehmungsmodus: `world_relative`
- keine Nullwelt in diesem Durchlauf; geprueft wird die reale spaete Anschlussfaehigkeit
- keine Handlung, keine Richtung, kein Gate und kein motorischer Impuls

## Familienbefund

| role_family | Basis | global gefunden | Welten mit Anschluss | ganze Familie | mittlere Abdeckung | Ereignisbalance | Ereignisse | Kontinuitaet | Lesung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| rf_07 | 2 | 2 | 15/15 | 15/15 | 1.000 | 0.782 | 386 | 0.978 | familienraum_konsistent_anschlussfaehig |
| rf_21 | 2 | 2 | 15/15 | 12/15 | 0.900 | 0.598 | 107 | 0.885 | familienraum_konsistent_anschlussfaehig |
| rf_05 | 8 | 8 | 15/15 | 2/15 | 0.800 | 0.833 | 339 | 0.740 | familienraum_breit_anschlussfaehig |

## Innere Rollenbewegung

Die Verteilungsdrift vergleicht die Ereignisanteile der Mitglieder zwischen 2066 und den neuen Folgewelten. `0` bedeutet gleiche Verteilung, `1` vollstaendige Verschiebung.

| role_family | Dominanz 2066 | Dominanz 2070 | Verteilungsdrift | innere Lesung | Profil 2066 | Profil 2070 |
|---|---|---|---:|---|---|---|
| rf_07 | dio_1ewh | dio_1ewh | 0.003 | rollenverteilung_nahe_stabil | dio_1ewh:1433;dio_0g2r:909 | dio_1ewh:235;dio_0g2r:151 |
| rf_21 | dio_1pij | dio_1v2w | 0.415 | starker_innerer_dominanzwechsel | dio_1pij:1033;dio_1v2w:413 | dio_1pij:32;dio_1v2w:75 |
| rf_05 | dio_0fe7 | dio_1xrt | 0.119 | leichter_dominanzwechsel_bei_naher_verteilung | dio_0fe7:636;dio_1xrt:567;dio_17dc:317;dio_1ba6:269;dio_0v65:253;dio_0ein:196;dio_0u24:85;dio_0qup:74 | dio_0fe7:70;dio_1xrt:92;dio_17dc:32;dio_1ba6:35;dio_0v65:49;dio_0ein:43;dio_0u24:10;dio_0qup:8 |

## Folgeweltmatrix

Jede Zelle zeigt `gefundene Mitglieder/Basis (Ereignisse)`.

| Welt | rf_07 | rf_21 | rf_05 |
|---|---:|---:|---:|
| BTC 5000-6000 | 2/2 (13) | 2/2 (6) | 6/8 (30) |
| BTC 6000-7000 | 2/2 (25) | 1/2 (5) | 6/8 (22) |
| BTC 7000-8000 | 2/2 (23) | 2/2 (8) | 7/8 (23) |
| DOGE 5000-6000 | 2/2 (37) | 1/2 (5) | 5/8 (15) |
| DOGE 6000-7000 | 2/2 (21) | 2/2 (3) | 7/8 (23) |
| DOGE 7000-8000 | 2/2 (30) | 2/2 (11) | 5/8 (17) |
| PAXG 5000-6000 | 2/2 (32) | 2/2 (8) | 8/8 (32) |
| PAXG 6000-7000 | 2/2 (23) | 2/2 (8) | 7/8 (15) |
| PAXG 7000-8000 | 2/2 (20) | 2/2 (4) | 8/8 (19) |
| SOL 5000-6000 | 2/2 (24) | 2/2 (11) | 7/8 (17) |
| SOL 6000-7000 | 2/2 (26) | 2/2 (11) | 6/8 (23) |
| SOL 7000-8000 | 2/2 (26) | 1/2 (4) | 5/8 (22) |
| XRP 5000-6000 | 2/2 (28) | 2/2 (7) | 5/8 (22) |
| XRP 6000-7000 | 2/2 (20) | 2/2 (8) | 7/8 (32) |
| XRP 7000-8000 | 2/2 (38) | 2/2 (8) | 7/8 (27) |

## Feldzeit und Nachhall

| role_family | Rekopplung spaet | Strain spaet | Nachhall-Delta | Feldzeit-Delta | Phasenbreite | Mitgliedsprofil |
|---|---:|---:|---:|---:|---:|---|
| rf_07 | 0.744 | 0.161 | 0.411 | 0.321 | 0.900 | dio_1ewh:235;dio_0g2r:151 |
| rf_21 | 0.711 | 0.183 | 0.192 | 0.366 | 0.267 | dio_1pij:32;dio_1v2w:75 |
| rf_05 | 0.745 | 0.142 | 0.188 | 0.341 | 0.225 | dio_0fe7:70;dio_1xrt:92;dio_17dc:32;dio_1ba6:35;dio_0v65:49;dio_0ein:43;dio_0u24:10;dio_0qup:8 |

## Lesung

- `rf_07`: `familienraum_konsistent_anschlussfaehig`; 15 von 15 Welten mit Anschluss, 15 davon mit vollstaendiger Familie; innere Bewegung: `rollenverteilung_nahe_stabil`.
- `rf_21`: `familienraum_konsistent_anschlussfaehig`; 15 von 15 Welten mit Anschluss, 12 davon mit vollstaendiger Familie; innere Bewegung: `starker_innerer_dominanzwechsel`.
- `rf_05`: `familienraum_breit_anschlussfaehig`; 15 von 15 Welten mit Anschluss, 2 davon mit vollstaendiger Familie; innere Bewegung: `leichter_dominanzwechsel_bei_naher_verteilung`.

Die Lesung ist diagnostisch. Sie beschreibt, ob ein Bedeutungsraum in spaeten realen Fenstern als Familie weiterlebt, ob er kernlastig wird oder in Fragmente zerfaellt.

## Grenze

Die Kennzahlen duerfen nicht als Strategie, Entry-Signal, Richtungsvorgabe oder Handlungsgate verwendet werden. Auch eine konsistente Familie bleibt eine passive Feldbedeutung.
