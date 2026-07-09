# 2072 - Bisher ungelesene Rollenfamilien in Folgewelten auf gleicher Symbolbasis

## Zweck

Diese Auswertung startet neue reale Folgeweltlaeufe und liest die vollstaendigen Mitglieder von `rf_06`, `rf_13`, `rf_10`, `rf_08`, `rf_17` direkt aus der angegebenen passiven Rollenfamilien-Memory zurueck.

Die Symbolbasis wird nicht neu gruppiert. Geprueft werden exakt die in 2066 gebildeten `dio_*`-Mitglieder.

## Methode

- reale 1h-Folgewelten: `15`
- Assets: `BTC;DOGE;PAXG;SOL;XRP`
- Startpunkte pro Asset: `[5000, 6000, 7000]`
- Beobachtungen pro Welt: `1000` Rohzeilen
- Weltbasis (Archiv): `data/2070_role_family_followworlds.zip`
- entpackte Weltdateien und Debug-Ausgaben bleiben lokal und werden nicht gepusht
- pro Welt ein Lauf mit frischer episodischer Memory
- Wahrnehmungsmodus: `world_relative`
- keine Nullwelt in diesem Durchlauf; geprueft wird die reale spaete Anschlussfaehigkeit
- keine Handlung, keine Richtung, kein Gate und kein motorischer Impuls

## Familienbefund

| role_family | Basis | global gefunden | Welten mit Anschluss | ganze Familie | mittlere Abdeckung | Ereignisbalance | Ereignisse | Kontinuitaet | Lesung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| rf_06 | 8 | 8 | 15/15 | 0/15 | 0.342 | 0.874 | 51 | 0.557 | familienraum_offen_anschlussfaehig |
| rf_13 | 3 | 3 | 14/15 | 1/15 | 0.533 | 0.632 | 38 | 0.590 | familienraum_offen_anschlussfaehig |
| rf_10 | 2 | 2 | 12/15 | 2/15 | 0.467 | 0.636 | 22 | 0.534 | familienraum_offen_anschlussfaehig |
| rf_08 | 2 | 2 | 15/15 | 9/15 | 0.800 | 0.681 | 47 | 0.818 | familienraum_konsistent_anschlussfaehig |
| rf_17 | 2 | 2 | 7/15 | 1/15 | 0.267 | 0.833 | 12 | 0.353 | familienraum_offen_anschlussfaehig |

## Innere Rollenbewegung

Die Verteilungsdrift vergleicht die Ereignisanteile der Mitglieder zwischen 2066 und den neuen Folgewelten. `0` bedeutet gleiche Verteilung, `1` vollstaendige Verschiebung.

Diese relationale Lesung muss immer zusammen mit Ereigniszahl, Weltpraesenz und Mitgliederabdeckung gelesen werden. Eine geringe Drift in einer duennen Spur ist noch kein Stabilitaetsnachweis.

| role_family | Dominanz 2066 | Dominanz 2072 | Verteilungsdrift | innere Lesung | Profil 2066 | Profil 2072 |
|---|---|---|---:|---|---|---|
| rf_06 | dio_0s8r | dio_1ejq | 0.304 | starker_innerer_dominanzwechsel | dio_0s8r:147;dio_1xme:126;dio_0f8s:111;dio_0nx9:105;dio_0gh3:92;dio_1ejq:82;dio_0lr0:72;dio_1yhs:65 | dio_0s8r:6;dio_1xme:3;dio_0f8s:3;dio_0nx9:11;dio_0gh3:3;dio_1ejq:12;dio_0lr0:9;dio_1yhs:4 |
| rf_13 | dio_1sub | dio_1sub | 0.055 | rollenverteilung_nahe_stabil | dio_1sub:262;dio_1t9l:93;dio_14l0:79 | dio_1sub:22;dio_1t9l:7;dio_14l0:9 |
| rf_10 | dio_0jsd | dio_0jsd | 0.125 | rollenverteilung_nahe_stabil | dio_0jsd:242;dio_0ioc:193 | dio_0jsd:15;dio_0ioc:7 |
| rf_08 | dio_0h6t | dio_0h6t | 0.155 | rollenverteilung_verschoben | dio_0h6t:155;dio_1w94:152 | dio_0h6t:31;dio_1w94:16 |
| rf_17 | dio_1udx | dio_1udx | 0.043 | rollenverteilung_nahe_stabil | dio_1udx:166;dio_1cmd:141 | dio_1udx:7;dio_1cmd:5 |

## Folgeweltmatrix

Jede Zelle zeigt `gefundene Mitglieder/Basis (Ereignisse)`.

