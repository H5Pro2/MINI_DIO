# Synthetische Randdominanz-Zeitdehnung Topologie-Synthese

Stand: 2026-06-22

## Zweck

Diese Synthese prueft den Zeitdehnungseffekt im Haertefall `rand_dominanz`.

Nach `bruch_rand` und `harmonic` ist das die dritte synthetische Grundform:

- hohe Randspannung,
- laute Reizphasen,
- asymmetrischer Bruch,
- ueberreizter Nachhall,
- spaete Rekopplungsversuche.

Die Pruefung ist passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Integriert Zeitdehnung auch starke Randdominanz?
2. Unterpruefung: Bleibt die Topologie stabil oder wird sie randlastig?
3. Unterpruefung: Wird die lauteste Randphase geloescht, gehalten oder rekoppelt?
4. Folgeschritt: Feldzeit als Integrationsachse gegen Reizqualitaet abgrenzen.

## Forschungslaeufe

| Lauf | Welt | Kerzen | Episoden | Unique Syntax | Rekopplung | Carry | Sinneskopplung |
|---|---|---:|---:|---:|---:|---:|---:|
| 729 | Randdominanz kompakt | 3300 | 3294 | 199 | 0.7338 | 0.5758 | 0.8924 |
| 730 | Randdominanz gedehnt | 13200 | 13194 | 262 | 0.7436 | 0.5957 | 0.8964 |

Befund:

- Beide Varianten reproduzieren Top-Syntax und Top-Familien mit `1.0` Ueberlappung.
- Die gedehnte Variante hat mehr Rekopplung, mehr Carry und mehr Sinneskopplung.
- Die eindeutige Syntaxmenge steigt von `199` auf `262`.

Das ist anders als bei `harmonic`: Dort sank die Symbolmenge leicht.
Randdominanz erzeugt unter laengerer Einwirkung also mehr Binnenvarianz, nicht nur ruhigere Verdichtung.

## Globale Topologie

| Welt | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| RAND_ZEIT_KOMPAKT | 3294 | 0.9174 | 0.0808 | 0.0018 | 0.7338 | 0.5758 | 0.8924 |
| RAND_ZEIT_GEDEHNT | 13194 | 0.9276 | 0.0719 | 0.0005 | 0.7436 | 0.5957 | 0.8964 |

Befund:

- Die globale Topologie bleibt zentrumsnah.
- Zeitdehnung erhoeht Zentrum leicht.
- Offene Variante und Rand/Kippnaehe nehmen global ab.
- Trotzdem bleibt die Welt deutlich offener als `harmonic`.

## Rezeptorachsen

| Welt | Zentrum | Offen | Rand/Kipp | Lautheit | Rohfeld | Adaptfeld | Ratio | High-Offen | High-Rand/Kipp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RAND_ZEIT_KOMPAKT | 0.7860 | 0.1509 | 0.0070 | 0.1006 | 0.0614 | 0.0533 | 0.8690 | 0.7879 | 0.0697 |
| RAND_ZEIT_GEDEHNT | 0.8729 | 0.0894 | 0.0039 | 0.0729 | 0.0480 | 0.0418 | 0.8696 | 0.6909 | 0.0386 |

Befund:

- Kompakte Randdominanz erzeugt die staerksten offenen Hochlastfenster.
- Gedehnte Randdominanz reduziert offene und randnahe Hochlast.
- Die Adaptionsratio bleibt nahezu gleich.

Lesart:

```text
Zeitdehnung veraendert nicht nur den Filter.
Sie veraendert, wie das Feld dieselbe Randqualitaet ueber Dauer integriert.
```

## Lokaler Phasenbefund

Die entscheidende Phase ist `laute_randphase`.

| Variante | Zentrum | Offen | Rekopplungsnaehe | Rand/Kipp | Feldinput | Lautheit | Schaerfe |
|---|---:|---:|---:|---:|---:|---:|---:|
| kompakt | 0.0275 | 0.8325 | 0.1025 | 0.0375 | 0.1663 | 0.2816 | 0.5414 |
| gedehnt | 0.1169 | 0.6625 | 0.1925 | 0.0281 | 0.1643 | 0.2772 | 0.5406 |

Befund:

