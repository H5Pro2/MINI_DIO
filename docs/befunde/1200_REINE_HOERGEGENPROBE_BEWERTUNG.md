# Befund 1200 - Reine Hoergegenprobe

## Grundfrage

Befund 1198 zeigte, dass chaotisches Hoeren bei stabiler Form mehr Rand-/Kippnaehe erzeugt als chaotischere visuelle Form bei stabilem Hoeren. Die naechste Frage war:

```text
Bildet die Hoerachse eine eigene passive Feldtopologie aus?
```

Dazu wurde eine Welt gebaut, in der die visuelle Form weitgehend stabil bleibt, waehrend die tonale bzw. energetische Achse steigt, faellt, pulsiert, still wird und Doppelimpulse bildet.

## Datengrundlage

- Builder: `data_builder/synthetic_desync_world_builder.py`
- Variant: `pure_hearing`
- Welt: `data/synthetic_mcm_pure_hearing_5m.csv`
- Lauf: `debug/1199_pure_hearing/dio_mini_lauf_2/`
- Matrix: `docs/befunde/1199_REINE_HOERGEGENPROBE_TOPOLOGIE_MATRIX.md`
- CSV: `docs/befunde/1199_REINE_HOERGEGENPROBE_TOPOLOGIE_MATRIX.csv`

Der Lauf wurde mit frischem Memory im Modus `world_relative` ausgefuehrt.

## Kerndaten

- Kerzen: `8400`
- Episoden: `8394`
- eindeutige Symbole: `46`
- Rekopplung: `0.7518`
- Carry: `0.6009`
- Strain: `0.1317`
- Sinneskopplung: `0.9063`
- Nachhall: `0.7516`
- Trust-Stuetze: `0.9264`
- Caution-Stuetze: `0.0410`

Passive Innenfeldklassen:

- `stabil`: `7966`
- `tragend_unruhig`: `371`
- `kippend`: `54`
- `gespannt`: `3`

Topologische Rollen:

| Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|
| `zentrum_stabil` | `0.9490` | `0.7566` | `0.6085` | `0.1251` | `0.9151` |
| `offene_variante` | `0.0442` | `0.6710` | `0.4687` | `0.2426` | `0.7601` |
| `spannungsrand_kippnaehe` | `0.0068` | `0.6140` | `0.3988` | `0.3233` | `0.6365` |

## Vergleich mit den Desync-Teilwelten

| Welt | Zentrum | Offene Variante | Rand/Kippnaehe |
|---|---:|---:|---:|
| `SYNTH_PURE_HEARING` | `0.9490` | `0.0442` | `0.0068` |
| `VIS_STABLE_HEARING_CHAOTIC` | `0.9513` | `0.0243` | `0.0243` |
| `VIS_CHAOTIC_HEARING_STABLE` | `0.9997` | `0.0003` | `0.0000` |
| `SYNTH_DESYNC_AXES` | `0.9803` | `0.0105` | `0.0092` |

## Bewertung

Die reine Hoergegenprobe erzeugt eine erkennbare passive Hoer-Topologie:

- Das Zentrum bleibt dominant.
- Die offene Variante steigt deutlich.
- Rand/Kippnaehe bleibt vorhanden, aber kleiner als beim chaotisches-Hoeren-Fall.

Die Unterscheidung ist wichtig:

```text
Reine Hoervariation erzeugt vor allem Uebergangsraum.
Chaotisches Hoeren bei stabiler Form erzeugt staerkere Rand-/Kippnaehe.
Stabiles Hoeren bei unruhigerer Form bleibt nahezu vollstaendig zentrumsstabil.
```

Damit wirkt Hoeren nicht einfach als "mehr Last". Hoeren erzeugt je nach Struktur verschiedene Feldrollen:

- steigende/fallende/pulsierende Energie: mehr offene Variante,
- impulsiver oder widerspruechlicher Ton: mehr Rand-/Kippnaehe,
- stabile tonale Achse: starke Rueckfuehrung, selbst bei visueller Unruhe.

## MCM-Lesart

Die Hoerachse wirkt im aktuellen MINI_DIO-System als energetischer Stimulationskanal. Sie ist naeher an Feldspannung als die reine visuelle Formaufnahme. Trotzdem wird sie durch Rezeptorik und weltrelative Anpassung nicht direkt als Rohlast ins Feld geworfen.

Das bestaetigt die aktuelle MCM-Trennung:

```text
Sehen -> Form und Struktur
Hoeren -> Energie, Ton, Spannung
Rezeptorik -> Uebersetzung in Feldwirkung
MCM-Feld -> Rueckfuehrung, Uebergang, Randnaehe
```

## Schlussfolgerung

MINI_DIO bildet unter reiner Hoervariation keine zufaellige Ueberlastung, sondern eine geordnete Verschiebung:

- Zentrum bleibt erhalten.
- Uebergangsraum waechst.
- Randnaehe bleibt klein, aber messbar.

Das spricht dafuer, dass die Hoerachse als eigene Wahrnehmungsachse im MCM-Feld lesbar wird.

## Wie es weitergeht

Als naechstes sollte die Hoerachse zeitlich aufgeloest werden: Welche Phasen der reinen Hoerwelt erzeugen offene Variante, welche erzeugen Rand/Kippnaehe, und wann kehrt das Feld ins Zentrum zurueck?
