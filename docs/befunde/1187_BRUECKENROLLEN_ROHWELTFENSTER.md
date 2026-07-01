# 1187 - Brueckenrollen Rohweltfenster

## Grundfrage

Welche konkreten Weltmerkmale halten eine Brueckenrolle stabil, und welche Merkmale begleiten ein Kippen der Rolle?

Die Auswertung bindet die passiven Rollen aus 1184/1185 an OHLCV-Fenster zurueck.
Sie bleibt Diagnose: keine Handlung, kein Gate, keine Strategie.

## Stabile Rollen

| Familie | Rolle | Ereignisse | Welten | Return | Range | Body | Volumen | Richtung | Rekopplung | Strain | Tension |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_06s7 | stabilisierende_rueckbindung | 226 | 8 | -0.00228 | 0.01233 | 0.00173 | 0.880 | 0.194 | 0.7238 | 0.1235 | 0.0527 |
| dio_0oc3 | spannungsnahe_belastung | 222 | 8 | +0.00174 | 0.01113 | 0.00157 | 0.741 | 0.204 | 0.6918 | 0.1693 | 0.1714 |
| dio_0tay | kohaerente_bruecke | 65 | 4 | +0.00195 | 0.01542 | 0.00189 | 0.715 | 0.198 | 0.7091 | 0.1399 | 0.0774 |
| dio_17ct | kohaerente_bruecke | 115 | 3 | -0.00383 | 0.01588 | 0.00196 | 0.897 | 0.211 | 0.7116 | 0.1469 | 0.1122 |
| dio_1kpz | stabilisierende_rueckbindung | 137 | 6 | +0.00360 | 0.01297 | 0.00168 | 0.881 | 0.220 | 0.7220 | 0.1214 | 0.0516 |
| dio_1r55 | uebergang_oeffnung | 62 | 4 | +0.00121 | 0.00764 | 0.00100 | 0.430 | 0.168 | 0.7063 | 0.1461 | 0.1261 |

## Gekippte Rollen

| Familie | Baseline | Beobachtet | Ereignisse | Welten | Return | Range | Body | Volumen | Richtung | Rekopplung | Strain | Tension |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_00ja | gemischte_nachbarschaft | uebergang_oeffnung:241 | 241 | 8 | +0.00191 | 0.01614 | 0.00227 | 1.183 | 0.199 | 0.6960 | 0.1605 | 0.0799 |
| dio_0tay | kohaerente_bruecke | stabilisierende_rueckbindung:33;uebergang_oeffnung:11;gemischte_nachbarschaft:4 | 48 | 4 | -0.00033 | 0.00617 | 0.00083 | 0.743 | 0.210 | 0.7073 | 0.1393 | 0.0787 |
| dio_17ct | kohaerente_bruecke | uebergang_oeffnung:85 | 85 | 5 | -0.00284 | 0.01131 | 0.00151 | 0.761 | 0.226 | 0.7056 | 0.1459 | 0.1142 |
| dio_1kpz | stabilisierende_rueckbindung | uebergang_oeffnung:11;gemischte_nachbarschaft:6 | 17 | 2 | +0.00215 | 0.00895 | 0.00130 | 0.656 | 0.192 | 0.7105 | 0.1227 | 0.0521 |
| dio_1lsu | gemischte_nachbarschaft | uebergang_oeffnung:202 | 202 | 8 | +0.00130 | 0.01165 | 0.00151 | 0.785 | 0.190 | 0.7046 | 0.1507 | 0.1194 |
| dio_1r55 | uebergang_oeffnung | spannungsnahe_belastung:16 | 16 | 1 | -0.00211 | 0.01178 | 0.00149 | 0.453 | 0.256 | 0.7027 | 0.1470 | 0.1317 |
| dio_1uof | gemischte_nachbarschaft | uebergang_oeffnung:91 | 91 | 7 | +0.00052 | 0.01314 | 0.00188 | 0.962 | 0.219 | 0.7002 | 0.1408 | 0.0392 |

## Vergleich

- durchschnittliche Roh-Range stabil: `0.01256`
- durchschnittliche Roh-Range gekippt: `0.01131`
- durchschnittliche MCM-Spannung stabil: `0.09858`
- durchschnittliche MCM-Spannung gekippt: `0.08790`
- durchschnittliche Strain stabil: `0.14118`
- durchschnittliche Strain gekippt: `0.14386`

## Lesart

Stabile Rollen sind nicht einfach haeufige Symbole, sondern erscheinen in Rohweltfenstern mit eigener MCM-Rueckbindung.
Kippende Rollen zeigen, dass eine Familie ihre lokale Bedeutung unter anderer Weltspannung verschieben kann.

Damit wird die MCM-Lesung konkreter: Die Rolle haengt nicht nur am Zeichen, sondern an Weltfenster, Ton, Form, Rezeptoraufnahme und Feldwirkung.

## Wie es weitergeht

Als naechstes sollte aus diesen Rohweltmerkmalen eine passive Rollenkarte entstehen: stabile Rueckbindung, belastete Randnaehe, Uebergangsoeffnung und gemischte Nachbarschaft als Feldzonen.
