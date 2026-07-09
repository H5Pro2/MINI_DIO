# Stress, Sideways und Expansion - Topologie-Synthese

Stand: 2026-06-21

## Zweck

Diese Synthese liest den Befund `530_STRESS_SIDEWAYS_EXPANSION_WELTRELATIVE_TOPOLOGIE_MATRIX`.
Geprueft wurde, ob Stress, Seitwaertsphase und Expansion die MCM-Topologie brechen oder nur unterschiedlich faerben.

Die Diagnose bleibt passiv.
Sie erzeugt keine Handlung, kein Gate und keine Richtungsvorgabe.

## Hierarchie

1. Grundfrage: Bleibt die MCM-Topologie unter unterschiedlicher Weltspannung stabil?
2. Unterpruefung: Steigt Rand/Kippnaehe bei Stress und Expansion wirklich systematisch?
3. Folgeschritt: Wenn keine pauschale Randzunahme sichtbar ist, muss Weltspannung differenzierter gelesen werden: Zentrum, Offenheit, Rand, Rekopplung und Wiederholung.

## Kurzbefund

Alle 16 geprueften Laeufe bleiben im Zustand:

```text
zentrum_mit_rand_und_uebergang
```

Damit zerfaellt die Topologie in diesen Gegenwelten nicht.

| Bedingung | Zentrum Mittel | Offen Mittel | Rand/Kipp Mittel | Reproduktion R1/R2 | Lesart |
|---|---:|---:|---:|---|---|
| QUIET2024 | 0.8085 | 0.1596 | 0.0319 | identisch | ruhige Referenz mit sichtbarem Uebergang |
| STRESS2024 | 0.8404 | 0.1064 | 0.0532 | identisch | mehr Rand, aber zugleich staerker zentriert |
| POS_EXP2023 | 0.8249 | 0.1489 | 0.0262 | identisch | Expansion bleibt getragen |
| EXT_EXP2023 | 0.8119 | 0.1479 | 0.0402 | sehr nah | extreme Expansion erhoeht Rand moderat |
| NEG_STRESS2023 | 0.8421 | 0.1278 | 0.0302 | sehr nah | negativer Stress rekoppelt zentrumsnah |
| NEG_STRESS2024 | 0.7958 | 0.1751 | 0.0292 | identisch | negativer Stress wird eher offen als randlastig |
| SIDEWAYS2024 | 0.8164 | 0.1585 | 0.0252 | sehr nah | Seitwaerts bleibt ruhig zentriert |
| SIDEWAYS2026 | 0.8224 | 0.1504 | 0.0272 | sehr nah | Seitwaerts bleibt ruhig zentriert |

## Wichtigster Befund

Stress ist nicht gleich Rand.

Die bisherige einfache Annahme

```text
mehr Stress -> mehr Rand/Kippnaehe
```

ist zu grob.

Die Befunde zeigen differenzierter:

```text
Stress kann Rand erhoehen.
Stress kann aber auch Zentrum verstaerken.
Stress kann offene Variante erzeugen.
Expansion kann getragen bleiben.
Seitwaerts kann zentriert bleiben.
```

Die Reaktion haengt also nicht nur von Weltlautstaerke oder Stresslabel ab.
Sie haengt davon ab, wie die Weltspannung in Rekopplung, Carry, Strain und Sinneskopplung ankommt.

## Reproduzierbarkeit

Die R1/R2-Gegenpruefung ist stark:

- `QUIET2024`, `STRESS2024`, `POS_EXP2023` und `NEG_STRESS2024` reproduzieren die Rollenanteile identisch.
- `EXT_EXP2023`, `NEG_STRESS2023`, `SIDEWAYS2024` und `SIDEWAYS2026` weichen nur minimal ab.

Damit ist die Rollenordnung in dieser Diagnose nicht zufaellig flackernd.
Sie ist innerhalb derselben Welt sehr stabil.

## Fachliche Lesart

Die MCM-Topologie wirkt unter diesen Bedingungen wie eine robuste passive Rollenordnung:

```text
Zentrum bleibt dominant.
Offenheit traegt Uebergang und Variantenbildung.
Rand/Kippnaehe bleibt klein, aber messbar.
Weltspannung faerbt die Anteile, zerstoert sie aber nicht.
```

Das ist fuer MINI_DIO wichtig, weil daraus keine harte Feldregulation folgt.
Die bisher sinnvollere Richtung bleibt:

```text
Aufnahme sauber halten.
Sinnesachsen getrennt lesen.
Feldwirkung passiv verdichten.
Topologische Rollen beobachten.
Keine Stress-Regel erzwingen.
```

## Grenze

Die kurzen `QUIET2024`- und `STRESS2024`-Fenster haben nur 94 Episoden.
Sie sind gut fuer lokale Gegenpruefung, aber nicht stark genug als alleinige Langwelt-Aussage.

Die 994-Episoden-Welten tragen den robusteren Teil dieser Synthese.

## Wie es weitergeht

Als naechstes sollte die gleiche Topologie-Synthese auf laengere Stress- und Expansionswelten gelegt werden.
Ziel ist zu pruefen, ob die starke R1/R2-Reproduktion auch bei groesserer Weltlaenge erhalten bleibt oder ob dort neue offene Bedeutungsraeume entstehen.
