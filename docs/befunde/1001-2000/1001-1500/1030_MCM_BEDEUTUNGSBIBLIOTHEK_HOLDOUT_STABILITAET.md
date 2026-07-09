# 1030 - Stabilitaet der passiven Bedeutungsbibliothek im Holdout

Passive Pruefung, welche Bedeutungsformen aus 1027 in der Holdout-Gruppe 1028/1029 stabil bleiben, sich erweitern oder offen werden.

## Sicherheitsgrenze

- passive Stabilitaetslesung
- keine Handlung
- kein Gate
- keine Strategie
- keine Richtungsvorgabe

## Statusuebersicht

- `stabil_bestaetigt`: `2`
- `bestaetigt_mit_erweiterung`: `1`
- `duenn_bestaetigt_offen`: `1`

## Bedeutungen

| Bedeutung | Form | Status | Bibliothek | Holdout | Typologie-Ueberlappung | Feld-Ueberlappung | Return Delta | Range Delta | Druck Delta | Rekopplung Delta |
|---|---|---|---:|---:|---|---|---:|---:|---:|---:|
| `dio_meaning_fallende_rueckbindung` | `fallende_rueckbindung` | `stabil_bestaetigt` | 11 | 3 | `abverkauf_mit_rekopplung | weite_volatilitaetszone` | `ruhige_rekopplung | starke_rekopplungsbindung` | 2.86313 | -2.934681 | 0.004155 | 0.000409 |
| `dio_meaning_ruhige_rekopplung` | `ruhige_gerichtete_rekopplung` | `stabil_bestaetigt` | 11 | 5 | `gerichtete_bewegung_mit_rekopplung | konsolidierung_mit_rekopplung | weite_volatilitaetszone` | `ruhige_rekopplung | starke_rekopplungsbindung` | 0.136037 | -5.960639 | 0.000363 | -0.000982 |
| `dio_meaning_weite_expansion` | `weite_aufwaerts_expansion` | `bestaetigt_mit_erweiterung` | 10 | 4 | `getragene_expansion | weite_volatilitaetszone` | `mittlere_feldspannung | ruhige_rekopplung | starke_rekopplungsbindung` | -4.119335 | -6.596632 | -0.017591 | 0.002077 |
| `dio_meaning_schmale_transition` | `schmale_offene_transition` | `duenn_bestaetigt_offen` | 9 | 1 | `gerichtete_bewegung_mit_bruch` | `schmale_offene_lage` | 1.034499 | 2.769056 | 0.013944 | 0.005664 |

## Einzeldeutung

### `dio_meaning_fallende_rueckbindung`

- Form: `fallende_rueckbindung`
- Status: `stabil_bestaetigt`
- Bibliothek: `11` Belege, Holdout: `3` Belege
- Typologie-Ueberlappung: `abverkauf_mit_rekopplung | weite_volatilitaetszone`
- Feldqualitaet-Ueberlappung: `ruhige_rekopplung | starke_rekopplungsbindung`
- Deutung: Die Bedeutung kehrt mit gemeinsamer Typologie und gemeinsamer Feldqualitaet wieder.

### `dio_meaning_ruhige_rekopplung`

- Form: `ruhige_gerichtete_rekopplung`
- Status: `stabil_bestaetigt`
- Bibliothek: `11` Belege, Holdout: `5` Belege
- Typologie-Ueberlappung: `gerichtete_bewegung_mit_rekopplung | konsolidierung_mit_rekopplung | weite_volatilitaetszone`
- Feldqualitaet-Ueberlappung: `ruhige_rekopplung | starke_rekopplungsbindung`
- Deutung: Die Bedeutung kehrt mit gemeinsamer Typologie und gemeinsamer Feldqualitaet wieder.

### `dio_meaning_weite_expansion`

- Form: `weite_aufwaerts_expansion`
- Status: `bestaetigt_mit_erweiterung`
- Bibliothek: `10` Belege, Holdout: `4` Belege
- Typologie-Ueberlappung: `getragene_expansion | weite_volatilitaetszone`
- Feldqualitaet-Ueberlappung: `mittlere_feldspannung | ruhige_rekopplung | starke_rekopplungsbindung`
- Deutung: Die Bedeutung kehrt wieder, aber Range, Druck oder Rekopplung verschieben sich sichtbar gegen die Bibliothek.

### `dio_meaning_schmale_transition`

- Form: `schmale_offene_transition`
- Status: `duenn_bestaetigt_offen`
- Bibliothek: `9` Belege, Holdout: `1` Belege
- Typologie-Ueberlappung: `gerichtete_bewegung_mit_bruch`
- Feldqualitaet-Ueberlappung: `schmale_offene_lage`
- Deutung: Die schmale Transition kehrt zurueck, bleibt aber belegtduenn und offen; sie ist Anwesenheit, keine stabile Tiefe.

## Befund

Die passive Bedeutungsbibliothek wird in der Holdout-Gruppe nicht geschlossen kopiert, sondern unterschiedlich getragen:

- stabile Bedeutungen bleiben mit Typologie- und Feldqualitaetsueberlappung lesbar,
- erweiterte Bedeutungen zeigen dieselbe Grundform bei veraenderter Range, Druck- oder Rekopplungsqualitaet,
- offene Bedeutungen bleiben schmal oder belegtduenn und duerfen nicht zu festen Bedeutungen erklaert werden.

## Schluss

Mini-DIOs passive Bedeutungsbibliothek wirkt damit nicht wie eine starre Liste, sondern wie ein offener Bedeutungsraum: wiedererkennbar, aber weltabhaengig dehnbar.

## Wie es weitergeht

Als naechstes sollte eine weitere Holdout-Gruppe mit anderem Asset- oder Zeitprofil gegen dieselbe Bibliothek gelesen werden. Entscheidend ist, ob dieselben Bedeutungen erneut stabil, erweitert oder offen erscheinen.
