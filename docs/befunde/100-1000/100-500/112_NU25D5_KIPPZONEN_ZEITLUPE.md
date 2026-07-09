# 112 - `nu25d5` Kippzonen-Zeitlupe

## Zweck

Diese Datei lokalisiert Kippbereiche von `nu25d5`
in den grossen Jahresdaten.

Ausgangspunkt:

- `111_ROLLENSTABILITAET_UND_UEBERGANGSZONEN.md`

Die Diagnose bleibt passiv.
Sie ist keine Handlung,
kein Gate,
kein Entry-Signal
und keine Strategie.

## Skript

`DIO_MINI/report_passive_nu25d5_kippzonen_zeitlupe.py`

## Eingabe

`debug/dio_mini_passive_topology_year_hardtest_worlds_20260618/`

## Ausgabe

Ordner:

`debug/dio_mini_passive_nu25d5_kippzonen_zeitlupe_20260618/`

Dateien:

- `nu25d5_kippzonen_events.csv`
- `nu25d5_kippzonen_windows.csv`
- `nu25d5_kippzonen_by_world.csv`
- `nu25d5_kippzonen_summary.json`

## Ergebnis

Gepruefte Welten:

- `4`

Kippereignisse:

- Gesamt: `6218`
- `kippvorfeld_randspannung`: `3695`
- `bruecke_zu_randspannung`: `1574`
- `randspannung_zu_bruecke`: `949`

## Weltuebersicht

`1-12_2023_5m_SOLUSDT`

- `nu25d5`-Treffer: `11361`
- Kippereignisse: `1994`
- Kippanteil: `0.175513`
- dominante Qualitaet: `brueckenfaehig`
- Randspannung: `0.206144`
- Brueckenfaehig: `0.462371`

`1-12_2024_5m_SOLUSDT`

- `nu25d5`-Treffer: `12064`
- Kippereignisse: `1832`
- Kippanteil: `0.151857`
- dominante Qualitaet: `brueckenfaehig`
- Randspannung: `0.167938`
- Brueckenfaehig: `0.518153`

`1-12_2025_5m_SOLUSDT`

- `nu25d5`-Treffer: `11777`
- Kippereignisse: `1712`
- Kippanteil: `0.145368`
- dominante Qualitaet: `brueckenfaehig`
- Randspannung: `0.156576`
- Brueckenfaehig: `0.549206`

`1-4_2026_5m_SOLUSDT`

- `nu25d5`-Treffer: `3933`
- Kippereignisse: `680`
- Kippanteil: `0.172896`
- dominante Qualitaet: `brueckenfaehig`
- Randspannung: `0.189677`
- Brueckenfaehig: `0.480803`

## Zeitlupenfenster

Mittelwerte ueber alle Kippfenster:

Vorfeld:

- Carry: `0.388062`
- Strain: `0.190265`
- Rekopplung: `0.667706`
- Randspannung: `0.178093`
- Brueckenfaehig: `0.666428`

Kippbereich:

- Carry: `0.386325`
- Strain: `0.196108`
- Rekopplung: `0.665535`
- Randspannung: `0.184013`
- Brueckenfaehig: `0.625635`

Nachfeld:

- Carry: `0.386363`
- Strain: `0.194597`
- Rekopplung: `0.666056`
- Randspannung: `0.163011`
- Brueckenfaehig: `0.629597`

## MCM-Lesung

`nu25d5` ist im Jahresraum dominant brueckenfaehig.

Die Kippzone ist kein harter Schalter.

Sie wirkt als weiche Feldschwelle:

```text
Vorfeld:
hohe Brueckenfaehigkeit

Kippbereich:
Strain steigt leicht,
Brueckenfaehigkeit faellt leicht,
Randspannung steigt leicht

Nachfeld:
Randspannung faellt wieder,
Brueckenfaehigkeit bleibt tragend
```

Das passt zur bisherigen Lesung:

`nu25d5` ist ein Uebergangsbereich
zwischen Randspannung
und offener entlastender Bruecke.

## Schluss

Der beste aktuelle Befund lautet:

```text
nu25d5_has_soft_transition_threshold
```

Die MCM-Topologie zeigt hier keine mechanische Umschaltung.
Sie zeigt eine weiche Kippzone,
in der Spannung und Brueckenfaehigkeit kurz gegeneinander arbeiten.

Das ist fuer Mini-DIO wichtig:

Uebergangszonen duerfen nicht als Fehler gelesen werden.
Sie sind Feldbereiche,
in denen Bedeutung ihre Rolle veraendert,
ohne ihre Grundkopplung zu verlieren.

## Wie es weitergeht

Grundfrage:

Kann Mini-DIO diese weichen Uebergangszonen
als eigene Innenfeldqualitaet speichern,
ohne daraus Handlung abzuleiten?

Unterpruefung:

Eine passive `uebergangsqualitaet` ableiten:

- stabil
- brueckenfaehig
- randspannungsnah
- weich_kippend

Folgeschritt:

Passive Uebergangsqualitaet in die Mini-DIO-Landkarte aufnehmen.
