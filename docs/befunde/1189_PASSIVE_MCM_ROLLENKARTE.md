# 1189 - Passive MCM-Rollenkarte

## Grundfrage

Welche passiven Feldzonen ergeben sich aus den stabilen und kippenden Brueckenrollen?

Die Rollenkarte ist eine Verdichtung der Befunde 1184 bis 1187.
Sie ist keine Steuerlogik und kein Gate.

## Feldzonen

| Feldzone | Ereignisse | Familien | Rekopplung | Carry | Strain | Tension | Ton | Formstabilitaet | Roh-Range |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| zone_uebergangsoeffnung | 766 | dio_1r55:3;dio_00ja:1;dio_0tay:1;dio_17ct:1;dio_1kpz:1;dio_1lsu:1;dio_1uof:1 | 0.7026 | 0.5175 | 0.1460 | 0.0976 | -0.0882 | +0.0314 | 0.01026 |
| zone_stabile_rueckbindung | 363 | dio_06s7:1;dio_1kpz:1 | 0.7229 | 0.5486 | 0.1225 | 0.0522 | -0.0292 | +0.0122 | 0.01265 |
| zone_belastete_randnaehe | 222 | dio_0oc3:1 | 0.6918 | 0.5151 | 0.1693 | 0.1714 | -0.3159 | -0.2226 | 0.01113 |
| zone_kohaerente_bruecke | 180 | dio_0tay:1;dio_17ct:1 | 0.7104 | 0.5364 | 0.1434 | 0.0948 | -0.1273 | +0.3000 | 0.01565 |
| zone_gemischte_nachbarschaft | 2 | dio_1uof:1 | 0.6687 | 0.4610 | 0.1594 | 0.0357 | +0.0418 | -0.0343 | 0.01018 |

## Lesart

Es entstehen `5` passive Feldzonen: `zone_uebergangsoeffnung, zone_stabile_rueckbindung, zone_belastete_randnaehe, zone_kohaerente_bruecke, zone_gemischte_nachbarschaft`.

Die Karte zeigt eine Feldorganisation:

- Rueckbindung ist eine eigene Zone mit hoher Rekopplung und niedriger Spannung.
- Belastete Randnaehe ist eine eigene Zone mit hoher Spannung und hohem Strain.
- Uebergangsoeffnung ist keine reine Stoerung, sondern eine wiederkehrende Rollenverschiebung.
- Kohaerente Bruecke liegt zwischen Rueckbindung und Uebergang.

Damit wird MINI_DIOs MCM-Feld als dynamische Zonenkonfiguration lesbar.
Die Bedeutung entsteht nicht isoliert im Symbol, sondern durch Lage im Feld, Weltfenster, Sinnesaufnahme und Nachbarschaft.

## Grenze

Diese Karte ist eine Forschungslesung.
Sie sagt nicht, dass MINI_DIO bewusst eine Zone auswaehlt.
Sie zeigt aber, dass sich aus passiver Feldwirkung eine stabile, beschreibbare Zonenstruktur ableiten laesst.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob diese Feldzonen ueber weitere Assets und Zeitraeume gleich bleiben oder ob neue Zonen entstehen.
