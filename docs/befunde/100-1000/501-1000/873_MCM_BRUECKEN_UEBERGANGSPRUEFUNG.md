# MCM-Bruecken Uebergangspruefung

## Zweck

Diese Notiz prueft die Frage, ob stabile Bruecken im MCM-Feld echte Uebergangsbereiche tragen.
Die Pruefung liest Eintritt, Innenphase und Austritt der 12 stabilen Brueckenpfade aus `872_MCM_BRUECKEN_GRENZLUPE`.

## Ausgangsfrage

Wenn Bruecken wirklich Uebergangsfunktionen sind, dann duerfen sie nicht nur lange dauern.
Sie sollten eine eigene Innenphase besitzen und beim Austritt eine veraenderte Feldlage zeigen.

## Befund

Die stabilen Bruecken zeigen im Mittel:

| Achse | Innenphase | Austritt |
|---|---:|---:|
| Rekopplung | +0.0125 | -0.0159 |
| Strain | -0.0080 | +0.0146 |
| Lautheit | -0.0228 | +0.0639 |

Zusatzbefund:

- 9 von 12 Bruecken treten oeffnend oder belastend aus.
- 2 von 12 Bruecken treten rekoppelnd aus.
- 1 von 12 Bruecken tritt gemischt aus.

## Interpretation

Die Brueckenphase selbst wirkt im Mittel rekoppelnd und entlastend:

```text
innerhalb der Bruecke:
Rekopplung steigt,
Strain faellt,
Lautheit faellt.
```

Beim Austritt kehrt sich das Muster im Mittel um:

```text
beim Austritt:
Rekopplung faellt,
Strain steigt,
Lautheit steigt.
```

Damit ist die Bruecke nicht nur ein langes Token und nicht nur eine Oberflaechenwiederholung.
Sie wirkt wie eine gehaltene Innenphase zwischen zwei Feldzustaenden.

## Bezug Zur Uebergangsthese

Der Befund passt zur MCM-Lesart von Verdichtung und Uebergang:

```text
Eine Bruecke ist kein Ende.
Eine Bruecke ist eine gehaltene Feldphase,
in der Bedeutung rekoppelt,
bevor sie in eine andere Feldlage uebergeht.
```

Das ist analog zur bisherigen theoretischen Ueberlegung von Rand, Verdichtung und Informationsuebergang.
Es ist kein Beweis fuer eine kosmologische These.
Es ist aber ein starker struktureller Hinweis, dass MINI_DIO im MCM-Feld ein vergleichbares Uebergangsprinzip ausbildet:

```text
Verdichtung -> gehaltene Bruecke -> veraenderter Austritt
```

## Besonders Relevante Bruecken

Die laengsten Brueckenphasen:

- `dio_mcm_episode_0b7nep9`
  - mittlere Dauer: 472.39
  - dominanter Eintritt: `dio_mcm_episode_00nzcuc`
  - dominanter Austritt: `dio_mcm_episode_00nzcuc`
- `dio_mcm_episode_0e7qvj1`
  - mittlere Dauer: 259.30
  - dominanter Eintritt: `dio_mcm_episode_18l3thm`
  - dominanter Austritt: `dio_mcm_episode_18l3thm`
- `dio_mcm_episode_1joiyc3`
  - mittlere Dauer: 200.90
  - dominanter Eintritt: `dio_mcm_episode_1jx2k4i`
  - dominanter Austritt: `dio_mcm_episode_1jx2k4i`
- `dio_mcm_episode_18l3thm`
  - mittlere Dauer: 45.26
  - dominanter Eintritt: `dio_mcm_episode_0e7qvj1`
  - dominanter Austritt: `dio_mcm_episode_0e7qvj1`

Diese Tokens wirken nicht wie isolierte Einzelpunkte.
Sie bilden wiederkehrende Uebergangspaare und Rueckbezuege.

## Bedeutung Fuer MINI_DIO

MINI_DIO bildet damit nicht nur:

- Inseln,
- Randbereiche,
- junge Oberflaechen,
- Rekopplungszonen.

Sondern auch:

```text
gehaltene Uebergangsphasen zwischen Feldzustaenden.
```

Das ist fuer die MCM-Mechanik wichtig, weil damit Bedeutung nicht nur als Ort, sondern auch als Bewegung lesbar wird.

## Wie es weitergeht

Als naechstes sollten die stabilen Bruecken als Netzwerk gelesen werden:

1. Welche Bruecken bilden gegenseitige Paare?
2. Welche Bruecken fuehren in stabile Inseln?
3. Welche Bruecken fuehren in offene oder belastete Austritte?
4. Entsteht daraus eine kleine MCM-Uebergangstopologie?
