# Bewertung 1318 - Passive MCM-Bedeutungsstruktur

## Prueffrage

Nach der balancierten Zwischenlagenpruefung war die naechste Frage:

```text
Kann MINI_DIO eine gemeinsame Feldform speichern,
ohne die Assetfaerbung und Weltoberflaeche zu verlieren?
```

## Umsetzung

Neu angelegt:

- `mini_dio/mcm_meaning_structure_memory.py`
- `tools/report_mcm_meaning_structure_memory.py`
- `docs/befunde/1001-2000/1001-1500/1317_MCM_BEDEUTUNGSSTRUKTUR_MEMORY.md`

Die Struktur speichert passiv:

- Feldform
- Assetfaerbung
- dominante Lagefolge
- Rohweltprofil
- mehrskaliges Profil
- Sinnesprofil

## Ergebnis

Aktuell entsteht eine gemeinsame Feldform:

```text
zwischenlage_gemischte_rohwelt
```

Darunter liegen fuenf Assetfaerbungen:

- `btc_offen_suchend_zu_offen_suchend`
- `doge_normale_weltspannung_zu_normale_weltspannung`
- `paxg_ruhig_zentrumsnah_zu_normale_weltspannung`
- `sol_normale_weltspannung_zu_normale_weltspannung`
- `xrp_normale_weltspannung_zu_normale_weltspannung`

## Lesart

Die Bedeutung ist nicht rohdatengleich.

Sie ist feldgleich:

```text
gleiche Feldform:
  zwischenlage_gemischte_rohwelt

unterschiedliche Faerbung:
  BTC offen-suchend
  PAXG zentrumsnah zu normal
  SOL/XRP/DOGE normal zu normal
```

PAXG unterscheidet sich zusaetzlich durch niedrigere Range.

BTC unterscheidet sich durch eine offenere dominante Folge.

SOL, XRP und DOGE liegen naeher beieinander.

## Wichtigster Befund

MINI_DIO kann eine Bedeutung als zusammengesetzte Struktur halten:

```text
Feldform + Weltfaerbung + Folge + Rohprofil + Sinnesprofil
```

Das ist fachlich sauberer als eine einfache Symboltabelle.

Es verhindert zwei Fehler:

- alles als gleich lesen
- alles als komplett getrennt speichern

## Bedeutung fuer das MCM-Feld

Das MCM-Feld zeigt hier eine Form von Bedeutungsverdichtung:

Eine wiederkehrende Feldform bleibt erkennbar, waehrend verschiedene Welten ihre eigene Faerbung behalten.

Das passt zur bisherigen Arbeitshypothese:

```text
MCM-Bedeutung entsteht nicht als starres Label,
sondern als getragene Feldform mit variabler Oberflaeche.
```

## Grenze

Die Bedeutungsstruktur ist passiv.

Sie wird nicht von MINI_DIO benutzt, um zu handeln.

Sie ist eine Forschungs- und Speicherstruktur fuer Innenfeldbedeutung.

Wie es weitergeht: Als naechstes sollte geprueft werden, ob diese Bedeutungsstruktur bei neuen Weltfenstern wiedererkannt, erweitert oder aufgespalten wird.
