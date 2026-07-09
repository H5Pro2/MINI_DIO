# Synthetische Phasenrollen - Innenfeldableitung

Stand: 2026-06-22

## Zweck

Diese Synthese liest synthetische Weltphasen gegen die entstehende MCM-Innenfeldrolle.

Die Phasen sind nur Auswertungshilfe. Sie greifen nicht in MINI_DIO ein und sind keine Runtime-Regel.

## Hierarchie

1. Grundfrage: Löst eine synthetisch gesetzte Weltphase eine unterscheidbare Innenfeldrolle aus?
2. Unterprüfung: Bleibt Harmonie überwiegend zentrumsnah?
3. Unterprüfung: Wird Bruch/Rand als offene Variante, Rekopplungsnähe oder Spannungsrand sichtbar?
4. Folgeschritt: Die Phasenlesung für weitere synthetische Welten nutzen, um Innenfeldantworten gezielt zu prüfen.

## Harmonische Welt

Die harmonische Kontrollwelt bleibt in allen Phasen stark zentrumsnah.

| Phase | Zentrum | Offen | Rand/Kipp | Rekopplung | Feldinput |
|---|---:|---:|---:|---:|---:|
| ruhig | 0.9911 | 0.0022 | 0.0011 | 0.7598 | 0.0144 |
| expansion | 0.9889 | 0.0078 | 0.0000 | 0.7562 | 0.0212 |
| unruhe | 0.9800 | 0.0111 | 0.0000 | 0.7549 | 0.0207 |
| kippnaehe | 0.9589 | 0.0167 | 0.0011 | 0.7508 | 0.0278 |
| rekopplung | 0.9933 | 0.0033 | 0.0011 | 0.7582 | 0.0197 |
| ruhe_rueckkehr | 0.9966 | 0.0022 | 0.0000 | 0.7608 | 0.0148 |

Lesart:

```text
Die harmonische Welt erzeugt leichte Phasenfärbung,
aber keine starke Rollenverschiebung.
```

## Bruch-/Randwelt

Die Bruch-/Randwelt erzeugt eine klare phasengebundene Innenfeldverschiebung.

| Phase | Zentrum | Offen | Rand/Kipp | Rekopplung | Feldinput | Lautheit | Schärfe |
|---|---:|---:|---:|---:|---:|---:|---:|
| ruhig_vorlast | 0.9843 | 0.0057 | 0.0014 | 0.7586 | 0.0173 | 0.0227 | 0.8387 |
| oeffnung | 0.9757 | 0.0114 | 0.0014 | 0.7558 | 0.0221 | 0.0287 | 0.8337 |
| bruch_impuls | 0.8829 | 0.0543 | 0.0000 | 0.7374 | 0.0478 | 0.0684 | 0.8077 |
| randflackern | 0.2871 | 0.4971 | 0.0043 | 0.6953 | 0.0938 | 0.1454 | 0.6242 |
| gegenpol | 0.9729 | 0.0100 | 0.0014 | 0.7474 | 0.0368 | 0.0510 | 0.8210 |
| rekopplung | 0.9914 | 0.0057 | 0.0014 | 0.7579 | 0.0212 | 0.0279 | 0.8355 |
| ruhe_nachhall | 0.9929 | 0.0029 | 0.0014 | 0.7596 | 0.0187 | 0.0252 | 0.8375 |
| zweiter_kippimpuls | 0.9800 | 0.0060 | 0.0040 | 0.7423 | 0.0538 | 0.0825 | 0.8027 |
| zweite_rekopplung | 0.9865 | 0.0051 | 0.0000 | 0.7575 | 0.0225 | 0.0315 | 0.8349 |

## Kernbefund

Die Phase `randflackern` ist der stärkste Gegenbefund zur reinen Zentrumslage:

```text
Zentrum fällt auf 0.2871.
Offene Variante steigt auf 0.4971.
Rekopplung fällt auf 0.6953.
Feldinput steigt auf 0.0938.
Lautheit steigt auf 0.1454.
Schärfe fällt auf 0.6242.
```

Danach kehrt das Feld in `gegenpol`, `rekopplung` und `ruhe_nachhall` wieder deutlich in Richtung Zentrum zurück.

Das ist der entscheidende Punkt:

```text
MINI_DIO liest die synthetische Bruchphase nicht nur als mehr Rauschen.
Die Innenfeldrolle verschiebt sich phasengebunden und rekoppelt danach wieder.
```

## Arbeitslesart

Die Bruch-/Randwelt erzeugt keine globale Topologieauflösung.

Sie erzeugt eine lokale Rollenverschiebung:

```text
ruhig_vorlast       = zentrumsnah
oeffnung            = leicht offener
bruch_impuls        = deutlich geöffnet
randflackern        = offene Variante dominiert
gegenpol            = Rückkehr zur Zentrumslage
rekopplung          = erneute Stabilisierung
ruhe_nachhall       = Nachhall bleibt zentrumsnah
zweiter_kippimpuls  = kurze Kippnähe ohne Kollaps
zweite_rekopplung   = Rückbindung
```

Damit wird die MCM-Feldantwort zeitlich und phasisch lesbar:

```text
Weltphase -> Rezeptoraufnahme -> MCM-Feldwirkung -> Innenfeldrolle
```

## Grenze

Die Phase erzeugt vor allem offene Variante, nicht stark dominanten Spannungsrand.

Das kann bedeuten:

- Die Rezeptorschicht schützt das Feld vor Randüberlastung.
- Die synthetische Randphase ist eher offene Instabilität als echter Feldkollaps.
- MINI_DIO liest Kippnähe bisher stärker als Öffnung/Rekopplungsnähe denn als Randdominanz.

Diese drei Möglichkeiten müssen später getrennt geprüft werden.

## Wie es weitergeht

Als nächstes sollte eine noch gezieltere synthetische Welt gebaut werden, die nicht nur `randflackern`, sondern echte Randdominanz provoziert. Ziel ist zu prüfen, ob das Feld einen klaren Spannungsrand ausbilden kann oder ob die Rezeptorschicht ihn konsequent in offene Variante und Rekopplungsnähe umwandelt.
