# 1511 - PAXG 2024 Geschwisterrollen Asset-Gegenpruefung

## Zweck

Nach der SOL-2024-Kontrolle wurde eine andere Asset-Welt geprueft:

`data/kontrolliert_paxg_2024_5m_test1_2000_PAXGUSDT.csv`

Der Lauf wurde frisch mit eigener Memory ausgefuehrt:

`debug/1511_real_paxg2024_5m_2000_randrollen_sibling_check`

Ziel war zu klaeren, ob `dio_0l7p` und `dio_14wj` nur SOL-artige Rollen sind oder auch in einer anders skalierten, ruhigeren Asset-Welt wiederkehren.

## Ergebnis

Beide Rollen erscheinen wieder.

| Familie | Count | Stable Share | Reversal Delta | Nachhall Delta | Hoer-Luecke Delta | Rekopplung Delta | Strain Delta |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `dio_0l7p` | 76 | 1.0000 | +0.1096 | +0.1480 | -0.0618 | +0.0258 | -0.0164 |
| `dio_14wj` | 109 | 1.0000 | -0.0111 | +0.3071 | -0.0839 | +0.0367 | -0.0221 |

Die Rohwerte liegen in:

`docs/befunde/1511_PAXG2024_GESCHWISTERROLLEN_REALWELT_PROFIL.csv`

## Deutung

PAXG veraendert die Gewichtung der Geschwisterrollen.

In SOL-2024 war `dio_0l7p` haeufiger als `dio_14wj`.

In PAXG-2024 ist es umgekehrt:

`dio_14wj` wird haeufiger und deutlich nachhallender.

Trotzdem bleibt der Kern erhalten:

- beide Rollen sind stabil
- beide sind rekoppelt
- beide haben niedrige Hoer-Feldluecke
- beide liegen unter dem Laufmittel bei Strain

## Rollenverschiebung

`dio_0l7p` bleibt auch in PAXG mit lokaler Umkehrnaehe verbunden.

`dio_14wj` wirkt in PAXG nicht nur als ruhige Rekopplungsnaehe, sondern als staerkerer Nachhalltraeger innerhalb stabiler Kopplung.

Das ist wichtig:

Die Rolle driftet nicht in Instabilitaet, sondern veraendert ihre Gewichtung.

PAXG scheint `dio_14wj` staerker zu tragen als SOL.

## MCM-Deutung

Damit entsteht eine feinere Lesung:

Eine Feldrolle kann in verschiedenen Welten dieselbe Grundqualitaet behalten, aber andere Dominanz bekommen.

`dio_14wj` bleibt nicht identisch in der Oberflaeche, aber es bleibt als stabile, hoernahe Rekopplungsrolle erkennbar.

Das spricht fuer ein dynamisches Bedeutungsnetz:

- Rolle bleibt lesbar
- Welt veraendert Gewichtung
- Topologie bleibt stabil genug
- Bedeutung ist nicht starr, sondern weltabhaengig moduliert

## Grenze

Auch dieser Befund ist passiv.

Er sagt nicht, dass `dio_14wj` etwas tun soll.

Er zeigt nur, dass MINI_DIO dieselbe Feldrolle in einer anderen Welt mit anderer Intensitaet wiederfindet.

## Wie es weitergeht

Als naechstes sollte eine bewusst lautere oder stressigere Asset-Welt geprueft werden, um zu sehen, ob `dio_14wj` dann stabil bleibt, in Randspannung driftet oder von einer anderen Rolle abgeloest wird.
