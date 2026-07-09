# Befund 2009 - Positive Mixed-Binding-Zielwelt rückgelesen

Stand: 2026-07-09

## Frage

Befund 2006 zeigte eine positive Reifung von drei `mixed_binding`-Kandidaten nach `realworld_bound`.

Befund 2008 zeigte danach, dass diese Reifung nicht durch beliebige ruhige Welten, beliebige PAXG-Fenster oder beliebige Übergangswelten wiederholt wurde.

Diese Rücklesung fragt deshalb enger:

```text
Welche konkrete Zielwelt- und Feldphase hat die Reifung aus Befund 2006 wirklich getroffen?
```

## Vorgehen

Ausgewertet wurden die Debugläufe der vier Zielwelten aus Befund 2006:

```text
debug/2005_mb_targeted_paxg_real2024
debug/2005_mb_targeted_btc_quiet2025
debug/2005_mb_targeted_doge_transition2024
debug/2005_mb_targeted_btc_follow6000_7000
```

Ziel-Symbole:

```text
dio_mcm_episode_05w9z7v
dio_mcm_episode_08g2xgt
dio_mcm_episode_0zkoaz0
dio_mcm_episode_15jz0fg
dio_mcm_episode_1i07qau
```

Detaildaten:

```text
docs/befunde/2001-3000/2009_MIXED_BINDING_POSITIVE_ZIELWELT_RAW_PHASE.csv
```

## Ergebnis

Alle Treffer der fünf Referenzrollen lagen ausschließlich in:

```text
MB_TARGET_RUHIG_PAXG_REAL2024
```

Die anderen Zielwelten trafen diese fünf Kandidaten nicht:

```text
MB_TARGET_RUHIG_BTC_QUIET2025
MB_TARGET_UEBERGANG_DOGE2024
MB_TARGET_UEBERGANG_BTC_FOLLOW6000_7000
```

## Messwerte der getroffenen Rollen

| Symbol | Treffer | Lesung | Rekopplung | Carry | Strain | Sensory | Visual Gap | Hearing Gap | Tension |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| `dio_mcm_episode_05w9z7v` | 3 | `ruhig_getragene_nahe` | 0.727959 | 0.583200 | 0.145865 | 0.860085 | 0.209655 | 0.025399 | 0.040075 |
| `dio_mcm_episode_08g2xgt` | 1 | `ruhig_getragene_nahe` | 0.726642 | 0.573542 | 0.138817 | 0.862428 | 0.189358 | 0.006145 | 0.044772 |
| `dio_mcm_episode_0zkoaz0` | 0 | keine erneute Berührung | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| `dio_mcm_episode_15jz0fg` | 3 | `sichtbare_uebergangsnaehe` | 0.725216 | 0.585856 | 0.157740 | 0.849046 | 0.221557 | 0.032115 | 0.058634 |
| `dio_mcm_episode_1i07qau` | 1 | `sichtbare_uebergangsnaehe` | 0.719058 | 0.587298 | 0.168969 | 0.824373 | 0.303702 | 0.037205 | 0.055243 |

## Lesung

Die positive Reifung wurde durch eine sehr spezifische Feldlage getragen:

```text
hohe Rekopplung,
mittleres Carry,
niedrige Strain-Werte,
niedrige Feldspannung,
niedrige Hörlücke,
stabile Wirkung,
hohe sensorische Kopplung.
```

Das ist genauer als die bisherige Kurzform `ruhige rekoppelnde Nähe`.

Die treffendere Beschreibung lautet:

```text
ruhig getragene, stark rekoppelnde PAXG-Feldphase mit niedriger Ton-/Spannungsabweichung
```

## Bedeutung

Die Reifung aus Befund 2006 war nicht einfach assetgebunden und nicht nur ruhig.

Sie entstand dort, wo die Außenwelt eine vorhandene innere Feldrolle mit passender Rekopplungsqualität erneut berührt hat.

Damit wird die Hypothese präziser:

```text
Mixed Binding reift nicht durch neue Weltmenge.
Mixed Binding reift durch passende Feldnähe.
```

## Grenze

Die Trefferzahl bleibt klein. Drei Symbole reiften klar, zwei blieben schwach oder ungetroffen.

Der Befund zeigt daher keinen allgemeinen Mechanismus, sondern eine konkrete positive Rücklesung einer vorher beobachteten Reifung.

## Wie es weitergeht

Als nächstes sollte aus dieser Messung eine gezielte Suchsignatur gebaut werden:

```text
hohe Rekopplung
niedrige Spannung
niedrige Hörlücke
stabile Wirkung
ausreichende sensorische Kopplung
```

Dann kann MINI_DIO in weiteren Welten nach ähnlichen Feldphasen suchen, ohne grob nach Assetnamen oder allgemeinen Weltklassen zu suchen.
