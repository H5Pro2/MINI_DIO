# Befund 1194 - Rand-/Kipp-Gegenprobe zur gravitativen 0-Punkt-Hypothese

## Grundfrage

Wenn der 0-Punkt im MCM-Feld eine rueckfuehrende, gravitative Feldfunktion uebernimmt, muesste eine bewusst randlastige Welt nicht automatisch das gesamte Feld kollabieren lassen. Sie muesste entweder Randnaehe ausbilden oder vom Feld ueber Rezeptorik, Rekopplung und Innenordnung integriert werden.

Diese Gegenprobe prueft daher:

- erhoeht eine synthetische Rand-/Kipp-Welt die Randrolle deutlich?
- bleibt das Feld trotzdem zentrumsnah stabil?
- zeigt sich Ueberlastung als dominanter Zustand oder nur als schmale Randspur?

## Datengrundlage

- Welt: `data/synthetic_mcm_rand_kipp_gegenprobe_9000_5m.csv`
- Lauf: `debug/1193_rand_kipp_gegenprobe/dio_mini_lauf_2/`
- Topologie-Matrix: `docs/befunde/1193_RAND_KIPP_GEGENPROBE_TOPOLOGIE_MATRIX.md`
- CSV-Matrix: `docs/befunde/1193_RAND_KIPP_GEGENPROBE_TOPOLOGIE_MATRIX.csv`

Der Lauf wurde mit frischem Memory im Modus `world_relative` ausgefuehrt.

## Messwerte

Der Lauf umfasst:

- Kerzen: `9000`
- Episoden: `8994`
- Trades: `0`
- durchschnittliche Rekopplung: `0.7377`
- durchschnittlicher Carry: `0.5860`
- durchschnittlicher Strain: `0.1326`
- durchschnittliche Sinneskopplung: `0.8885`
- durchschnittlicher Nachhall: `0.5981`
- zeitliche Trust-Stuetze: `0.8581`
- zeitliche Caution-Stuetze: `0.0786`

Passive Innenfeldklassen:

- `stabil`: `8124`
- `tragend_unruhig`: `864`
- `kippend`: `5`
- `gespannt`: `1`

Episode-Memory-Zustaende:

- `field_carried`: `8993`
- `field_strained`: `1`

## Topologische Rollen

Die weltrelative Rollenmatrix zeigt:

| Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|
| `zentrum_stabil` | `0.9033` | `0.7444` | `0.5944` | `0.1266` | `0.9007` |
| `offene_variante` | `0.0961` | `0.6762` | `0.5085` | `0.1882` | `0.7751` |
| `spannungsrand_kippnaehe` | `0.0007` | `0.5763` | `0.3309` | `0.3064` | `0.6823` |

## Bewertung

Die Gegenprobe erzeugt keine breite Randdominanz. Obwohl die Welt absichtlich rand- und kippnah konstruiert wurde, bleibt der dominante Feldzustand zentrumsnah stabil. Rand/Kippnaehe tritt auf, aber nur als sehr schmale Spur.

Das ist wichtig:

- MINI_DIO reicht Rohspannung nicht einfach ungefiltert in das MCM-Feld durch.
- Die Rezeptorik und weltrelative Aufnahme wirken offenbar als Integrationsschicht.
- Das Feld bildet weiter eine starke Rueckfuehrungsordnung.
- Randnaehe bleibt messbar, aber sie dominiert das Feld nicht.

Damit wird die Hypothese `0-Punkt als gravitative Feldfunktion` im aktuellen Datenraum weiter gestuetzt: Der 0-Punkt wirkt nicht als starre Mitte, sondern als rueckfuehrende Feldnaehe, in die selbst starke Aussenweltspannung teilweise integriert werden kann.

## Grenze der Aussage

Das ist kein physikalischer Beweis und keine Aussage ueber reale Gravitation. Es ist eine MCM-interne Feldhypothese:

```text
Wiederkehrende Weltwirkung erzeugt Verdichtung.
Verdichtung bildet Bedeutungsinseln.
Der 0-Punkt wirkt als Rueckfuehrungsnaehe.
Randnaehe erscheint dort, wo Rekopplung schwach und Strain hoch wird.
```

Die Gegenprobe zeigt auch eine methodische Grenze: Einfach mehr Rohspannung reicht nicht zwingend aus, um das Feld in Randdominanz zu bringen. Fuer einen haerteren Test braucht es nicht nur lautere Welt, sondern stoerende Struktur:

- Sinnesachsen bewusst gegeneinander verschieben,
- Rezeptoradaptation testweise schwacher stellen,
- abrupte Phasenbrueche mit widerspruechlicher Form-/Ton-/Feldlage erzeugen,
- gleiche Welt mit und ohne Rezeptorschicht vergleichen.

## Schlussfolgerung

Die aktuelle Gegenprobe spricht nicht gegen die MCM-Topologie. Sie zeigt eher, dass MINI_DIO bereits eine robuste Rueckfuehrungs- und Integrationsfaehigkeit besitzt. Randspannung wird nicht einfach eins zu eins uebernommen, sondern vom Feld teilweise geordnet.

Das ist fuer die weitere Forschung zentral: Die MCM wirkt nicht nur als Speicherort von Daten, sondern als selbstordnende Feldorganisation mit Zentrum, Uebergang und Randnaehe.

## Wie es weitergeht

Als naechstes sollte nicht nur eine lautere Randwelt gebaut werden. Die naechste Pruefung sollte eine desynchronisierte Welt sein: Sehen, Hoeren und Feldspannung zeigen dabei nicht dieselbe Richtung. Damit laesst sich testen, ob die Topologie auch unter widerspruechlicher Sinnesaufnahme stabil bleibt oder ob echte Randdominanz entsteht.
