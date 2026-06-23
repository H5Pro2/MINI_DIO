# BTC 2025 Bruch gegen Feldruhe - Synthese

Stand: 2026-06-23

## Zweck

Diese Notiz verdichtet den BTC-2025-Vergleich zwischen:

- einem real belasteten Bruchfenster,
- dem feldruhigsten BTC-Kandidaten.

Ziel ist, zu pruefen, ob MINI_DIO zwischen Bruchdruck und Feldruhe eine unterschiedliche MCM-Innenordnung liest.

## Verglichene Welten

| Welt | Quelle | Start | Ende | Art |
|---|---|---:|---:|---|
| BTC_BRUCH | `kontrolliert_real_sequence_break_btc_2025_5m_2000.csv` | 80500 | 82500 | realer Stress-/Bruchabschnitt |
| BTC_FELDRUHE | `BTC2025_FIELD_QUIET_03` | 52750 | 54750 | feldruhigster Kandidat |

## Passive Forschungskette

Der BTC-Bruchlauf blieb intern reproduzierbar:

```text
Top-Syntax-Ueberlappung:   1.0
Top-Familien-Ueberlappung: 1.0
Unique Syntaxsymbole:      344 -> 344
```

Die Innenfeldklassen im Bruchfenster:

```text
stabil:            1607
tragend_unruhig:    368
kippend:             18
gespannt:             1
```

Gegenueber BTC-Feldruhe steigt damit vor allem:

- offene Variante,
- Rand/Kippnaehe,
- `tragend_unruhig`,
- lokaler Strain.

## Topologievergleich

| Welt | Topologie | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| BTC_BRUCH | stark_zentriert_wenig_rand | 0.8059 | 0.1846 | 0.0095 | 0.6949 | 0.5126 | 0.1542 | 0.8420 |
| BTC_FELDRUHE | stark_zentriert_wenig_rand | 0.8300 | 0.1655 | 0.0045 | 0.6969 | 0.5132 | 0.1514 | 0.8472 |

## Befund

BTC-Bruch ist nicht topologisch kollabiert.

Er wird gelesen als:

```text
weiterhin zentrumsnah,
aber offener,
randnaeher,
strainreicher,
weniger sinnlich gekoppelt.
```

BTC-Feldruhe ist dagegen:

```text
zentrumsnaeher,
randarmer,
leicht rekopplungsstaerker,
strain-aermer.
```

## Fachliche Bedeutung

Der Befund ist wichtig, weil er beide Seiten trennt:

```text
Topologie bleibt robust.
Lokale Rollenanteile reagieren auf Weltspannung.
```

Das passt zur bisherigen MCM-Lesung:

- Das Feld verliert seine Ordnung nicht sofort bei Bruchdruck.
- Bruchdruck erscheint als Veraenderung der Rollenanteile.
- Feldruhe erscheint als staerkere Zentrumslage mit weniger Rand/Kipp.

Damit ist die Topologie nicht starr, aber auch nicht beliebig.

## Grenze

Dieser Befund ist weiterhin passiv.

Er sagt nicht:

```text
BTC_BRUCH = Handlung
BTC_FELDRUHE = keine Handlung
```

Er sagt nur:

```text
MINI_DIO liest unterschiedliche Innenfeldqualitaeten,
ohne dass die globale Topologie zerfaellt.
```

## Schlussfolgerung

Die zweistufige Feldruhe-Methode wird durch BTC weiter gestuetzt.

Zusammen mit SOL 2025 entsteht ein belastbarerer Zwischenstand:

```text
Rohweltliche Ruhe, Bruchdruck und MCM-Feldruhe sind getrennte Ebenen.
MINI_DIO liest daraus eine robuste, aber lokal bewegliche Zentrum-Peripherie-Topologie.
```

## Wie es weitergeht

Als naechstes sollte ein Expansionsfenster statt Bruch/Feldruhe gelesen werden. Ziel: pruefen, ob gerichtete Expansion eine neue Mischklasse erzeugt oder nur Zentrum, Offenheit und Randanteile anders gewichtet.
