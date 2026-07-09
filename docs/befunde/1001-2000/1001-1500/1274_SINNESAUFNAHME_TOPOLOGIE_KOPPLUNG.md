# Sinnesaufnahme gegen Topologie

Passive Kopplungspruefung: Welche Hoer-/Seh-/Fuehl-Konstellationen begleiten welche Feldrollen?

Quelle sind Feldphasen-Segmentdateien. Es wird keine Handlung, kein Gate und keine Richtung abgeleitet.

## Rollenmatrix

| Quelle | Rolle | Segmente | Dauer | Lautheit | Sicht | Rohfeld | Rekopplung | Strain | Signatur |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| REAL_1H_RECEPTOR | offene_variante | 2744 | 5380 | 0.2909 | 0.6120 | 0.1706 | 0.6703 | 0.1750 | laut_unscharf_feldmittel_offen |
| REAL_1H_RECEPTOR | rekopplungsnaehe | 1768 | 2132 | 0.1777 | 0.6625 | 0.1070 | 0.7055 | 0.1433 | mittelton_mittelsicht_feldmittel_getragen |
| REAL_1H_RECEPTOR | spannungsrand_kippnaehe | 313 | 334 | 0.6853 | 0.5548 | 0.3911 | 0.5883 | 0.2769 | laut_unscharf_feldstark_angespannt |
| REAL_1H_RECEPTOR | zentrum_stabil | 2851 | 8130 | 0.1487 | 0.6790 | 0.0905 | 0.7217 | 0.1391 | leise_scharf_feldduenn_getragen |
| REAL_5M_RECEPTOR | offene_variante | 2912 | 5672 | 0.2864 | 0.6146 | 0.1688 | 0.6713 | 0.1737 | laut_unscharf_feldmittel_offen |
| REAL_5M_RECEPTOR | rekopplungsnaehe | 1866 | 2222 | 0.1795 | 0.6644 | 0.1084 | 0.7055 | 0.1430 | mittelton_mittelsicht_feldmittel_getragen |
| REAL_5M_RECEPTOR | spannungsrand_kippnaehe | 258 | 281 | 0.6757 | 0.5587 | 0.3877 | 0.5853 | 0.2796 | laut_unscharf_feldstark_angespannt |
| REAL_5M_RECEPTOR | zentrum_stabil | 2978 | 7801 | 0.1493 | 0.6858 | 0.0908 | 0.7214 | 0.1382 | leise_scharf_feldduenn_getragen |
| SYNTH_SENSORY_AXES | offene_variante | 693 | 1385 | 0.3359 | 0.6289 | 0.1947 | 0.6724 | 0.1832 | laut_mittelsicht_feldstark_offen |
| SYNTH_SENSORY_AXES | rekopplungsnaehe | 592 | 720 | 0.1734 | 0.6636 | 0.1074 | 0.7059 | 0.1493 | mittelton_mittelsicht_feldmittel_getragen |
| SYNTH_SENSORY_AXES | spannungsrand_kippnaehe | 391 | 395 | 0.8213 | 0.7311 | 0.4860 | 0.6179 | 0.2828 | laut_scharf_feldstark_angespannt |
| SYNTH_SENSORY_AXES | zentrum_stabil | 1057 | 28776 | 0.0374 | 0.8284 | 0.0283 | 0.7566 | 0.1218 | leise_scharf_feldduenn_getragen |

## Rollenlesung

### offene_variante

- Staerkster Feldkontakt: `SYNTH_SENSORY_AXES` mit `0.1947`.
- Staerkste Rekopplung: `SYNTH_SENSORY_AXES` mit `0.6724`.
- Schaerfste Sicht: `SYNTH_SENSORY_AXES` mit `0.6289`.
- Lauteste Aufnahme: `SYNTH_SENSORY_AXES` mit `0.3359`.

### rekopplungsnaehe

- Staerkster Feldkontakt: `REAL_5M_RECEPTOR` mit `0.1084`.
- Staerkste Rekopplung: `SYNTH_SENSORY_AXES` mit `0.7059`.
- Schaerfste Sicht: `REAL_5M_RECEPTOR` mit `0.6644`.
- Lauteste Aufnahme: `REAL_5M_RECEPTOR` mit `0.1795`.

### spannungsrand_kippnaehe

- Staerkster Feldkontakt: `SYNTH_SENSORY_AXES` mit `0.4860`.
- Staerkste Rekopplung: `SYNTH_SENSORY_AXES` mit `0.6179`.
- Schaerfste Sicht: `SYNTH_SENSORY_AXES` mit `0.7311`.
- Lauteste Aufnahme: `SYNTH_SENSORY_AXES` mit `0.8213`.

### zentrum_stabil

- Staerkster Feldkontakt: `REAL_5M_RECEPTOR` mit `0.0908`.
- Staerkste Rekopplung: `SYNTH_SENSORY_AXES` mit `0.7566`.
- Schaerfste Sicht: `SYNTH_SENSORY_AXES` mit `0.8284`.
- Lauteste Aufnahme: `REAL_5M_RECEPTOR` mit `0.1493`.

## Befund

Die Feldrollen tragen unterschiedliche Sinnesprofile. Damit ist die Topologie nicht nur eine abstrakte Rolle, sondern mit Aufnahmequalitaet gekoppelt.

Zentrum und Rekopplungsnaehe muessen nicht maximal laut sein. Sie entstehen eher dort, wo Feldkontakt, Sicht und Rekopplung zusammen tragbar bleiben.

Rand/Kipp entsteht nicht nur aus Lautheit. Entscheidend ist die Kombination aus Feldaufnahme, Strain und schwacherer Tragfaehigkeit.

## Bewertung

Die Sinnesregulation ist dadurch fachlich enger gefasst: Sie muss nicht das MCM-Feld selbst steuern, sondern die Aufnahmequalitaet vor dem Feld lesbar machen.

Das passt zur aktuellen Trennung:

```text
Sehen / Hoeren / Fuehlen -> Rezeptorschicht -> MCM-Feldtopologie
```

Wie es weitergeht: Als naechstes sollte eine episodische Sinnesaufnahme-Memory entstehen: Welche Sinnes-Signatur fuehrte spaeter zu Zentrum, Bruecke, Rand oder Drift?