| Welt | rf_06 | rf_13 | rf_10 | rf_08 | rf_17 |
|---|---:|---:|---:|---:|---:|
| BTC 5000-6000 | 4/8 (4) | 1/3 (1) | 1/2 (1) | 2/2 (5) | 1/2 (1) |
| BTC 6000-7000 | 3/8 (3) | 1/3 (1) | 0/2 (0) | 1/2 (1) | 0/2 (0) |
| BTC 7000-8000 | 3/8 (6) | 2/3 (3) | 1/2 (3) | 2/2 (4) | 0/2 (0) |
| DOGE 5000-6000 | 2/8 (3) | 2/3 (2) | 2/2 (3) | 2/2 (3) | 0/2 (0) |
| DOGE 6000-7000 | 3/8 (3) | 1/3 (2) | 0/2 (0) | 1/2 (3) | 1/2 (1) |
| DOGE 7000-8000 | 4/8 (6) | 1/3 (5) | 1/2 (1) | 1/2 (1) | 0/2 (0) |
| PAXG 5000-6000 | 3/8 (5) | 2/3 (3) | 0/2 (0) | 2/2 (3) | 2/2 (5) |
| PAXG 6000-7000 | 3/8 (4) | 3/3 (4) | 1/2 (2) | 2/2 (4) | 1/2 (1) |
| PAXG 7000-8000 | 3/8 (3) | 2/3 (3) | 1/2 (1) | 1/2 (2) | 1/2 (2) |
| SOL 5000-6000 | 4/8 (5) | 2/3 (2) | 1/2 (1) | 2/2 (7) | 1/2 (1) |
| SOL 6000-7000 | 2/8 (2) | 2/3 (4) | 1/2 (1) | 2/2 (4) | 0/2 (0) |
| SOL 7000-8000 | 2/8 (2) | 2/3 (2) | 1/2 (3) | 2/2 (2) | 0/2 (0) |
| XRP 5000-6000 | 1/8 (1) | 2/3 (5) | 1/2 (2) | 1/2 (2) | 0/2 (0) |
| XRP 6000-7000 | 2/8 (2) | 0/3 (0) | 2/2 (2) | 2/2 (4) | 0/2 (0) |
| XRP 7000-8000 | 2/8 (2) | 1/3 (1) | 1/2 (2) | 1/2 (2) | 1/2 (1) |

## Feldzeit und Nachhall

| role_family | Rekopplung spaet | Strain spaet | Nachhall-Delta | Feldzeit-Delta | Phasenbreite | Mitgliedsprofil |
|---|---:|---:|---:|---:|---:|---|
| rf_06 | 0.708 | 0.185 | 0.010 | 0.063 | 0.000 | dio_0s8r:6;dio_1xme:3;dio_0f8s:3;dio_0nx9:11;dio_0gh3:3;dio_1ejq:12;dio_0lr0:9;dio_1yhs:4 |
| rf_13 | 0.687 | 0.209 | 0.041 | 0.123 | 0.044 | dio_1sub:22;dio_1t9l:7;dio_14l0:9 |
| rf_10 | 0.692 | 0.205 | 0.012 | 0.029 | 0.033 | dio_0jsd:15;dio_0ioc:7 |
| rf_08 | 0.732 | 0.148 | 0.046 | 0.171 | 0.033 | dio_0h6t:31;dio_1w94:16 |
| rf_17 | 0.694 | 0.199 | 0.007 | 0.044 | 0.000 | dio_1udx:7;dio_1cmd:5 |

## Lesung

- `rf_06`: `familienraum_offen_anschlussfaehig`; 15 von 15 Welten mit Anschluss, 0 davon mit vollstaendiger Familie; innere Bewegung: `starker_innerer_dominanzwechsel`.
- `rf_13`: `familienraum_offen_anschlussfaehig`; 14 von 15 Welten mit Anschluss, 1 davon mit vollstaendiger Familie; innere Bewegung: `rollenverteilung_nahe_stabil`.
- `rf_10`: `familienraum_offen_anschlussfaehig`; 12 von 15 Welten mit Anschluss, 2 davon mit vollstaendiger Familie; innere Bewegung: `rollenverteilung_nahe_stabil`.
- `rf_08`: `familienraum_konsistent_anschlussfaehig`; 15 von 15 Welten mit Anschluss, 9 davon mit vollstaendiger Familie; innere Bewegung: `rollenverteilung_verschoben`.
- `rf_17`: `familienraum_offen_anschlussfaehig`; 7 von 15 Welten mit Anschluss, 1 davon mit vollstaendiger Familie; innere Bewegung: `rollenverteilung_nahe_stabil`.

Die Lesung ist diagnostisch. Sie beschreibt, ob ein Bedeutungsraum in spaeten realen Fenstern als Familie weiterlebt, ob er kernlastig wird oder in Fragmente zerfaellt.

## Grenze

Die Kennzahlen duerfen nicht als Strategie, Entry-Signal, Richtungsvorgabe oder Handlungsgate verwendet werden. Auch eine konsistente Familie bleibt eine passive Feldbedeutung.

Wie es weitergeht: Die neuen Folgeweltbefunde sollten als naechstes als weitere numerische Evidenzschicht in die passive Rollenfamilien-Memory rueckgekoppelt werden.
