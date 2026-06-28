# MCM-Rolennetzwerk: Reproduktionsvergleich

## Zweck

Diese Datei vergleicht die passive Rolennetzwerk-Lesung zwischen frueher und spaeter Weltgruppe.
Sie prueft, ob dieselbe Feldmechanik wiederkehrt, driftet oder neue Zentrumsqualitaet bildet.

## Sicherheitsgrenze

- passive Diagnose
- keine Handlung
- kein Gate
- keine Strategie

## Vergleich

| Zustand | Frueh | Spaet | Delta | Frueh Rekopplung | Spaet Rekopplung | Frueh Strain | Spaet Strain | Lesung |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `netz_driftend_getragen` | 22 | 33 | 11 | 0.024412 | 0.047962 | -0.013821 | 0.006937 | Getragene Drift nimmt zu und wirkt als Folgereifung statt Zerfall. |
| `netz_fragmentiert_belastet` | 28 | 17 | -11 | -0.059659 | -0.061817 | 0.063822 | 0.065432 | Belastete Fragmentierung nimmt in der spaeten Gruppe ab. |
| `netz_rekoppelnd_einzeln` | 17 | 26 | 9 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | Einzelrekopplung nimmt zu; Teile loesen sich aus dichter Verbindung. |
| `netz_offen_verbunden` | 32 | 29 | -3 | -0.044234 | -0.043888 | 0.051729 | 0.048462 | Offene Verbindung bleibt sichtbar, wird aber weniger dominant. |
| `netz_rekoppelnd_verbunden` | 28 | 30 | 2 | 0.041417 | 0.029334 | -0.012833 | -0.016203 | Rekoppelnde Verbindung bleibt ueber beide Gruppen stabil sichtbar. |
| `netz_zentrum_getragen` | 0 | 2 | 2 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | Spaete Gruppe bildet zusaetzliche getragene Zentrumsqualitaet. |
| `netz_zentrum_mit_anschluss` | 8 | 6 | -2 | 0.006569 | 0.023122 | 0.006378 | 0.007736 | Zustand nimmt in der spaeten Gruppe ab. |

## Kernbefund

Die spaete Gruppe erzeugt keine voellig andere Topologie.
Sie verschiebt die Gewichtung innerhalb derselben Feldfamilie:

- weniger `netz_fragmentiert_belastet`
- mehr `netz_driftend_getragen`
- weiterhin stabile `netz_rekoppelnd_verbunden`
- erstmals `netz_zentrum_getragen` als kleine zusaetzliche Zentrumsqualitaet

## Arbeitsableitung

```text
Das Rolennetzwerk reproduziert sich nicht als starre Kopie.
Es bleibt in der Grundtopologie aehnlich, verschiebt aber Last, Drift und Zentrumsnaehe je nach Weltgruppe.
```

## Wie es weitergeht

Als naechstes sollte die spaete Zentrumsqualitaet gegen ihre Rohwelt und Sensorik zurueckgelesen werden.
Wenn sie nicht zufaellig ist, zeigt sie, wann aus Rekopplung eine getragene Mitte wird.