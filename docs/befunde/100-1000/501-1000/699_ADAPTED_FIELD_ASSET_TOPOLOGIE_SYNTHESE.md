# Adaptierte Feldkopplung: Asset-Topologie-Synthese

Stand: 2026-06-22

## Zweck

Diese Synthese fasst die Pruefung nach der Umstellung auf adaptierte Feldkopplung zusammen.

Geprueft wurden:

- BTC 2024 5m 2k
- SOL 2024 5m 2k
- KAS 2024 5m 2k
- PAXG 2024 5m 10k
- DOGE 2024 5m 10k
- XRP 2024 5m 10k

Die Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Kernergebnis

Die MCM-Topologie bleibt nach der adaptieren Feldkopplung erhalten.

Das Feld wird nicht flach stabilisiert. Es zeigt weiter:

- zentrumsnahe Stabilisierung,
- offene tragende Varianten,
- kleine Rand-/Kippbereiche,
- Rekopplungsnaehe als Uebergangsqualitaet.

Die Rohaufnahme wird nicht direkt als MCM-Feldspannung verwendet. Das Feld erhaelt die adaptierte Aufnahme. Dadurch wird dauerhafte Rohlast reduziert, ohne die topologische Differenzierung zu verlieren.

## Weltvergleich

PAXG ist im aktuellen Test am staerksten zentriert:

- Zentrum: ca. `0.847`
- Offen: ca. `0.150`
- Rand/Kipp: ca. `0.003`

DOGE und XRP zeigen mehr offene Varianten:

- DOGE Offen: ca. `0.197`
- XRP Offen: ca. `0.196`

BTC, SOL und KAS bleiben gemischter:

- Zentrum liegt grob zwischen `0.754` und `0.793`
- Offen liegt grob zwischen `0.198` und `0.237`
- Rand/Kipp bleibt klein, aber sichtbar.

## Rezeptorbefund

Die Adaptionsratio bleibt ueber die geprueften Welten eng beieinander, grob bei `0.85`.

Das bedeutet:

- verschiedene Assets wirken unterschiedlich,
- Hochlastfenster bleiben sichtbar,
- aber die Rezeptorschicht begrenzt die direkte Felduebertragung.

Damit wirkt die Rezeptoradaptation nicht wie ein harter Filter, sondern wie eine organische Aufnahmegrenze.

## Interpretation

Die bisherige Beobachtung spricht fuer eine robuste Rollen-Topologie:

```text
Zentrum      = stabile Innenfeldwirkung
Offen        = tragende, noch bewegliche Variante
Rand/Kipp    = lokale Spannung und Bruchnaehe
Rekopplung   = Verbindung zwischen Feldwirkung und wieder stabiler Lesbarkeit
```

Wichtig: Das ist keine geometrische Beweisform. Es ist eine reproduzierbare passive Rollenordnung in den aktuell geprueften Welten.

## Abgrenzung

Befunde vor `683_ADAPTIERTE_FELDKOPPLUNG_UMSETZUNG.md` koennen noch Rohaufnahme und MCM-Feldspannung vermischen.

Ab `683` gilt:

```text
Rohaufnahme = Diagnose
adaptierte Aufnahme = MCM-Feldwirkung
```

Damit sind die Befunde ab `683` die fachlich relevante Linie fuer die aktuelle MCM-Rezeptorarchitektur.

## Wie es weitergeht

Als naechstes sollte eine laengere ruhige Welt gegen eine laengere Stress-/Expansionswelt gelegt werden. Ziel ist nicht mehr nur Assetvergleich, sondern die Frage, ob die gleiche Rollenordnung unter Zeitdehnung, Dauerlast und ruhiger Wiederkehr stabil bleibt.
