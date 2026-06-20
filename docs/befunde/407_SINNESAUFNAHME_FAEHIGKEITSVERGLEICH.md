# 407 - Sinnesaufnahme Faehigkeitsvergleich

## Fragestellung

Nach `hoeren_hin` wird dieselbe passive Lesart auf alle lokalen Aufnahmeachsen gelegt. Geprueft wird, welche Achse ruhig rekoppelt, welche visuell tragend wirkt und welche mehr Kontaktlast in das Feld bringt.

Wichtig: Das ist Diagnose der Aufnahmequalitaet. Es ist keine Handlung, kein Gate und keine Steuerregel.

## Achsenmittel

| Achse | Balance | Rekopplung | Strain | Feldinput | Stable | Lesart |
|---|---:|---:|---:|---:|---:|---|
| hoeren_hin | 0.5648 | 0.7153 | 0.1348 | 0.0627 | 0.9839 | ruhige_akustische_rekopplung |
| sehen_fokus | 0.5386 | 0.7071 | 0.1422 | 0.1055 | 0.9858 | visuelle_formtragfaehigkeit |
| sehen_abstand | 0.4776 | 0.6808 | 0.1727 | 0.1220 | 0.5550 | visueller_abstand |
| hoeren_leise | 0.4493 | 0.6779 | 0.1809 | 0.1908 | 0.7422 | akustische_daempfungsnaehe |
| ausgeglichen | 0.5243 | 0.7087 | 0.1551 | 0.1174 | 0.9536 | ausgeglichene_aufnahme |
| feldinput | 0.3821 | 0.6543 | 0.2084 | 0.2550 | 0.5693 | direkter_feldkontakt_last |
| fuehlen_abstand | 0.3319 | 0.6268 | 0.2339 | 0.2438 | 0.1303 | kontaktabstand_unruhe |

## Top-3 je Welt

| Welt | Rang | Achse | Qualitaet | Balance | Strain | Feldinput | Stable |
|---|---:|---|---|---:|---:|---:|---:|
| BTC_2025_1H_2000 | 1 | hoeren_hin | ruhig_tragend | 0.5693 | 0.1341 | 0.0606 | 0.9924 |
| BTC_2025_1H_2000 | 2 | sehen_fokus | ruhig_tragend | 0.5465 | 0.1396 | 0.0969 | 0.9751 |
| BTC_2025_1H_2000 | 3 | ausgeglichen | tragend | 0.5321 | 0.1525 | 0.1140 | 0.9545 |
| KAS_2024_1H_2000 | 1 | hoeren_hin | ruhig_tragend | 0.5632 | 0.1354 | 0.0635 | 0.9779 |
| KAS_2024_1H_2000 | 2 | sehen_fokus | tragend | 0.5378 | 0.1425 | 0.1059 | 0.9874 |
| KAS_2024_1H_2000 | 3 | ausgeglichen | tragend | 0.5217 | 0.1567 | 0.1186 | 0.9416 |
| KAS_2024_5M_2000 | 1 | hoeren_hin | ruhig_tragend | 0.5645 | 0.1346 | 0.0623 | 0.9804 |
| KAS_2024_5M_2000 | 2 | sehen_fokus | tragend | 0.5360 | 0.1433 | 0.1092 | 0.9959 |
| KAS_2024_5M_2000 | 3 | ausgeglichen | tragend | 0.5201 | 0.1559 | 0.1186 | 0.9630 |
| SOL_2025_5M_2000 | 1 | hoeren_hin | ruhig_tragend | 0.5622 | 0.1351 | 0.0645 | 0.9845 |
| SOL_2025_5M_2000 | 2 | sehen_fokus | tragend | 0.5339 | 0.1434 | 0.1103 | 0.9843 |
| SOL_2025_5M_2000 | 3 | ausgeglichen | tragend | 0.5208 | 0.1558 | 0.1194 | 0.9573 |

## Interpretation

`hoeren_hin` bleibt die klarste ruhige Rekopplungsfaehigkeit. `sehen_fokus` bleibt ebenfalls tragend, aber naeher an Formspannung. `feldinput` ist nicht falsch; er ist der direkte Kontaktlast-Traeger. Dadurch wird sichtbar: Aufnahmequalitaet ist nicht ein globaler Wert, sondern eine lokale Auswahl der Wahrnehmungsart.

Fachlich bedeutet das: MINI_DIO braucht keine Regel wie 'immer hinhoren'. Der Organismus braucht die Faehigkeit, die Art der Aufnahme zu unterscheiden: akustisch ruhig rekoppeln, visuell Form halten oder Feldkontakt als Druck wahrnehmen.

## Mechanische Grenze

Diese Schicht bleibt vor dem MCM-Feld:

```text
Sehen / Hoeren / Feldkontakt
  -> rezeptorische Aufnahmequalitaet
  -> MCM-Feldwirkung
```

Das Feld wird nicht umgebaut. Es liest, was die Aufnahmeart mit ihm macht.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob MINI_DIO diese Aufnahmequalitaeten episodisch wiedererkennt: gleiche Weltlage, gleiche Aufnahmeart, aehnliche Feldwirkung. Das waere der Uebergang von Diagnose zu passiver Lernspur.
