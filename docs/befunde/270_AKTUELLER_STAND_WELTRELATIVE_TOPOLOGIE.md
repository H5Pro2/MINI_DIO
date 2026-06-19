# Aktueller Stand: weltrelative Wahrnehmung und Topologie

Stand: 2026-06-19

## Zweck

Diese Datei haelt den aktuellen MINI_DIO-Forschungsstand nach der Pruefung der weltrelativen Wahrnehmungsaufnahme und der passiven Topologie-Matrix fest.

Sie ist Dokumentation, kein Handlungsmodul.

## Umgesetzter Stand

MINI_DIO besitzt jetzt einen expliziten Forschungsmodus fuer weltrelative Sinnesaufnahme:

```powershell
python -m mini_dio.run_mini --data <welt.csv> --sense-mode world_relative
```

Der Standard bleibt weiterhin `fixed`.

Der Modus `world_relative`:

- baut ein passives Weltprofil aus der jeweiligen Datenwelt,
- liest Sehen, Hoeren und Fuehlen relativ zur Weltspannung,
- verwendet weiche Kompression statt harter absoluter Teiler,
- erzeugt keine Handlung,
- erzeugt kein Gate,
- erzeugt kein Entry-Signal,
- bleibt reine Forschungs- und Diagnoseaufnahme.

## Wichtige Befunde

### 1. Feste Wahrnehmung war weltuebergreifend zu roh

Die Diagnose `262_WELTUEBERGREIFENDE_INFORMATIONSAUFNAHME_DIAGNOSE` zeigte, dass feste Teiler und harte Skalierung verschiedene Welten unterschiedlich stark uebersteuern koennen.

Das betrifft besonders:

- SOL gegen BTC,
- 5m gegen 1h,
- ruhige gegen stressigere Weltfenster.

Damit wurde klar: Nicht nur das MCM-Feld selbst ist wichtig, sondern auch die Qualitaet der Sinnesaufnahme vor dem Feld.

### 2. Der erste relative Adapter war nicht ausreichend

Die erste weltrelative Skalierung verbesserte die Aufnahme nicht.

Der Befund war eindeutig:

```text
Verbesserte Achsen:      0
Verschlechterte Achsen: 13
Weiter auffaellige Achsen: 22
```

Damit war klar: reine Normalisierung reicht nicht.

### 3. Der weiche weltrelative Adapter funktioniert deutlich besser

Die weichere weltrelative Kompression reduzierte die Auffaelligkeiten stark:

```text
Verbesserte Achsen:      22
Verschlechterte Achsen:  0
Weiter auffaellige Achsen: 0
```

Die Mehrweltlaeufe zeigten danach eine deutlich vergleichbarere Innenfeldaufnahme ueber SOL/BTC, 5m/1h und Stresswelten.

### 4. Bruch, Rhythmuswechsel und Kippnaehe bleiben sichtbar

Ein wichtiger Einwand war: Wenn `world_relative` zu stark beruhigt, koennte MINI_DIO echte Weltspannung verlieren.

Die Diagnosen `267` und `268` entlasten diesen Punkt im aktuellen Stand.

In den geprueften Welten wurden rohe Bruchfenster weiterhin sensorisch erfasst.

Kurzbefund:

```text
Bruch erhalten:        4 von 4 frischen SOL/BTC-Laeufen
Bruch abgeschwaecht:   0
Zu stark beruhigt:     0
```

Das bedeutet: Die Aufnahme wird vergleichbarer, ohne bisher Bruchsignale blind glattzuziehen.

### 5. Passive Topologie bleibt unter world_relative sichtbar

Die neue Diagnose `269_WELTRELATIVE_TOPOLOGIE_MATRIX` liest die Topologie nicht ueber feste `dio_*`-Namen.

Sie liest Rollenqualitaet aus:

- Innenfeldwirkung,
- Rekopplung,
- Carry,
- Strain,
- Sinnes-MCM-Kopplung,
- visueller und auditiver Feldnaehe.

In den geprueften SOL/BTC- und 5m/1h-Welten zeigte sich derselbe Rollenzustand:

```text
zentrum_mit_rand_und_uebergang
```

Die sichtbaren Rollen:

```text
Zentrum      = stabile Innenfeldwirkung
Rand/Kipp    = lokale Spannung und Bruchnaehe
Offen        = tragende, aber noch nicht fest gereifte Variante
Rekopplung   = Qualitaet, die Zentrum und Uebergang stabilisiert
```

## Interpretation

Der aktuelle Stand spricht fuer eine stabile passive Rollen-Topologie im MINI_DIO-Feld.

Das ist keine Aussage, dass eine universelle MCM-Geometrie bewiesen ist.

Es ist aber ein belastbarer aktueller Befund:

```text
Wenn die Sinnesaufnahme weltrelativ sauberer wird,
verschwindet die passive Rollenordnung nicht.
Sie bleibt als Zentrum, offene Variante und Rand/Kippnaehe lesbar.
```

Damit wird die Hypothese staerker, dass die beobachtete Ordnung nicht nur ein Artefakt harter Rohdatenteiler war.

## Aktuelle technische Grenze

`world_relative` ist weiterhin Forschungsmodus.

Der Modus sollte erst dann Standard werden, wenn:

- lange ruhige Welten,
- lange Stresswelten,
- Expansionswelten,
- Seitwaerts- und Bruchwelten

gegen dieselbe Matrix geprueft wurden.

## Stand der Topologie

Aktuell sichtbar:

- zentrumsnahe Stabilitaet,
- offene Uebergangsvariante,
- Rand-/Kippnaehe,
- Rekopplung als stabilisierende Qualitaet.

Noch offen:

- ob Stresswelten den Randanteil sichtbar erhoehen,
- ob ruhige Welten das Zentrum zu stark dominieren,
- ob Expansionswelten eine echte neue Mischklasse erzeugen,
- ob die Rollenordnung bei laengeren Welten stabil bleibt.

## Forschungsgrenze

Alle aktuellen Reports bleiben passiv.

Sie duerfen nicht als:

- Handlung,
- Strategie,
- Gate,
- Entry-Signal,
- Zielstruktur,
- Beweis einer universellen Topologie

verwendet werden.

Die richtige Lesart ist:

```text
MINI_DIO bildet unter den aktuell geprueften Bedingungen
eine wiederkehrende passive Rollenordnung im MCM-Feld.
```

## Wie es weitergeht

Als naechstes wird dieselbe Topologie-Matrix auf weitere Weltklassen gelegt:

1. lange ruhige Welt,
2. lange Stresswelt,
3. Expansionswelt,
4. Seitwaerts-/Driftwelt.

Ziel:

- bleibt `zentrum_mit_rand_und_uebergang` stabil?
- nimmt Rand/Kippnaehe bei Stress sichtbar zu?
- entstehen neue Mischklassen?
- bleibt Rekopplung eine zentrale Qualitaet?
- ist `world_relative` robust genug, um spaeter Standardaufnahme zu werden?
