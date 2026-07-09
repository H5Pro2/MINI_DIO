# 1984 - Rollenbreitenpruefung TRX 10k

## Grundfrage

Reifen leise/kleinpreisige Welten in vorhandene MCM-Rollen hinein, oder erzwingen sie nach KAS und XLM eine neue starke Feldordnung?

## Unterpruefung

Geprueft wurde `FOLLOW_EQ10K_TRX_2024_5M` mit 10.000 Zeilen aus:

```text
data/kontrolliert_trx_2024_5m_10k_TRXUSDT.csv
```

Ausgangspunkt war der Speicherstand nach der XLM-10k-Pruefung:

```text
memory/preview_depth_role_breadth_equal10k_xlm_probe.json
```

Der neue Speicherstand liegt hier:

```text
memory/preview_depth_role_breadth_equal10k_trx_probe.json
```

## Ergebnis

TRX bestaetigt die Richtung aus KAS und XLM.

Vor TRX:

```text
breite_grundrolle: 29
uebergangsrolle:    1
milieurolle:        5
nebenrolle:       125
```

Nach TRX:

```text
breite_grundrolle: 31
uebergangsrolle:    1
milieurolle:        5
nebenrolle:       143
```

Es entstehen also keine neuen Milieurollen. Stattdessen reifen zwei Nebenrollen zu breiten Grundrollen:

```text
dio_mcm_episode_1qv5i56: nebenrolle -> breite_grundrolle
dio_mcm_episode_0n6m7si: nebenrolle -> breite_grundrolle
```

Die zuvor aus KAS gereifte Milieurolle bleibt Milieurolle:

```text
dio_mcm_episode_1b57ksv: milieurolle -> milieurolle
```

## Staerkste Zunahmen

Die groessten Zunahmen liegen weiterhin bei bereits tragenden Rollen:

```text
dio_mcm_episode_12tgchq  +4805
dio_mcm_episode_1qlxgj7  +2285
dio_mcm_episode_0icnf2v   +636
dio_mcm_episode_0iwh9d2   +551
dio_mcm_episode_1yxc2ug   +177
```

Einige bestehende Grundrollen wechseln mit TRX ihre Top-Welt zu `FOLLOW_EQ10K_TRX_2024_5M`, ohne ihre Rolle zu verlieren:

```text
dio_mcm_episode_1eav7xq
dio_mcm_episode_0bsaqu1
dio_mcm_episode_14sn1ov
dio_mcm_episode_08g1nk4
dio_mcm_episode_05upp98
dio_mcm_episode_14pd6eb
```

## Interpretation

Die dritte leise Welt erweitert das Feld nicht chaotisch. Sie wirkt wie eine weitere Rekopplungswelt:

- vorhandene Grundrollen werden breiter,
- Nebenrollen entstehen weiter,
- einzelne Nebenrollen reifen in Grundrollen,
- die bestehende Milieurolle bleibt erhalten,
- keine neue starke Milieuordnung wird erzwungen.

Damit wirkt die Rollenbildung stabiler als eine einfache Asset-Spezialitaet. KAS, XLM und TRX unterscheiden sich in Rohpreis, Bewegung und Lautheit, koppeln aber dennoch an eine vergleichbare Feldordnung an.

## Schlussfolgerung

Die leisen/kleinpreisigen Welten zeigen bisher keine neue dominante Topologie. Sie verbreitern bestehende Rollen und lassen einzelne Nebenrollen reifen.

Das spricht fuer folgende Lesart:

```text
Neue leise Welt -> Rekopplung an vorhandene Rollen -> Nebenrollenbildung -> punktuelle Reifung
```

Nicht:

```text
Neue leise Welt -> Zerfall der Topologie
Neue leise Welt -> komplette neue Hauptordnung
```
