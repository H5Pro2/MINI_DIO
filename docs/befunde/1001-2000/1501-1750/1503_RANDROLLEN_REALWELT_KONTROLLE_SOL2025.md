# 1503 - Randrollen gegen reale SOL-5m-Welt

## Fragestellung

Nach der synthetischen Randrollenkarte sollte geprueft werden:

Treten die bekannten Randrollen auch in einer realen Weltspur auf?

Gepruefte Rollen:

- `dio_1wdi` - nachhallender Randbruch-Phaenotyp
- `dio_0l7p` - fokussierte Start-/End-Randnaehe
- `dio_14wj` - verschobene beidseitige Randspannung

## Aufbau

Reale Kontrollwelt:

- Datei: `data/kontrolliert_sol_2025_5m_test1_2000_SOLUSDT.csv`
- 2000 Zeilen
- passive Auswertung
- frisches Memory
- `world_relative`-Sinnesaufnahme

## Ergebnis

| Kennwert | Wert |
| --- | ---: |
| Top-Symbol | `dio_104t4us` |
| Top-Count | 113 |
| `dio_1wdi` | 0 |
| `dio_0l7p` | 144 |
| `dio_14wj` | 0 |
| unique symbols | 351 |
| stabile Feldwirkung | 1503 |
| carried_unrest | 477 |
| avg_rekopplung_quality | 0.691874 |
| avg_afterimage | 0.122426 |
| focus_tone | 1988 |
| observation_tone | 6 |

## Deutung

Die reale Weltspur bildet eigene dominante Familien. Der Hauptanker ist `dio_104t`, nicht eine der synthetischen Randrollen.

Trotzdem taucht `dio_0l7p` deutlich auf:

- Symbol `dio_0l7pvdk`: 72
- Familie `dio_0l7p`: 144

Das ist eine partielle Uebertragung der fokussierten Randnaehe in reale Weltspur.

`dio_1wdi` und `dio_14wj` erscheinen in dieser realen Kontrollwelt nicht. Daraus folgt:

- Die nachhallende synthetische Randbruchrolle ist nicht automatisch real allgemein.
- Die verschobene beidseitige Randspannung ist in diesem Realfenster nicht sichtbar.
- `dio_0l7p` ist bisher die robusteste synthetisch gefundene Randrolle mit realer Anschlussfaehigkeit.

## Wichtige Grenze

Dieser Befund bestaetigt nicht die gesamte Randrollenkarte in realen Daten.

Er zeigt nur:

Eine der Rollen, `dio_0l7p`, kann in realer Weltspur wieder auftauchen, ohne dominant zu sein.

Das ist fachlich sauberer als eine Vollbestaetigung. Die reale Welt ist breiter, rauscht mehr und bildet eigene dominante Familien.

## MCM-Deutung

Die synthetischen Rollen sind keine starren Universalbegriffe.

Sie wirken eher wie Feldnaehen, die in realer Weltspur wieder anschlussfaehig werden koennen, wenn die reale Lage aehnliche Innenfeldqualitaet traegt.

Das passt zur bisherigen MCM-Lesung:

- Bedeutung ist feldnah, nicht tabellarisch.
- Wiederkehr kann partiell sein.
- Reale Weltspur erzeugt eigene Rollen und kann bekannte Rollen mitfuehren.
