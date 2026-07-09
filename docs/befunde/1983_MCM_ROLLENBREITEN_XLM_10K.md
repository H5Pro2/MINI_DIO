# 1983 - Rollenbreitenpruefung XLM 10k

## Grundfrage

War die KAS-10k-Beobachtung nur assettypisch, oder koppeln auch andere leise/kleinpreisige Welten eher an vorhandene MCM-Rollen an, bevor sie neue starke Milieus bilden?

## Unterpruefung

Geprueft wurde `FOLLOW_EQ10K_XLM_2024_5M` mit 10.000 Zeilen aus `kontrolliert_xlm_2024_5m_10k_XLMUSDT.csv`.

Ausgangspunkt war der Speicherstand nach der KAS-10k-Pruefung:

```text
memory/preview_depth_role_breadth_equal10k_kas_probe.json
```

Die neue Vergleichsmemory liegt hier:

```text
memory/preview_depth_role_breadth_equal10k_xlm_probe.json
```

## Ergebnis

Die zweite leise Welt bestaetigt die Richtung der KAS-Pruefung.

Vor XLM:

```text
breite_grundrolle: 28
uebergangsrolle:    1
milieurolle:        4
nebenrolle:       107
```

Nach XLM:

```text
breite_grundrolle: 29
uebergangsrolle:    1
milieurolle:        5
nebenrolle:       125
```

XLM erzeugt also keine komplette Neuordnung. Die vorhandenen Grundrollen bleiben stabil und werden weiter verbreitert. Gleichzeitig entstehen neue Nebenrollen, und zwei vorhandene Nebenrollen reifen weiter:

```text
dio_mcm_episode_1b57ksv: nebenrolle -> milieurolle
dio_mcm_episode_0izppf1: nebenrolle -> breite_grundrolle
```

## Staerkste Zunahmen

Die staerksten Zaehlerzunahmen liegen weiterhin bei bereits tragenden Rollen:

```text
dio_mcm_episode_12tgchq  +5591
dio_mcm_episode_1qlxgj7  +2526
dio_mcm_episode_1rj8742   +246
dio_mcm_episode_1b57ksv   +242
dio_mcm_episode_1yxc2ug   +210
```

Besonders wichtig: `dio_mcm_episode_12tgchq` und `dio_mcm_episode_1qlxgj7` wechseln mit XLM zur neuen Top-Welt `FOLLOW_EQ10K_XLM_2024_5M`. Das bedeutet nicht, dass XLM eine neue Feldordnung erzwingt. Es zeigt eher, dass XLM vorhandene Bedeutungsraeume stark anspricht.

## Interpretation

Die aktuelle Lesart:

- Leise/kleinpreisige Welten werden vom Feld nicht als voellig fremder Raum behandelt.
- Neue Weltinformation wird zuerst an vorhandene Grundrollen und Bedeutungsraeume gekoppelt.
- Neue Symbole entstehen, bleiben aber ueberwiegend Nebenrollen.
- Eine neue Milieurolle entsteht erst aus einer bereits vorhandenen Nebenrolle.
- Eine neue Grundrolle entsteht ebenfalls nicht aus dem Nichts, sondern aus einer vorhandenen Nebenrolle.

Damit wirkt die MCM-Ordnung nicht wie eine starre Symboltabelle. Sie wirkt eher wie ein dynamisches Bedeutungsnetz: bestehende Rollen werden breiter, einzelne Nebenrollen reifen, neue Nebenrollen lagern sich an.

## Schlussfolgerung

KAS war kein isolierter Sonderfall. XLM bestaetigt, dass kleinpreisige/leise Welten im aktuellen Modell eher rekoppeln als kollabieren oder das Feld neu aufbauen.

Das ist fuer MINI_DIO relevant, weil es zeigt:

```text
Neue Welt -> vorhandene Rollenbreite -> begrenzte Nebenrollenbildung -> moegliche Reifung
```

Nicht:

```text
Neue Welt -> komplette neue Symbolordnung
```

## Wie es weitergeht

Als naechstes sollte eine dritte leise Welt oder ein bewusst anderer Kleinpreis-Charakter geprueft werden. Ziel ist zu klaeren, ob die neue Milieurolle `dio_mcm_episode_1b57ksv` weiter reift oder KAS-nahe bleibt.
