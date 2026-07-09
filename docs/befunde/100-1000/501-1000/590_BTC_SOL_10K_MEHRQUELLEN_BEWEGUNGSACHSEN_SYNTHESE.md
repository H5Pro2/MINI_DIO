# Mehrquellen-Synthese: BTC/SOL-10k-Feldbewegungsachsen

Stand: 2026-06-21

## Zweck

Diese Synthese verdichtet die vorhandenen BTC- und SOL-10k-Uebergangspaare in einer gemeinsamen MCM-Feldbewegungs-Memory.

Die Auswertung bleibt passiv.
Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Gibt es Bewegungsachsen, die ueber SOL und BTC gemeinsam wiederkehren?
2. Unterpruefung: Bleibt die Achse um `dio_mcm_episode_0e7qvj1` erhalten?
3. Unterpruefung: Sind die Bewegungen rekoppelnd/entlastend oder oeffnend/belastend gerichtet?
4. Folgeschritt: Trennen zwischen allgemeiner MCM-Achse und assetnaher Nachbarschaft.

## Datenbasis

Eingaben:

- `580_CROSS_ANCHOR_2024_10K_PREVIEW_UEBERGANGSPAARE.csv`
- `565_ANCHOR_2025_10K_PREVIEW_UEBERGANGSPAARE.csv`
- `586_CROSS_ANCHOR_BTC_5M_10K_PREVIEW_UEBERGANGSPAARE.csv`

Gesamt:

- Bewegungsachsen: 339

## Feldbewegungsqualitaet

| Qualitaet | Anzahl |
|---|---:|
| `recurrently_opening_strain` | 104 |
| `recurrently_reconnecting` | 95 |
| `young` | 91 |
| `world_specific` | 49 |

## Bewegungswirkung

| Wirkung | Anzahl |
|---|---:|
| `rekoppelnd_entlastend` | 135 |
| `oeffnend_belastend` | 131 |
| `bewegung_offen` | 42 |
| `spannungsnah` | 31 |

## Staerkste Mehrquellen-Achsen

| Bewegung | Ereignisse | Qualitaet | Wirkung | Druckdelta | Rekopplungsdelta | Lautheitsdelta |
|---|---:|---|---|---:|---:|---:|
| `0e7qvj1 -> 1hdpu9s` | 125 | `recurrently_reconnecting` | `rekoppelnd_entlastend` | -0.0181 | +0.0112 | -0.0466 |
| `1hdpu9s -> 0e7qvj1` | 118 | `recurrently_opening_strain` | `oeffnend_belastend` | +0.0629 | -0.0437 | +0.1642 |
| `0mji3u6 -> 0e7qvj1` | 99 | `recurrently_opening_strain` | `oeffnend_belastend` | -0.0010 | +0.0022 | +0.0222 |
| `0z748ck -> 0e7qvj1` | 70 | `recurrently_opening_strain` | `oeffnend_belastend` | +0.0059 | -0.0058 | +0.0102 |
| `0qzjuvj -> 0z748ck` | 69 | `recurrently_opening_strain` | `oeffnend_belastend` | +0.0046 | -0.0015 | +0.0159 |
| `0jbl5pq -> 0qzjuvj` | 66 | `recurrently_reconnecting` | `rekoppelnd_entlastend` | -0.0063 | +0.0044 | -0.0106 |
| `0e7qvj1 -> 1jwnjz4` | 58 | `recurrently_reconnecting` | `rekoppelnd_entlastend` | -0.0277 | +0.0149 | -0.0882 |
| `1jwnjz4 -> 0e7qvj1` | 58 | `recurrently_opening_strain` | `oeffnend_belastend` | +0.0681 | -0.0440 | +0.2108 |
| `0e7qvj1 -> 0mji3u6` | 57 | `recurrently_reconnecting` | `rekoppelnd_entlastend` | -0.0043 | -0.0037 | -0.0609 |

## Arbeitsbefund

Die Mehrquellen-Memory bestaetigt die Achse um `0e7qvj1` als wiederkehrenden MCM-Bewegungsraum.

Besonders klar ist die paarige Asymmetrie:

```text
0e7qvj1 -> 1hdpu9s
  rekoppelnd / entlastend

1hdpu9s -> 0e7qvj1
  oeffnend / belastend
```

Dasselbe Muster erscheint abgeschwaecht auch bei:

```text
0e7qvj1 -> 1jwnjz4
  rekoppelnd / entlastend

1jwnjz4 -> 0e7qvj1
  oeffnend / belastend
```

Damit wirkt `0e7qvj1` nicht als isolierter Punkt, sondern als Bewegungsanker.
Die Bedeutung entsteht nicht nur durch die Insel selbst, sondern durch gerichtete Uebergaenge um diese Insel.

## Deutung

Der Befund spricht fuer eine passive MCM-Feldbewegung:

- vom Anker in bestimmte Nachbarschaften kann Entlastung/Rekopplung entstehen,
- aus bestimmten Nachbarschaften zurueck zum Anker kann Oeffnung/Belastung entstehen,
- dieselbe Grundbewegung kann ueber verschiedene Assets sichtbar bleiben,
- die konkrete Nachbarschaft bleibt welt- und assetabhaengig.

Damit wird die bisherige Lesart geschaerft:

```text
Stabil ist nicht zwingend das Einzelzeichen.
Stabiler wirkt die gerichtete Feldbewegung und ihre Tragart.
```

## Grenze

Das ist kein Beweis fuer eine allgemeine MCM-Topologie.
Es ist ein reproduzierbarer Befund innerhalb der bisher geprueften BTC/SOL-10k-Welten.

Die naechste Pruefung muss zeigen, ob die Achse auch bei laengerer KAS-Welt oder weiteren nicht-SOL/BTC-Welten erhalten bleibt.

## Wie es weitergeht

Als naechstes sollte eine echte dritte Assetklasse mit laengerer Weltlaenge in dieselbe Mehrquellen-Memory aufgenommen werden. Ziel ist zu pruefen, ob `0e7qvj1` als Bewegungsanker allgemein bleibt oder ob BTC/SOL nur eine gemeinsame Nachbarschaft teilen.