- Die laute Randphase bleibt in beiden Varianten offen dominant.
- Gedehnte Zeit erhoeht Zentrum von `0.0275` auf `0.1169`.
- Gedehnte Zeit erhoeht Rekopplungsnaehe von `0.1025` auf `0.1925`.
- Offenheit sinkt von `0.8325` auf `0.6625`.
- Feldinput, Lautheit und Schaerfe bleiben fast gleich.

Das ist der wichtigste Befund:

```text
Die Randqualitaet wird nicht geloescht.
Sie wird durch Zeitdehnung besser gehalten und teilweise rekoppelt.
```

## Weitere Phasen

`asymmetrischer_bruch`:

- kompakt: Zentrum `0.6143`, Offen `0.2200`, Rekopplungsnaehe `0.1657`
- gedehnt: Zentrum `0.9314`, Offen `0.0271`, Rekopplungsnaehe `0.0414`

`ueberreizter_nachhall`:

- kompakt: Zentrum `0.8743`, Offen `0.0457`, Rekopplungsnaehe `0.0771`
- gedehnt: Zentrum `0.9357`, Offen `0.0293`, Rekopplungsnaehe `0.0343`

`zweiter_randstoss`:

- kompakt: Zentrum `0.8400`, Offen `0.1100`, Rand/Kipp `0.0100`
- gedehnt: Zentrum `0.9892`, Offen `0.0067`, Rand/Kipp `0.0017`

Befund:

- Viele Rand-/Bruchphasen werden durch Dehnung deutlich zentrumsnaeher.
- Nur die `laute_randphase` bleibt stark offen.
- Damit ist die Randqualitaet phasengebunden, nicht globaler Kollaps.

## Vergleich der drei Zeitdehnungswelten

| Grundform | Wirkung der Zeitdehnung |
|---|---|
| `harmonic` | Dehnung macht fast alles zentrumsnaeher; kaum neue offene Varianz. |
| `bruch_rand` | Dehnung integriert `randflackern` teilweise; offene Phase bleibt sichtbar. |
| `rand_dominanz` | Dehnung reduziert Randlast global, aber laute Randphase bleibt offen dominant und erzeugt mehr Binnenvarianz. |

Ableitung:

```text
Zeitdehnung ist keine pauschale Beruhigung.
Zeitdehnung ist eine Integrationsachse.
Was integriert wird, haengt von der Weltform ab.
```

## MCM-Lesart

Der Haertefall spricht gegen eine simple Regel wie:

```text
mehr Zeit = alles wird ruhig
```

Stattdessen zeigt sich:

```text
mehr Feldzeit = mehr Moeglichkeit zur Integration
aber starke Randqualitaet bleibt als Randqualitaet lesbar
```

Das ist fuer MINI_DIO wichtig:

- Das Feld darf Reizqualitaeten nicht wegfiltern.
- Es soll sie aufnehmen, begrenzen, halten und organisieren.
- Zeitliche Tiefe hilft bei Integration, ersetzt aber nicht die Struktur der Welt.

## Bedeutung fuer MINI_DIO

MINI_DIO zeigt in diesem Haertefall drei relevante Eigenschaften:

1. Reproduktion bleibt stabil.
2. Topologie bleibt erhalten.
3. Lokale Randqualitaet bleibt unterscheidbar.

Damit wirkt das Feld nicht wie ein starrer Normalisierer.
Es wirkt eher wie ein Innenfeld, das Weltwirkung begrenzt und trotzdem Bedeutung erhaelt.

## Grenze

Das ist weiterhin synthetische Forschung.

Der Befund ist stark fuer die getesteten Welten, aber noch keine allgemeine MCM-Theorie.
Er zeigt eine robuste Arbeitsrichtung:

```text
Feldzeit als Integrationsqualitaet.
Rezeptoradaptation als Aufnahmegrenze.
Topologie als stabile Innenordnung.
Phasenrolle als lokale Bedeutungsbildung.
```

## Wie es weitergeht

Als naechstes sollte die dreiteilige Zeitdehnungsreihe zusammengefasst werden: `harmonic`, `bruch_rand`, `rand_dominanz`. Ziel: eine klare Forschungsnotiz zur Feldzeit-Mechanik erstellen, bevor weitere Welten dazukommen.
