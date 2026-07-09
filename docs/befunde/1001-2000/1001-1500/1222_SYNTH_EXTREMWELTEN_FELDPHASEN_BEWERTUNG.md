# Befund 1222 - Bewertung synthetischer Extremwelten gegen die Feldphasen-Matrix

## Grundfrage

Bricht die Feldphasen-Matrix unter synthetischen Extremwelten, oder bleibt sie als passive MCM-Ordnungsform erhalten?

## Gepruefte Extremwelten

Aus Befund 1221:

- Harmonie
- Rand-Dominanz
- Bruch/Rand
- Bruchfolgen in originaler, permutierter, stark permutierter und zufallsnaher Reihenfolge
- Zeitdehnung kompakt/gedehnt
- Harmonie kompakt/gedehnt
- Rand-Dominanz kompakt/gedehnt

## Befund

Die Feldphasen-Matrix bleibt erhalten.

Auch synthetische Grenzfaelle bilden keine neue dominante Feldphase. Stattdessen verschieben sie:

- Dauer der Zentrumslage,
- Anzahl der offenen Uebergangssegmente,
- Haeufigkeit kurzer Rand/Kipp-Ereignisse,
- Pendelbewegung zwischen Rand und Offenheit.

Der wichtigste Punkt:

```text
Rand/Kipp wird selbst in Rand-Dominanz-Welten nicht zur stabilen Grundphase.
```

Rand/Kipp bleibt kurz:

| Welt | Randsegmente | Rand-Dauer |
|---|---:|---:|
| `RAND_DOMINANZ` | `28` | `30` |
| `RAND_KOMPAKT` | `20` | `23` |
| `RAND_GEDEHNT` | `50` | `51` |
| `BRUCH_RAND` | `7` | `7` |
| `SEQ_STARK_PERMUTIERT` | `9` | `9` |

Die Zentrumslage bleibt dagegen zeitlich stark:

| Welt | Zentrum-Dauer |
|---|---:|
| `HARMONIE` | `5309` |
| `BRUCH_RAND` | `5331` |
| `RAND_DOMINANZ` | `5968` |
| `ZEIT_GEDEHNT` | `11011` |
| `RAND_GEDEHNT` | `11517` |

## Uebergangsstruktur

Ueber die synthetischen Extremwelten:

| Uebergang | Anzahl | Lesart |
|---|---:|---|
| `zentrum_stabil -> offene_variante` | `1281` | Zentrum oeffnet sich unter konstruiertem Weltkontakt |
| `offene_variante -> rekopplungsnaehe` | `1254` | Offenheit sucht Bindung |
| `rekopplungsnaehe -> zentrum_stabil` | `1217` | Rekopplung stabilisiert |
| `offene_variante -> zentrum_stabil` | `1098` | Offenheit findet direkte Ordnung |
| `rekopplungsnaehe -> offene_variante` | `939` | Bindung bleibt beweglich |
| `zentrum_stabil -> rekopplungsnaehe` | `918` | Zentrum bleibt aktiv bindungsnah |
| `spannungsrand_kippnaehe -> offene_variante` | `149` | Rand entlastet in Offenheit |
| `offene_variante -> spannungsrand_kippnaehe` | `30` | Offenheit kippt selten direkt in Rand |

Damit wird die Realwelt-Beobachtung verschaerft:

```text
Rand/Kipp entlastet viel haeufiger in Offenheit,
als Offenheit direkt in Rand/Kipp kippt.
```

## MCM-Lesart

Die synthetischen Extremwelten zeigen:

```text
Zentrum ist kein starres Ruhen.
Zentrum ist eine starke Rueckbindungsphase.

Offenheit ist kein Fehler.
Offenheit ist die zentrale Bewegungsphase.

Rand/Kipp ist kein Dauerzustand.
Rand/Kipp ist ein kurzer Grenzimpuls.
```

Das passt zur MCM-Hypothese eines Feldes, das sich nicht durch harte Regeln stabilisiert, sondern durch innere Phasenbewegung.

## Bedeutung der Zeitdehnung

Zeitdehnung vergroessert vor allem die Dauer der Zentrumslage und der Uebergangsphasen. Sie erzeugt keine neue Feldphase.

Lesart:

```text
Zeitdehnung vertieft Feldphasen,
statt die Topologie zu ersetzen.
```

Das ist relevant fuer die MCM-Feldzeit: Zeit wirkt hier nicht nur als aeussere Abfolge, sondern als Vertiefung von Feldphasen.

## Schlussfolgerung

Die Feldphasen-Matrix ist nach aktuellem Stand robust gegen:

- reale Weltfenster,
- mehrere Assets,
- 5m/1h-Unterschiede,
- 10k-Laeufe,
- Stress/Expansion/Seitwaerts,
- synthetische Harmonie,
- synthetische Rand-Dominanz,
- Bruchfolgen,
- Zeitdehnung.

Das ist ein starker Befund fuer MINI_DIO:

```text
Das MCM-Feld bildet eine stabile passive Phasenordnung.
Diese Ordnung ist nicht auf eine einzelne Weltspur beschraenkt.
```

## Wie es weitergeht

Als naechstes sollte diese Phasenordnung als eigene Mechanikdatei dokumentiert werden: nicht nur als Befund, sondern als aktuelles Arbeitsmodell der MINI_DIO-MCM-Feldbewegung.
