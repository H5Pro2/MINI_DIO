# Reale Welten Gegen Synthetische Rezeptorklassen

## Zweck

Diese Diagnose liest reale Welt-Hochlastfenster gegen die synthetischen Rezeptorklassen.
Sie prueft, ob reale Welten eher zentriert, offen oder randnah gelesen werden.

Die Diagnose ist passiv: kein Gate, keine Handlung, keine Runtime-Regel.

## Synthetische Referenz

| Referenz | Max Offen | Max Rand/Kipp | Max Rohfeld | Max Reduktion | Klasse |
|---|---:|---:|---:|---:|---|
| RAND_DOMINANZ | 0.7612 | 0.0288 | 0.1644 | 0.0291 | lokale_rand_oeffnung |
| BRUCH_RAND | 0.5157 | 0.0020 | 0.0938 | 0.0130 | lokale_oeffnung_ohne_rand |
| HARMONIC | 0.0178 | 0.0011 | 0.0278 | 0.0026 | stabile_zentrierung |

## Reale Weltmatrix

| Welt | Klasse | Naechste Synth-Klasse | Zentrum | Offen | Rand | High-Offen | High-Rand | High-Rohfeld | High-Reduktion | High-Lautheit | Rand ueber Synth-Max |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| KAS_2024_5M | reale_starke_rand_oeffnung | RAND_DOMINANZ | 0.3781 | 0.4443 | 0.0201 | 0.8100 | 0.1900 | 0.2940 | 0.0553 | 0.5157 | 0.1613 |
| PAXG_2025_5M | reale_oeffnung_mit_randanteil | RAND_DOMINANZ | 0.6709 | 0.2116 | 0.0108 | 0.8330 | 0.0990 | 0.2890 | 0.0532 | 0.5020 | 0.0703 |
| DOGE_2025_5M | reale_starke_rand_oeffnung | RAND_DOMINANZ | 0.6061 | 0.2615 | 0.0162 | 0.8260 | 0.1510 | 0.2937 | 0.0547 | 0.5139 | 0.1222 |
| XRP_2025_5M | reale_oeffnung_mit_randanteil | RAND_DOMINANZ | 0.6164 | 0.2562 | 0.0161 | 0.8410 | 0.1450 | 0.2976 | 0.0557 | 0.5204 | 0.1163 |

## Befund

- Staerkstes reales Hochlast-Randfenster: `KAS_2024_5M` mit `0.1900`.
- Staerkste reale Hochlast-Oeffnung: `XRP_2025_5M` mit `0.8410`.
- Staerkste reale Gesamtzentrierung in dieser Gruppe: `PAXG_2025_5M` mit `0.6709`.
- Staerkste synthetische Randreferenz: `RAND_DOMINANZ` mit `0.0288`.
- Staerkste synthetische Oeffnungsreferenz: `RAND_DOMINANZ` mit `0.7612`.

## Einordnung

Die realen Hochlastfenster sind nicht schwaecher als die synthetischen Klassen. Besonders KAS zeigt deutlich mehr reale Rand/Kipp-Naehe als die bisherige synthetische Randdominanz.

Damit ist die synthetische Randwelt kein Maximalstressmodell. Sie ist ein kontrolliertes Referenzmuster. Reale Welten koennen lokal staerker randnah werden, waehrend das Gesamtfeld trotzdem zentriert oder gemischt bleibt.

Die Rezeptoradaptation wirkt auch hier nicht als Wegloeschen der Wirkung. Sie begrenzt Rohaufnahme, aber laesst Hochlastfenster als offene oder randnahe Innenfeldlagen sichtbar.

## Wie es weitergeht

Als naechstes sollte KAS als reale Randreferenz phasenweise isoliert werden. Ziel ist zu verstehen, welche Weltabschnitte die starke reale Randnaehe erzeugen.
